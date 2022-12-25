# Issue 2251: sage 2.10.2.rc0: rings/number_field/number_field.py doctest failure

archive/issues_002251.json:
```json
{
    "body": "Assignee: @craigcitro\n\n```\nsage -t -long devel/sage-main/sage/rings/number_field/number_field.py\n**********************************************************************\nFile \"number_field.py\", line 2619:\n    sage: [Plist[i]==K.ideal(pilist[i]) for i in range(len(Plist))]\nExpected:\n    [True, False, False]\nGot:\n    [True, False, True]\n**********************************************************************\n1 items had failures:\n   1 of  13 in __main__.example_78\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file .doctest_number_field.py\n         [20.4 s]\nexit code: 256\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/2251\n\n",
    "created_at": "2008-02-21T19:32:46Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "sage 2.10.2.rc0: rings/number_field/number_field.py doctest failure",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2251",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @craigcitro

```
sage -t -long devel/sage-main/sage/rings/number_field/number_field.py
**********************************************************************
File "number_field.py", line 2619:
    sage: [Plist[i]==K.ideal(pilist[i]) for i in range(len(Plist))]
Expected:
    [True, False, False]
Got:
    [True, False, True]
**********************************************************************
1 items had failures:
   1 of  13 in __main__.example_78
***Test Failed*** 1 failures.
For whitespace errors, see the file .doctest_number_field.py
         [20.4 s]
exit code: 256
```

Issue created by migration from https://trac.sagemath.org/ticket/2251





---

archive/issue_comments_014881.json:
```json
{
    "body": "Attachment [trac-2252.patch](tarball://root/attachments/some-uuid/ticket2251/trac-2252.patch) by @craigcitro created at 2008-02-21 23:13:49\n\nFixes the doctest to the answer that sage was producing, which is correct. (One can check it within sage, i.e. it's easy to check that the two ideals are equal to one another, and I even double-checked in Pari to make sure we weren't missing something in moving the answer from Pari to Sage.)",
    "created_at": "2008-02-21T23:13:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2251#issuecomment-14881",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-2252.patch](tarball://root/attachments/some-uuid/ticket2251/trac-2252.patch) by @craigcitro created at 2008-02-21 23:13:49

Fixes the doctest to the answer that sage was producing, which is correct. (One can check it within sage, i.e. it's easy to check that the two ideals are equal to one another, and I even double-checked in Pari to make sure we weren't missing something in moving the answer from Pari to Sage.)



---

archive/issue_comments_014882.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-21T23:13:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2251#issuecomment-14882",
    "user": "https://github.com/craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_014883.json:
```json
{
    "body": "Note that the patch says 2252.patch, but it's really for this ticket.",
    "created_at": "2008-02-21T23:14:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2251#issuecomment-14883",
    "user": "https://github.com/craigcitro"
}
```

Note that the patch says 2252.patch, but it's really for this ticket.



---

archive/issue_comments_014884.json:
```json
{
    "body": "Merged in Sage 2.10.2.rc0",
    "created_at": "2008-02-22T00:59:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2251#issuecomment-14884",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.2.rc0



---

archive/issue_comments_014885.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-22T00:59:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2251#issuecomment-14885",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_005339.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-22T00:59:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2251",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2251#event-5339"
}
```
