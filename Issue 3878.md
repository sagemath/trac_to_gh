# Issue 3878: Constructing a c_graph from a DiGraph doubles the edges.

archive/issues_003878.json:
```json
{
    "body": "Assignee: @rlmill\n\nKeywords: c_graph\n\n\n```\nsage: D = DiGraph({0:[1]})\nsage: D.edges()\n[(0, 1, None)]\nsage: DiGraph(D).edges()\n[(0, 1, None)]\nsage: DiGraph(D,implementation=\"c_graph\").edges()\n[(0, 1, None), (1, 0, None)]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3878\n\n",
    "created_at": "2008-08-16T08:30:54Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1",
    "title": "Constructing a c_graph from a DiGraph doubles the edges.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3878",
    "user": "https://github.com/saliola"
}
```
Assignee: @rlmill

Keywords: c_graph


```
sage: D = DiGraph({0:[1]})
sage: D.edges()
[(0, 1, None)]
sage: DiGraph(D).edges()
[(0, 1, None)]
sage: DiGraph(D,implementation="c_graph").edges()
[(0, 1, None), (1, 0, None)]
```


Issue created by migration from https://trac.sagemath.org/ticket/3878





---

archive/issue_comments_027616.json:
```json
{
    "body": "Attachment [trac_3878-fixed.patch](tarball://root/attachments/some-uuid/ticket3878/trac_3878-fixed.patch) by @saliola created at 2008-08-16 08:55:38",
    "created_at": "2008-08-16T08:55:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3878#issuecomment-27616",
    "user": "https://github.com/saliola"
}
```

Attachment [trac_3878-fixed.patch](tarball://root/attachments/some-uuid/ticket3878/trac_3878-fixed.patch) by @saliola created at 2008-08-16 08:55:38



---

archive/issue_comments_027617.json:
```json
{
    "body": "D'OH",
    "created_at": "2008-08-16T09:29:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3878#issuecomment-27617",
    "user": "https://github.com/rlmill"
}
```

D'OH



---

archive/issue_comments_027618.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-16T21:49:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3878#issuecomment-27618",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_027619.json:
```json
{
    "body": "Merged in Sage 3.1.final",
    "created_at": "2008-08-16T21:49:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3878#issuecomment-27619",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.final
