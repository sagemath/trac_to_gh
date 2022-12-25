# Issue 1606: plotting -- add aspect_ratio option to show command

archive/issues_001606.json:
```json
{
    "body": "Assignee: @williamstein\n\n> \n> I've been looking for a plot.option that ensures a 1:1 aspect ratio\n> for 2D plots (e.g. something like AspectRatio->Automatic in Mma). Does\n> this exist in Sage? I'm trying to set things up so that\n> \n> circle((0,0),2).show()\n> \n> shows a circle rather than an ellipse, regardless of the plot window\n> dimensions. Apologies if this has already been covered somewhere.\n\nWe should just add\n    P.show(aspect_ratio=\"automatic\")\netc., exactly as in Mathematica.  The goal with 2d graphics in Sage\nis that they at least support all options that Mathematica has. \n\nAnyway, here is a function show11 that works exactly like show(...), but\nit will always show with a 1:1 aspect ratio:\n\n\n```\ndef show11(g, figsize=[5,4], **kwds):\n    for k in ['xmin', 'xmax', 'ymin', 'ymax']:\n        if kwds.has_key(k): g.__getattribute__(k)(kwds[k])\n    scale = (g.xmax() - g.xmin())/(g.ymax() - g.ymin())\n    g.show(figsize=[figsize[0], figsize[0]/scale], **kwds)\n```\n\n\n\n```\nshow11(plot(sin, 0, 5))\n```\n\n\n\n```\nshow11(circle((0,0), 2), xmin=-3, xmax=4)\n```\n\n\n -- William\n\nIssue created by migration from https://trac.sagemath.org/ticket/1606\n\n",
    "created_at": "2007-12-27T03:19:48Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "plotting -- add aspect_ratio option to show command",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1606",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

> 
> I've been looking for a plot.option that ensures a 1:1 aspect ratio
> for 2D plots (e.g. something like AspectRatio->Automatic in Mma). Does
> this exist in Sage? I'm trying to set things up so that
> 
> circle((0,0),2).show()
> 
> shows a circle rather than an ellipse, regardless of the plot window
> dimensions. Apologies if this has already been covered somewhere.

We should just add
    P.show(aspect_ratio="automatic")
etc., exactly as in Mathematica.  The goal with 2d graphics in Sage
is that they at least support all options that Mathematica has. 

Anyway, here is a function show11 that works exactly like show(...), but
it will always show with a 1:1 aspect ratio:


```
def show11(g, figsize=[5,4], **kwds):
    for k in ['xmin', 'xmax', 'ymin', 'ymax']:
        if kwds.has_key(k): g.__getattribute__(k)(kwds[k])
    scale = (g.xmax() - g.xmin())/(g.ymax() - g.ymin())
    g.show(figsize=[figsize[0], figsize[0]/scale], **kwds)
```



```
show11(plot(sin, 0, 5))
```



```
show11(circle((0,0), 2), xmin=-3, xmax=4)
```


 -- William

Issue created by migration from https://trac.sagemath.org/ticket/1606





---

archive/issue_comments_010177.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-19T18:51:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1606#issuecomment-10177",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to assigned.



---

archive/issue_comments_010178.json:
```json
{
    "body": "Attachment [trac-1606.patch](tarball://root/attachments/some-uuid/ticket1606/trac-1606.patch) by @williamstein created at 2008-01-19 22:16:52",
    "created_at": "2008-01-19T22:16:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1606#issuecomment-10178",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac-1606.patch](tarball://root/attachments/some-uuid/ticket1606/trac-1606.patch) by @williamstein created at 2008-01-19 22:16:52



---

archive/issue_comments_010179.json:
```json
{
    "body": "By the way, I also removed explicit mention of mathematica and matlab in the file, in order to not get in trademark trouble with them. \n\nThe main point about this patch is that the notion of aspect_ratio implemented in it is different than in mathematica.  It is very useful though in practice, and consistent with what we've implemented for 3d graphics.",
    "created_at": "2008-01-19T22:18:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1606#issuecomment-10179",
    "user": "https://github.com/williamstein"
}
```

By the way, I also removed explicit mention of mathematica and matlab in the file, in order to not get in trademark trouble with them. 

The main point about this patch is that the notion of aspect_ratio implemented in it is different than in mathematica.  It is very useful though in practice, and consistent with what we've implemented for 3d graphics.



---

archive/issue_comments_010180.json:
```json
{
    "body": "Works for me.",
    "created_at": "2008-01-21T03:23:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1606#issuecomment-10180",
    "user": "https://github.com/mwhansen"
}
```

Works for me.



---

archive/issue_comments_010181.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-21T03:25:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1606#issuecomment-10181",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_010182.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha1",
    "created_at": "2008-01-21T03:25:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1606#issuecomment-10182",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.1.alpha1



---

archive/issue_events_003991.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-21T03:25:47Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1606",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1606#event-3991"
}
```
