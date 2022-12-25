# Issue 2616: Replace all matrix.submatrix() instances

archive/issues_002616.json:
```json
{
    "body": "Assignee: @dfdeshom\n\nPending review and inclusion of #2355, we can replace all instances of M.submatrix() with `M[indexa, indexb]`\n\nNote: I only found one function is using the submatrix method (subdivisions in matrix2.pyx). \n\nIssue created by migration from https://trac.sagemath.org/ticket/2616\n\n",
    "created_at": "2008-03-20T17:51:24Z",
    "labels": [
        "component: linear algebra",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "Replace all matrix.submatrix() instances",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2616",
    "user": "https://github.com/dfdeshom"
}
```
Assignee: @dfdeshom

Pending review and inclusion of #2355, we can replace all instances of M.submatrix() with `M[indexa, indexb]`

Note: I only found one function is using the submatrix method (subdivisions in matrix2.pyx). 

Issue created by migration from https://trac.sagemath.org/ticket/2616





---

archive/issue_comments_017917.json:
```json
{
    "body": "Attachment [2616-replace_submatrix.patch](tarball://root/attachments/some-uuid/ticket2616/2616-replace_submatrix.patch) by @aghitza created at 2008-04-13 22:21:20",
    "created_at": "2008-04-13T22:21:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2616#issuecomment-17917",
    "user": "https://github.com/aghitza"
}
```

Attachment [2616-replace_submatrix.patch](tarball://root/attachments/some-uuid/ticket2616/2616-replace_submatrix.patch) by @aghitza created at 2008-04-13 22:21:20



---

archive/issue_comments_017918.json:
```json
{
    "body": "Actually, there are a couple of other places where submatrix() is used.  See the attached patch, where I have replaced all of them.",
    "created_at": "2008-04-13T22:22:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2616#issuecomment-17918",
    "user": "https://github.com/aghitza"
}
```

Actually, there are a couple of other places where submatrix() is used.  See the attached patch, where I have replaced all of them.



---

archive/issue_comments_017919.json:
```json
{
    "body": "Replying to [comment:1 AlexGhitza]:\n> Actually, there are a couple of other places where submatrix() is used.  See the attached patch, where I have replaced all of them.\n\nThanks! Patch looks good. I say apply!",
    "created_at": "2008-04-14T20:17:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2616#issuecomment-17919",
    "user": "https://github.com/dfdeshom"
}
```

Replying to [comment:1 AlexGhitza]:
> Actually, there are a couple of other places where submatrix() is used.  See the attached patch, where I have replaced all of them.

Thanks! Patch looks good. I say apply!



---

archive/issue_events_002806.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-04-14T20:39:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2616",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2616#event-2806"
}
```



---

archive/issue_comments_017920.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-14T20:39:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2616#issuecomment-17920",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_017921.json:
```json
{
    "body": "Merged in Sage 3.0.alpha5",
    "created_at": "2008-04-14T20:39:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2616#issuecomment-17921",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.alpha5
