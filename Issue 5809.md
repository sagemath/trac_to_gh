# Issue 5809: schemes/generic/hypersurface.py is completely broken

Issue created by migration from https://trac.sagemath.org/ticket/5809

Original creator: AlexGhitza

Original creation time: 2009-04-17 10:44:25

Assignee: AlexGhitza

Keywords: hypersurface

The file has zero doctests, imports nonexisting classes and looks like it's never been used.

I'm attaching a patch that implements only the basic constructors and properties of projective and affine hypersurfaces, with 100% doctest coverage (of course :)

I plan to add some more interesting functionality later, but this is a start.



---

Attachment


---

Comment by AlexGhitza created at 2009-04-17 11:28:10

Changing status from new to assigned.


---

Comment by cremona created at 2009-04-18 16:11:18

apply after the main patch


---

Attachment

Positive review!

I added this to the reference manual which required a little tweaking (the EXAMPLES in an __init__ docstring are excluded from the manual since the function name starts with an underscore;  what works well is to copy the same examples into the class's own docstring, then they get into the manual).

I tested that the docs now build ok and look ok in the html ref manual.

I guess Alex should ok the extra patch.


---

Comment by AlexGhitza created at 2009-04-18 22:18:26

John, thanks for reviewing and for the new fixes.  Your patch looks good.


---

Comment by mabshoff created at 2009-04-23 06:35:24

There are some doctest failures against 3.4.1:

```
        sage -t  devel/sage/sage/schemes/elliptic_curves/ell_point.py # 2 doctests failed
        sage -t  devel/sage/sage/schemes/elliptic_curves/ell_generic.py # 3 doctests failed
        sage -t  devel/sage/sage/schemes/plane_curves/constructor.py # 1 doctests failed
        sage -t  devel/sage/sage/schemes/elliptic_curves/ell_field.py # 1 doctests failed
```

For example:

```
sage -t  "devel/sage/sage/schemes/elliptic_curves/ell_point.py"
**********************************************************************
File "/scratch/mabshoff/sage-3.4.2.alpha0/devel/sage/sage/schemes/elliptic_curves/ell_point.py", line 175:
    sage: E(1,0,0)
Expected:
    Traceback (most recent call last):
    ...
    TypeError: coordinates [1, 0, 0] do not define a point on
    Elliptic Curve defined by y^2 + y = x^3 - x over Rational Field
Got:
    Traceback (most recent call last):
      File "/scratch/mabshoff/sage-3.4.2.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.4.2.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.4.2.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[6]>", line 1, in <module>
        E(Integer(1),Integer(0),Integer(0))###line 175:
    sage: E(1,0,0)
      File "/scratch/mabshoff/sage-3.4.2.alpha0/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_generic.py", line 611, in __call__
        return plane_curve.ProjectiveCurve_generic.__call__(self, *args, **kwds)
      File "/scratch/mabshoff/sage-3.4.2.alpha0/local/lib/python2.5/site-packages/sage/schemes/generic/scheme.py", line 198, in __call__
        return self.point(args)
      File "/scratch/mabshoff/sage-3.4.2.alpha0/local/lib/python2.5/site-packages/sage/schemes/generic/scheme.py", line 232, in point
        return self._point_class(self, v, check=check)
      File "/scratch/mabshoff/sage-3.4.2.alpha0/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_point.py", line 275, in __init__
        point_homset.codomain()._check_satisfies_equations(v)
      File "/scratch/mabshoff/sage-3.4.2.alpha0/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_field.py", line 34, in _check_satisfies_equations
        self._error_bad_coords(v)
    AttributeError: 'EllipticCurve_rational_field' object has no attribute '_error_bad_coords'
**********************************************************************
<SNIP>
```



---

Comment by mabshoff created at 2009-04-23 06:47:05

Ooops, wrong patch to complain about, reinstating positive review. My bad :)

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-23 06:47:58

Merged in Sage 3.4.2.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-23 06:47:58

Resolution: fixed
