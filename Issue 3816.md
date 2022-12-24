# Issue 3816: [with patch; needs review] notebook -- SyntaxWarning in twist.py

archive/issues_003816.json:
```json
{
    "body": "Assignee: boothby\n\nthis was in there forever, but for some reason it causes a warning...\n\nFrom Cremona:\n\n```\n\nI have a successful build of 3.1.alpha1.  When I make a clone, the\n*first* time I run sage (by typing ./sage in SAGE_ROOT right after the\nsage -clone) I get this message after the banner and before the first\nprompt:\n\n/home/john/sage-3.1.alpha1/local/lib/python2.5/site-packages/sage/server/notebook/twist.py:1762:\nSyntaxWarning: name 'notebook' is used prior to global declaration\n global notebook\n\nBut if I then quit and restart, the message does not recur.\n\nWhat gives?\n\nJohn\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3816\n\n",
    "created_at": "2008-08-12T13:16:44Z",
    "labels": [
        "notebook",
        "blocker",
        "bug"
    ],
    "title": "[with patch; needs review] notebook -- SyntaxWarning in twist.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3816",
    "user": "was"
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

archive/issue_comments_027148.json:
```json
{
    "body": "Attachment [sage-3816.patch](tarball://root/attachments/some-uuid/ticket3816/sage-3816.patch) by was created at 2008-08-12 13:17:10",
    "created_at": "2008-08-12T13:17:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3816#issuecomment-27148",
    "user": "was"
}
```

Attachment [sage-3816.patch](tarball://root/attachments/some-uuid/ticket3816/sage-3816.patch) by was created at 2008-08-12 13:17:10



---

archive/issue_comments_027149.json:
```json
{
    "body": "Positive review. Patch looks good to me.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-13T06:38:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3816#issuecomment-27149",
    "user": "mabshoff"
}
```

Positive review. Patch looks good to me.

Cheers,

Michael



---

archive/issue_comments_027150.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-13T06:39:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3816#issuecomment-27150",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_027151.json:
```json
{
    "body": "Merged in Sage 3.1.alpha2",
    "created_at": "2008-08-13T06:39:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3816#issuecomment-27151",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.alpha2
