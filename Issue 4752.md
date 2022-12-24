# Issue 4752: list_plot3d crashes sage with some exact input

archive/issues_004752.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: list_plot3d, graphics\n\nThe following is an example of the problem (which was first noticed by \"Snark\" on the IRC sage-devel channel):\n\n```\nsage: pts =[(-4/5, -2/5, -2/5), (-4/5, -2/5, 2/5), (-4/5, 2/5, -2/5), (-4/5, 2/5, 2/5), (-2/5, -4/5, -2/5), (-2/5, -4/5, 2/5), (-2/5, -2/5, -4/5), (-2/5, -2/5, 4/5), (-2/5, 2/5, -4/5), (-2/5, 2/5, 4/5), (-2/5, 4/5, -2/5), (-2/5, 4/5, 2/5), (2/5, -4/5, -2/5), (2/5, -4/5, 2/5), (2/5, -2/5, -4/5), (2/5, -2/5, 4/5), (2/5, 2/5, -4/5), (2/5, 2/5, 4/5), (2/5, 4/5, -2/5), (2/5, 4/5, 2/5), (4/5, -2/5, -2/5), (4/5, -2/5, 2/5), (4/5, 2/5, -2/5), (4/5, 2/5, 2/5)]\nsage: show(list_plot3d(pts))\n\n------------------------------------------------------------\nUnhandled SIGBUS: A bus error occured in SAGE.\nThis probably occured because a *compiled* component\nof SAGE has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run SAGE under gdb with 'sage -gdb' to debug this.\nSAGE will now terminate (sorry).\n------------------------------------------------------------\n\npython(2829) malloc: *** error for object 0xed2f1f0: incorrect checksum for freed object - object was probably modified after being freed, break at szone_error to debug\npython(2829) malloc: *** set a breakpoint in szone_error to debug\n```\n\n\nIt doesn't crash if the pts are converted to numerical values, although the interpolated surface looks bad no matter which interpolation setting is used.  The example points are on a sphere.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4752\n\n",
    "created_at": "2008-12-10T21:11:34Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "list_plot3d crashes sage with some exact input",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4752",
    "user": "mhampton"
}
```
Assignee: @williamstein

Keywords: list_plot3d, graphics

The following is an example of the problem (which was first noticed by "Snark" on the IRC sage-devel channel):

```
sage: pts =[(-4/5, -2/5, -2/5), (-4/5, -2/5, 2/5), (-4/5, 2/5, -2/5), (-4/5, 2/5, 2/5), (-2/5, -4/5, -2/5), (-2/5, -4/5, 2/5), (-2/5, -2/5, -4/5), (-2/5, -2/5, 4/5), (-2/5, 2/5, -4/5), (-2/5, 2/5, 4/5), (-2/5, 4/5, -2/5), (-2/5, 4/5, 2/5), (2/5, -4/5, -2/5), (2/5, -4/5, 2/5), (2/5, -2/5, -4/5), (2/5, -2/5, 4/5), (2/5, 2/5, -4/5), (2/5, 2/5, 4/5), (2/5, 4/5, -2/5), (2/5, 4/5, 2/5), (4/5, -2/5, -2/5), (4/5, -2/5, 2/5), (4/5, 2/5, -2/5), (4/5, 2/5, 2/5)]
sage: show(list_plot3d(pts))

------------------------------------------------------------
Unhandled SIGBUS: A bus error occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------

