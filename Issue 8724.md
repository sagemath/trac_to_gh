# Issue 8724: Notebook redirects use wrong HTTP Status Code (301 Moved Permanently)

archive/issues_008724.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  mpatel\n\nNotebook redirects use status code 301 to redirect to new pages, when they should use code 303 See Other. Because of this, Google Chrome caches the redirect, leading to problems with creating new worksheets, emptying trash, etc. If the redirect is cached, the requested action will not be performed, as the browser will redirect directly to the original url.\n\nFor example, if you are to click the \"New Worksheet\" link twice, you would expect to create two new worksheets. However, the second click redirects you directly to the first created worksheet.\n\nThanks to mpatel for spotting this.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8724\n\n",
    "created_at": "2010-04-20T12:10:30Z",
    "labels": [
        "notebook",
        "blocker",
        "bug"
    ],
    "title": "Notebook redirects use wrong HTTP Status Code (301 Moved Permanently)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8724",
    "user": "timdumol"
}
```
Assignee: jason, was

CC:  mpatel

Notebook redirects use status code 301 to redirect to new pages, when they should use code 303 See Other. Because of this, Google Chrome caches the redirect, leading to problems with creating new worksheets, emptying trash, etc. If the redirect is cached, the requested action will not be performed, as the browser will redirect directly to the original url.

For example, if you are to click the "New Worksheet" link twice, you would expect to create two new worksheets. However, the second click redirects you directly to the first created worksheet.

Thanks to mpatel for spotting this.

Issue created by migration from https://trac.sagemath.org/ticket/8724





---

archive/issue_comments_079691.json:
```json
{
    "body": "Attachment\n\nChanges status code of redirects to 303. Also fixes a bunch of Selenium tests. Apply to sagenb repo.",
    "created_at": "2010-04-20T12:12:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8724#issuecomment-79691",
    "user": "timdumol"
}
```

Attachment

Changes status code of redirects to 303. Also fixes a bunch of Selenium tests. Apply to sagenb repo.



---

archive/issue_comments_079692.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-20T12:13:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8724#issuecomment-79692",
    "user": "timdumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_079693.json:
```json
{
    "body": "(I'm not changing any notebook code in Sage 4.4.)",
    "created_at": "2010-04-23T04:39:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8724#issuecomment-79693",
    "user": "jhpalmieri"
}
```

(I'm not changing any notebook code in Sage 4.4.)



---

archive/issue_comments_079694.json:
```json
{
    "body": "This looks great!",
    "created_at": "2010-04-24T19:27:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8724#issuecomment-79694",
    "user": "was"
}
```

This looks great!



---

archive/issue_comments_079695.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-24T19:27:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8724#issuecomment-79695",
    "user": "was"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_079696.json:
```json
{
    "body": "Apply after first patch",
    "created_at": "2010-04-24T19:59:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8724#issuecomment-79696",
    "user": "acleone"
}
```

Apply after first patch



---

archive/issue_comments_079697.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-04-27T14:24:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8724#issuecomment-79697",
    "user": "jhpalmieri"
}
```

Attachment



---

archive/issue_comments_079698.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-29T04:56:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8724#issuecomment-79698",
    "user": "was"
}
```

Resolution: fixed
