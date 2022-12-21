# Issue 713: [with patch] Interrupting Singular doesn't work

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2007-09-20 18:31:26

Assignee: was

Consider

```
sage: P = PolynomialRing(QQ,10,'x')
sage: I = sage.rings.ideal.Katsura(P)
sage: I.groebner_basis() # forever!
```

Ctrl-C does not interrupt nor kill the Singular process doing the hard work. The attached patch fixes that.


---

Attachment


---

Comment by was created at 2007-09-20 18:57:02

Resolution: fixed
