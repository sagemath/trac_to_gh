# Issue 3731: [with patch, needs review] missing some derivatives in wester

archive/issues_003731.json:
```json
{
    "body": "Assignee: @garyfurnish\n\nKeywords: wester, calculus\n\nThere is an example in sage.calculus.wester starting like this:\n\n```\nsage: # (YES) Expand (1+x)^20, take derivative and factorize. \n```\n\nThe ensuing calculation involves no derivatives, just expanding and factoring (1+x)^20.\n\nThe patch adds in some derivative calculations.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3731\n\n",
    "created_at": "2008-07-27T15:32:24Z",
    "labels": [
        "component: calculus",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1",
    "title": "[with patch, needs review] missing some derivatives in wester",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3731",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: @garyfurnish

Keywords: wester, calculus

There is an example in sage.calculus.wester starting like this:

```
sage: # (YES) Expand (1+x)^20, take derivative and factorize. 
```

The ensuing calculation involves no derivatives, just expanding and factoring (1+x)^20.

The patch adds in some derivative calculations.



Issue created by migration from https://trac.sagemath.org/ticket/3731





---

archive/issue_comments_026432.json:
```json
{
    "body": "Attachment [3731.patch](tarball://root/attachments/some-uuid/ticket3731/3731.patch) by @jhpalmieri created at 2008-07-27 15:32:49",
    "created_at": "2008-07-27T15:32:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3731#issuecomment-26432",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [3731.patch](tarball://root/attachments/some-uuid/ticket3731/3731.patch) by @jhpalmieri created at 2008-07-27 15:32:49



---

archive/issue_comments_026433.json:
```json
{
    "body": "Attachment [3731.2.patch](tarball://root/attachments/some-uuid/ticket3731/3731.2.patch) by @jhpalmieri created at 2008-07-27 20:29:03",
    "created_at": "2008-07-27T20:29:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3731#issuecomment-26433",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [3731.2.patch](tarball://root/attachments/some-uuid/ticket3731/3731.2.patch) by @jhpalmieri created at 2008-07-27 20:29:03



---

archive/issue_comments_026434.json:
```json
{
    "body": "I'm not sure why there are two patches here; when submitting the second one, I must have forgotten to check the box about replacing patches with the same name.  Ignore the first patch.",
    "created_at": "2008-07-29T20:33:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3731#issuecomment-26434",
    "user": "https://github.com/jhpalmieri"
}
```

I'm not sure why there are two patches here; when submitting the second one, I must have forgotten to check the box about replacing patches with the same name.  Ignore the first patch.



---

archive/issue_comments_026435.json:
```json
{
    "body": "Fine by me.",
    "created_at": "2008-08-11T06:12:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3731#issuecomment-26435",
    "user": "https://github.com/ncalexan"
}
```

Fine by me.



---

archive/issue_comments_026436.json:
```json
{
    "body": "Merged 3731.2.patch in Sage 3.1.alpha1",
    "created_at": "2008-08-11T07:42:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3731#issuecomment-26436",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged 3731.2.patch in Sage 3.1.alpha1



---

archive/issue_comments_026437.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-11T07:42:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3731#issuecomment-26437",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_003955.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-08-11T07:42:06Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3731",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3731#event-3955"
}
```
