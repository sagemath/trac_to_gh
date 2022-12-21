# Issue 9020: random degrees for random_element()s univariate polynomial rings

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2010-05-22 21:58:30

Assignee: AlexGhitza

Attached patch allows using a tuple as the `degree` argument when calling the `random_element()` method of univariate polynomial rings. The tuple specifies the minimum and maximum degrees so we don't always get polynomials of the same degree:


```
sage: R.<x> = ZZ[]
sage: R.random_element(degree=(0,8))
2*x^7 - x^5 + 4*x^4 - 5*x^3 + x^2 + 14*x - 1
sage: R.random_element(degree=(0,8))
-2*x^3 + x^2 + x + 4
```


This is also directly usable by matrices:


```
sage: M = Matrix(R,2,2)
sage: M.randomize(degree=(0,6))
sage: M
[              -40*x^3 - 3*x^2 - 5*x            -x^4 + 476*x^3 - 3*x + 3]
[-12*x^6 + 2*x^4 - x^3 + x^2 + x - 1                           -52*x + 5]
```



---

Comment by burcin created at 2010-05-22 22:00:09

Changing status from new to needs_review.


---

Attachment


---

Comment by cremona created at 2010-05-27 20:38:48

Good idea.  Patch applies fine to 4.4.3.alpha0 and all tests in sage/rings/polynomials/ pass.


---

Comment by cremona created at 2010-05-27 20:38:48

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-06-06 01:22:21

Resolution: fixed
