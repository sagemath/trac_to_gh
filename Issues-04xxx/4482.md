# Issue 4482: Sage 3.2.rc0: optional Magma doctest failure in devel/sage/sage/rings/polynomial/pbori.pyx

archive/issues_004482.json:
```json
{
    "body": "Assignee: @williamstein\n\n#4395 fixes a similar issue, but the following still fails after applying that patch:\n\n```\nsage -t -long -optional devel/sage/sage/rings/polynomial/pbori.pyx\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.1.3.final/tmp/pbori.py\", line 988:\n    sage: B._magma_() # optional requires magma\nExpected:\n    Affine Algebra of rank 3 over GF(2)\n    Lexicographical Order\n    Variables: x, y, z\n    Quotient relations:\n    [\n    x^2 + x,\n    y^2 + y,\n    z^2 + z\n    ]\nGot:\n    Affine Algebra of rank 3 over GF(2)\n    Lexicographical Order\n    Variables: x, y, z\n    Quotient relations:\n    [\n    0,\n    0,\n    0\n    ]\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.1.3.final/tmp/pbori.py\", line 1024:\n    sage: B._magma_() # optional requires magma, indirect doctest\nExpected:\n    Affine Algebra of rank 3 over GF(2)\n    Lexicographical Order\n    Variables: x, y, z\n    Quotient relations:\n    [\n    x^2 + x,\n    y^2 + y,\n    z^2 + z\n    ]\nGot:\n    Affine Algebra of rank 3 over GF(2)\n    Lexicographical Order\n    Variables: x, y, z\n    Quotient relations:\n    [\n    0,\n    0,\n    0\n    ]\n**********************************************************************\n```\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4482\n\n",
    "closed_at": "2008-11-24T22:54:48Z",
    "created_at": "2008-11-09T17:37:22Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "Sage 3.2.rc0: optional Magma doctest failure in devel/sage/sage/rings/polynomial/pbori.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4482",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @williamstein

#4395 fixes a similar issue, but the following still fails after applying that patch:

```
sage -t -long -optional devel/sage/sage/rings/polynomial/pbori.pyx
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.3.final/tmp/pbori.py", line 988:
    sage: B._magma_() # optional requires magma
Expected:
    Affine Algebra of rank 3 over GF(2)
    Lexicographical Order
    Variables: x, y, z
    Quotient relations:
    [
    x^2 + x,
    y^2 + y,
    z^2 + z
    ]
Got:
    Affine Algebra of rank 3 over GF(2)
    Lexicographical Order
    Variables: x, y, z
    Quotient relations:
    [
    0,
    0,
    0
    ]
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.3.final/tmp/pbori.py", line 1024:
    sage: B._magma_() # optional requires magma, indirect doctest
Expected:
    Affine Algebra of rank 3 over GF(2)
    Lexicographical Order
    Variables: x, y, z
    Quotient relations:
    [
    x^2 + x,
    y^2 + y,
    z^2 + z
    ]
Got:
    Affine Algebra of rank 3 over GF(2)
    Lexicographical Order
    Variables: x, y, z
    Quotient relations:
    [
    0,
    0,
    0
    ]
**********************************************************************
```

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4482





---

archive/issue_comments_033052.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-24T22:54:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4482",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4482#issuecomment-33052",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_010137.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-24T22:54:48Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4482",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4482#event-10137"
}
```



---

archive/issue_comments_033053.json:
```json
{
    "body": "Fixed in Sage 3.2.1.alpha1 via #4601.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-24T22:54:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4482",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4482#issuecomment-33053",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Fixed in Sage 3.2.1.alpha1 via #4601.

Cheers,

Michael
