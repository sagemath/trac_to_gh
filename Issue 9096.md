# Issue 9096: Fixes wrong sphinx markup :cls:

Issue created by migration from https://trac.sagemath.org/ticket/9096

Original creator: hivert

Original creation time: 2010-05-30 18:52:00

Assignee: hivert

CC:  sage-combinat

Keywords: Sphinx

The file `disjoint_union_enumerated_sets.py` contains the following wrong line

```
        Normalization of arguments; see :cls:`UniqueRepresentation`.
```



---

Attachment

Ready for review


---

Comment by hivert created at 2010-05-30 18:54:51

Changing status from new to needs_review.


---

Comment by nthiery created at 2010-05-31 13:20:53

Trivial patch. Florent: you may set a positive review as soon as you have checked that all test pass.


---

Comment by nthiery created at 2010-05-31 13:20:53

Changing assignee from hivert to nthiery.


---

Comment by hivert created at 2010-05-31 13:27:26

Changing status from needs_review to positive_review.


---

Comment by hivert created at 2010-05-31 13:27:26

Replying to [comment:2 nthiery]:
> Trivial patch. Florent: you may set a positive review as soon as you have checked that all test pass.

Massena already did :-) !


---

Comment by hivert created at 2010-06-02 18:25:18

Changing assignee from nthiery to hivert.


---

Comment by mhansen created at 2010-06-06 00:45:59

Resolution: fixed
