# Issue 1722: Symbolic Matrices should be callable.

Issue created by migration from https://trac.sagemath.org/ticket/1722

Original creator: boothby

Original creation time: 2008-01-08 19:11:43

Assignee: was

Matrices of symbolic objects should either be callable, or support substitution, per user request at conference.


---

Comment by mhansen created at 2008-01-27 01:17:49

Changing assignee from was to mhansen.


---

Comment by mhansen created at 2008-01-27 01:17:49

Changing status from new to assigned.


---

Comment by ncalexan created at 2008-02-15 05:17:29

Great doctests, good comments, looks good to me.  I say apply.


---

Comment by mabshoff created at 2008-02-15 05:20:49

Against my 2.10.2.alpha0 I get a reject:

```
patch -p1 --dry-run < trac_1722.patch
patching file sage/matrix/matrix_symbolic_dense.pxd
patching file sage/matrix/matrix_symbolic_dense.pyx
Hunk #1 succeeded at 15 with fuzz 2 (offset 9 lines).
Hunk #2 succeeded at 48 with fuzz 2 (offset 8 lines).
Hunk #3 succeeded at 536 (offset 248 lines).
Hunk #4 FAILED at 617.
Hunk #5 FAILED at 681.
2 out of 5 hunks FAILED -- saving rejects to file sage/matrix/matrix_symbolic_dense.pyx.rej
```

The patch should be rebased against 2.10.2.alpha0 once it is out.

Cheers,

Michael


---

Attachment


---

Comment by mhansen created at 2008-02-27 20:16:46

New rebased patch attached.


---

Comment by mabshoff created at 2008-02-28 00:43:14

Merged in Sage 2.10.3.rc0


---

Comment by mabshoff created at 2008-02-28 00:43:14

Resolution: fixed
