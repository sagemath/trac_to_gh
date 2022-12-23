# Issue 8207: Factoring a constant generic multivariate polynomial broken

archive/issues_008207.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nThe following raises an `IndexError`:\n\n\n```\nsage: R.<x,y> = CC[]\nsage: R(1).factor()\n---------------------------------------------------------------------------\nIndexError                                Traceback (most recent call last)\n\n/data/wpalenst/sage/sage-4.3.1/<ipython console> in <module>()\n\n/data/wpalenst/sage/sage-4.3.1/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_element.pyc in factor(self, proof)\n   1422         # try to use univariate factoring first\n   1423         try:\n-> 1424             F = self.univariate_polynomial().factor()\n   1425             return Factorization([(R(f),m) for f,m in F], unit=F.unit())\n   1426         except TypeError:\n\n/data/wpalenst/sage/sage-4.3.1/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_element.pyc in univariate_polynomial(self, R)\n   1055         #construct ring if None\n   1056         if R is None:\n-> 1057             R = self.base_ring()[str(self.variables()[0])]\n   1058 \n   1059         monomial_coefficients = self._MPolynomial_element__element.dict()\n\nIndexError: tuple index out of range\n```\n\n\nThe call `R(1).univariate_polynomial()` seems to fail.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8207\n\n",
    "created_at": "2010-02-07T13:10:04Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "Factoring a constant generic multivariate polynomial broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8207",
    "user": "wjp"
}
```
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

Issue created by migration from https://trac.sagemath.org/ticket/8207





---

archive/issue_comments_072378.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-13T19:25:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8207#issuecomment-72378",
    "user": "jsyri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_072379.json:
```json
{
    "body": "Attachment\n\nMy first patch on Sage. I hope I've got everything all right.",
    "created_at": "2010-05-13T19:25:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8207#issuecomment-72379",
    "user": "jsyri"
}
```

Attachment

My first patch on Sage. I hope I've got everything all right.



---

archive/issue_comments_072380.json:
```json
{
    "body": "The patch looks fine to me, applies ok to 4.4.2.rc0 and all tests in sage/rings/polynomial pass.\n\nLooking at the code in this file, some of it seems very over-complicated -- do people agree?  The is_univariate() function could just return self.nvariables()<2.  And the conversion to univariate function (which this patch patches) could more simply, after constructing the ring R as now, return `f([R.gen()]*f.parent().ngens())` saving 20 complicated lines.\n\nI am copying in malb who may have an opinion.  If people agree we could open a ticket for simplifying these.  But this patch gets a positive review from me anyway.",
    "created_at": "2010-05-16T14:37:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8207#issuecomment-72380",
    "user": "cremona"
}
```

The patch looks fine to me, applies ok to 4.4.2.rc0 and all tests in sage/rings/polynomial pass.

Looking at the code in this file, some of it seems very over-complicated -- do people agree?  The is_univariate() function could just return self.nvariables()<2.  And the conversion to univariate function (which this patch patches) could more simply, after constructing the ring R as now, return `f([R.gen()]*f.parent().ngens())` saving 20 complicated lines.

I am copying in malb who may have an opinion.  If people agree we could open a ticket for simplifying these.  But this patch gets a positive review from me anyway.



---

archive/issue_comments_072381.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-16T14:37:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8207#issuecomment-72381",
    "user": "cremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072382.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-06T01:01:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8207#issuecomment-72382",
    "user": "mhansen"
}
```

Resolution: fixed
