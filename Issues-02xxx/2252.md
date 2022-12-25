# Issue 2252: [with patch, positive review] sage 2.10.2.rc0: rings/number_field/number_field_ideal.py failure

archive/issues_002252.json:
```json
{
    "body": "Assignee: @craigcitro\n\n```\nsage -t -long devel/sage-main/sage/rings/number_field/number_field_ideal.py\n**********************************************************************\nFile \"number_field_ideal.py\", line 868:\n    sage: I.prime_factors()\nExpected:\n    [Fractional ideal (w)]\nGot:\n    [Fractional ideal (-w)]\n**********************************************************************\n1 items had failures:\n   1 of   3 in __main__.example_32\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file .doctest_number_field_ideal.py\n         [6.6 s]\nexit code: 256\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/2252\n\n",
    "closed_at": "2008-02-22T00:26:16Z",
    "created_at": "2008-02-21T19:33:49Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "[with patch, positive review] sage 2.10.2.rc0: rings/number_field/number_field_ideal.py failure",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2252",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @craigcitro

```
sage -t -long devel/sage-main/sage/rings/number_field/number_field_ideal.py
**********************************************************************
File "number_field_ideal.py", line 868:
    sage: I.prime_factors()
Expected:
    [Fractional ideal (w)]
Got:
    [Fractional ideal (-w)]
**********************************************************************
1 items had failures:
   1 of   3 in __main__.example_32
***Test Failed*** 1 failures.
For whitespace errors, see the file .doctest_number_field_ideal.py
         [6.6 s]
exit code: 256
```

Issue created by migration from https://trac.sagemath.org/ticket/2252





---

archive/issue_comments_014886.json:
```json
{
    "body": "Attachment [trac-2252.patch](tarball://root/attachments/some-uuid/ticket2252/trac-2252.patch) by @craigcitro created at 2008-02-21 23:57:57",
    "created_at": "2008-02-21T23:57:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2252#issuecomment-14886",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-2252.patch](tarball://root/attachments/some-uuid/ticket2252/trac-2252.patch) by @craigcitro created at 2008-02-21 23:57:57



---

archive/issue_comments_014887.json:
```json
{
    "body": "The answer is still mathematically correct, and it's what sage is producing, so there's nothing \"wrong\" with it. However, there's something slightly unsavory (for me) about this -- tracing through the code, Pari doesn't seem to be producing the minus sign. I'm not sure where it's coming from.",
    "created_at": "2008-02-22T00:05:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2252#issuecomment-14887",
    "user": "https://github.com/craigcitro"
}
```

The answer is still mathematically correct, and it's what sage is producing, so there's nothing "wrong" with it. However, there's something slightly unsavory (for me) about this -- tracing through the code, Pari doesn't seem to be producing the minus sign. I'm not sure where it's coming from.



---

archive/issue_comments_014888.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-22T00:05:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2252#issuecomment-14888",
    "user": "https://github.com/craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_014889.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-22T00:26:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2252#issuecomment-14889",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_005340.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-22T00:26:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2252",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2252#event-5340"
}
```



---

archive/issue_comments_014890.json:
```json
{
    "body": "Merged in Sage 2.10.2.rc0",
    "created_at": "2008-02-22T00:26:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2252#issuecomment-14890",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.2.rc0
