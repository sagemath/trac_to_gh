# Issue 9035: add degree argument to univariate polynomial reverse() method

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2010-05-24 13:06:18

Assignee: AlexGhitza

Attached patch adds a `degree` argument to the `reverse()` method of univariate polynomials and wraps the methods provided by FLINT in `polynomial_zmod_flint` and `polynomial_integer_dense_flint` classes.


---

Attachment


---

Comment by burcin created at 2010-05-24 13:10:39

Changing status from new to needs_review.


---

Comment by cremona created at 2010-05-27 11:58:10

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2010-05-27 11:58:10

Patch applies fine to 4.4.3.alpha0, and looks good to me.

Tests pass (I tested all files in sage/rings/polynomial plus some other random tests).

I am giving this a positive review, but wonder whether the following reverse functions should also be changed to be consistent:

```
libs/ntl/ntl_GF2X.pyx:645:    def reverse(self, int hi = -2):
libs/ntl/ntl_ZZX.pyx:768:    def reverse(self, hi=None):
libs/ntl/ntl_ZZ_pEX.pyx:850:    def reverse(self, hi=None):
libs/ntl/ntl_ZZ_pX.pyx:947:    def reverse(self, hi=None):
...
rings/polynomial/polynomial_modn_dense_ntl.pyx:1005:    def reverse(self):
rings/polynomial/polynomial_modn_dense_ntl.pyx:1548:    def reverse(self):
rings/polynomial/polynomial_real_mpfr_dense.pyx:484:    def reverse(self):
...
rings/polynomial/padics/polynomial_padic_capped_relative_dense.py:840:    def reverse(self, n = None):
```



---

Comment by mhansen created at 2010-06-06 01:24:27

Resolution: fixed
