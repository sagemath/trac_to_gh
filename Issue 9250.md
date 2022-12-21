# Issue 9250: Bug in crystal code

Issue created by migration from Trac.

Original creator: aschilling

Original creation time: 2010-06-16 21:25:50

Assignee: sage-combinat

CC:  combinat

This currently breaks:

sage: B=KirillovReshetikhinCrystal(['D',5,1], 3,1)
sage: B[0].e(0)

This has to do with the method intermediate_shape for plus/minus diagrams.


---

Comment by aschilling created at 2010-06-16 21:43:10

Changing status from new to needs_review.


---

Comment by aschilling created at 2010-06-16 21:43:10

Changing keywords from "" to "crystals".


---

Attachment


---

Comment by bump created at 2010-06-25 20:51:33

Changing status from needs_review to positive_review.


---

Comment by bump created at 2010-06-25 20:51:33

After the patch, passes `sage -testall`.

Fixes the crash mentioned in the Description.

Includes doctest.

Apparently the intermediate_shape method of PMDiagram presumed
that self.n was 2.

This one-line fix is obviously correct.


---

Comment by mpatel created at 2010-07-21 01:44:09

Resolution: fixed
