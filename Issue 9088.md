# Issue 9088: line3d does not take a tuple of points

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2010-05-29 19:47:00

Assignee: jason, was

CC:  kcrisman mhampton

Right now, this fails:


```
line3d(( (0,0,0), (1,2,3) ))
```


since the copy of the input data is not converted to a list.  This is an easy fix.


---

Attachment


---

Comment by jason created at 2010-05-29 19:53:13

Fix attached.  This should be a trivial review!


---

Comment by jason created at 2010-05-29 19:53:13

Changing status from new to needs_review.


---

Comment by kcrisman created at 2010-06-18 18:44:38

Positive review.


---

Comment by kcrisman created at 2010-06-18 18:44:38

Changing status from needs_review to positive_review.


---

Comment by davidloeffler created at 2010-07-01 09:03:25

This patch and #9066 seem to conflict -- if I apply both, I get a doctest failure:

```
sage -t  "devel/sage-reviewing/sage/plot/plot3d/shapes2.py"
**********************************************************************
File "/storage/masiao/sage-4.5.alpha1/devel/sage-reviewing/sage/plot/plot3d/shapes2.py", line 700:
    sage: P.tachyon_repr(P.default_render_params())
Expected:
    'Sphere center 1.0 2.0 3.0 Rad 0.015 texture84'
Got:
    'Sphere center 1.0 2.0 3.0 Rad 0.015 texture85'
**********************************************************************
File "/storage/masiao/sage-4.5.alpha1/devel/sage-reviewing/sage/plot/plot3d/shapes2.py", line 717:
    sage: P.obj_repr(P.default_render_params())[0][0:2]
Expected:
    ['g obj_1', 'usemtl texture86']
Got:
    ['g obj_1', 'usemtl texture87']
**********************************************************************
File "/storage/masiao/sage-4.5.alpha1/devel/sage-reviewing/sage/plot/plot3d/shapes2.py", line 825:
    sage: L.tachyon_repr(L.default_render_params())[0]
Expected:
    'FCylinder base 1.0 0.0 0.0 apex 0.999950000417 0.00999983333417 0.0001 rad 0.005 texture126'
Got:
    'FCylinder base 1.0 0.0 0.0 apex 0.999950000417 0.00999983333417 0.0001 rad 0.005 texture127'
**********************************************************************
3 items had failures:
   1 of   4 in __main__.example_13
   1 of   4 in __main__.example_14
   1 of   4 in __main__.example_19
***Test Failed*** 3 failures.
```


This doesn't come up if I apply either one of the patches on its own.


---

Comment by kcrisman created at 2010-07-01 13:47:32

I'm not exactly sure how the texture numbers get decided, but I think there is some linear order involved with their names.  Anyway, this is easy enough to fix.  We should definitely apply #9088 first because it is much more annoying, and then it would be very simple to add a reviewer patch to fix these trivialities.

I'll leave this as positive review until the release manager decides what order to merge these in, though - wouldn't want to overstep his prerogative :)  then he can mark whichever one needs work thus.


---

Comment by mpatel created at 2010-07-20 10:12:39

Resolution: fixed
