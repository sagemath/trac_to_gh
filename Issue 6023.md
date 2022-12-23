# Issue 6023: Bring plot/polygon.py to 100% coverage

Issue created by migration from https://trac.sagemath.org/ticket/6023

Original creator: kcrisman

Original creation time: 2009-05-12 00:25:25

Assignee: tba

Bring plot/polygon.py to 100% coverage.


---

Attachment

Also improves plot3d function.

See [http://groups.google.com/group/sage-devel/browse_thread/thread/1adac4035031b140/c36f1f8a7c8a9b43#c36f1f8a7c8a9b43](http://groups.google.com/group/sage-devel/browse_thread/thread/1adac4035031b140/c36f1f8a7c8a9b43#c36f1f8a7c8a9b43) for why there is no loads(dumps()) doctest.


---

Comment by mvngu created at 2009-05-13 04:41:24

Same issues as per [my comment](http://trac.sagemath.org/sage_trac/ticket/6006#comment:4) at #6006.


---

Comment by mabshoff created at 2009-05-13 17:20:05

No, the issue with `__init__` not showing up in the documentation will be fixed in the future, i.e. sphinx 0.6.

Cheer,s

Michael


---

Comment by kcrisman created at 2009-05-14 15:34:28

Changing assignee from tba to kcrisman.


---

Comment by kcrisman created at 2009-05-14 15:34:28

Changing status from new to assigned.


---

Attachment

Positive review! Apply patches in the following order:
 1. `trac_6023.patch`
 1. `trac_6023-fix.patch`


---

Comment by mabshoff created at 2009-05-15 07:55:08

Merged both patches in Sage 4.0.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-15 07:55:08

Resolution: fixed
