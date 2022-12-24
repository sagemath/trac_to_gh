# Issue 8421: Change BipartiteGraph .left and .right to sets

archive/issues_008421.json:
```json
{
    "body": "Assignee: rlm\n\nCC:  rlm jason ncohen\n\nKeywords: BipartiteGraph, partitions, sets\n\nThe documentation describes the 'left' and 'right' attributes of BipartiteGrpah as sets.  And deleting vertices is much more efficient if they are.  But they are currently stored as lists.\n\n```\nsage: bg = BipartiteGraph(graphs.CycleGraph(4))\nsage: bg.left\n[0, 2]\n```\n\n\nOf course, it's easy to change from one to the other.  But we will get better performance from sets.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8421\n\n",
    "created_at": "2010-03-02T16:05:50Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "Change BipartiteGraph .left and .right to sets",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8421",
    "user": "rhinton"
}
```
Assignee: rlm

CC:  rlm jason ncohen

Keywords: BipartiteGraph, partitions, sets

The documentation describes the 'left' and 'right' attributes of BipartiteGrpah as sets.  And deleting vertices is much more efficient if they are.  But they are currently stored as lists.

```
sage: bg = BipartiteGraph(graphs.CycleGraph(4))
sage: bg.left
[0, 2]
```


Of course, it's easy to change from one to the other.  But we will get better performance from sets.


Issue created by migration from https://trac.sagemath.org/ticket/8421





---

archive/issue_comments_075481.json:
```json
{
    "body": "Changing assignee from rlm to rhinton.",
    "created_at": "2010-03-02T16:28:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8421#issuecomment-75481",
    "user": "rhinton"
}
```

Changing assignee from rlm to rhinton.



---

archive/issue_comments_075482.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-02T16:49:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8421#issuecomment-75482",
    "user": "rhinton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_075483.json:
```json
{
    "body": "Patch implements change.  It sits on my MQ stack on top of #8331 and #8329, but I don't think either of these are required.",
    "created_at": "2010-03-02T16:49:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8421#issuecomment-75483",
    "user": "rhinton"
}
```

Patch implements change.  It sits on my MQ stack on top of #8331 and #8329, but I don't think either of these are required.



---

archive/issue_comments_075484.json:
```json
{
    "body": "Attachment [trac_8421-bipartite-partition-sets.patch](tarball://root/attachments/some-uuid/ticket8421/trac_8421-bipartite-partition-sets.patch) by rhinton created at 2010-03-05 02:05:46\n\nupdated commit message",
    "created_at": "2010-03-05T02:05:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8421#issuecomment-75484",
    "user": "rhinton"
}
```

Attachment [trac_8421-bipartite-partition-sets.patch](tarball://root/attachments/some-uuid/ticket8421/trac_8421-bipartite-partition-sets.patch) by rhinton created at 2010-03-05 02:05:46

updated commit message



---

archive/issue_comments_075485.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-06T22:18:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8421#issuecomment-75485",
    "user": "rlm"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_075486.json:
```json
{
    "body": "Merged \"trac_8421-bipartite-partition-sets.patch\" into 4.4.alpha0",
    "created_at": "2010-04-15T23:46:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8421#issuecomment-75486",
    "user": "jhpalmieri"
}
```

Merged "trac_8421-bipartite-partition-sets.patch" into 4.4.alpha0



---

archive/issue_comments_075487.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-15T23:46:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8421#issuecomment-75487",
    "user": "jhpalmieri"
}
```

Resolution: fixed
