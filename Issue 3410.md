# Issue 3410: [with patch, needs review] conversion of matrices over polynomial rings to magma is broken

archive/issues_003410.json:
```json
{
    "body": "Assignee: @williamstein\n\nAttached patch fixes conversion of matrices over polynomial rings to magma.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3410\n\n",
    "created_at": "2008-06-13T05:29:44Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "[with patch, needs review] conversion of matrices over polynomial rings to magma is broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3410",
    "user": "@burcin"
}
```
Assignee: @williamstein

Attached patch fixes conversion of matrices over polynomial rings to magma.

Issue created by migration from https://trac.sagemath.org/ticket/3410





---

archive/issue_comments_023916.json:
```json
{
    "body": "Attachment [matrix_polyring_magma.patch](tarball://root/attachments/some-uuid/ticket3410/matrix_polyring_magma.patch) by @burcin created at 2008-06-13 05:30:44\n\nfix matrix conversion over polynomial ring to magma",
    "created_at": "2008-06-13T05:30:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3410",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3410#issuecomment-23916",
    "user": "@burcin"
}
```

Attachment [matrix_polyring_magma.patch](tarball://root/attachments/some-uuid/ticket3410/matrix_polyring_magma.patch) by @burcin created at 2008-06-13 05:30:44

fix matrix conversion over polynomial ring to magma



---

archive/issue_comments_023917.json:
```json
{
    "body": "REPORT:\n\n1. This directly conflicts with #3040\n\n2. This patch will *massively suck* performance wise, since it changes _magma_ to make a call out to Magma for every single entry of a matrix.  Thus, e.g., converting a 500x500 matrix (which takes a reasonable amount of time with #3040) will go from one single  pexpect call to magma, to 250,000 separate pexpect calls to magma, which will take literally forever. \n\nFor reason 2 this patch is not acceptable.",
    "created_at": "2008-06-13T13:41:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3410",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3410#issuecomment-23917",
    "user": "@williamstein"
}
```

REPORT:

1. This directly conflicts with #3040

2. This patch will *massively suck* performance wise, since it changes _magma_ to make a call out to Magma for every single entry of a matrix.  Thus, e.g., converting a 500x500 matrix (which takes a reasonable amount of time with #3040) will go from one single  pexpect call to magma, to 250,000 separate pexpect calls to magma, which will take literally forever. 

For reason 2 this patch is not acceptable.



---

archive/issue_comments_023918.json:
```json
{
    "body": "Attachment [trac3410-matrix_polyring_magma-2.patch](tarball://root/attachments/some-uuid/ticket3410/trac3410-matrix_polyring_magma-2.patch) by @burcin created at 2008-06-14 00:09:15\n\nfix conversion of matrices over polynomial rings to magma 2nd try",
    "created_at": "2008-06-14T00:09:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3410",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3410#issuecomment-23918",
    "user": "@burcin"
}
```

Attachment [trac3410-matrix_polyring_magma-2.patch](tarball://root/attachments/some-uuid/ticket3410/trac3410-matrix_polyring_magma-2.patch) by @burcin created at 2008-06-14 00:09:15

fix conversion of matrices over polynomial rings to magma 2nd try



---

archive/issue_comments_023919.json:
```json
{
    "body": "attachment:trac3410-matrix_polyring_magma-2.patch addresses both of the problems pointed out in comment:1. It applies to 3.0.3.alpha2, doesn't call magma for each matrix element, and on the way probably optimizes conversion of polynomials to magma as well.",
    "created_at": "2008-06-14T00:15:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3410",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3410#issuecomment-23919",
    "user": "@burcin"
}
```

attachment:trac3410-matrix_polyring_magma-2.patch addresses both of the problems pointed out in comment:1. It applies to 3.0.3.alpha2, doesn't call magma for each matrix element, and on the way probably optimizes conversion of polynomials to magma as well.



---

archive/issue_comments_023920.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_craigcitro\".",
    "created_at": "2008-06-15T21:55:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3410",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3410#issuecomment-23920",
    "user": "@craigcitro"
}
```

Changing keywords from "" to "editor_craigcitro".



---

archive/issue_comments_023921.json:
```json
{
    "body": "REVIEW:\n\nGreat!  However the function \n\n```\ndef _magma_gens(self): \n```\n\n\nneeds documentation and doctests. \n\nPending this big +1.",
    "created_at": "2008-06-20T04:05:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3410",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3410#issuecomment-23921",
    "user": "@williamstein"
}
```

REVIEW:

Great!  However the function 

```
def _magma_gens(self): 
```


needs documentation and doctests. 

Pending this big +1.



---

archive/issue_comments_023922.json:
```json
{
    "body": "Attachment [trac3410-matrix_polyring_magma-3.patch](tarball://root/attachments/some-uuid/ticket3410/trac3410-matrix_polyring_magma-3.patch) by @burcin created at 2008-06-26 15:31:51\n\nconversion of matrices over polynomial rings to magma 3rd version",
    "created_at": "2008-06-26T15:31:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3410",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3410#issuecomment-23922",
    "user": "@burcin"
}
```

Attachment [trac3410-matrix_polyring_magma-3.patch](tarball://root/attachments/some-uuid/ticket3410/trac3410-matrix_polyring_magma-3.patch) by @burcin created at 2008-06-26 15:31:51

conversion of matrices over polynomial rings to magma 3rd version



---

archive/issue_comments_023923.json:
```json
{
    "body": "attachment:trac3410-matrix_polyring_magma-3.patch adds doctests to `_magma_gens`. \n\nIn the new patch, the `_magma_init_` method introduced in attachment:trac3410-matrix_polyring_magma-2.patch is moved to sage/rings/polynomial/                multi_polynomial.pyx. This allows us to remove the _magma_ method in MPolynomial_element and extends support of conversion of matrices over polynomial rings to rings not supported by libsingular. (I.e., now ZZ[x,y] is also supported.)",
    "created_at": "2008-06-26T15:36:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3410",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3410#issuecomment-23923",
    "user": "@burcin"
}
```

attachment:trac3410-matrix_polyring_magma-3.patch adds doctests to `_magma_gens`. 

In the new patch, the `_magma_init_` method introduced in attachment:trac3410-matrix_polyring_magma-2.patch is moved to sage/rings/polynomial/                multi_polynomial.pyx. This allows us to remove the _magma_ method in MPolynomial_element and extends support of conversion of matrices over polynomial rings to rings not supported by libsingular. (I.e., now ZZ[x,y] is also supported.)



---

archive/issue_comments_023924.json:
```json
{
    "body": "REVIEW: \n\n* Enthusiastic positive review.\n\n* Note to Mabshoff -- Just apply *only* trac3410-matrix_polyring_magma-3.patch -- don't apply either of the other patches (it took me like 10 minutes to figure this out).",
    "created_at": "2008-07-01T06:46:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3410",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3410#issuecomment-23924",
    "user": "@williamstein"
}
```

REVIEW: 

* Enthusiastic positive review.

* Note to Mabshoff -- Just apply *only* trac3410-matrix_polyring_magma-3.patch -- don't apply either of the other patches (it took me like 10 minutes to figure this out).



---

archive/issue_comments_023925.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-02T19:23:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3410",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3410#issuecomment-23925",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_023926.json:
```json
{
    "body": "Merged trac3410-matrix_polyring_magma-3.patch in Sage 3.0.4.alpha2",
    "created_at": "2008-07-02T19:23:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3410",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3410#issuecomment-23926",
    "user": "mabshoff"
}
```

Merged trac3410-matrix_polyring_magma-3.patch in Sage 3.0.4.alpha2
