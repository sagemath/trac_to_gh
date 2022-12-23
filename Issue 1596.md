# Issue 1596: preparser hangs if line starts with ...

Issue created by migration from https://trac.sagemath.org/ticket/1596

Original creator: wjp

Original creation time: 2007-12-24 19:59:37

Assignee: was

As reported by 'Octoploid' on IRC: The preparser crashes if a line starts with '...'.

This is caused by a string index in preparse_ellipsis() becoming negative and wrapping to the end of the string.

Patch attached. This makes preparse('...') return 'Ellipsis'. Not sure if that's the desired behaviour. Maybe a syntax error would be better?


---

Attachment


---

Comment by wjp created at 2007-12-24 20:08:49

Changing priority from major to blocker.


---

Comment by wjp created at 2007-12-24 20:08:49

Changing component from algebraic geometry to user interface.


---

Attachment

This patch fixes the problem. 

I agree that a syntax error would be preferable, see second patch (to replace the first). I also made the error on [1..] more explicit.


---

Comment by mabshoff created at 2008-01-04 21:34:04

Looks good to me. Merged in Sage 2.9.2.rc1.


---

Comment by mabshoff created at 2008-01-04 21:34:04

Resolution: fixed
