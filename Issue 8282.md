# Issue 8282: implement victor_miller_basis over an arbitrary base ring

archive/issues_008282.json:
```json
{
    "body": "Assignee: craigcitro\n\nThis can now be done as:\n\n\n```\nsage: time bas = victor_miller_basis(2000, prec=200)\nCPU times: user 8.44 s, sys: 0.08 s, total: 8.52 s\nWall time: 8.55 s\nsage: time bas_mod7 = [ f.change_ring(GF(7)) for f in bas ]\nCPU times: user 2.52 s, sys: 0.00 s, total: 2.52 s\nWall time: 2.61 s\n```\n\n\nIt would be nice (and presumably much faster and less memory-consuming) to compute the Victor Miller basis *directly over GF(7)*.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8282\n\n",
    "created_at": "2010-02-16T13:11:56Z",
    "labels": [
        "modular forms",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "implement victor_miller_basis over an arbitrary base ring",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8282",
    "user": "AlexGhitza"
}
```
Assignee: craigcitro

This can now be done as:


```
sage: time bas = victor_miller_basis(2000, prec=200)
CPU times: user 8.44 s, sys: 0.08 s, total: 8.52 s
Wall time: 8.55 s
sage: time bas_mod7 = [ f.change_ring(GF(7)) for f in bas ]
CPU times: user 2.52 s, sys: 0.00 s, total: 2.52 s
Wall time: 2.61 s
```


It would be nice (and presumably much faster and less memory-consuming) to compute the Victor Miller basis *directly over GF(7)*.


Issue created by migration from https://trac.sagemath.org/ticket/8282


