# Issue 2055: [with patch, needs review] MPolynomialRing(BooleanPolynomial)

Issue created by migration from https://trac.sagemath.org/ticket/2055

Original creator: malb

Original creation time: 2008-02-05 15:09:15

Assignee: malb

CC:  burcin


```
sage: B.<x,y,z> = BooleanPolynomialRing(3)
sage: P.<x,y,z> = MPolynomialRing(QQ,3)
sage: P(B.gen(0))
x
```



---

Attachment


---

Comment by malb created at 2008-02-14 23:35:59

fixes an exposed sigsegv in libsingular interface


---

Attachment

This should be applied.

The `__call__` method is not as general as it could be.  See ticket #2165 for an enhancement.


---

Comment by mabshoff created at 2008-02-15 00:20:27

Resolution: fixed


---

Comment by mabshoff created at 2008-02-15 00:20:27

Merged in Sage 2.10.2.alpha0
