# Issue 3922: [with patch, needs review] Make nice arrows

archive/issues_003922.json:
```json
{
    "body": "Assignee: @williamstein\n\nWe've been having lots of trouble with arrows looking nice.  In this patch, there is a new matplotlib class that puts an arrow at the end of a line, using the same sort of things they do to put markers on lines.  This way, the arrows:\n\n1. don't depend on the aspect ratio of the plot\n\n2. don't depend on the scale of the plot.\n\nThey always look pretty :).\n\nIt would be nice to eventually upstream this functionality into the matplotlib Line2D class.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3922\n\n",
    "created_at": "2008-08-21T22:41:37Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "[with patch, needs review] Make nice arrows",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3922",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

We've been having lots of trouble with arrows looking nice.  In this patch, there is a new matplotlib class that puts an arrow at the end of a line, using the same sort of things they do to put markers on lines.  This way, the arrows:

1. don't depend on the aspect ratio of the plot

2. don't depend on the scale of the plot.

They always look pretty :).

It would be nice to eventually upstream this functionality into the matplotlib Line2D class.

Issue created by migration from https://trac.sagemath.org/ticket/3922





---

archive/issue_comments_027995.json:
```json
{
    "body": "Oh, the patch also updates the sage \"arrow\" class.  This patch is made for after applying the patch at #3853, but it might be possible to apply it before.",
    "created_at": "2008-08-21T22:43:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3922#issuecomment-27995",
    "user": "https://github.com/jasongrout"
}
```

Oh, the patch also updates the sage "arrow" class.  This patch is made for after applying the patch at #3853, but it might be possible to apply it before.



---

archive/issue_comments_027996.json:
```json
{
    "body": "It looks like a few doctests fail when they try to do `from sage.all_cmdline import *` or something.  I'm not sure exactly what this issue is here.  The error is that, in arrow_line.py, `import matplotlib` throws an error that there is no module named matplotlib.",
    "created_at": "2008-08-21T23:42:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3922#issuecomment-27996",
    "user": "https://github.com/jasongrout"
}
```

It looks like a few doctests fail when they try to do `from sage.all_cmdline import *` or something.  I'm not sure exactly what this issue is here.  The error is that, in arrow_line.py, `import matplotlib` throws an error that there is no module named matplotlib.



---

archive/issue_comments_027997.json:
```json
{
    "body": "Updated patch to correct some of the drawing code and added documentation.",
    "created_at": "2008-08-27T13:47:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3922#issuecomment-27997",
    "user": "https://github.com/jasongrout"
}
```

Updated patch to correct some of the drawing code and added documentation.



---

archive/issue_comments_027998.json:
```json
{
    "body": "The patch applies cleanly to sage 3.1.2alpha1.  All doctests pass with the patch applied on sage.math.",
    "created_at": "2008-08-27T13:57:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3922#issuecomment-27998",
    "user": "https://github.com/jasongrout"
}
```

The patch applies cleanly to sage 3.1.2alpha1.  All doctests pass with the patch applied on sage.math.



---

archive/issue_comments_027999.json:
```json
{
    "body": "The arrow_line.py should probably be moved to the matplotlib spkg.",
    "created_at": "2008-08-27T20:41:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3922#issuecomment-27999",
    "user": "https://github.com/mwhansen"
}
```

The arrow_line.py should probably be moved to the matplotlib spkg.



---

archive/issue_comments_028000.json:
```json
{
    "body": "Attachment [arrow_line.patch](tarball://root/attachments/some-uuid/ticket3922/arrow_line.patch) by @jasongrout created at 2008-09-03 23:47:30",
    "created_at": "2008-09-03T23:47:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3922#issuecomment-28000",
    "user": "https://github.com/jasongrout"
}
```

Attachment [arrow_line.patch](tarball://root/attachments/some-uuid/ticket3922/arrow_line.patch) by @jasongrout created at 2008-09-03 23:47:30



---

archive/issue_comments_028001.json:
```json
{
    "body": "Patch is updated to remove the arrow_line.py file and put it in the matplotlib spkg as a patch.  The updated matplotlib spkg is at: http://sage.math.washington.edu/home/jason/matplotlib-0.98.3.p1.spkg",
    "created_at": "2008-09-03T23:55:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3922#issuecomment-28001",
    "user": "https://github.com/jasongrout"
}
```

Patch is updated to remove the arrow_line.py file and put it in the matplotlib spkg as a patch.  The updated matplotlib spkg is at: http://sage.math.washington.edu/home/jason/matplotlib-0.98.3.p1.spkg



---

archive/issue_comments_028002.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-09-04T00:37:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3922#issuecomment-28002",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_028003.json:
```json
{
    "body": "Positive review on the spkg. \n\nCheers,\n\nMichael",
    "created_at": "2008-09-04T00:45:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3922#issuecomment-28003",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review on the spkg. 

Cheers,

Michael



---

archive/issue_comments_028004.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-04T01:10:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3922#issuecomment-28004",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_028005.json:
```json
{
    "body": "Merged patch and spkg in Sage 3.1.2.rc0",
    "created_at": "2008-09-04T01:10:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3922#issuecomment-28005",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged patch and spkg in Sage 3.1.2.rc0
