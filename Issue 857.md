# Issue 857: update info about cython in license() output

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2007-10-12 03:12:23

Assignee: tba

In 2.8.6, license() still talks about pyrex/sagex, not cython



---

Comment by mabshoff created at 2007-10-19 19:26:32

This ought to be easily done during Bug Day 4.

Cheers,

Michael


---

Comment by mabshoff created at 2007-10-19 19:26:32

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-10-19 19:26:32

Changing assignee from tba to mabshoff.


---

Attachment


---

Comment by mabshoff created at 2007-12-22 11:39:23

This is COPYING.txt from 2.9.1.alpha3, where I made the following changes:

 * rename pyrex/sagex to cython
 * add flint
 * update singular's license section to the lastest version shipped with 3-0-4

Cheers,

Michael


---

Comment by rlm created at 2007-12-22 17:38:02

Resolution: fixed


---

Comment by rlm created at 2007-12-22 17:38:02

I updated the sagex/pyrex description part also, and moved it to its place. I added a description for flint.
