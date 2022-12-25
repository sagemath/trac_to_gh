# Issue 5145: increase default plot_points value for contour_plot

archive/issues_005145.json:
```json
{
    "body": "Assignee: tbd\n\nMotivation: Somewhat regularly on sage-support we get emails like this:\n\n\n```\nHi everyone,\n\nI run into a very strange problem, that looks like critical to me.\nBasically, I plot two functions that I know must be tangent at a given\npoint, and they are not.\n\nFirst, the code:\n\nx,y=var('x,y')\nutility=y*x^2\nbudget = 24-x\ncp=contour_plot(utility,(x,0,24),(y,\n0,24),fill=False,cmap='cool',contours=(100,1000,2048,2700,3500))\nbp=plot(budget,(x,0,24),color='red')\ncp+bp\n\nNow, the plot that comes after calling 'cp+bp' must have the following\nproperty: the straight red line must be tangent to the contour of the\nutility function evaluated at level utility=2048; and they must be\ntangent at the point (16,8). In my system (Sage 3.2.3 on OpenSuse11.1)\nthey are NOT tangent; in fact, the sage plot indicates tangency at a\nlower level, ~1820.\n...\n- Or else is it a calculation problem on the part of sage? I'd find\nthis absolutely strange. And critical: I want to trust Sage to do the\ncalculations correctly.\n\nCan you reproduce it?\n\nThanks,\n```\n\n\nBut putting plot_points=200 fixes things.   Right now the default is a mere 25, which seems absurdly small.   I think we should change the default plot_points parameter.  It was very low, I think, because evaluation of symbolic expressions used to be slow -- now it's extremely fast -- so we should increase the default number of points to at least 200. \n\nIssue created by migration from https://trac.sagemath.org/ticket/5145\n\n",
    "created_at": "2009-01-31T15:19:12Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "increase default plot_points value for contour_plot",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5145",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd

Motivation: Somewhat regularly on sage-support we get emails like this:


```
Hi everyone,

I run into a very strange problem, that looks like critical to me.
Basically, I plot two functions that I know must be tangent at a given
point, and they are not.

First, the code:

x,y=var('x,y')
utility=y*x^2
budget = 24-x
cp=contour_plot(utility,(x,0,24),(y,
0,24),fill=False,cmap='cool',contours=(100,1000,2048,2700,3500))
bp=plot(budget,(x,0,24),color='red')
cp+bp

Now, the plot that comes after calling 'cp+bp' must have the following
property: the straight red line must be tangent to the contour of the
utility function evaluated at level utility=2048; and they must be
tangent at the point (16,8). In my system (Sage 3.2.3 on OpenSuse11.1)
they are NOT tangent; in fact, the sage plot indicates tangency at a
lower level, ~1820.
...
- Or else is it a calculation problem on the part of sage? I'd find
this absolutely strange. And critical: I want to trust Sage to do the
calculations correctly.

Can you reproduce it?

Thanks,
```


But putting plot_points=200 fixes things.   Right now the default is a mere 25, which seems absurdly small.   I think we should change the default plot_points parameter.  It was very low, I think, because evaluation of symbolic expressions used to be slow -- now it's extremely fast -- so we should increase the default number of points to at least 200. 

Issue created by migration from https://trac.sagemath.org/ticket/5145





---

archive/issue_comments_039281.json:
```json
{
    "body": "From the OP: \n\n```\nI second the idea of increaisng the default plot-points, at least to\n100. On my not so recent intel duo it took less than a second with\n200.\n```\n",
    "created_at": "2009-01-31T16:58:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5145#issuecomment-39281",
    "user": "https://github.com/williamstein"
}
```

From the OP: 

```
I second the idea of increaisng the default plot-points, at least to
100. On my not so recent intel duo it took less than a second with
200.
```




---

archive/issue_comments_039282.json:
```json
{
    "body": "Changing assignee from tbd to @williamstein.",
    "created_at": "2009-07-05T08:08:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5145#issuecomment-39282",
    "user": "https://github.com/loefflerd"
}
```

Changing assignee from tbd to @williamstein.



---

archive/issue_comments_039283.json:
```json
{
    "body": "This should be in \"graphics\" I guess.",
    "created_at": "2009-07-05T08:08:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5145#issuecomment-39283",
    "user": "https://github.com/loefflerd"
}
```

This should be in "graphics" I guess.



---

archive/issue_comments_039284.json:
```json
{
    "body": "Changing component from algebra to graphics.",
    "created_at": "2009-07-05T08:08:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5145#issuecomment-39284",
    "user": "https://github.com/loefflerd"
}
```

Changing component from algebra to graphics.



---

archive/issue_comments_039285.json:
```json
{
    "body": "This changes this to 100, except for implicit_plot, which is changed to 150 since it is usually used to see more detail.",
    "created_at": "2009-08-27T03:05:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5145#issuecomment-39285",
    "user": "https://github.com/kcrisman"
}
```

This changes this to 100, except for implicit_plot, which is changed to 150 since it is usually used to see more detail.



---

archive/issue_comments_039286.json:
```json
{
    "body": "Great work!  I'm glad to see this patch!\n\nThis needs to be rebased after #5448.  That patch changes the `@`options decorator for contour_plot, for example, and so there is a reject on applying this patch.",
    "created_at": "2009-09-10T15:23:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5145#issuecomment-39286",
    "user": "https://github.com/jasongrout"
}
```

Great work!  I'm glad to see this patch!

This needs to be rebased after #5448.  That patch changes the `@`options decorator for contour_plot, for example, and so there is a reject on applying this patch.



---

archive/issue_comments_039287.json:
```json
{
    "body": "Based on 4.1.1 and #5448",
    "created_at": "2009-09-10T15:45:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5145#issuecomment-39287",
    "user": "https://github.com/kcrisman"
}
```

Based on 4.1.1 and #5448



---

archive/issue_comments_039288.json:
```json
{
    "body": "Attachment [trac_5145-plot-points-default.patch](tarball://root/attachments/some-uuid/ticket5145/trac_5145-plot-points-default.patch) by @kcrisman created at 2009-09-10 15:46:05\n\nTry this.",
    "created_at": "2009-09-10T15:46:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5145#issuecomment-39288",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_5145-plot-points-default.patch](tarball://root/attachments/some-uuid/ticket5145/trac_5145-plot-points-default.patch) by @kcrisman created at 2009-09-10 15:46:05

Try this.



---

archive/issue_comments_039289.json:
```json
{
    "body": "The code looks good; passes doctests in the affected file.",
    "created_at": "2009-09-15T09:06:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5145#issuecomment-39289",
    "user": "https://github.com/jasongrout"
}
```

The code looks good; passes doctests in the affected file.



---

archive/issue_comments_039290.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-15T20:27:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5145#issuecomment-39290",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
