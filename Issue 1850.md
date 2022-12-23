# Issue 1850: graphics -- serious bug in parametric plotting of curves.

archive/issues_001850.json:
```json
{
    "body": "Assignee: was\n\nThis works fine\n\n```\nsage: parametric_plot3d((sin(x), cos(x), x), (x,0,10*pi))\n```\n\n\nThis is missing half of the parametric plot!!\n\n```\nsage: parametric_plot3d((sin(x), cos(x), x), (x,0,10*pi), plot_points=500)\n```\n\n\nI suspect this may be a bug introduced by me or Bobby M. in refactoring some plotting code. \n\nIssue created by migration from https://trac.sagemath.org/ticket/1850\n\n",
    "created_at": "2008-01-19T20:26:06Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "title": "graphics -- serious bug in parametric plotting of curves.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1850",
    "user": "was"
}
```
Assignee: was

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

archive/issue_comments_011707.json:
```json
{
    "body": "Very disturbingly, if you render using tachyon you don't see the problem:\n\n```\nsage: parametric_plot3d((sin(x), cos(x), x), (x,0,10*pi), plot_points=500, viewer='tachyon')\n```\n\n\nAlso, rendering some more complicated things makes it so the problem vanishes.\n\n```\nsage: parametric_plot3d((sin(x), cos(x), x+sin(x^2)), (x,0,10*pi), plot_points=500)\n```\n\n\n\nSo this is probably a pretty tricky bug to fix, possibly a bug in jmol.",
    "created_at": "2008-01-19T20:33:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1850#issuecomment-11707",
    "user": "was"
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

archive/issue_comments_011708.json:
```json
{
    "body": "This seems to hit a hard-coded point limit of 256 in jmol's `org/jmol/shapespecial/Draw.java`, line 69.\n\nI guess we could either change jmol to support arbitrary numbers of points, or split up  curves in 'subcurves' of at most 256 points each.",
    "created_at": "2008-01-19T21:27:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1850#issuecomment-11708",
    "user": "wjp"
}
```

This seems to hit a hard-coded point limit of 256 in jmol's `org/jmol/shapespecial/Draw.java`, line 69.

I guess we could either change jmol to support arbitrary numbers of points, or split up  curves in 'subcurves' of at most 256 points each.



---

archive/issue_comments_011709.json:
```json
{
    "body": "Changing assignee from was to robertwb.",
    "created_at": "2008-01-20T00:45:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1850#issuecomment-11709",
    "user": "robertwb"
}
```

Changing assignee from was to robertwb.



---

archive/issue_comments_011710.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-20T00:45:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1850#issuecomment-11710",
    "user": "robertwb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_011711.json:
```json
{
    "body": "Chopping it up seems like the simplest choice, preferably at a point of maximum curvature. Setting MAX_POINTS arbitrarily high would increase the memory footprint of every line, and re-writing it to not be so would probably be a significant amount of work (though I can't figure out why it is so in the first place).",
    "created_at": "2008-01-20T00:45:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1850#issuecomment-11711",
    "user": "robertwb"
}
```

Chopping it up seems like the simplest choice, preferably at a point of maximum curvature. Setting MAX_POINTS arbitrarily high would increase the memory footprint of every line, and re-writing it to not be so would probably be a significant amount of work (though I can't figure out why it is so in the first place).



---

archive/issue_comments_011712.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-01-20T01:06:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1850#issuecomment-11712",
    "user": "robertwb"
}
```

Attachment



---

archive/issue_comments_011713.json:
```json
{
    "body": "It works well for me.  Thanks Robert!",
    "created_at": "2008-01-20T01:35:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1850#issuecomment-11713",
    "user": "was"
}
```

It works well for me.  Thanks Robert!



---

archive/issue_comments_011714.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-20T01:53:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1850#issuecomment-11714",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_011715.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha0",
    "created_at": "2008-01-20T01:53:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1850#issuecomment-11715",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.1.alpha0
