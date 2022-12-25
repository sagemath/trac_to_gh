# Issue 1391: bug in unit part of factorizations of multivariate polynomials

archive/issues_001391.json:
```json
{
    "body": "Assignee: @malb\n\nBehold this behavior:\n\n\n```\nsage: R.<a,b,c,d> = QQ[]\nsage: f =  (-1) * (a - d) * (-a + b) * (b - d) * (a - c) * (b - c) * (c - d)\nsage: f.factor()\n(-1) * (a - d) * (-a + b) * (b - d) * (a - c) * (b - c) * (c - d)\nsage: F = f.factor()\nsage: F[0][0]\n-1\nsage: F.unit_part ()\n1\n```\n\n\nHowever it should be that F.unit_part() is -1 and F[0][0] is a-d.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1391\n\n",
    "created_at": "2007-12-04T04:38:52Z",
    "labels": [
        "component: commutative algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "bug in unit part of factorizations of multivariate polynomials",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1391",
    "user": "https://github.com/williamstein"
}
```
Assignee: @malb

Behold this behavior:


```
sage: R.<a,b,c,d> = QQ[]
sage: f =  (-1) * (a - d) * (-a + b) * (b - d) * (a - c) * (b - c) * (c - d)
sage: f.factor()
(-1) * (a - d) * (-a + b) * (b - d) * (a - c) * (b - c) * (c - d)
sage: F = f.factor()
sage: F[0][0]
-1
sage: F.unit_part ()
1
```


However it should be that F.unit_part() is -1 and F[0][0] is a-d.

Issue created by migration from https://trac.sagemath.org/ticket/1391





---

archive/issue_comments_008924.json:
```json
{
    "body": "Bug Day material?\n\nCheers,\n\nMichael",
    "created_at": "2007-12-26T03:30:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1391#issuecomment-8924",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Bug Day material?

Cheers,

Michael



---

archive/issue_comments_008925.json:
```json
{
    "body": "Attachment [trac_1391.patch](tarball://root/attachments/some-uuid/ticket1391/trac_1391.patch) by @malb created at 2008-01-16 17:09:12",
    "created_at": "2008-01-16T17:09:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1391#issuecomment-8925",
    "user": "https://github.com/malb"
}
```

Attachment [trac_1391.patch](tarball://root/attachments/some-uuid/ticket1391/trac_1391.patch) by @malb created at 2008-01-16 17:09:12



---

archive/issue_comments_008926.json:
```json
{
    "body": "The attached patch fixes the issue",
    "created_at": "2008-01-16T17:09:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1391#issuecomment-8926",
    "user": "https://github.com/malb"
}
```

The attached patch fixes the issue



---

archive/issue_comments_008927.json:
```json
{
    "body": "Patch looks reasonable.  The parameter to factor() is not standard sage but seems appropriate.  I say apply!",
    "created_at": "2008-01-19T22:08:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1391#issuecomment-8927",
    "user": "https://github.com/ncalexan"
}
```

Patch looks reasonable.  The parameter to factor() is not standard sage but seems appropriate.  I say apply!



---

archive/issue_comments_008928.json:
```json
{
    "body": "The patch no longer applies to me in 2.10.1.alpha0, so it probably needs just a rebase:\n\n```\nsage-2.10.1.alpha0/devel/sage$ patch -p1 --dry-run < trac_1391.patch\npatching file sage/rings/polynomial/multi_polynomial_libsingular.pyx\nHunk #1 FAILED at 3096.\nHunk #2 succeeded at 3159 (offset 22 lines).\n1 out of 2 hunks FAILED -- saving rejects to file sage/rings/polynomial/multi_polynomial_libsingular.pyx.rej\n```\n\nCheers,\n\nMichael",
    "created_at": "2008-01-20T02:05:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1391#issuecomment-8928",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The patch no longer applies to me in 2.10.1.alpha0, so it probably needs just a rebase:

```
sage-2.10.1.alpha0/devel/sage$ patch -p1 --dry-run < trac_1391.patch
patching file sage/rings/polynomial/multi_polynomial_libsingular.pyx
Hunk #1 FAILED at 3096.
Hunk #2 succeeded at 3159 (offset 22 lines).
1 out of 2 hunks FAILED -- saving rejects to file sage/rings/polynomial/multi_polynomial_libsingular.pyx.rej
```

Cheers,

Michael



---

archive/issue_comments_008929.json:
```json
{
    "body": "Attachment [trac-1391-apply_after_patch_rej_from_other_patch.patch](tarball://root/attachments/some-uuid/ticket1391/trac-1391-apply_after_patch_rej_from_other_patch.patch) by @williamstein created at 2008-01-20 02:15:35",
    "created_at": "2008-01-20T02:15:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1391#issuecomment-8929",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac-1391-apply_after_patch_rej_from_other_patch.patch](tarball://root/attachments/some-uuid/ticket1391/trac-1391-apply_after_patch_rej_from_other_patch.patch) by @williamstein created at 2008-01-20 02:15:35



---

archive/issue_comments_008930.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha0",
    "created_at": "2008-01-20T02:36:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1391#issuecomment-8930",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.1.alpha0



---

archive/issue_comments_008931.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-20T02:36:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1391#issuecomment-8931",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_001535.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-01-20T02:36:50Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1391",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1391#event-1535"
}
```
