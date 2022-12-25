# Issue 4067: [with patch, needs review] hmm.pyx and ghmm.pyx valgrind issues

archive/issues_004067.json:
```json
{
    "body": "Assignee: mabshoff\n\nThis is a broken out patch from #3984. It does not fix the doctest, but numerous issues valgrind picks up. Someone needs to remember that C strings are NULL terminated :)\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4067\n\n",
    "created_at": "2008-09-05T10:10:37Z",
    "labels": [
        "component: memleak",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "[with patch, needs review] hmm.pyx and ghmm.pyx valgrind issues",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4067",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

This is a broken out patch from #3984. It does not fix the doctest, but numerous issues valgrind picks up. Someone needs to remember that C strings are NULL terminated :)

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4067





---

archive/issue_comments_029292.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-05T10:10:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4067",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4067#issuecomment-29292",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_029293.json:
```json
{
    "body": "Attachment [trac_4067.patch](tarball://root/attachments/some-uuid/ticket4067/trac_4067.patch) by @malb created at 2008-09-05 10:38:02\n\nPatch looks good, I only read it though.",
    "created_at": "2008-09-05T10:38:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4067",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4067#issuecomment-29293",
    "user": "https://github.com/malb"
}
```

Attachment [trac_4067.patch](tarball://root/attachments/some-uuid/ticket4067/trac_4067.patch) by @malb created at 2008-09-05 10:38:02

Patch looks good, I only read it though.



---

archive/issue_events_009285.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-05T11:05:13Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4067",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4067#event-9285"
}
```



---

archive/issue_comments_029294.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc0",
    "created_at": "2008-09-05T11:05:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4067",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4067#issuecomment-29294",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.2.rc0



---

archive/issue_comments_029295.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-05T11:05:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4067",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4067#issuecomment-29295",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
