# Issue 3547: create a polygon3d function

archive/issues_003547.json:
```json
{
    "body": "Assignee: was\n\nThis should be the 3d analogue of the polygon function.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3547\n\n",
    "created_at": "2008-07-03T21:28:47Z",
    "labels": [
        "graphics",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "create a polygon3d function",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3547",
    "user": "mhansen"
}
```
Assignee: was

This should be the 3d analogue of the polygon function.

Issue created by migration from https://trac.sagemath.org/ticket/3547





---

archive/issue_comments_025087.json:
```json
{
    "body": "Please remember to assign milestones to all tickets.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-06T20:22:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3547#issuecomment-25087",
    "user": "mabshoff"
}
```

Please remember to assign milestones to all tickets.

Cheers,

Michael



---

archive/issue_comments_025088.json:
```json
{
    "body": "Oops :-)",
    "created_at": "2008-07-06T20:23:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3547#issuecomment-25088",
    "user": "mhansen"
}
```

Oops :-)



---

archive/issue_comments_025089.json:
```json
{
    "body": "Also, the polygon function should defer to this when the input is 3d points \n\n\n```\n\nOn Dec 16, 2008, at 8:28 AM, philt wrote:\n\nHello,\n\nI got some trouble trying to draw polygons in JMol because the\nfunction looks not available easily.\nSage is featuring the following:\npoint() -> try point2d else point3d\nline() -> try line2d else line3d\npolygon() -> only 2d\nbut many fancy volumes are available in 3D...\n\nI think it'd be more natural to have polygon working in a similar\nflexible way.\nSomething like:\n\ntry:\n        return polygon2d(points, **kwds)\n    except ValueError:\n        from sage.plot.plot3d.platonic import IndexFaceSet as\npolygon3d\n        return polygon3d(points, **kwds)\n\nwith polygon2d being the current code of polygon()\n```\n",
    "created_at": "2008-12-16T18:49:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3547#issuecomment-25089",
    "user": "robertwb"
}
```

Also, the polygon function should defer to this when the input is 3d points 


```

On Dec 16, 2008, at 8:28 AM, philt wrote:

Hello,

I got some trouble trying to draw polygons in JMol because the
function looks not available easily.
Sage is featuring the following:
point() -> try point2d else point3d
line() -> try line2d else line3d
polygon() -> only 2d
but many fancy volumes are available in 3D...

I think it'd be more natural to have polygon working in a similar
flexible way.
Something like:

try:
        return polygon2d(points, **kwds)
    except ValueError:
        from sage.plot.plot3d.platonic import IndexFaceSet as
polygon3d
        return polygon3d(points, **kwds)

with polygon2d being the current code of polygon()
```




---

archive/issue_comments_025090.json:
```json
{
    "body": "Attachment [trac_3547.patch](tarball://root/attachments/some-uuid/ticket3547/trac_3547.patch) by abergeron created at 2008-12-24 22:54:59",
    "created_at": "2008-12-24T22:54:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3547#issuecomment-25090",
    "user": "abergeron"
}
```

Attachment [trac_3547.patch](tarball://root/attachments/some-uuid/ticket3547/trac_3547.patch) by abergeron created at 2008-12-24 22:54:59



---

archive/issue_comments_025091.json:
```json
{
    "body": "I did a trial implementation using IndexFaceSet.  The code is really simple (and dumb).\n\nIt works with any number of points and just draws triangles as in a triangle strip.  \n\nThe alternative would have been to draw the enclosed space, but that functionality is already provided by Polyhedron and does not mimick what polygon[2d] does.",
    "created_at": "2008-12-24T23:01:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3547#issuecomment-25091",
    "user": "abergeron"
}
```

I did a trial implementation using IndexFaceSet.  The code is really simple (and dumb).

It works with any number of points and just draws triangles as in a triangle strip.  

The alternative would have been to draw the enclosed space, but that functionality is already provided by Polyhedron and does not mimick what polygon[2d] does.



---

archive/issue_comments_025092.json:
```json
{
    "body": "Changing assignee from was to abergeron.",
    "created_at": "2008-12-24T23:01:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3547#issuecomment-25092",
    "user": "abergeron"
}
```

Changing assignee from was to abergeron.



---

archive/issue_comments_025093.json:
```json
{
    "body": "looks good to me",
    "created_at": "2009-01-24T12:27:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3547#issuecomment-25093",
    "user": "shumow"
}
```

looks good to me



---

archive/issue_comments_025094.json:
```json
{
    "body": "Merged in Sage 3.3.alpha3.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-28T16:17:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3547#issuecomment-25094",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha3.

Cheers,

Michael



---

archive/issue_comments_025095.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-28T16:17:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3547#issuecomment-25095",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_025096.json:
```json
{
    "body": "Is it possible for someone to attach an image or two to this ticket to illustrate the sort of images one can get from using the new function `polygon3d()`? I'm looking for an image of a plot resulting from using the function `polygon3d()`. What I have in mind is something along the line of the images attached to #2770 and #4976. Such images should serve as a high-level summary of what a (new) plotting function can do. And having such images mean that they can be referred to from a release tour note on the Sage wiki. The point is: when introducing new functionalities one would upload a patch to trac, together with doctests and examples. But when a new function deals with graphics and plots, I think it's a good idea to upload an image or two whenever possible. I don't always have the latest alpha on my work machine, only the latest stable version, so can someone please upload an image?",
    "created_at": "2009-02-07T04:21:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3547#issuecomment-25096",
    "user": "mvngu"
}
```

Is it possible for someone to attach an image or two to this ticket to illustrate the sort of images one can get from using the new function `polygon3d()`? I'm looking for an image of a plot resulting from using the function `polygon3d()`. What I have in mind is something along the line of the images attached to #2770 and #4976. Such images should serve as a high-level summary of what a (new) plotting function can do. And having such images mean that they can be referred to from a release tour note on the Sage wiki. The point is: when introducing new functionalities one would upload a patch to trac, together with doctests and examples. But when a new function deals with graphics and plots, I think it's a good idea to upload an image or two whenever possible. I don't always have the latest alpha on my work machine, only the latest stable version, so can someone please upload an image?
