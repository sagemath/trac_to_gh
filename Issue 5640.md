# Issue 5640: no way to figure out list of colormaps from matrix plot's docstring

archive/issues_005640.json:
```json
{
    "body": "Assignee: @williamstein\n\nThis sentence, which is in the help for contour_plot, should also be in the help for the plot method on matrices:\n\n\n```\n                        cmap -- the name of\n                        a predefined colormap, a list of colors\n                        or an instance of a matplotlib Colormap.\n                        Type: import matplotlib.cm; matplotlib.cm.datad.keys()\n                        for available colormap names.\n```\n\n\nIt should also be in the output here too:\n\n```\nsage: matrix(QQ,1,1).plot(cmap0=0)\n          \t\n\nverbose 0 (84: primitive.py, options) WARNING: Ignoring option 'cmap0'=0\nverbose 0 (84: primitive.py, options) \nThe allowed options for MatrixPlot defined by a 1 x 1 data grid are:\n    cmap           the name of a predefined colormap, \n                        a list of colors or an instance of a \n                        matplotlib Colormap.\n    zorder         The layer level in which to draw                     \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5640\n\n",
    "created_at": "2009-03-30T03:16:35Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1",
    "title": "no way to figure out list of colormaps from matrix plot's docstring",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5640",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

This sentence, which is in the help for contour_plot, should also be in the help for the plot method on matrices:


```
                        cmap -- the name of
                        a predefined colormap, a list of colors
                        or an instance of a matplotlib Colormap.
                        Type: import matplotlib.cm; matplotlib.cm.datad.keys()
                        for available colormap names.
```


It should also be in the output here too:

```
sage: matrix(QQ,1,1).plot(cmap0=0)
          	

verbose 0 (84: primitive.py, options) WARNING: Ignoring option 'cmap0'=0
verbose 0 (84: primitive.py, options) 
The allowed options for MatrixPlot defined by a 1 x 1 data grid are:
    cmap           the name of a predefined colormap, 
                        a list of colors or an instance of a 
                        matplotlib Colormap.
    zorder         The layer level in which to draw                     
```


Issue created by migration from https://trac.sagemath.org/ticket/5640





---

archive/issue_comments_043970.json:
```json
{
    "body": "Depends on #6269, at least potentially",
    "created_at": "2009-06-20T01:10:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5640#issuecomment-43970",
    "user": "https://github.com/kcrisman"
}
```

Depends on #6269, at least potentially



---

archive/issue_comments_043971.json:
```json
{
    "body": "Attachment [trac_5640.patch](tarball://root/attachments/some-uuid/ticket5640/trac_5640.patch) by @kcrisman created at 2009-06-20 01:16:31\n\nThis should take care of the issue on the description.  Patch may depend on #6269; even though I can't find any specific instances where they overlap on code hunks, they do overlap in files, so better to be safe.  Note that this patch does not take care of #5083.  I have also added/improved documentation on the files in question.",
    "created_at": "2009-06-20T01:16:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5640#issuecomment-43971",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_5640.patch](tarball://root/attachments/some-uuid/ticket5640/trac_5640.patch) by @kcrisman created at 2009-06-20 01:16:31

This should take care of the issue on the description.  Patch may depend on #6269; even though I can't find any specific instances where they overlap on code hunks, they do overlap in files, so better to be safe.  Note that this patch does not take care of #5083.  I have also added/improved documentation on the files in question.



---

archive/issue_comments_043972.json:
```json
{
    "body": "Changing assignee from @williamstein to @kcrisman.",
    "created_at": "2009-06-20T01:16:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5640#issuecomment-43972",
    "user": "https://github.com/kcrisman"
}
```

Changing assignee from @williamstein to @kcrisman.



---

archive/issue_comments_043973.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-20T01:16:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5640#issuecomment-43973",
    "user": "https://github.com/kcrisman"
}
```

Changing status from new to assigned.



---

