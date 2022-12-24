# Issue 3703: [with patch, needs review] bug in set_edge_label

archive/issues_003703.json:
```json
{
    "body": "Assignee: @rlmill\n\n\n```\nsage: G = Graph({0:{1:1}}, implementation='c_graph')\nsage: G.num_edges()\n1\nsage: G.set_edge_label(0,1,1)\nsage: G.num_edges()\n2\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3703\n\n",
    "created_at": "2008-07-22T00:17:40Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1",
    "title": "[with patch, needs review] bug in set_edge_label",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3703",
    "user": "@rlmill"
}
```
Assignee: @rlmill


```
sage: G = Graph({0:{1:1}}, implementation='c_graph')
sage: G.num_edges()
1
sage: G.set_edge_label(0,1,1)
sage: G.num_edges()
2
```


Issue created by migration from https://trac.sagemath.org/ticket/3703





---

archive/issue_comments_026262.json:
```json
{
    "body": "Attachment [trac3703-set_edge_label.patch](tarball://root/attachments/some-uuid/ticket3703/trac3703-set_edge_label.patch) by @jasongrout created at 2008-07-22 14:49:19\n\nPositive review.  Good catch!\n\nPasses doctests in graphs/*.py, graphs/*.pyx, and graphs/base/*.pyx",
    "created_at": "2008-07-22T14:49:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3703",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3703#issuecomment-26262",
    "user": "@jasongrout"
}
```

Attachment [trac3703-set_edge_label.patch](tarball://root/attachments/some-uuid/ticket3703/trac3703-set_edge_label.patch) by @jasongrout created at 2008-07-22 14:49:19

Positive review.  Good catch!

Passes doctests in graphs/*.py, graphs/*.pyx, and graphs/base/*.pyx



---

archive/issue_comments_026263.json:
```json
{
    "body": "I spent most of a day hunting for this one; I wasn't expecting to find it where I did. I was writing new code, so I was convinced it was there...",
    "created_at": "2008-07-22T16:36:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3703",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3703#issuecomment-26263",
    "user": "@rlmill"
}
```

I spent most of a day hunting for this one; I wasn't expecting to find it where I did. I was writing new code, so I was convinced it was there...



---

archive/issue_comments_026264.json:
```json
{
    "body": "That's a nice blog post you have talking about finding this bug:\n\nhttp://rlmill.blogspot.com/2008/07/adinkras.html",
    "created_at": "2008-07-25T15:00:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3703",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3703#issuecomment-26264",
    "user": "@jasongrout"
}
```

That's a nice blog post you have talking about finding this bug:

http://rlmill.blogspot.com/2008/07/adinkras.html



---

archive/issue_comments_026265.json:
```json
{
    "body": "This has been sitting positively reviewed for several release cycles now. What's going on??",
    "created_at": "2008-07-30T20:07:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3703",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3703#issuecomment-26265",
    "user": "@rlmill"
}
```

This has been sitting positively reviewed for several release cycles now. What's going on??



---

archive/issue_comments_026266.json:
```json
{
    "body": "Replying to [comment:5 rlm]:\n> This has been sitting positively reviewed for several release cycles now. What's going on??\n\n3.0.5 was supposed to be ultra stable, but one bug introduced mandated another 3.0.6 stable release. So this patch fell by the side. It will be merged in 3.1.alpha0 in a couple minutes provided the doctests pass.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-30T22:30:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3703",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3703#issuecomment-26266",
    "user": "mabshoff"
}
```

Replying to [comment:5 rlm]:
> This has been sitting positively reviewed for several release cycles now. What's going on??

3.0.5 was supposed to be ultra stable, but one bug introduced mandated another 3.0.6 stable release. So this patch fell by the side. It will be merged in 3.1.alpha0 in a couple minutes provided the doctests pass.

Cheers,

Michael



---

archive/issue_comments_026267.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-30T22:31:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3703",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3703#issuecomment-26267",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_026268.json:
```json
{
    "body": "Merged in Sage 3.1.alpha0",
    "created_at": "2008-07-30T22:31:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3703",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3703#issuecomment-26268",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.alpha0
