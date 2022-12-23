# Issue 9205: Discrete logs to composite bases

Issue created by migration from https://trac.sagemath.org/ticket/9205

Original creator: davidloeffler

Original creation time: 2010-06-10 14:11:02

Assignee: was

At present, we have a discrete log function which claims to work for Z/NZ when this group is cyclic, but it can be wrong when N is not prime, as in this example:

```
sage: Mod(5,9).log(Mod(2, 9))
6
sage: sage: discrete_log(Mod(5, 9), Mod(2, 9))
5
```


The first answer is totally wrong, because Pari's znlog function is intended to be used with a prime modulus and silently returns junk in the non-prime case.

I need to be able to express elements of Z/NZ* in terms of generators in the non-cyclic case anway, so I will fix this in the process.


---

Comment by davidloeffler created at 2010-06-10 14:41:53

patch against 4.4.4.alpha0


---

Comment by davidloeffler created at 2010-06-10 14:43:26

Changing status from new to needs_review.


---

Attachment

Here's a patch. It fixes the "log" method so it returns the right answer when the multiplicative group is cyclic, and adds a new method (I called this "generalised log" -- I didn't know what else to call it) which returns a vector of exponents with respect to the generators of the unit group.


---

Comment by cremona created at 2010-06-23 16:14:56

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2010-06-23 16:14:56

Looks fine, applies to 4.4.4.alpha1 also and tests in rings/finite_rings pass.


---

Comment by davidloeffler created at 2010-06-30 19:03:21

apply over previous patch


---

Attachment

Replying to [comment:2 cremona]:
> Looks fine, applies to 4.4.4.alpha1 also and tests in rings/finite_rings pass.

... but one of the doctest in sage/functions/log doesn't. Here's a tiny patch that fixes that.


---

Comment by mpatel created at 2010-07-20 07:18:59

Resolution: fixed
