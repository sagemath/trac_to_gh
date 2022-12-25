# Issue 3763: [with patch, needs review] add conversions from AA/QQbar to standard types

archive/issues_003763.json:
```json
{
    "body": "Assignee: somebody\n\nThis was triggered by a comment from Jason Grout on IRC a couple of weeks ago.\n\nCurrently several of the conversions that \"ought to be there\", like CDF(QQbar(3)), are missing.\n\nThis patch adds conversions and tests, so that all of the conversions from AA/QQbar to float,complex,RDF,CDF,RR,CC,RIF,CIF,ZZ,QQ do the right thing.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3763\n\n",
    "created_at": "2008-08-03T00:28:15Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1",
    "title": "[with patch, needs review] add conversions from AA/QQbar to standard types",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3763",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: somebody

This was triggered by a comment from Jason Grout on IRC a couple of weeks ago.

Currently several of the conversions that "ought to be there", like CDF(QQbar(3)), are missing.

This patch adds conversions and tests, so that all of the conversions from AA/QQbar to float,complex,RDF,CDF,RR,CC,RIF,CIF,ZZ,QQ do the right thing.

Issue created by migration from https://trac.sagemath.org/ticket/3763





---

archive/issue_comments_026700.json:
```json
{
    "body": "Attachment [trac3763-qqbar-conversions.patch](tarball://root/attachments/some-uuid/ticket3763/trac3763-qqbar-conversions.patch) by @JohnCremona created at 2008-08-08 20:44:04\n\nI applied the patch to 3.1.alpha0.  It worked though this message appeared:\n\n```\npatching file sage/rings/qqbar.py\nHunk #1 succeeded at 122 with fuzz 2 (offset 0 lines).\n```\n\n\nI tested the file sage/rings/qqbar.py and found the following failure:\n\n```\nsage -t  devel/sage-qqbar/sage/rings/qqbar.py               **********************************************************************\nFile \"/home/john/tmp/sage-3.1.alpha0/tmp/qqbar.py\", line 368:\n    sage: convert_test_all(RIF)\nExpected:\n    [42.000000000000000?, 3.142857142857143?, 1.618033988749895?, -13.000000000000000?, 1.6181818181818183?, -2.645751311064591?, None]\nGot:\n    [[42.000000000000000 .. 42.000000000000000], [3.1428571428571427 .. 3.1428571428571433], [1.6180339887498946 .. 1.6180339887498950], [-13.000000000000000 .. -13.000000000000000], [1.6181818181818181 .. 1.6181818181818184], [-2.6457513110645908 .. -2.6457513110645902], None]\n**********************************************************************\nFile \"/home/john/tmp/sage-3.1.alpha0/tmp/qqbar.py\", line 370:\n    sage: convert_test_all(CIF)\nExpected:\n    [42.000000000000000?, 3.142857142857143?, 1.618033988749895?, -13.000000000000000?, 1.6181818181818183?, -2.645751311064591?, 0.3090169943749475? + 0.9510565162951536?*I]\nGot:\n    [[42.000000000000000 .. 42.000000000000000], [3.1428571428571427 .. 3.1428571428571433], [1.6180339887498946 .. 1.6180339887498950], [-13.000000000000000 .. -13.000000000000000], [1.6181818181818181 .. 1.6181818181818184], [-2.6457513110645908 .. -2.6457513110645902], [0.30901699437494739 .. 0.30901699437494746] + [0.95105651629515353 .. 0.95105651629515365]*I]\n```\n\n\nThe code looks reasonable to me, but some work is needed.  On second thoughts, looking at the \"expected\" output it seems that this patch relies on another -- the one where the output format ending in ? is introduced.  I'll go looking for that...",
    "created_at": "2008-08-08T20:44:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3763#issuecomment-26700",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac3763-qqbar-conversions.patch](tarball://root/attachments/some-uuid/ticket3763/trac3763-qqbar-conversions.patch) by @JohnCremona created at 2008-08-08 20:44:04

I applied the patch to 3.1.alpha0.  It worked though this message appeared:

```
patching file sage/rings/qqbar.py
Hunk #1 succeeded at 122 with fuzz 2 (offset 0 lines).
```


I tested the file sage/rings/qqbar.py and found the following failure:

```
sage -t  devel/sage-qqbar/sage/rings/qqbar.py               **********************************************************************
File "/home/john/tmp/sage-3.1.alpha0/tmp/qqbar.py", line 368:
    sage: convert_test_all(RIF)
Expected:
    [42.000000000000000?, 3.142857142857143?, 1.618033988749895?, -13.000000000000000?, 1.6181818181818183?, -2.645751311064591?, None]
Got:
    [[42.000000000000000 .. 42.000000000000000], [3.1428571428571427 .. 3.1428571428571433], [1.6180339887498946 .. 1.6180339887498950], [-13.000000000000000 .. -13.000000000000000], [1.6181818181818181 .. 1.6181818181818184], [-2.6457513110645908 .. -2.6457513110645902], None]
**********************************************************************
File "/home/john/tmp/sage-3.1.alpha0/tmp/qqbar.py", line 370:
    sage: convert_test_all(CIF)
Expected:
    [42.000000000000000?, 3.142857142857143?, 1.618033988749895?, -13.000000000000000?, 1.6181818181818183?, -2.645751311064591?, 0.3090169943749475? + 0.9510565162951536?*I]
Got:
    [[42.000000000000000 .. 42.000000000000000], [3.1428571428571427 .. 3.1428571428571433], [1.6180339887498946 .. 1.6180339887498950], [-13.000000000000000 .. -13.000000000000000], [1.6181818181818181 .. 1.6181818181818184], [-2.6457513110645908 .. -2.6457513110645902], [0.30901699437494739 .. 0.30901699437494746] + [0.95105651629515353 .. 0.95105651629515365]*I]
```


The code looks reasonable to me, but some work is needed.  On second thoughts, looking at the "expected" output it seems that this patch relies on another -- the one where the output format ending in ? is introduced.  I'll go looking for that...



---

archive/issue_comments_026701.json:
```json
{
    "body": "John,\n\nthat \"question mark\" patch is #3757, which has been merged in Sage 3.1.alpha1 - out hopefully tonight.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-08T20:57:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3763#issuecomment-26701",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

John,

that "question mark" patch is #3757, which has been merged in Sage 3.1.alpha1 - out hopefully tonight.

Cheers,

Michael



---

archive/issue_comments_026702.json:
```json
{
    "body": "OK, I applied also the two patches from #3757 and now the tests pass, so I am happy to endorse this patch too.",
    "created_at": "2008-08-08T21:16:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3763#issuecomment-26702",
    "user": "https://github.com/JohnCremona"
}
```

OK, I applied also the two patches from #3757 and now the tests pass, so I am happy to endorse this patch too.



---

archive/issue_comments_026703.json:
```json
{
    "body": "Merged in Sage 3.1.alpha1",
    "created_at": "2008-08-08T22:40:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3763#issuecomment-26703",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.alpha1



---

archive/issue_comments_026704.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-08T22:40:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3763#issuecomment-26704",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_003985.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-08-08T22:40:48Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3763",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3763#event-3985"
}
```
