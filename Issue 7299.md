# Issue 7299: show() regression: Picture cropped too much

archive/issues_007299.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @rlmill @rbeezer\n\nIn sage 4.1.2 and later, the show() function shows graphs so cropped that their vertices are partially missing.\n\nThis is a regression in 4.1.2 and later, Sage 4.1.1 is fine.\n\nAttaching the figures from\n\n```\nG=graphs.CycleGraph(3);G.show()\n```\nto show the issue.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7299\n\n",
    "created_at": "2009-10-25T18:26:25Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "show() regression: Picture cropped too much",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7299",
    "user": "https://github.com/haaninjo"
}
```
Assignee: @williamstein

CC:  @rlmill @rbeezer

In sage 4.1.2 and later, the show() function shows graphs so cropped that their vertices are partially missing.

This is a regression in 4.1.2 and later, Sage 4.1.1 is fine.

Attaching the figures from

```
G=graphs.CycleGraph(3);G.show()
```
to show the issue.

Issue created by migration from https://trac.sagemath.org/ticket/7299





---

archive/issue_comments_060723.json:
```json
{
    "body": "Attachment [Triangle-sage_4.1.1.png](tarball://root/attachments/some-uuid/ticket7299/Triangle-sage_4.1.1.png) by @haaninjo created at 2009-10-25 18:27:11\n\nTriangle graph in 4.1.1",
    "created_at": "2009-10-25T18:27:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7299#issuecomment-60723",
    "user": "https://github.com/haaninjo"
}
```

Attachment [Triangle-sage_4.1.1.png](tarball://root/attachments/some-uuid/ticket7299/Triangle-sage_4.1.1.png) by @haaninjo created at 2009-10-25 18:27:11

Triangle graph in 4.1.1



---

archive/issue_comments_060724.json:
```json
{
    "body": "Attachment [Triangle-Sage_4.1.2.png](tarball://root/attachments/some-uuid/ticket7299/Triangle-Sage_4.1.2.png) by @haaninjo created at 2009-10-25 18:27:32\n\nTriangle graph in 4.1.2",
    "created_at": "2009-10-25T18:27:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7299#issuecomment-60724",
    "user": "https://github.com/haaninjo"
}
```

Attachment [Triangle-Sage_4.1.2.png](tarball://root/attachments/some-uuid/ticket7299/Triangle-Sage_4.1.2.png) by @haaninjo created at 2009-10-25 18:27:32

Triangle graph in 4.1.2



---

archive/issue_comments_060725.json:
```json
{
    "body": "Attachment [trac-7299-graph-pad.patch](tarball://root/attachments/some-uuid/ticket7299/trac-7299-graph-pad.patch) by @jasongrout created at 2010-01-20 10:54:19",
    "created_at": "2010-01-20T10:54:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7299#issuecomment-60725",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-7299-graph-pad.patch](tarball://root/attachments/some-uuid/ticket7299/trac-7299-graph-pad.patch) by @jasongrout created at 2010-01-20 10:54:19



---

archive/issue_comments_060726.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-20T10:54:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7299#issuecomment-60726",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_060727.json:
```json
{
    "body": "The attached patch is a one-line fix that makes graph vertices not be cut off now.",
    "created_at": "2010-01-20T10:54:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7299#issuecomment-60727",
    "user": "https://github.com/jasongrout"
}
```

The attached patch is a one-line fix that makes graph vertices not be cut off now.



---

archive/issue_comments_060728.json:
```json
{
    "body": "LGTM. Such a small change for a big impact.",
    "created_at": "2010-01-20T10:58:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7299#issuecomment-60728",
    "user": "https://github.com/robertwb"
}
```

LGTM. Such a small change for a big impact.



---

archive/issue_comments_060729.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-20T10:58:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7299#issuecomment-60729",
    "user": "https://github.com/robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_017277.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-01-23T22:45:47Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7299",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7299#event-17277"
}
```



---

archive/issue_comments_060730.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-23T22:45:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7299#issuecomment-60730",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_060731.json:
```json
{
    "body": "Merged [trac-7299-graph-pad.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7299/trac-7299-graph-pad.patch).",
    "created_at": "2010-01-23T22:45:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7299#issuecomment-60731",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged [trac-7299-graph-pad.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7299/trac-7299-graph-pad.patch).
