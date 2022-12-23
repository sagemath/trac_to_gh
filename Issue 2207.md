# Issue 2207: fcp for matrices over SR

Issue created by migration from https://trac.sagemath.org/ticket/2207

Original creator: jason

Original creation time: 2008-02-18 21:25:50

Assignee: was




---

Comment by jason created at 2008-02-18 21:26:07

tidbits from mhansen's patch at 2028.


---

Comment by jason created at 2008-02-18 21:26:29

Changing type from defect to enhancement.


---

Attachment


---

Comment by ncalexan created at 2008-02-19 00:28:42

Apply.


---

Comment by mabshoff created at 2008-02-19 15:07:13

Please rebase:

```
sage$ patch -p1 --dry-run < trac-2028-part1.patch
patching file sage/matrix/matrix_symbolic_dense.pyx
Hunk #1 FAILED at 365.
1 out of 1 hunk FAILED -- saving rejects to file sage/matrix/matrix_symbolic_dense.pyx.rej
```


Cheers,

Michael


---

Comment by mhansen created at 2008-03-05 00:38:31

This code made it in in #2053.


---

Comment by mhansen created at 2008-03-05 00:38:31

Resolution: fixed


---

Comment by mhansen created at 2008-03-05 01:09:01

Resolution changed from fixed to 


---

Comment by mhansen created at 2008-03-05 01:09:01

Changing status from closed to reopened.


---

Attachment

New patch against 2.10.3.rc1 attached which adds missing doctests


---

Comment by mabshoff created at 2008-03-05 05:35:27

Merged in Sage 2.10.3.rc2 - due to some hg stupidity parts of this patch made it in rc0. Mike Hansen's latest patch adds the missing docstring and doctest.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-05 05:35:27

Resolution: fixed


---

Comment by cremona created at 2008-03-05 22:08:30

When I tested 2.10.3.rc2 I got this:


```
sage -t  devel/sage-main/sage/matrix/matrix_symbolic_dense.pyxemacs devel/sage-main/sage/matrix/matrix_symbolic_dense.pyx**********************************************************************
File "matrix_symbolic_dense.pyx", line 871:
    sage: list(a.fcp())
Expected:
    [(x^2 - 65*x - 250, 1), (x, 3)]
Got:
    [(x, 3), (x^2 - 65*x - 250, 1)]
**********************************************************************
```


and I suggest changing line 871 from

```
            sage: list(a.fcp())
```

to

```
            sage: sorted(list(a.fcp()))
```

