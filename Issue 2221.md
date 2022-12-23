# Issue 2221: Silent failure of sage-env

Issue created by migration from https://trac.sagemath.org/ticket/2221

Original creator: gfurnish

Original creation time: 2008-02-20 06:29:55

Assignee: mabshoff

source sage-env currently fails silently to change $SAGE_ROOT if it is already set to a different directory.  This patch prints a warning message if sage-env should have changed $SAGE_ROOT but did not.  


---

Attachment


---

Comment by mabshoff created at 2008-02-20 10:22:24

Patch looks good and solves a long standing annoyance. We might even go so far to not only print a warning, but to also exit since the warning might just fly by.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-20 10:22:58

Resolution: fixed


---

Comment by mabshoff created at 2008-02-20 10:22:58

Merged in Sage 2.10.2.alpha2
