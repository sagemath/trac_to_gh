# Issue 6194: [with patch, needs review] fixes for sage.symbolic.pynac.py_mod

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2009-06-03 15:16:05

Assignee: burcin

CC:  mhansen

Our version of GiNaC's mod function doesn't match the behavior of the original and fails silently when there is an error. This stops some simplifications such as `exp(2*pi*I) -> 1` to work.

Attached patch fixes these issues.


---

Attachment

fix to sage.symbolic.pynac.py_mod


---

Comment by mhansen created at 2009-06-05 02:03:22

Looks good to me.

Merged in 4.0.1.rc2.


---

Comment by mhansen created at 2009-06-05 02:03:22

Resolution: fixed
