# Issue 7360: isomorphism_type_info_simple_group returns an exception instead of raising it

Issue created by migration from Trac.

Original creator: AlexGhitza

Original creation time: 2009-10-31 13:04:24

Assignee: joyner

Currently (sage-4.2):


```
sage: S = KleinFourGroup()
sage: S.isomorphism_type_info_simple_group()
(<type 'exceptions.TypeError'>, 'Group must be simple.')
```


The attached patch fixes this and adds a doctest.



---

Attachment


---

Comment by AlexGhitza created at 2009-10-31 13:08:13

Changing status from new to needs_review.


---

Comment by kcrisman created at 2009-11-10 22:34:13

Positive review - nice catch.


---

Comment by kcrisman created at 2009-11-10 22:34:13

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-11-12 06:50:30

Resolution: fixed
