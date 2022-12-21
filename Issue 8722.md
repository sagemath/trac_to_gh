# Issue 8722: S-units sometimes broken and sometimes just plain wrong for relative fields

Issue created by migration from Trac.

Original creator: davidloeffler

Original creation time: 2010-04-20 09:09:57

Assignee: davidloeffler


```
sage: L.<a,b> = NumberField([x^2 + 1, x^2 - 5])
sage: p = L.ideal((-1/2*b - 1/2)*a + 1/2*b - 1/2)
sage: p.absolute_norm()
9
sage: p.is_prime()
True
sage: W = L.S_units([p]); W
[1/2*a + 7/4, a, 1/2*b - 1/2]
sage: W[0].valuation(L.primes_above(2)[0])
-4
```

So the first element of the list of S-units isn't actually an S-unit! In other examples the code just blows up, because it calls `residue_field` and that dies because of #8721:

```
sage: L.<a, b> = NumberField([polygen(QQ)^2 - 3, polygen(QQ)^2 - 5])
sage: L.S_units([L.ideal(a)])
```

This is arguably less bad: raising an error is far better than silently a wrong answer.


---

Comment by davidloeffler created at 2010-04-20 09:52:42

Here's a patch. Turns out that the code was using `K.gen` and the correct answer is to call `K.absolute_generator`, which isn't the same in the above example. This fixes the first example; the second is an instance of #8721.


---

Comment by davidloeffler created at 2010-04-20 09:52:42

Changing status from new to needs_review.


---

Attachment

apply over patches at #8446


---

Comment by cremona created at 2010-04-21 08:36:52

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2010-04-21 08:36:52

Looks good, applied fine to 4.4.alpha0 + #8446 patches, and all tests in sage/rings/number_field pass.

Positive review!


---

Comment by jhpalmieri created at 2010-04-23 17:09:40

Resolution: fixed


---

Comment by jhpalmieri created at 2010-04-23 17:09:40

Merged into 4.4.alpha2.
