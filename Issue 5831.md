# Issue 5831: [with patch, not ready for review] reducible root system fixes

Issue created by migration from Trac.

Original creator: bump

Original creation time: 2009-04-20 05:10:13

Assignee: bump

CC:  sage-combinat

The methods simple_roots(), fundamental_weights() and simple_coroots() for the ambient space of a root system are supposed to return a family. This was never correctly implemented for the reducible types, and the patch corrects this.

There are also some changes in weyl_characters.py, where it was assumed that the root system was irreducible in a few places. The patch corrects this.

The patch is probably correct but I haven't confirmed that it applies cleanly to sage-3.4.1.rc3 or that it passes `sage --testall` so wait to review.


---

Comment by bump created at 2009-04-20 05:15:14

fixes for reducible root systems


---

Comment by bump created at 2009-04-20 05:18:01

Changing status from new to assigned.


---

Attachment


---

Comment by nthiery created at 2009-04-20 21:50:40

Sounds good to me.
Is it needed to implement simple_roots? I would have expected the default implementation
for ambient spaces (as coroots associated to the simple roots) to work.


---

Comment by bump created at 2009-04-21 00:12:08

Replying to the last message, I think it is necessary to implement simple_roots (and also simple_coroots and fundamental_weights).

Nicolas requested a doctest. See:

http://groups.google.com/group/sage-combinat-devel/msg/4004c4a8471f3cfa?hl=en&pli=1

I did this. I put the new doctest in type_reducible.py.


---

Comment by nthiery created at 2009-04-21 05:24:38

> Replying to the last message, I think it is necessary to implement simple_roots (and also simple_coroots and fundamental_weights).

Oops, sorry for the confusion. I was wondering wether it was necessary to implement the simple *coroots*.
For the roots, definitely yes.

> Nicolas requested a doctest. See:
> http://groups.google.com/group/sage-combinat-devel/msg/4004c4a8471f3cfa?hl=en&pli=1
> I did this. I put the new doctest in type_reducible.py.

Thanks!


---

Attachment


---

Comment by bump created at 2009-04-23 01:27:08

Revised: WeylCharacterRing derives the name of its Cartan Type from its Cartan Type's `__repr__` method.


---

Comment by bump created at 2009-05-01 16:29:32

This ticket may be closed if trac_5794-revised.patch is merged. See #5794.


---

Comment by mvngu created at 2009-08-26 21:18:29

Closing this ticket as a duplicate of #5794.


---

Comment by mvngu created at 2009-08-26 21:18:29

Resolution: duplicate
