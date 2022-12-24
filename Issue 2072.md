# Issue 2072: Remove _neg_c_impl and _invert_c_impl from some classes.

archive/issues_002072.json:
```json
{
    "body": "Assignee: somebody\n\nUnary arithmetic operations don't benefit from the coercion model, `__neg__` and `__invert__` should be used instead. \n\nIssue created by migration from https://trac.sagemath.org/ticket/2072\n\n",
    "created_at": "2008-02-06T07:20:25Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.7",
    "title": "Remove _neg_c_impl and _invert_c_impl from some classes.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2072",
    "user": "robertwb"
}
```
Assignee: somebody

Unary arithmetic operations don't benefit from the coercion model, `__neg__` and `__invert__` should be used instead. 

Issue created by migration from https://trac.sagemath.org/ticket/2072





---

archive/issue_comments_013399.json:
```json
{
    "body": "New commits:",
    "created_at": "2015-04-13T15:35:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2072",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2072#issuecomment-13399",
    "user": "mmezzarobba"
}
```

New commits:



---

archive/issue_comments_013400.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2015-04-13T15:35:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2072",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2072#issuecomment-13400",
    "user": "mmezzarobba"
}
```

Changing priority from major to minor.



---

archive/issue_comments_013401.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-04-13T15:35:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2072",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2072#issuecomment-13401",
    "user": "mmezzarobba"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_013402.json:
```json
{
    "body": "Use `~foo` instead of `foo.__invert__()`.",
    "created_at": "2015-04-21T12:14:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2072",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2072#issuecomment-13402",
    "user": "jdemeyer"
}
```

Use `~foo` instead of `foo.__invert__()`.



---

archive/issue_comments_013403.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2015-04-21T12:14:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2072",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2072#issuecomment-13403",
    "user": "jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_013404.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2015-04-22T12:03:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2072",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2072#issuecomment-13404",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_013405.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2015-04-22T12:13:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2072",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2072#issuecomment-13405",
    "user": "mmezzarobba"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_013406.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-04-22T13:03:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2072",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2072#issuecomment-13406",
    "user": "jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_013407.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-04-23T03:21:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2072",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2072#issuecomment-13407",
    "user": "vbraun"
}
```

Resolution: fixed
