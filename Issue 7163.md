# Issue 7163: right kernel does not respect sparse=True

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2009-10-08 21:05:55

Assignee: tbd


```
<Submarine> hi
<Submarine> sage: ker=m.right_kernel(sparse=True)
<Submarine> sage: type(ker.basis_matrix())
<Submarine> <type 'sage.matrix.matrix_rational_dense.Matrix_rational_dense'>
<Submarine> Is it normal I'm getting a dense matrix?
```



---

Comment by was created at 2009-10-10 02:57:55


```
The "sparse=True" option you are passing to right_kernel isn't
implemented at all.

In fact, the way right_kernel is implemented you can make up an
options you want and they will be silently ignored:


sage: ker=m.right_kernel(foobar=True, stand_on_your_head=True,
use_the_force=True, super_sparse=True, dumb=False)

In the meantime you can get a sparse matrix as follows:

sage: ker=m.right_kernel().basis_matrix().sparse_matrix()
sage: type(ker)
<type 'sage.matrix.matrix_rational_sparse.Matrix_rational_sparse'>
sage: ker.row_module()
Sparse vector space of degree 100 and dimension 99 over Rational Field
Basis matrix:
99 x 100 sparse matrix over Rational Field

Here's the relevant code for "right_kernel", which as you can see does
nothing with sparseness...

Obviously it would be desirable for somebody to fix the right_kernel
command so one gets errors for all unused options, and all options
that should be supported are supported.


       if R.is_field():
           E = self.echelon_form(*args, **kwds)
           pivots = E.pivots()
           pivots_set = set(pivots)
           basis = []
           V = R ** self.ncols()
           ONE = R(1)
           for i in xrange(self._ncols):
               if not (i in pivots_set):
                   v = V(0)
                   v[i] = ONE
                   for r in range(len(pivots)):
                       v[pivots[r]] = -E[r,i]
                   basis.append(v)
           W = V.submodule(basis)
           if W.dimension() != len(basis):
               raise RuntimeError, "bug in right_kernel function in
matrix2.pyx -- basis from echelon form is not a basis."
           self.cache('right_kernel', W)
           return W
```



---

Comment by AlexGhitza created at 2009-11-15 13:11:19

Changing component from algebra to linear algebra.
