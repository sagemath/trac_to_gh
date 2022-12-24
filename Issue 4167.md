# Issue 4167: wrong colors cornercase in list_plot

archive/issues_004167.json:
```json
{
    "body": "Assignee: was\n\nCC:  wavetable@gmx.at\n\n[published example of this bug](https://sage.math.washington.edu:8101/home/pub/27/)\n\nPlotting \n\n\n```\nx=srange(0, 1.1, 0.5)\nw=srange(0, 1.1, 0.5)\nxw = zip(x,w)\nlist_plot(xw, rgbcolor=(0.8, 0.8, 0), pointsize=40)\n```\n\nproduces blue and brown dots.\n\nPlotting\n\n```\nx=srange(0, 2.1, 0.5)\nw=srange(0, 2.1, 0.5)\nxw = zip(x,w)\nlist_plot(xw, rgbcolor=(0.8, 0.8, 0), pointsize=40)\n```\n\n\n4 yellow ones.\n\noriginal report:\n\n```\nlist_plot with a list of len == 3 produces 'random' point colors.\nit works with len != 3.\n\ni've created a worksheet on the milnix server, that shows the problem.\nhttp://75.75.6.176/home/pub/17\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4167\n\n",
    "created_at": "2008-09-22T12:05:05Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "wrong colors cornercase in list_plot",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4167",
    "user": "schilly"
}
```
Assignee: was

CC:  wavetable@gmx.at

[published example of this bug](https://sage.math.washington.edu:8101/home/pub/27/)

Plotting 


```
x=srange(0, 1.1, 0.5)
w=srange(0, 1.1, 0.5)
xw = zip(x,w)
list_plot(xw, rgbcolor=(0.8, 0.8, 0), pointsize=40)
```

produces blue and brown dots.

Plotting

```
x=srange(0, 2.1, 0.5)
w=srange(0, 2.1, 0.5)
xw = zip(x,w)
list_plot(xw, rgbcolor=(0.8, 0.8, 0), pointsize=40)
```


4 yellow ones.

original report:

```
list_plot with a list of len == 3 produces 'random' point colors.
it works with len != 3.

i've created a worksheet on the milnix server, that shows the problem.
http://75.75.6.176/home/pub/17
```


Issue created by migration from https://trac.sagemath.org/ticket/4167





---

archive/issue_comments_030249.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-09-22T22:56:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4167#issuecomment-30249",
    "user": "mabshoff"
}
```

Resolution: duplicate



---

archive/issue_comments_030250.json:
```json
{
    "body": "This is a dupe of #2076 which has a patch and will likely be in 3.1.3.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-22T22:56:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4167#issuecomment-30250",
    "user": "mabshoff"
}
```

This is a dupe of #2076 which has a patch and will likely be in 3.1.3.

Cheers,

Michael



---

archive/issue_comments_030251.json:
```json
{
    "body": "FYI, with the patch at #2076, both of the above examples correctly produce yellow dots.",
    "created_at": "2008-09-23T00:48:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4167#issuecomment-30251",
    "user": "jason"
}
```

FYI, with the patch at #2076, both of the above examples correctly produce yellow dots.
