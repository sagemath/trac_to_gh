# Issue 977: Schubert polynomials send 1 -> wrong polynomial ring

archive/issues_000977.json:
```json
{
    "body": "Assignee: mhansen\n\nCC:  sage-combinat\n\nIt seems that this is only happening with the identity element. Here's an example:\n\n\n```\nsage: R = SchubertPolynomialRing(ZZ)\nsage: f = R([1])\nsage: type(f.expand())\n<type 'sage.rings.polynomial.polynomial_integer_dense_ntl.Polynomial_integer_dense_ntl'>\nsage: f = R([1,2])\nsage: type(f.expand())\n<type 'sage.rings.polynomial.polynomial_integer_dense_ntl.Polynomial_integer_dense_ntl'>\n\n# But all of the polynomials returned should be multi-polynomials\n\nsage: f = R([1,3,2,4])\nsage: type(f.expand())\n<class 'sage.rings.polynomial.multi_polynomial_element.MPolynomial_polydict'>\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/977\n\n",
    "created_at": "2007-10-23T21:06:30Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "title": "Schubert polynomials send 1 -> wrong polynomial ring",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/977",
    "user": "rlm"
}
```
Assignee: mhansen

CC:  sage-combinat

It seems that this is only happening with the identity element. Here's an example:


```
sage: R = SchubertPolynomialRing(ZZ)
sage: f = R([1])
sage: type(f.expand())
<type 'sage.rings.polynomial.polynomial_integer_dense_ntl.Polynomial_integer_dense_ntl'>
sage: f = R([1,2])
sage: type(f.expand())
<type 'sage.rings.polynomial.polynomial_integer_dense_ntl.Polynomial_integer_dense_ntl'>

# But all of the polynomials returned should be multi-polynomials

sage: f = R([1,3,2,4])
sage: type(f.expand())
<class 'sage.rings.polynomial.multi_polynomial_element.MPolynomial_polydict'>
```


Issue created by migration from https://trac.sagemath.org/ticket/977





---

archive/issue_comments_005964.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-23T23:50:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/977#issuecomment-5964",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_005965.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-24T21:48:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/977#issuecomment-5965",
    "user": "malb"
}
```

Resolution: fixed



---

archive/issue_comments_005966.json:
```json
{
    "body": "Attachment\n\nthis is applied to 2.8.9.alpha1",
    "created_at": "2007-10-24T21:48:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/977#issuecomment-5966",
    "user": "malb"
}
```

Attachment

this is applied to 2.8.9.alpha1