python(2829) malloc: *** error for object 0xed2f1f0: incorrect checksum for freed object - object was probably modified after being freed, break at szone_error to debug
python(2829) malloc: *** set a breakpoint in szone_error to debug
```


It doesn't crash if the pts are converted to numerical values, although the interpolated surface looks bad no matter which interpolation setting is used.  The example points are on a sphere.

Issue created by migration from https://trac.sagemath.org/ticket/4752





---

archive/issue_comments_035957.json:
```json
{
    "body": "See also #4815 that is a dup of this, but has a traceback.",
    "created_at": "2008-12-16T16:39:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4752#issuecomment-35957",
    "user": "@williamstein"
}
```

See also #4815 that is a dup of this, but has a traceback.



---

archive/issue_comments_035958.json:
```json
{
    "body": "Josh Kantor remarks:\n\n```\nYeah, thats borked. Incidentally those test points include the top and bottom of the sphere so that will never look good. Even using only the top oints it looks crappy.\n\nOver the summer as part of the internship I learned how to do meshless interpolation easily using a technique called Radial basis functions. I attached something I wrote from scratch that works well with those points. I'll have to work it into a patch.\n\nIt may be that in the upgrade of scipy that something changed with the the scipy packages we are using, I'll have to check that, if not I'll replace that with something from scratch.\n```\n",
    "created_at": "2008-12-17T02:24:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4752#issuecomment-35958",
    "user": "@williamstein"
}
```

Josh Kantor remarks:

```
Yeah, thats borked. Incidentally those test points include the top and bottom of the sphere so that will never look good. Even using only the top oints it looks crappy.

Over the summer as part of the internship I learned how to do meshless interpolation easily using a technique called Radial basis functions. I attached something I wrote from scratch that works well with those points. I'll have to work it into a patch.

