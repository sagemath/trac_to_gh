# Issue 2477: [with patch, positive review] 3d plotting of graphs -- need to force aspect_ratio=[1,1,1] by default (trivial to fix this!)

archive/issues_002477.json:
```json
{
    "body": "Assignee: @rlmill\n\n```\nsage: g = graphs.PetersenGraph()\nsage: g.plot3d()\n[a crappy looking plot]\nsage: g = graphs.PetersenGraph()\nsage: g.plot3d(aspect_ratio=[1,1,1])\n[a much better looking plot]\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/2477\n\n",
    "closed_at": "2008-03-31T13:44:28Z",
    "created_at": "2008-03-11T23:13:24Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "[with patch, positive review] 3d plotting of graphs -- need to force aspect_ratio=[1,1,1] by default (trivial to fix this!)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2477",
    "user": "https://github.com/williamstein"
}
```
Assignee: @rlmill

```
sage: g = graphs.PetersenGraph()
sage: g.plot3d()
[a crappy looking plot]
sage: g = graphs.PetersenGraph()
sage: g.plot3d(aspect_ratio=[1,1,1])
[a much better looking plot]
```

Issue created by migration from https://trac.sagemath.org/ticket/2477





---

archive/issue_comments_016737.json:
```json
{
    "body": "Attachment [2477.patch](tarball://root/attachments/some-uuid/ticket2477/2477.patch) by @rlmill created at 2008-03-14 14:53:02",
    "created_at": "2008-03-14T14:53:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2477#issuecomment-16737",
    "user": "https://github.com/rlmill"
}
```

Attachment [2477.patch](tarball://root/attachments/some-uuid/ticket2477/2477.patch) by @rlmill created at 2008-03-14 14:53:02



---

archive/issue_comments_016738.json:
```json
{
    "body": "This is a different bug, but the funny thing is my experience is\n\n```\nsage: g = graphs.PetersenGraph()\nsage: g.plot3d()\n[a crappy looking plot]\nsage: g = graphs.PetersenGraph()\nsage: g.plot3d(aspect_ratio=[1,1,1])\n[an even crappier looking plot]\n```\nThe new plot has vertices with holes in them. I have no idea what is causing this at all.",
    "created_at": "2008-03-14T14:54:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2477#issuecomment-16738",
    "user": "https://github.com/rlmill"
}
```

This is a different bug, but the funny thing is my experience is

```
sage: g = graphs.PetersenGraph()
sage: g.plot3d()
[a crappy looking plot]
sage: g = graphs.PetersenGraph()
sage: g.plot3d(aspect_ratio=[1,1,1])
[an even crappier looking plot]
```
The new plot has vertices with holes in them. I have no idea what is causing this at all.



---

archive/issue_events_005851.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-29T19:48:19Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2477",
    "milestone": "sage-2.11",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2477#event-5851"
}
```



---

archive/issue_comments_016739.json:
```json
{
    "body": "I think the patch ought to use:\n\n```\naspect_ratio = kwds.setdefault('aspect_ratio', [1,1,1])\n```\n\nor even just\n\n```\nkwds.setdefault('aspect_ratio', [1,1,1])\n```\n\nwhich is the python way to do this.",
    "created_at": "2008-03-29T20:05:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2477#issuecomment-16739",
    "user": "https://github.com/jasongrout"
}
```

I think the patch ought to use:

```
aspect_ratio = kwds.setdefault('aspect_ratio', [1,1,1])
```

or even just

```
kwds.setdefault('aspect_ratio', [1,1,1])
```

which is the python way to do this.



---

archive/issue_comments_016740.json:
```json
{
    "body": "The reason this ticket wasn't flagged was because setting aspect ratio to 1,1,1 causes the vertices to look very bad on some systems. In order for this to happen, something needs to happen, either in the code for spheres, or the way graphs are calling them. This isn't ready.",
    "created_at": "2008-03-29T20:14:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2477#issuecomment-16740",
    "user": "https://github.com/rlmill"
}
```

