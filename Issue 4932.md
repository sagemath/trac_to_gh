# Issue 4932: fix solve_left_LU for matrix_double_dense, which was totally broken forever (?)

Issue created by migration from https://trac.sagemath.org/ticket/4932

Original creator: was

Original creation time: 2009-01-03 06:25:33

Assignee: was




---

Comment by jason created at 2009-01-03 08:08:18

Yep, it looks like this might have happened in the transition to numpy and probably was my fault.  Here are errors:


```
sage: A = matrix(RDF, 3,3, [1,2,5,7.6,2.3,1,1,2,-1]); A

[ 1.0  2.0  5.0]
[ 7.6  2.3  1.0]
[ 1.0  2.0 -1.0]
sage: b = vector(RDF,[1,2,3])
sage: A.solve_left(b)       
(-0.113695090439, 1.39018087855, -0.333333333333)
sage: A.solve_left_LU(b)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/grout/<ipython console> in <module>()

/home/grout/sage/local/lib/python2.5/site-packages/sage/matrix/matrix_double_dense.so in sage.matrix.matrix_double_dense.Matrix_double_dense.solve_left_LU (sage/matrix/matrix_double_dense.c:4930)()

TypeError: unsupported operand type(s) for *: 'NoneType' and 'NoneType'
sage: A.LU()

([0.0 1.0 0.0]
[1.0 0.0 0.0]
[0.0 0.0 1.0],
 [           1.0            0.0            0.0]
[0.131578947368            1.0            0.0]
[0.131578947368            1.0            1.0],
 [          7.6           2.3           1.0]
[          0.0 1.69736842105 4.86842105263]
[          0.0           0.0          -6.0])
sage: A.solve_left_LU(b)
too many axes: 2 (effrank=2), expected rank=1
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (981, 0))

---------------------------------------------------------------------------
error                                     Traceback (most recent call last)

/home/grout/<ipython console> in <module>()

/home/grout/sage/local/lib/python2.5/site-packages/sage/matrix/matrix_double_dense.so in sage.matrix.matrix_double_dense.Matrix_double_dense.solve_left_LU (sage/matrix/matrix_double_dense.c:4995)()

/home/grout/sage/local/lib/python2.5/site-packages/scipy/linalg/basic.pyc in lu_solve((lu, piv), b, trans, overwrite_b)
     48         raise ValueError, "incompatible dimensions."
     49     getrs, = get_lapack_funcs(('getrs',),(lu,b1))
---> 50     x,info = getrs(lu,piv,b1,trans=trans,overwrite_b=overwrite_b)
     51     if info==0:
     52         return x

error: failed in converting 2nd argument `piv' of clapack.dgetrs to C/Fortran array
```


The first error comes from the code not computing LU before using the cached LU decomposition.  The second error apparently comes from a mistake in calling scipy.


---

Comment by jason created at 2009-01-03 08:08:25

Changing status from new to assigned.


---

Comment by jason created at 2009-01-03 08:08:25

Changing assignee from was to jason.


---

Comment by jason created at 2009-01-03 10:17:44

Okay, apparently lu_factor and lu in the scipy library return two completely different things.

Some notes from some experimentation:

1. scipy.linalg.lu is usually significantly slower than scipy.linalg.lu_factor

2. scipy.linalg.lu_factor returns a much more compact answer

3. scipy.linalg.lu_factor returns an answer directly suitable for lu_solve, etc.

I say we cache the lu_factor results and then build the P,L,U from these results if needed.

The strictly lower triangular part of the returned matrix is the L, the upper triangular part is the U, so that the returned matrix is (L-identity)+U.

The pivot array gives the row swaps needed.  For example, the following code constructs the new order of rows based on the pivot array piv:


```
arr=range(size)
for i in range(size):
    arr[i],arr[piv[i]] = arr[piv[i]],arr[i]
