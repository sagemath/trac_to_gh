# Issue 3976: [with patch, needs review] improve doctests to expect.py, maxima.py, and lie.py

Issue created by migration from https://trac.sagemath.org/ticket/3976

Original creator: mhansen

Original creation time: 2008-08-28 19:39:29

Assignee: was




---

Attachment


---

Comment by rlm created at 2008-08-28 22:06:24

After discussion with mhansen, we decided it would be better to use `os.popen` instead of `os.system`, in order to remove many `#not tested` bits.


---

Attachment


---

Attachment

The patches apply cleanly (with some light fuzz for the first patch), and pass all tests. Apply this.


---

Comment by mabshoff created at 2008-08-28 22:57:14

Merged all three patches in Sage 3.1.2.alpha2


---

Comment by mabshoff created at 2008-08-28 22:57:14

Resolution: fixed
