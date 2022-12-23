# Issue 9207: random_element does not work for BooleanPolynomialRing of degree 1 or 2

Issue created by migration from https://trac.sagemath.org/ticket/9207

Original creator: mariah

Original creation time: 2010-06-10 20:03:45

Assignee: malb

random_element does not work for BooleanPolynomialRing of degree 1 or 2; for example,


```
sage: n = 2
sage: S = BooleanPolynomialRing(n,'y','lex')
sage: S.random_element()
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
```



---

Attachment


---

Comment by malb created at 2010-07-12 15:53:34

Changing status from new to needs_review.


---

Comment by mariah created at 2010-07-13 14:13:08


```
This patch fixed the reported problem.

sage-4.4.4.1 with this patch pass all tests
when I do 'make testlong'

The patch code looks reasonable.

Positive review.
```



---

Comment by mariah created at 2010-07-13 14:13:08

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-07-21 01:45:41

Resolution: fixed
