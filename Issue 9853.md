# Issue 9853: make networkx compatibel with numpy-1.4.1

Issue created by migration from Trac.

Original creator: maldun

Original creation time: 2010-09-04 00:11:18

Assignee: tbd

In order to finish Ticket #9808 (http://trac.sagemath.org/sage_trac/ticket/9808) there have to be a small patch applied to networks


---

Attachment

changes


---

Comment by maldun created at 2010-09-04 00:17:54

Changing status from new to needs_review.


---

Attachment

Downward compatibel patch


---

Comment by maldun created at 2010-09-04 01:30:03

modified version for networkx to make numpy-1.4.1 compatible


---

Attachment


---

Comment by fbissey created at 2010-09-04 08:45:52

As I mentioned in the numpy upgrade bug we are moving to networkx-1.2.
So this bug may be invalid. Check have to be done against networkx-1.2 not 1.0.1.


---

Comment by maldun created at 2010-09-04 20:20:17

Ok like mentioned in #9808 networkx-1.2 works with the numpy packages just fine.
But I had to install a new version, because I was not able to just install networkx-1.2 into my old version of sage-4.2. After intalling it and applying the patches it still didn't work correctly. But the patch of 1.0.1 above worked well for me. So it could still be usefull.
But I think we could close this ticket then.


---

Comment by maldun created at 2010-09-04 20:51:51

Resolution: fixed


---

Comment by mvngu created at 2010-09-05 05:12:53

How is this ticket considered fixed? Do you want the attached NetworkX package to be merged in the Sage standard repository? If so, has it been merged yet? If not, you need to explain why you closed this ticket.


---

Comment by mvngu created at 2010-09-05 05:12:53

Changing status from closed to needs_work.


---

Comment by fbissey created at 2010-09-05 08:47:45

Replying to [comment:8 mvngu]:
> How is this ticket considered fixed? Do you want the attached NetworkX package to be merged in the Sage standard repository? If so, has it been merged yet? If not, you need to explain why you closed this ticket.

It should have been closed invalid. Numpy-1.4.1 and networkx-1.0.1 don't go along
very well together. But it doesn't matter since next sage release will use networkx-1.2 which works well with numpy-1.4.1. I am changing it to "invalid".


---

Comment by fbissey created at 2010-09-05 08:47:45

Resolution changed from fixed to invalid
