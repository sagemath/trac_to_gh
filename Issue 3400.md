# Issue 3400: Elements of GL(n,R) should coerce properly to matrices

archive/issues_003400.json:
```json
{
    "body": "Assignee: robertwb\n\nCC:  alexghitza\n\nFor example:\n\n\n```\nsage: M = Matrix(GF(2), [[1,1,1,1]])\nsage: G = GL(4,2)\nsage: N = G.0\nsage: M\n[1 1 1 1]\nsage: N\n\n[1 1 0 0]\n[0 1 0 0]\n[0 0 1 0]\n[0 0 0 1]\nsage: M*N\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/Users/rlmill/sage-3.0.2/<ipython console> in <module>()\n\n/Users/rlmill/sage-3.0.2/element.pyx in sage.structure.element.Matrix.__mul__ (sage/structure/element.c:11352)()\n\n/Users/rlmill/sage-3.0.2/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.bin_op_c (sage/structure/coerce.c:5301)()\n\nTypeError: unsupported operand parent(s) for '*': 'Full MatrixSpace of 1 by 4 dense matrices over Finite Field of size 2' and 'General Linear Group of degree 4 over Finite Field of size 2'\nsage: M*N.matrix()\n[1 0 1 1]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3400\n\n",
    "created_at": "2008-06-11T16:23:08Z",
    "labels": [
        "coercion",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "Elements of GL(n,R) should coerce properly to matrices",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3400",
    "user": "rlm"
}
```
Assignee: robertwb

CC:  alexghitza

For example:


```
sage: M = Matrix(GF(2), [[1,1,1,1]])
sage: G = GL(4,2)
sage: N = G.0
sage: M
[1 1 1 1]
sage: N

[1 1 0 0]
[0 1 0 0]
[0 0 1 0]
[0 0 0 1]
sage: M*N
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/rlmill/sage-3.0.2/<ipython console> in <module>()

/Users/rlmill/sage-3.0.2/element.pyx in sage.structure.element.Matrix.__mul__ (sage/structure/element.c:11352)()

/Users/rlmill/sage-3.0.2/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.bin_op_c (sage/structure/coerce.c:5301)()

TypeError: unsupported operand parent(s) for '*': 'Full MatrixSpace of 1 by 4 dense matrices over Finite Field of size 2' and 'General Linear Group of degree 4 over Finite Field of size 2'
sage: M*N.matrix()
[1 0 1 1]
```


Issue created by migration from https://trac.sagemath.org/ticket/3400





---

archive/issue_comments_023810.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-19T06:55:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3400#issuecomment-23810",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_023811.json:
```json
{
    "body": "Changing assignee from robertwb to mhansen.",
    "created_at": "2008-09-19T06:55:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3400#issuecomment-23811",
    "user": "mhansen"
}
```

Changing assignee from robertwb to mhansen.



---

archive/issue_comments_023812.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-17T11:09:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3400#issuecomment-23812",
    "user": "robertwb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_023813.json:
```json
{
    "body": "Attachment [3400-matrix-group-action.patch](tarball://root/attachments/some-uuid/ticket3400/3400-matrix-group-action.patch) by robertwb created at 2010-01-17 11:09:21",
    "created_at": "2010-01-17T11:09:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3400#issuecomment-23813",
    "user": "robertwb"
}
```

Attachment [3400-matrix-group-action.patch](tarball://root/attachments/some-uuid/ticket3400/3400-matrix-group-action.patch) by robertwb created at 2010-01-17 11:09:21



---

archive/issue_comments_023814.json:
```json
{
    "body": "Passes all tests and works as advertised.  Positive review.",
    "created_at": "2010-01-18T05:09:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3400#issuecomment-23814",
    "user": "rbeezer"
}
```

Passes all tests and works as advertised.  Positive review.



---

archive/issue_comments_023815.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-18T05:09:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3400#issuecomment-23815",
    "user": "rbeezer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_023816.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-18T22:43:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3400#issuecomment-23816",
    "user": "rlm"
}
```

Resolution: fixed
