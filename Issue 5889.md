# Issue 5889: [with patch, needs review] random simplicial complexes

archive/issues_005889.json:
```json
{
    "body": "Assignee: @jhpalmieri\n\nAdd random simplicial complexes to the class of examples of simplicial complexes, so you can do\n\n```\nsage: simplicial_complexes.RandomComplex(6, 2)\n```\n\nto get a random simplicial complex with 6 vertices, all possible edges, and the possible 2-dimensional simplices (triangles) randomly included (or not).\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5889\n\n",
    "created_at": "2009-04-24T17:14:45Z",
    "labels": [
        "component: misc",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "[with patch, needs review] random simplicial complexes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5889",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: @jhpalmieri

Add random simplicial complexes to the class of examples of simplicial complexes, so you can do

```
sage: simplicial_complexes.RandomComplex(6, 2)
```

to get a random simplicial complex with 6 vertices, all possible edges, and the possible 2-dimensional simplices (triangles) randomly included (or not).


Issue created by migration from https://trac.sagemath.org/ticket/5889





---

archive/issue_comments_046472.json:
```json
{
    "body": "This looks good.\n\nThere is one little issue: as far as I know, you do not need to label the doctest with #random.  Sage doctests work in such a way that the same random seed is set before testing, so you will get the same results.  So the #random should be removed from line 712.\n\nApart from that, positive review.\n\n\nMichael, should we have a new trac component labeled \"algebraic topology\"?  It's a bit weird to have this under \"misc\", and it will probably come in handy at the next Sage Days in Seattle.",
    "created_at": "2009-04-30T12:24:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5889#issuecomment-46472",
    "user": "https://github.com/aghitza"
}
```

This looks good.

There is one little issue: as far as I know, you do not need to label the doctest with #random.  Sage doctests work in such a way that the same random seed is set before testing, so you will get the same results.  So the #random should be removed from line 712.

Apart from that, positive review.


Michael, should we have a new trac component labeled "algebraic topology"?  It's a bit weird to have this under "misc", and it will probably come in handy at the next Sage Days in Seattle.



---

archive/issue_comments_046473.json:
```json
{
    "body": "Okay, this patch is identical to the first one, but without \"#random\".  It passes all tests for me on sage.math, although I would like someone else to double-check that.",
    "created_at": "2009-04-30T20:51:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5889#issuecomment-46473",
    "user": "https://github.com/jhpalmieri"
}
```

Okay, this patch is identical to the first one, but without "#random".  It passes all tests for me on sage.math, although I would like someone else to double-check that.



---

archive/issue_comments_046474.json:
```json
{
    "body": "Attachment [random-complex.patch](tarball://root/attachments/some-uuid/ticket5889/random-complex.patch) by @jhpalmieri created at 2009-04-30 20:52:18",
    "created_at": "2009-04-30T20:52:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5889#issuecomment-46474",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [random-complex.patch](tarball://root/attachments/some-uuid/ticket5889/random-complex.patch) by @jhpalmieri created at 2009-04-30 20:52:18



---

archive/issue_comments_046475.json:
```json
{
    "body": "It also passes doctests for me.",
    "created_at": "2009-04-30T21:12:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5889#issuecomment-46475",
    "user": "https://github.com/aghitza"
}
```

It also passes doctests for me.



---

archive/issue_comments_046476.json:
```json
{
    "body": "Alex,\n\n\"Algebraic Topology\" - here we come. I have made John default owner for now :)\n\nIf you want any other component please let me know and I will add them.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-30T21:40:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5889#issuecomment-46476",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Alex,

"Algebraic Topology" - here we come. I have made John default owner for now :)

If you want any other component please let me know and I will add them.

Cheers,

Michael



---

archive/issue_comments_046477.json:
```json
{
    "body": "Changing component from misc to algebraic topology.",
    "created_at": "2009-04-30T21:40:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5889#issuecomment-46477",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing component from misc to algebraic topology.



---

archive/issue_comments_046478.json:
```json
{
    "body": "Excellent!",
    "created_at": "2009-04-30T21:54:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5889#issuecomment-46478",
    "user": "https://github.com/jhpalmieri"
}
```

Excellent!



---

archive/issue_comments_046479.json:
```json
{
    "body": "Merged in Sage 4.0.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-11T13:19:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5889#issuecomment-46479",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 4.0.alpha0.

Cheers,

Michael



---

archive/issue_comments_046480.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-11T13:19:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5889#issuecomment-46480",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_006144.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-05-11T13:19:38Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5889",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5889#event-6144"
}
```
