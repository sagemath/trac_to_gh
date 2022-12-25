# Issue 1850: graphics -- serious bug in parametric plotting of curves.

archive/issues_001850.json:
```json
{
    "body": "Assignee: @williamstein\n\nThis works fine\n\n```\nsage: parametric_plot3d((sin(x), cos(x), x), (x,0,10*pi))\n```\n\n\nThis is missing half of the parametric plot!!\n\n```\nsage: parametric_plot3d((sin(x), cos(x), x), (x,0,10*pi), plot_points=500)\n```\n\n\nI suspect this may be a bug introduced by me or Bobby M. in refactoring some plotting code. \n\nIssue created by migration from https://trac.sagemath.org/ticket/1850\n\n",
    "created_at": "2008-01-19T20:26:06Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "graphics -- serious bug in parametric plotting of curves.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1850",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

This works fine

```
sage: parametric_plot3d((sin(x), cos(x), x), (x,0,10*pi))
```


This is missing half of the parametric plot!!

```
sage: parametric_plot3d((sin(x), cos(x), x), (x,0,10*pi), plot_points=500)
```


I suspect this may be a bug introduced by me or Bobby M. in refactoring some plotting code. 

Issue created by migration from https://trac.sagemath.org/ticket/1850





---

archive/issue_comments_011678.json:
```json
{
    "body": "Very disturbingly, if you render using tachyon you don't see the problem:\n\n```\nsage: parametric_plot3d((sin(x), cos(x), x), (x,0,10*pi), plot_points=500, viewer='tachyon')\n```\n\n\nAlso, rendering some more complicated things makes it so the problem vanishes.\n\n```\nsage: parametric_plot3d((sin(x), cos(x), x+sin(x^2)), (x,0,10*pi), plot_points=500)\n```\n\n\n\nSo this is probably a pretty tricky bug to fix, possibly a bug in jmol.",
    "created_at": "2008-01-19T20:33:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1850#issuecomment-11678",
    "user": "https://github.com/williamstein"
}
```

Very disturbingly, if you render using tachyon you don't see the problem:

```
sage: parametric_plot3d((sin(x), cos(x), x), (x,0,10*pi), plot_points=500, viewer='tachyon')
```


Also, rendering some more complicated things makes it so the problem vanishes.

```
sage: parametric_plot3d((sin(x), cos(x), x+sin(x^2)), (x,0,10*pi), plot_points=500)
```



So this is probably a pretty tricky bug to fix, possibly a bug in jmol.



---

archive/issue_comments_011679.json:
```json
{
    "body": "This seems to hit a hard-coded point limit of 256 in jmol's `org/jmol/shapespecial/Draw.java`, line 69.\n\nI guess we could either change jmol to support arbitrary numbers of points, or split up  curves in 'subcurves' of at most 256 points each.",
    "created_at": "2008-01-19T21:27:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1850#issuecomment-11679",
    "user": "https://github.com/wjp"
}
```

This seems to hit a hard-coded point limit of 256 in jmol's `org/jmol/shapespecial/Draw.java`, line 69.

I guess we could either change jmol to support arbitrary numbers of points, or split up  curves in 'subcurves' of at most 256 points each.



---

archive/issue_comments_011680.json:
```json
{
    "body": "Changing assignee from @williamstein to @robertwb.",
    "created_at": "2008-01-20T00:45:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1850#issuecomment-11680",
    "user": "https://github.com/robertwb"
}
```

Changing assignee from @williamstein to @robertwb.



---

archive/issue_comments_011681.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-20T00:45:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1850#issuecomment-11681",
    "user": "https://github.com/robertwb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_011682.json:
```json
{
    "body": "Chopping it up seems like the simplest choice, preferably at a point of maximum curvature. Setting MAX_POINTS arbitrarily high would increase the memory footprint of every line, and re-writing it to not be so would probably be a significant amount of work (though I can't figure out why it is so in the first place).",
    "created_at": "2008-01-20T00:45:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1850#issuecomment-11682",
    "user": "https://github.com/robertwb"
}
```

Chopping it up seems like the simplest choice, preferably at a point of maximum curvature. Setting MAX_POINTS arbitrarily high would increase the memory footprint of every line, and re-writing it to not be so would probably be a significant amount of work (though I can't figure out why it is so in the first place).



---

archive/issue_comments_011683.json:
```json
{
    "body": "Attachment [1850-jmol-pointlimit.diff](tarball://root/attachments/some-uuid/ticket1850/1850-jmol-pointlimit.diff) by @robertwb created at 2008-01-20 01:06:15",
    "created_at": "2008-01-20T01:06:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1850#issuecomment-11683",
    "user": "https://github.com/robertwb"
}
```

Attachment [1850-jmol-pointlimit.diff](tarball://root/attachments/some-uuid/ticket1850/1850-jmol-pointlimit.diff) by @robertwb created at 2008-01-20 01:06:15



---

archive/issue_comments_011684.json:
```json
{
    "body": "It works well for me.  Thanks Robert!",
    "created_at": "2008-01-20T01:35:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1850#issuecomment-11684",
    "user": "https://github.com/williamstein"
}
```

It works well for me.  Thanks Robert!



---

archive/issue_comments_011685.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-20T01:53:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1850#issuecomment-11685",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_011686.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha0",
    "created_at": "2008-01-20T01:53:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1850#issuecomment-11686",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.1.alpha0



---

archive/issue_events_002008.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-01-20T01:53:55Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1850",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1850#event-2008"
}
```
