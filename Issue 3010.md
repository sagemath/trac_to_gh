# Issue 3010: Numerical noise doctest failure in rings/complex_double.pyx

archive/issues_003010.json:
```json
{
    "body": "Assignee: failure\n\nAndrzej Giniewicz reported:\n\n```\nsage -t  devel/sage-main/sage/rings/complex_double.pyx\n**********************************************************************\nFile \"/opt/sage-3.0.rc1/tmp/complex_double.py\", line 1659:\n    sage: z^2 - z + 1\nExpected:\n    2.22044604925e-16 + ...e-16*I\nGot:\n    2.22044604925e-16\n**********************************************************************\n1 items had failures:\n   1 of   7 in __main__.example_93\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /opt/sage-3.0.rc1/\ntmp/.doctest_complex_double.py\n         [4.1 s]\nexit code: 1024\n```\n\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/3010\n\n",
    "created_at": "2008-04-23T21:07:14Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "title": "Numerical noise doctest failure in rings/complex_double.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3010",
    "user": "mabshoff"
}
```
Assignee: failure

Andrzej Giniewicz reported:

```
sage -t  devel/sage-main/sage/rings/complex_double.pyx
**********************************************************************
File "/opt/sage-3.0.rc1/tmp/complex_double.py", line 1659:
    sage: z^2 - z + 1
Expected:
    2.22044604925e-16 + ...e-16*I
Got:
    2.22044604925e-16
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_93
***Test Failed*** 1 failures.
For whitespace errors, see the file /opt/sage-3.0.rc1/
tmp/.doctest_complex_double.py
         [4.1 s]
exit code: 1024
```


Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/3010





---

archive/issue_comments_020694.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-05-03T15:37:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3010#issuecomment-20694",
    "user": "mabshoff"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_020695.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-05-03T15:53:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3010#issuecomment-20695",
    "user": "mabshoff"
}
```

Attachment



---

archive/issue_comments_020696.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-05-03T15:54:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3010#issuecomment-20696",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_020697.json:
```json
{
    "body": "Changing assignee from failure to mabshoff.",
    "created_at": "2008-05-03T15:54:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3010#issuecomment-20697",
    "user": "mabshoff"
}
```

Changing assignee from failure to mabshoff.



---

archive/issue_comments_020698.json:
```json
{
    "body": "After applying that patch, doctest pass without problem",
    "created_at": "2008-05-03T16:29:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3010#issuecomment-20698",
    "user": "aginiewicz"
}
```

After applying that patch, doctest pass without problem



---

archive/issue_comments_020699.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-03T16:33:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3010#issuecomment-20699",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_020700.json:
```json
{
    "body": "Merged in Sage 3.0.1.final",
    "created_at": "2008-05-03T16:33:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3010#issuecomment-20700",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.1.final
