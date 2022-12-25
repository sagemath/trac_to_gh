# Issue 6659: cores() is broken for some digraphs, and is *way* too slow

archive/issues_006659.json:
```json
{
    "body": "Assignee: @rlmill\n\nCC:  @rlmill @rbeezer hartke\n\nHere is a patch, based on the networkx code, which implements some of the optimizations noted in the paper referenced in the networkx documentation.  This leads to what I think are asymptotic speedups.\n\nAs for the bug, before, the doctest added would fail from an error in the networkx code.  Now it does not.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6659\n\n",
    "created_at": "2009-07-30T08:38:51Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "cores() is broken for some digraphs, and is *way* too slow",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6659",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @rlmill

CC:  @rlmill @rbeezer hartke

Here is a patch, based on the networkx code, which implements some of the optimizations noted in the paper referenced in the networkx documentation.  This leads to what I think are asymptotic speedups.

As for the bug, before, the doctest added would fail from an error in the networkx code.  Now it does not.

Issue created by migration from https://trac.sagemath.org/ticket/6659





---

archive/issue_comments_054562.json:
```json
{
    "body": "I fixed a bug (the doctest I added used to fail), implemented some optimizations that massively sped things up, and cleaned up the documentation.\n\nRobert or Rob, can one of you review this so it can go into 4.1.1?",
    "created_at": "2009-07-30T09:35:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6659#issuecomment-54562",
    "user": "https://github.com/jasongrout"
}
```

I fixed a bug (the doctest I added used to fail), implemented some optimizations that massively sped things up, and cleaned up the documentation.

Robert or Rob, can one of you review this so it can go into 4.1.1?



---

archive/issue_comments_054563.json:
```json
{
    "body": "An example of a speedup:\n\nBEFORE:\n\n\n```\nsage: a=random_matrix(GF(2), 50000, density=0.0001,sparse=True)\nsage: len(a.nonzero_positions())\n125063\nsage: c=DiGraph(50000)\nsage: c.add_edges(a.nonzero_positions())\nsage: %time\nsage: e=c.cores(with_labels=True)\nCPU time: 429.14 s,  Wall time: 430.89 s\n```\n\n\nAFTER:\n\n\n```\nsage: d=c.cores(with_labels=True)\nCPU time: 1.86 s,  Wall time: 1.86 s\nsage: e==d\nTrue\n```\n",
    "created_at": "2009-07-30T09:39:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6659#issuecomment-54563",
    "user": "https://github.com/jasongrout"
}
```

An example of a speedup:

BEFORE:


```
sage: a=random_matrix(GF(2), 50000, density=0.0001,sparse=True)
sage: len(a.nonzero_positions())
125063
sage: c=DiGraph(50000)
sage: c.add_edges(a.nonzero_positions())
sage: %time
sage: e=c.cores(with_labels=True)
CPU time: 429.14 s,  Wall time: 430.89 s
```


AFTER:


```
sage: d=c.cores(with_labels=True)
CPU time: 1.86 s,  Wall time: 1.86 s
sage: e==d
True
```




---

archive/issue_comments_054564.json:
```json
{
    "body": "Attachment [trac_6659-graph-cores.patch](tarball://root/attachments/some-uuid/ticket6659/trac_6659-graph-cores.patch) by @jasongrout created at 2009-07-31 07:28:59\n\nI added a couple of comments to help the reader see what is happening in the source code.",
    "created_at": "2009-07-31T07:28:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6659#issuecomment-54564",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac_6659-graph-cores.patch](tarball://root/attachments/some-uuid/ticket6659/trac_6659-graph-cores.patch) by @jasongrout created at 2009-07-31 07:28:59

I added a couple of comments to help the reader see what is happening in the source code.



---

archive/issue_comments_054565.json:
```json
{
    "body": "reviewer patch; typo fix",
    "created_at": "2009-08-25T02:21:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6659#issuecomment-54565",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

reviewer patch; typo fix



---

archive/issue_comments_054566.json:
```json
{
    "body": "Attachment [trac_6659-reviewer.patch](tarball://root/attachments/some-uuid/ticket6659/trac_6659-reviewer.patch) by mvngu created at 2009-08-25 02:22:16\n\nThe patch `trac_6659-reviewer.patch` fixes a typo found in `trac_6659-graph-cores.patch`.",
    "created_at": "2009-08-25T02:22:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6659#issuecomment-54566",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_6659-reviewer.patch](tarball://root/attachments/some-uuid/ticket6659/trac_6659-reviewer.patch) by mvngu created at 2009-08-25 02:22:16

The patch `trac_6659-reviewer.patch` fixes a typo found in `trac_6659-graph-cores.patch`.



---

archive/issue_comments_054567.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-25T03:04:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6659#issuecomment-54567",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_006895.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-08-25T03:04:27Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6659",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6659#event-6895"
}
```



---

archive/issue_comments_054568.json:
```json
{
    "body": "Merged both patches.",
    "created_at": "2009-08-25T03:05:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6659#issuecomment-54568",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged both patches.
