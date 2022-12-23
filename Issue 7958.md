# Issue 7958: Conversion of rationals into the fraction field of integer polynomials

Issue created by migration from https://trac.sagemath.org/ticket/7958

Original creator: spancratz

Original creation time: 2010-01-16 19:28:41

Assignee: AlexGhitza


```
sage: F = Frac(PolynomialRing(ZZ, 't'))
sage: F(1/2)
...
TypeError: no conversion of this rational to integer
```



---

Comment by spancratz created at 2010-01-16 19:29:45

Changing assignee from AlexGhitza to robertwb.


---

Comment by spancratz created at 2010-01-16 19:29:45

Changing component from algebra to coercion.


---

Attachment


---

Comment by spancratz created at 2010-01-16 21:30:13

Changing status from new to needs_review.


---

Comment by wjp created at 2010-01-17 17:50:30

Your fix does work great for QQ, but this is actually a more general issue than just QQ:


```
sage: _.<x> = ZZ[]
sage: K.<a> = NumberField(x^2-2)
sage: R.<b> = K.ring_of_integers()
sage: S.<y> = R[]
sage: F = FractionField(S)
sage: F(1)/F(a)
1/a
sage: F(1/a)
*boom*
```


And a minor issue: I think the comment about QQ should be a code comment rather than in the doctest, since it might now confuse users (who might think they need to handle QQ specially themselves).


---

Comment by wjp created at 2010-01-17 17:50:30

Changing status from needs_review to needs_work.


---

Attachment


---

Comment by spancratz created at 2010-01-17 21:45:52

To see that this issue is now resolved (for rationals and number fields), consider

```
sage: _.<x> = ZZ[]
sage: K.<a> = NumberField(x^5-3*x^4+2424*x^3+2*x-232)
sage: R.<b> = K.ring_of_integers()
sage: S.<y> = R[]
sage: F = Frac(S)
sage: F(1/a)
a^4 - 3*a^3 + 2424*a^2 + 2/232
sage: F(1/a).numerator()
a^4 - 3*a^3 + 2424*a^2 + 2
sage: F(1/a).denominator()
232
```


But the last three lines highlight a bug in the printing routines.


---

Comment by spancratz created at 2010-01-17 21:45:52

Changing priority from minor to major.


---

Comment by spancratz created at 2010-01-17 21:45:52

Changing status from needs_work to needs_review.


---

Attachment


```

sage: _.<x> = ZZ[]
sage: K.<a> = NumberField(x^5-3*x^4+2424*x^3+2*x-232)
sage: R.<b> = K.ring_of_integers()
sage: S.<y> = R[]
sage: F = Frac(S)
sage: F(1/a)
a^4 - 3*a^3 + 2424*a^2 + 2/232
sage: F(1/a).numerator()
a^4 - 3*a^3 + 2424*a^2 + 2
sage: F(1/a).denominator()
232

```



---

Comment by mhansen created at 2010-01-20 04:28:41

Combined version of the above patches.


---

Attachment


---

Comment by spancratz created at 2010-01-20 07:19:15

Applying the two patches

- trac7958.2.patch
- trac_7958-atomic.patch

this applies cleanly and passes all doctests.


---

Comment by spancratz created at 2010-01-20 07:19:15

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-01-23 07:47:55

Resolution: fixed


---

Comment by mvngu created at 2010-01-23 07:47:55

Merged patches in this order:

 1. [trac7958.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7958/trac7958.2.patch)
 1. [trac_7958-atomic.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7958/trac_7958-atomic.patch)
