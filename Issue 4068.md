# Issue 4068: determinants for matrices over multivariate polynomial rings slow

archive/issues_004068.json:
```json
{
    "body": "Assignee: @malb\n\nphil <fongpwf__AT__gmail.com> wrote on [sage-devel]\n> I have a matrix that is composed of multivariant polynomial\n> entries.  I want to compute its determinant.  The problem is that it\n> is very slow or runs out of memory.  For example,\n> R.<x,y> = QQ[]\n> C = random_matrix(R,10,10)\n> Cdet = C.determinant()   # this line takes a long time\n\nIf you have more variables, it will run out of memory instead (on a 32\nbit installation).\n\nIssue created by migration from https://trac.sagemath.org/ticket/4068\n\n",
    "created_at": "2008-09-05T17:16:22Z",
    "labels": [
        "linear algebra",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "determinants for matrices over multivariate polynomial rings slow",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4068",
    "user": "@malb"
}
```
Assignee: @malb

phil <fongpwf__AT__gmail.com> wrote on [sage-devel]
> I have a matrix that is composed of multivariant polynomial
> entries.  I want to compute its determinant.  The problem is that it
> is very slow or runs out of memory.  For example,
> R.<x,y> = QQ[]
> C = random_matrix(R,10,10)
> Cdet = C.determinant()   # this line takes a long time

If you have more variables, it will run out of memory instead (on a 32
bit installation).

Issue created by migration from https://trac.sagemath.org/ticket/4068





---

archive/issue_comments_029355.json:
```json
{
    "body": "Here's a workaround:\n\n\n```\nsage: R.<x,y> = QQ[]\nsage: C = random_matrix(R,8,8)\nsage: %time d = C.determinant()\nCPU times: user 2.64 s, sys: 0.00 s, total: 2.65 s\nWall time: 2.67 s\n```\n\n\n\n```\nsage: %time d2 = R(C._singular_().det())\nCPU times: user 0.04 s, sys: 0.01 s, total: 0.05 s\nWall time: 0.15 s\n```\n\n\n\n```\nsage: d2 == d\nTrue\n```\n\n\nSo we need to call Singular instead of using the native code.",
    "created_at": "2008-09-05T17:16:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4068",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4068#issuecomment-29355",
    "user": "@malb"
}
```

Here's a workaround:


```
sage: R.<x,y> = QQ[]
sage: C = random_matrix(R,8,8)
sage: %time d = C.determinant()
CPU times: user 2.64 s, sys: 0.00 s, total: 2.65 s
Wall time: 2.67 s
```



```
sage: %time d2 = R(C._singular_().det())
CPU times: user 0.04 s, sys: 0.01 s, total: 0.05 s
Wall time: 0.15 s
```



```
sage: d2 == d
True
```


So we need to call Singular instead of using the native code.



---

archive/issue_comments_029356.json:
```json
{
    "body": "Attachment [matrix_mpoly_det.patch](tarball://root/attachments/some-uuid/ticket4068/matrix_mpoly_det.patch) by @malb created at 2008-09-05 19:20:48",
    "created_at": "2008-09-05T19:20:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4068",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4068#issuecomment-29356",
    "user": "@malb"
}
```

Attachment [matrix_mpoly_det.patch](tarball://root/attachments/some-uuid/ticket4068/matrix_mpoly_det.patch) by @malb created at 2008-09-05 19:20:48



---

archive/issue_comments_029357.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-09-05T19:58:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4068",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4068#issuecomment-29357",
    "user": "@mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_029358.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc0",
    "created_at": "2008-09-06T00:07:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4068",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4068#issuecomment-29358",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.rc0



---

archive/issue_comments_029359.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-06T00:07:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4068",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4068#issuecomment-29359",
    "user": "mabshoff"
}
```

Resolution: fixed
