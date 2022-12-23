# Issue 1391: bug in unit part of factorizations of multivariate polynomials

archive/issues_001391.json:
```json
{
    "body": "Assignee: malb\n\nBehold this behavior:\n\n\n```\nsage: R.<a,b,c,d> = QQ[]\nsage: f =  (-1) * (a - d) * (-a + b) * (b - d) * (a - c) * (b - c) * (c - d)\nsage: f.factor()\n(-1) * (a - d) * (-a + b) * (b - d) * (a - c) * (b - c) * (c - d)\nsage: F = f.factor()\nsage: F[0][0]\n-1\nsage: F.unit_part ()\n1\n```\n\n\nHowever it should be that F.unit_part() is -1 and F[0][0] is a-d.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1391\n\n",
    "created_at": "2007-12-04T04:38:52Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "title": "bug in unit part of factorizations of multivariate polynomials",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1391",
    "user": "was"
}
```
Assignee: malb

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

archive/issue_comments_008948.json:
```json
{
    "body": "Bug Day material?\n\nCheers,\n\nMichael",
    "created_at": "2007-12-26T03:30:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1391#issuecomment-8948",
    "user": "mabshoff"
}
```

Bug Day material?

Cheers,

Michael



---

archive/issue_comments_008949.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-01-16T17:09:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1391#issuecomment-8949",
    "user": "malb"
}
```

Attachment



---

archive/issue_comments_008950.json:
```json
{
    "body": "The attached patch fixes the issue",
    "created_at": "2008-01-16T17:09:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1391#issuecomment-8950",
    "user": "malb"
}
```

The attached patch fixes the issue



---

archive/issue_comments_008951.json:
```json
{
    "body": "Patch looks reasonable.  The parameter to factor() is not standard sage but seems appropriate.  I say apply!",
    "created_at": "2008-01-19T22:08:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1391#issuecomment-8951",
    "user": "ncalexan"
}
```

Patch looks reasonable.  The parameter to factor() is not standard sage but seems appropriate.  I say apply!



---

archive/issue_comments_008952.json:
```json
{
    "body": "The patch no longer applies to me in 2.10.1.alpha0, so it probably needs just a rebase:\n\n```\nsage-2.10.1.alpha0/devel/sage$ patch -p1 --dry-run < trac_1391.patch\npatching file sage/rings/polynomial/multi_polynomial_libsingular.pyx\nHunk #1 FAILED at 3096.\nHunk #2 succeeded at 3159 (offset 22 lines).\n1 out of 2 hunks FAILED -- saving rejects to file sage/rings/polynomial/multi_polynomial_libsingular.pyx.rej\n```\n\nCheers,\n\nMichael",
    "created_at": "2008-01-20T02:05:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1391#issuecomment-8952",
    "user": "mabshoff"
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

archive/issue_comments_008953.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-01-20T02:15:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1391#issuecomment-8953",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_008954.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha0",
    "created_at": "2008-01-20T02:36:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1391#issuecomment-8954",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.1.alpha0



---

archive/issue_comments_008955.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-20T02:36:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1391#issuecomment-8955",
    "user": "mabshoff"
}
```

Resolution: fixed
