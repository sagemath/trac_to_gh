# Issue 8207: Factoring a constant generic multivariate polynomial broken

Issue created by migration from https://trac.sagemath.org/ticket/8207

Original creator: wjp

Original creation time: 2010-02-07 13:10:04

Assignee: AlexGhitza

The following raises an `IndexError`:


```
sage: R.<x,y> = CC[]
sage: R(1).factor()
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)

/data/wpalenst/sage/sage-4.3.1/<ipython console> in <module>()

/data/wpalenst/sage/sage-4.3.1/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_element.pyc in factor(self, proof)
   1422         # try to use univariate factoring first
   1423         try:
-> 1424             F = self.univariate_polynomial().factor()
   1425             return Factorization([(R(f),m) for f,m in F], unit=F.unit())
   1426         except TypeError:

/data/wpalenst/sage/sage-4.3.1/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_element.pyc in univariate_polynomial(self, R)
   1055         #construct ring if None
   1056         if R is None:
-> 1057             R = self.base_ring()[str(self.variables()[0])]
   1058 
   1059         monomial_coefficients = self._MPolynomial_element__element.dict()

IndexError: tuple index out of range
```


The call `R(1).univariate_polynomial()` seems to fail.


---

Comment by jsyri created at 2010-05-13 19:25:37

Changing status from new to needs_review.


---

Attachment

My first patch on Sage. I hope I've got everything all right.


---

Comment by cremona created at 2010-05-16 14:37:19

The patch looks fine to me, applies ok to 4.4.2.rc0 and all tests in sage/rings/polynomial pass.

Looking at the code in this file, some of it seems very over-complicated -- do people agree?  The is_univariate() function could just return self.nvariables()<2.  And the conversion to univariate function (which this patch patches) could more simply, after constructing the ring R as now, return `f([R.gen()]*f.parent().ngens())` saving 20 complicated lines.

I am copying in malb who may have an opinion.  If people agree we could open a ticket for simplifying these.  But this patch gets a positive review from me anyway.


---

Comment by cremona created at 2010-05-16 14:37:19

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-06-06 01:01:28

Resolution: fixed
