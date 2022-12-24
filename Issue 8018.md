# Issue 8018: Eigenvalues sorted, but not eigenvectors, in modular/modform/numerical.py

archive/issues_008018.json:
```json
{
    "body": "Assignee: craigcitro\n\nCC:  was\n\nIn `sage/modular/modform/numerical.py`, the last half of `_eigenvectors` looks for eigenvectors with eigenvalues having multiplicty 1.  The eigenvalues get sorted for openers, but the eigenvectors in `B` don't follow along.\n\nPrint statements before and after the sort, and then running doctests on just this file, produces output like:\n\n\n```\n    Hecke: before sort [-283.0, 108.522012456, -92.2176402155, -90.3043722401, 142.0]\n    Hecke: after sort [-283.0, -92.2176402155, -90.3043722401, 108.522012456, 142.0]\n```\n\n\nOne fix would be to delete the sorting if the order of the eigenvectors is not important.\n\nAll the doctests in this module that call this code lack eigenvalues of multiplicity greater than 1, so maybe a new doctest could test this case.\n\nAlso, it appears the cached value returned differs from the return at the bottom of the function.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8018\n\n",
    "created_at": "2010-01-21T00:24:52Z",
    "labels": [
        "modular forms",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "Eigenvalues sorted, but not eigenvectors, in modular/modform/numerical.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8018",
    "user": "rbeezer"
}
```
Assignee: craigcitro

CC:  was

In `sage/modular/modform/numerical.py`, the last half of `_eigenvectors` looks for eigenvectors with eigenvalues having multiplicty 1.  The eigenvalues get sorted for openers, but the eigenvectors in `B` don't follow along.

Print statements before and after the sort, and then running doctests on just this file, produces output like:


```
    Hecke: before sort [-283.0, 108.522012456, -92.2176402155, -90.3043722401, 142.0]
    Hecke: after sort [-283.0, -92.2176402155, -90.3043722401, 108.522012456, 142.0]
```


One fix would be to delete the sorting if the order of the eigenvectors is not important.

All the doctests in this module that call this code lack eigenvalues of multiplicity greater than 1, so maybe a new doctest could test this case.

Also, it appears the cached value returned differs from the return at the bottom of the function.

Issue created by migration from https://trac.sagemath.org/ticket/8018





---

archive/issue_comments_070066.json:
```json
{
    "body": "This patch depends on #4756 due to intermediate changes in some of the CDF eigenvector code, so apply that patch first.  Since this patch computes the eigenvalues directly, it is not necessary to understand #4756.\n\nSummary:\n\n1.  Return value has changed to be the subset of eigenvectors with multiplicity one, rather than all the eigenvectors.  First few lines (immediate return without recalculation) indicate this was the intent.\n\n2.  The eigenvalues do not get sorted now, fixing the observed bug.  An extra check of `uniq` will cause the loop to speed-up when the eigenvector has high multiplicity.\n\n3.  Eigenvalues and eigenvectors are computed directly via `SciPy`.  This avoids various conversion overhead.\n\n4.  Lots of blank lines marked as changed in the patch file.  An accident of a massive cut/paste job to recover from an error.",
    "created_at": "2010-01-24T05:25:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8018#issuecomment-70066",
    "user": "rbeezer"
}
```

This patch depends on #4756 due to intermediate changes in some of the CDF eigenvector code, so apply that patch first.  Since this patch computes the eigenvalues directly, it is not necessary to understand #4756.

Summary:

1.  Return value has changed to be the subset of eigenvectors with multiplicity one, rather than all the eigenvectors.  First few lines (immediate return without recalculation) indicate this was the intent.

2.  The eigenvalues do not get sorted now, fixing the observed bug.  An extra check of `uniq` will cause the loop to speed-up when the eigenvector has high multiplicity.

3.  Eigenvalues and eigenvectors are computed directly via `SciPy`.  This avoids various conversion overhead.

4.  Lots of blank lines marked as changed in the patch file.  An accident of a massive cut/paste job to recover from an error.



---

archive/issue_comments_070067.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-24T05:25:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8018#issuecomment-70067",
    "user": "rbeezer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_070068.json:
```json
{
    "body": "Attachment [trac_8018-numerical-eigenforms.patch](tarball://root/attachments/some-uuid/ticket8018/trac_8018-numerical-eigenforms.patch) by rbeezer created at 2010-01-24 05:25:32",
    "created_at": "2010-01-24T05:25:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8018#issuecomment-70068",
    "user": "rbeezer"
}
```

Attachment [trac_8018-numerical-eigenforms.patch](tarball://root/attachments/some-uuid/ticket8018/trac_8018-numerical-eigenforms.patch) by rbeezer created at 2010-01-24 05:25:32



---

archive/issue_comments_070069.json:
```json
{
    "body": "Looks good.",
    "created_at": "2010-04-03T07:53:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8018#issuecomment-70069",
    "user": "AlexGhitza"
}
```

Looks good.



---

archive/issue_comments_070070.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-03T07:53:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8018#issuecomment-70070",
    "user": "AlexGhitza"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_070071.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-15T20:12:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8018#issuecomment-70071",
    "user": "jhpalmieri"
}
```

Resolution: fixed



---

archive/issue_comments_070072.json:
```json
{
    "body": "Merged \"trac_8018-numerical-eigenforms.patch\" in 4.4.alpha0",
    "created_at": "2010-04-15T20:12:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8018#issuecomment-70072",
    "user": "jhpalmieri"
}
```

Merged "trac_8018-numerical-eigenforms.patch" in 4.4.alpha0
