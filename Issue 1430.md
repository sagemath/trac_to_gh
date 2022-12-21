# Issue 1430: [with spkg] sparse eigenvalues and splines

Issue created by migration from Trac.

Original creator: jkantor

Original creation time: 2007-12-08 22:57:19

Assignee: was

scipy has a sandbox directory with experimental or code in development.
One of the packages is an arpack wrapper which computes eigenvalues of sparse matrices.
matlab uses this in its eigs command. Although the arpack wrapper is not completely finished, it
has useful functionality, and since this has been requested multiple times I think including it is good, it will also maybe spur some people to take the wrapper the last mile (me probably).

Also included is a wrapper of fitpack which has some spline functions (bivariate spline, etc).

http://sage.math.washington.edu/home/jkantor/spkgs/scipy_sandbox.spkg


The following shows how to compute the smallest five eigenvalues 
(in magnitude) of a 2000x2000 matrix


```
import arpack
from scipy import sparse
m=sparse.csc_matrix(random_matrix(RDF,2000,2000,density=.02).numpy())
e,v=arpack.eigen(m,5)
```



---

Comment by jkantor created at 2007-12-13 06:55:07

patch with doctests 
http://sage.math.washington.edu/home/jkantor/spkgs/arpack_doctest.patch


---

Comment by mabshoff created at 2007-12-13 09:04:55

Merged in 2.9.alpha6.


---

Comment by mabshoff created at 2007-12-13 09:04:55

Resolution: fixed


---

Comment by jkantor created at 2007-12-14 21:49:03

new patch, makes the doctest more stable (hopefully)
http://sage.math.washington.edu/home/jkantor/spkgs/arpack_doctest_2.patch

(apply after applying the first one)


---

Comment by mabshoff created at 2007-12-15 09:35:59

I apply arpack_doctest_2.patch to 2.9.rc0.

Cheers,

Michael