The reason this ticket wasn't flagged was because setting aspect ratio to 1,1,1 causes the vertices to look very bad on some systems. In order for this to happen, something needs to happen, either in the code for spheres, or the way graphs are calling them. This isn't ready.



---

archive/issue_comments_016741.json:
```json
{
    "body": "The aspect_ratio:\n\naspect_ratio=[1,1,1.0000001]\n\nworks great for me, while the aspect_ratio=[1,1,1] gives the holes.\n\nI'd say just make the aspect ratio the above (which is *really* close to 1,1,1).",
    "created_at": "2008-03-29T20:34:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2477#issuecomment-16741",
    "user": "https://github.com/jasongrout"
}
```

The aspect_ratio:

aspect_ratio=[1,1,1.0000001]

works great for me, while the aspect_ratio=[1,1,1] gives the holes.

I'd say just make the aspect ratio the above (which is *really* close to 1,1,1).



---

archive/issue_comments_016742.json:
```json
{
    "body": "Playing around with this, it doesn't seem very reliable. In fact, the two problems of inconsistent edge thickness and vertex holeyness seem to come and go in loose inverse proportion of each other (although I've seen all holes and all messed up edges and I've seen no holes and no messed up edges too...). Just try fiddling that last parameter around, 1.1, 1.01, 1.00000001, they all come out very different for me (and none of them problem-free!)",
    "created_at": "2008-03-29T20:52:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2477#issuecomment-16742",
    "user": "https://github.com/rlmill"
}
```

Playing around with this, it doesn't seem very reliable. In fact, the two problems of inconsistent edge thickness and vertex holeyness seem to come and go in loose inverse proportion of each other (although I've seen all holes and all messed up edges and I've seen no holes and no messed up edges too...). Just try fiddling that last parameter around, 1.1, 1.01, 1.00000001, they all come out very different for me (and none of them problem-free!)



---

archive/issue_comments_016743.json:
```json
{
    "body": "I think the issue here is the radius of the vertices (0.06).  We see the same problem with the following:\n\n\nsphere(center=(-1,0,0),size=.06) + sphere(center=(1,0,0), size=0.06, \naspect_ratio=[1,1,1])\n\nFor me, an alternative to setting the aspect_ratio to [1,1,1.000001] would be setting the radius of the vertices to 0.1 (at least, a radius of 0.1 fixes the holes in the above spheres).",
    "created_at": "2008-03-29T21:05:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2477#issuecomment-16743",
    "user": "https://github.com/jasongrout"
}
```

I think the issue here is the radius of the vertices (0.06).  We see the same problem with the following:


sphere(center=(-1,0,0),size=.06) + sphere(center=(1,0,0), size=0.06, 
aspect_ratio=[1,1,1])

For me, an alternative to setting the aspect_ratio to [1,1,1.000001] would be setting the radius of the vertices to 0.1 (at least, a radius of 0.1 fixes the holes in the above spheres).



---

archive/issue_comments_016744.json:
```json
{
    "body": "This looks like a jmol issue to me in rendering very small spheres.",
    "created_at": "2008-03-29T21:08:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2477#issuecomment-16744",
    "user": "https://github.com/jasongrout"
}
```

This looks like a jmol issue to me in rendering very small spheres.



---

archive/issue_comments_016745.json:
```json
{
    "body": "This post addresses this exact issue:\n\nhttp://www.mail-archive.com/jmol-users`@`lists.sourceforge.net/msg07676.html\n\n(and the followup threads)",
    "created_at": "2008-03-29T21:09:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2477#issuecomment-16745",
    "user": "https://github.com/jasongrout"
}
```

This post addresses this exact issue:

http://www.mail-archive.com/jmol-users`@`lists.sourceforge.net/msg07676.html

(and the followup threads)



---

