# Issue 3431: [with patch, needs review] QEPCAD interface

Issue created by migration from https://trac.sagemath.org/ticket/3431

Original creator: cwitty

Original creation time: 2008-06-15 21:46:21

Assignee: was

CC:  burcin

Keywords: editor_cwitty

This provides an extensive Sage interface to QEPCAD.  (The patch was formerly posted on #772; we're moving it here to keep one issue per ticket.)


---

Attachment


---

Comment by cwitty created at 2008-06-15 22:17:33

Changing type from defect to enhancement.


---

Comment by jason created at 2008-08-16 21:38:47

This patch looks very nice and seems to behave as advertised.  There are some doctests that should be updated for qepcad 1.50 and also for the new interval printing notation in Sage 3.1.  Positive review pending fixing those things.


---

Attachment

I've attached a patch to update the qepcad interface to deal with the newest interval printing, and to avoid locking the interface to one particular version of qepcad.

Note that this patch depends on #3910 (without #3910, one doctest will fail).


---

Comment by jason created at 2008-08-27 17:08:55

With the newest qepcad spkg up at #772, all doctests in qepcad.py pass on sage 3.1.2alpha1.  It looks good to me.


---

Comment by mabshoff created at 2008-08-28 02:54:29

Merged both patches in Sage 3.1.2.alpha2


---

Comment by mabshoff created at 2008-08-28 02:54:29

Resolution: fixed
