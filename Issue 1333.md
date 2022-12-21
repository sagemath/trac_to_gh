# Issue 1333: [with trivial patch] fix a major inefficiency in floating point square root computation in Sage

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-11-29 06:53:50

Assignee: somebody

Paul Zimmerman's benchmarks unveiled a serious slowdown in x.sqrt() for x mpfr.

This patch fixes the problem. 


---

Attachment


---

Comment by cwitty created at 2007-12-01 03:27:20

(I didn't actually test it, but...) looks good to me.


---

Comment by mabshoff created at 2007-12-01 18:21:31

Resolution: fixed


---

Comment by mabshoff created at 2007-12-01 18:21:31

Merged in 2.8.15.alpha1.
