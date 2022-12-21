# Issue 8975: Methods missing for reducible root systems

Issue created by migration from Trac.

Original creator: Bruce

Original creation time: 2010-05-15 21:25:22

Assignee: AlexGhitza

The class sage.combinat.root_system.type_reducible.CartanType
is missing an is_crystalographic and is_simply_laced


```
 sage: R = CartanType("D4xA5")
 sage: R.is_crystalographic()
 sage: R.is_simply_laced()
```


These both give False which is incorrect.


---

Comment by tscrim created at 2012-05-12 13:31:30

Changing status from new to needs_review.


---

Comment by tscrim created at 2012-05-12 13:31:30

Changing keywords from "" to "days38".


---

Comment by tscrim created at 2012-05-12 13:31:30

This has been taken care of (probably in #6588).


```
sage: R = CartanType("D5xA4")
sage: R.is_crystalographic()
True
sage: R.is_simply_laced()
True
```


I'm requesting that this ticket be closed.


---

Comment by kini created at 2012-05-16 14:03:49

Changing status from needs_review to positive_review.


---

Comment by kini created at 2012-05-16 14:03:49

When you want the release manager to close a ticket, you should set it to positive_review, so he will see it.


---

Comment by jdemeyer created at 2012-05-21 08:06:48

Resolution: worksforme
