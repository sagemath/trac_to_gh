# Issue 6115: make symbolic matrices use pynac symbolics

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-05-21 18:39:36

Assignee: was

Currently, it looks like the symbolic matrix code in `matrix/matrix_symbolic_dense.pyx` goes to maxima for everything.  This makes things **slow** and, at least in 3.4.2, it was easy to crash Maxima by calculating a 6x6 determinant, for example.

Here is an example of how the current general algorithms in Sage can speed things up (even before making the matrix be stored in Sage instead of Maxima).


```
sage: var('x00,x01,x10,x11')
sage: a=matrix(2,[[x00,x01],[x10,x11]])
sage: %timeit a.det()
10 loops, best of 3: 218 ms per loop
```


I went into matrix/matrix_symbolic_dense.pyx and just commented out the determinant routine.  This way, it uses the generic determinant routine for matrices.  Note that we still have to get values from maxima for this, but the multiplication and things are done in pynac.

Generic determinant algorithm:


```
sage: var('x00,x01,x10,x11')
(x00, x01, x10, x11)
sage: a=matrix(2,[[x00,x01],[x10,x11]])
sage: %timeit a.det()
100000 loops, best of 3: 5.85 µs per loop
sage: %timeit a.det()
100000 loops, best of 3: 6.15 µs per loop
```


So, the generic Sage code with pynac took about 3% of the time it took to call maxima and ask it for the determinant.


---

Comment by jason created at 2009-05-21 18:46:19

Mike Hansen mentions that all of the docstrings should be moved up to the module docstring.  Most of this patch would probably be just deleting functions in matrix_symbolic_dense.pyx.


---

Comment by jason created at 2009-05-26 19:16:22

Almost positive review.  Here is a problem:


```
sage: a=matrix(SR, [[1,2],[3,4]])
sage: a.eig
a.eigenmatrix_left    a.eigenspaces         a.eigenspaces_right   a.eigenvectors_left   
a.eigenmatrix_right   a.eigenspaces_left    a.eigenvalues         a.eigenvectors_right  
sage: a.eigenm
a.eigenmatrix_left   a.eigenmatrix_right  
sage: a.eigenmatrix_right()
/home/grout/.sage/temp/good/26004/_home_grout__sage_init_sage_0.py:1: UserWarning: Using generic algorithm for an inexact ring, which may result in garbarge from numerical precision issues.
  # -*- coding: utf-8 -*-
/home/grout/.sage/temp/good/26004/_home_grout__sage_init_sage_0.py:1: UserWarning: Using generic algorithm for an inexact ring, which will probably give incorrect results due to numerical precision issues.
  # -*- coding: utf-8 -*-
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/grout/.sage/temp/good/26004/_home_grout__sage_init_sage_0.py in <module>()

/home/grout/download/sage-sage-4.0.alpha0.5/local/lib/python2.5/site-packages/sage/matrix/matrix2.so in sage.matrix.matrix2.Matrix.eigenmatrix_right (sage/matrix/matrix2.c:21183)()
   3505             True
   3506         """
-> 3507         D,P=self.transpose().eigenmatrix_left()
   3508         return D,P.transpose()
   3509 

/home/grout/download/sage-sage-4.0.alpha0.5/local/lib/python2.5/site-packages/sage/matrix/matrix2.so in sage.matrix.matrix2.Matrix.eigenmatrix_left (sage/matrix/matrix2.c:20868)()
   3440         """
   3441         from sage.misc.flatten import flatten
-> 3442         evecs = self.eigenvectors_left()
   3443         D = sage.matrix.constructor.diagonal_matrix(flatten([This is the Trac macro *e[0* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#e[0-macro)*e[2] for e in evecs]))
   3444         rows = []

/home/grout/download/sage-sage-4.0.alpha0.5/local/lib/python2.5/site-packages/sage/matrix/matrix2.so in sage.matrix.matrix2.Matrix.eigenvectors_left (sage/matrix/matrix2.c:20199)()
   3324         from sage.rings.qqbar import QQbar
   3325         from sage.categories.homset import hom
-> 3326         eigenspaces = self.eigenspaces_left(algebraic_multiplicity=True)
   3327         evec_list=[]
   3328         n = self._nrows

/home/grout/download/sage-sage-4.0.alpha0.5/local/lib/python2.5/site-packages/sage/matrix/matrix2.so in sage.matrix.matrix2.Matrix.eigenspaces_left (sage/matrix/matrix2.c:18811)()
   3061         i = 0
   3062         for h, e in G:
-> 3063             if h.degree() == 1:
   3064                 alpha = -h[0]/h[1]
   3065                 F = alpha.parent()

TypeError: degree() takes exactly one argument (0 given)
```



---

Comment by jason created at 2009-05-26 19:17:33

I should mention that all but about 3 lines of the above patch are Mike Hansen's, so I'm not reviewing my own patch!  I did add the simplify_rational() calls to the exponent doctests and the deprecation warning to is_simplified; those should be reviewed by someone other than me.


---

Comment by jason created at 2009-05-26 19:24:59

Playing around with things gives more interesting errors:


```
sage: a=matrix(SR, [[1,2],[3,x]])
sage: a.fcp('x')
-6
sage: a.fcp('y')
-x*y + y^2 + x - y - 6
```



---

Comment by jason created at 2009-05-26 21:03:12

apply on top of previous patches


---

Attachment

the trac-6115-symbolic-eigenvalues.patch  patch needs to be reviewed as well.


---

Comment by jason created at 2009-05-28 05:06:08

the complaints that I raise above happened with the old implementation of symbolic matrices, so they are beyond the scope of this ticket.

I positively review mhansen's part (the first patch, which I posted).  My part (the second patch) needs to be reviewed, though.


---

Comment by jason created at 2009-05-28 05:10:03

(well, and the three or so lines that I changed from mhansen's patch; see my above comment)


---

Comment by mhansen created at 2009-05-28 05:12:11

Jason's patch looks good to me.  I just put up a new version of #6115 which fixes a doctest failure in sage/matrix/tests.py.


---

Comment by jason created at 2009-05-28 05:18:35

Yep, and Mike's change looks good to me and makes tests.py pass doctests, so positive review.


---

Attachment


---

Comment by mhansen created at 2009-05-28 06:04:44

Merged both patches in 4.0.rc1.


---

Comment by mhansen created at 2009-05-28 06:04:44

Resolution: fixed
