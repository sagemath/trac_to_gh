# Issue 2770: plot_region function

archive/issues_002770.json:
```json
{
    "body": "Assignee: was\n\nIt would be great to have a plot_region function which would plot a region where a system of equations/inequalities were true.\n\nHere is an initial version:\n\n\n```\ndef plot_region(funcs, var1_range, var2_range, plot_points=400, **kwds):\n    if not isinstance(funcs, (list, tuple)):\n        funcs = [funcs]\n    hvar, hmin, hmax = var1_range\n    vvar, vmin, vmax = var2_range\n    funcs = prod([f._fast_float_(\"%r\"%hvar, \"%r\"%vvar) for f in funcs])\n    return contour_plot(funcs, var1_range, var2_range, plot_points=plot_points,**kwds)\n```\n\n\nThis uses an idea from cwitty (to use contour_plot) and the patch from #2768.  A screenshot is attached below.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2770\n\n",
    "created_at": "2008-04-02T07:49:40Z",
    "labels": [
        "graphics",
        "major",
        "enhancement"
    ],
    "title": "plot_region function",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2770",
    "user": "jason"
}
```
Assignee: was

It would be great to have a plot_region function which would plot a region where a system of equations/inequalities were true.

Here is an initial version:


```
def plot_region(funcs, var1_range, var2_range, plot_points=400, **kwds):
    if not isinstance(funcs, (list, tuple)):
        funcs = [funcs]
    hvar, hmin, hmax = var1_range
    vvar, vmin, vmax = var2_range
    funcs = prod([f._fast_float_("%r"%hvar, "%r"%vvar) for f in funcs])
    return contour_plot(funcs, var1_range, var2_range, plot_points=plot_points,**kwds)
```


This uses an idea from cwitty (to use contour_plot) and the patch from #2768.  A screenshot is attached below.

Issue created by migration from https://trac.sagemath.org/ticket/2770





---

archive/issue_comments_019030.json:
```json
{
    "body": "Changing assignee from was to abergeron.",
    "created_at": "2008-12-28T01:11:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2770#issuecomment-19030",
    "user": "abergeron"
}
```

Changing assignee from was to abergeron.



---

archive/issue_comments_019031.json:
```json
{
    "body": "Attachment\n\nIf you want to try out part1, you need to apply the patch at #4884.  At the moment it support only one function.\n\nMultiple function support is coming in part2.",
    "created_at": "2008-12-28T01:11:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2770#issuecomment-19031",
    "user": "abergeron"
}
```

Attachment

If you want to try out part1, you need to apply the patch at #4884.  At the moment it support only one function.

Multiple function support is coming in part2.



---

archive/issue_comments_019032.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-12-28T20:47:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2770#issuecomment-19032",
    "user": "abergeron"
}
```

Changing status from new to assigned.



---

archive/issue_comments_019033.json:
```json
{
    "body": "Attachment\n\nNow it is complete, apply both patches and the patch at #4884 to test.\n\nThe example in the screenshot should work, but is rather ugly at the default plot_points setting, try at plot_points=200 to see it looking good.",
    "created_at": "2008-12-28T20:47:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2770#issuecomment-19033",
    "user": "abergeron"
}
```

Attachment

Now it is complete, apply both patches and the patch at #4884 to test.

The example in the screenshot should work, but is rather ugly at the default plot_points setting, try at plot_points=200 to see it looking good.



---

archive/issue_comments_019034.json:
```json
{
    "body": "Since there is heavy discussion at #4884 I will wait until that settles to update this patch to work with whatever is decided upon.",
    "created_at": "2008-12-29T20:50:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2770#issuecomment-19034",
    "user": "abergeron"
}
```

Since there is heavy discussion at #4884 I will wait until that settles to update this patch to work with whatever is decided upon.



---

archive/issue_comments_019035.json:
```json
{
    "body": "#4884 is settled",
    "created_at": "2008-12-30T01:51:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2770#issuecomment-19035",
    "user": "abergeron"
}
```

#4884 is settled



---

archive/issue_comments_019036.json:
```json
{
    "body": "This has some odd behavior which I hope the author could please comment on:\n\nThis looks good:\n\n```\nsage: P1 = region_plot(cos(x^2+y^2) <= 0, (-3, 3), (-3, 3), incol='green', bordercol='red')\nsage: show(P1)\n```\n\n\nThis looks very odd (wrong but maybe the algorithm just needs more points?):\n\n```\nsage: P2 = region_plot(cos(x^2+y^2) <= 0, (-30, 30), (-30, 30), incol='green', bordercol='red')\nsage: show(P2)\n```\n\n\nThis looks plain wrong (and I think we have provided enough points:-):\n\n\n```\nsage: P3 = region_plot(cos(x^2+y^2) <= 0, (-30, 30), (-30, 30), incol='green', bordercol='red', plot_points=1000)\nsage: show(P3)\n```\n",
    "created_at": "2008-12-30T05:22:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2770#issuecomment-19036",
    "user": "wdj"
}
```

This has some odd behavior which I hope the author could please comment on:

This looks good:

```
sage: P1 = region_plot(cos(x^2+y^2) <= 0, (-3, 3), (-3, 3), incol='green', bordercol='red')
sage: show(P1)
```


This looks very odd (wrong but maybe the algorithm just needs more points?):

```
sage: P2 = region_plot(cos(x^2+y^2) <= 0, (-30, 30), (-30, 30), incol='green', bordercol='red')
sage: show(P2)
```


This looks plain wrong (and I think we have provided enough points:-):


```
sage: P3 = region_plot(cos(x^2+y^2) <= 0, (-30, 30), (-30, 30), incol='green', bordercol='red', plot_points=1000)
sage: show(P3)
```




---

archive/issue_comments_019037.json:
```json
{
    "body": "Means to add to the review above:\n\nIf you first apply the first patch at #4884 (but not the second), then the two patches above apply cleanly to 3.2.2.",
    "created_at": "2008-12-30T05:24:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2770#issuecomment-19037",
    "user": "wdj"
}
```

Means to add to the review above:

If you first apply the first patch at #4884 (but not the second), then the two patches above apply cleanly to 3.2.2.



---

archive/issue_comments_019038.json:
```json
{
    "body": "The first very wrong case is really because there is not enough data to interpolate properly.\n\nIn the second case it's too much of a good thing.  There is too much data and every insignificant contour line gets plotted and since they have a minimum width you get a red picture.\n\nFor this example, plot_points=400 looks much more reasonable.",
    "created_at": "2008-12-30T05:57:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2770#issuecomment-19038",
    "user": "abergeron"
}
```

The first very wrong case is really because there is not enough data to interpolate properly.

In the second case it's too much of a good thing.  There is too much data and every insignificant contour line gets plotted and since they have a minimum width you get a red picture.

For this example, plot_points=400 looks much more reasonable.



---

archive/issue_comments_019039.json:
```json
{
    "body": "Okay, thanks for that explanation. This is a useful patch.\n\nMy impression is that if it can't be easily fixed, then at least it should be documented how to adjust the parameters to get proper behaviour. I'm guessing that the people who will use this patch are students and teachers, so the more detailed examples the better:-) Does this seem reasonable?\n\nWith that's I'd be prepared to give it a positive review.\n\nOther cool examples you could include:\n\n```\nsage: region_plot(x*(x-1)*(x+1)+y^2<0, (-3, 2), (-3, 3), incol='lightblue', bordercol='gray', plot_points=400)\nsage: region_plot([x*(x-1)*(x+1)+y^2<0, x>-1], (-3, 2), (-3, 3), incol='lightblue', bordercol='gray', plot_points=400)\n```\n\nAnd one similar to Jason's:\n\n```\nsage: P = region_plot([x^2+y^2<4, x>-1], (-2, 2), (-2, 2), incol='lightblue', bordercol='gray', plot_points=400)\nsage: P.show(aspect_ratio=1)\n```\n\n(I know you have \n\n\n```\nregion_plot([x^2+y^2<1, x<y], (-2,2), (-2,2)) \n```\n\nbut it looks odd without the aspect ratio set.)\n\nDo these seem reasonable Arnaud?",
    "created_at": "2008-12-30T06:52:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2770#issuecomment-19039",
    "user": "wdj"
}
```

Okay, thanks for that explanation. This is a useful patch.

My impression is that if it can't be easily fixed, then at least it should be documented how to adjust the parameters to get proper behaviour. I'm guessing that the people who will use this patch are students and teachers, so the more detailed examples the better:-) Does this seem reasonable?

With that's I'd be prepared to give it a positive review.

Other cool examples you could include:

```
sage: region_plot(x*(x-1)*(x+1)+y^2<0, (-3, 2), (-3, 3), incol='lightblue', bordercol='gray', plot_points=400)
sage: region_plot([x*(x-1)*(x+1)+y^2<0, x>-1], (-3, 2), (-3, 3), incol='lightblue', bordercol='gray', plot_points=400)
```

And one similar to Jason's:

```
sage: P = region_plot([x^2+y^2<4, x>-1], (-2, 2), (-2, 2), incol='lightblue', bordercol='gray', plot_points=400)
sage: P.show(aspect_ratio=1)
```

(I know you have 


```
region_plot([x^2+y^2<1, x<y], (-2,2), (-2,2)) 
```

but it looks odd without the aspect ratio set.)

Do these seem reasonable Arnaud?



---

archive/issue_comments_019040.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-12-30T19:16:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2770#issuecomment-19040",
    "user": "abergeron"
}
```

Attachment



---

archive/issue_comments_019041.json:
```json
{
    "body": "I agree with more examples.  I just did not have a huge inspiration for them.\n\nThe last patch adds your suggested examples.",
    "created_at": "2008-12-30T19:17:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2770#issuecomment-19041",
    "user": "abergeron"
}
```

I agree with more examples.  I just did not have a huge inspiration for them.

The last patch adds your suggested examples.



---

archive/issue_comments_019042.json:
```json
{
    "body": "The patches applied fine but the test timed out on my machine (amd64 ubuntu 8.10). So, positive review for the patch but I could not do the test using sage -t. (The examples seemed to work okay though.)",
    "created_at": "2008-12-30T23:18:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2770#issuecomment-19042",
    "user": "wdj"
}
```

The patches applied fine but the test timed out on my machine (amd64 ubuntu 8.10). So, positive review for the patch but I could not do the test using sage -t. (The examples seemed to work okay though.)



---

archive/issue_comments_019043.json:
```json
{
    "body": "This is a slightly rebased version of Arnaud Bergeron's patch",
    "created_at": "2009-01-12T01:59:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2770#issuecomment-19043",
    "user": "mabshoff"
}
```

This is a slightly rebased version of Arnaud Bergeron's patch



---

archive/issue_comments_019044.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-12T02:00:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2770#issuecomment-19044",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_019045.json:
```json
{
    "body": "Attachment\n\nMerged all three patches in Sage 3.3.alpha0",
    "created_at": "2009-01-12T02:00:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2770#issuecomment-19045",
    "user": "mabshoff"
}
```

Attachment

Merged all three patches in Sage 3.3.alpha0
