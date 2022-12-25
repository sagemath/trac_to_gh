# Issue 5221: default cmap for contour plot makes last contour line invisible when fill=False

archive/issues_005221.json:
```json
{
    "body": "Assignee: @williamstein\n\nExamine the output of \n\n\n```\nvar('x,y')\ncontour_plot(x-y^2,(x,-5,5),(y,-3,3),contours=[-4,0,1], fill=False)\n```\n\n\n\nThe last contour line (level curve at z=1) is invisible because the default cmap makes it white.  Compare that to a different color map:\n\n\n```\nvar('x,y')\ncontour_plot(x-y^2,(x,-5,5),(y,-3,3),contours=[-4,0,1],cmap='winter',fill=False)\n```\n\n\nWe should make the default cmap something less confusing when fill=False.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5221\n\n",
    "created_at": "2009-02-09T16:12:04Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "default cmap for contour plot makes last contour line invisible when fill=False",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5221",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

Examine the output of 


```
var('x,y')
contour_plot(x-y^2,(x,-5,5),(y,-3,3),contours=[-4,0,1], fill=False)
```



The last contour line (level curve at z=1) is invisible because the default cmap makes it white.  Compare that to a different color map:


```
var('x,y')
contour_plot(x-y^2,(x,-5,5),(y,-3,3),contours=[-4,0,1],cmap='winter',fill=False)
```


We should make the default cmap something less confusing when fill=False.


Issue created by migration from https://trac.sagemath.org/ticket/5221





---

archive/issue_comments_039938.json:
```json
{
    "body": "As it turns out, no cmap with any better visibility is any better - many of them have white as one of the options.  So this patch creates a custom cmap which is almost the same as 'gray' for the situation where fill is False, a cmap is not specified, but there are a specific number of contours (or exact contours) specified.\n\nNote this patch depends on the patch at #5145.",
    "created_at": "2009-08-27T03:08:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5221#issuecomment-39938",
    "user": "https://github.com/kcrisman"
}
```

As it turns out, no cmap with any better visibility is any better - many of them have white as one of the options.  So this patch creates a custom cmap which is almost the same as 'gray' for the situation where fill is False, a cmap is not specified, but there are a specific number of contours (or exact contours) specified.

Note this patch depends on the patch at #5145.



---

archive/issue_comments_039939.json:
```json
{
    "body": "Thanks for the patch!\n\nI think this patch needs to be rebased after #5448.  The `@`options decorator for contour_plot is changed in that patch.",
    "created_at": "2009-09-10T15:24:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5221#issuecomment-39939",
    "user": "https://github.com/jasongrout"
}
```

Thanks for the patch!

I think this patch needs to be rebased after #5448.  The `@`options decorator for contour_plot is changed in that patch.



---

archive/issue_comments_039940.json:
```json
{
    "body": "Based on 4.1.1 and #5448 and #5145",
    "created_at": "2009-09-10T15:47:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5221#issuecomment-39940",
    "user": "https://github.com/kcrisman"
}
```

Based on 4.1.1 and #5448 and #5145



---

archive/issue_comments_039941.json:
```json
{
    "body": "Attachment [trac_5221-contour-plot-default-cmap.patch](tarball://root/attachments/some-uuid/ticket5221/trac_5221-contour-plot-default-cmap.patch) by @kcrisman created at 2009-09-10 15:47:11\n\nTry this.",
    "created_at": "2009-09-10T15:47:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5221#issuecomment-39941",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_5221-contour-plot-default-cmap.patch](tarball://root/attachments/some-uuid/ticket5221/trac_5221-contour-plot-default-cmap.patch) by @kcrisman created at 2009-09-10 15:47:11

Try this.



---

archive/issue_comments_039942.json:
```json
{
    "body": "Very nice!",
    "created_at": "2009-09-22T21:23:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5221#issuecomment-39942",
    "user": "https://github.com/jasongrout"
}
```

Very nice!



---

archive/issue_comments_039943.json:
```json
{
    "body": "(generally, you should do: \"if 'cmap' in options\", rather than \"options.has_key('cmap')\".",
    "created_at": "2009-09-22T21:26:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5221#issuecomment-39943",
    "user": "https://github.com/jasongrout"
}
```

(generally, you should do: "if 'cmap' in options", rather than "options.has_key('cmap')".



---

archive/issue_comments_039944.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-23T00:21:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5221#issuecomment-39944",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_039945.json:
```json
{
    "body": "There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.",
    "created_at": "2009-09-27T09:41:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5221#issuecomment-39945",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
