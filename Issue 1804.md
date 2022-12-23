# Issue 1804: Factorization.__mul__ assumes that the primes in the factorization commute, which may not be a valid assumption

Issue created by migration from https://trac.sagemath.org/ticket/1804

Original creator: was

Original creation time: 2008-01-17 19:52:14

Assignee: somebody

This is LAME:


```
sage: R.<x,y> = FreeAlgebra(QQ, 2)
sage: F = Factorization([(x,3), (y,2)]); F
x^3 * y^2
sage: F*F
x^6 * y^4
```



---

Comment by was created at 2008-01-17 19:57:48

Same comments apply to __invert__ in the file factorization.py.  

```
sage: R.<x,y> = FreeAlgebra(QQ, 2)
sage: F = Factorization([(x,3), (y,2)]); F
x^3 * y^2
sage: F^(-1)
x^-3 * y^-2

```



---

Attachment


---

Comment by mhansen created at 2008-01-21 02:04:22

Looks good to me.


---

Comment by mabshoff created at 2008-01-21 02:10:09

Resolution: fixed


---

Comment by mabshoff created at 2008-01-21 02:10:09

Merged in Sage 2.10.1.alpha1
