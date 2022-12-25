# Issue 8331: BipartiteGraph constructor does not create partitions for dict inputs

archive/issues_008331.json:
```json
{
    "body": "Assignee: @rhinton\n\nCC:  @jasongrout @rlmill\n\nKeywords: BipartiteGraph\n\nThe BipartiteGraph constructor does not create partitions for dict inputs.\n\n```\nsage: t1 = BipartiteGraph({'a': ['b'], 'b':['c']})\nsage: t1.left\n...\nAttributeError: 'BipartiteGraph' object has no attribute 'left'\n```\n\nThe problem comes in the constructor in the \"other inputs\" case.  A Graph object is created, but not all the control paths find a bipartition.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8331\n\n",
    "closed_at": "2010-03-03T14:25:55Z",
    "created_at": "2010-02-23T01:04:44Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "BipartiteGraph constructor does not create partitions for dict inputs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8331",
    "user": "https://github.com/rhinton"
}
```
Assignee: @rhinton

CC:  @jasongrout @rlmill

Keywords: BipartiteGraph

The BipartiteGraph constructor does not create partitions for dict inputs.

```
sage: t1 = BipartiteGraph({'a': ['b'], 'b':['c']})
sage: t1.left
...
AttributeError: 'BipartiteGraph' object has no attribute 'left'
```

The problem comes in the constructor in the "other inputs" case.  A Graph object is created, but not all the control paths find a bipartition.


Issue created by migration from https://trac.sagemath.org/ticket/8331





---

archive/issue_comments_074063.json:
```json
{
    "body": "another duplicate of part of #1941.",
    "created_at": "2010-02-23T01:26:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8331#issuecomment-74063",
    "user": "https://github.com/rlmill"
}
```

another duplicate of part of #1941.



---

archive/issue_comments_074064.json:
```json
{
    "body": "Attachment [trac_8331-bipartite-dict-initializer.patch](tarball://root/attachments/some-uuid/ticket8331/trac_8331-bipartite-dict-initializer.patch) by @rhinton created at 2010-02-23 01:29:33\n\nThe patch trac_8331-... fixes the bug, adds a doctest, and slightly improves the ReST markup for the constructor.  (I am certainly not an expert.)",
    "created_at": "2010-02-23T01:29:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8331#issuecomment-74064",
    "user": "https://github.com/rhinton"
}
```

Attachment [trac_8331-bipartite-dict-initializer.patch](tarball://root/attachments/some-uuid/ticket8331/trac_8331-bipartite-dict-initializer.patch) by @rhinton created at 2010-02-23 01:29:33

The patch trac_8331-... fixes the bug, adds a doctest, and slightly improves the ReST markup for the constructor.  (I am certainly not an expert.)



---

archive/issue_comments_074065.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-23T01:29:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8331#issuecomment-74065",
    "user": "https://github.com/rhinton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_074066.json:
```json
{
    "body": "Changing assignee from @rlmill to @rhinton.",
    "created_at": "2010-02-23T01:32:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8331#issuecomment-74066",
    "user": "https://github.com/rhinton"
}
```

Changing assignee from @rlmill to @rhinton.



---

archive/issue_comments_074067.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-02T03:09:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8331#issuecomment-74067",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_074068.json:
```json
{
    "body": "Works for me :-)",
    "created_at": "2010-03-02T03:09:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8331#issuecomment-74068",
    "user": "https://github.com/rlmill"
}
```

Works for me :-)



---

archive/issue_comments_074069.json:
```json
{
    "body": "Ryan: remember to put a sensible commit message in your patch, together with the ticket number.",
    "created_at": "2010-03-03T14:25:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8331#issuecomment-74069",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Ryan: remember to put a sensible commit message in your patch, together with the ticket number.



---

archive/issue_events_019947.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-03-03T14:25:55Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8331",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8331#event-19947"
}
```



---

archive/issue_comments_074070.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-03T14:25:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8331#issuecomment-74070",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
