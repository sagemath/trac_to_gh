# Issue 3816: [with patch; needs review] notebook -- SyntaxWarning in twist.py

archive/issues_003816.json:
```json
{
    "body": "Assignee: boothby\n\nthis was in there forever, but for some reason it causes a warning...\n\nFrom Cremona:\n\n```\n\nI have a successful build of 3.1.alpha1.  When I make a clone, the\n*first* time I run sage (by typing ./sage in SAGE_ROOT right after the\nsage -clone) I get this message after the banner and before the first\nprompt:\n\n/home/john/sage-3.1.alpha1/local/lib/python2.5/site-packages/sage/server/notebook/twist.py:1762:\nSyntaxWarning: name 'notebook' is used prior to global declaration\n global notebook\n\nBut if I then quit and restart, the message does not recur.\n\nWhat gives?\n\nJohn\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3816\n\n",
    "created_at": "2008-08-12T13:16:44Z",
    "labels": [
        "component: notebook",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1",
    "title": "[with patch; needs review] notebook -- SyntaxWarning in twist.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3816",
    "user": "https://github.com/williamstein"
}
```
Assignee: boothby

this was in there forever, but for some reason it causes a warning...

From Cremona:

```

I have a successful build of 3.1.alpha1.  When I make a clone, the
*first* time I run sage (by typing ./sage in SAGE_ROOT right after the
sage -clone) I get this message after the banner and before the first
prompt:

/home/john/sage-3.1.alpha1/local/lib/python2.5/site-packages/sage/server/notebook/twist.py:1762:
SyntaxWarning: name 'notebook' is used prior to global declaration
 global notebook

But if I then quit and restart, the message does not recur.

What gives?

John

```


Issue created by migration from https://trac.sagemath.org/ticket/3816





---

archive/issue_comments_027090.json:
```json
{
    "body": "Attachment [sage-3816.patch](tarball://root/attachments/some-uuid/ticket3816/sage-3816.patch) by @williamstein created at 2008-08-12 13:17:10",
    "created_at": "2008-08-12T13:17:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3816#issuecomment-27090",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-3816.patch](tarball://root/attachments/some-uuid/ticket3816/sage-3816.patch) by @williamstein created at 2008-08-12 13:17:10



---

archive/issue_comments_027091.json:
```json
{
    "body": "Positive review. Patch looks good to me.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-13T06:38:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3816#issuecomment-27091",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review. Patch looks good to me.

Cheers,

Michael



---

archive/issue_comments_027092.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-13T06:39:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3816#issuecomment-27092",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_027093.json:
```json
{
    "body": "Merged in Sage 3.1.alpha2",
    "created_at": "2008-08-13T06:39:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3816#issuecomment-27093",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.alpha2
