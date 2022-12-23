# Issue 3583: randomness in some worksheet doctests

archive/issues_003583.json:
```json
{
    "body": "Assignee: failure\n\nOn Debian 64-bit vmware:\n\n\n```\nFile \"/home/was/build/sage-3.0.4.alpha2/tmp/worksheet.py\", line 2677:\n    sage: W.interrupt()\nExpected:\n    True\nGot:\n    False\n**********************************************************************\nFile \"/home/was/build/sage-3.0.4.alpha2/tmp/worksheet.py\", line 2681:\n    sage: W.check_comp()\nExpected:\n    ('e', None)\nGot:\n    ('w', Cell 0; in=factor(2^997-1), out=)\n**********************************************************************\n1 items had failures:\n   2 of  10 in __main__.example_85\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file /home/was/build/sage-3.0.4.alpha2/tmp/.doctest_worksheet.py\n```\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3583\n\n",
    "created_at": "2008-07-07T15:19:22Z",
    "labels": [
        "doctest coverage",
        "blocker",
        "bug"
    ],
    "title": "randomness in some worksheet doctests",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3583",
    "user": "was"
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

archive/issue_comments_025297.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-07-07T18:44:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3583#issuecomment-25297",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_025298.json:
```json
{
    "body": "After brief discussion with wstein in #sage-devel, this looks fine.",
    "created_at": "2008-07-07T18:51:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3583#issuecomment-25298",
    "user": "ncalexan"
}
```

After brief discussion with wstein in #sage-devel, this looks fine.



---

archive/issue_comments_025299.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-07T21:50:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3583#issuecomment-25299",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_025300.json:
```json
{
    "body": "Merged in Sage 3.0.4.rc0",
    "created_at": "2008-07-07T21:51:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3583#issuecomment-25300",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.4.rc0
