# Issue 9375: more documentation & doctests for BalancedTree, BarbellGraph, BubbleSortGraph, BullGraph, ChvatalGraph

archive/issues_009375.json:
```json
{
    "body": "Assignee: jason, ncohen, rlm\n\nAs the subject says. \n\n**Prerequisite:** #9373\n\nIssue created by migration from https://trac.sagemath.org/ticket/9375\n\n",
    "created_at": "2010-06-29T17:33:48Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "more documentation & doctests for BalancedTree, BarbellGraph, BubbleSortGraph, BullGraph, ChvatalGraph",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9375",
    "user": "mvngu"
}
```
Assignee: jason, ncohen, rlm

As the subject says. 

**Prerequisite:** #9373

Issue created by migration from https://trac.sagemath.org/ticket/9375





---

archive/issue_comments_089085.json:
```json
{
    "body": "Attachment [trac_9375-graph-doctests.patch](tarball://root/attachments/some-uuid/ticket9375/trac_9375-graph-doctests.patch) by mvngu created at 2010-06-29 17:39:50",
    "created_at": "2010-06-29T17:39:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9375",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9375#issuecomment-89085",
    "user": "mvngu"
}
```

Attachment [trac_9375-graph-doctests.patch](tarball://root/attachments/some-uuid/ticket9375/trac_9375-graph-doctests.patch) by mvngu created at 2010-06-29 17:39:50



---

archive/issue_comments_089086.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-29T17:40:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9375",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9375#issuecomment-89086",
    "user": "mvngu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_089087.json:
```json
{
    "body": "Excellent ! You can set this one to \"positive review\" immediately after #9375 :-)\n\nOne unimportant detail, though... You used subgraph_search in your doctests, the follwing way :\n\n\n```\nsage: s_K = g.subgraph_search(K_n1, induced=True) \nsage: s_P = g.subgraph_search(P_n2, induced=True) \nsage: K_n1.is_isomorphic(s_K) \n```\n\n\nWell, subgraph_search should of course *always* return subgraphs isomorphic to S_k. Actually, the order of the vertices should even be the same, but when it finds nothing, it returns a None, which is_isomorphic may not like... It's not really a problem in this case, as this would report a doctest failure anyway :-)\n\nNathann",
    "created_at": "2010-07-16T03:03:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9375",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9375#issuecomment-89087",
    "user": "@nathanncohen"
}
```

Excellent ! You can set this one to "positive review" immediately after #9375 :-)

One unimportant detail, though... You used subgraph_search in your doctests, the follwing way :


```
sage: s_K = g.subgraph_search(K_n1, induced=True) 
sage: s_P = g.subgraph_search(P_n2, induced=True) 
sage: K_n1.is_isomorphic(s_K) 
```


Well, subgraph_search should of course *always* return subgraphs isomorphic to S_k. Actually, the order of the vertices should even be the same, but when it finds nothing, it returns a None, which is_isomorphic may not like... It's not really a problem in this case, as this would report a doctest failure anyway :-)

Nathann



---

archive/issue_comments_089088.json:
```json
{
    "body": "Replying to [comment:2 ncohen]:\n> You can set this one to \"positive review\" immediately after #9375 :-)\n\nI don't understand what you mean. Care to elaborate on this point?",
    "created_at": "2010-07-16T05:28:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9375",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9375#issuecomment-89088",
    "user": "mvngu"
}
```

Replying to [comment:2 ncohen]:
> You can set this one to "positive review" immediately after #9375 :-)

I don't understand what you mean. Care to elaborate on this point?



---

archive/issue_comments_089089.json:
```json
{
    "body": "Sorry, I meant #9373 :-)\n\nIt was just to avoid having a ticket A depending on B such that a is positively reviewed while B is not.\n\nNathann",
    "created_at": "2010-07-16T05:36:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9375",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9375#issuecomment-89089",
    "user": "@nathanncohen"
}
```

Sorry, I meant #9373 :-)

It was just to avoid having a ticket A depending on B such that a is positively reviewed while B is not.

Nathann



---

archive/issue_comments_089090.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-16T05:36:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9375",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9375#issuecomment-89090",
    "user": "@nathanncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_089091.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-21T02:48:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9375",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9375#issuecomment-89091",
    "user": "@qed777"
}
```

Resolution: fixed
