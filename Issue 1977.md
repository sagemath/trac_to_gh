# Issue 1977: valgrind 3.3.0 no longer appends $PID per default to the logs

archive/issues_001977.json:
```json
{
    "body": "Assignee: mabshoff\n\nI read something about this in the release notes, but the `--help` section of the valgrind command seems to be missing any clue how to reenable it.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1977\n\n",
    "created_at": "2008-01-30T04:30:52Z",
    "labels": [
        "component: memleak",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "valgrind 3.3.0 no longer appends $PID per default to the logs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1977",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

I read something about this in the release notes, but the `--help` section of the valgrind command seems to be missing any clue how to reenable it.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1977





---

archive/issue_comments_012785.json:
```json
{
    "body": "For valgrind 3.3.0 we need to append `%p` to all the logfile names.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-02T05:03:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1977#issuecomment-12785",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

For valgrind 3.3.0 we need to append `%p` to all the logfile names.

Cheers,

Michael



---

archive/issue_comments_012786.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-02T05:03:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1977#issuecomment-12786",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_012787.json:
```json
{
    "body": "Attachment [Sage-2.10.1.rc5-fix-valgrind-log-pids_trac_1977.patch](tarball://root/attachments/some-uuid/ticket1977/Sage-2.10.1.rc5-fix-valgrind-log-pids_trac_1977.patch) by @williamstein created at 2008-02-02 06:29:51\n\nLooks good to me.",
    "created_at": "2008-02-02T06:29:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1977#issuecomment-12787",
    "user": "https://github.com/williamstein"
}
```

Attachment [Sage-2.10.1.rc5-fix-valgrind-log-pids_trac_1977.patch](tarball://root/attachments/some-uuid/ticket1977/Sage-2.10.1.rc5-fix-valgrind-log-pids_trac_1977.patch) by @williamstein created at 2008-02-02 06:29:51

Looks good to me.



---

archive/issue_comments_012788.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-02T06:31:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1977#issuecomment-12788",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_012789.json:
```json
{
    "body": "Merged in Sage 2.10.1.rc5",
    "created_at": "2008-02-02T06:31:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1977#issuecomment-12789",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.1.rc5
