# Issue 8136: fix ref manual issues in linear_code.py

archive/issues_008136.json:
```json
{
    "body": "Assignee: wdj\n\nCC:  spancratz\n\nBuilding the reference manual in 4.3.2.alpha0 produces some warnings for the file linear_code.py, I think coming from #6486.  The attached patch fixes them.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8136\n\n",
    "created_at": "2010-01-31T06:48:52Z",
    "labels": [
        "coding theory",
        "major",
        "bug"
    ],
    "title": "fix ref manual issues in linear_code.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8136",
    "user": "jhpalmieri"
}
```
Assignee: wdj

CC:  spancratz

Building the reference manual in 4.3.2.alpha0 produces some warnings for the file linear_code.py, I think coming from #6486.  The attached patch fixes them.


Issue created by migration from https://trac.sagemath.org/ticket/8136





---

archive/issue_comments_071549.json:
```json
{
    "body": "Attachment [trac_8136-ref-manual.patch](tarball://root/attachments/some-uuid/ticket8136/trac_8136-ref-manual.patch) by jhpalmieri created at 2010-01-31 06:50:26",
    "created_at": "2010-01-31T06:50:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8136",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8136#issuecomment-71549",
    "user": "jhpalmieri"
}
```

Attachment [trac_8136-ref-manual.patch](tarball://root/attachments/some-uuid/ticket8136/trac_8136-ref-manual.patch) by jhpalmieri created at 2010-01-31 06:50:26



---

archive/issue_comments_071550.json:
```json
{
    "body": "I'll referee this, unless someone beats me to it. Thanks very much for fixing this up!",
    "created_at": "2010-01-31T15:04:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8136",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8136#issuecomment-71550",
    "user": "wdj"
}
```

I'll referee this, unless someone beats me to it. Thanks very much for fixing this up!



---

archive/issue_comments_071551.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-31T17:52:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8136",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8136#issuecomment-71551",
    "user": "wdj"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071552.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-31T17:53:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8136",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8136#issuecomment-71552",
    "user": "wdj"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071553.json:
```json
{
    "body": "This applied fine to 4.3.2.a0 and pased sage -testall except for apparently unrelated failures on a mac 10.6.2.\n\nPositive review.",
    "created_at": "2010-01-31T17:53:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8136",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8136#issuecomment-71553",
    "user": "wdj"
}
```

This applied fine to 4.3.2.a0 and pased sage -testall except for apparently unrelated failures on a mac 10.6.2.

Positive review.



---

archive/issue_comments_071554.json:
```json
{
    "body": "Thank you very much for this, John! The total number of warnings resulting from building the HTML version of the reference manual is now 151.",
    "created_at": "2010-02-02T00:27:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8136",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8136#issuecomment-71554",
    "user": "mvngu"
}
```

Thank you very much for this, John! The total number of warnings resulting from building the HTML version of the reference manual is now 151.



---

archive/issue_comments_071555.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-02T00:27:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8136",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8136#issuecomment-71555",
    "user": "mvngu"
}
```

Resolution: fixed
