# Issue 3583: randomness in some worksheet doctests

archive/issues_003583.json:
```json
{
    "body": "Assignee: failure\n\nOn Debian 64-bit vmware:\n\n\n```\nFile \"/home/was/build/sage-3.0.4.alpha2/tmp/worksheet.py\", line 2677:\n    sage: W.interrupt()\nExpected:\n    True\nGot:\n    False\n**********************************************************************\nFile \"/home/was/build/sage-3.0.4.alpha2/tmp/worksheet.py\", line 2681:\n    sage: W.check_comp()\nExpected:\n    ('e', None)\nGot:\n    ('w', Cell 0; in=factor(2^997-1), out=)\n**********************************************************************\n1 items had failures:\n   2 of  10 in __main__.example_85\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file /home/was/build/sage-3.0.4.alpha2/tmp/.doctest_worksheet.py\n```\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3583\n\n",
    "created_at": "2008-07-07T15:19:22Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "randomness in some worksheet doctests",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3583",
    "user": "https://github.com/williamstein"
}
```
Assignee: failure

On Debian 64-bit vmware:


```
File "/home/was/build/sage-3.0.4.alpha2/tmp/worksheet.py", line 2677:
    sage: W.interrupt()
Expected:
    True
Got:
    False
**********************************************************************
File "/home/was/build/sage-3.0.4.alpha2/tmp/worksheet.py", line 2681:
    sage: W.check_comp()
Expected:
    ('e', None)
Got:
    ('w', Cell 0; in=factor(2^997-1), out=)
**********************************************************************
1 items had failures:
   2 of  10 in __main__.example_85
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/was/build/sage-3.0.4.alpha2/tmp/.doctest_worksheet.py
```




Issue created by migration from https://trac.sagemath.org/ticket/3583





---

archive/issue_events_008202.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2008-07-07T15:19:29Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3583",
    "milestone": "sage-3.0.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3583#event-8202"
}
```



---

archive/issue_comments_025247.json:
```json
{
    "body": "Attachment [sage-3583.patch](tarball://root/attachments/some-uuid/ticket3583/sage-3583.patch) by @williamstein created at 2008-07-07 18:44:25",
    "created_at": "2008-07-07T18:44:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3583#issuecomment-25247",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-3583.patch](tarball://root/attachments/some-uuid/ticket3583/sage-3583.patch) by @williamstein created at 2008-07-07 18:44:25



---

archive/issue_comments_025248.json:
```json
{
    "body": "After brief discussion with wstein in #sage-devel, this looks fine.",
    "created_at": "2008-07-07T18:51:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3583#issuecomment-25248",
    "user": "https://github.com/ncalexan"
}
```

After brief discussion with wstein in #sage-devel, this looks fine.



---

archive/issue_comments_025249.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-07T21:50:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3583#issuecomment-25249",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_008203.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2008-07-07T21:50:02Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3583",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3583#event-8203"
}
```



---

archive/issue_comments_025250.json:
```json
{
    "body": "Merged in Sage 3.0.4.rc0",
    "created_at": "2008-07-07T21:51:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3583#issuecomment-25250",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.4.rc0
