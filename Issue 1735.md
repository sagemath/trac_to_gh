# Issue 1735: do not mark a spkg as installed if sage-check fails

Issue created by migration from https://trac.sagemath.org/ticket/1735

Original creator: mabshoff

Original creation time: 2008-01-09 11:16:51

Assignee: mabshoff

If `SAGE_CHECK` is exported as a non-empty string we run spkg-check per default if it is available. But if spkg-check fails we still mark the spkg as installed. This should obviously not happen.

Cheers,

Michael


---

Attachment


---

Comment by ncalexan created at 2008-01-13 01:52:10

+1 -- this should be applied.  Perhaps the error message could be abstracted to a function, for future use?


---

Comment by mabshoff created at 2008-01-13 02:00:51

The wording is slightly different, but it would still be a good idea to factor it out.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-13 02:01:09

Merged in Sage 2.10.alpha3.


---

Comment by mabshoff created at 2008-01-13 02:01:09

Resolution: fixed
