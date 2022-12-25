# Issue 2503: Sage 2.10.4.alpha4: doctest failout in sage/misc/functional.py from #2421

archive/issues_002503.json:
```json
{
    "body": "Assignee: failure\n\nThe following doctest failure in sage/misc/functional.py happends due to #2421:\n\n```\nsage -t -long devel/sage-main/sage/misc/functional.py\n**********************************************************************\nFile \"functional.py\", line 848:\n    sage: round(b)\nExpected:\n    5.0000000000000000\nGot:\n    5\n**********************************************************************\n1 items had failures:\n   1 of   5 in __main__.example_52\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file .doctest_functional.py\n         [5.0 s]\nexit code: 256\n\n----------------------------------------------------------------------\n```\n\nThe fix is obvious - patch coming up.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/2503\n\n",
    "created_at": "2008-03-12T21:19:49Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.4",
    "title": "Sage 2.10.4.alpha4: doctest failout in sage/misc/functional.py from #2421",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2503",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: failure

The following doctest failure in sage/misc/functional.py happends due to #2421:

```
sage -t -long devel/sage-main/sage/misc/functional.py
**********************************************************************
File "functional.py", line 848:
    sage: round(b)
Expected:
    5.0000000000000000
Got:
    5
**********************************************************************
1 items had failures:
   1 of   5 in __main__.example_52
***Test Failed*** 1 failures.
For whitespace errors, see the file .doctest_functional.py
         [5.0 s]
exit code: 256

----------------------------------------------------------------------
```

The fix is obvious - patch coming up.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/2503





---

archive/issue_comments_016923.json:
```json
{
    "body": "Attachment [trac_2503.patch](tarball://root/attachments/some-uuid/ticket2503/trac_2503.patch) by mabshoff created at 2008-03-12 21:23:00",
    "created_at": "2008-03-12T21:23:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2503#issuecomment-16923",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_2503.patch](tarball://root/attachments/some-uuid/ticket2503/trac_2503.patch) by mabshoff created at 2008-03-12 21:23:00



---

archive/issue_comments_016924.json:
```json
{
    "body": "Works for me.",
    "created_at": "2008-03-13T02:54:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2503#issuecomment-16924",
    "user": "https://github.com/mwhansen"
}
```

Works for me.



---

archive/issue_comments_016925.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-13T06:01:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2503#issuecomment-16925",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_016926.json:
```json
{
    "body": "Merged in Sage 2.10.4.alpha0",
    "created_at": "2008-03-13T06:01:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2503#issuecomment-16926",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.4.alpha0



---

archive/issue_events_005885.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-13T06:01:46Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2503",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2503#event-5885"
}
```
