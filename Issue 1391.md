# Issue 1391: bug in unit part of factorizations of multivariate polynomials

Issue created by migration from https://trac.sagemath.org/ticket/1391

Original creator: was

Original creation time: 2007-12-04 04:38:52

Assignee: malb

Behold this behavior:


```
sage: R.<a,b,c,d> = QQ[]
sage: f =  (-1) * (a - d) * (-a + b) * (b - d) * (a - c) * (b - c) * (c - d)
sage: f.factor()
(-1) * (a - d) * (-a + b) * (b - d) * (a - c) * (b - c) * (c - d)
sage: F = f.factor()
sage: F[0][0]
-1
sage: F.unit_part ()
1
```


However it should be that F.unit_part() is -1 and F[0][0] is a-d.


---

Comment by mabshoff created at 2007-12-26 03:30:56

Bug Day material?

Cheers,

Michael


---

Attachment


---

Comment by malb created at 2008-01-16 17:09:38

The attached patch fixes the issue


---

Comment by ncalexan created at 2008-01-19 22:08:27

Patch looks reasonable.  The parameter to factor() is not standard sage but seems appropriate.  I say apply!


---

Comment by mabshoff created at 2008-01-20 02:05:55

The patch no longer applies to me in 2.10.1.alpha0, so it probably needs just a rebase:

```
sage-2.10.1.alpha0/devel/sage$ patch -p1 --dry-run < trac_1391.patch
patching file sage/rings/polynomial/multi_polynomial_libsingular.pyx
Hunk #1 FAILED at 3096.
Hunk #2 succeeded at 3159 (offset 22 lines).
1 out of 2 hunks FAILED -- saving rejects to file sage/rings/polynomial/multi_polynomial_libsingular.pyx.rej
```

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2008-01-20 02:36:50

Merged in Sage 2.10.1.alpha0


---

Comment by mabshoff created at 2008-01-20 02:36:50

Resolution: fixed
