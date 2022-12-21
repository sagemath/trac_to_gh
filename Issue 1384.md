# Issue 1384: 2.8.15.rc0: fix numerical doctest fallout on PCC

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-12-03 19:10:19

Assignee: mabshoff

There are various doctest failures related to numerical noise and different order of result on PPC for

devel/sage-main/sage/rings/polynomial/complex_roots.py
devel/sage-main/sage/rings/polynomial/polynomial_element.pyx
devel/sage-main/sage/rings/qqbar.py

Patch coming shortly.

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2007-12-03 19:28:22

I needed another minimal fix for x86-64 Linux, but this is now in.

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-03 19:28:51

Merged in 2.8.15.rc1.


---

Comment by mabshoff created at 2007-12-03 19:28:51

Resolution: fixed
