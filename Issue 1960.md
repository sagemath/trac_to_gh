# Issue 1960: bug when reducing Gröbner basis

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-01-28 14:48:54

Assignee: malb

This bug was reported by James Carlson:


```
sage: R.<u,v> = PolynomialRing(QQ)
sage: g = u^4 + v^4 + u^3 + v^3
sage: I = ideal(g) + ideal(g.jacob())
sage: I.dimension()
0
sage: PD = I.primary_decomposition()
sage: len(PD)
1
sage: P = PD[0]
sage: I == P
True
sage: I.vector_space_dimension()
9 
sage: P.vector_space_dimension()
4 # <<<<<<<<<<<<< doesn't match
```



---

Attachment

In fact, the behaviour was correct in the sense that the specification (documentation) and the code agreed. However, this was at least counter intuitive. This method returned the vector space dimension of the ring modulo the leading terms of the generators of the ideal rather than modulo the ideal. This makes sense in the context of Singular where an ideal is identified with its generators but it doesn't make sense in the context of Sage where this identification is not true. Thus, now allways the vector space dimension of ring modulo the ideal is returned.


---

Comment by AlexGhitza created at 2008-01-31 01:37:58

Changes look good, and sage -t is happy.


---

Comment by mabshoff created at 2008-02-01 00:31:12

Merged in Sage 2.10.1.rc4


---

Comment by mabshoff created at 2008-02-01 00:39:21

Resolution: fixed


---

Comment by mabshoff created at 2008-02-01 00:39:21

Merged in Sage 2.10.1.rc4
