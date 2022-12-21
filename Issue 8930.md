# Issue 8930: Deprecate EnumeratedSet

Issue created by migration from Trac.

Original creator: hivert

Original creation time: 2010-05-08 05:34:09

Assignee: hivert

Keywords: EnumeratedSet, deprecate

It is not use, redundant with `Set()` and confusing with `EnumeratedSets()`. Therefore it should be removed


---

Comment by hivert created at 2010-05-08 05:40:21

Changing status from new to needs_review.


---

Comment by hivert created at 2010-05-12 17:31:25

There was a failing doctest and I also discovered some typos in the doc of the Category EnumeratedSets (missing s)... I reupload a new patch.


---

Comment by hivert created at 2010-05-31 10:25:00

From Nicolas on combinat-series file:

```
trac_8930-enumerated_set_deprecate-fh.patch       # Positive review, assuming tests pass (NT)
```

I got a all test pass on massena. I'll just reupload from the queue, can you put a positive review ?


---

Comment by nthiery created at 2010-05-31 11:51:09

Changing status from needs_review to positive_review.


---

Attachment

Simple patch; does what it claims, and what it claims is good; pass tests; positive review!


---

Comment by mhansen created at 2010-06-05 22:11:50

Resolution: fixed
