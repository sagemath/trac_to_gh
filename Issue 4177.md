# Issue 4177: Put Sage version in Notebook

archive/issues_004177.json:
```json
{
    "body": "Assignee: boothby\n\nUnder the \"Sage notebook\" on the upper left in the home page as well as in the individual worksheets, it might be nice to have the Sage version number of that installation in a small font, to remember - as well as to enhance bug reports coming from non-installing users.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4177\n\n",
    "created_at": "2008-09-23T18:18:17Z",
    "labels": [
        "component: notebook",
        "trivial"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "Put Sage version in Notebook",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4177",
    "user": "https://github.com/kcrisman"
}
```
Assignee: boothby

Under the "Sage notebook" on the upper left in the home page as well as in the individual worksheets, it might be nice to have the Sage version number of that installation in a small font, to remember - as well as to enhance bug reports coming from non-installing users.

Issue created by migration from https://trac.sagemath.org/ticket/4177





---

archive/issue_comments_030250.json:
```json
{
    "body": "Attachment [nb-version-number.patch](tarball://root/attachments/some-uuid/ticket4177/nb-version-number.patch) by @kcrisman created at 2008-10-17 19:03:18",
    "created_at": "2008-10-17T19:03:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4177#issuecomment-30250",
    "user": "https://github.com/kcrisman"
}
```

Attachment [nb-version-number.patch](tarball://root/attachments/some-uuid/ticket4177/nb-version-number.patch) by @kcrisman created at 2008-10-17 19:03:18



---

archive/issue_comments_030251.json:
```json
{
    "body": "Since the word \"Notebook\" appears in slightly different height in Safari vs. Firefox, the placement looks better in Safari; even with that and using the smallest font size HTML supports it looks ok.",
    "created_at": "2008-10-17T19:05:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4177#issuecomment-30251",
    "user": "https://github.com/kcrisman"
}
```

Since the word "Notebook" appears in slightly different height in Safari vs. Firefox, the placement looks better in Safari; even with that and using the smallest font size HTML supports it looks ok.



---

archive/issue_comments_030252.json:
```json
{
    "body": "Looks good to me, both the code and the appearance in Firefox on linux. One style question: is it any better to put the line\n\n```\nfrom   sage.version        import version\n```\n\nin the code for `html_banner` instead of at the top of the file? I'm a Python novice, so I have no idea which way is better.\n\nI'll give it a positive review regardless of the location of the `import` statement.",
    "created_at": "2008-10-17T20:56:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4177#issuecomment-30252",
    "user": "https://github.com/jhpalmieri"
}
```

Looks good to me, both the code and the appearance in Firefox on linux. One style question: is it any better to put the line

```
from   sage.version        import version
```

in the code for `html_banner` instead of at the top of the file? I'm a Python novice, so I have no idea which way is better.

I'll give it a positive review regardless of the location of the `import` statement.



---

archive/issue_comments_030253.json:
```json
{
    "body": "This patch breaks the twist.py doctest:\n\n```\nsage -t -long devel/sage/sage/server/notebook/twist.py      \n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.alpha0/tmp/twist.py\", line 1505:\n    sage: E.render(None)\nExpected:\n    <twisted.web2.http.Response code=200, streamlen=603>\nGot:\n    <twisted.web2.http.Response code=200, streamlen=701>\n**********************************************************************\n```\n\nThe fix is trivial, so I will post a reviewer patch in a second.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-18T19:05:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4177#issuecomment-30253",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This patch breaks the twist.py doctest:

```
sage -t -long devel/sage/sage/server/notebook/twist.py      
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.alpha0/tmp/twist.py", line 1505:
    sage: E.render(None)
Expected:
    <twisted.web2.http.Response code=200, streamlen=603>
Got:
    <twisted.web2.http.Response code=200, streamlen=701>
**********************************************************************
```

The fix is trivial, so I will post a reviewer patch in a second.

Cheers,

Michael



---

archive/issue_comments_030254.json:
```json
{
    "body": "Attachment [trac_4177_reviewer.patch](tarball://root/attachments/some-uuid/ticket4177/trac_4177_reviewer.patch) by mabshoff created at 2008-10-18 19:11:33\n\nThe reviewer patch \"...\" the length since it will otherwise break from version to version.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-18T19:11:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4177#issuecomment-30254",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_4177_reviewer.patch](tarball://root/attachments/some-uuid/ticket4177/trac_4177_reviewer.patch) by mabshoff created at 2008-10-18 19:11:33

The reviewer patch "..." the length since it will otherwise break from version to version.

Cheers,

Michael



---

archive/issue_comments_030255.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-18T19:13:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4177#issuecomment-30255",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004414.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-10-18T19:13:59Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4177",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4177#event-4414"
}
```



---

archive/issue_comments_030256.json:
```json
{
    "body": "Merged in Sage 3.2.alpha0",
    "created_at": "2008-10-18T19:13:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4177#issuecomment-30256",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.alpha0
