# Issue 3806: improvements to plot.py

archive/issues_003806.json:
```json
{
    "body": "Assignee: @williamstein\n\nIf you do\n\n\n```\nsage: plot(sin(x), 100, 120))\n```\n\n\nyou get a plot which goes from -1 to 120 which is mostly empty space.  The is due to the behavior of Graphics() and _extend_axes.  Many of the other graphics objects suffer this same problem.  This patch fixes that and cleans up some of the useless code factoring in plot.py which hopefully makes it easier to understand.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3806\n\n",
    "created_at": "2008-08-11T19:57:07Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1",
    "title": "improvements to plot.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3806",
    "user": "@mwhansen"
}
```
Assignee: @williamstein

If you do


```
sage: plot(sin(x), 100, 120))
```


you get a plot which goes from -1 to 120 which is mostly empty space.  The is due to the behavior of Graphics() and _extend_axes.  Many of the other graphics objects suffer this same problem.  This patch fixes that and cleans up some of the useless code factoring in plot.py which hopefully makes it easier to understand.

Issue created by migration from https://trac.sagemath.org/ticket/3806





---

archive/issue_comments_027047.json:
```json
{
    "body": "Attachment [trac_3806-1.patch](tarball://root/attachments/some-uuid/ticket3806/trac_3806-1.patch) by @mwhansen created at 2008-08-11 19:58:28",
    "created_at": "2008-08-11T19:58:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3806#issuecomment-27047",
    "user": "@mwhansen"
}
```

