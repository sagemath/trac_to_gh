# Issue 8762: the sparse=True flag is horribly broken for GF(p)[x]

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-04-25 07:17:01

Assignee: AlexGhitza


```
On Apr 24, 2010, at 5:36 PM, Michael Rybalkin wrote:

How to get monomial with large exponent in the polynomial rings?

For example I hsave polynomial ring over large finite field:
p = next_prime(10^20)
R.<x> = PolynomialRing(GF(p), sparse=True)

Monomial x^(10^7) construction takes 2 seconds:
time tmp = x^(10^7)

Monomial x^(10^8) construction uses all 6 Gb server memory and cannot
finish.
And without 'sparse=True' option I cannot even get x^(10^6).

What is the limitations for monomial exponents in polynomial rings?
What can be done in my case? For example GAP handles this case without
any problem.

Seems like the sparse=True flag is horribly broken for GF(p)[x]:

sage: p = next_prime(10^20)
sage: R.<x> = PolynomialRing(GF(p), sparse=True)
sage: type(x)
<type 'sage.rings.polynomial.polynomial_zz_pex.Polynomial_ZZ_pEX'>

sage: R.<x> = PolynomialRing(QQ, sparse=True)
sage: x^(10^8)
x^100000000


- Robert Bradshaw
```



---

Comment by ylchapuy created at 2010-08-09 21:44:57

it also broken for pAdics. see `_single_variable` in `rings/polynomial/polynomial_ring.py` not taking care of the `sparse` argument.


---

Comment by jsrn created at 2010-09-13 13:23:35

I don't have the grand overview of this, but it seems that simply adding the condition to only use NTL whenever sparse=False works and was the original intention. I'm uploading the (simple) patch for this, so you can see what I mean.

Cheers
Johan


---

Comment by ylchapuy created at 2010-09-17 07:28:16

This patch seems ok to me, but could you please add some doctest to show the bug is gone?

I also opened another ticket for the pAdics problem ( #9929 ).


---

Comment by jsrn created at 2010-09-17 07:48:43

Sure - I should have done that to begin with.


---

Comment by jsrn created at 2010-09-17 07:48:43

Changing status from new to needs_review.


---

Attachment

Only use NTL with non-sparse polynomial rings over finite fields. Now with doctest.


---

Comment by ylchapuy created at 2010-09-25 11:24:33

Changing status from needs_review to positive_review.


---

Comment by ylchapuy created at 2010-09-25 11:24:33

Ok for me.


---

Comment by mpatel created at 2010-09-29 08:39:18

Resolution: fixed
