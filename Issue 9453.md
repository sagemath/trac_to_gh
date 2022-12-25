# Issue 9453: Implement Aurifeuillian factorization

archive/issues_009453.json:
```json
{
    "body": "Assignee: tbd\n\nImplement Aurifeuillian factorization of integers, see\nhttp://mathworld.wolfram.com/AurifeuilleanFactorization.html\n\nIssue created by migration from https://trac.sagemath.org/ticket/9453\n\n",
    "created_at": "2010-07-08T14:12:32Z",
    "labels": [
        "component: factorization",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7.2",
    "title": "Implement Aurifeuillian factorization",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9453",
    "user": "https://github.com/jdemeyer"
}
```
Assignee: tbd

Implement Aurifeuillian factorization of integers, see
http://mathworld.wolfram.com/AurifeuilleanFactorization.html

Issue created by migration from https://trac.sagemath.org/ticket/9453





---

archive/issue_comments_090434.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-12-08T10:06:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9453#issuecomment-90434",
    "user": "https://github.com/a-andre"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_090435.json:
```json
{
    "body": "#5945 has to be applied first because of the new factorint.pyx module.",
    "created_at": "2010-12-08T10:06:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9453#issuecomment-90435",
    "user": "https://github.com/a-andre"
}
```

#5945 has to be applied first because of the new factorint.pyx module.



---

archive/issue_comments_090436.json:
```json
{
    "body": "Obviously, it should be implemented in general, not only for bases 2,3 and 5...",
    "created_at": "2010-12-08T10:16:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9453#issuecomment-90436",
    "user": "https://github.com/jdemeyer"
}
```

Obviously, it should be implemented in general, not only for bases 2,3 and 5...



---

archive/issue_comments_090437.json:
```json
{
    "body": "Depends on #5945\n\nHere is a more general version.",
    "created_at": "2010-12-22T16:55:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9453#issuecomment-90437",
    "user": "https://github.com/a-andre"
}
```

Depends on #5945

Here is a more general version.



---

archive/issue_comments_090438.json:
```json
{
    "body": "Attachment [trac_9453_aurifeuillian_factorization.patch](tarball://root/attachments/some-uuid/ticket9453/trac_9453_aurifeuillian_factorization.patch) by @a-andre created at 2011-01-17 13:41:43\n\nDepends on #5945 and #10623",
    "created_at": "2011-01-17T13:41:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9453#issuecomment-90438",
    "user": "https://github.com/a-andre"
}
```

Attachment [trac_9453_aurifeuillian_factorization.patch](tarball://root/attachments/some-uuid/ticket9453/trac_9453_aurifeuillian_factorization.patch) by @a-andre created at 2011-01-17 13:41:43

Depends on #5945 and #10623



---

archive/issue_comments_090439.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-06-15T14:18:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9453#issuecomment-90439",
    "user": "https://trac.sagemath.org/admin/accounts/users/mariah"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_090440.json:
```json
{
    "body": "Applied patch to sage-4.7.1.alpha2 and did 'make testlong'.  All tests passed.  Positive review!",
    "created_at": "2011-06-15T14:18:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9453#issuecomment-90440",
    "user": "https://trac.sagemath.org/admin/accounts/users/mariah"
}
```

Applied patch to sage-4.7.1.alpha2 and did 'make testlong'.  All tests passed.  Positive review!



---

archive/issue_comments_090441.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-07-22T17:06:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9453#issuecomment-90441",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_009609.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-07-22T17:06:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9453",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9453#event-9609"
}
```
