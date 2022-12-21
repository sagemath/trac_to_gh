# Issue 6291: Missing identity function in AbelianGroup

Issue created by migration from Trac.

Original creator: jlefebvre

Original creation time: 2009-06-15 03:30:39

Assignee: joyner

Keywords: AbelianGroup

Missing identity function

AbelianGroup patch
Since we can do;

```
sage: G = DihedralGroup(10)
sage: G.identity()
()
sage: G = SymmetricGroup(5)
sage: G.identity()
()
```

I thought we should be able to do the following

```
sage: G = AbelianGroup([2,2])
sage: G.identity()
1
```



---

Attachment

The identity Function


---

Comment by rbeezer created at 2009-10-05 05:01:03

Good idea.

Applies, builds, functions, docs build, passes long tests.

Positive review.


---

Comment by rbeezer created at 2009-10-05 05:01:03

Changing keywords from "AbelianGroup" to "AbelianGroup, identity".


---

Comment by jason created at 2009-10-06 19:01:34

Changing status from new to needs_review.


---

Comment by jason created at 2009-10-06 19:01:42

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-10-19 05:49:23

Resolution: fixed
