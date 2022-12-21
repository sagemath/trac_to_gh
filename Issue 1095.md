# Issue 1095: [with patch] silly annoyance in sage -coverage

Issue created by migration from Trac.

Original creator: craigcitro

Original creation time: 2007-11-04 01:15:24

Assignee: craigcitro

I made a silly mistake when I was editing sage-coverage -- it will always tell you that a function is "possibly wrong" (i.e. function name doesn't occur in doctest) when there is no doctest; this is pretty obvious. This patch fixes it, so that now things only appear in the "possibly wrong" list if they *don't* appear in either of the other lists (missing documentation or missing doctests).


---

Attachment

bundle for $SAGE_ROOT/local/bin


---

Comment by mabshoff created at 2007-11-06 22:33:52

applied to 2.8.12.rc0


---

Comment by mabshoff created at 2007-11-06 22:33:52

Resolution: fixed
