# Issue 9610: int(finite field element) should only work when it is in the prime subfield

archive/issues_009610.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @malb\n\nThis was the real cause of #8406, and the fix there introduced the following bug:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: n = 20\nsage: k = 3\nsage: g = DiGraph()\nsage: g.add_edges( (i,Mod(i+j,n)) for i in range(n) for j in range(1,k+1) )\nsage: g.vertices()\n[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]\nsage: g.strongly_connected_components()\n[[0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]]\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/9610\n\n",
    "created_at": "2010-07-27T12:01:24Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.3",
    "title": "int(finite field element) should only work when it is in the prime subfield",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9610",
    "user": "https://github.com/rlmill"
}
```
Assignee: @williamstein

CC:  @malb

This was the real cause of #8406, and the fix there introduced the following bug:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: n = 20
sage: k = 3
sage: g = DiGraph()
sage: g.add_edges( (i,Mod(i+j,n)) for i in range(n) for j in range(1,k+1) )
sage: g.vertices()
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
sage: g.strongly_connected_components()
[[0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]]
```

Issue created by migration from https://trac.sagemath.org/ticket/9610





---

archive/issue_comments_092935.json:
```json
{
    "body": "Attachment [trac_9610.patch](tarball://root/attachments/some-uuid/ticket9610/trac_9610.patch) by @rlmill created at 2010-07-27 12:23:19",
    "created_at": "2010-07-27T12:23:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9610#issuecomment-92935",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_9610.patch](tarball://root/attachments/some-uuid/ticket9610/trac_9610.patch) by @rlmill created at 2010-07-27 12:23:19



---

archive/issue_comments_092936.json:
```json
{
    "body": "Looks good.",
    "created_at": "2010-07-27T12:25:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9610#issuecomment-92936",
    "user": "https://github.com/malb"
}
```

Looks good.



---

archive/issue_comments_092937.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-27T12:25:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9610#issuecomment-92937",
    "user": "https://github.com/malb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_092938.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-27T12:25:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9610#issuecomment-92938",
    "user": "https://github.com/malb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_023942.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-08-09T09:40:36Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9610",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9610#event-23942"
}
```



---

archive/issue_comments_092939.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-08-09T09:40:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9610#issuecomment-92939",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
