# Issue 4493: derivative and integral of a matrix

archive/issues_004493.json:
```json
{
    "body": "Assignee: burcin\n\nIt would be handy in differential equations to be able to do differentiation and integration of matrices and vectors, with the exact same answer as obtained by using the apply_map method.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4493\n\n",
    "created_at": "2008-11-11T18:22:50Z",
    "labels": [
        "calculus",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "derivative and integral of a matrix",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4493",
    "user": "jason"
}
```
Assignee: burcin

It would be handy in differential equations to be able to do differentiation and integration of matrices and vectors, with the exact same answer as obtained by using the apply_map method.

Issue created by migration from https://trac.sagemath.org/ticket/4493





---

archive/issue_comments_033222.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-12-05T06:45:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4493#issuecomment-33222",
    "user": "jason"
}
```

Changing status from new to assigned.



---

archive/issue_comments_033223.json:
```json
{
    "body": "Changing assignee from burcin to jason.",
    "created_at": "2008-12-05T06:45:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4493#issuecomment-33223",
    "user": "jason"
}
```

Changing assignee from burcin to jason.



---

archive/issue_comments_033224.json:
```json
{
    "body": "This depends on #4713\n\nI guess the integral of a matrix doesn't come up that often, so I'm changing my request.  Besides, the integral can calculated using the apply_map function at #4713 for vectors or the existing apply_map function for matrices.",
    "created_at": "2008-12-05T08:14:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4493#issuecomment-33224",
    "user": "jason"
}
```

This depends on #4713

I guess the integral of a matrix doesn't come up that often, so I'm changing my request.  Besides, the integral can calculated using the apply_map function at #4713 for vectors or the existing apply_map function for matrices.



---

archive/issue_comments_033225.json:
```json
{
    "body": "Attachment [vector_derivative.patch](tarball://root/attachments/some-uuid/ticket4493/vector_derivative.patch) by jason created at 2008-12-05 08:15:34",
    "created_at": "2008-12-05T08:15:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4493#issuecomment-33225",
    "user": "jason"
}
```

Attachment [vector_derivative.patch](tarball://root/attachments/some-uuid/ticket4493/vector_derivative.patch) by jason created at 2008-12-05 08:15:34



---

archive/issue_comments_033226.json:
```json
{
    "body": "Attachment [matrix-derivative.patch](tarball://root/attachments/some-uuid/ticket4493/matrix-derivative.patch) by jason created at 2008-12-05 08:31:54",
    "created_at": "2008-12-05T08:31:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4493#issuecomment-33226",
    "user": "jason"
}
```

Attachment [matrix-derivative.patch](tarball://root/attachments/some-uuid/ticket4493/matrix-derivative.patch) by jason created at 2008-12-05 08:31:54



---

archive/issue_comments_033227.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-07T09:59:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4493#issuecomment-33227",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_033228.json:
```json
{
    "body": "Merged both patches in Sage 3.2.2.alpha1",
    "created_at": "2008-12-07T09:59:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4493#issuecomment-33228",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.2.2.alpha1