Attachment [trac_3806-1.patch](tarball://root/attachments/some-uuid/ticket3806/trac_3806-1.patch) by @mwhansen created at 2008-08-11 19:58:28



---

archive/issue_comments_027048.json:
```json
{
    "body": "Attachment [trac_3806-2.patch](tarball://root/attachments/some-uuid/ticket3806/trac_3806-2.patch) by @mwhansen created at 2008-08-11 19:59:41",
    "created_at": "2008-08-11T19:59:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3806#issuecomment-27048",
    "user": "@mwhansen"
}
```

Attachment [trac_3806-2.patch](tarball://root/attachments/some-uuid/ticket3806/trac_3806-2.patch) by @mwhansen created at 2008-08-11 19:59:41



---

archive/issue_comments_027049.json:
```json
{
    "body": "mabshoff is going to test it, but super-dooper +1 on style!",
    "created_at": "2008-08-12T01:52:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3806#issuecomment-27049",
    "user": "ekirkman"
}
```

mabshoff is going to test it, but super-dooper +1 on style!



---

archive/issue_comments_027050.json:
```json
{
    "body": "The following test fails:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.alpha2$ ./sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_point.py\nsage -t -long devel/sage/sage/schemes/elliptic_curves/ell_point.py\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.1.alpha2/tmp/ell_point.py\", line 392:\n    sage: P.plot(pointsize=30, rgbcolor=(1,0,0))\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.alpha2/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_18[3]>\", line 1, in <module>\n        P.plot(pointsize=Integer(30), rgbcolor=(Integer(1),Integer(0),Integer(0)))###line 392:\n    sage: P.plot(pointsize=30, rgbcolor=(1,0,0))\n      File \"sage_object.pyx\", line 92, in sage.structure.sage_object.SageObject.__repr__ (sage/structure/sage_object.c:795)\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.alpha2/local/lib/python2.5/site-packages/sage/plot/plot.py\", line 740, in _repr_\n        self.show()\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.alpha2/local/lib/python2.5/site-packages/sage/plot/plot.py\", line 1242, in show\n        aspect_ratio=aspect_ratio)\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.alpha2/local/lib/python2.5/site-packages/sage/plot/plot.py\", line 1421, in save\n        xmin, xmax, ymin, ymax = sage_axes.add_xy_axes(subplot, xmin, xmax, ymin, ymax)\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.alpha2/local/lib/python2.5/site-packages/sage/plot/axes.py\", line 320, in add_xy_axes\n        y_axis_xpos, xstep, xtslminor, xtslmajor = self._find_axes(xmin, xmax)\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.alpha2/local/lib/python2.5/site-packages/sage/plot/axes.py\", line 234, in _find_axes\n        raise ValueError, \"maxval >= minval is required\"\n    ValueError: maxval >= minval is required\n**********************************************************************\n1 items had failures:\n   1 of   4 in __main__.example_18\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.1.alpha2/tmp/.doctest_ell_point.py\n         [11.0 s]\nexit code: 1024\n```\n",
    "created_at": "2008-08-12T02:08:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3806#issuecomment-27050",
    "user": "mabshoff"
}
```

The following test fails:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.alpha2$ ./sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_point.py
sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_point.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.alpha2/tmp/ell_point.py", line 392:
    sage: P.plot(pointsize=30, rgbcolor=(1,0,0))
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.1.alpha2/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_18[3]>", line 1, in <module>
        P.plot(pointsize=Integer(30), rgbcolor=(Integer(1),Integer(0),Integer(0)))###line 392:
    sage: P.plot(pointsize=30, rgbcolor=(1,0,0))
      File "sage_object.pyx", line 92, in sage.structure.sage_object.SageObject.__repr__ (sage/structure/sage_object.c:795)
      File "/scratch/mabshoff/release-cycle/sage-3.1.alpha2/local/lib/python2.5/site-packages/sage/plot/plot.py", line 740, in _repr_
        self.show()
      File "/scratch/mabshoff/release-cycle/sage-3.1.alpha2/local/lib/python2.5/site-packages/sage/plot/plot.py", line 1242, in show
        aspect_ratio=aspect_ratio)
      File "/scratch/mabshoff/release-cycle/sage-3.1.alpha2/local/lib/python2.5/site-packages/sage/plot/plot.py", line 1421, in save
        xmin, xmax, ymin, ymax = sage_axes.add_xy_axes(subplot, xmin, xmax, ymin, ymax)
      File "/scratch/mabshoff/release-cycle/sage-3.1.alpha2/local/lib/python2.5/site-packages/sage/plot/axes.py", line 320, in add_xy_axes
        y_axis_xpos, xstep, xtslminor, xtslmajor = self._find_axes(xmin, xmax)
      File "/scratch/mabshoff/release-cycle/sage-3.1.alpha2/local/lib/python2.5/site-packages/sage/plot/axes.py", line 234, in _find_axes
        raise ValueError, "maxval >= minval is required"
    ValueError: maxval >= minval is required
**********************************************************************
1 items had failures:
   1 of   4 in __main__.example_18
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.1.alpha2/tmp/.doctest_ell_point.py
         [11.0 s]
exit code: 1024
```




---

archive/issue_comments_027051.json:
```json
{
    "body": "Equivalently,\n\n```\nsage: point((-1,1),pointsize=30, rgbcolor=(1,0,0))\n<boom>\n```\n",
    "created_at": "2008-08-12T05:46:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3806#issuecomment-27051",
    "user": "@rlmill"
}
```

Equivalently,

```
sage: point((-1,1),pointsize=30, rgbcolor=(1,0,0))
<boom>
```




---

archive/issue_comments_027052.json:
```json
{
    "body": "Attachment [trac_3806-bug.patch](tarball://root/attachments/some-uuid/ticket3806/trac_3806-bug.patch) by @mwhansen created at 2008-08-12 06:00:36\n\n+1 to rlm's patch",
    "created_at": "2008-08-12T06:00:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3806#issuecomment-27052",
    "user": "@mwhansen"
}
```

Attachment [trac_3806-bug.patch](tarball://root/attachments/some-uuid/ticket3806/trac_3806-bug.patch) by @mwhansen created at 2008-08-12 06:00:36

+1 to rlm's patch



---

archive/issue_comments_027053.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-12T06:30:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3806#issuecomment-27053",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_027054.json:
```json
{
    "body": "Merged all three patches in Sage 3.1.alpha2",
    "created_at": "2008-08-12T06:30:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3806#issuecomment-27054",
    "user": "mabshoff"
}
```

Merged all three patches in Sage 3.1.alpha2
