# Issue 5108: Add infinite planes to Sage 3d graphics

archive/issues_005108.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\n> Is there an easy way to draw infinite planes in Sage, given, say, the\n> > normal vector and a point on the plane?  Of course, you can draw them\n> > using parametric_plot3d, but that requires me specifying a range, etc.\n> > It also seems like it wouldn't be terribly efficient, since the infinite\n> > plane could be represented with a jmol plane primitive or a Tachyon\n> > plane primitive, which is presumably more efficient than a bunch of\n> > triangles.  It seems like it would be handy to have a primitive for an\n> > infinite plane.\n> >\n> > I'm posting to sage-devel because I suspect there is not a primitive for\n> > an infinite plane.\n> >\n> > I imagine that such a primitive would look something like:\n> >\n> > plane(normal, point=(0,0,0))\n> >\n> > If it was drawn by itself, it would pick some default bounding box,\n> > centered around the point.  If it wasn't drawn by itself, it would just\n> > fit itself inside of whatever the current bounding box for everything\n> > else was.  Or maybe it would still specify a bounding box around the\n> > point, since that is likely to be a point of interest to the viewers,\n> > but the plane would grow to fill the entire bounding box constructed in\n> > a composite graphic.\n\nThis isn't in Sage, and it would be very useful if somebody (=you, of\ncourse) were to add it.  You would want to look at the\nplot3d/platonic.py file to get an idea how to make index_face_set.pyx\ndo what you want.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5108\n\n",
    "created_at": "2009-01-26T21:37:51Z",
    "labels": [
        "component: graphics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Add infinite planes to Sage 3d graphics",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5108",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein


```
> Is there an easy way to draw infinite planes in Sage, given, say, the
> > normal vector and a point on the plane?  Of course, you can draw them
> > using parametric_plot3d, but that requires me specifying a range, etc.
> > It also seems like it wouldn't be terribly efficient, since the infinite
> > plane could be represented with a jmol plane primitive or a Tachyon
> > plane primitive, which is presumably more efficient than a bunch of
> > triangles.  It seems like it would be handy to have a primitive for an
> > infinite plane.
> >
> > I'm posting to sage-devel because I suspect there is not a primitive for
> > an infinite plane.
> >
> > I imagine that such a primitive would look something like:
> >
> > plane(normal, point=(0,0,0))
> >
> > If it was drawn by itself, it would pick some default bounding box,
> > centered around the point.  If it wasn't drawn by itself, it would just
> > fit itself inside of whatever the current bounding box for everything
> > else was.  Or maybe it would still specify a bounding box around the
> > point, since that is likely to be a point of interest to the viewers,
> > but the plane would grow to fill the entire bounding box constructed in
> > a composite graphic.

This isn't in Sage, and it would be very useful if somebody (=you, of
course) were to add it.  You would want to look at the
plot3d/platonic.py file to get an idea how to make index_face_set.pyx
do what you want.
```


Issue created by migration from https://trac.sagemath.org/ticket/5108





---

archive/issue_comments_038954.json:
```json
{
    "body": "Changing assignee from @williamstein to @jasongrout.",
    "created_at": "2009-01-26T21:38:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5108",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5108#issuecomment-38954",
    "user": "https://github.com/jasongrout"
}
```

Changing assignee from @williamstein to @jasongrout.



---

archive/issue_comments_038955.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-26T21:38:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5108",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5108#issuecomment-38955",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to assigned.
