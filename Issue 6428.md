# Issue 6428: Large exponents overflow to negative in polydict ring

Issue created by migration from Trac.

Original creator: broune

Original creation time: 2009-06-26 18:26:31

Assignee: tbd

Large exponents overflow to negative in polydict ring:

sage: from sage.rings.polynomial.multi_polynomial_ring import \
...       MPolynomialRing_polydict
sage: ring = MPolynomialRing_polydict(ZZ, 3, ['a','b','c'], "lex")
sage: a = ring.gens()[0]

sage: a<sup>(2</sup>31-1)
a^2147483647

sage: a<sup>(2</sup>31)
a^-2147483648

sage: a<sup>(2</sup>32)
1


---

Comment by broune created at 2009-06-26 18:29:07

Fixed layout.


---

Comment by AlexGhitza created at 2009-11-15 13:14:19

Changing component from algebra to commutative algebra.


---

Comment by was created at 2010-01-18 01:39:18

This is still a bug.   Ick!


```
sage: R.<y,z> =Frac(QQ['x'])[]
sage: y^(2^32)
1
sage: y^(2^32-1)
y^-1
sage: y^(2^31)
y^-2147483648
```



---

Comment by was created at 2010-01-18 09:59:31

Here is better input to replicate what is at the core of the problem:

```
sage: a = sage.rings.polynomial.polydict.PolyDict({(2147483647r,):1r})
sage: a*a
PolyDict with representation {(-2,): 1}
```



---

Attachment


---

Comment by was created at 2010-01-18 10:19:29

Changing status from new to needs_review.


---

Comment by broune created at 2010-01-18 18:58:53

This patch simply reports an error if this happens. I thought the polydict ring was supposed to allow arbitrary precision exponents.


---

Comment by was created at 2010-01-18 22:35:52

> This patch simply reports an error if this happens. I thought the polydict
> ring was supposed to allow arbitrary precision exponents. 

Since in the entire Cython implementation of polydict, the exponents are represented internally as C ints there is no way it is supposed to represent arbitrary precision exponents.   One could write something that does arbitrary exponents, but that ETuple stuff simply isn't such a thing.


---

Comment by was created at 2010-01-18 22:37:03

By the way, for basic arithmetic, the symbolic ring supports arbitrary exponents. 


```
sage: var('y')
y
sage: y^(2^32)
y^4294967296
sage: y^(2^50)
y^1125899906842624
sage: y^(2^50+y)
y^(y + 1125899906842624)
```



---

Attachment

I added a new patch (to be applied instead of the old one) that also handles negative exponents. (The previous patch broke LaurentPolynomials).


---

Comment by spancratz created at 2010-01-21 00:57:18

This now passes all doctests.


---

Comment by spancratz created at 2010-01-21 01:02:16

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-01-23 09:05:39

Resolution: fixed


---

Comment by mvngu created at 2010-01-23 09:05:39

Merged [6428_ETuple_overflow.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6428/6428_ETuple_overflow.patch).
