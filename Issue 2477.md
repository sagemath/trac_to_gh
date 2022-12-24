# Issue 2477: 3d plotting of graphs -- need to force aspect_ratio=[1,1,1] by default (trivial to fix this!)

archive/issues_002477.json:
```json
{
    "body": "Assignee: rlm\n\n\n```\nsage: g = graphs.PetersenGraph()\nsage: g.plot3d()\n[a crappy looking plot]\nsage: g = graphs.PetersenGraph()\nsage: g.plot3d(aspect_ratio=[1,1,1])\n[a much better looking plot]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2477\n\n",
    "created_at": "2008-03-11T23:13:24Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "3d plotting of graphs -- need to force aspect_ratio=[1,1,1] by default (trivial to fix this!)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2477",
    "user": "was"
}
```
Assignee: rlm


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

archive/issue_comments_016773.json:
```json
{
    "body": "Attachment [2477.patch](tarball://root/attachments/some-uuid/ticket2477/2477.patch) by rlm created at 2008-03-14 14:53:02",
    "created_at": "2008-03-14T14:53:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2477#issuecomment-16773",
    "user": "rlm"
}
```

Attachment [2477.patch](tarball://root/attachments/some-uuid/ticket2477/2477.patch) by rlm created at 2008-03-14 14:53:02



---

archive/issue_comments_016774.json:
```json
{
    "body": "This is a different bug, but the funny thing is my experience is\n\n```\nsage: g = graphs.PetersenGraph()\nsage: g.plot3d()\n[a crappy looking plot]\nsage: g = graphs.PetersenGraph()\nsage: g.plot3d(aspect_ratio=[1,1,1])\n[an even crappier looking plot]\n```\n\nThe new plot has vertices with holes in them. I have no idea what is causing this at all.",
    "created_at": "2008-03-14T14:54:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2477#issuecomment-16774",
    "user": "rlm"
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

archive/issue_comments_016775.json:
```json
{
    "body": "I think the patch ought to use:\n\n\n```\naspect_ratio = kwds.setdefault('aspect_ratio', [1,1,1])\n```\n\n\nor even just\n\n\n```\nkwds.setdefault('aspect_ratio', [1,1,1])\n```\n\n\nwhich is the python way to do this.",
    "created_at": "2008-03-29T20:05:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2477#issuecomment-16775",
    "user": "jason"
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

archive/issue_comments_016776.json:
```json
{
    "body": "The reason this ticket wasn't flagged was because setting aspect ratio to 1,1,1 causes the vertices to look very bad on some systems. In order for this to happen, something needs to happen, either in the code for spheres, or the way graphs are calling them. This isn't ready.",
    "created_at": "2008-03-29T20:14:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2477#issuecomment-16776",
    "user": "rlm"
}
```

The reason this ticket wasn't flagged was because setting aspect ratio to 1,1,1 causes the vertices to look very bad on some systems. In order for this to happen, something needs to happen, either in the code for spheres, or the way graphs are calling them. This isn't ready.



---

archive/issue_comments_016777.json:
```json
{
    "body": "The aspect_ratio:\n\naspect_ratio=[1,1,1.0000001]\n\nworks great for me, while the aspect_ratio=[1,1,1] gives the holes.\n\nI'd say just make the aspect ratio the above (which is *really* close to 1,1,1).",
    "created_at": "2008-03-29T20:34:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2477#issuecomment-16777",
    "user": "jason"
}
```

The aspect_ratio:

aspect_ratio=[1,1,1.0000001]

works great for me, while the aspect_ratio=[1,1,1] gives the holes.

I'd say just make the aspect ratio the above (which is *really* close to 1,1,1).



---

archive/issue_comments_016778.json:
```json
{
    "body": "Playing around with this, it doesn't seem very reliable. In fact, the two problems of inconsistent edge thickness and vertex holeyness seem to come and go in loose inverse proportion of each other (although I've seen all holes and all messed up edges and I've seen no holes and no messed up edges too...). Just try fiddling that last parameter around, 1.1, 1.01, 1.00000001, they all come out very different for me (and none of them problem-free!)",
    "created_at": "2008-03-29T20:52:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2477#issuecomment-16778",
    "user": "rlm"
}
```

Playing around with this, it doesn't seem very reliable. In fact, the two problems of inconsistent edge thickness and vertex holeyness seem to come and go in loose inverse proportion of each other (although I've seen all holes and all messed up edges and I've seen no holes and no messed up edges too...). Just try fiddling that last parameter around, 1.1, 1.01, 1.00000001, they all come out very different for me (and none of them problem-free!)



---

archive/issue_comments_016779.json:
```json
{
    "body": "I think the issue here is the radius of the vertices (0.06).  We see the same problem with the following:\n\n\nsphere(center=(-1,0,0),size=.06) + sphere(center=(1,0,0), size=0.06, \naspect_ratio=[1,1,1])\n\nFor me, an alternative to setting the aspect_ratio to [1,1,1.000001] would be setting the radius of the vertices to 0.1 (at least, a radius of 0.1 fixes the holes in the above spheres).",
    "created_at": "2008-03-29T21:05:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2477#issuecomment-16779",
    "user": "jason"
}
```

I think the issue here is the radius of the vertices (0.06).  We see the same problem with the following:


sphere(center=(-1,0,0),size=.06) + sphere(center=(1,0,0), size=0.06, 
aspect_ratio=[1,1,1])

For me, an alternative to setting the aspect_ratio to [1,1,1.000001] would be setting the radius of the vertices to 0.1 (at least, a radius of 0.1 fixes the holes in the above spheres).



---

archive/issue_comments_016780.json:
```json
{
    "body": "This looks like a jmol issue to me in rendering very small spheres.",
    "created_at": "2008-03-29T21:08:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2477#issuecomment-16780",
    "user": "jason"
}
```

This looks like a jmol issue to me in rendering very small spheres.



---

archive/issue_comments_016781.json:
```json
{
    "body": "This post addresses this exact issue:\n\nhttp://www.mail-archive.com/jmol-users`@`lists.sourceforge.net/msg07676.html\n\n(and the followup threads)",
    "created_at": "2008-03-29T21:09:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2477#issuecomment-16781",
    "user": "jason"
}
```

This post addresses this exact issue:

http://www.mail-archive.com/jmol-users`@`lists.sourceforge.net/msg07676.html

(and the followup threads)



---

archive/issue_comments_016782.json:
```json
{
    "body": "http://jmol.sourceforge.net/docs/surface/ seems to indicate that the default is resolution 2, if I've read it right.\n\nI'd say we fix this ticket with an aspect_ratio of [1,1,1] and then open another ticket that sets the resolution of sphere.jmol_repr when a small sphere is drawn.",
    "created_at": "2008-03-29T21:16:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2477#issuecomment-16782",
    "user": "jason"
}
```

http://jmol.sourceforge.net/docs/surface/ seems to indicate that the default is resolution 2, if I've read it right.

I'd say we fix this ticket with an aspect_ratio of [1,1,1] and then open another ticket that sets the resolution of sphere.jmol_repr when a small sphere is drawn.



---

archive/issue_comments_016783.json:
```json
{
    "body": "See http://trac.sagemath.org/sage_trac/ticket/2729 for the sphere holes issue.",
    "created_at": "2008-03-30T00:02:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2477#issuecomment-16783",
    "user": "robertwb"
}
```

See http://trac.sagemath.org/sage_trac/ticket/2729 for the sphere holes issue.



---

archive/issue_comments_016784.json:
```json
{
    "body": "apply instead of the previous patch.",
    "created_at": "2008-03-30T00:42:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2477#issuecomment-16784",
    "user": "jason"
}
```

apply instead of the previous patch.



---

archive/issue_comments_016785.json:
```json
{
    "body": "Attachment [trac-2477-aspect-ratio.patch](tarball://root/attachments/some-uuid/ticket2477/trac-2477-aspect-ratio.patch) by jason created at 2008-03-30 00:44:27\n\nThe patch at 2729 fixes the vertices so they don't look like tinker toys.  The second patch above should be reviewed (it's a simplifications of the first patch).  Apply second patch only (and give rlm credit for the initial version of the patch).",
    "created_at": "2008-03-30T00:44:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2477#issuecomment-16785",
    "user": "jason"
}
```

Attachment [trac-2477-aspect-ratio.patch](tarball://root/attachments/some-uuid/ticket2477/trac-2477-aspect-ratio.patch) by jason created at 2008-03-30 00:44:27

The patch at 2729 fixes the vertices so they don't look like tinker toys.  The second patch above should be reviewed (it's a simplifications of the first patch).  Apply second patch only (and give rlm credit for the initial version of the patch).



---

archive/issue_comments_016786.json:
```json
{
    "body": "Is this only a jmol thing, or should it be applied at a higher level?",
    "created_at": "2008-03-30T00:49:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2477#issuecomment-16786",
    "user": "robertwb"
}
```

Is this only a jmol thing, or should it be applied at a higher level?



---

archive/issue_comments_016787.json:
```json
{
    "body": "Looks good. Apply after #2279.\n\nThis is just a graphs issue, but the issue at #2279 is more applicable to jmol in general.",
    "created_at": "2008-03-30T00:51:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2477#issuecomment-16787",
    "user": "rlm"
}
```

Looks good. Apply after #2279.

This is just a graphs issue, but the issue at #2279 is more applicable to jmol in general.



---

archive/issue_comments_016788.json:
```json
{
    "body": "Err, #2729.",
    "created_at": "2008-03-30T00:51:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2477#issuecomment-16788",
    "user": "rlm"
}
```

Err, #2729.



---

archive/issue_comments_016789.json:
```json
{
    "body": "Merged trac-2477-aspect-ratio.patch in Sage 3.0.alpha0",
    "created_at": "2008-03-31T13:44:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2477#issuecomment-16789",
    "user": "mabshoff"
}
```

Merged trac-2477-aspect-ratio.patch in Sage 3.0.alpha0



---

archive/issue_comments_016790.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-31T13:44:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2477#issuecomment-16790",
    "user": "mabshoff"
}
```

Resolution: fixed
