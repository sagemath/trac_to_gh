# Issue 5702: make "make check" & friends doctest the documentation too

Issue created by migration from https://trac.sagemath.org/ticket/5702

Original creator: mabshoff

Original creation time: 2009-04-06 23:18:03

Assignee: mabshoff

Right now the various make check targets do not test the documentation. Fix that.

Patch coming up.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-06 23:18:09

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-04-16 09:15:52

Note that this patch is a traditional patch since the file in question is not under version control.

Cheers,

Michael


---

Attachment


---

Comment by craigcitro created at 2009-04-16 10:05:46

Looks good -- these are the same paths occurring in `sage/local/bin/sage-maketest`, which gives me a lot of confidence.


---

Comment by mabshoff created at 2009-04-16 10:20:11

Resolution: fixed


---

Comment by mabshoff created at 2009-04-16 10:20:11

Merged in Sage 3.4.1.rc3.

Cheers,

Michael
