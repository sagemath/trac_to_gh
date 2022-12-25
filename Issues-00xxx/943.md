# Issue 943: echelon_form over ZZ (hermite form) -- add ntl as additional optional algorithm

archive/issues_000943.json:
```json
{
    "body": "Assignee: @williamstein\n\nWe have in Magma (64-bit linux 2.33ghz):\n\n```\n\n> time A := MatrixAlgebra(IntegerRing(),200)![Random(-2,2) : i in [1..200^2]];\n> time d := Determinant(A);\nTime: 0.140\n> time H := HermiteForm(A);\nTime: 0.290\n```\n\nThis blows away Sage:\n\n```\nsage: a = MatrixSpace(ZZ,200).random_element(x=-2, y=2)    # -2 to 2\nsage: time b=a.echelon_form()\nCPU times: user 13.13 s, sys: 0.09 s, total: 13.22 s\nWall time: 13.27\nsage: time b=a.det()\nCPU times: user 1.81 s, sys: 0.00 s, total: 1.81 s\nWall time: 1.87\n```\n\nBut NTL is better -- it's twice as fast or more:\n\n```\n            sage: a = MatrixSpace(ZZ,200).random_element(x=-2, y=2)    # -2 to 2\n            sage: A = ntl.mat_ZZ(200,200)\n            sage: for i in xrange(a.nrows()):\n            ...     for j in xrange(a.ncols()):\n            ...         A[i,j] = a[i,j]\n            ...\n            sage: t = cputime(); d = A.determinant()\n            sage: cputime(t)\n            0.33201999999999998\n            sage: t = cputime(); B = A.HNF(d)\n            sage: cputime(t)\n            6.4924050000000006\n```\n\nSo at least we should use NTL for det and/or Hermite normal form for now, and at least make it\neasy to choose to use NTL. \n\nIn the longer run we need to implement a fast multimodular algorithm.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/943\n\n",
    "closed_at": "2007-10-20T21:42:29Z",
    "created_at": "2007-10-20T11:37:43Z",
    "labels": [
        "component: linear algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.8",
    "title": "echelon_form over ZZ (hermite form) -- add ntl as additional optional algorithm",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/943",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

We have in Magma (64-bit linux 2.33ghz):

```

> time A := MatrixAlgebra(IntegerRing(),200)![Random(-2,2) : i in [1..200^2]];
> time d := Determinant(A);
Time: 0.140
> time H := HermiteForm(A);
Time: 0.290
```

This blows away Sage:

```
sage: a = MatrixSpace(ZZ,200).random_element(x=-2, y=2)    # -2 to 2
sage: time b=a.echelon_form()
CPU times: user 13.13 s, sys: 0.09 s, total: 13.22 s
Wall time: 13.27
sage: time b=a.det()
CPU times: user 1.81 s, sys: 0.00 s, total: 1.81 s
Wall time: 1.87
```

But NTL is better -- it's twice as fast or more:

```
            sage: a = MatrixSpace(ZZ,200).random_element(x=-2, y=2)    # -2 to 2
            sage: A = ntl.mat_ZZ(200,200)
            sage: for i in xrange(a.nrows()):
            ...     for j in xrange(a.ncols()):
            ...         A[i,j] = a[i,j]
            ...
            sage: t = cputime(); d = A.determinant()
            sage: cputime(t)
            0.33201999999999998
            sage: t = cputime(); B = A.HNF(d)
            sage: cputime(t)
            6.4924050000000006
```

So at least we should use NTL for det and/or Hermite normal form for now, and at least make it
easy to choose to use NTL. 

In the longer run we need to implement a fast multimodular algorithm.


Issue created by migration from https://trac.sagemath.org/ticket/943





---

archive/issue_comments_005749.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2007-10-20T11:37:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/943#issuecomment-5749",
    "user": "https://github.com/williamstein"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_005750.json:
```json
{
    "body": "Attachment [7031.patch](tarball://root/attachments/some-uuid/ticket943/7031.patch) by @malb created at 2007-10-20 20:42:38",
    "created_at": "2007-10-20T20:42:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/943#issuecomment-5750",
    "user": "https://github.com/malb"
}
```

Attachment [7031.patch](tarball://root/attachments/some-uuid/ticket943/7031.patch) by @malb created at 2007-10-20 20:42:38



---

archive/issue_comments_005751.json:
```json
{
    "body": "Attachment [7032.patch](tarball://root/attachments/some-uuid/ticket943/7032.patch) by @malb created at 2007-10-20 20:44:36\n\nThe attached patches implement the NTL wrapping. They also make echelon_form fall back gracefully if ntl.mat_ZZ.HNF fails. However in that case NTL prints \"HNF: bad input\" which also shows up during the doctests.",
    "created_at": "2007-10-20T20:44:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/943#issuecomment-5751",
    "user": "https://github.com/malb"
}
```

Attachment [7032.patch](tarball://root/attachments/some-uuid/ticket943/7032.patch) by @malb created at 2007-10-20 20:44:36

The attached patches implement the NTL wrapping. They also make echelon_form fall back gracefully if ntl.mat_ZZ.HNF fails. However in that case NTL prints "HNF: bad input" which also shows up during the doctests.



---

archive/issue_events_002604.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-20T21:42:29Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/943",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/943#event-2604"
}
```



---

archive/issue_comments_005752.json:
```json
{
    "body": "I've applied this patch and it works.",
    "created_at": "2007-10-20T21:42:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/943#issuecomment-5752",
    "user": "https://github.com/williamstein"
}
```

I've applied this patch and it works.



---

archive/issue_comments_005753.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-20T21:42:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/943#issuecomment-5753",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_002605.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-10-21T02:27:36Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/943",
    "milestone": "sage-2.8.8",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/943#event-2605"
}
```
