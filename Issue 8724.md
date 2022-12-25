# Issue 8724: Notebook redirects use wrong HTTP Status Code (301 Moved Permanently)

archive/issues_008724.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  @qed777\n\nNotebook redirects use status code 301 to redirect to new pages, when they should use code 303 See Other. Because of this, Google Chrome caches the redirect, leading to problems with creating new worksheets, emptying trash, etc. If the redirect is cached, the requested action will not be performed, as the browser will redirect directly to the original url.\n\nFor example, if you are to click the \"New Worksheet\" link twice, you would expect to create two new worksheets. However, the second click redirects you directly to the first created worksheet.\n\nThanks to mpatel for spotting this.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8724\n\n",
    "created_at": "2010-04-20T12:10:30Z",
    "labels": [
        "component: notebook",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.1",
    "title": "Notebook redirects use wrong HTTP Status Code (301 Moved Permanently)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8724",
    "user": "https://github.com/TimDumol"
}
```
Assignee: jason, was

CC:  @qed777

Notebook redirects use status code 301 to redirect to new pages, when they should use code 303 See Other. Because of this, Google Chrome caches the redirect, leading to problems with creating new worksheets, emptying trash, etc. If the redirect is cached, the requested action will not be performed, as the browser will redirect directly to the original url.

For example, if you are to click the "New Worksheet" link twice, you would expect to create two new worksheets. However, the second click redirects you directly to the first created worksheet.

Thanks to mpatel for spotting this.

Issue created by migration from https://trac.sagemath.org/ticket/8724





---

archive/issue_comments_079561.json:
```json
{
    "body": "Attachment [trac_8724-sagenb-redirect-code.patch](tarball://root/attachments/some-uuid/ticket8724/trac_8724-sagenb-redirect-code.patch) by @TimDumol created at 2010-04-20 12:12:41\n\nChanges status code of redirects to 303. Also fixes a bunch of Selenium tests. Apply to sagenb repo.",
    "created_at": "2010-04-20T12:12:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8724#issuecomment-79561",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_8724-sagenb-redirect-code.patch](tarball://root/attachments/some-uuid/ticket8724/trac_8724-sagenb-redirect-code.patch) by @TimDumol created at 2010-04-20 12:12:41

Changes status code of redirects to 303. Also fixes a bunch of Selenium tests. Apply to sagenb repo.



---

archive/issue_comments_079562.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-20T12:13:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8724#issuecomment-79562",
    "user": "https://github.com/TimDumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_079563.json:
```json
{
    "body": "(I'm not changing any notebook code in Sage 4.4.)",
    "created_at": "2010-04-23T04:39:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8724#issuecomment-79563",
    "user": "https://github.com/jhpalmieri"
}
```

(I'm not changing any notebook code in Sage 4.4.)



---

archive/issue_comments_079564.json:
```json
{
    "body": "This looks great!",
    "created_at": "2010-04-24T19:27:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8724#issuecomment-79564",
    "user": "https://github.com/williamstein"
}
```

This looks great!



---

archive/issue_comments_079565.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-24T19:27:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8724#issuecomment-79565",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_079566.json:
```json
{
    "body": "Apply after first patch",
    "created_at": "2010-04-24T19:59:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8724#issuecomment-79566",
    "user": "https://trac.sagemath.org/admin/accounts/users/acleone"
}
```

Apply after first patch



---

archive/issue_comments_079567.json:
```json
{
    "body": "Attachment [trac_8724-doctest-fix.patch](tarball://root/attachments/some-uuid/ticket8724/trac_8724-doctest-fix.patch) by @jhpalmieri created at 2010-04-27 14:24:18",
    "created_at": "2010-04-27T14:24:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8724#issuecomment-79567",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_8724-doctest-fix.patch](tarball://root/attachments/some-uuid/ticket8724/trac_8724-doctest-fix.patch) by @jhpalmieri created at 2010-04-27 14:24:18



---

archive/issue_comments_079568.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-29T04:56:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8724#issuecomment-79568",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_008894.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2010-04-29T04:56:39Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8724",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8724#event-8894"
}
```