archive/issue_comments_016746.json:
```json
{
    "body": "http://jmol.sourceforge.net/docs/surface/ seems to indicate that the default is resolution 2, if I've read it right.\n\nI'd say we fix this ticket with an aspect_ratio of [1,1,1] and then open another ticket that sets the resolution of sphere.jmol_repr when a small sphere is drawn.",
    "created_at": "2008-03-29T21:16:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2477#issuecomment-16746",
    "user": "https://github.com/jasongrout"
}
```

http://jmol.sourceforge.net/docs/surface/ seems to indicate that the default is resolution 2, if I've read it right.

I'd say we fix this ticket with an aspect_ratio of [1,1,1] and then open another ticket that sets the resolution of sphere.jmol_repr when a small sphere is drawn.



---

archive/issue_comments_016747.json:
```json
{
    "body": "See http://trac.sagemath.org/sage_trac/ticket/2729 for the sphere holes issue.",
    "created_at": "2008-03-30T00:02:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2477#issuecomment-16747",
    "user": "https://github.com/robertwb"
}
```

See http://trac.sagemath.org/sage_trac/ticket/2729 for the sphere holes issue.



---

archive/issue_comments_016748.json:
```json
{
    "body": "apply instead of the previous patch.",
    "created_at": "2008-03-30T00:42:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2477#issuecomment-16748",
    "user": "https://github.com/jasongrout"
}
```

apply instead of the previous patch.



---

archive/issue_comments_016749.json:
```json
{
    "body": "Attachment [trac-2477-aspect-ratio.patch](tarball://root/attachments/some-uuid/ticket2477/trac-2477-aspect-ratio.patch) by @jasongrout created at 2008-03-30 00:44:27\n\nThe patch at 2729 fixes the vertices so they don't look like tinker toys.  The second patch above should be reviewed (it's a simplifications of the first patch).  Apply second patch only (and give rlm credit for the initial version of the patch).",
    "created_at": "2008-03-30T00:44:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2477#issuecomment-16749",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-2477-aspect-ratio.patch](tarball://root/attachments/some-uuid/ticket2477/trac-2477-aspect-ratio.patch) by @jasongrout created at 2008-03-30 00:44:27

The patch at 2729 fixes the vertices so they don't look like tinker toys.  The second patch above should be reviewed (it's a simplifications of the first patch).  Apply second patch only (and give rlm credit for the initial version of the patch).



---

archive/issue_comments_016750.json:
```json
{
    "body": "Is this only a jmol thing, or should it be applied at a higher level?",
    "created_at": "2008-03-30T00:49:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2477#issuecomment-16750",
    "user": "https://github.com/robertwb"
}
```

Is this only a jmol thing, or should it be applied at a higher level?



---

archive/issue_comments_016751.json:
```json
{
    "body": "Looks good. Apply after #2279.\n\nThis is just a graphs issue, but the issue at #2279 is more applicable to jmol in general.",
    "created_at": "2008-03-30T00:51:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2477#issuecomment-16751",
    "user": "https://github.com/rlmill"
}
```

Looks good. Apply after #2279.

This is just a graphs issue, but the issue at #2279 is more applicable to jmol in general.



---

archive/issue_comments_016752.json:
```json
{
    "body": "Err, #2729.",
    "created_at": "2008-03-30T00:51:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2477#issuecomment-16752",
    "user": "https://github.com/rlmill"
}
```

Err, #2729.



---

archive/issue_comments_016753.json:
```json
{
    "body": "Merged trac-2477-aspect-ratio.patch in Sage 3.0.alpha0",
    "created_at": "2008-03-31T13:44:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2477#issuecomment-16753",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged trac-2477-aspect-ratio.patch in Sage 3.0.alpha0



---

archive/issue_comments_016754.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-31T13:44:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2477#issuecomment-16754",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_005852.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-31T13:44:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2477",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2477#event-5852"
}
```
