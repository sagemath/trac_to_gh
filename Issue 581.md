# Issue 581: apply LinBox's Changeset 2803 - this removes the workaround for #498 and fixes the problem itself

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-09-03 16:39:24

Assignee: mabshoff

See http://groups.google.com/group/linbox-use/t/513b47fcedb0f736 for details.

Cheers,

Michael


---

Comment by mabshoff created at 2007-09-03 16:39:30

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-09-03 16:40:14

The diff itself can be downloaded from http://linalg.org/projects/linalg/changeset/2803


---

Comment by mabshoff created at 2007-09-03 19:23:20

By the way: The fix for #498 never made it into 2.8.3:

```
sage: M=Matrix(Integers(),20,20,L)
sage: M.det()
ERROR in reconstruction ?

0
sage: M.rank()
20
sage:
```

William, do you have a clue what happened to the fixed spkg? I certainly send you a link. The SPKG.txt also doesn't contain my change log entry.

Cheers,

Michael


---

Comment by mabshoff created at 2007-09-03 19:41:48

A new spkg with ChangeSet 2803 applied can be found at 

http://fsmath.mathematik.uni-dortmund.de/~mabshoff/sage/linbox-20070903.spkg

Cheers,

Michael


---

Comment by was created at 2007-09-04 01:52:04

applied and tested


---

Comment by was created at 2007-09-04 01:52:04

Resolution: fixed
