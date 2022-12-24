# Issue 3626: Graph.set_boundary only takes lists

archive/issues_003626.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @rlmill\n\n\n```\nsage: G = Graph(\"George\")\nsage: G.set_boundary(set([1,2,3]))\nsage: G.get_boundary()\n[]\n```\n\n\n... which makes sense, given the code...\n\n\n```\n    def set_boundary(self, boundary):\n        ...\n        if isinstance(boundary,list):\n            self._boundary = boundary\n\n    def set_embedding(self, embedding):\n        ...\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3626\n\n",
    "created_at": "2008-07-09T18:49:36Z",
    "labels": [
        "graph theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.6",
    "title": "Graph.set_boundary only takes lists",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3626",
    "user": "boothby"
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

archive/issue_comments_025661.json:
```json
{
    "body": "Attachment [3626_graphboundary.patch](tarball://root/attachments/some-uuid/ticket3626/3626_graphboundary.patch) by boothby created at 2008-07-09 18:53:37",
    "created_at": "2008-07-09T18:53:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3626",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3626#issuecomment-25661",
    "user": "boothby"
}
```

Attachment [3626_graphboundary.patch](tarball://root/attachments/some-uuid/ticket3626/3626_graphboundary.patch) by boothby created at 2008-07-09 18:53:37



---

archive/issue_comments_025662.json:
```json
{
    "body": "+1",
    "created_at": "2008-07-12T16:51:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3626",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3626#issuecomment-25662",
    "user": "@rlmill"
}
```

+1



---

archive/issue_comments_025663.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-16T00:42:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3626",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3626#issuecomment-25663",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_025664.json:
```json
{
    "body": "Merged in Sage 3.0.6.alpha0",
    "created_at": "2008-07-16T00:42:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3626",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3626#issuecomment-25664",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.6.alpha0
