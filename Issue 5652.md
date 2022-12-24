# Issue 5652: powermod is slower than Integer.power_mod

archive/issues_005652.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  mvngu @williamstein\n\nConsider the following example:\n\n\n```\nsage: time a = power_mod(5, 10^2000, 10^3000)\nCPU times: user 3.67 s, sys: 0.00 s, total: 3.67 s\nWall time: 3.67 s\nsage: time b = 5.powermod(10^2000, 10^3000)  \nCPU times: user 2.82 s, sys: 0.00 s, total: 2.83 s\nWall time: 2.84 s\nsage: a == b\nTrue\nsage: time a = power_mod(5, 10^4000, 10^7000)\nCPU times: user 27.17 s, sys: 0.01 s, total: 27.18 s\nWall time: 27.30 s\nsage: time b = 5.powermod(10^4000, 10^7000)  \nCPU times: user 21.38 s, sys: 0.04 s, total: 21.42 s\nWall time: 21.44 s\nsage: a == b\nTrue\n```\n\n\n(The problem is that power_mod() uses generic code, while Integer.powermod() uses gmp, which is faster.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/5652\n\n",
    "created_at": "2009-03-31T20:51:20Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "powermod is slower than Integer.power_mod",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5652",
    "user": "bober"
}
```
Assignee: somebody

CC:  mvngu @williamstein

Consider the following example:


```
sage: time a = power_mod(5, 10^2000, 10^3000)
CPU times: user 3.67 s, sys: 0.00 s, total: 3.67 s
Wall time: 3.67 s
sage: time b = 5.powermod(10^2000, 10^3000)  
CPU times: user 2.82 s, sys: 0.00 s, total: 2.83 s
Wall time: 2.84 s
sage: a == b
True
sage: time a = power_mod(5, 10^4000, 10^7000)
CPU times: user 27.17 s, sys: 0.01 s, total: 27.18 s
Wall time: 27.30 s
sage: time b = 5.powermod(10^4000, 10^7000)  
CPU times: user 21.38 s, sys: 0.04 s, total: 21.42 s
Wall time: 21.44 s
sage: a == b
True
```


(The problem is that power_mod() uses generic code, while Integer.powermod() uses gmp, which is faster.)

Issue created by migration from https://trac.sagemath.org/ticket/5652





---

archive/issue_comments_044140.json:
```json
{
    "body": "This is a duplicate of #5082.\n\nI suggest it is closed as a duplicate. Since trac doesn't let me, Minh or William, as release managers, can you close this?",
    "created_at": "2009-07-15T19:50:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5652#issuecomment-44140",
    "user": "@burcin"
}
```

This is a duplicate of #5082.

I suggest it is closed as a duplicate. Since trac doesn't let me, Minh or William, as release managers, can you close this?



---

archive/issue_comments_044141.json:
```json
{
    "body": "Replying to [comment:1 burcin]:\n> This is a duplicate of #5082.\n> \n> I suggest it is closed as a duplicate. Since trac doesn't let me, Minh or William, as release managers, can you close this?\nI don't have admin privileges on trac, so I can't close tickets at the moment. I've merged about 5 tickets so far, but their status has not been set accordingly.",
    "created_at": "2009-07-15T19:53:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5652#issuecomment-44141",
    "user": "mvngu"
}
```

Replying to [comment:1 burcin]:
> This is a duplicate of #5082.
> 
> I suggest it is closed as a duplicate. Since trac doesn't let me, Minh or William, as release managers, can you close this?
I don't have admin privileges on trac, so I can't close tickets at the moment. I've merged about 5 tickets so far, but their status has not been set accordingly.



---

archive/issue_comments_044142.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-07-21T03:20:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5652#issuecomment-44142",
    "user": "mvngu"
}
```

Resolution: duplicate
