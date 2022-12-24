# Issue 4363: Do not automatically evaluate interact cells in notebook

archive/issues_004363.json:
```json
{
    "body": "Assignee: boothby\n\nCurrent behavior is that `@`interact cells automatically evaluate upon opening a worksheet.  This can cause problems if (for instance) the cell depends on other cells which are not automatically evaluated, and also can take a long time if there are lots of them.  \n\nSince other cells do not auto-evaluate, and since this functionality still is easily available by putting #auto in the cell, this ticket calls for the current behavior to be changed.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4363\n\n",
    "created_at": "2008-10-24T15:15:48Z",
    "labels": [
        "notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "Do not automatically evaluate interact cells in notebook",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4363",
    "user": "kcrisman"
}
```
Assignee: boothby

Current behavior is that `@`interact cells automatically evaluate upon opening a worksheet.  This can cause problems if (for instance) the cell depends on other cells which are not automatically evaluated, and also can take a long time if there are lots of them.  

Since other cells do not auto-evaluate, and since this functionality still is easily available by putting #auto in the cell, this ticket calls for the current behavior to be changed.


Issue created by migration from https://trac.sagemath.org/ticket/4363





---

archive/issue_comments_032051.json:
```json
{
    "body": "I second that this should be changed.",
    "created_at": "2008-10-24T21:30:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4363#issuecomment-32051",
    "user": "jason"
}
```

I second that this should be changed.



---

archive/issue_comments_032052.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-11-13T23:25:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4363#issuecomment-32052",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_032053.json:
```json
{
    "body": "I've also added this as a test case to the notebook test suite.",
    "created_at": "2008-11-13T23:25:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4363#issuecomment-32053",
    "user": "mhansen"
}
```

I've also added this as a test case to the notebook test suite.



---

archive/issue_comments_032054.json:
```json
{
    "body": "Changing assignee from boothby to mhansen.",
    "created_at": "2008-11-13T23:25:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4363#issuecomment-32054",
    "user": "mhansen"
}
```

Changing assignee from boothby to mhansen.



---

archive/issue_comments_032055.json:
```json
{
    "body": "I think to solve this trac ticket, it is necessary that:\n\n1. Output of interact cells should be completely empty when a worksheet is open.\n\n2. `@`interact needs to work with #auto (or %auto?) because I have a project with a student that involves making a bunch of interacts that are all %hideall'd, so one sees *only* the controls.",
    "created_at": "2008-11-14T00:13:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4363#issuecomment-32055",
    "user": "was"
}
```

I think to solve this trac ticket, it is necessary that:

1. Output of interact cells should be completely empty when a worksheet is open.

2. `@`interact needs to work with #auto (or %auto?) because I have a project with a student that involves making a bunch of interacts that are all %hideall'd, so one sees *only* the controls.



---

archive/issue_comments_032056.json:
```json
{
    "body": "Just to emphasize, the patch above mysteriously doesn't work with #auto...",
    "created_at": "2008-11-14T00:13:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4363#issuecomment-32056",
    "user": "was"
}
```

Just to emphasize, the patch above mysteriously doesn't work with #auto...



---

archive/issue_comments_032057.json:
```json
{
    "body": "Attachment [trac_4363.patch](tarball://root/attachments/some-uuid/ticket4363/trac_4363.patch) by mhansen created at 2009-01-19 04:16:14",
    "created_at": "2009-01-19T04:16:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4363#issuecomment-32057",
    "user": "mhansen"
}
```

Attachment [trac_4363.patch](tarball://root/attachments/some-uuid/ticket4363/trac_4363.patch) by mhansen created at 2009-01-19 04:16:14



---

archive/issue_comments_032058.json:
```json
{
    "body": "I've posted a patch which does not enqueue interact cells at startup and deletes their output so that users don't think that they're running.\n\nI've also made a ticket to fix the auto-evaluation at http://trac.sagemath.org/sage_trac/ticket/5020 .  I think this is a separate issue, and I'm looking into it.",
    "created_at": "2009-01-19T04:19:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4363#issuecomment-32058",
    "user": "mhansen"
}
```

I've posted a patch which does not enqueue interact cells at startup and deletes their output so that users don't think that they're running.

I've also made a ticket to fix the auto-evaluation at http://trac.sagemath.org/sage_trac/ticket/5020 .  I think this is a separate issue, and I'm looking into it.



---

archive/issue_comments_032059.json:
```json
{
    "body": "This seems to solve the problem, and the auto-launch problem of #4947.  My setup seems to have some issues with #auto cells, so I can't test the compatibility of this patch with that, but that is addressed in other ways by #5020.",
    "created_at": "2009-01-19T05:01:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4363#issuecomment-32059",
    "user": "mhampton"
}
```

This seems to solve the problem, and the auto-launch problem of #4947.  My setup seems to have some issues with #auto cells, so I can't test the compatibility of this patch with that, but that is addressed in other ways by #5020.



---

archive/issue_comments_032060.json:
```json
{
    "body": "Changing priority from minor to major.",
    "created_at": "2009-01-19T05:01:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4363#issuecomment-32060",
    "user": "mhampton"
}
```

Changing priority from minor to major.



---

archive/issue_comments_032061.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-19T06:10:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4363#issuecomment-32061",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_032062.json:
```json
{
    "body": "Merged in Sage 3.3.alpha0",
    "created_at": "2009-01-19T06:10:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4363#issuecomment-32062",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha0
