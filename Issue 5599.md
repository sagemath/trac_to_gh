# Issue 5599: density_plot not centered correctly

archive/issues_005599.json:
```json
{
    "body": "Assignee: was\n\nCC:  wcauchois\n\n\n```\nsage: var('x,y')\n(x, y)\nsage: density_plot(1/(x^10+y^10), (x, -10, 10), (y, -10, 10))\n\n```\n\n\nclearly illustrates this problem\n\nIssue created by migration from https://trac.sagemath.org/ticket/5599\n\n",
    "created_at": "2009-03-24T10:28:46Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "title": "density_plot not centered correctly",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5599",
    "user": "robertwb"
}
```
Assignee: was

CC:  wcauchois


```
sage: var('x,y')
(x, y)
sage: density_plot(1/(x^10+y^10), (x, -10, 10), (y, -10, 10))

```


clearly illustrates this problem

Issue created by migration from https://trac.sagemath.org/ticket/5599





---

archive/issue_comments_043649.json:
```json
{
    "body": "The patch fixes the error and also fixes the same error several other places in the plotting code.",
    "created_at": "2009-03-24T21:08:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5599#issuecomment-43649",
    "user": "jason"
}
```

The patch fixes the error and also fixes the same error several other places in the plotting code.



---

archive/issue_comments_043650.json:
```json
{
    "body": "Yep, that fixes the issue.",
    "created_at": "2009-04-16T06:18:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5599#issuecomment-43650",
    "user": "robertwb"
}
```

Yep, that fixes the issue.



---

archive/issue_comments_043651.json:
```json
{
    "body": "Unfortunately this patch has bitrotted, so please rebase against 3.4.1.rc3.\n\n```\nsage-3.4.1.rc3/devel/sage$ patch -p1 < trac_5599-plot-center.patch \npatching file sage/plot/contour_plot.py\nHunk #1 succeeded at 149 (offset 1 line).\nHunk #2 FAILED at 246.\nHunk #3 FAILED at 264.\nHunk #4 succeeded at 285 (offset 14 lines).\n2 out of 4 hunks FAILED -- saving rejects to file sage/plot/contour_plot.py.rej\npatching file sage/plot/density_plot.py\nHunk #1 succeeded at 117 with fuzz 2.\n```\n\nOnce it is rebased the postive review can be reinstated provided the rejects are trivial to resolve. \n\nCheers,\n\nMichael",
    "created_at": "2009-04-16T11:49:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5599#issuecomment-43651",
    "user": "mabshoff"
}
```

Unfortunately this patch has bitrotted, so please rebase against 3.4.1.rc3.

```
sage-3.4.1.rc3/devel/sage$ patch -p1 < trac_5599-plot-center.patch 
patching file sage/plot/contour_plot.py
Hunk #1 succeeded at 149 (offset 1 line).
Hunk #2 FAILED at 246.
Hunk #3 FAILED at 264.
Hunk #4 succeeded at 285 (offset 14 lines).
2 out of 4 hunks FAILED -- saving rejects to file sage/plot/contour_plot.py.rej
patching file sage/plot/density_plot.py
Hunk #1 succeeded at 117 with fuzz 2.
```

Once it is rebased the postive review can be reinstated provided the rejects are trivial to resolve. 

Cheers,

Michael



---

archive/issue_comments_043652.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-05-30T08:23:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5599#issuecomment-43652",
    "user": "jason"
}
```

Attachment



---

archive/issue_comments_043653.json:
```json
{
    "body": "I've rebased the patch against 4.0.  Bill, can you review it?",
    "created_at": "2009-05-30T08:24:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5599#issuecomment-43653",
    "user": "jason"
}
```

I've rebased the patch against 4.0.  Bill, can you review it?



---

archive/issue_comments_043654.json:
```json
{
    "body": "Or Robert, can you review it?",
    "created_at": "2009-05-30T08:28:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5599#issuecomment-43654",
    "user": "jason"
}
```

Or Robert, can you review it?



---

archive/issue_comments_043655.json:
```json
{
    "body": "REFEREE REPORT\n\nApplies fine to Sage 4.0.rc0, and the changes look good. I tested some other plots as well, and they seemed fine. Positive review.",
    "created_at": "2009-06-02T09:11:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5599#issuecomment-43655",
    "user": "wcauchois"
}
```

REFEREE REPORT

Applies fine to Sage 4.0.rc0, and the changes look good. I tested some other plots as well, and they seemed fine. Positive review.



---

archive/issue_comments_043656.json:
```json
{
    "body": "Merged in 4.0.1.rc0.",
    "created_at": "2009-06-03T18:38:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5599#issuecomment-43656",
    "user": "mhansen"
}
```

Merged in 4.0.1.rc0.



---

archive/issue_comments_043657.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-03T18:38:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5599#issuecomment-43657",
    "user": "mhansen"
}
```

Resolution: fixed
