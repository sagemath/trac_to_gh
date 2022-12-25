# Issue 3626: Graph.set_boundary only takes lists

archive/issues_003626.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @rlmill\n\n```\nsage: G = Graph(\"George\")\nsage: G.set_boundary(set([1,2,3]))\nsage: G.get_boundary()\n[]\n```\n\n... which makes sense, given the code...\n\n```\n    def set_boundary(self, boundary):\n        ...\n        if isinstance(boundary,list):\n            self._boundary = boundary\n\n    def set_embedding(self, embedding):\n        ...\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3626\n\n",
    "created_at": "2008-07-09T18:49:36Z",
    "labels": [
        "component: graph theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.6",
    "title": "Graph.set_boundary only takes lists",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3626",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```
Assignee: boothby

CC:  @rlmill

```
sage: G = Graph("George")
sage: G.set_boundary(set([1,2,3]))
sage: G.get_boundary()
[]
```

... which makes sense, given the code...

```
    def set_boundary(self, boundary):
        ...
        if isinstance(boundary,list):
            self._boundary = boundary

    def set_embedding(self, embedding):
        ...
```


Issue created by migration from https://trac.sagemath.org/ticket/3626





---

archive/issue_comments_025608.json:
```json
{
    "body": "Attachment [3626_graphboundary.patch](tarball://root/attachments/some-uuid/ticket3626/3626_graphboundary.patch) by boothby created at 2008-07-09 18:53:37",
    "created_at": "2008-07-09T18:53:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3626",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3626#issuecomment-25608",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Attachment [3626_graphboundary.patch](tarball://root/attachments/some-uuid/ticket3626/3626_graphboundary.patch) by boothby created at 2008-07-09 18:53:37



---

archive/issue_comments_025609.json:
```json
{
    "body": "+1",
    "created_at": "2008-07-12T16:51:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3626",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3626#issuecomment-25609",
    "user": "https://github.com/rlmill"
}
```

+1



---

archive/issue_comments_025610.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-16T00:42:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3626",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3626#issuecomment-25610",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_008327.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-07-16T00:42:12Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3626",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3626#event-8327"
}
```



---

archive/issue_comments_025611.json:
```json
{
    "body": "Merged in Sage 3.0.6.alpha0",
    "created_at": "2008-07-16T00:42:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3626",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3626#issuecomment-25611",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.6.alpha0
