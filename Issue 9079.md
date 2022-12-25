# Issue 9079: fix bug in singular polynomial interface

archive/issues_009079.json:
```json
{
    "body": "Assignee: @malb\n\n\n```\nsage: PolynomialRing(QQ,'u_ba')._singular_init_()\n...\nRuntimeError: Singular error:\n   ? error occurred in STDIN line 33: `if(defined(_b)>0){kill _b;};`\n   ? last reserved name was `defined`\n   skipping text from `)`\n```\n\n\nThis is because the function _singular_init_ incorrectly defines _vars.  The attached patch fixes this. \n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9079\n\n",
    "created_at": "2010-05-29T00:47:18Z",
    "labels": [
        "component: commutative algebra",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.3",
    "title": "fix bug in singular polynomial interface",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9079",
    "user": "https://github.com/williamstein"
}
```
Assignee: @malb


```
sage: PolynomialRing(QQ,'u_ba')._singular_init_()
...
RuntimeError: Singular error:
   ? error occurred in STDIN line 33: `if(defined(_b)>0){kill _b;};`
   ? last reserved name was `defined`
   skipping text from `)`
```


This is because the function _singular_init_ incorrectly defines _vars.  The attached patch fixes this. 


Issue created by migration from https://trac.sagemath.org/ticket/9079





---

archive/issue_comments_084148.json:
```json
{
    "body": "Attachment [trac_9079.patch](tarball://root/attachments/some-uuid/ticket9079/trac_9079.patch) by @williamstein created at 2010-05-29 00:55:50",
    "created_at": "2010-05-29T00:55:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9079#issuecomment-84148",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_9079.patch](tarball://root/attachments/some-uuid/ticket9079/trac_9079.patch) by @williamstein created at 2010-05-29 00:55:50



---

archive/issue_comments_084149.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-29T00:56:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9079#issuecomment-84149",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_084150.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-29T11:55:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9079#issuecomment-84150",
    "user": "https://github.com/malb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084151.json:
```json
{
    "body": "patch looks good.",
    "created_at": "2010-05-29T11:55:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9079#issuecomment-84151",
    "user": "https://github.com/malb"
}
```

patch looks good.



---

archive/issue_comments_084152.json:
```json
{
    "body": "Replying to [comment:2 malb]:\n> patch looks good.\n\nSorry, I was a bit too late. But I agree that it looks good.",
    "created_at": "2010-05-31T08:13:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9079#issuecomment-84152",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:2 malb]:
> patch looks good.

Sorry, I was a bit too late. But I agree that it looks good.



---

archive/issue_comments_084153.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-03T04:27:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9079#issuecomment-84153",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
