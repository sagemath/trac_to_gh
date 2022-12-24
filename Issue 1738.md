# Issue 1738: [with patch] fraction field __pow__ doesn't handle negative exp. elegantly

archive/issues_001738.json:
```json
{
    "body": "Assignee: was\n\nNegative exponents put fraction field elements in the denominator of a fraction field element.\n\n\n```\nsage: R.<x>=ZZ[]\nsage: (1/x)^-3\n1/(1/x^3)\n```\n\n\nWith the patch:\n\n```\nsage: R.<x>=ZZ[]\nsage: (1/x)^-3\nx^3\n```\n\n \n\nIssue created by migration from https://trac.sagemath.org/ticket/1738\n\n",
    "created_at": "2008-01-10T01:49:26Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "title": "[with patch] fraction field __pow__ doesn't handle negative exp. elegantly",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1738",
    "user": "jbmohler"
}
```
Assignee: was

Negative exponents put fraction field elements in the denominator of a fraction field element.


```
sage: R.<x>=ZZ[]
sage: (1/x)^-3
1/(1/x^3)
```


With the patch:

```
sage: R.<x>=ZZ[]
sage: (1/x)^-3
x^3
```

 

Issue created by migration from https://trac.sagemath.org/ticket/1738





---

archive/issue_comments_010995.json:
```json
{
    "body": "Attachment [fraction_field_pow.patch](tarball://root/attachments/some-uuid/ticket1738/fraction_field_pow.patch) by was created at 2008-01-10 03:43:39\n\nIt looks good to me except change the somewhat too verbose\n\n```\n  sage: x = PolynomialRing(RationalField(),'x').gen() \n```\n\nto one of the following (take your pick):\n\n```\n  sage: x = polygen(QQ, 'x')\n```\n\nor \n\n```\n  sage: R.<x> = QQ[]\n```\n\nor \n\n```\n  sage: x = PolynomialRing(QQ,'x').gen()\n```\n\n\nI think it is important that the docstrings give illustrations of good usage of Sage.",
    "created_at": "2008-01-10T03:43:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1738",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1738#issuecomment-10995",
    "user": "was"
}
```

Attachment [fraction_field_pow.patch](tarball://root/attachments/some-uuid/ticket1738/fraction_field_pow.patch) by was created at 2008-01-10 03:43:39

It looks good to me except change the somewhat too verbose

```
  sage: x = PolynomialRing(RationalField(),'x').gen() 
```

to one of the following (take your pick):

```
  sage: x = polygen(QQ, 'x')
```

or 

```
  sage: R.<x> = QQ[]
```

or 

```
  sage: x = PolynomialRing(QQ,'x').gen()
```


I think it is important that the docstrings give illustrations of good usage of Sage.



---

archive/issue_comments_010996.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-01-16T22:05:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1738",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1738#issuecomment-10996",
    "user": "mhansen"
}
```

Resolution: duplicate



---

archive/issue_comments_010997.json:
```json
{
    "body": "This is a duplicate of #1786.  I didn't realize that this was indeed the issue when opening #1786.",
    "created_at": "2008-01-16T22:06:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1738",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1738#issuecomment-10997",
    "user": "mhansen"
}
```

This is a duplicate of #1786.  I didn't realize that this was indeed the issue when opening #1786.
