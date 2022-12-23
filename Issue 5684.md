# Issue 5684: [with patch, needs review] Taking negative powers of Laurent polynomial throws exception

Issue created by migration from https://trac.sagemath.org/ticket/5684

Original creator: wjp

Original creation time: 2009-04-04 20:40:48

Assignee: tbd

Taking negative powers of a Laurent polynomial doesn't currently work due to a typo in LaurentPolynomial_mpair.__pow__(). The attached patch fixes this.


```
sage: F.<t> = LaurentPolynomialRing(GF(3))
sage: (1+t)^(-1)
TypeError: fraction_field() takes no arguments (1 given)
```



---

Attachment


---

Comment by mabshoff created at 2009-04-13 01:49:40

Merged in Sage 3.4.1.rc3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-13 01:49:40

Resolution: fixed