```


The P matrix will then have a 1 in the (i,arr[i]) position (or the (arr[i],i) position...).

THE LU MATRIX RETURNED FROM lu_factor MIGHT BE TRANSPOSED!  It was in my case, for some reason.


---

Comment by jason created at 2009-01-03 10:19:36

However, the results from lu_factor also appear to give spurious answers, while the results from lu seem more correct numerically...


---

Comment by jason created at 2009-01-03 10:20:25

Replying to [comment:4 jason]:
> However, the results from lu_factor also appear to give spurious answers, while the results from lu seem more correct numerically...

never mind; it seems like that comment is not true; I get the same spurious answers from lu()


---

Comment by mabshoff created at 2009-01-04 19:39:36

Better luck in 3.3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-06 22:58:48

3.4 is for ReST tickets only.

Cheers,

Michael


---

Comment by dagss created at 2009-12-21 15:05:52

Changing status from new to needs_work.


---

Comment by dagss created at 2009-12-21 15:05:52

I'm thinking of fixing this ticket as soon as I've got time for it.

At any rate, one piece of opinion:

 - `solve_left_LU` should be removed (the current NotImplementedError has served as deprecation for over a year)
 - `solve_left` should, for numerical types, take an `algorithm` argument to switch between different numerical methods for solving, where LU is one of them. `solve_left` should 
 - By default, `solve_left` should use some iterative steps to ensure an error below a given treshold (and, say, fall back to QR etc.).

In addition, numerical matrices should have a `set_solve_algorithm` method. It is often known in the outer, calling code what kind of numerical algorithm is needed to solve a system, while some inner code might want to perform the actual call to `solve_left`. I.e. what algorithms perform well for a matrix is typically a property of the given matrix.


---

Comment by rbeezer created at 2011-02-19 07:12:17

It appears "straight" LU decomposition in `SciPy/NumPy` will accept non-square matrices as input, while the LU-factor routine still requires square input.

Do we want to try to support non-square systems with the straight LU decomposition?  It would mean foregoing the built-in solve routine that extens the LU-factor decomposition, and possibly a decision would have to be made about what to cache:  square (very compact) or non-square (more general).


---

Comment by rbeezer created at 2011-02-19 07:12:17

Changing status from needs_work to needs_info.


---

Comment by rbeezer created at 2011-02-24 05:40:25

According to:

http://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.solve.html#numpy.linalg.solve

The generic "solve" from `NumPy` uses LU decomposition anyway, via an LAPACK routine.

So it does not appear to me that `solve_left_LU` adds anything to `solve_left`?


---

Comment by rbeezer created at 2011-02-24 22:46:37

Changing status from needs_info to needs_review.


---

Attachment

This routine needs lots of work, has been "Not Implemented" for a long time, and with two routines for solving systems available (#7852), this should be removed.  Patch does just that.


---

Comment by jason created at 2011-02-24 23:39:10

Replying to [comment:10 rbeezer]:
> According to:
> 
> http://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.solve.html#numpy.linalg.solve
> 
> The generic "solve" from `NumPy` uses LU decomposition anyway, via an LAPACK routine.
> 
> So it does not appear to me that `solve_left_LU` adds anything to `solve_left`?

The point behind this patch is that the LU decomposition is cached in the matrix so that multiple solves using this matrix are much faster because you don't have to compute the LU decomposition each time.


---

Comment by jason created at 2011-02-24 23:39:25

(I mean, the point behind this function...)


---

Comment by rbeezer created at 2011-02-25 05:16:06

Changing status from needs_review to needs_info.


---

Comment by rbeezer created at 2011-02-25 05:16:06

OK, that makes sense, I was reading the code, not the doc string.  Three ideas:

  * Probably should be `solve_right`.

  * How about a more descriptive name, like `solve_right_precomputed`?

  * LU decomposition now works for rectangular matrices (#10839).  I'd think it would make the most sense to cache the "LU factor" matrix just for this purpose.  That's the _square_ matrix where L and U share space and the diagonal 1's are not present.


---

Comment by jdemeyer created at 2015-02-23 11:13:07

New commits:


---

Comment by jdemeyer created at 2015-02-23 11:13:07

Changing status from needs_info to positive_review.


---

Comment by vbraun created at 2015-02-24 00:39:27

Resolution: fixed
