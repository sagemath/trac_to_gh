# Issue 7488: plot3d? doesn't document some important options, which causes confusion

archive/issues_007488.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\n\n\nOn Wed, Nov 18, 2009 at 9:16 AM, Laurent <> wrote:\n> Hi.\n>\n> I'm writing the following code in order to plot sin(x^2+x^2) :\n>\n> var('x,y')\n> g(x,y)=sin(x**2+y**2)\n> plot3d(g(x,y),(x,-5,5),(y,-5,5))\n>\n> My problem is that the result is quite bad because of the sampling : all\n> the points with x^2+y^2=pi/2 are not taken, so that I don't get\n> beautiful circles.\n>\n> How can I ask for a finer sampling, or to compute more intermediate points ?\n\nUse the plot_points option.  Type \"parametric_plot3d?\" for more details:\n\n        -  ``plot_points`` - (default: \"automatic\", which is\n           75 for curves and [40,40] for surfaces) initial number of sample\n           points in each parameter; an integer for a curve, and a pair of\n           integers for a surface.\n        \nNote that the documentation output by \"plot3d?\" doesn't even mention the plot_points option, which is why you're confused.  \n\nWilliam\n\n\n\n -- William\n\n> I'm sure there is an option to add, but I don't see in the documentation\n> which one. (I'm reading the Sage reference manual, version 4.1.1, Agust\n> 14 2009).\n\nIssue created by migration from https://trac.sagemath.org/ticket/7488\n\n",
    "created_at": "2009-11-18T17:32:44Z",
    "labels": [
        "component: graphics",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "plot3d? doesn't document some important options, which causes confusion",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7488",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein


```


On Wed, Nov 18, 2009 at 9:16 AM, Laurent <> wrote:
> Hi.
>
> I'm writing the following code in order to plot sin(x^2+x^2) :
>
> var('x,y')
> g(x,y)=sin(x**2+y**2)
> plot3d(g(x,y),(x,-5,5),(y,-5,5))
>
> My problem is that the result is quite bad because of the sampling : all
> the points with x^2+y^2=pi/2 are not taken, so that I don't get
> beautiful circles.
>
> How can I ask for a finer sampling, or to compute more intermediate points ?

Use the plot_points option.  Type "parametric_plot3d?" for more details:

        -  ``plot_points`` - (default: "automatic", which is
           75 for curves and [40,40] for surfaces) initial number of sample
           points in each parameter; an integer for a curve, and a pair of
           integers for a surface.
        
Note that the documentation output by "plot3d?" doesn't even mention the plot_points option, which is why you're confused.  

William



 -- William

> I'm sure there is an option to add, but I don't see in the documentation
> which one. (I'm reading the Sage reference manual, version 4.1.1, Agust
> 14 2009).

Issue created by migration from https://trac.sagemath.org/ticket/7488





---

archive/issue_comments_063125.json:
```json
{
    "body": "Attachment [sagelib_7488.patch](tarball://root/attachments/some-uuid/ticket7488/sagelib_7488.patch) by @williamstein created at 2009-11-18 18:08:57",
    "created_at": "2009-11-18T18:08:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7488#issuecomment-63125",
    "user": "https://github.com/williamstein"
}
```

Attachment [sagelib_7488.patch](tarball://root/attachments/some-uuid/ticket7488/sagelib_7488.patch) by @williamstein created at 2009-11-18 18:08:57



---

archive/issue_comments_063126.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-18T18:08:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7488#issuecomment-63126",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_063127.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-11-18T18:10:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7488#issuecomment-63127",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_063128.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-18T18:10:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7488#issuecomment-63128",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_007717.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2009-11-19T10:16:13Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7488",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7488#event-7717"
}
```



---

archive/issue_comments_063129.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-19T10:16:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7488#issuecomment-63129",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
