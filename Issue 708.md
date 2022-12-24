# Issue 708: performance issue -- Magma is way faster at testing some polynomials for irreducibility

archive/issues_000708.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  burcin\n\n\n```\nsage: R = QQ['x']\nsage: f = R.random_element(1000)\nsage: time f.is_irreducible()\nCPU times: user 31.45 s, sys: 0.10 s, total: 31.54 s\nWall time: 31.79\nTrue\nsage: g = magma(f)\nsage: time g.IsIrreducible()\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 2.57\ntrue\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/708\n\n",
    "created_at": "2007-09-20T17:40:44Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "performance issue -- Magma is way faster at testing some polynomials for irreducibility",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/708",
    "user": "was"
}
```
Assignee: somebody

CC:  burcin


```
sage: R = QQ['x']
sage: f = R.random_element(1000)
sage: time f.is_irreducible()
CPU times: user 31.45 s, sys: 0.10 s, total: 31.54 s
Wall time: 31.79
True
sage: g = magma(f)
sage: time g.IsIrreducible()
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 2.57
true
```


Issue created by migration from https://trac.sagemath.org/ticket/708





---

archive/issue_comments_003718.json:
```json
{
    "body": "This is still the case:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 3.1.2.alpha0, Release Date: 2008-08-22                |\n| Type notebook() for the GUI, and license() for information.        |\nsage: R = QQ['x']\nsage: f = R.random_element(1000)\nsage: time f.is_irreducible()\nCPU times: user 57.86 s, sys: 0.13 s, total: 57.99 s\nWall time: 58.02 s\nTrue\nsage: g = magma(f)\nsage: time g.IsIrreducible()\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 4.22 s\ntrue\nsage: \nExiting SAGE (CPU time 0m58.11s, Wall time 3m26.33s).\nExiting spawned Magma process.\n```\n\nIs anyone working in that area?\n\nCheers,\n\nMichael",
    "created_at": "2008-08-27T01:29:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/708",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/708#issuecomment-3718",
    "user": "mabshoff"
}
```

This is still the case:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.1.2.alpha0, Release Date: 2008-08-22                |
| Type notebook() for the GUI, and license() for information.        |
sage: R = QQ['x']
sage: f = R.random_element(1000)
sage: time f.is_irreducible()
CPU times: user 57.86 s, sys: 0.13 s, total: 57.99 s
Wall time: 58.02 s
True
sage: g = magma(f)
sage: time g.IsIrreducible()
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 4.22 s
true
sage: 
Exiting SAGE (CPU time 0m58.11s, Wall time 3m26.33s).
Exiting spawned Magma process.
```

Is anyone working in that area?

Cheers,

Michael



---

archive/issue_comments_003719.json:
```json
{
    "body": "Attachment [708-speedup_poly_irred.patch](tarball://root/attachments/some-uuid/ticket708/708-speedup_poly_irred.patch) by AlexGhitza created at 2008-08-29 22:38:15\n\nThere is a simple way of getting within range of Magma's speed: by Gauss' lemma, we can clear the denominators to get a polynomial over the integers, then test it for irreducibility using the significantly faster code over ZZ.\n\nSee the attached patch.  I'm getting a speedup factor of about 10, but I can't compare to Magma since I don't have it.",
    "created_at": "2008-08-29T22:38:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/708",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/708#issuecomment-3719",
    "user": "AlexGhitza"
}
```

Attachment [708-speedup_poly_irred.patch](tarball://root/attachments/some-uuid/ticket708/708-speedup_poly_irred.patch) by AlexGhitza created at 2008-08-29 22:38:15

There is a simple way of getting within range of Magma's speed: by Gauss' lemma, we can clear the denominators to get a polynomial over the integers, then test it for irreducibility using the significantly faster code over ZZ.

See the attached patch.  I'm getting a speedup factor of about 10, but I can't compare to Magma since I don't have it.



---

archive/issue_comments_003720.json:
```json
{
    "body": "Speed report:\n\n\n```\nsage: R = QQ['x']\nsage: f = R.random_element(1000)\nsage: time f.is_irreducible()\nCPU times: user 2.06 s, sys: 0.00 s, total: 2.06 s\nWall time: 2.06 s\nTrue\nsage: g = magma(f)\nsage: t = magma.cputime()\nsage: sage: time g.IsIrreducible()\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 5.24 s\ntrue\nsage: magma.cputime(t)\n5.2400000000000002\n```\n\n\nThe new code seems to compare favorably to Magma. IIRC Bill Hart suggested to do pretty much everything with Flint w.r.t. to QQ[x]. Maybe that could be another ticket/task.",
    "created_at": "2008-08-30T00:31:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/708",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/708#issuecomment-3720",
    "user": "malb"
}
```

Speed report:


```
sage: R = QQ['x']
sage: f = R.random_element(1000)
sage: time f.is_irreducible()
CPU times: user 2.06 s, sys: 0.00 s, total: 2.06 s
Wall time: 2.06 s
True
sage: g = magma(f)
sage: t = magma.cputime()
sage: sage: time g.IsIrreducible()
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 5.24 s
true
sage: magma.cputime(t)
5.2400000000000002
```


The new code seems to compare favorably to Magma. IIRC Bill Hart suggested to do pretty much everything with Flint w.r.t. to QQ[x]. Maybe that could be another ticket/task.



---

archive/issue_comments_003721.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha3",
    "created_at": "2008-08-30T01:48:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/708",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/708#issuecomment-3721",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.alpha3



---

archive/issue_comments_003722.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-30T01:48:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/708",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/708#issuecomment-3722",
    "user": "mabshoff"
}
```

Resolution: fixed
