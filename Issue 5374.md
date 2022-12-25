# Issue 5374: [with patch, needs review] minor problem with ReST in misc/hg.py

archive/issues_005374.json:
```json
{
    "body": "Assignee: @jhpalmieri\n\nThis fixes the one problem remaining from ticket #4919.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5374\n\n",
    "created_at": "2009-02-26T00:17:28Z",
    "labels": [
        "component: misc",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4",
    "title": "[with patch, needs review] minor problem with ReST in misc/hg.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5374",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: @jhpalmieri

This fixes the one problem remaining from ticket #4919.


Issue created by migration from https://trac.sagemath.org/ticket/5374





---

archive/issue_comments_041311.json:
```json
{
    "body": "Attachment [hg-rst.patch](tarball://root/attachments/some-uuid/ticket5374/hg-rst.patch) by @jhpalmieri created at 2009-02-26 00:17:52",
    "created_at": "2009-02-26T00:17:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5374#issuecomment-41311",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [hg-rst.patch](tarball://root/attachments/some-uuid/ticket5374/hg-rst.patch) by @jhpalmieri created at 2009-02-26 00:17:52



---

archive/issue_comments_041312.json:
```json
{
    "body": "Changing component from misc to documentation.",
    "created_at": "2009-02-26T00:37:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5374#issuecomment-41312",
    "user": "https://github.com/jhpalmieri"
}
```

Changing component from misc to documentation.



---

archive/issue_comments_041313.json:
```json
{
    "body": "REFEREE REPORT\n\n\n\nThe patch **hg-rst.patch** applied fine against 3.4.alpha0 and all doctests passed with the options\n\n```\n-t -long -optional\n```\n\nWell, one doesn't need to run doctests on `sage/misc/` since this is just a minor formatting fix, but I did so anyway just to make sure... The reference manual built OK with this command\n\n```\nsage -docbuild reference html\n```\n\nChecking the relevant file\n\n```\n/path/to/html/en/reference/sage/misc/hg.html\n```\n\nI see that the formatting of both `import_patch()` and `patch()` is consistent with each other. So positive review.",
    "created_at": "2009-02-27T09:11:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5374#issuecomment-41313",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

REFEREE REPORT



The patch **hg-rst.patch** applied fine against 3.4.alpha0 and all doctests passed with the options

```
-t -long -optional
```

Well, one doesn't need to run doctests on `sage/misc/` since this is just a minor formatting fix, but I did so anyway just to make sure... The reference manual built OK with this command

```
sage -docbuild reference html
```

Checking the relevant file

```
/path/to/html/en/reference/sage/misc/hg.html
```

I see that the formatting of both `import_patch()` and `patch()` is consistent with each other. So positive review.



---

archive/issue_comments_041314.json:
```json
{
    "body": "Merged in Sage 3.4.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-28T16:23:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5374#issuecomment-41314",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.rc0.

Cheers,

Michael



---

archive/issue_comments_041315.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-28T16:23:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5374#issuecomment-41315",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_005629.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-28T16:23:42Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5374",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5374#event-5629"
}
```
