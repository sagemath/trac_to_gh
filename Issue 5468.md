# Issue 5468: matrix creation over laurent polynomial rings

archive/issues_005468.json:
```json
{
    "body": "Assignee: malb\n\n\n```\nA.<Y> = QQ[]\nR.<X> = LaurentPolynomialRing(A)\nmatrix(R,2,2,[X,0,0,1])\n```\n\ngives a\n\n```\nTypeError: Unable to coerce X (<type 'sage.rings.polynomial.laurent_polynomial.LaurentPolynomial_mpair'>) to Rational\n```\n\n\nThe same problem occurs with `LaurentSeriesRing`, but not with `PowerSeriesRing`.\n\nI have not tried to chase where the problem actually comes from.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5468\n\n",
    "created_at": "2009-03-10T18:30:00Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "title": "matrix creation over laurent polynomial rings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5468",
    "user": "wuthrich"
}
```
Assignee: malb


```
A.<Y> = QQ[]
R.<X> = LaurentPolynomialRing(A)
matrix(R,2,2,[X,0,0,1])
```

gives a

```
TypeError: Unable to coerce X (<type 'sage.rings.polynomial.laurent_polynomial.LaurentPolynomial_mpair'>) to Rational
```


The same problem occurs with `LaurentSeriesRing`, but not with `PowerSeriesRing`.

I have not tried to chase where the problem actually comes from.

Issue created by migration from https://trac.sagemath.org/ticket/5468





---

archive/issue_comments_042444.json:
```json
{
    "body": "This is fixed by #3617",
    "created_at": "2010-01-19T22:00:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5468",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5468#issuecomment-42444",
    "user": "mhansen"
}
```

This is fixed by #3617



---

archive/issue_comments_042445.json:
```json
{
    "body": "Closed as fixed by #3617.",
    "created_at": "2010-01-23T08:14:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5468",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5468#issuecomment-42445",
    "user": "mvngu"
}
```

Closed as fixed by #3617.



---

archive/issue_comments_042446.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-23T08:14:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5468",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5468#issuecomment-42446",
    "user": "mvngu"
}
```

Resolution: fixed
