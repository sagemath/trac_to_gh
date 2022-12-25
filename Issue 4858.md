# Issue 4858: parenthesis badly handled in notebook sheet titles

archive/issues_004858.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  phil-sage@teuwen.org\n\n[from notebook bug reporter](http://spreadsheets.google.com/ver?key=pCwvGVwSMxTzT6E2xNdo5fA&t=1230037542957000&pt=1230037522957000&diffWidget=true&s=AJVazbXknPq-Bx-rR5kIauR1GyZU7hV7yg)\n\n\n```\nHi,\n\nI had some notebook sheets with parenthesis in the title with Sage v3.1.1\nBut since I upgraded to 3.2.1 the parenthesis are escaped, even multiple times, every time the sheet is opened again.\nTo reproduce the problem:\nCreate new sheet \"Untitled\"\nRename it as \"Untitled (test)\"\nClose it, it appears properly in the list\nOpen it again -> \"Untitled &amp;#40;test&amp;#41;\"\nSo the bug was introduced somewhere between 3.1.1 and 3.2.1\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4858\n\n",
    "created_at": "2008-12-23T13:16:47Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "parenthesis badly handled in notebook sheet titles",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4858",
    "user": "https://github.com/haraldschilly"
}
```
Assignee: boothby

CC:  phil-sage@teuwen.org

[from notebook bug reporter](http://spreadsheets.google.com/ver?key=pCwvGVwSMxTzT6E2xNdo5fA&t=1230037542957000&pt=1230037522957000&diffWidget=true&s=AJVazbXknPq-Bx-rR5kIauR1GyZU7hV7yg)


```
Hi,

I had some notebook sheets with parenthesis in the title with Sage v3.1.1
But since I upgraded to 3.2.1 the parenthesis are escaped, even multiple times, every time the sheet is opened again.
To reproduce the problem:
Create new sheet "Untitled"
Rename it as "Untitled (test)"
Close it, it appears properly in the list
Open it again -> "Untitled &amp;#40;test&amp;#41;"
So the bug was introduced somewhere between 3.1.1 and 3.2.1
```


Issue created by migration from https://trac.sagemath.org/ticket/4858





---

archive/issue_comments_036752.json:
```json
{
    "body": "Harald,\n\nthis looks like a dupe of #4851, so I would suggest we close this.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-23T13:31:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4858#issuecomment-36752",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Harald,

this looks like a dupe of #4851, so I would suggest we close this.

Cheers,

Michael



---

archive/issue_comments_036753.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-01-19T08:06:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4858#issuecomment-36753",
    "user": "https://github.com/mwhansen"
}
```

Resolution: duplicate



---

archive/issue_events_011171.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-01-19T08:06:17Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4858",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4858#event-11171"
}
```



---

archive/issue_comments_036754.json:
```json
{
    "body": "Yep, I'll mark this as a duplicate.  There is a fix at #4851.",
    "created_at": "2009-01-19T08:06:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4858#issuecomment-36754",
    "user": "https://github.com/mwhansen"
}
```

Yep, I'll mark this as a duplicate.  There is a fix at #4851.



---

archive/issue_events_011172.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-01-19T08:06:17Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4858",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4858#event-11172"
}
```
