# Issue 9288: Implement complex reflection groups

Issue created by migration from https://trac.sagemath.org/ticket/9288

Original creator: nthiery

Original creation time: 2010-06-21 07:26:13

Assignee: AlexGhitza

CC:  sage-combinat


```
    sage: ComplexReflectionGroup(1,1,5)
    WeylGroup of type A4

    sage: W = ComplexReflectionGroup(33); W
    returns the 33 rd exceptional group

    sage: W.diagram()
```


Note: the current implementation of Coxeter groups is in principle
designed to open the door for such generalizations; see in particular
the WeylGroup code for Coxeter groups implemented in terms of matrix
groups.



---

Comment by chapoton created at 2014-03-06 10:54:00

See #11187


---

Comment by chapoton created at 2015-06-05 15:48:20

Duplicate of #11187, can be closed.


---

Comment by chapoton created at 2015-06-05 15:48:20

Changing status from new to needs_review.


---

Comment by stumpc5 created at 2015-06-05 19:20:01

Resolution: duplicate


---

Comment by chapoton created at 2015-06-05 19:29:05

hmm, I think closed is only for the release manager... but no way back..
