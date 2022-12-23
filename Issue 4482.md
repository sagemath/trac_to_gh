# Issue 4482: Sage 3.2.rc0: optional Magma doctest failure in devel/sage/sage/rings/polynomial/pbori.pyx

archive/issues_004482.json:
```json
{
    "body": "Assignee: was\n\n#4395 fixes a similar issue, but the following still fails after applying that patch:\n\n```\nsage -t -long -optional devel/sage/sage/rings/polynomial/pbori.pyx\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.1.3.final/tmp/pbori.py\", line 988:\n    sage: B._magma_() # optional requires magma\nExpected:\n    Affine Algebra of rank 3 over GF(2)\n    Lexicographical Order\n    Variables: x, y, z\n    Quotient relations:\n    [\n    x^2 + x,\n    y^2 + y,\n    z^2 + z\n    ]\nGot:\n    Affine Algebra of rank 3 over GF(2)\n    Lexicographical Order\n    Variables: x, y, z\n    Quotient relations:\n    [\n    0,\n    0,\n    0\n    ]\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.1.3.final/tmp/pbori.py\", line 1024:\n    sage: B._magma_() # optional requires magma, indirect doctest\nExpected:\n    Affine Algebra of rank 3 over GF(2)\n    Lexicographical Order\n    Variables: x, y, z\n    Quotient relations:\n    [\n    x^2 + x,\n    y^2 + y,\n    z^2 + z\n    ]\nGot:\n    Affine Algebra of rank 3 over GF(2)\n    Lexicographical Order\n    Variables: x, y, z\n    Quotient relations:\n    [\n    0,\n    0,\n    0\n    ]\n**********************************************************************\n```\n\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4482\n\n",
    "created_at": "2008-11-09T17:37:22Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "title": "Sage 3.2.rc0: optional Magma doctest failure in devel/sage/sage/rings/polynomial/pbori.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4482",
    "user": "mabshoff"
}
```
Assignee: was

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

archive/issue_comments_033117.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-24T22:54:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4482",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4482#issuecomment-33117",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_033118.json:
```json
{
    "body": "Fixed in Sage 3.2.1.alpha1 via #4601.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-24T22:54:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4482",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4482#issuecomment-33118",
    "user": "mabshoff"
}
```

Fixed in Sage 3.2.1.alpha1 via #4601.

Cheers,

Michael
