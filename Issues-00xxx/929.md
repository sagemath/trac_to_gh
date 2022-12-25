# Issue 929: [with patch] wrap fpLLL-2.0

archive/issues_000929.json:
```json
{
    "body": "Assignee: @malb\n\nDamien Stehle published a new and much improved version of his fpLLL package at http://perso.ens-lyon.fr/damien.stehle/english.html . This should be wrapped for SAGE instead of fpLLL-1.3. This makes the fpLLL patch attached to #723 obsolete and should also provide SAGE with a performance comparable to MAGMA for LLL computations.\n\nIssue created by migration from https://trac.sagemath.org/ticket/929\n\n",
    "closed_at": "2007-10-23T19:39:38Z",
    "created_at": "2007-10-19T17:29:00Z",
    "labels": [
        "component: linear algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.9",
    "title": "[with patch] wrap fpLLL-2.0",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/929",
    "user": "https://github.com/malb"
}
```
Assignee: @malb

Damien Stehle published a new and much improved version of his fpLLL package at http://perso.ens-lyon.fr/damien.stehle/english.html . This should be wrapped for SAGE instead of fpLLL-1.3. This makes the fpLLL patch attached to #723 obsolete and should also provide SAGE with a performance comparable to MAGMA for LLL computations.

Issue created by migration from https://trac.sagemath.org/ticket/929





---

archive/issue_comments_005663.json:
```json
{
    "body": "Attachment [fpLLL-sage.patch](tarball://root/attachments/some-uuid/ticket929/fpLLL-sage.patch) by @malb created at 2007-10-21 16:20:20\n\nThe attached patch requires http://sage.math.washington.edu/home/malb/pkgs/libfplll-2.0-20071020.spkg to be installed. After that package has be installed and the patch was applied, fpLLL is the default implementation for Matrix_integer_dense.LLL. I'd appreciate if somebody more into LLL would check my documentation.",
    "created_at": "2007-10-21T16:20:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/929",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/929#issuecomment-5663",
    "user": "https://github.com/malb"
}
```

Attachment [fpLLL-sage.patch](tarball://root/attachments/some-uuid/ticket929/fpLLL-sage.patch) by @malb created at 2007-10-21 16:20:20

The attached patch requires http://sage.math.washington.edu/home/malb/pkgs/libfplll-2.0-20071020.spkg to be installed. After that package has be installed and the patch was applied, fpLLL is the default implementation for Matrix_integer_dense.LLL. I'd appreciate if somebody more into LLL would check my documentation.



---

archive/issue_events_002554.json:
```json
{
    "actor": "https://github.com/malb",
    "created_at": "2007-10-21T16:20:20Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/929",
    "milestone": "sage-2.8.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/929#event-2554"
}
```



---

archive/issue_comments_005664.json:
```json
{
    "body": "The mandatory benchmarks of Stehle vs. Stehle :-)\n\n```\nsage: a = random_matrix(ZZ,200)\nsage: time b=a.LLL()\nCPU times: user 1.90 s, sys: 0.02 s, total: 1.92 s\nWall time: 1.94\nsage: m = magma(a)\nsage: time c=m.LLL()\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 1.53\n\nsage: a = random_matrix(ZZ,400)\nsage: time b=a.LLL()\nCPU times: user 18.77 s, sys: 0.11 s, total: 18.88 s\nWall time: 19.08\nsage: time c=magma(a)\nCPU times: user 0.31 s, sys: 0.04 s, total: 0.34 s\nWall time: 0.54\nsage: time d=c.LLL()\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 19.48\n```\n\nAlso, the `sage.libs.fplll.fplll` module contains several generators for random matrices with interesting shapes.",
    "created_at": "2007-10-21T16:24:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/929",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/929#issuecomment-5664",
    "user": "https://github.com/malb"
}
```

The mandatory benchmarks of Stehle vs. Stehle :-)

```
sage: a = random_matrix(ZZ,200)
sage: time b=a.LLL()
CPU times: user 1.90 s, sys: 0.02 s, total: 1.92 s
Wall time: 1.94
sage: m = magma(a)
sage: time c=m.LLL()
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 1.53

sage: a = random_matrix(ZZ,400)
sage: time b=a.LLL()
CPU times: user 18.77 s, sys: 0.11 s, total: 18.88 s
Wall time: 19.08
sage: time c=magma(a)
CPU times: user 0.31 s, sys: 0.04 s, total: 0.34 s
Wall time: 0.54
sage: time d=c.LLL()
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 19.48
```

Also, the `sage.libs.fplll.fplll` module contains several generators for random matrices with interesting shapes.



---

archive/issue_comments_005665.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-21T22:44:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/929",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/929#issuecomment-5665",
    "user": "https://github.com/malb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_005666.json:
```json
{
    "body": "This is applied to 2.8.9.alpha0 and thus fixed.",
    "created_at": "2007-10-23T19:39:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/929",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/929#issuecomment-5666",
    "user": "https://github.com/malb"
}
```

This is applied to 2.8.9.alpha0 and thus fixed.



---

archive/issue_events_002555.json:
```json
{
    "actor": "https://github.com/malb",
    "created_at": "2007-10-23T19:39:38Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/929",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/929#event-2555"
}
```



---

archive/issue_comments_005667.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-23T19:39:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/929",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/929#issuecomment-5667",
    "user": "https://github.com/malb"
}
```

Resolution: fixed
