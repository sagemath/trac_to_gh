# Issue 4035: [with patch, needs review] fix optional doctests for multivariate polynomials

archive/issues_004035.json:
```json
{
    "body": "Assignee: malb\n\nCC:  mhansen\n\nSee attached patch.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4035\n\n",
    "created_at": "2008-09-01T09:55:46Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] fix optional doctests for multivariate polynomials",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4035",
    "user": "malb"
}
```
Assignee: malb

CC:  mhansen

See attached patch.

Issue created by migration from https://trac.sagemath.org/ticket/4035





---

archive/issue_comments_029107.json:
```json
{
    "body": "Attachment\n\nGary, can you review this (I'm asking you since it involves M2)",
    "created_at": "2008-09-01T09:56:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4035",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4035#issuecomment-29107",
    "user": "malb"
}
```

Attachment

Gary, can you review this (I'm asking you since it involves M2)



---

archive/issue_comments_029108.json:
```json
{
    "body": "I assume this ticket depends on the series of changes you made starting with the number field support? As is the patch does not apply.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-04T00:22:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4035",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4035#issuecomment-29108",
    "user": "mabshoff"
}
```

I assume this ticket depends on the series of changes you made starting with the number field support? As is the patch does not apply.

Cheers,

Michael



---

archive/issue_comments_029109.json:
```json
{
    "body": "yeah, that could be.",
    "created_at": "2008-09-04T01:17:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4035",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4035#issuecomment-29109",
    "user": "malb"
}
```

yeah, that could be.



---

archive/issue_comments_029110.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-20T15:47:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4035",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4035#issuecomment-29110",
    "user": "malb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_029111.json:
```json
{
    "body": "Unfortunately this patch has bitrotted:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.alpha1/devel/sage$ patch -p1 < trac_4035_m2_optional_doctests.patch \npatching file sage/rings/polynomial/multi_polynomial.pyx\npatching file sage/rings/polynomial/multi_polynomial_ideal.py\nHunk #1 FAILED at 60.\nHunk #2 succeeded at 1659 (offset 58 lines).\nHunk #3 succeeded at 1883 (offset 64 lines).\nHunk #4 FAILED at 2031.\n2 out of 4 hunks FAILED -- saving rejects to file sage/rings/polynomial/multi_polynomial_ideal.py.rej\npatching file sage/rings/polynomial/multi_polynomial_ring.py\n```\n\n\nMike: Once it is rebased can you review it?\n\nCheers,\n\nMichael",
    "created_at": "2008-10-26T21:39:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4035",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4035#issuecomment-29111",
    "user": "mabshoff"
}
```

Unfortunately this patch has bitrotted:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.alpha1/devel/sage$ patch -p1 < trac_4035_m2_optional_doctests.patch 
patching file sage/rings/polynomial/multi_polynomial.pyx
patching file sage/rings/polynomial/multi_polynomial_ideal.py
Hunk #1 FAILED at 60.
Hunk #2 succeeded at 1659 (offset 58 lines).
Hunk #3 succeeded at 1883 (offset 64 lines).
Hunk #4 FAILED at 2031.
2 out of 4 hunks FAILED -- saving rejects to file sage/rings/polynomial/multi_polynomial_ideal.py.rej
patching file sage/rings/polynomial/multi_polynomial_ring.py
```


Mike: Once it is rebased can you review it?

Cheers,

Michael



---

archive/issue_comments_029112.json:
```json
{
    "body": "Fixed via the patch at #4420.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-02T16:16:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4035",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4035#issuecomment-29112",
    "user": "mabshoff"
}
```

Fixed via the patch at #4420.

Cheers,

Michael



---

archive/issue_comments_029113.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-02T16:16:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4035",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4035#issuecomment-29113",
    "user": "mabshoff"
}
```

Resolution: fixed
