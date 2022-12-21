# Issue 9923: Doctest error in sage/geometry/polyhedra.py

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-09-16 23:41:58

Assignee: mvngu

CC:  alexghitza novoselt vbraun

I get this doctest error with a trial 4.6.alpha1 on sage.math and many other Sage cluster and Skynet machines:

```python
sage -t -long  devel/sage/sage/geometry/polyhedra.py
**********************************************************************
File "/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1/devel/sage-main/sage/geometry/polyhedra.py", line 1270:
    sage: p1.projection().show() + p2.projection().show() + p3.projection().show()
Expected nothing
Got:
    doctest:4555: DeprecationWarning: (Since Sage 4.6) use the option 'width' instead of 'thickness'
    <BLANKLINE>
**********************************************************************
```



---

Comment by mpatel created at 2010-09-16 23:42:41

If it's feasible to create a patch now, I can merge it into 4.6.alpha1, while I wait for a response to a build error at #4000.


---

Comment by AlexGhitza created at 2010-09-17 00:33:29

I'm not seeing this in 4.6.alpha0.  It looks like some graphics ticket you merged between alpha0 and alpha1 introduced a new deprecation warning.  Any idea which ticket it might be?

If we can find that out, it shouldn't be difficult to change either the code or the doctest to use the new non-deprecated way of doing things.


---

Comment by vbraun created at 2010-09-17 00:41:49

Ticket #7154 changed the options for point/arrow thickness and was merged in 4.6.alpha1. I didn't realize that this impacts the polyhedra package, but of course it does. Anyways, the obvious patch is to change the option name in polyhedra.py.


---

Comment by mpatel created at 2010-09-17 00:49:46

By the way, the unofficial, trial 4.6.alpha1 is in `/home/release/sage-4.6.alpha1` on the Sage cluster.


---

Attachment


---

Comment by AlexGhitza created at 2010-09-17 01:40:35

Changing status from new to needs_review.


---

Comment by AlexGhitza created at 2010-09-17 01:40:35

OK, a fairly trivial patch is now up.


---

Comment by novoselt created at 2010-09-17 03:22:36

Solves the for me issue!


---

Comment by novoselt created at 2010-09-17 03:22:36

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-09-17 03:27:16

Thanks!


---

Comment by mpatel created at 2010-09-17 03:27:16

Resolution: fixed
