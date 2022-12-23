# Issue 3078: [with patch; needs review] sage's spkg-install doesn't return failure if build failed

Issue created by migration from https://trac.sagemath.org/ticket/3078

Original creator: wjp

Original creation time: 2008-05-02 10:44:38

Assignee: mabshoff

If `sage -ba-force` failed, `spkg-install` accidentally returns the return value of an `echo` command.


---

Attachment


---

Comment by mabshoff created at 2008-05-02 11:55:02

Merged in Sage 3.0.1.rc0


---

Comment by mabshoff created at 2008-05-02 11:55:02

Resolution: fixed
