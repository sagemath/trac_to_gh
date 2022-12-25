# Issue 3703: [with patch, positive review] bug in set_edge_label

archive/issues_003703.json:
```json
{
    "body": "Assignee: @rlmill\n\n```\nsage: G = Graph({0:{1:1}}, implementation='c_graph')\nsage: G.num_edges()\n1\nsage: G.set_edge_label(0,1,1)\nsage: G.num_edges()\n2\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/3703\n\n",
    "closed_at": "2008-07-30T22:31:39Z",
    "created_at": "2008-07-22T00:17:40Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1",
    "title": "[with patch, positive review] bug in set_edge_label",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3703",
    "user": "https://github.com/rlmill"
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

archive/issue_comments_026207.json:
```json
{
    "body": "Attachment [trac3703-set_edge_label.patch](tarball://root/attachments/some-uuid/ticket3703/trac3703-set_edge_label.patch) by @jasongrout created at 2008-07-22 14:49:19\n\nPositive review.  Good catch!\n\nPasses doctests in graphs/*.py, graphs/*.pyx, and graphs/base/*.pyx",
    "created_at": "2008-07-22T14:49:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3703",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3703#issuecomment-26207",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac3703-set_edge_label.patch](tarball://root/attachments/some-uuid/ticket3703/trac3703-set_edge_label.patch) by @jasongrout created at 2008-07-22 14:49:19

Positive review.  Good catch!

Passes doctests in graphs/*.py, graphs/*.pyx, and graphs/base/*.pyx



---

archive/issue_comments_026208.json:
```json
{
    "body": "I spent most of a day hunting for this one; I wasn't expecting to find it where I did. I was writing new code, so I was convinced it was there...",
    "created_at": "2008-07-22T16:36:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3703",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3703#issuecomment-26208",
    "user": "https://github.com/rlmill"
}
```

I spent most of a day hunting for this one; I wasn't expecting to find it where I did. I was writing new code, so I was convinced it was there...



---

archive/issue_comments_026209.json:
```json
{
    "body": "That's a nice blog post you have talking about finding this bug:\n\nhttp://rlmill.blogspot.com/2008/07/adinkras.html",
    "created_at": "2008-07-25T15:00:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3703",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3703#issuecomment-26209",
    "user": "https://github.com/jasongrout"
}
```

That's a nice blog post you have talking about finding this bug:

http://rlmill.blogspot.com/2008/07/adinkras.html



---

archive/issue_events_008477.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2008-07-25T19:46:43Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3703",
    "milestone": "sage-3.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3703#event-8477"
}
```



---

archive/issue_comments_026210.json:
```json
{
    "body": "This has been sitting positively reviewed for several release cycles now. What's going on??",
    "created_at": "2008-07-30T20:07:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3703",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3703#issuecomment-26210",
    "user": "https://github.com/rlmill"
}
```

This has been sitting positively reviewed for several release cycles now. What's going on??



---

archive/issue_comments_026211.json:
```json
{
    "body": "Replying to [comment:5 rlm]:\n> This has been sitting positively reviewed for several release cycles now. What's going on??\n\n\n3.0.5 was supposed to be ultra stable, but one bug introduced mandated another 3.0.6 stable release. So this patch fell by the side. It will be merged in 3.1.alpha0 in a couple minutes provided the doctests pass.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-30T22:30:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3703",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3703#issuecomment-26211",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:5 rlm]:
> This has been sitting positively reviewed for several release cycles now. What's going on??


3.0.5 was supposed to be ultra stable, but one bug introduced mandated another 3.0.6 stable release. So this patch fell by the side. It will be merged in 3.1.alpha0 in a couple minutes provided the doctests pass.

Cheers,

Michael



---

archive/issue_events_008478.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-07-30T22:31:39Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3703",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3703#event-8478"
}
```



---

archive/issue_comments_026212.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-30T22:31:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3703",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3703#issuecomment-26212",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_026213.json:
```json
{
    "body": "Merged in Sage 3.1.alpha0",
    "created_at": "2008-07-30T22:31:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3703",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3703#issuecomment-26213",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.alpha0
