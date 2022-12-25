# Issue 1088: [with patch] graphs: minimum spanning tree function

archive/issues_001088.json:
```json
{
    "body": "Assignee: @mwhansen\n\nKeywords: graphs\n\nHere's an implementation of a minimum spanning tree function.  Well, actually 3 implementations, defaulting to Kruskal's algorithm.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1088\n\n",
    "created_at": "2007-11-03T20:45:05Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.12",
    "title": "[with patch] graphs: minimum spanning tree function",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1088",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @mwhansen

Keywords: graphs

Here's an implementation of a minimum spanning tree function.  Well, actually 3 implementations, defaulting to Kruskal's algorithm.

Issue created by migration from https://trac.sagemath.org/ticket/1088





---

archive/issue_comments_006564.json:
```json
{
    "body": "Attachment [minspantree.patch](tarball://root/attachments/some-uuid/ticket1088/minspantree.patch) by @jasongrout created at 2007-11-03 20:45:18",
    "created_at": "2007-11-03T20:45:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1088",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1088#issuecomment-6564",
    "user": "https://github.com/jasongrout"
}
```

Attachment [minspantree.patch](tarball://root/attachments/some-uuid/ticket1088/minspantree.patch) by @jasongrout created at 2007-11-03 20:45:18



---

archive/issue_comments_006565.json:
```json
{
    "body": "Attachment [doc_1088.patch](tarball://root/attachments/some-uuid/ticket1088/doc_1088.patch) by @rlmill created at 2007-11-03 23:20:23",
    "created_at": "2007-11-03T23:20:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1088",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1088#issuecomment-6565",
    "user": "https://github.com/rlmill"
}
```

Attachment [doc_1088.patch](tarball://root/attachments/some-uuid/ticket1088/doc_1088.patch) by @rlmill created at 2007-11-03 23:20:23



---

archive/issue_comments_006566.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-03T23:38:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1088",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1088#issuecomment-6566",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_001212.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-11-03T23:38:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1088",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1088#event-1212"
}
```



---

archive/issue_comments_006567.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2007-11-06T22:36:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1088",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1088#issuecomment-6567",
    "user": "https://github.com/jasongrout"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_006568.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-11-06T22:36:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1088",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1088#issuecomment-6568",
    "user": "https://github.com/jasongrout"
}
```

Changing status from closed to reopened.



---

archive/issue_events_001213.json:
```json
{
    "actor": "https://github.com/jasongrout",
    "created_at": "2007-11-06T22:36:49Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/1088",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1088#event-1213"
}
```



---

archive/issue_comments_006569.json:
```json
{
    "body": "I believe there is a bug in the code change of the doc_1088 patch above.  The third patch (1088-correct-bugs-improve-doctests.patch) reverses this change, reimplements the doctests, and makes the code faster by sorting using key instead of cmp.\n\nThe third doctest should be applied after the first two doctests.",
    "created_at": "2007-11-06T22:36:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1088",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1088#issuecomment-6569",
    "user": "https://github.com/jasongrout"
}
```

I believe there is a bug in the code change of the doc_1088 patch above.  The third patch (1088-correct-bugs-improve-doctests.patch) reverses this change, reimplements the doctests, and makes the code faster by sorting using key instead of cmp.

The third doctest should be applied after the first two doctests.



---

archive/issue_comments_006570.json:
```json
{
    "body": "Attachment [1088-correct-bugs-improve-doctests.patch](tarball://root/attachments/some-uuid/ticket1088/1088-correct-bugs-improve-doctests.patch) by @jasongrout created at 2007-11-06 22:37:16",
    "created_at": "2007-11-06T22:37:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1088",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1088#issuecomment-6570",
    "user": "https://github.com/jasongrout"
}
```

Attachment [1088-correct-bugs-improve-doctests.patch](tarball://root/attachments/some-uuid/ticket1088/1088-correct-bugs-improve-doctests.patch) by @jasongrout created at 2007-11-06 22:37:16



---

archive/issue_comments_006571.json:
```json
{
    "body": "The third patch above also corrects a bug in the original code.",
    "created_at": "2007-11-06T22:38:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1088",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1088#issuecomment-6571",
    "user": "https://github.com/jasongrout"
}
```

The third patch above also corrects a bug in the original code.



---

archive/issue_comments_006572.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-06T23:54:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1088",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1088#issuecomment-6572",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_001214.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-11-06T23:54:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1088",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1088#event-1214"
}
```
