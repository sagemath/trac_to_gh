# Issue 6761: solve_left on a vector returns a matrix

archive/issues_006761.json:
```json
{
    "body": "Assignee: was\n\nCC:  jason\n\nThis is inconsistent with solve_right and contrary to the documentation. \n\n\n```\nsage: A = random_matrix(ZZ, 5)\nsage: b = vector(ZZ, range(5))\nsage: A.solve_left(b)\n[    47/630  -233/1170       2/65     34/819 -5269/8190]\nsage: A.solve_left(b).parent()\nFull MatrixSpace of 1 by 5 dense matrices over Rational Field\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6761\n\n",
    "created_at": "2009-08-16T09:13:10Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "title": "solve_left on a vector returns a matrix",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6761",
    "user": "robertwb"
}
```
Assignee: was

CC:  jason

This is inconsistent with solve_right and contrary to the documentation. 


```
sage: A = random_matrix(ZZ, 5)
sage: b = vector(ZZ, range(5))
sage: A.solve_left(b)
[    47/630  -233/1170       2/65     34/819 -5269/8190]
sage: A.solve_left(b).parent()
Full MatrixSpace of 1 by 5 dense matrices over Rational Field
```


Issue created by migration from https://trac.sagemath.org/ticket/6761





---

archive/issue_comments_055667.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-11-06T08:13:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6761#issuecomment-55667",
    "user": "klee"
}
```

Attachment



---

archive/issue_comments_055668.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-06T08:19:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6761#issuecomment-55668",
    "user": "klee"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_055669.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-06T20:06:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6761#issuecomment-55669",
    "user": "robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_055670.json:
```json
{
    "body": "Thanks!",
    "created_at": "2009-11-06T20:06:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6761#issuecomment-55670",
    "user": "robertwb"
}
```

Thanks!



---

archive/issue_comments_055671.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-07T04:59:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6761#issuecomment-55671",
    "user": "mhansen"
}
```

Resolution: fixed
