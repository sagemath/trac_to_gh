# Issue 662: Start Browser with clean environment

archive/issues_000662.json:
```json
{
    "body": "Assignee: was\n\nIf I call `sage -notebook` and Firefox/Iceweasel comes up automatically, it crashes on me with \n\n\n```\n/usr/lib/iceweasel/firefox-bin: symbol lookup error: /usr/lib/libxml2.so.2: undefined symbol: gzopen64\n```\n\n\nwhen logging in.\n\nIf I start Iceweasel again afterwards, I can log in and everything works. I suspect that this behaviour is caused by the SAGE environment variables (e.g. `LD_PATH`). A fix would be to start the browser with a clean (as in pre-SAGE) environment.\n\nIssue created by migration from https://trac.sagemath.org/ticket/662\n\n",
    "created_at": "2007-09-15T19:08:50Z",
    "labels": [
        "user interface",
        "major",
        "bug"
    ],
    "title": "Start Browser with clean environment",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/662",
    "user": "malb"
}
```
Assignee: was

If I call `sage -notebook` and Firefox/Iceweasel comes up automatically, it crashes on me with 


```
/usr/lib/iceweasel/firefox-bin: symbol lookup error: /usr/lib/libxml2.so.2: undefined symbol: gzopen64
```


when logging in.

If I start Iceweasel again afterwards, I can log in and everything works. I suspect that this behaviour is caused by the SAGE environment variables (e.g. `LD_PATH`). A fix would be to start the browser with a clean (as in pre-SAGE) environment.

Issue created by migration from https://trac.sagemath.org/ticket/662





---

archive/issue_comments_003439.json:
```json
{
    "body": "Post a patch to fix this, since it will be too hard for me to debug and test myself.",
    "created_at": "2007-09-21T00:14:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/662",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/662#issuecomment-3439",
    "user": "was"
}
```

Post a patch to fix this, since it will be too hard for me to debug and test myself.



---

archive/issue_comments_003440.json:
```json
{
    "body": "Changing assignee from was to mabshoff.",
    "created_at": "2007-10-02T21:59:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/662",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/662#issuecomment-3440",
    "user": "mabshoff"
}
```

Changing assignee from was to mabshoff.



---

archive/issue_comments_003441.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-02T21:59:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/662",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/662#issuecomment-3441",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_003442.json:
```json
{
    "body": "a fix is attached.",
    "created_at": "2007-10-05T10:09:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/662",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/662#issuecomment-3442",
    "user": "malb"
}
```

a fix is attached.



---

archive/issue_comments_003443.json:
```json
{
    "body": "Changing assignee from mabshoff to malb.",
    "created_at": "2007-10-05T10:09:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/662",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/662#issuecomment-3443",
    "user": "malb"
}
```

Changing assignee from mabshoff to malb.



---

archive/issue_comments_003444.json:
```json
{
    "body": "Changing status from assigned to new.",
    "created_at": "2007-10-05T10:09:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/662",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/662#issuecomment-3444",
    "user": "malb"
}
```

Changing status from assigned to new.



---

archive/issue_comments_003445.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-10-05T10:09:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/662",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/662#issuecomment-3445",
    "user": "malb"
}
```

Attachment



---

archive/issue_comments_003446.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-13T07:39:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/662",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/662#issuecomment-3446",
    "user": "was"
}
```

Resolution: fixed
