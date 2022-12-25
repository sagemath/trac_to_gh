# Issue 2538: Sage 2.10.4.rc0: server/notebook/interact.py is broken due to #2530

archive/issues_002538.json:
```json
{
    "body": "Assignee: wstein\n\n```\nsage-2.10.4.rc0$ ./sage -t -long devel/sage/sage/server/notebook/interact.py\nsage -t -long devel/sage-main/sage/server/notebook/interact.py\n**********************************************************************\nFile \"interact.py\", line 1641:\n    sage: selector([1,2,7], default=2).default()\nExpected:\n    2\nGot:\n    1\n**********************************************************************\n1 items had failures:\n   1 of   1 in __main__.example_70\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file .doctest_interact.py\n         [2.9 s]\nexit code: 256\n\n----------------------------------------------------------------------\nThe following tests failed:\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/2538\n\n",
    "created_at": "2008-03-16T01:24:51Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.4",
    "title": "Sage 2.10.4.rc0: server/notebook/interact.py is broken due to #2530",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2538",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: wstein

```
sage-2.10.4.rc0$ ./sage -t -long devel/sage/sage/server/notebook/interact.py
sage -t -long devel/sage-main/sage/server/notebook/interact.py
**********************************************************************
File "interact.py", line 1641:
    sage: selector([1,2,7], default=2).default()
Expected:
    2
Got:
    1
**********************************************************************
1 items had failures:
   1 of   1 in __main__.example_70
***Test Failed*** 1 failures.
For whitespace errors, see the file .doctest_interact.py
         [2.9 s]
exit code: 256

----------------------------------------------------------------------
The following tests failed:
```

Issue created by migration from https://trac.sagemath.org/ticket/2538





---

archive/issue_comments_017274.json:
```json
{
    "body": "The new output, i.e., 1 is definitely now correct.   Feel free to\nmake this change and close this ticket.",
    "created_at": "2008-03-16T02:57:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2538#issuecomment-17274",
    "user": "https://github.com/williamstein"
}
```

The new output, i.e., 1 is definitely now correct.   Feel free to
make this change and close this ticket.



---

archive/issue_comments_017275.json:
```json
{
    "body": "Attachment [trac_2538.patch](tarball://root/attachments/some-uuid/ticket2538/trac_2538.patch) by mabshoff created at 2008-03-16 05:27:35",
    "created_at": "2008-03-16T05:27:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2538#issuecomment-17275",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_2538.patch](tarball://root/attachments/some-uuid/ticket2538/trac_2538.patch) by mabshoff created at 2008-03-16 05:27:35



---

archive/issue_comments_017276.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-16T05:28:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2538#issuecomment-17276",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_017277.json:
```json
{
    "body": "Changing assignee from wstein to mabshoff.",
    "created_at": "2008-03-16T05:28:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2538#issuecomment-17277",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from wstein to mabshoff.



---

archive/issue_comments_017278.json:
```json
{
    "body": "Looks okay to me.",
    "created_at": "2008-03-16T06:07:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2538#issuecomment-17278",
    "user": "https://github.com/mwhansen"
}
```

Looks okay to me.



---

archive/issue_comments_017279.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-16T06:45:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2538#issuecomment-17279",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_017280.json:
```json
{
    "body": "Merged in Sage 2.10.4.rc0",
    "created_at": "2008-03-16T06:45:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2538#issuecomment-17280",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.4.rc0



---

archive/issue_events_005952.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-16T06:45:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2538",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2538#event-5952"
}
```
