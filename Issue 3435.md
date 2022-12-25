# Issue 3435: physically delete GSL BLAS so that nothing can link against it

archive/issues_003435.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @slel\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3435\n\n",
    "created_at": "2008-06-16T00:34:34Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "physically delete GSL BLAS so that nothing can link against it",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3435",
    "user": "https://github.com/mwhansen"
}
```
Assignee: mabshoff

CC:  @slel



Issue created by migration from https://trac.sagemath.org/ticket/3435





---

archive/issue_comments_024155.json:
```json
{
    "body": "Changing type from defect to task.",
    "created_at": "2010-03-17T05:56:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3435#issuecomment-24155",
    "user": "https://github.com/jasongrout"
}
```

Changing type from defect to task.



---

archive/issue_comments_024156.json:
```json
{
    "body": "Why nothing should link against GSL BLAS?",
    "created_at": "2014-07-25T23:23:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3435#issuecomment-24156",
    "user": "https://github.com/a-andre"
}
```

Why nothing should link against GSL BLAS?



---

archive/issue_comments_024157.json:
```json
{
    "body": "This was solved by #15685 where BLAS and LAPACK were replaced by ATLAS.\n\nThen OpenBLAS was introduced as an optional package in #20129 and made standard in in #20096.",
    "created_at": "2018-11-04T23:54:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3435#issuecomment-24157",
    "user": "https://github.com/slel"
}
```

This was solved by #15685 where BLAS and LAPACK were replaced by ATLAS.

Then OpenBLAS was introduced as an optional package in #20129 and made standard in in #20096.



---

archive/issue_comments_024158.json:
```json
{
    "body": "Changing keywords from \"\" to \"blas\".",
    "created_at": "2018-11-04T23:54:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3435#issuecomment-24158",
    "user": "https://github.com/slel"
}
```

Changing keywords from "" to "blas".



---

archive/issue_comments_024159.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2018-11-04T23:54:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3435#issuecomment-24159",
    "user": "https://github.com/slel"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_024160.json:
```json
{
    "body": "Note also that BLAS linking was removed from Cython modules in #18777.",
    "created_at": "2018-11-04T23:56:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3435#issuecomment-24160",
    "user": "https://github.com/slel"
}
```

Note also that BLAS linking was removed from Cython modules in #18777.



---

archive/issue_comments_024161.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2018-11-30T20:46:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3435#issuecomment-24161",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_024162.json:
```json
{
    "body": "very old stuff indeed, obsolete",
    "created_at": "2018-11-30T20:46:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3435#issuecomment-24162",
    "user": "https://github.com/fchapoton"
}
```

very old stuff indeed, obsolete



---

archive/issue_comments_024163.json:
```json
{
    "body": "Presuming these are all correctly reviewed as either duplicate, invalid, or wontfix.",
    "created_at": "2019-02-26T13:58:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3435#issuecomment-24163",
    "user": "https://github.com/embray"
}
```

Presuming these are all correctly reviewed as either duplicate, invalid, or wontfix.



---

archive/issue_comments_024164.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2019-02-26T13:58:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3435#issuecomment-24164",
    "user": "https://github.com/embray"
}
```

Resolution: invalid
