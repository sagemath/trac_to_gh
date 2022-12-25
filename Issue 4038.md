# Issue 4038: Problem in factor() and roots() for p-adic polynomials

archive/issues_004038.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  @categorie\n\nKeywords: polynomial p-adic\n\nThis was reported by Chris Wuthrich while reviewing #3377:\n\n\n```\nsage: E = EllipticCurve('37a1')\nsage: K =Qp(7,10)                 \nsage: EK = E.base_extend(K)\nsage: E = EllipticCurve('37a1')\nsage: K = Qp(7,10)             \nsage: EK = E.base_extend(K)    \nsage: g = EK.division_polynomial_0(3)\nsage: type(g)\n<class 'sage.rings.polynomial.padics.polynomial_padic_capped_relative_dense.Polynomial_padic_capped_relative_dense'>\nsage: g.factor()\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n\n/home/john/sage-3.1.2.alpha3/<ipython console> in <module>()\n\n/home/john/sage-3.1.2.alpha3/local/lib/python2.5/site-packages/sage/rings/polynomial/padics/polynomial_padic_capped_relative_dense.py in factor(self)\n   1009         R = ZpCA(base.prime(), prec = m)\n   1010         S = PolynomialRing(R, self.parent().variable_name())\n-> 1011         F = S(self).factor()\n   1012         return Factorization([(self.parent()(a), b) for (a, b) in F], base(F.unit()))\n   1013 \n\n/home/john/sage-3.1.2.alpha3/local/lib/python2.5/site-packages/sage/rings/polynomial/padics/polynomial_padic_flat.py in factor(self, absprec)\n    133             lval = F[i][0].leading_coefficient().valuation()\n    134             if upart != 1:\n--> 135                 F[i] = (F[i][0] // upart, F[i][1])\n    136                 u *= upart ** F[i][1]\n    137             c -= lval * F[i][1]\n\n/home/john/sage-3.1.2.alpha3/polynomial_element.pyx in sage.rings.polynomial.polynomial_element.Polynomial_generic_dense.__floordiv__ (sage/rings/polynomial/polynomial_element.c:28101)()\n\nAttributeError: 'Polynomial_padic_flat' object has no attribute '__coeffs'\n```\n\n\nSomewhere in the polynomial hierarchy, this particular type of polynomial is not having its `__coeffs` field set.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4038\n\n",
    "created_at": "2008-09-02T13:37:32Z",
    "labels": [
        "component: commutative algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.3",
    "title": "Problem in factor() and roots() for p-adic polynomials",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4038",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: @malb

CC:  @categorie

Keywords: polynomial p-adic

This was reported by Chris Wuthrich while reviewing #3377:


```
sage: E = EllipticCurve('37a1')
sage: K =Qp(7,10)                 
sage: EK = E.base_extend(K)
sage: E = EllipticCurve('37a1')
sage: K = Qp(7,10)             
sage: EK = E.base_extend(K)    
sage: g = EK.division_polynomial_0(3)
sage: type(g)
<class 'sage.rings.polynomial.padics.polynomial_padic_capped_relative_dense.Polynomial_padic_capped_relative_dense'>
sage: g.factor()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/john/sage-3.1.2.alpha3/<ipython console> in <module>()

/home/john/sage-3.1.2.alpha3/local/lib/python2.5/site-packages/sage/rings/polynomial/padics/polynomial_padic_capped_relative_dense.py in factor(self)
   1009         R = ZpCA(base.prime(), prec = m)
   1010         S = PolynomialRing(R, self.parent().variable_name())
-> 1011         F = S(self).factor()
   1012         return Factorization([(self.parent()(a), b) for (a, b) in F], base(F.unit()))
   1013 

/home/john/sage-3.1.2.alpha3/local/lib/python2.5/site-packages/sage/rings/polynomial/padics/polynomial_padic_flat.py in factor(self, absprec)
    133             lval = F[i][0].leading_coefficient().valuation()
    134             if upart != 1:
--> 135                 F[i] = (F[i][0] // upart, F[i][1])
    136                 u *= upart ** F[i][1]
    137             c -= lval * F[i][1]

/home/john/sage-3.1.2.alpha3/polynomial_element.pyx in sage.rings.polynomial.polynomial_element.Polynomial_generic_dense.__floordiv__ (sage/rings/polynomial/polynomial_element.c:28101)()

AttributeError: 'Polynomial_padic_flat' object has no attribute '__coeffs'
```


Somewhere in the polynomial hierarchy, this particular type of polynomial is not having its `__coeffs` field set.

Issue created by migration from https://trac.sagemath.org/ticket/4038





---

archive/issue_comments_029073.json:
```json
{
    "body": "Attachment [trac_4038.patch](tarball://root/attachments/some-uuid/ticket4038/trac_4038.patch) by @JohnCremona created at 2008-12-22 12:02:22\n\nIn 3.2.2 the error message changes to:\n\n```\nsage: g.factor()\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n\n/home/jec/.sage/temp/host_57_89/5017/_home_jec__sage_init_sage_0.py in <module>()\n----> 1\n      2\n      3\n      4\n      5\n\n/home/jec/sage-3.2.2/local/lib/python2.5/site-packages/sage/rings/polynomial/padics/polynomial_padic_capped_relative_dense.pyc in factor(self)\n   1009         R = ZpCA(base.prime(), prec = m)\n   1010         S = PolynomialRing(R, self.parent().variable_name())\n-> 1011         F = S(self).factor()\n   1012         return Factorization([(self.parent()(a), b) for (a, b) in F], base(F.unit()))\n   1013\n\n/home/jec/sage-3.2.2/local/lib/python2.5/site-packages/sage/rings/polynomial/padics/polynomial_padic_flat.pyc in factor(self, absprec)\n    133             lval = F[i][0].leading_coefficient().valuation()\n    134             if upart != 1:\n--> 135                 F[i] = (F[i][0] // upart, F[i][1])\n    136                 u *= upart ** F[i][1]\n    137             c -= lval * F[i][1]\n\n/home/jec/sage-3.2.2/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_element.so in sage.rings.polynomial.polynomial_element.Polynomial_generic_dense.__floordiv__ (sage/rings/polynomial/polynomial_element.c:30443)()\n   4436\n   4437\n-> 4438\n   4439\n   4440\n\nAttributeError: 'Polynomial_padic_flat' object has no attribute '_parent'\n```\n\nAnd the problem goes away if I change \"//\" to \"/\" on line 135 of sage/rings/polynomial/padics/polynomial_padic_flat.py.\n\nAttached patch applies to 3.2.2.",
    "created_at": "2008-12-22T12:02:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4038",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4038#issuecomment-29073",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_4038.patch](tarball://root/attachments/some-uuid/ticket4038/trac_4038.patch) by @JohnCremona created at 2008-12-22 12:02:22

In 3.2.2 the error message changes to:

```
sage: g.factor()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/jec/.sage/temp/host_57_89/5017/_home_jec__sage_init_sage_0.py in <module>()
----> 1
      2
      3
      4
      5

/home/jec/sage-3.2.2/local/lib/python2.5/site-packages/sage/rings/polynomial/padics/polynomial_padic_capped_relative_dense.pyc in factor(self)
   1009         R = ZpCA(base.prime(), prec = m)
   1010         S = PolynomialRing(R, self.parent().variable_name())
-> 1011         F = S(self).factor()
   1012         return Factorization([(self.parent()(a), b) for (a, b) in F], base(F.unit()))
   1013

/home/jec/sage-3.2.2/local/lib/python2.5/site-packages/sage/rings/polynomial/padics/polynomial_padic_flat.pyc in factor(self, absprec)
    133             lval = F[i][0].leading_coefficient().valuation()
    134             if upart != 1:
--> 135                 F[i] = (F[i][0] // upart, F[i][1])
    136                 u *= upart ** F[i][1]
    137             c -= lval * F[i][1]

/home/jec/sage-3.2.2/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_element.so in sage.rings.polynomial.polynomial_element.Polynomial_generic_dense.__floordiv__ (sage/rings/polynomial/polynomial_element.c:30443)()
   4436
   4437
-> 4438
   4439
   4440

AttributeError: 'Polynomial_padic_flat' object has no attribute '_parent'
```

And the problem goes away if I change "//" to "/" on line 135 of sage/rings/polynomial/padics/polynomial_padic_flat.py.

Attached patch applies to 3.2.2.



---

archive/issue_comments_029074.json:
```json
{
    "body": "Looks good.",
    "created_at": "2008-12-23T12:58:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4038",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4038#issuecomment-29074",
    "user": "https://github.com/aghitza"
}
```

Looks good.



---

archive/issue_comments_029075.json:
```json
{
    "body": "Merged in Sage 3.2.3.alpha0",
    "created_at": "2008-12-23T21:14:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4038",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4038#issuecomment-29075",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.3.alpha0



---

archive/issue_comments_029076.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-23T21:14:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4038",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4038#issuecomment-29076",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004268.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-23T21:14:17Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4038",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4038#event-4268"
}
```
