# Issue 7088: factoring certain polynomials over ZZ gets all mixed up (wrong constant) via our PARI wrapper

Issue created by migration from https://trac.sagemath.org/ticket/7088

Original creator: was

Original creation time: 2009-10-01 03:23:39

Assignee: somebody


```
Hi all,

Found this simple bug in a simple Z[x] factoring example.

R.<x>=PolynomialRing(ZZ)
f = 12*x^10 + x^9 + 432*x^3 + 9011
g = 13*x^11 + 89*x^3 + 1
F = f^2 * g^3
G = F.factor()
should_be_zero = F - G.prod()
should_be_zero == 0

The problem was that F.factor returns

2028 * (12*x^10 + x^9 + 432*x^3 + 9011)^2 * (13*x^11 + 89*x^3 + 1)^3

Not 1 * (12*x^10 + x^9 + 432*x^3 + 9011)^2 * (13*x^11 + 89*x^3 + 1)^3

```



---

Comment by robertwb created at 2009-10-01 06:36:21

Changing assignee from somebody to robertwb.


---

Attachment


---

Comment by mhansen created at 2009-10-01 07:49:05

I attached a patch with a one character change: ( TESTS:: to TESTS:).

Other than that, it looks good to me.


---

Comment by was created at 2009-10-02 17:47:15

Resolution: fixed
