# Issue 5716: lifting a subdivided matrix should preserve the subdivision, but doesn't.

archive/issues_005716.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @jasongrout\n\n\n```\nsage: a = random_matrix(GF(3),4)\nsage: a.subdivide(2,2)\nsage: a\n[2 0|0 2]\n[2 1|1 0]\n[---+---]\n[1 2|1 0]\n[1 0|0 1]\nsage: a.lift()\n[2 0 0 2]\n[2 1 1 0]\n[1 2 1 0]\n[1 0 0 1]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5716\n\n",
    "created_at": "2009-04-08T19:18:52Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.1",
    "title": "lifting a subdivided matrix should preserve the subdivision, but doesn't.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5716",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

CC:  @jasongrout


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

archive/issue_comments_044586.json:
```json
{
    "body": "Is this a high priority issue? I am not convinced and since there is no patch and no sign of anyone working on fixing this I am bumping this to 3.4.2. There are also various dupes, one of which go reopened, i.e. #5715, so let's figure this out. \n\nCheers,\n\nMichael",
    "created_at": "2009-04-09T18:45:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5716#issuecomment-44586",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Is this a high priority issue? I am not convinced and since there is no patch and no sign of anyone working on fixing this I am bumping this to 3.4.2. There are also various dupes, one of which go reopened, i.e. #5715, so let's figure this out. 

Cheers,

Michael



---

archive/issue_comments_044587.json:
```json
{
    "body": "(I don't think this is actually a duplicate.)",
    "created_at": "2009-05-06T22:30:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5716#issuecomment-44587",
    "user": "https://github.com/jhpalmieri"
}
```

(I don't think this is actually a duplicate.)



---

archive/issue_comments_044588.json:
```json
{
    "body": "Here's a patch.  This should change things so that subdivisions are preserved when calling `mat.change_ring()`, `mat.lift()`, `mat.dense_matrix()`, and `mat.sparse_matrix()`.",
    "created_at": "2009-05-07T04:35:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5716#issuecomment-44588",
    "user": "https://github.com/jhpalmieri"
}
```

Here's a patch.  This should change things so that subdivisions are preserved when calling `mat.change_ring()`, `mat.lift()`, `mat.dense_matrix()`, and `mat.sparse_matrix()`.



---

archive/issue_comments_044589.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-07T04:35:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5716#issuecomment-44589",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from new to assigned.



---

archive/issue_comments_044590.json:
```json
{
    "body": "Changing assignee from @williamstein to @jhpalmieri.",
    "created_at": "2009-05-07T04:35:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5716#issuecomment-44590",
    "user": "https://github.com/jhpalmieri"
}
```

Changing assignee from @williamstein to @jhpalmieri.



---

archive/issue_comments_044591.json:
```json
{
    "body": "This applies fine to 4.0.rc1 and all doctests in sage/matrix pass (except the known numerical-noise failure which is nothing to do with this patch). But I'm not completely happy with it, because not all of the functions where the behaviour has changed have doctests to prove it, so I'm changing this to \"needs work\". \n\nDavid",
    "created_at": "2009-05-29T11:03:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5716#issuecomment-44591",
    "user": "https://github.com/loefflerd"
}
```

This applies fine to 4.0.rc1 and all doctests in sage/matrix pass (except the known numerical-noise failure which is nothing to do with this patch). But I'm not completely happy with it, because not all of the functions where the behaviour has changed have doctests to prove it, so I'm changing this to "needs work". 

David



---

archive/issue_comments_044592.json:
```json
{
    "body": "Okay, here's a new patch.  I think that this tests everything, although there is at least one function (sparse_matrix, maybe) which is tested in a doctest for another (by looking at `a.dense_matrix().sparse_matrix()` or something like that).",
    "created_at": "2009-05-29T18:48:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5716#issuecomment-44592",
    "user": "https://github.com/jhpalmieri"
}
```

Okay, here's a new patch.  I think that this tests everything, although there is at least one function (sparse_matrix, maybe) which is tested in a doctest for another (by looking at `a.dense_matrix().sparse_matrix()` or something like that).



---

archive/issue_comments_044593.json:
```json
{
    "body": "Attachment [trac_5716.patch](tarball://root/attachments/some-uuid/ticket5716/trac_5716.patch) by @jasongrout created at 2009-05-30 05:02:11",
    "created_at": "2009-05-30T05:02:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5716#issuecomment-44593",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac_5716.patch](tarball://root/attachments/some-uuid/ticket5716/trac_5716.patch) by @jasongrout created at 2009-05-30 05:02:11



---

archive/issue_comments_044594.json:
```json
{
    "body": "It passes doctests (and everything is tested).  Looks good to me.  Positive review.",
    "created_at": "2009-05-30T05:52:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5716#issuecomment-44594",
    "user": "https://github.com/jasongrout"
}
```

It passes doctests (and everything is tested).  Looks good to me.  Positive review.



---

archive/issue_comments_044595.json:
```json
{
    "body": "Merged in 4.0.alpha0.",
    "created_at": "2009-05-31T23:47:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5716#issuecomment-44595",
    "user": "https://github.com/mwhansen"
}
```

Merged in 4.0.alpha0.



---

archive/issue_comments_044596.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-31T23:47:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5716#issuecomment-44596",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
