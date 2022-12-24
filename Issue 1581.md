# Issue 1581: 3d graphics do not show all objects by default

archive/issues_001581.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nfrom sage.plot.plot3d.all import Sphere\nSphere(.1).translate(1,2,3).show()\n```\n\n\ndoes not adjust the viewpoint, etc. to include the sphere, so it confusingly looks like a blank plot until, for example, the interactive version is rotated around.  It would be nice to have at least some part of the plot, if not the whole thing, visible by default.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1581\n\n",
    "created_at": "2007-12-21T08:58:06Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10",
    "title": "3d graphics do not show all objects by default",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1581",
    "user": "@jasongrout"
}
```
Assignee: @williamstein


```
from sage.plot.plot3d.all import Sphere
Sphere(.1).translate(1,2,3).show()
```


does not adjust the viewpoint, etc. to include the sphere, so it confusingly looks like a blank plot until, for example, the interactive version is rotated around.  It would be nice to have at least some part of the plot, if not the whole thing, visible by default.

Issue created by migration from https://trac.sagemath.org/ticket/1581





---

archive/issue_comments_010073.json:
```json
{
    "body": "Changing assignee from @williamstein to @robertwb.",
    "created_at": "2007-12-30T10:55:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1581#issuecomment-10073",
    "user": "@robertwb"
}
```

Changing assignee from @williamstein to @robertwb.



---

archive/issue_comments_010074.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-30T10:55:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1581#issuecomment-10074",
    "user": "@robertwb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_010075.json:
```json
{
    "body": "I've done a little bit of work on bounding boxes, this is what I think we should be using. (There are more sophisticated bounding methods, but I don't think we'll need them for out application.)",
    "created_at": "2007-12-30T10:56:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1581#issuecomment-10075",
    "user": "@robertwb"
}
```

I've done a little bit of work on bounding boxes, this is what I think we should be using. (There are more sophisticated bounding methods, but I don't think we'll need them for out application.)



---

archive/issue_comments_010076.json:
```json
{
    "body": "This patch fixes the problem, plus does a *lot* of other work.  This is a snapshot --  it is not suitable for inclusion in the next version of Sage as is -- probably many 3d doctests still fail.",
    "created_at": "2008-01-01T10:30:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1581#issuecomment-10076",
    "user": "@williamstein"
}
```

This patch fixes the problem, plus does a *lot* of other work.  This is a snapshot --  it is not suitable for inclusion in the next version of Sage as is -- probably many 3d doctests still fail.



---

archive/issue_comments_010077.json:
```json
{
    "body": "Attachment [3d.hg](tarball://root/attachments/some-uuid/ticket1581/3d.hg) by @robertwb created at 2008-01-15 06:14:01\n\nThis has already been resolved included in Sage.",
    "created_at": "2008-01-15T06:14:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1581#issuecomment-10077",
    "user": "@robertwb"
}
```

Attachment [3d.hg](tarball://root/attachments/some-uuid/ticket1581/3d.hg) by @robertwb created at 2008-01-15 06:14:01

This has already been resolved included in Sage.



---

archive/issue_comments_010078.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-15T06:14:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1581#issuecomment-10078",
    "user": "@robertwb"
}
```

Resolution: fixed
