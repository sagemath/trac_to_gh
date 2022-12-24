# Issue 7577: move multivariate polynomials over RR to libsingular

archive/issues_007577.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  @burcin nchoen\n\nSingular supports real numbers as 'base field', we only need to implement the conversion routines.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7577\n\n",
    "created_at": "2009-12-01T23:14:00Z",
    "labels": [
        "commutative algebra",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "move multivariate polynomials over RR to libsingular",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7577",
    "user": "@malb"
}
```
Assignee: @malb

CC:  @burcin nchoen

Singular supports real numbers as 'base field', we only need to implement the conversion routines.

Issue created by migration from https://trac.sagemath.org/ticket/7577





---

archive/issue_comments_064534.json:
```json
{
    "body": "Attachment [mpolynomial_rr_libsingular.patch](tarball://root/attachments/some-uuid/ticket7577/mpolynomial_rr_libsingular.patch) by @malb created at 2009-12-01 23:15:19\n\nI am CCing burcin because he knows libSingular and I am CCing ncohen because I wrote this patch in order to speed up the linear programming interface.",
    "created_at": "2009-12-01T23:15:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7577",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7577#issuecomment-64534",
    "user": "@malb"
}
```

Attachment [mpolynomial_rr_libsingular.patch](tarball://root/attachments/some-uuid/ticket7577/mpolynomial_rr_libsingular.patch) by @malb created at 2009-12-01 23:15:19

I am CCing burcin because he knows libSingular and I am CCing ncohen because I wrote this patch in order to speed up the linear programming interface.



---

archive/issue_comments_064535.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2009-12-02T13:04:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7577",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7577#issuecomment-64535",
    "user": "@mwhansen"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_064536.json:
```json
{
    "body": "I get the following failures with this patch:\n\n\n```\n        sage -t  devel/sage-main/sage/matrix/matrix_sparse.pyx # 1 doctests failed\n        sage -t  devel/sage-main/sage/calculus/desolvers.py # Segfault\n        sage -t  devel/sage-main/sage/rings/polynomial/multi_polynomial.pyx # 2 doctests failed\n        sage -t  devel/sage-main/sage/matrix/matrix_mpolynomial_dense.pyx # 2 doctests failed\n```\n",
    "created_at": "2009-12-02T13:04:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7577",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7577#issuecomment-64536",
    "user": "@mwhansen"
}
```

I get the following failures with this patch:


```
        sage -t  devel/sage-main/sage/matrix/matrix_sparse.pyx # 1 doctests failed
        sage -t  devel/sage-main/sage/calculus/desolvers.py # Segfault
        sage -t  devel/sage-main/sage/rings/polynomial/multi_polynomial.pyx # 2 doctests failed
        sage -t  devel/sage-main/sage/matrix/matrix_mpolynomial_dense.pyx # 2 doctests failed
```




---

archive/issue_comments_064537.json:
```json
{
    "body": "On what kind of machine?",
    "created_at": "2009-12-02T13:30:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7577",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7577#issuecomment-64537",
    "user": "@malb"
}
```

On what kind of machine?



---

archive/issue_comments_064538.json:
```json
{
    "body": "On sage.math.  This is with the new Singular spkg from 7194.",
    "created_at": "2009-12-02T13:31:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7577",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7577#issuecomment-64538",
    "user": "@mwhansen"
}
```

On sage.math.  This is with the new Singular spkg from 7194.



---

archive/issue_comments_064539.json:
```json
{
    "body": "I can reproduce\n\n\n```\nsage -t  devel/sage-main/sage/matrix/matrix_sparse.pyx # 1 doctests failed\nsage -t  devel/sage-main/sage/calculus/desolvers.py # Segfault\nsage -t  devel/sage-main/sage/matrix/matrix_mpolynomial_dense.pyx # 2 doctests failed\n```\n\n\nbut not\n\n\n```\nsage -t  devel/sage-main/sage/rings/polynomial/multi_polynomial.pyx # 2 doctests failed\n```\n\n\nI am attaching a fix for the failures I can reproduce.",
    "created_at": "2009-12-02T14:13:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7577",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7577#issuecomment-64539",
    "user": "@malb"
}
```

I can reproduce


```
sage -t  devel/sage-main/sage/matrix/matrix_sparse.pyx # 1 doctests failed
sage -t  devel/sage-main/sage/calculus/desolvers.py # Segfault
sage -t  devel/sage-main/sage/matrix/matrix_mpolynomial_dense.pyx # 2 doctests failed
```


but not


```
sage -t  devel/sage-main/sage/rings/polynomial/multi_polynomial.pyx # 2 doctests failed
```


I am attaching a fix for the failures I can reproduce.



---

archive/issue_comments_064540.json:
```json
{
    "body": "There is another issue: Singular uses MPF instead of MPFR to implement floating point numbers. Thus, we get less assurance about the precision with this new patch.",
    "created_at": "2009-12-02T14:14:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7577",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7577#issuecomment-64540",
    "user": "@malb"
}
```

There is another issue: Singular uses MPF instead of MPFR to implement floating point numbers. Thus, we get less assurance about the precision with this new patch.



---

archive/issue_comments_064541.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2009-12-02T14:14:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7577",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7577#issuecomment-64541",
    "user": "@malb"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_064542.json:
```json
{
    "body": "Attachment [mpolynomial_rr_libsingular_fixes.patch](tarball://root/attachments/some-uuid/ticket7577/mpolynomial_rr_libsingular_fixes.patch) by @malb created at 2009-12-02 14:32:32",
    "created_at": "2009-12-02T14:32:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7577",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7577#issuecomment-64542",
    "user": "@malb"
}
```

Attachment [mpolynomial_rr_libsingular_fixes.patch](tarball://root/attachments/some-uuid/ticket7577/mpolynomial_rr_libsingular_fixes.patch) by @malb created at 2009-12-02 14:32:32
