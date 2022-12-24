# Issue 8833: fix riemann.pyx numerical noise issues on t2 (etc.)

archive/issues_008833.json:
```json
{
    "body": "Assignee: burcin\n\nA new patch introduced some new noise.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8833\n\n",
    "created_at": "2010-05-01T06:01:55Z",
    "labels": [
        "calculus",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.1",
    "title": "fix riemann.pyx numerical noise issues on t2 (etc.)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8833",
    "user": "was"
}
```
Assignee: burcin

A new patch introduced some new noise.

Issue created by migration from https://trac.sagemath.org/ticket/8833





---

archive/issue_comments_081225.json:
```json
{
    "body": "Attachment [trac_8833.patch](tarball://root/attachments/some-uuid/ticket8833/trac_8833.patch) by was created at 2010-05-01 06:03:02",
    "created_at": "2010-05-01T06:03:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8833#issuecomment-81225",
    "user": "was"
}
```

Attachment [trac_8833.patch](tarball://root/attachments/some-uuid/ticket8833/trac_8833.patch) by was created at 2010-05-01 06:03:02



---

archive/issue_comments_081226.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-01T06:03:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8833#issuecomment-81226",
    "user": "was"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_081227.json:
```json
{
    "body": "I had these failures on 64-bit Ubuntu 9.10 Intel Core Duo 2 with 4.4.1.alpha2.  This patch was rolled into 4.4.1.alpha3 and as part of building that (with long tests enabled) this change passed the tests.  And it looks harmless, just shortening up precision by a digit or two.  So, positive review.",
    "created_at": "2010-05-01T14:37:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8833#issuecomment-81227",
    "user": "rbeezer"
}
```

I had these failures on 64-bit Ubuntu 9.10 Intel Core Duo 2 with 4.4.1.alpha2.  This patch was rolled into 4.4.1.alpha3 and as part of building that (with long tests enabled) this change passed the tests.  And it looks harmless, just shortening up precision by a digit or two.  So, positive review.



---

archive/issue_comments_081228.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-01T14:37:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8833#issuecomment-81228",
    "user": "rbeezer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_081229.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-01T19:18:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8833#issuecomment-81229",
    "user": "was"
}
```

Resolution: fixed
