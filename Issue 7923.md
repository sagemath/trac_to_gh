# Issue 7923: signed int overflow in givaro elements' __pow__ method

Issue created by migration from https://trac.sagemath.org/ticket/7923

Original creator: roed

Original creation time: 2010-01-14 00:15:44

Assignee: AlexGhitza

When 2^31 < q^2 < 2^32, one can get an overflow in exponentiation (because of the use of signed vs unsigned ints).  This occurs for q=3^10.


```
sage: K.<a> = GF(3^10)
sage: b = a^9 + a^7 + 2*a^6 + a^4 + a^3 + 2*a^2 + a + 2
sage: b^(71*7381) == (b^71)^7381
False
```



---

Attachment


---

Comment by roed created at 2010-01-14 00:19:29

Changing status from new to needs_review.


---

Comment by roed created at 2010-01-14 15:23:11

This is based against 4.3.rc0 and the patch 7585_ALL.patch, but that will only change relative positioning, so it should apply with just a shift.


---

Comment by fwclarke created at 2010-01-16 10:16:08

Changing status from needs_review to positive_review.


---

Comment by fwclarke created at 2010-01-16 10:16:08

The code looks good, it does apply to 4.3, and it corrects the bug.  Positive review.


---

Comment by rlm created at 2010-01-18 23:45:35

Resolution: fixed
