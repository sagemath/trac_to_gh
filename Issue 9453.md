# Issue 9453: Implement Aurifeuillian factorization

archive/issues_009453.json:
```json
{
    "body": "Assignee: tbd\n\nImplement Aurifeuillian factorization of integers, see\nhttp://mathworld.wolfram.com/AurifeuilleanFactorization.html\n\nIssue created by migration from https://trac.sagemath.org/ticket/9453\n\n",
    "created_at": "2010-07-08T14:12:32Z",
    "labels": [
        "factorization",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7.2",
    "title": "Implement Aurifeuillian factorization",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9453",
    "user": "jdemeyer"
}
```
Assignee: tbd

Implement Aurifeuillian factorization of integers, see
http://mathworld.wolfram.com/AurifeuilleanFactorization.html

Issue created by migration from https://trac.sagemath.org/ticket/9453





---

archive/issue_comments_090583.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-12-08T10:06:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9453#issuecomment-90583",
    "user": "aapitzsch"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_090584.json:
```json
{
    "body": "#5945 has to be applied first because of the new factorint.pyx module.",
    "created_at": "2010-12-08T10:06:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9453#issuecomment-90584",
    "user": "aapitzsch"
}
```

#5945 has to be applied first because of the new factorint.pyx module.



---

archive/issue_comments_090585.json:
```json
{
    "body": "Obviously, it should be implemented in general, not only for bases 2,3 and 5...",
    "created_at": "2010-12-08T10:16:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9453#issuecomment-90585",
    "user": "jdemeyer"
}
```

Obviously, it should be implemented in general, not only for bases 2,3 and 5...



---

archive/issue_comments_090586.json:
```json
{
    "body": "Depends on #5945\n\nHere is a more general version.",
    "created_at": "2010-12-22T16:55:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9453#issuecomment-90586",
    "user": "aapitzsch"
}
```

Depends on #5945

Here is a more general version.



---

archive/issue_comments_090587.json:
```json
{
    "body": "Attachment [trac_9453_aurifeuillian_factorization.patch](tarball://root/attachments/some-uuid/ticket9453/trac_9453_aurifeuillian_factorization.patch) by aapitzsch created at 2011-01-17 13:41:43\n\nDepends on #5945 and #10623",
    "created_at": "2011-01-17T13:41:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9453#issuecomment-90587",
    "user": "aapitzsch"
}
```

Attachment [trac_9453_aurifeuillian_factorization.patch](tarball://root/attachments/some-uuid/ticket9453/trac_9453_aurifeuillian_factorization.patch) by aapitzsch created at 2011-01-17 13:41:43

Depends on #5945 and #10623



---

archive/issue_comments_090588.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-06-15T14:18:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9453#issuecomment-90588",
    "user": "mariah"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_090589.json:
```json
{
    "body": "Applied patch to sage-4.7.1.alpha2 and did 'make testlong'.  All tests passed.  Positive review!",
    "created_at": "2011-06-15T14:18:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9453#issuecomment-90589",
    "user": "mariah"
}
```

Applied patch to sage-4.7.1.alpha2 and did 'make testlong'.  All tests passed.  Positive review!



---

archive/issue_comments_090590.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-07-22T17:06:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9453#issuecomment-90590",
    "user": "jdemeyer"
}
```

Resolution: fixed