It may be that in the upgrade of scipy that something changed with the the scipy packages we are using, I'll have to check that, if not I'll replace that with something from scratch.
```




---

archive/issue_comments_035959.json:
```json
{
    "body": "Attachment [radial.py](tarball://root/attachments/some-uuid/ticket4752/radial.py) by jkantor created at 2008-12-17 06:29:36\n\nThe segfault problem is because scipy just doesn't like multiple points with the same x,y coordinates and different z coordinates. The attached patch fixes that.\n\n```\nsage: pts =[(-4/5, -2/5, -2/5), (-4/5, -2/5, 2/5), (-4/5, 2/5, -2/5), (-4/5, 2/5, 2/5), (-2/5, -4/5, -2/5), (-2/5, -4/5, 2/5), (-2/5, -2/5, -4/5), (-2/5, -2/5, 4/5), (-2/5, 2/5, -4/5), (-2/5, 2/5, 4/5), (-2/5, 4/5, -2/5), (-2/5, 4/5, 2/5), (2/5, -4/5, -2/5), (2/5, -4/5, 2/5), (2/5, -2/5, -4/5), (2/5, -2/5, 4/5), (2/5, 2/5, -4/5), (2/5, 2/5, 4/5), (2/5, 4/5, -2/5), (2/5, 4/5, 2/5), (4/5, -2/5, -2/5), (4/5, -2/5, 2/5), (4/5, 2/5, -2/5), (4/5, 2/5, 2/5)]\nsage: show(list_plot3d(pts))\n```\n\nI still intend to add the radial basis stuff, but this fixes the segfault\n\n\nnow raises an exception while\n\n\n```\nsage: pts =[(-4/5, -2/5, -2/5), (-4/5, -2/5, 2/5), (-4/5, 2/5, -2/5), (-4/5, 2/5, 2/5), (-2/5, -4/5, -2/5), (-2/5, -4/5, 2/5), (-2/5, -2/5, -4/5), (-2/5, -2/5, 4/5), (-2/5, 2/5, -4/5), (-2/5, 2/5, 4/5), (-2/5, 4/5, -2/5), (-2/5, 4/5, 2/5), (2/5, -4/5, -2/5), (2/5, -4/5, 2/5), (2/5, -2/5, -4/5), (2/5, -2/5, 4/5), (2/5, 2/5, -4/5), (2/5, 2/5, 4/5), (2/5, 4/5, -2/5), (2/5, 4/5, 2/5), (4/5, -2/5, -2/5), (4/5, -2/5, 2/5), (4/5, 2/5, -2/5), (4/5, 2/5, 2/5)]\nsage: pts=[a in pts if a[2]>0]\nsage: show(list_plot3d(pts))\n```\n\nworks.",
    "created_at": "2008-12-17T06:29:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4752#issuecomment-35959",
    "user": "jkantor"
}
```

Attachment [radial.py](tarball://root/attachments/some-uuid/ticket4752/radial.py) by jkantor created at 2008-12-17 06:29:36

The segfault problem is because scipy just doesn't like multiple points with the same x,y coordinates and different z coordinates. The attached patch fixes that.

```
sage: pts =[(-4/5, -2/5, -2/5), (-4/5, -2/5, 2/5), (-4/5, 2/5, -2/5), (-4/5, 2/5, 2/5), (-2/5, -4/5, -2/5), (-2/5, -4/5, 2/5), (-2/5, -2/5, -4/5), (-2/5, -2/5, 4/5), (-2/5, 2/5, -4/5), (-2/5, 2/5, 4/5), (-2/5, 4/5, -2/5), (-2/5, 4/5, 2/5), (2/5, -4/5, -2/5), (2/5, -4/5, 2/5), (2/5, -2/5, -4/5), (2/5, -2/5, 4/5), (2/5, 2/5, -4/5), (2/5, 2/5, 4/5), (2/5, 4/5, -2/5), (2/5, 4/5, 2/5), (4/5, -2/5, -2/5), (4/5, -2/5, 2/5), (4/5, 2/5, -2/5), (4/5, 2/5, 2/5)]
sage: show(list_plot3d(pts))
```

I still intend to add the radial basis stuff, but this fixes the segfault


now raises an exception while


```
sage: pts =[(-4/5, -2/5, -2/5), (-4/5, -2/5, 2/5), (-4/5, 2/5, -2/5), (-4/5, 2/5, 2/5), (-2/5, -4/5, -2/5), (-2/5, -4/5, 2/5), (-2/5, -2/5, -4/5), (-2/5, -2/5, 4/5), (-2/5, 2/5, -4/5), (-2/5, 2/5, 4/5), (-2/5, 4/5, -2/5), (-2/5, 4/5, 2/5), (2/5, -4/5, -2/5), (2/5, -4/5, 2/5), (2/5, -2/5, -4/5), (2/5, -2/5, 4/5), (2/5, 2/5, -4/5), (2/5, 2/5, 4/5), (2/5, 4/5, -2/5), (2/5, 4/5, 2/5), (4/5, -2/5, -2/5), (4/5, -2/5, 2/5), (4/5, 2/5, -2/5), (4/5, 2/5, 2/5)]
sage: pts=[a in pts if a[2]>0]
sage: show(list_plot3d(pts))
```

works.



---

archive/issue_comments_035960.json:
```json
{
    "body": "what I mean is the first code block raises an exception the second plots.",
    "created_at": "2008-12-17T06:30:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4752#issuecomment-35960",
    "user": "jkantor"
}
```

what I mean is the first code block raises an exception the second plots.



---

archive/issue_comments_035961.json:
```json
{
    "body": "Attachment [list_plot_patch.patch](tarball://root/attachments/some-uuid/ticket4752/list_plot_patch.patch) by jkantor created at 2008-12-17 06:31:28\n\npatch to list_plot3d",
    "created_at": "2008-12-17T06:31:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4752#issuecomment-35961",
    "user": "jkantor"
}
```

Attachment [list_plot_patch.patch](tarball://root/attachments/some-uuid/ticket4752/list_plot_patch.patch) by jkantor created at 2008-12-17 06:31:28

patch to list_plot3d



---

archive/issue_comments_035962.json:
```json
{
    "body": "2nd patch applied on top of first adds a doctest to demonstrate segfault does not occur it just catches the exception thrown.\n\nAlso I added a check that there are more than three points which is required for the interpolation. This is the issue with 4818.",
    "created_at": "2008-12-17T07:48:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4752#issuecomment-35962",
    "user": "jkantor"
}
```

2nd patch applied on top of first adds a doctest to demonstrate segfault does not occur it just catches the exception thrown.

Also I added a check that there are more than three points which is required for the interpolation. This is the issue with 4818.



---

archive/issue_comments_035963.json:
```json
{
    "body": "Attachment [list_plot_patch_2.patch](tarball://root/attachments/some-uuid/ticket4752/list_plot_patch_2.patch) by jkantor created at 2008-12-17 07:49:10",
    "created_at": "2008-12-17T07:49:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4752#issuecomment-35963",
    "user": "jkantor"
}
```

Attachment [list_plot_patch_2.patch](tarball://root/attachments/some-uuid/ticket4752/list_plot_patch_2.patch) by jkantor created at 2008-12-17 07:49:10



---

archive/issue_comments_035964.json:
```json
{
    "body": "REFEREE REPORT:\n\nThere are two problems:\n\n1. A typo: \"differet\"\n\n2. The illustrations of exceptions being raised are formatted incorrectly.  There's are thousands of examples in the sage doctests.  Find one and copy it.",
    "created_at": "2008-12-17T07:57:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4752#issuecomment-35964",
    "user": "@williamstein"
}
```

REFEREE REPORT:

There are two problems:

1. A typo: "differet"

2. The illustrations of exceptions being raised are formatted incorrectly.  There's are thousands of examples in the sage doctests.  Find one and copy it.



---

archive/issue_comments_035965.json:
```json
{
    "body": "addresses referree comments rebased against 3.2.3",
    "created_at": "2009-01-23T04:10:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4752#issuecomment-35965",
    "user": "jkantor"
}
```

addresses referree comments rebased against 3.2.3



---

archive/issue_comments_035966.json:
```json
{
    "body": "Attachment [4752_patch.patch](tarball://root/attachments/some-uuid/ticket4752/4752_patch.patch) by jkantor created at 2009-01-23 04:11:15\n\nThe 4752_patch fixes the issues raised by the referee and is rebased against 3.2.3",
    "created_at": "2009-01-23T04:11:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4752#issuecomment-35966",
    "user": "jkantor"
}
```

Attachment [4752_patch.patch](tarball://root/attachments/some-uuid/ticket4752/4752_patch.patch) by jkantor created at 2009-01-23 04:11:15

The 4752_patch fixes the issues raised by the referee and is rebased against 3.2.3



---

archive/issue_comments_035967.json:
```json
{
    "body": "William,\n\ncan you re-review this patch? Josh updated it, but I guess he forgot to change the status.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-02T04:21:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4752#issuecomment-35967",
    "user": "mabshoff"
}
```

William,

can you re-review this patch? Josh updated it, but I guess he forgot to change the status.

Cheers,

Michael



---

archive/issue_comments_035968.json:
```json
{
    "body": "This one ought to go into 3.3, so I am moving it.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-07T06:42:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4752#issuecomment-35968",
    "user": "mabshoff"
}
```

This one ought to go into 3.3, so I am moving it.

Cheers,

Michael



---

archive/issue_comments_035969.json:
```json
{
    "body": "Oops, 3.3 now.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-07T06:42:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4752#issuecomment-35969",
    "user": "mabshoff"
}
```

Oops, 3.3 now.

Cheers,

Michael



---

archive/issue_comments_035970.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-02-08T23:27:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4752#issuecomment-35970",
    "user": "@mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_035971.json:
```json
{
    "body": "4752_patch.patch needs to be rebased since the first hunk failed:\n\n```\nsage-3.3.rc0/devel/sage$ patch -p1 < trac_4752_patch.patch \npatching file sage/plot/plot3d/list_plot3d.py\nHunk #1 FAILED at 98.\nHunk #2 succeeded at 179 (offset 10 lines).\nHunk #3 succeeded at 199 (offset 10 lines).\n1 out of 3 hunks FAILED -- saving rejects to file sage/plot/plot3d/list_plot3d.py.rej\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2009-02-09T08:06:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4752#issuecomment-35971",
    "user": "mabshoff"
}
```

4752_patch.patch needs to be rebased since the first hunk failed:

```
sage-3.3.rc0/devel/sage$ patch -p1 < trac_4752_patch.patch 
patching file sage/plot/plot3d/list_plot3d.py
Hunk #1 FAILED at 98.
Hunk #2 succeeded at 179 (offset 10 lines).
Hunk #3 succeeded at 199 (offset 10 lines).
1 out of 3 hunks FAILED -- saving rejects to file sage/plot/plot3d/list_plot3d.py.rej
```


Cheers,

Michael



---

archive/issue_comments_035972.json:
```json
{
    "body": "Attachment [trac_4752_patch.2.patch](tarball://root/attachments/some-uuid/ticket4752/trac_4752_patch.2.patch) by mabshoff created at 2009-02-09 08:13:48\n\nThis is a rebase version of Josh's patch. The problem was trivial since only doctests had been added to the docstring. Apply only this patch.",
    "created_at": "2009-02-09T08:13:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4752#issuecomment-35972",
    "user": "mabshoff"
}
```

Attachment [trac_4752_patch.2.patch](tarball://root/attachments/some-uuid/ticket4752/trac_4752_patch.2.patch) by mabshoff created at 2009-02-09 08:13:48

This is a rebase version of Josh's patch. The problem was trivial since only doctests had been added to the docstring. Apply only this patch.



---

archive/issue_comments_035973.json:
```json
{
    "body": "We need a doctest fix for this one:\n\n```\nsage -t -long \"devel/sage/sage/plot/plot3d/list_plot3d.py\"  \n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.3.rc0/devel/sage/sage/plot/plot3d/list_plot3d.py\", line 119:\n    sage: show(list_plot3d(pts,interpolation_type='nn'))\nExpected:\n    Traceback (most recent call last):\n    ...\n    ValueError: We need at least 3 points to perform the interpolation\nGot nothing\n**********************************************************************\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2009-02-09T08:20:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4752#issuecomment-35973",
    "user": "mabshoff"
}
```

We need a doctest fix for this one:

```
sage -t -long "devel/sage/sage/plot/plot3d/list_plot3d.py"  
**********************************************************************
File "/scratch/mabshoff/sage-3.3.rc0/devel/sage/sage/plot/plot3d/list_plot3d.py", line 119:
    sage: show(list_plot3d(pts,interpolation_type='nn'))
