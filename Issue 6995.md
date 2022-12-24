# Issue 6995: plotting specific contour lines should shade values above/below the extreme contour values

archive/issues_006995.json:
```json
{
    "body": "Assignee: was\n\nCC:  kcrisman\n\nNotice that this plot is mostly white, but the white space represents two different values---one is above the top contour, the other is below the bottom contour.\n\nWe ought to make it so that stuff above/below the requested contours is shaded appropriately.\n\n\n```\nvar('x,y')\ncontour_plot(x-y^2,(x,-5,5),(y,-3,3),contours=[-4,0,1])\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6995\n\n",
    "created_at": "2009-09-22T21:32:13Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "plotting specific contour lines should shade values above/below the extreme contour values",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6995",
    "user": "jason"
}
```
Assignee: was

CC:  kcrisman

Notice that this plot is mostly white, but the white space represents two different values---one is above the top contour, the other is below the bottom contour.

We ought to make it so that stuff above/below the requested contours is shaded appropriately.


```
var('x,y')
contour_plot(x-y^2,(x,-5,5),(y,-3,3),contours=[-4,0,1])
```



Issue created by migration from https://trac.sagemath.org/ticket/6995





---

archive/issue_comments_057856.json:
```json
{
    "body": "I wonder if #5221 fixes this.  I don't have an up-to-date alpha to test this, though.",
    "created_at": "2009-10-12T18:24:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6995",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6995#issuecomment-57856",
    "user": "jason"
}
```

I wonder if #5221 fixes this.  I don't have an up-to-date alpha to test this, though.



---

archive/issue_comments_057857.json:
```json
{
    "body": "Attachment [trac-6995-contour-extremes.patch](tarball://root/attachments/some-uuid/ticket6995/trac-6995-contour-extremes.patch) by jason created at 2009-11-10 17:28:26",
    "created_at": "2009-11-10T17:28:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6995",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6995#issuecomment-57857",
    "user": "jason"
}
```

Attachment [trac-6995-contour-extremes.patch](tarball://root/attachments/some-uuid/ticket6995/trac-6995-contour-extremes.patch) by jason created at 2009-11-10 17:28:26



---

archive/issue_comments_057858.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-10T17:28:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6995",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6995#issuecomment-57858",
    "user": "jason"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_057859.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-10T19:07:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6995",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6995#issuecomment-57859",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_057860.json:
```json
{
    "body": "Positive review.  I wonder if this is also the 'right' way to have fixed #5221, since you mention that ticket? See [this link](http://matplotlib.sourceforge.net/api/pyplot_api.html?highlight=contourf#matplotlib.pyplot.contourf).\n\nNote to release manager: this depends on #4898.",
    "created_at": "2009-11-10T19:07:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6995",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6995#issuecomment-57860",
    "user": "kcrisman"
}
```

Positive review.  I wonder if this is also the 'right' way to have fixed #5221, since you mention that ticket? See [this link](http://matplotlib.sourceforge.net/api/pyplot_api.html?highlight=contourf#matplotlib.pyplot.contourf).

Note to release manager: this depends on #4898.



---

archive/issue_comments_057861.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-12T06:57:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6995",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6995#issuecomment-57861",
    "user": "mhansen"
}
```

Resolution: fixed
