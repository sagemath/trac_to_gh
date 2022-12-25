# Issue 6902: log(x) is typeset as \ln x

archive/issues_006902.json:
```json
{
    "body": "\n```\nsage: log(x)\nlog(x)\nsage: latex(log(x))\n\\ln\\left(x\\right)\n```\n\n\nWe should switch back to `\\log`. See this thread:\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/dc6530a2071bd6db\n\nIssue created by migration from https://trac.sagemath.org/ticket/6902\n\n",
    "created_at": "2009-09-07T19:05:26Z",
    "labels": [
        "component: symbolics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "log(x) is typeset as \\ln x",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6902",
    "user": "https://github.com/burcin"
}
```

```
sage: log(x)
log(x)
sage: latex(log(x))
\ln\left(x\right)
```


We should switch back to `\log`. See this thread:

http://groups.google.com/group/sage-devel/browse_thread/thread/dc6530a2071bd6db

Issue created by migration from https://trac.sagemath.org/ticket/6902





---

archive/issue_comments_056907.json:
```json
{
    "body": "Set assignee to @burcin.",
    "created_at": "2009-09-19T15:11:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6902#issuecomment-56907",
    "user": "https://github.com/burcin"
}
```

Set assignee to @burcin.



---

archive/issue_comments_056908.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-09-19T15:11:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6902#issuecomment-56908",
    "user": "https://github.com/burcin"
}
```

Changing status from new to assigned.



---

archive/issue_comments_056909.json:
```json
{
    "body": "Attachment [trac_6902-log_latex.patch](tarball://root/attachments/some-uuid/ticket6902/trac_6902-log_latex.patch) by @burcin created at 2009-09-19 15:11:41\n\nThis is fixed in my pynac tree. Doctest for Sage is in attachment:trac_6902-log_latex.patch.\n\nI will post a new pynac spkg and review instructions soon.",
    "created_at": "2009-09-19T15:11:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6902#issuecomment-56909",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_6902-log_latex.patch](tarball://root/attachments/some-uuid/ticket6902/trac_6902-log_latex.patch) by @burcin created at 2009-09-19 15:11:41

This is fixed in my pynac tree. Doctest for Sage is in attachment:trac_6902-log_latex.patch.

I will post a new pynac spkg and review instructions soon.



---

archive/issue_comments_056910.json:
```json
{
    "body": "New pynac package available at #6993.",
    "created_at": "2009-09-22T19:28:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6902#issuecomment-56910",
    "user": "https://github.com/burcin"
}
```

New pynac package available at #6993.



---

archive/issue_comments_056911.json:
```json
{
    "body": "This works.  Pending of course review of new Pynac as a whole.",
    "created_at": "2009-09-23T02:35:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6902#issuecomment-56911",
    "user": "https://github.com/kcrisman"
}
```

This works.  Pending of course review of new Pynac as a whole.



---

archive/issue_comments_056912.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-25T22:44:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6902#issuecomment-56912",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_056913.json:
```json
{
    "body": "There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.",
    "created_at": "2009-09-27T10:39:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6902#issuecomment-56913",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
