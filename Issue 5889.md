# Issue 5889: [with patch, needs review] random simplicial complexes

archive/issues_005889.json:
```json
{
    "body": "Assignee: jhpalmieri\n\nAdd random simplicial complexes to the class of examples of simplicial complexes, so you can do\n\n```\nsage: simplicial_complexes.RandomComplex(6, 2)\n```\n\nto get a random simplicial complex with 6 vertices, all possible edges, and the possible 2-dimensional simplices (triangles) randomly included (or not).\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5889\n\n",
    "created_at": "2009-04-24T17:14:45Z",
    "labels": [
        "misc",
        "minor",
        "enhancement"
    ],
    "title": "[with patch, needs review] random simplicial complexes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5889",
    "user": "jhpalmieri"
}
```
Assignee: jhpalmieri

Add random simplicial complexes to the class of examples of simplicial complexes, so you can do

```
sage: simplicial_complexes.RandomComplex(6, 2)
```

to get a random simplicial complex with 6 vertices, all possible edges, and the possible 2-dimensional simplices (triangles) randomly included (or not).


Issue created by migration from https://trac.sagemath.org/ticket/5889





---

archive/issue_comments_046561.json:
```json
{
    "body": "This looks good.\n\nThere is one little issue: as far as I know, you do not need to label the doctest with #random.  Sage doctests work in such a way that the same random seed is set before testing, so you will get the same results.  So the #random should be removed from line 712.\n\nApart from that, positive review.\n\n\nMichael, should we have a new trac component labeled \"algebraic topology\"?  It's a bit weird to have this under \"misc\", and it will probably come in handy at the next Sage Days in Seattle.",
    "created_at": "2009-04-30T12:24:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5889#issuecomment-46561",
    "user": "AlexGhitza"
}
```

This looks good.

There is one little issue: as far as I know, you do not need to label the doctest with #random.  Sage doctests work in such a way that the same random seed is set before testing, so you will get the same results.  So the #random should be removed from line 712.

Apart from that, positive review.


Michael, should we have a new trac component labeled "algebraic topology"?  It's a bit weird to have this under "misc", and it will probably come in handy at the next Sage Days in Seattle.



---

archive/issue_comments_046562.json:
```json
{
    "body": "Okay, this patch is identical to the first one, but without \"#random\".  It passes all tests for me on sage.math, although I would like someone else to double-check that.",
    "created_at": "2009-04-30T20:51:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5889#issuecomment-46562",
    "user": "jhpalmieri"
}
```

Okay, this patch is identical to the first one, but without "#random".  It passes all tests for me on sage.math, although I would like someone else to double-check that.



---

archive/issue_comments_046563.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-04-30T20:52:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5889#issuecomment-46563",
    "user": "jhpalmieri"
}
```

Attachment



---

archive/issue_comments_046564.json:
```json
{
    "body": "It also passes doctests for me.",
    "created_at": "2009-04-30T21:12:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5889#issuecomment-46564",
    "user": "AlexGhitza"
}
```

It also passes doctests for me.



---

archive/issue_comments_046565.json:
```json
{
    "body": "Alex,\n\n\"Algebraic Topology\" - here we come. I have made John default owner for now :)\n\nIf you want any other component please let me know and I will add them.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-30T21:40:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5889#issuecomment-46565",
    "user": "mabshoff"
}
```

Alex,

"Algebraic Topology" - here we come. I have made John default owner for now :)

If you want any other component please let me know and I will add them.

Cheers,

Michael



---

archive/issue_comments_046566.json:
```json
{
    "body": "Changing component from misc to algebraic topology.",
    "created_at": "2009-04-30T21:40:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5889#issuecomment-46566",
    "user": "mabshoff"
}
```

Changing component from misc to algebraic topology.



---

archive/issue_comments_046567.json:
```json
{
    "body": "Excellent!",
    "created_at": "2009-04-30T21:54:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5889#issuecomment-46567",
    "user": "jhpalmieri"
}
```

Excellent!



---

archive/issue_comments_046568.json:
```json
{
    "body": "Merged in Sage 4.0.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-11T13:19:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5889#issuecomment-46568",
    "user": "mabshoff"
}
```

Merged in Sage 4.0.alpha0.

Cheers,

Michael



---

archive/issue_comments_046569.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-11T13:19:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5889#issuecomment-46569",
    "user": "mabshoff"
}
```

Resolution: fixed
