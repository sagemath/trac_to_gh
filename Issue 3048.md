# Issue 3048: add generic LU decomposition

Issue created by migration from https://trac.sagemath.org/ticket/3048

Original creator: mhansen

Original creation time: 2008-04-27 21:40:02

Assignee: was

CC:  rbeezer rishi yzh




---

Attachment


---

Comment by mhansen created at 2008-04-27 21:41:40

Changing status from new to assigned.


---

Comment by mhansen created at 2008-04-27 21:41:40

Changing assignee from was to mhansen.


---

Comment by dmharvey created at 2008-05-01 06:02:19

Couple of comments:

 * in the docstring, I want to *see* the decomposition for at least one example. I want to see three matrices of the right form! Is the permutation non-trivial in that example? Can you give examples that give the code a workout? For example, get the test code to loop over all elements of S4 and construct examples with each permutation.
 * does it work in the boundary cases of 0x0 and 1x1 matrices. These should be in the docstring.
 * the docstring should mention that we are working over the fraction field, so this doesn't make sense for example over a non-domain
 * what is the complexity? in terms of ring operations as a function of the matrix dimension? Is it cubic? (would be nice to verify this empirically for example over some GF)
 * you might want to mention that the algorithm is probably not very numerically stable for non-exact rings (or correct me if I'm wrong about this!)


---

Comment by mhansen created at 2008-05-01 06:08:10

Thanks for the review.  I'll try to get around to these sometime here in the near future.


---

Comment by jason created at 2009-06-04 22:48:57

Another implementation, based on modifying echelon_form (this isn't PLU, just LU, and it still has leftover cruft from the echelon_form function


```
    def _lu_decomposition_in_place_classical(self):
        """
        Return a matrix such that the lower-triangular part of the
        *pivot columns* is L (diagonal of L is assumed to be all
        ones).  U is found by taking the upper-triangular (including
        diagonal) submatrix of pivot columns, then inserting the
        non-pivot columns in the appropriate places.  We should have
        self=L*U.
        
        EXAMPLES::
        
            sage: t = matrix(QQ, 3, range(9)); t
            [0 1 2]
            [3 4 5]
            [6 7 8]
            sage: E = t._echelon_in_place_classical(); t
            [ 1  0 -1]
            [ 0  1  2]
            [ 0  0  0]
        """
        tm = verbose('generic in-place Gauss elimination on %s x %s matrix'%(self._nrows, self._ncols))
        cdef Py_ssize_t start_row, c, r, nr, nc, i
        if self.fetch('in_echelon_form'):
            return

        self.check_mutability()
        cdef Matrix A

        nr = self._nrows
        nc = self._ncols
        A = self
        
        start_row = 0
        pivots = []

        for c from 0 <= c < nc:
            print "checking column ", c
            if PyErr_CheckSignals(): raise KeyboardInterrupt
            for r from start_row <= r < nr:
                print "checking row ", r
                if A.get_unsafe(r, c):
                    #pivots.append(c)
                    #a_inverse = ~A.get_unsafe(r,c)
                    #A.rescale_row(r, a_inverse, c)
                    # We assume that we do not have to do row swaps
                    # (later, we'll implement PLU decomposition)
                    if r != start_row:
                        raise ValueError, "row reduction required row swaps, which is not allowed in generic LU decomposition"
                    #A.swap_rows(r, start_row)
                    for i from start_row < i < nr:
                        if A.get_unsafe(i,c):
                            minus_b = -A.get_unsafe(i, c)*~A.get_unsafe(r,c)
                            #print "replacing row ", i, " with i + ", minus_b, " times row ", start_row, ", starting at column ", c
                            #print self.str()
                                                        
                            A.add_multiple_of_row(i, start_row, minus_b, c)
                            A.set_unsafe(i,c,-minus_b)
                    start_row = start_row + 1
                    break
        #self.cache('pivots', pivots)
        #self.cache('in_echelon_form', True)
        #self.cache('echelon_form', self)
        verbose('done with LU decomposition', tm)
```



---

Comment by jason created at 2009-06-04 23:56:39

Here is another try.  Next step is maybe to compare the speed of Mike's implementation and my reworking of echelon_form.

Then maybe we can change the generic determinant algorithm to use this and be really fast.


```
    def _lu_decomposition_(self):
        """
        Return the PLU decomposition P, L, and U such that self=P*L*U.
        If self is an mxn matrix, then P is an mxm permutation matrix,
        L is a mxm unit lower-triangular matrix, and U is an mxn
        upper-triangular matrix.
        
        The decomposition is done over the fraction field of self.base_ring().
        
        EXAMPLES::
        
        """
        tm = verbose('generic in-place LU decomposition on %s x %s matrix'%(self._nrows, self._ncols))
        cdef Py_ssize_t start_row, c, r, nr, nc, i
        x = self.fetch('PLU')
        if x is not None:
            return x[0].matrix(), x[1], x[2]

        cdef Matrix A, L

        nr = self._nrows
        nc = self._ncols
        R = self.base_ring().fraction_field()
        A = self.change_ring(R).copy()
        L = A.new_matrix(nr, nr)

        one = R(1)
        for r from 0<= r < nr:
            L.set_unsafe(r,r,one)
        
        from sage.groups.all import SymmetricGroup 
        S = SymmetricGroup(nr)
        p = S(1)

        start_row = 0
        pivots = []
        for c from 0 <= c < nc:
            if PyErr_CheckSignals(): raise KeyboardInterrupt
            for r from start_row <= r < nr:
                if A.get_unsafe(r, c):
                    pivots.append(c)
                    if r != start_row:
                        A.swap_rows(r, start_row)
                        p *= S((r+1, start_row+1))
                    a_inverse = ~A.get_unsafe(start_row,c)
                    for i from start_row < i < nr:
                        if A.get_unsafe(i,c):
                            b = A.get_unsafe(i, c)*a_inverse
                            A.add_multiple_of_row(i, start_row, -b, c)
                            L.set_unsafe(i,start_row,b)
                    start_row += 1
                    break
        self.cache('pivots', pivots)
        self.cache('PLU', (p,L,A))
        verbose('done with LU decomposition', tm)            
        return p.matrix(), L, A
```



---

Comment by jason created at 2009-06-04 23:58:02

Also, it would be nice to implement partial pivoting (for this and for generic echelon_form), which would help with the numeric error (and really be easy, in fact).


---

Comment by jason created at 2009-06-05 04:43:18

The new patch is based on the echelon_form function.  It also touches several other computations that should benefit from lu decompositions.


---

Comment by jason created at 2009-06-05 04:43:49

The lu_decomposition patch still needs documentation and timing tests to make sure there are no regressions in the affected functions.


---

Comment by jason created at 2009-06-05 04:47:36

sorry, I accidentally changed the description...


---

Comment by jason created at 2009-06-05 12:13:16

Grr...We need to special-case symbolics because the entire symbolic ring is considered inexact, even though most of the time we are working with symbolics, we are working with exact things.  The lu decomposition of a matrix filled with variables doesn't work now because it assumes that you need partial pivoting.  We need to make sure that if we have variables, we don't use partial pivoting.


---

Comment by jason created at 2009-09-29 05:54:36

Changing assignee from mhansen to jason.


---

Comment by jason created at 2009-09-29 05:54:36

Changing status from assigned to new.


---

Comment by jason created at 2010-04-15 19:04:13

Things to do:

 1. This patch does an insane amount of copying because it actually swaps rows, when it should just keep track of indices without actually doing row swaps
 1. implement scaled partial pivoting
 1. implement complete pivoting


---

Attachment

apply instead of previous patch


---

Comment by jason created at 2010-04-22 03:06:04

posted a work-in-progress patch that is still broken, but a bit closer.  One nice thing is that it uses maxima to get the lu decomposition of a symbolic matrix.
