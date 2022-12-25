# Issue 2615: wish: compute the jordan basis together with the jordan canonical form

archive/issues_002615.json:
```json
{
    "body": "Assignee: @williamstein\n\nSage has now an implementation of the Jordan canonical form (see #874)\n\nHowever for most applications (like computing the exponential of a matrix,\nsee #2273) we would need to be able to compute not only the Jordan form, but\nthe Jordan basis as well (or what is equivalent the coordinate-change matrix P\nsuch that P^(-1) A P = J, where A is the matrix, and J is its Jordan normal form)\n\n(As far as I know, Maple can do that)\n\nIssue created by migration from https://trac.sagemath.org/ticket/2615\n\n",
    "created_at": "2008-03-20T14:51:21Z",
    "labels": [
        "component: linear algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "wish: compute the jordan basis together with the jordan canonical form",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2615",
    "user": "https://github.com/pdenapo"
}
```
Assignee: @williamstein

Sage has now an implementation of the Jordan canonical form (see #874)

However for most applications (like computing the exponential of a matrix,
see #2273) we would need to be able to compute not only the Jordan form, but
the Jordan basis as well (or what is equivalent the coordinate-change matrix P
such that P^(-1) A P = J, where A is the matrix, and J is its Jordan normal form)

(As far as I know, Maple can do that)

Issue created by migration from https://trac.sagemath.org/ticket/2615





---

archive/issue_comments_017911.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-04-15T04:10:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2615#issuecomment-17911",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_017912.json:
```json
{
    "body": "Changing assignee from @williamstein to @mwhansen.",
    "created_at": "2008-04-15T04:10:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2615#issuecomment-17912",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from @williamstein to @mwhansen.



---

archive/issue_comments_017913.json:
```json
{
    "body": "Attachment [2615.patch](tarball://root/attachments/some-uuid/ticket2615/2615.patch) by @mwhansen created at 2008-04-15 22:21:54",
    "created_at": "2008-04-15T22:21:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2615#issuecomment-17913",
    "user": "https://github.com/mwhansen"
}
```

Attachment [2615.patch](tarball://root/attachments/some-uuid/ticket2615/2615.patch) by @mwhansen created at 2008-04-15 22:21:54



---

archive/issue_comments_017914.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-04-15T23:40:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2615#issuecomment-17914",
    "user": "https://github.com/aghitza"
}
```

Looks good to me.



---

archive/issue_events_002805.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-04-16T01:43:44Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2615",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2615#event-2805"
}
```



---

archive/issue_comments_017915.json:
```json
{
    "body": "Merged in Sagr 3.0.alpha6",
    "created_at": "2008-04-16T01:43:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2615#issuecomment-17915",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sagr 3.0.alpha6



---

archive/issue_comments_017916.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-16T01:43:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2615#issuecomment-17916",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
