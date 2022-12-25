# Issue 9485: Fix strongly_connected_components_digraph to actually do something

archive/issues_009485.json:
```json
{
    "body": "Assignee: jason, ncohen, rlm\n\nCC:  sage-combinat @rlmill\n\nKeywords: strongly connected components\n\nGraphs produced with strongly_connected_components_digraph had no\nedges in them due to a typo in the code:\n\n```\n    sage: g = DiGraph({0:[1,2,3],1:[2],2:[1,3]})\n    sage: scc_digraph = g.strongly_connected_components_digraph()\n    sage: scc_digraph.vertices()\n    [{0}, {3}, {1, 2}]\n    sage: scc_digraph.edges()\n    []\n```\n\nAfter this patch, the result is more likely to be correct:\n\n```\n    [({0}, {3}, None), ({0}, {1, 2}, None), ({1, 2}, {3}, None)]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9485\n\n",
    "created_at": "2010-07-12T18:55:21Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "Fix strongly_connected_components_digraph to actually do something",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9485",
    "user": "https://github.com/nthiery"
}
```
Assignee: jason, ncohen, rlm

CC:  sage-combinat @rlmill

Keywords: strongly connected components

Graphs produced with strongly_connected_components_digraph had no
edges in them due to a typo in the code:

```
    sage: g = DiGraph({0:[1,2,3],1:[2],2:[1,3]})
    sage: scc_digraph = g.strongly_connected_components_digraph()
    sage: scc_digraph.vertices()
    [{0}, {3}, {1, 2}]
    sage: scc_digraph.edges()
    []
```

After this patch, the result is more likely to be correct:

```
    [({0}, {3}, None), ({0}, {1, 2}, None), ({1, 2}, {3}, None)]
```


Issue created by migration from https://trac.sagemath.org/ticket/9485





---

archive/issue_comments_090913.json:
```json
{
    "body": "Attachment [trac_9485-strongly_connected_componnents_digraph-fix-nt.patch](tarball://root/attachments/some-uuid/ticket9485/trac_9485-strongly_connected_componnents_digraph-fix-nt.patch) by @nthiery created at 2010-07-12 19:01:15",
    "created_at": "2010-07-12T19:01:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9485#issuecomment-90913",
    "user": "https://github.com/nthiery"
}
```

Attachment [trac_9485-strongly_connected_componnents_digraph-fix-nt.patch](tarball://root/attachments/some-uuid/ticket9485/trac_9485-strongly_connected_componnents_digraph-fix-nt.patch) by @nthiery created at 2010-07-12 19:01:15



---

archive/issue_comments_090914.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-12T19:03:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9485#issuecomment-90914",
    "user": "https://github.com/nthiery"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_090915.json:
```json
{
    "body": "Oops... Some very, very bad typo ... Thank youuuuuuu ! :-)\n\nNathann",
    "created_at": "2010-07-12T23:11:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9485#issuecomment-90915",
    "user": "https://github.com/nathanncohen"
}
```

Oops... Some very, very bad typo ... Thank youuuuuuu ! :-)

Nathann



---

archive/issue_comments_090916.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-12T23:11:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9485#issuecomment-90916",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_090917.json:
```json
{
    "body": "Thanks for the instantaneous review!\n\nAnd thanks as well for the original code. It was still quicker for me to fix it than to have to implement it myself :-)",
    "created_at": "2010-07-13T13:41:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9485#issuecomment-90917",
    "user": "https://github.com/nthiery"
}
```

Thanks for the instantaneous review!

And thanks as well for the original code. It was still quicker for me to fix it than to have to implement it myself :-)



---

archive/issue_events_023520.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-07-21T02:49:04Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9485",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9485#event-23520"
}
```



---

archive/issue_comments_090918.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-21T02:49:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9485#issuecomment-90918",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
