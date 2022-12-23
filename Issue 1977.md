# Issue 1977: valgrind 3.3.0 no longer appends $PID per default to the logs

archive/issues_001977.json:
```json
{
    "body": "Assignee: mabshoff\n\nI read something about this in the release notes, but the `--help` section of the valgrind command seems to be missing any clue how to reenable it.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1977\n\n",
    "created_at": "2008-01-30T04:30:52Z",
    "labels": [
        "memleak",
        "major",
        "bug"
    ],
    "title": "valgrind 3.3.0 no longer appends $PID per default to the logs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1977",
    "user": "mabshoff"
}
```
Assignee: mabshoff

I read something about this in the release notes, but the `--help` section of the valgrind command seems to be missing any clue how to reenable it.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1977





---

archive/issue_comments_012816.json:
```json
{
    "body": "For valgrind 3.3.0 we need to append `%p` to all the logfile names.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-02T05:03:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1977#issuecomment-12816",
    "user": "mabshoff"
}
```

For valgrind 3.3.0 we need to append `%p` to all the logfile names.

Cheers,

Michael



---

archive/issue_comments_012817.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-02T05:03:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1977#issuecomment-12817",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_012818.json:
```json
{
    "body": "Attachment\n\nLooks good to me.",
    "created_at": "2008-02-02T06:29:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1977#issuecomment-12818",
    "user": "was"
}
```

Attachment

Looks good to me.



---

archive/issue_comments_012819.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-02T06:31:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1977#issuecomment-12819",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_012820.json:
```json
{
    "body": "Merged in Sage 2.10.1.rc5",
    "created_at": "2008-02-02T06:31:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1977#issuecomment-12820",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.1.rc5
