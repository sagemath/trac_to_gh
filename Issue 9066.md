# Issue 9066: Improve documentation in shapes2.py

Issue created by migration from https://trac.sagemath.org/ticket/9066

Original creator: kcrisman

Original creation time: 2010-05-27 15:03:33

Assignee: mvngu

CC:  jason mvngu robertwb

plot.plot3d.shapes2.py was a mess, including having several weird helper functions that didn't really need doctests, such as

```
    def avg(a,b):
        return (a+b)/2.0
```

This cleans up the situation here.


---

Attachment

Based on 4.4.2


---

Comment by kcrisman created at 2010-05-27 15:13:01

This also improves the copyright situation, for which reason I have added robertwb and was to this, in case they have any emendations to it.  I figured they were mostly responsible, though :)

Also, I'm not sure what purpose the ruler functions serve.  They were never documented before, and do not show up anywhere else in the HG repository than in this file!  So one could remove them if they were intended for something else that is now handled elsewhere; either way is fine.


---

Comment by kcrisman created at 2010-05-27 15:13:01

Changing status from new to needs_review.


---

Attachment


---

Comment by mvngu created at 2010-06-15 01:50:34

I'm OK with kcrisman's patch, except for a few points which I have added in my reviewer patch. Changes in the reviewer patch include:

 * Use the new style of raising exceptions, e.g. use `TypeError` as if it's a function, not a statement. This new style is more consistent with Python 3.x. When it comes time to switch to using Python 3.x, there would be less work involved in making the transition to Python 3.x.
 * Put exception tests into a `TESTS` block.
 * Fix up docstring in `bezier3d` so it renders nicely in the reference manual.
 * Some miscellaneous typo fixes.

If my patch gets a positive review, the whole ticket is good to go.


---

Comment by kcrisman created at 2010-06-15 13:21:37

>  * Use the new style of raising exceptions, e.g. use `TypeError` as if it's a function, not a statement. This new style is more consistent with Python 3.x. When it comes time to switch to using Python 3.x, there would be less work involved in making the transition to Python 3.x.
Okay, as long as this still works in Python 2.6 or whatever.
>  * Put exception tests into a `TESTS` block.
Ok.
>  * Fix up docstring in `bezier3d` so it renders nicely in the reference manual.
I'm a minimalist about this sort of thing, as you know :)
>  * Some miscellaneous typo fixes.
So did we say `3-D` and not `3D`?  I purposely put `3D` because I thought that was the default... I never know.


---

Comment by kcrisman created at 2010-06-15 13:32:03

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2010-06-15 13:32:03

Docs look nice when built, passes tests.  Let's get this in!


---

Comment by davidloeffler created at 2010-07-01 09:03:45

This patch and #9088 seem to conflict -- if I apply both, I get a doctest failure:

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

Comment by kcrisman created at 2010-07-01 13:46:38

I'm not exactly sure how the texture numbers get decided, but I think there is some linear order involved with their names.  Anyway, this is easy enough to fix.  We should definitely apply this one first because it is much more annoying, and then it would be very simple to add a reviewer patch to #9088 to fix these trivialities.


---

Comment by ddrake created at 2010-07-22 07:44:59

Replying to [comment:6 kcrisman]:
>  We should definitely apply this one first because it is much more annoying, and then it would be very simple to add a reviewer patch to #9088 to fix these trivialities.

Oops, it's now too late for that. Applying these patches to 4.5.2.alpha0, I get the doctest errors mentioned above. We've already merged #9088, so we'll need to fix the problem here.


---

Comment by ddrake created at 2010-07-22 07:44:59

Changing status from positive_review to needs_work.


---

Comment by kcrisman created at 2010-07-22 12:39:51

Unfortunately I am not a queueing expert, so in order to fix this I will have to add yet another doctest fix patch.  Is that okay with the release managers?


---

Comment by ddrake created at 2010-07-22 13:05:50

Replying to [comment:8 kcrisman]:
> Unfortunately I am not a queueing expert, so in order to fix this I will have to add yet another doctest fix patch.  Is that okay with the release managers?

That's no problem at all.


---

Attachment

Apply this last.


---

Comment by kcrisman created at 2010-07-22 13:32:02

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2010-07-22 13:32:02

This should do it.  Hopefully a release manager can very easily review this.  Apply in order doc, reviewer, then doctest-fix.


---

Comment by ddrake created at 2010-07-23 00:10:04

Changing status from needs_review to positive_review.


---

Comment by ddrake created at 2010-07-23 00:10:04

Replying to [comment:10 kcrisman]:
> This should do it.  Hopefully a release manager can very easily review this.  Apply in order doc, reviewer, then doctest-fix.

Looks good.


---

Comment by ddrake created at 2010-07-23 00:10:35

Merged all three patches in 4.5.2.alpha1.


---

Comment by ddrake created at 2010-07-23 00:10:35

Resolution: fixed
