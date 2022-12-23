# Issue 9206: faster finite field creation with proof=False, done right (via proof architecture)

Issue created by migration from https://trac.sagemath.org/ticket/9206

Original creator: was

Original creation time: 2010-06-10 19:59:00

Assignee: AlexGhitza




---

Comment by was created at 2010-07-07 20:10:23

This example illustrates the effect of this patch:

```
sage: time GF(next_prime(10^40)^5,'a')
CPU times: user 0.51 s, sys: 0.00 s, total: 0.52 s
Wall time: 0.52 s
Finite Field in a of size 10000000000000000000000000000000000000121^5
sage: proof.arithmetic(False)
sage: time GF(next_prime(10^40)^5,'a')
CPU times: user 0.07 s, sys: 0.00 s, total: 0.07 s
Wall time: 0.07 s
Finite Field in a of size 10000000000000000000000000000000000000121^5
```


Unfortunately, it does *not* address this problem that David Harvey mentioned.  However, it has a similar "flavor":


```
sage: R.<x> = PolynomialRing(Integers(16219299585*2^16612 - 1))
```

David Harvey: "Maybe not literally forever, but I got sick of waiting. Should be instantaneous."


---

Attachment

I didn't write the attached patch, but I polished it up, so it would be good if somebody else could sign off on this.  I'm OK with it, as is.


---

Comment by was created at 2010-07-07 20:12:53

Changing status from new to needs_review.


---

Comment by robertwb created at 2010-07-08 03:18:11

Changing status from needs_review to positive_review.


---

Comment by robertwb created at 2010-07-08 03:18:11

Looks good to me.


---

Comment by mpatel created at 2010-07-20 09:20:45

Resolution: fixed
