# Issue 2780: factorisation over number field has wrong unit part

Issue created by migration from https://trac.sagemath.org/ticket/2780

Original creator: dmharvey

Original creation time: 2008-04-02 21:39:35

Assignee: somebody

When factoring a multivariate polynomial over a number field, the unit part of the factorisation is reported incorrectly:


```
sage: K.<a> = NumberField(x^2 + 1)
sage: R.<y, z> = PolynomialRing(K)
sage: f = 2*y^2 + 2*z^2
sage: F = f.factor(); F
2 * (y + (-a)*z) * (y + a*z)
sage: F.unit_part()
1
```


The unit part should be 2.

Reported by Genya Zaytman.

See also: http://groups.google.com/group/sage-devel/browse_thread/thread/cc519fe6a67ff9e



---

Comment by mabshoff created at 2008-04-03 08:54:24

Changing component from basic arithmetic to factorization.


---

Comment by mabshoff created at 2008-04-03 08:54:24

Changing assignee from somebody to tbd.


---

Attachment

See the patch.


---

Comment by mhansen created at 2008-04-12 07:22:58

Looks good to me.


---

Comment by mabshoff created at 2008-04-12 11:23:53

Merged in Sage 3.0.alpha4


---

Comment by mabshoff created at 2008-04-12 11:23:53

Resolution: fixed
