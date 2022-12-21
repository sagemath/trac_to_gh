# Issue 2104: missing dependency: lcalc on mpfr

Issue created by migration from Trac.

Original creator: tabbott

Original creation time: 2008-02-08 08:27:26

Assignee: mabshoff

lcalc seems to link against mpfr, but doesn't depend on it in the spkg/standard/deps.


---

Attachment


---

Comment by mabshoff created at 2008-02-10 01:44:55

Patch looks good to me and fixes a real bug that we just don't hit due to luck. 

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-10 01:46:33

Resolution: fixed


---

Comment by mabshoff created at 2008-02-10 01:46:33

Merged in Sage 2.10.2.alpha0
