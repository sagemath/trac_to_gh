# Issue 6959: modular forms -- add aplist and anlist for newforms

archive/issues_006959.json:
```json
{
    "body": "Assignee: craigcitro\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6959\n\n",
    "created_at": "2009-09-19T05:01:49Z",
    "labels": [
        "modular forms",
        "major",
        "enhancement"
    ],
    "title": "modular forms -- add aplist and anlist for newforms",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6959",
    "user": "was"
}
```
Assignee: craigcitro



Issue created by migration from https://trac.sagemath.org/ticket/6959





---

archive/issue_comments_057561.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-09-19T05:02:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6959#issuecomment-57561",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_057562.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-10-29T21:19:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6959#issuecomment-57562",
    "user": "cremona"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_057563.json:
```json
{
    "body": "Looks mainly good to me -- patch applies and tests (in sage/modular/modform) pass.  One glitch:\n\n```\n        if not all_embeddings: \n \t            return A \n \treturn A \n```\n\nlooks like a typo.\n\nIt does not seem very efficient to factor all the n in the range, and that is not the way I have always done this.  The result is pretty slow -- for example, if you wanted to compute all a_n for n<10^6, this is not good enough:\n\n```\nsage: f = CuspForms(11,2).newforms()[0]; f\nq - 2*q^2 - q^3 + 2*q^4 + q^5 + O(q^6)\nsage: time an = f.anlist(1000)\nCPU times: user 0.40 s, sys: 0.00 s, total: 0.40 s\nWall time: 0.40 s\nsage: time an = f.anlist(10000)\nCPU times: user 13.84 s, sys: 0.79 s, total: 14.63 s\nWall time: 14.65 s\nsage: time an = f.anlist(100000)\n#(gave up waiting after a few minutes)\n```\n\nOn second thoughts it is probably computing the a_p which is slow here.  But are they even cached?\n\n```\nsage: time an = f.aplist(10000)\nCPU times: user 11.09 s, sys: 0.65 s, total: 11.74 s\nWall time: 11.81 s\nsage: time an = f.anlist(10000)\nCPU times: user 13.71 s, sys: 0.69 s, total: 14.40 s\nWall time: 14.53 s\n```\n\n-- it seems not.",
    "created_at": "2009-10-29T21:19:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6959#issuecomment-57563",
    "user": "cremona"
}
```

Looks mainly good to me -- patch applies and tests (in sage/modular/modform) pass.  One glitch:

```
        if not all_embeddings: 
 	            return A 
 	return A 
```

looks like a typo.

It does not seem very efficient to factor all the n in the range, and that is not the way I have always done this.  The result is pretty slow -- for example, if you wanted to compute all a_n for n<10^6, this is not good enough:

```
sage: f = CuspForms(11,2).newforms()[0]; f
q - 2*q^2 - q^3 + 2*q^4 + q^5 + O(q^6)
sage: time an = f.anlist(1000)
CPU times: user 0.40 s, sys: 0.00 s, total: 0.40 s
Wall time: 0.40 s
sage: time an = f.anlist(10000)
CPU times: user 13.84 s, sys: 0.79 s, total: 14.63 s
Wall time: 14.65 s
sage: time an = f.anlist(100000)
#(gave up waiting after a few minutes)
```

On second thoughts it is probably computing the a_p which is slow here.  But are they even cached?

```
sage: time an = f.aplist(10000)
CPU times: user 11.09 s, sys: 0.65 s, total: 11.74 s
Wall time: 11.81 s
sage: time an = f.anlist(10000)
CPU times: user 13.71 s, sys: 0.69 s, total: 14.40 s
Wall time: 14.53 s
```

-- it seems not.



---

archive/issue_comments_057564.json:
```json
{
    "body": "Changing keywords from \"\" to \"newform\".",
    "created_at": "2013-09-01T12:13:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6959#issuecomment-57564",
    "user": "chapoton"
}
```

Changing keywords from "" to "newform".



---

archive/issue_comments_057565.json:
```json
{
    "body": "there are three failing doctest (sage 5.12.beta4)",
    "created_at": "2013-09-01T12:13:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6959#issuecomment-57565",
    "user": "chapoton"
}
```

there are three failing doctest (sage 5.12.beta4)



---

archive/issue_comments_057566.json:
```json
{
    "body": "New commits:",
    "created_at": "2014-06-19T20:23:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6959#issuecomment-57566",
    "user": "chapoton"
}
```

New commits:



---

archive/issue_comments_057567.json:
```json
{
    "body": "The 3 failing doctests looks to me like a problem with galois ambiguity (i.e. an algebraic number a1 is replaced by its conjugate -a1). Maybe one can just replace them by the results ?",
    "created_at": "2014-06-19T20:25:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6959#issuecomment-57567",
    "user": "chapoton"
}
```

The 3 failing doctests looks to me like a problem with galois ambiguity (i.e. an algebraic number a1 is replaced by its conjugate -a1). Maybe one can just replace them by the results ?



---

archive/issue_comments_057568.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-03-01T11:14:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6959#issuecomment-57568",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_057569.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-06-08T19:42:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6959#issuecomment-57569",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_057570.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2018-03-11T19:57:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6959#issuecomment-57570",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:
