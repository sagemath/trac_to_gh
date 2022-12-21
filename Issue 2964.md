# Issue 2964: Improvements to weyl_group.py

Issue created by migration from Trac.

Original creator: bump

Original creation time: 2008-04-20 03:51:15

Assignee: mhansen

CC:  sage-combinat

WeylGroup gets a proper __call__ method that produces a WeylGroup element. Previously if G is a Weyl group then G(m) produced a MatrixRing element. This part is a bugfix.

Root systems get a method to produce the highest root, relevant to the affine root system. This could be
implemented as a case-by-case method and that would be faster, but searching through the roots for
the highest weight is of acceptable speed.

Weyl Groups get a method to produce the long element of the Weyl group. Not implemented yet for E7 and E8.

Weyl group also gets a method to produce the identity element as a WeylGroup element. Strictly speaking this is
not necessary since W(1) will also produce the unit.


---

Attachment


---

Attachment

These are patches against 3.0alpha6.


---

Comment by bump created at 2008-04-20 04:02:05

There will be a further patch because I forgot to finish the doctests.


---

Comment by mhansen created at 2008-04-20 04:05:36

Okay, excellent.  I'll review them when you put them up.


---

Attachment


---

Comment by bump created at 2008-04-20 04:08:58

I added a third patch with doctest for long element and now I think it is OK.

Thanks, Dan


---

Attachment


---

Comment by mhansen created at 2008-04-20 05:51:57

Looks good to me. Apply all four patches.


---

Comment by mabshoff created at 2008-04-20 06:20:10

Resolution: fixed


---

Comment by mabshoff created at 2008-04-20 06:20:10

Merged all four patches in Sage 3.0.rc0
