# Issue 4269: add code to help detect which systems are used in performing a computation

Issue created by migration from https://trac.sagemath.org/ticket/4269

Original creator: mhansen

Original creation time: 2008-10-12 18:02:57

Assignee: cwitty




---

Attachment

The detection strings could probably use some refinement, but I'm going to spend some time working one something else.


---

Comment by mhansen created at 2008-10-12 18:09:02

Changing assignee from cwitty to mhansen.


---

Comment by mhansen created at 2008-10-12 18:09:02

Changing status from new to assigned.


---

Attachment


---

Comment by robertwb created at 2008-10-14 20:19:02

I added a bit more of a disclaimer, and raised a better error on non-strings (so when one types `get_systems('integrate(x^2, x)')` one doesn't get an obscure error. 

I give this a positive review, but someone should look at my changes.


---

Comment by PolyBoRi created at 2008-10-21 09:12:42

I tested the type checking and ran some other example.
Michael


---

Comment by mabshoff created at 2008-10-26 02:26:00

Merged both patches in Sage 3.2.alpha1


---

Comment by mabshoff created at 2008-10-26 02:26:00

Resolution: fixed
