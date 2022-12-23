# Issue 4628: [with patch; needs review] sage-3.2.1.alpha1 -- setup.py build system is foobar'd

Issue created by migration from https://trac.sagemath.org/ticket/4628

Original creator: was

Original creation time: 2008-11-26 22:33:45

Assignee: mabshoff




---

Attachment


---

Comment by craigcitro created at 2008-11-26 23:13:09

Yep, this is exactly the right fix. As one can see from the comments in the original code, I had intended to pass the module along -- I apparently just forgot to finish. Oops.


---

Comment by mabshoff created at 2008-11-27 02:02:47

Merged in Sage 3.2.1.alpha2


---

Comment by mabshoff created at 2008-11-27 02:02:47

Resolution: fixed
