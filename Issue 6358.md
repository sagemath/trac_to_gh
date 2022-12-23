# Issue 6358: use numpy to optimize RDF and CDF solve_right functions

Issue created by migration from https://trac.sagemath.org/ticket/6358

Original creator: was

Original creation time: 2009-06-18 19:44:09

Assignee: was

CC:  rbeezer


```
> Does sage have a way to use a numeric method (such as Jacobi, or Gauss-
> Sidel) to solve matrix equations of the form A*x = b? (CDF matrices by
> the way). the A.solve_right(b) method is too slow.
>
> Thanks,
> Ethan

Here is an example of how to convert back/forth to numpy to solve A*x
# b very quickly.  Below we do this with A a 1000x1000 matrix, and it
takes about a half second.   It would be *great* if somebody made it
so this would work in Sage automatically without having to explicitly
use numpy like I've done before.  But for you, I bet this is a minor
inconvenience.

sage: n = 1000
sage: a = random_matrix(CDF,n); v = random_matrix(CDF,n,1)
sage: aa = a.numpy(); vv = v.numpy()
sage: import numpy
sage: time ww = numpy.linalg.solve(aa, vv)
Time: CPU 0.57 s, Wall: 0.41 s
sage: w = matrix(CDF, ww)
sage: max([abs(z) for z in a*w - v])
5.46740430707e-12 + 8.431033649e-13*I
```



---

Comment by jason created at 2009-06-19 02:54:03

This already works.  The problem is that it is backwardly-named solve_left.  The solve_right function incurs the overhead of a matrix copy (but then solves the backwards equation, since solve_left is backwards).

To fix all this:

  1. Rename the matrix_double_dense.pyx solve_left to solve_right
  2. implement a matrix_double_dense.pyx solve_left that takes the transpose and then calls solve_right


Eventually, we also need to fix the lu solve.  There is another trac ticket for this somewhere.  The problem is that the function does not deal correctly with the output of the scipy lu decomposition.


---

Comment by jason created at 2009-06-21 06:49:13

rbeezer: Ideally, we should also make sure the solve_* functionality mimics how you did the kernel_* functionality (i.e., that a person can define either or both in a matrix subclass and the right thing is done to make the other function make sense).


---

Comment by jdemeyer created at 2016-03-31 12:10:45

`solve_left` and `solve_right` already use `scipy` currently...


---

Comment by jdemeyer created at 2016-03-31 12:10:45

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2016-03-31 12:10:50

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2016-06-12 12:02:30

Resolution: fixed
