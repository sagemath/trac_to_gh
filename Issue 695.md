# Issue 695: SAGE's multivariate gcd sucks over QQ and/or ZZ

archive/issues_000695.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\n\nI think those timings are way out of date, since Singular 3 seems\nto be *very* fast at mod p multivariate GCD computation, even\nthough it sucks over QQ.   Check out this paper:\n\n          http://www.cecm.sfu.ca/CAG/papers/brown.ps\n\nIt on exactly the problem of GCD over QQ (or equiv ZZ),\nand section 2 has a complete description of a gcd algorithm \nthat reduces gcd over ZZ to doing gcd's mod p.\n\nWho wants to be a hero -- like Jon Bober and number of partitions -- \nand implement this for Sage, so that multivariate GCD's aren't \nembarrassingly slow in Sage anymore?   This slowness *has* \nbeen something reported to me on several occasions during \nthe last 2 years. \n\nWilliam\n```\n\n\nNOTE -- I would implement this modular GCD algorithm in Sage, not Singular.\n\nIssue created by migration from https://trac.sagemath.org/ticket/695\n\n",
    "created_at": "2007-09-19T20:24:55Z",
    "labels": [
        "basic arithmetic",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "SAGE's multivariate gcd sucks over QQ and/or ZZ",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/695",
    "user": "was"
}
```
Assignee: somebody


```

I think those timings are way out of date, since Singular 3 seems
to be *very* fast at mod p multivariate GCD computation, even
though it sucks over QQ.   Check out this paper:

          http://www.cecm.sfu.ca/CAG/papers/brown.ps

It on exactly the problem of GCD over QQ (or equiv ZZ),
and section 2 has a complete description of a gcd algorithm 
that reduces gcd over ZZ to doing gcd's mod p.

Who wants to be a hero -- like Jon Bober and number of partitions -- 
and implement this for Sage, so that multivariate GCD's aren't 
embarrassingly slow in Sage anymore?   This slowness *has* 
been something reported to me on several occasions during 
the last 2 years. 

William
```


NOTE -- I would implement this modular GCD algorithm in Sage, not Singular.

Issue created by migration from https://trac.sagemath.org/ticket/695





---

archive/issue_comments_003641.json:
```json
{
    "body": "See #694 instead!",
    "created_at": "2007-09-19T20:35:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/695#issuecomment-3641",
    "user": "was"
}
```

See #694 instead!



---

archive/issue_comments_003642.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2007-09-19T20:35:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/695#issuecomment-3642",
    "user": "was"
}
```

Resolution: duplicate