archive/issue_comments_043974.json:
```json
{
    "body": "Some hunk failures when applied against Sage 4.1.alpha0:\n\n```\nsage: hg_sage.apply(\"http://trac.sagemath.org/sage_trac/raw-attachment/ticket/5640/trac_5640.patch\")\nAttempting to load remote file: http://trac.sagemath.org/sage_trac/raw-attachment/ticket/5640/trac_5640.patch\nLoading: [.....]\ncd \"/scratch/mvngu/sage-4.1.alpha0-sage.math-only-x86_64-Linux/devel/sage\" && hg status\ncd \"/scratch/mvngu/sage-4.1.alpha0-sage.math-only-x86_64-Linux/devel/sage\" && hg status\ncd \"/scratch/mvngu/sage-4.1.alpha0-sage.math-only-x86_64-Linux/devel/sage\" && hg import   \"/home/mvngu/.sage/temp/sage.math.washington.edu/23662/tmp_1.patch\"\napplying /home/mvngu/.sage/temp/sage.math.washington.edu/23662/tmp_1.patch\npatching file sage/plot/contour_plot.py\nHunk #2 FAILED at 76\nHunk #3 FAILED at 84\nHunk #5 FAILED at 147\nHunk #6 FAILED at 223\nHunk #7 FAILED at 266\nHunk #8 FAILED at 287\nHunk #9 FAILED at 405\n7 out of 9 hunks FAILED -- saving rejects to file sage/plot/contour_plot.py.rej\npatching file sage/plot/density_plot.py\nHunk #2 FAILED at 78\nHunk #3 FAILED at 86\nHunk #4 FAILED at 121\n3 out of 4 hunks FAILED -- saving rejects to file sage/plot/density_plot.py.rej\npatching file sage/plot/matrix_plot.py\nHunk #2 FAILED at 81\nHunk #4 FAILED at 135\n2 out of 4 hunks FAILED -- saving rejects to file sage/plot/matrix_plot.py.rej\nabort: patch failed to apply\n```\n",
    "created_at": "2009-06-24T22:15:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5640#issuecomment-43974",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Some hunk failures when applied against Sage 4.1.alpha0:

```
sage: hg_sage.apply("http://trac.sagemath.org/sage_trac/raw-attachment/ticket/5640/trac_5640.patch")
Attempting to load remote file: http://trac.sagemath.org/sage_trac/raw-attachment/ticket/5640/trac_5640.patch
Loading: [.....]
cd "/scratch/mvngu/sage-4.1.alpha0-sage.math-only-x86_64-Linux/devel/sage" && hg status
cd "/scratch/mvngu/sage-4.1.alpha0-sage.math-only-x86_64-Linux/devel/sage" && hg status
cd "/scratch/mvngu/sage-4.1.alpha0-sage.math-only-x86_64-Linux/devel/sage" && hg import   "/home/mvngu/.sage/temp/sage.math.washington.edu/23662/tmp_1.patch"
applying /home/mvngu/.sage/temp/sage.math.washington.edu/23662/tmp_1.patch
patching file sage/plot/contour_plot.py
Hunk #2 FAILED at 76
Hunk #3 FAILED at 84
Hunk #5 FAILED at 147
Hunk #6 FAILED at 223
Hunk #7 FAILED at 266
Hunk #8 FAILED at 287
Hunk #9 FAILED at 405
7 out of 9 hunks FAILED -- saving rejects to file sage/plot/contour_plot.py.rej
patching file sage/plot/density_plot.py
Hunk #2 FAILED at 78
Hunk #3 FAILED at 86
Hunk #4 FAILED at 121
3 out of 4 hunks FAILED -- saving rejects to file sage/plot/density_plot.py.rej
patching file sage/plot/matrix_plot.py
Hunk #2 FAILED at 81
Hunk #4 FAILED at 135
2 out of 4 hunks FAILED -- saving rejects to file sage/plot/matrix_plot.py.rej
abort: patch failed to apply
```




---

archive/issue_comments_043975.json:
```json
{
    "body": "kcrisman: Can you rebase the patch?",
    "created_at": "2009-06-25T00:14:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5640#issuecomment-43975",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

kcrisman: Can you rebase the patch?



---

archive/issue_comments_043976.json:
```json
{
    "body": "rebased against Sage 4.1.alpha1",
    "created_at": "2009-06-26T00:05:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5640#issuecomment-43976",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

rebased against Sage 4.1.alpha1



---

archive/issue_comments_043977.json:
```json
{
    "body": "Attachment [trac_5640-rebased.patch](tarball://root/attachments/some-uuid/ticket5640/trac_5640-rebased.patch) by mvngu created at 2009-06-26 00:10:25\n\nThe patch `trac_5640-rebased.patch` is rebased against Sage 4.1.alpha1 and depends on #6269. Thus patches should be applied in the following order:\n1. the rebased patch at #6269\n2. the rebased patch on this ticket",
    "created_at": "2009-06-26T00:10:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5640#issuecomment-43977",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_5640-rebased.patch](tarball://root/attachments/some-uuid/ticket5640/trac_5640-rebased.patch) by mvngu created at 2009-06-26 00:10:25

The patch `trac_5640-rebased.patch` is rebased against Sage 4.1.alpha1 and depends on #6269. Thus patches should be applied in the following order:
1. the rebased patch at #6269
2. the rebased patch on this ticket



---

archive/issue_events_005883.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/boothby",
    "created_at": "2009-06-26T23:11:50Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5640",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5640#event-5883"
}
```



---

archive/issue_comments_043978.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-26T23:11:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5640#issuecomment-43978",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Resolution: fixed
