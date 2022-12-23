# Issue 2417: discriminant method sometimes returns values in the fraction field

archive/issues_002417.json:
```json
{
    "body": "Assignee: was\n\nFor non-monic polynomials, the discriminant method introduced in #2392 returns values in the fraction field of the base ring, instead of in the base ring.\n\n```\nsage: R.<y> = QQ[]\nsage: S.<x> = R[]\nsage: (x*y+x+y+1).discriminant()\n1\nsage: (x*y+x+y+1).discriminant().parent()\nFraction Field of Univariate Polynomial Ring in y over Rational Field\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2417\n\n",
    "created_at": "2008-03-07T04:43:09Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "title": "discriminant method sometimes returns values in the fraction field",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2417",
    "user": "cwitty"
}
```
Assignee: was

For non-monic polynomials, the discriminant method introduced in #2392 returns values in the fraction field of the base ring, instead of in the base ring.

```
sage: R.<y> = QQ[]
sage: S.<x> = R[]
sage: (x*y+x+y+1).discriminant()
1
sage: (x*y+x+y+1).discriminant().parent()
Fraction Field of Univariate Polynomial Ring in y over Rational Field
```



Issue created by migration from https://trac.sagemath.org/ticket/2417





---

archive/issue_comments_016300.json:
```json
{
    "body": "Attachment\n\nThis is due to the fact that discriminants are computed via resultants, using a formula that sometimes divides the resultant by the leading coefficient.  When the coefficients are themselves polynomials, this makes the result appear in the fraction field.\n\nThe fix is very simple: just coerce the result back into the base ring before returning.  This is in the attached patch, together with a couple of typo fixes.  I've also replaced one of the doctests that was supposed to illustrate precisely this behavior (but didn't) with Carl's example.",
    "created_at": "2008-03-24T02:16:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2417#issuecomment-16300",
    "user": "AlexGhitza"
}
```

Attachment

This is due to the fact that discriminants are computed via resultants, using a formula that sometimes divides the resultant by the leading coefficient.  When the coefficients are themselves polynomials, this makes the result appear in the fraction field.

The fix is very simple: just coerce the result back into the base ring before returning.  This is in the attached patch, together with a couple of typo fixes.  I've also replaced one of the doctests that was supposed to illustrate precisely this behavior (but didn't) with Carl's example.



---

archive/issue_comments_016301.json:
```json
{
    "body": "Works well for me.",
    "created_at": "2008-03-26T06:03:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2417#issuecomment-16301",
    "user": "robertwb"
}
```

Works well for me.



---

archive/issue_comments_016302.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-26T22:09:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2417#issuecomment-16302",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_016303.json:
```json
{
    "body": "Merged in Sage 2.11.alpha2",
    "created_at": "2008-03-26T22:09:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2417#issuecomment-16303",
    "user": "mabshoff"
}
```

Merged in Sage 2.11.alpha2
