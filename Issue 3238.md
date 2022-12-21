# Issue 3238: [with patch; needs review] libfpll spkg -- update to work with cygwin

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-05-17 16:00:30

Assignee: mabshoff

This was completely straightforward

   http://sage.math.washington.edu/home/was/cygwin/libfplll-2.1.6-20071129.p4.spkg


---

Comment by mabshoff created at 2008-05-18 13:19:21

Spkg looks good. I updated the fplll.h.patch to reflect the latest diff. In addition I send the fix upstream so that we do not have to patch this once the new upstream libfplll is released.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-18 13:19:53

Merged in Sage 3.0.2.alpha1


---

Comment by mabshoff created at 2008-05-18 13:19:53

Resolution: fixed
