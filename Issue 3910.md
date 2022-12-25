# Issue 3910: [with patch,  needs review] adjust interval printing: precise integers print as integers

archive/issues_003910.json:
```json
{
    "body": "Assignee: somebody\n\nThis patch adjusts interval printing so that sufficiently small precise integers print as integers.  (It also fixes a loss-of-precision bug when one endpoint is tiny and the other endpoint is zero.)\n\nBefore:\n\n```\nsage: RIF(0)\n0.?e-17\nsage: RIF(1)\n1.0000000000000000?\nsage: RIF(0, 2^-256)\n1.?e-17\n```\n\n\nAfter:\n\n```\nsage: RIF(0)\n0\nsage: RIF(1)\n1\nsage: RIF(0, 2^-256)\n1.?e-77\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3910\n\n",
    "created_at": "2008-08-20T14:22:59Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "[with patch,  needs review] adjust interval printing: precise integers print as integers",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3910",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: somebody

This patch adjusts interval printing so that sufficiently small precise integers print as integers.  (It also fixes a loss-of-precision bug when one endpoint is tiny and the other endpoint is zero.)

Before:

```
sage: RIF(0)
0.?e-17
sage: RIF(1)
1.0000000000000000?
sage: RIF(0, 2^-256)
1.?e-17
```


After:

```
sage: RIF(0)
0
sage: RIF(1)
1
sage: RIF(0, 2^-256)
1.?e-77
```



Issue created by migration from https://trac.sagemath.org/ticket/3910





---

archive/issue_comments_027912.json:
```json
{
    "body": "Attachment [trac3910-interval-integers.patch](tarball://root/attachments/some-uuid/ticket3910/trac3910-interval-integers.patch) by cwitty created at 2008-08-20 14:23:57",
    "created_at": "2008-08-20T14:23:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3910",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3910#issuecomment-27912",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [trac3910-interval-integers.patch](tarball://root/attachments/some-uuid/ticket3910/trac3910-interval-integers.patch) by cwitty created at 2008-08-20 14:23:57



---

archive/issue_comments_027913.json:
```json
{
    "body": "The design decision behind this was well aired on sage-devel and I seem to remember the consensus was for this change.\n\nThe patch (a lot of which consists in changing the doctest outputs) looks fine, applies cleanly to 3.1.1 and passes all doctests in sage/rings and sage/calculus.  I did not check the docs.\n\nI recommend that this passes.",
    "created_at": "2008-08-23T20:47:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3910",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3910#issuecomment-27913",
    "user": "https://github.com/JohnCremona"
}
```

The design decision behind this was well aired on sage-devel and I seem to remember the consensus was for this change.

The patch (a lot of which consists in changing the doctest outputs) looks fine, applies cleanly to 3.1.1 and passes all doctests in sage/rings and sage/calculus.  I did not check the docs.

I recommend that this passes.



---

archive/issue_comments_027914.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha1. All doctests pass with the patch applied.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-25T01:43:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3910",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3910#issuecomment-27914",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.2.alpha1. All doctests pass with the patch applied.

Cheers,

Michael



---

archive/issue_comments_027915.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-25T01:43:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3910",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3910#issuecomment-27915",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
