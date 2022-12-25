# Issue 8424: bounding box calculation doesn't handle NaN or infinity

archive/issues_008424.json:
```json
{
    "body": "Assignee: @jasongrout\n\nCC:  @robertwb @robert-marik drkirkby\n\nRobert Marik pointed out that there is a bug in the bounding box calculation of the following plot:\n\n```\nvar('y')\nplot3d(sqrt(sin(x)*sin(y)), (x,0,2*pi),(y,0,2*pi))\n```\n\nThe problem is that there are lots of NaNs generated in the evaluation of the plot, and these are not handled well by the bounding box calculation.\n\nThe attached patch fixes the issues in two of the three places the bounding box is calculated.  A third place is not touched in plot3d/transform.pyx, where I don't have time to make sure the fix is the right one and supply the necessary doctests.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8424\n\n",
    "closed_at": "2010-04-15T23:50:54Z",
    "created_at": "2010-03-02T19:14:58Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "bounding box calculation doesn't handle NaN or infinity",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8424",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @jasongrout

CC:  @robertwb @robert-marik drkirkby

Robert Marik pointed out that there is a bug in the bounding box calculation of the following plot:

```
var('y')
plot3d(sqrt(sin(x)*sin(y)), (x,0,2*pi),(y,0,2*pi))
```

The problem is that there are lots of NaNs generated in the evaluation of the plot, and these are not handled well by the bounding box calculation.

The attached patch fixes the issues in two of the three places the bounding box is calculated.  A third place is not touched in plot3d/transform.pyx, where I don't have time to make sure the fix is the right one and supply the necessary doctests.

Issue created by migration from https://trac.sagemath.org/ticket/8424





---

archive/issue_comments_075394.json:
```json
{
    "body": "Changing assignee from @williamstein to @jasongrout.",
    "created_at": "2010-03-02T19:21:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8424#issuecomment-75394",
    "user": "https://github.com/jasongrout"
}
```

Changing assignee from @williamstein to @jasongrout.



---

archive/issue_comments_075395.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-02T19:26:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8424#issuecomment-75395",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_075396.json:
```json
{
    "body": "Attachment [trac-8424-bounding-boxes.patch](tarball://root/attachments/some-uuid/ticket8424/trac-8424-bounding-boxes.patch) by @jasongrout created at 2010-03-04 02:25:39\n\nNew patch fixes one doctest.  Robert (either one! :), feel free to review this.\n\ndrkirkby: I use the INFINITY constant and the isfinite macro from math.h.  Does this pose a problem on Solaris?",
    "created_at": "2010-03-04T02:25:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8424#issuecomment-75396",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-8424-bounding-boxes.patch](tarball://root/attachments/some-uuid/ticket8424/trac-8424-bounding-boxes.patch) by @jasongrout created at 2010-03-04 02:25:39

New patch fixes one doctest.  Robert (either one! :), feel free to review this.

drkirkby: I use the INFINITY constant and the isfinite macro from math.h.  Does this pose a problem on Solaris?



---

archive/issue_comments_075397.json:
```json
{
    "body": "Works for me, installs fine, solves the problem, tests passed. \n\nWhen tested, I observed another (related, but probably independent) problem - #8433 \n\nDocumentation builds fine. Thanks for the patch, positive review!",
    "created_at": "2010-03-04T08:18:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8424#issuecomment-75397",
    "user": "https://github.com/robert-marik"
}
```

Works for me, installs fine, solves the problem, tests passed. 

When tested, I observed another (related, but probably independent) problem - #8433 

Documentation builds fine. Thanks for the patch, positive review!



---

archive/issue_comments_075398.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-04T08:18:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8424#issuecomment-75398",
    "user": "https://github.com/robert-marik"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_075399.json:
```json
{
    "body": "Hi Jason, \n\nThe macros isfinite() and isinf() are both defined in math.h, so the use of either of those would not present a problem. \n\nINFINITY is defined for C99 code, so I believe that as long as you specify -std=c99 as an option to gcc, then it will be ok. \n\nDave",
    "created_at": "2010-03-04T15:03:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8424#issuecomment-75399",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Hi Jason, 

The macros isfinite() and isinf() are both defined in math.h, so the use of either of those would not present a problem. 

INFINITY is defined for C99 code, so I believe that as long as you specify -std=c99 as an option to gcc, then it will be ok. 

Dave



---

archive/issue_comments_075400.json:
```json
{
    "body": "Merged \"trac-8424-bounding-boxes.patch\" into 4.4.alpha0.",
    "created_at": "2010-04-15T23:50:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8424#issuecomment-75400",
    "user": "https://github.com/jhpalmieri"
}
```

Merged "trac-8424-bounding-boxes.patch" into 4.4.alpha0.



---

archive/issue_events_020184.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2010-04-15T23:50:54Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8424",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8424#event-20184"
}
```



---

archive/issue_comments_075401.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-15T23:50:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8424#issuecomment-75401",
    "user": "https://github.com/jhpalmieri"
}
```

Resolution: fixed
