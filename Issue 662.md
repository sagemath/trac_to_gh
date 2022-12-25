# Issue 662: Start Browser with clean environment

archive/issues_000662.json:
```json
{
    "body": "Assignee: @williamstein\n\nIf I call `sage -notebook` and Firefox/Iceweasel comes up automatically, it crashes on me with \n\n\n```\n/usr/lib/iceweasel/firefox-bin: symbol lookup error: /usr/lib/libxml2.so.2: undefined symbol: gzopen64\n```\n\n\nwhen logging in.\n\nIf I start Iceweasel again afterwards, I can log in and everything works. I suspect that this behaviour is caused by the SAGE environment variables (e.g. `LD_PATH`). A fix would be to start the browser with a clean (as in pre-SAGE) environment.\n\nIssue created by migration from https://trac.sagemath.org/ticket/662\n\n",
    "created_at": "2007-09-15T19:08:50Z",
    "labels": [
        "component: user interface",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.7",
    "title": "Start Browser with clean environment",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/662",
    "user": "https://github.com/malb"
}
```
Assignee: @williamstein

If I call `sage -notebook` and Firefox/Iceweasel comes up automatically, it crashes on me with 


```
/usr/lib/iceweasel/firefox-bin: symbol lookup error: /usr/lib/libxml2.so.2: undefined symbol: gzopen64
```


when logging in.

If I start Iceweasel again afterwards, I can log in and everything works. I suspect that this behaviour is caused by the SAGE environment variables (e.g. `LD_PATH`). A fix would be to start the browser with a clean (as in pre-SAGE) environment.

Issue created by migration from https://trac.sagemath.org/ticket/662





---

archive/issue_comments_003426.json:
```json
{
    "body": "Post a patch to fix this, since it will be too hard for me to debug and test myself.",
    "created_at": "2007-09-21T00:14:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/662",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/662#issuecomment-3426",
    "user": "https://github.com/williamstein"
}
```

Post a patch to fix this, since it will be too hard for me to debug and test myself.



---

archive/issue_events_001774.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-09-21T00:14:34Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/662",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/662#event-1774"
}
```



---

archive/issue_comments_003427.json:
```json
{
    "body": "Changing assignee from @williamstein to mabshoff.",
    "created_at": "2007-10-02T21:59:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/662",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/662#issuecomment-3427",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from @williamstein to mabshoff.



---

archive/issue_comments_003428.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-02T21:59:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/662",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/662#issuecomment-3428",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_003429.json:
```json
{
    "body": "a fix is attached.",
    "created_at": "2007-10-05T10:09:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/662",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/662#issuecomment-3429",
    "user": "https://github.com/malb"
}
```

a fix is attached.



---

archive/issue_comments_003430.json:
```json
{
    "body": "Changing assignee from mabshoff to @malb.",
    "created_at": "2007-10-05T10:09:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/662",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/662#issuecomment-3430",
    "user": "https://github.com/malb"
}
```

Changing assignee from mabshoff to @malb.



---

archive/issue_comments_003431.json:
```json
{
    "body": "Changing status from assigned to new.",
    "created_at": "2007-10-05T10:09:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/662",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/662#issuecomment-3431",
    "user": "https://github.com/malb"
}
```

Changing status from assigned to new.



---

archive/issue_events_001775.json:
```json
{
    "actor": "https://github.com/malb",
    "created_at": "2007-10-05T10:09:16Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/662",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/662#event-1775"
}
```



---

archive/issue_events_001776.json:
```json
{
    "actor": "https://github.com/malb",
    "created_at": "2007-10-05T10:09:16Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/662",
    "milestone": "sage-2.8.7",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/662#event-1776"
}
```



---

archive/issue_comments_003432.json:
```json
{
    "body": "Attachment [firefox-crash-bugfix.patch](tarball://root/attachments/some-uuid/ticket662/firefox-crash-bugfix.patch) by @malb created at 2007-10-05 10:09:58",
    "created_at": "2007-10-05T10:09:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/662",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/662#issuecomment-3432",
    "user": "https://github.com/malb"
}
```

Attachment [firefox-crash-bugfix.patch](tarball://root/attachments/some-uuid/ticket662/firefox-crash-bugfix.patch) by @malb created at 2007-10-05 10:09:58



---

archive/issue_events_001777.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-13T07:39:29Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/662",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/662#event-1777"
}
```



---

archive/issue_comments_003433.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-13T07:39:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/662",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/662#issuecomment-3433",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
