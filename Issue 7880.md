# Issue 7880: Category of sets with partial maps.

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2010-01-09 19:40:58

Assignee: nthiery

In support of #7585 and Tate's algorithm over function fields.


---

Attachment


---

Comment by robertwb created at 2010-01-09 19:50:25

Changing status from new to needs_review.


---

Comment by robertwb created at 2010-01-09 19:50:44

Changing status from needs_review to positive_review.


---

Comment by robertwb created at 2010-01-09 19:50:44

Looks good.


---

Comment by nthiery created at 2010-01-09 21:40:54

I am not convinced about the name, which suggests at first that the objects are Sets with more structure, not less. I don't have a better suggestion though. If nobody comes up with something better (ObjectsWith???) in a day or two, just put back a positive review.


---

Comment by nthiery created at 2010-01-09 21:40:54

Changing status from positive_review to needs_work.


---

Comment by nthiery created at 2010-01-09 21:41:05

Changing status from needs_work to needs_info.


---

Comment by roed created at 2010-02-23 14:54:28

This is needed for the series of patches starting at 8218.  I agree that the name is not optimal, but nobody's come up with a better one in 6 weeks...


---

Comment by roed created at 2010-02-23 14:54:28

Changing status from needs_info to needs_review.


---

Comment by roed created at 2010-02-23 17:38:47

Part of a series:

```
8218 -> 8332 -> 7880 -> 7883 -> 8333 -> 8334 -> 8335
```

I tried to make each of these mostly self contained, with doctests passing after every ticket, but I didn't entirely succeed.  If you're reviewing one of these tickets, applying later tickets will hopefully fix doctest failures that you're seeing.


---

Attachment

replaces previous patch


---

Comment by davidloeffler created at 2010-03-17 21:44:04

Looks good to me. I've made some tiny doctest fixes, and uploaded a new version of the patch, still with roed's user stamp on it. This applies cleanly to 4.3.4.rc0, if you apply the patches in the following order:

```
$ sage -hg qseries
trac_8218_fixes_434alpha1.patch
trac_8332_givaro_python.patch
trac_8332_reviewer.patch
trac_7880-sets_with_partial_maps.patch
```



on top of the patches at #8218 and #8332.


---

Comment by davidloeffler created at 2010-03-17 21:44:04

Changing status from needs_review to positive_review.


---

Comment by nthiery created at 2010-03-20 15:55:16

Oh, just one thing: are objects in SetsWithPartialMaps parents or not?


---

Comment by jhpalmieri created at 2010-04-15 20:13:34

Merged "trac_7880-sets_with_partial_maps.patch" in 4.4.alpha0


---

Comment by jhpalmieri created at 2010-04-15 20:13:34

Resolution: fixed
