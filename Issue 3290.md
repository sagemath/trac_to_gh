# Issue 3290: [with spkg, positive reivew] Integrate ATLAS 3.8.1 Errata

archive/issues_003290.json:
```json
{
    "body": "Assignee: mabshoff\n\nFrom http://math-atlas.sourceforge.net/errata.html#JITNaN:\n\n```\nComplex GEMM sometimes accesses C when BETA=0\nThis happens when K is much larger than M and N, and is caused by a bug in special-case GEMM code. To fix, edit ATLAS/src/blas/gemm/ATL_cmmJITcp.c, and change lines 267 and 268 from:\n\n   else  /* two or more dim < NB, requires generated cleanup */\n      NBmm0 = NBmm1 = NBmmX = Mjoin(PATLU,pKBmm);\n\nto:\n\n   else { NBmm0 = NBmm1 = NBmmX = Mjoin(PATLU,pKBmm);\n          if (SCALAR_IS_ZERO(beta)) Mjoin(PATL,gezero)(M, N, C, ldc); }\n```\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/3290\n\n",
    "closed_at": "2008-06-27T03:24:53Z",
    "created_at": "2008-05-23T20:29:59Z",
    "labels": [
        "component: numerical",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "[with spkg, positive reivew] Integrate ATLAS 3.8.1 Errata",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3290",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

From http://math-atlas.sourceforge.net/errata.html#JITNaN:

```
Complex GEMM sometimes accesses C when BETA=0
This happens when K is much larger than M and N, and is caused by a bug in special-case GEMM code. To fix, edit ATLAS/src/blas/gemm/ATL_cmmJITcp.c, and change lines 267 and 268 from:

   else  /* two or more dim < NB, requires generated cleanup */
      NBmm0 = NBmm1 = NBmmX = Mjoin(PATLU,pKBmm);

to:

   else { NBmm0 = NBmm1 = NBmmX = Mjoin(PATLU,pKBmm);
          if (SCALAR_IS_ZERO(beta)) Mjoin(PATL,gezero)(M, N, C, ldc); }
```

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/3290





---

archive/issue_comments_022716.json:
```json
{
    "body": "Changing assignee from jkantor to mabshoff.",
    "created_at": "2008-05-23T20:30:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3290#issuecomment-22716",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from jkantor to mabshoff.



---

archive/issue_comments_022717.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-05-23T20:30:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3290#issuecomment-22717",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_events_007390.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-06-27T00:27:06Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3290",
    "milestone": "sage-3.0.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3290#event-7390"
}
```



---

archive/issue_comments_022718.json:
```json
{
    "body": "This ticket is fixed in the spkg at #3380\n\nCheers,\n\nMichael",
    "created_at": "2008-06-27T00:27:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3290#issuecomment-22718",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This ticket is fixed in the spkg at #3380

Cheers,

Michael



---

archive/issue_comments_022719.json:
```json
{
    "body": "Since #3380 got a positive review by William I am also giving this ticket a positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-27T03:24:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3290#issuecomment-22719",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Since #3380 got a positive review by William I am also giving this ticket a positive review.

Cheers,

Michael



---

archive/issue_comments_022720.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha1",
    "created_at": "2008-06-27T03:24:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3290#issuecomment-22720",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.4.alpha1



---

archive/issue_events_007391.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-06-27T03:24:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3290",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3290#event-7391"
}
```



---

archive/issue_comments_022721.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-27T03:24:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3290#issuecomment-22721",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
