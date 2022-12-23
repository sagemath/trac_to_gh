# Issue 5716: lifting a subdivided matrix should preserve the subdivision, but doesn't.

archive/issues_005716.json:
```json
{
    "body": "Assignee: was\n\nCC:  jason\n\n\n```\nsage: a = random_matrix(GF(3),4)\nsage: a.subdivide(2,2)\nsage: a\n[2 0|0 2]\n[2 1|1 0]\n[---+---]\n[1 2|1 0]\n[1 0|0 1]\nsage: a.lift()\n[2 0 0 2]\n[2 1 1 0]\n[1 2 1 0]\n[1 0 0 1]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5716\n\n",
    "created_at": "2009-04-08T19:18:52Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "title": "lifting a subdivided matrix should preserve the subdivision, but doesn't.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5716",
    "user": "was"
}
```
Assignee: was

CC:  jason


```
sage: a = random_matrix(GF(3),4)
sage: a.subdivide(2,2)
sage: a
[2 0|0 2]
[2 1|1 0]
[---+---]
[1 2|1 0]
[1 0|0 1]
sage: a.lift()
[2 0 0 2]
[2 1 1 0]
[1 2 1 0]
[1 0 0 1]
```


Issue created by migration from https://trac.sagemath.org/ticket/5716





---

archive/issue_comments_044671.json:
```json
{
    "body": "Is this a high priority issue? I am not convinced and since there is no patch and no sign of anyone working on fixing this I am bumping this to 3.4.2. There are also various dupes, one of which go reopened, i.e. #5715, so let's figure this out. \n\nCheers,\n\nMichael",
    "created_at": "2009-04-09T18:45:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5716#issuecomment-44671",
    "user": "mabshoff"
}
```

Is this a high priority issue? I am not convinced and since there is no patch and no sign of anyone working on fixing this I am bumping this to 3.4.2. There are also various dupes, one of which go reopened, i.e. #5715, so let's figure this out. 

Cheers,

Michael



---

archive/issue_comments_044672.json:
```json
{
    "body": "(I don't think this is actually a duplicate.)",
    "created_at": "2009-05-06T22:30:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5716#issuecomment-44672",
    "user": "jhpalmieri"
}
```

(I don't think this is actually a duplicate.)



---

archive/issue_comments_044673.json:
```json
{
    "body": "Here's a patch.  This should change things so that subdivisions are preserved when calling `mat.change_ring()`, `mat.lift()`, `mat.dense_matrix()`, and `mat.sparse_matrix()`.",
    "created_at": "2009-05-07T04:35:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5716#issuecomment-44673",
    "user": "jhpalmieri"
}
```

Here's a patch.  This should change things so that subdivisions are preserved when calling `mat.change_ring()`, `mat.lift()`, `mat.dense_matrix()`, and `mat.sparse_matrix()`.



---

archive/issue_comments_044674.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-07T04:35:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5716#issuecomment-44674",
    "user": "jhpalmieri"
}
```

Changing status from new to assigned.



---

archive/issue_comments_044675.json:
```json
{
    "body": "Changing assignee from was to jhpalmieri.",
    "created_at": "2009-05-07T04:35:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5716#issuecomment-44675",
    "user": "jhpalmieri"
}
```

Changing assignee from was to jhpalmieri.



---

archive/issue_comments_044676.json:
```json
{
    "body": "This applies fine to 4.0.rc1 and all doctests in sage/matrix pass (except the known numerical-noise failure which is nothing to do with this patch). But I'm not completely happy with it, because not all of the functions where the behaviour has changed have doctests to prove it, so I'm changing this to \"needs work\". \n\nDavid",
    "created_at": "2009-05-29T11:03:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5716#issuecomment-44676",
    "user": "davidloeffler"
}
```

This applies fine to 4.0.rc1 and all doctests in sage/matrix pass (except the known numerical-noise failure which is nothing to do with this patch). But I'm not completely happy with it, because not all of the functions where the behaviour has changed have doctests to prove it, so I'm changing this to "needs work". 

David



---

archive/issue_comments_044677.json:
```json
{
    "body": "Okay, here's a new patch.  I think that this tests everything, although there is at least one function (sparse_matrix, maybe) which is tested in a doctest for another (by looking at `a.dense_matrix().sparse_matrix()` or something like that).",
    "created_at": "2009-05-29T18:48:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5716#issuecomment-44677",
    "user": "jhpalmieri"
}
```

Okay, here's a new patch.  I think that this tests everything, although there is at least one function (sparse_matrix, maybe) which is tested in a doctest for another (by looking at `a.dense_matrix().sparse_matrix()` or something like that).



---

archive/issue_comments_044678.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-05-30T05:02:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5716#issuecomment-44678",
    "user": "jason"
}
```

Attachment



---

archive/issue_comments_044679.json:
```json
{
    "body": "It passes doctests (and everything is tested).  Looks good to me.  Positive review.",
    "created_at": "2009-05-30T05:52:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5716#issuecomment-44679",
    "user": "jason"
}
```

It passes doctests (and everything is tested).  Looks good to me.  Positive review.



---

archive/issue_comments_044680.json:
```json
{
    "body": "Merged in 4.0.alpha0.",
    "created_at": "2009-05-31T23:47:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5716#issuecomment-44680",
    "user": "mhansen"
}
```

Merged in 4.0.alpha0.



---

archive/issue_comments_044681.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-31T23:47:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5716#issuecomment-44681",
    "user": "mhansen"
}
```

Resolution: fixed
