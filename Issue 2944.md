# Issue 2944: [with patch, needs review] add E2 parameter to padic_height_via_multiply

archive/issues_002944.json:
```json
{
    "body": "Assignee: @williamstein\n\nThis patch adds an optional E2 parameter to `padic_height_via_multiply`. The idea is to make it possible to use a precomputed value of E2. Since the E2 computation is very expensive relative to the p-adic height computation, this makes it easier to do profiling work on the p-adic height portion of the computation.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2944\n\n",
    "created_at": "2008-04-16T22:32:27Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "[with patch, needs review] add E2 parameter to padic_height_via_multiply",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2944",
    "user": "dmharvey"
}
```
Assignee: @williamstein

This patch adds an optional E2 parameter to `padic_height_via_multiply`. The idea is to make it possible to use a precomputed value of E2. Since the E2 computation is very expensive relative to the p-adic height computation, this makes it easier to do profiling work on the p-adic height portion of the computation.


Issue created by migration from https://trac.sagemath.org/ticket/2944





---

archive/issue_comments_020304.json:
```json
{
    "body": "Attachment [height-E2.patch](tarball://root/attachments/some-uuid/ticket2944/height-E2.patch) by dmharvey created at 2008-04-16 22:32:44",
    "created_at": "2008-04-16T22:32:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2944",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2944#issuecomment-20304",
    "user": "dmharvey"
}
```

Attachment [height-E2.patch](tarball://root/attachments/some-uuid/ticket2944/height-E2.patch) by dmharvey created at 2008-04-16 22:32:44



---

archive/issue_comments_020305.json:
```json
{
    "body": "Fine by me.",
    "created_at": "2008-04-17T05:12:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2944",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2944#issuecomment-20305",
    "user": "@ncalexan"
}
```

Fine by me.



---

archive/issue_comments_020306.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-17T06:13:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2944",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2944#issuecomment-20306",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_020307.json:
```json
{
    "body": "Merged in Sage 3.0.alpha6",
    "created_at": "2008-04-17T06:13:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2944",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2944#issuecomment-20307",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha6
