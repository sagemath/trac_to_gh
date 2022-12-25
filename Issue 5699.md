# Issue 5699: notebook -- %r mode is completely broken (trivial to fix)

archive/issues_005699.json:
```json
{
    "body": "Assignee: boothby\n\nIn the notebook\n\n\n```\n%r\n2+5\n///\nTraceback (most recent call last):\n...\nTypeError: eval() got multiple values for keyword argument 'synchronize'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5699\n\n",
    "created_at": "2009-04-06T19:28:16Z",
    "labels": [
        "component: notebook",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "notebook -- %r mode is completely broken (trivial to fix)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5699",
    "user": "https://github.com/williamstein"
}
```
Assignee: boothby

In the notebook


```
%r
2+5
///
Traceback (most recent call last):
...
TypeError: eval() got multiple values for keyword argument 'synchronize'
```


Issue created by migration from https://trac.sagemath.org/ticket/5699





---

archive/issue_comments_044462.json:
```json
{
    "body": "Attachment [trac_5699.patch](tarball://root/attachments/some-uuid/ticket5699/trac_5699.patch) by @williamstein created at 2009-04-07 18:59:12",
    "created_at": "2009-04-07T18:59:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5699#issuecomment-44462",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_5699.patch](tarball://root/attachments/some-uuid/ticket5699/trac_5699.patch) by @williamstein created at 2009-04-07 18:59:12



---

archive/issue_comments_044463.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-04-10T22:14:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5699#issuecomment-44463",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_044464.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-11T00:00:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5699#issuecomment-44464",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_044465.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc2.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-11T00:00:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5699#issuecomment-44465",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.1.rc2.

Cheers,

Michael
