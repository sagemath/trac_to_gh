# Issue 2733: PARI in Debian has the mathnf bug

Issue created by migration from https://trac.sagemath.org/ticket/2733

Original creator: tabbott

Original creation time: 2008-03-30 05:14:16

Assignee: tabbott

Is this bug important enough to bother Bill Allombert (the maintainer of PARI in Debian) to upgrade PARI in Debian?

sage -t  devel/sage-main/sage/matrix/tests.py               **********************************************************************
File "tests.py", line 55:
    sage: a.mathnf(1)[1][1,] == gp('[4, 2, 1, 0, 3, 1, 1, 0, 1, 1, 2, 2, 3, 3, 0, 0, 1, 3]')
Expected:
    True
Got:
    False
**********************************************************************



---

Comment by mabshoff created at 2008-03-30 09:50:43

This is not "Sage Specific": This is a packaging bug in Debian's pari.deb and should be filed as a bug report at the Debian bug tracker. See http://wiki.sagemath.org/TracGuidelines for the rules that up to now weren't written down.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-30 09:50:43

Resolution: wontfix
