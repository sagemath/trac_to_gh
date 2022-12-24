# Issue 4462: contour_plot defaults changed to fill, affects implicit_plot

archive/issues_004462.json:
```json
{
    "body": "Assignee: was\n\nIn Sage 3.1.1,\n\n```\nimplicit_plot(x^2+y^2-1,(x,-1.1,1.1),(y,-1.1,1.1),plot_points=100).show(aspect_ratio=1)\n```\n\nproduces a very nice circle.\n\nIn Sage 3.1.4, the same code produces a filled-in disc. Likewise, implicit_plot tries to fill in all curves;\n\n```\nimplicit_plot(5*x^4-x^2-y^2,(x,-5,5),(y,-5,5))\n```\n\nlooks odd.\n\nThe cause is contour_plot (called by implicit_plot): the default for the fill option is True. Feeding fill=False to implicit_plot produces the desired behavior:\n\n```\nimplicit_plot(x^2+y^2-1,(x,-1.1,1.1),(y,-1.1,1.1),plot_points=100,fill=False).show(aspect_ratio=1)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4462\n\n",
    "created_at": "2008-11-07T16:48:30Z",
    "labels": [
        "graphics",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "contour_plot defaults changed to fill, affects implicit_plot",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4462",
    "user": "john_perry"
}
```
Assignee: was

In Sage 3.1.1,

```
implicit_plot(x^2+y^2-1,(x,-1.1,1.1),(y,-1.1,1.1),plot_points=100).show(aspect_ratio=1)
```

produces a very nice circle.

In Sage 3.1.4, the same code produces a filled-in disc. Likewise, implicit_plot tries to fill in all curves;

```
implicit_plot(5*x^4-x^2-y^2,(x,-5,5),(y,-5,5))
```

looks odd.

The cause is contour_plot (called by implicit_plot): the default for the fill option is True. Feeding fill=False to implicit_plot produces the desired behavior:

```
implicit_plot(x^2+y^2-1,(x,-1.1,1.1),(y,-1.1,1.1),plot_points=100,fill=False).show(aspect_ratio=1)
```


Issue created by migration from https://trac.sagemath.org/ticket/4462





---

archive/issue_comments_032944.json:
```json
{
    "body": "Attachment [circle_sage3.1.1.png](tarball://root/attachments/some-uuid/ticket4462/circle_sage3.1.1.png) by john_perry created at 2008-11-07 16:49:03\n\nresult of implicit_plot in sage 3.1.1",
    "created_at": "2008-11-07T16:49:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4462",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4462#issuecomment-32944",
    "user": "john_perry"
}
```

Attachment [circle_sage3.1.1.png](tarball://root/attachments/some-uuid/ticket4462/circle_sage3.1.1.png) by john_perry created at 2008-11-07 16:49:03

result of implicit_plot in sage 3.1.1



---

archive/issue_comments_032945.json:
```json
{
    "body": "result of implicit_plot in sage 3.1.4",
    "created_at": "2008-11-07T16:49:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4462",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4462#issuecomment-32945",
    "user": "john_perry"
}
```

result of implicit_plot in sage 3.1.4



---

archive/issue_comments_032946.json:
```json
{
    "body": "Attachment [circle_sage3.1.4.png](tarball://root/attachments/some-uuid/ticket4462/circle_sage3.1.4.png) by john_perry created at 2008-11-07 16:57:19\n\nThe fix is easy: change line 2926 of site-packages/sage/plot/plot.py, which currently reads\n\n```\n@options(contours=(0,0))\n```\n\nto\n\n```\n@options(contours=(0,0),fill=False)\n```\n",
    "created_at": "2008-11-07T16:57:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4462",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4462#issuecomment-32946",
    "user": "john_perry"
}
```

Attachment [circle_sage3.1.4.png](tarball://root/attachments/some-uuid/ticket4462/circle_sage3.1.4.png) by john_perry created at 2008-11-07 16:57:19

The fix is easy: change line 2926 of site-packages/sage/plot/plot.py, which currently reads

```
@options(contours=(0,0))
```

to

```
@options(contours=(0,0),fill=False)
```




---

archive/issue_comments_032947.json:
```json
{
    "body": "It looks like #4201 forgot to override that option of contour plot.  That's where the change was made.\n\nI refereed that patch; my bad.",
    "created_at": "2008-11-07T17:26:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4462",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4462#issuecomment-32947",
    "user": "jason"
}
```

It looks like #4201 forgot to override that option of contour plot.  That's where the change was made.

I refereed that patch; my bad.



---

archive/issue_comments_032948.json:
```json
{
    "body": "Attachment [implicit-plot-no-fill.patch](tarball://root/attachments/some-uuid/ticket4462/implicit-plot-no-fill.patch) by jason created at 2008-11-07 17:33:24",
    "created_at": "2008-11-07T17:33:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4462",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4462#issuecomment-32948",
    "user": "jason"
}
```

Attachment [implicit-plot-no-fill.patch](tarball://root/attachments/some-uuid/ticket4462/implicit-plot-no-fill.patch) by jason created at 2008-11-07 17:33:24



---

archive/issue_comments_032949.json:
```json
{
    "body": "John Perry should also receive credit for the patch, since he gave the actual fix in his comment.  I added documentation as well.",
    "created_at": "2008-11-07T18:34:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4462",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4462#issuecomment-32949",
    "user": "jason"
}
```

John Perry should also receive credit for the patch, since he gave the actual fix in his comment.  I added documentation as well.



---

archive/issue_comments_032950.json:
```json
{
    "body": "Looks good.",
    "created_at": "2008-11-08T05:28:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4462",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4462#issuecomment-32950",
    "user": "mhansen"
}
```

Looks good.



---

archive/issue_comments_032951.json:
```json
{
    "body": "Merged implicit-plot-no-fill.patch in Sage 3.2.rc0",
    "created_at": "2008-11-08T07:13:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4462",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4462#issuecomment-32951",
    "user": "mabshoff"
}
```

Merged implicit-plot-no-fill.patch in Sage 3.2.rc0



---

archive/issue_comments_032952.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-08T07:13:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4462",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4462#issuecomment-32952",
    "user": "mabshoff"
}
```

Resolution: fixed
