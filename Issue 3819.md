# Issue 3819: Sage 3.1.alpha1> time_series.pyx numerical noise doctest failures

archive/issues_003819.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @JohnCremona\n\nReported by John Cremona:\n\n```\n*******************\nFile \"/home/john/sage-3.1.alpha1/tmp/time_series.py\", line 1507:\n    sage: finance.TimeSeries([z.hurst_exponent() for z in y]).mean()\nExpected:\n    0.57984822577934747\nGot:\n    0.57984822577934769\n**********************************************************************\nFile \"/home/john/sage-3.1.alpha1/tmp/time_series.py\", line 1515:\n    sage: finance.TimeSeries([z.hurst_exponent() for z in y]).mean()\nExpected:\n    0.2861023256237053\nGot:\n    0.28610232562370524\n**********************************************************************\n1 items had failures:\n   2 of  16 in __main__.example_46\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file\n/home/john/sage-3.1.alpha1/tmp/.doctest_time_series.py\n         [9.8 s]\nexit code: 1024\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3819\n\n",
    "created_at": "2008-08-12T15:33:51Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1",
    "title": "Sage 3.1.alpha1> time_series.pyx numerical noise doctest failures",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3819",
    "user": "mabshoff"
}
```
Assignee: mabshoff

CC:  @JohnCremona

Reported by John Cremona:

```
*******************
File "/home/john/sage-3.1.alpha1/tmp/time_series.py", line 1507:
    sage: finance.TimeSeries([z.hurst_exponent() for z in y]).mean()
Expected:
    0.57984822577934747
Got:
    0.57984822577934769
**********************************************************************
File "/home/john/sage-3.1.alpha1/tmp/time_series.py", line 1515:
    sage: finance.TimeSeries([z.hurst_exponent() for z in y]).mean()
Expected:
    0.2861023256237053
Got:
    0.28610232562370524
**********************************************************************
1 items had failures:
   2 of  16 in __main__.example_46
***Test Failed*** 2 failures.
For whitespace errors, see the file
/home/john/sage-3.1.alpha1/tmp/.doctest_time_series.py
         [9.8 s]
exit code: 1024
```


Issue created by migration from https://trac.sagemath.org/ticket/3819





---

archive/issue_comments_027160.json:
```json
{
    "body": "John,\n\ncan you review this?\n\nCheers,\n\nMichael",
    "created_at": "2008-08-12T17:13:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3819#issuecomment-27160",
    "user": "mabshoff"
}
```

John,

can you review this?

Cheers,

Michael



---

archive/issue_comments_027161.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-08-12T17:13:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3819#issuecomment-27161",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_027162.json:
```json
{
    "body": "Attachment [trac_3819.patch](tarball://root/attachments/some-uuid/ticket3819/trac_3819.patch) by mabshoff created at 2008-08-12 17:23:00\n\nOops, adding John to the CC would help a lot when asking for his review :)\n\nCheers,\n\nMichael",
    "created_at": "2008-08-12T17:23:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3819#issuecomment-27162",
    "user": "mabshoff"
}
```

Attachment [trac_3819.patch](tarball://root/attachments/some-uuid/ticket3819/trac_3819.patch) by mabshoff created at 2008-08-12 17:23:00

Oops, adding John to the CC would help a lot when asking for his review :)

Cheers,

Michael



---

archive/issue_comments_027163.json:
```json
{
    "body": "I agree with this patch.",
    "created_at": "2008-08-13T00:18:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3819#issuecomment-27163",
    "user": "@williamstein"
}
```

I agree with this patch.



---

archive/issue_comments_027164.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-13T00:20:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3819#issuecomment-27164",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_027165.json:
```json
{
    "body": "Merged in Sage 3.1.alpha2",
    "created_at": "2008-08-13T00:20:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3819#issuecomment-27165",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.alpha2
