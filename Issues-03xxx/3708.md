# Issue 3708: [with patch, positive review] something screwy in the reference manual -- very easy to fix!

archive/issues_003708.json:
```json
{
    "body": "Assignee: wdjoyner\n\nIn the reference manual see the \"AUTHOR:\"\n\n```\n39. Coding Theory\n\n    * 39.1 Linear Codes\n    * 39.2 AUTHOR: \n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/3708\n\n",
    "closed_at": "2008-07-31T03:54:22Z",
    "created_at": "2008-07-22T14:17:04Z",
    "labels": [
        "component: coding theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1",
    "title": "[with patch, positive review] something screwy in the reference manual -- very easy to fix!",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3708",
    "user": "https://github.com/williamstein"
}
```
Assignee: wdjoyner

In the reference manual see the "AUTHOR:"

```
39. Coding Theory

    * 39.1 Linear Codes
    * 39.2 AUTHOR: 
```

Issue created by migration from https://trac.sagemath.org/ticket/3708





---

archive/issue_comments_026267.json:
```json
{
    "body": "Attachment [10104.patch](tarball://root/attachments/some-uuid/ticket3708/10104.patch) by @wdjoyner created at 2008-07-22 15:25:43\n\npatch based on 3.0.6.rc0",
    "created_at": "2008-07-22T15:25:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3708",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3708#issuecomment-26267",
    "user": "https://github.com/wdjoyner"
}
```

Attachment [10104.patch](tarball://root/attachments/some-uuid/ticket3708/10104.patch) by @wdjoyner created at 2008-07-22 15:25:43

patch based on 3.0.6.rc0



---

archive/issue_comments_026268.json:
```json
{
    "body": "Patch attached. One liner added to a docstring, so did not run sage -testall. (I'll run this right now and post in a few hours if there is a failure.)",
    "created_at": "2008-07-22T15:26:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3708",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3708#issuecomment-26268",
    "user": "https://github.com/wdjoyner"
}
```

Patch attached. One liner added to a docstring, so did not run sage -testall. (I'll run this right now and post in a few hours if there is a failure.)



---

archive/issue_comments_026269.json:
```json
{
    "body": "I applied the patch ok and did \"sage -br\", then opened a notebook and clicked through to the ref manual, but the AUTHOR entry was still there.  If you can tell me how to get the manual to rebuild then I'll happily give this a positive review.",
    "created_at": "2008-07-29T01:39:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3708",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3708#issuecomment-26269",
    "user": "https://github.com/JohnCremona"
}
```

I applied the patch ok and did "sage -br", then opened a notebook and clicked through to the ref manual, but the AUTHOR entry was still there.  If you can tell me how to get the manual to rebuild then I'll happily give this a positive review.



---

archive/issue_comments_026270.json:
```json
{
    "body": "With rebuild in doc the issue is fixed in the documentation. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-31T03:53:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3708",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3708#issuecomment-26270",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

With rebuild in doc the issue is fixed in the documentation. Positive review.

Cheers,

Michael



---

archive/issue_comments_026271.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-31T03:54:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3708",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3708#issuecomment-26271",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_008486.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-07-31T03:54:22Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3708",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3708#event-8486"
}
```



---

archive/issue_comments_026272.json:
```json
{
    "body": "Merged in Sage 3.1.alpha0",
    "created_at": "2008-07-31T03:54:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3708",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3708#issuecomment-26272",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.alpha0