Expected:
    Traceback (most recent call last):
    ...
    ValueError: We need at least 3 points to perform the interpolation
Got nothing
**********************************************************************
```


Cheers,

Michael



---

archive/issue_comments_035974.json:
```json
{
    "body": "The error message about needing at least 3 points occurs in the function list_plot3d_tuples, which isn't even called unless there are at least 3 points.  So I just deleted this part of the doctest.  Hope that's okay.",
    "created_at": "2009-02-12T04:00:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4752#issuecomment-35974",
    "user": "@jhpalmieri"
}
```

The error message about needing at least 3 points occurs in the function list_plot3d_tuples, which isn't even called unless there are at least 3 points.  So I just deleted this part of the doctest.  Hope that's okay.



---

archive/issue_comments_035975.json:
```json
{
    "body": "Never mind, here's a patch which keeps the doctest.  This one is better, so I'm replacing the old one.  It also fixes some typos and such in the old docstring.",
    "created_at": "2009-02-12T06:08:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4752#issuecomment-35975",
    "user": "@jhpalmieri"
}
```

Never mind, here's a patch which keeps the doctest.  This one is better, so I'm replacing the old one.  It also fixes some typos and such in the old docstring.



---

archive/issue_comments_035976.json:
```json
{
    "body": "Attachment [4752-doctest.patch](tarball://root/attachments/some-uuid/ticket4752/4752-doctest.patch) by @jhpalmieri created at 2009-02-12 06:08:15\n\napply this on top of trac_4752_patch.2.patch",
    "created_at": "2009-02-12T06:08:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4752#issuecomment-35976",
    "user": "@jhpalmieri"
}
```

Attachment [4752-doctest.patch](tarball://root/attachments/some-uuid/ticket4752/4752-doctest.patch) by @jhpalmieri created at 2009-02-12 06:08:15

apply this on top of trac_4752_patch.2.patch



---

archive/issue_comments_035977.json:
```json
{
    "body": "4752-doctest.patch looks good to me. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-14T02:32:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4752#issuecomment-35977",
    "user": "mabshoff"
}
```

4752-doctest.patch looks good to me. Positive review.

Cheers,

Michael



---

archive/issue_comments_035978.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-14T09:15:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4752#issuecomment-35978",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_035979.json:
```json
{
    "body": "Merged  trac_4752_patch.2.patch and 4752-doctest.patch in Sage 3.3.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-14T09:15:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4752#issuecomment-35979",
    "user": "mabshoff"
}
```

Merged  trac_4752_patch.2.patch and 4752-doctest.patch in Sage 3.3.rc1.

Cheers,

Michael
