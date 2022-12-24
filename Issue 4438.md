# Issue 4438: Sage 3.2.a2: numerical noise in sage/calculus/functional.py and wester.py

archive/issues_004438.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\nsage -t  devel/sage/sage/calculus/functional.py             \n**********************************************************************\nFile \"/home/mabshoff/build-3.2.a2/sage-3.2.alpha2-menas/tmp/functional.py\", line 248:\n    sage: [float(h(i)) for i in range(5)]\nExpected:\n    <BLANKLINE>\n    [0.0,\n     -1.1102230246251565e-16,\n     -5.5511151231257827e-17,\n     -5.5511151231257827e-17,\n     -6.9388939039072284e-17]\nGot:\n    [0.0, -1.1102230246251565e-16, 5.5511151231257827e-17, -5.5511151231257827e-17, -6.9388939039072284e-17]\n**********************************************************************\n\n\nsage -t  devel/sage/sage/calculus/wester.py                 \n**********************************************************************\nFile \"/home/mabshoff/build-3.2.a2/sage-3.2.alpha2-menas/tmp/wester.py\", line 261:\n    : [float(f(i/10)) for i in range(1,5)]\nExpected:\n    <BLANKLINE>\n    [-0.00033670040754082975,\n     -0.0027778004096620235,\n     -0.0098909940914040928,\n     -0.025411145508414501]\nGot:\n    [-0.00033670040754082975, -0.0027778004096620235, -0.0098909940914039263, -0.02541114550841439]\n**********************************************************************\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4438\n\n",
    "created_at": "2008-11-04T13:55:36Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "Sage 3.2.a2: numerical noise in sage/calculus/functional.py and wester.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4438",
    "user": "mabshoff"
}
```
Assignee: mabshoff


```
sage -t  devel/sage/sage/calculus/functional.py             
**********************************************************************
File "/home/mabshoff/build-3.2.a2/sage-3.2.alpha2-menas/tmp/functional.py", line 248:
    sage: [float(h(i)) for i in range(5)]
Expected:
    <BLANKLINE>
    [0.0,
     -1.1102230246251565e-16,
     -5.5511151231257827e-17,
     -5.5511151231257827e-17,
     -6.9388939039072284e-17]
Got:
    [0.0, -1.1102230246251565e-16, 5.5511151231257827e-17, -5.5511151231257827e-17, -6.9388939039072284e-17]
**********************************************************************


sage -t  devel/sage/sage/calculus/wester.py                 
**********************************************************************
File "/home/mabshoff/build-3.2.a2/sage-3.2.alpha2-menas/tmp/wester.py", line 261:
    : [float(f(i/10)) for i in range(1,5)]
Expected:
    <BLANKLINE>
    [-0.00033670040754082975,
     -0.0027778004096620235,
     -0.0098909940914040928,
     -0.025411145508414501]
Got:
    [-0.00033670040754082975, -0.0027778004096620235, -0.0098909940914039263, -0.02541114550841439]
**********************************************************************
```


Issue created by migration from https://trac.sagemath.org/ticket/4438





---

archive/issue_comments_032626.json:
```json
{
    "body": "Hi, these failures do not seem to be related.\n\nIn the \"functional.py\" case, the sign of the third entry flips (!); in the \"wester.py\" case, the last three digits of the third entry disagree.",
    "created_at": "2008-11-04T22:11:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4438#issuecomment-32626",
    "user": "GeorgSWeber"
}
```

Hi, these failures do not seem to be related.

In the "functional.py" case, the sign of the third entry flips (!); in the "wester.py" case, the last three digits of the third entry disagree.



---

archive/issue_comments_032627.json:
```json
{
    "body": "Replying to [comment:1 GeorgSWeber]:\n> Hi, these failures do not seem to be related.\n\nYeah, I know. The point was that these are two small failures, so one ticket seem to cover it.\n\n> In the \"functional.py\" case, the sign of the third entry flips (!); in the \"wester.py\" case, the last three digits of the third entry disagree.\n\nYep, I have patches that will be up shortly.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-04T22:18:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4438#issuecomment-32627",
    "user": "mabshoff"
}
```

Replying to [comment:1 GeorgSWeber]:
> Hi, these failures do not seem to be related.

Yeah, I know. The point was that these are two small failures, so one ticket seem to cover it.

> In the "functional.py" case, the sign of the third entry flips (!); in the "wester.py" case, the last three digits of the third entry disagree.

Yep, I have patches that will be up shortly.

Cheers,

Michael



---

archive/issue_comments_032628.json:
```json
{
    "body": "Attachment [trac_4438.patch](tarball://root/attachments/some-uuid/ticket4438/trac_4438.patch) by mabshoff created at 2008-11-05 22:28:02",
    "created_at": "2008-11-05T22:28:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4438#issuecomment-32628",
    "user": "mabshoff"
}
```

Attachment [trac_4438.patch](tarball://root/attachments/some-uuid/ticket4438/trac_4438.patch) by mabshoff created at 2008-11-05 22:28:02



---

archive/issue_comments_032629.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-11-05T22:28:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4438#issuecomment-32629",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_032630.json:
```json
{
    "body": "Looks good.",
    "created_at": "2008-11-05T22:31:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4438#issuecomment-32630",
    "user": "@craigcitro"
}
```

Looks good.



---

archive/issue_comments_032631.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-05T23:14:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4438#issuecomment-32631",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_032632.json:
```json
{
    "body": "Merged in Sage 3.2.alpha3",
    "created_at": "2008-11-05T23:14:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4438#issuecomment-32632",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.alpha3
