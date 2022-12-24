# Issue 1859: 3d and 2d graphics -- some unification

archive/issues_001859.json:
```json
{
    "body": "Assignee: was\n\nMake it so that the following sort of thing works:\n\n\n```\nsage: sphere() + plot(sin(x), (x,0,10))\nsage: plot(sin(x), (x,0,10)).graphic3d()\n```\n\n\nand\n\n\n```\nsage: plot(sin(x), (x,0,10)).show(viewer='jmol')\n```\n\n\nIn each case the plot would be rendered using 3d primitives instead of 2d primitives, when possible -- primitives that aren't implemented in 3d would degrade or be removed.   Basically make a way of *coercing* 2d plots into the world of 3d plots. \n\nThis would make it possible to view whole arrays, groups, whatever of 2d plots all organized in some spatial way in 3d, and also to zoom in very close, etc., on 2d plots.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1859\n\n",
    "created_at": "2008-01-20T01:27:25Z",
    "labels": [
        "graphics",
        "major",
        "enhancement"
    ],
    "title": "3d and 2d graphics -- some unification",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1859",
    "user": "was"
}
```
Assignee: was

Make it so that the following sort of thing works:


```
sage: sphere() + plot(sin(x), (x,0,10))
sage: plot(sin(x), (x,0,10)).graphic3d()
```


and


```
sage: plot(sin(x), (x,0,10)).show(viewer='jmol')
```


In each case the plot would be rendered using 3d primitives instead of 2d primitives, when possible -- primitives that aren't implemented in 3d would degrade or be removed.   Basically make a way of *coercing* 2d plots into the world of 3d plots. 

This would make it possible to view whole arrays, groups, whatever of 2d plots all organized in some spatial way in 3d, and also to zoom in very close, etc., on 2d plots.


Issue created by migration from https://trac.sagemath.org/ticket/1859





---

archive/issue_comments_011763.json:
```json
{
    "body": "Changing assignee from was to robertwb.",
    "created_at": "2008-01-20T01:44:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1859#issuecomment-11763",
    "user": "robertwb"
}
```

Changing assignee from was to robertwb.



---

archive/issue_comments_011764.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-20T01:44:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1859#issuecomment-11764",
    "user": "robertwb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_011765.json:
```json
{
    "body": "Attachment [1859-2d-3d.diff](tarball://root/attachments/some-uuid/ticket1859/1859-2d-3d.diff) by robertwb created at 2008-01-20 04:15:03",
    "created_at": "2008-01-20T04:15:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1859#issuecomment-11765",
    "user": "robertwb"
}
```

Attachment [1859-2d-3d.diff](tarball://root/attachments/some-uuid/ticket1859/1859-2d-3d.diff) by robertwb created at 2008-01-20 04:15:03



---

archive/issue_comments_011766.json:
```json
{
    "body": "I've implemented turning most 2d primitives into 3d primitives, e.g. \n\n\n```\nsage: sphere(aspect_ratio=[1,1,1]) + plot(sin(x), 0, 10)\nsage: sum([plot(z*sin(x), 0, 10).plot3d(z) for z in range(10)])\n```\n",
    "created_at": "2008-01-20T04:22:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1859#issuecomment-11766",
    "user": "robertwb"
}
```

I've implemented turning most 2d primitives into 3d primitives, e.g. 


```
sage: sphere(aspect_ratio=[1,1,1]) + plot(sin(x), 0, 10)
sage: sum([plot(z*sin(x), 0, 10).plot3d(z) for z in range(10)])
```




---

archive/issue_comments_011767.json:
```json
{
    "body": "AWESOME!!\n\nJust playing around\n\n```\nsage: var('x y'); p1 = parametric_plot3d((x,y,0), (x,-2,2), (y,-2,2), color='red', opacity=0.5)\n(x, y)\nsage: p2 = plot(sin(x),(-2,2)).plot3d().translate(0,0,0.1)\nsage: p1 + p2 + sphere((0,0,1),0.01) + polygon([(0,0), (0,1), (1,2), (2,0)]).plot3d().translate((0,0,-0.1)) + sphere((0,0,-1),0.1)\n\n```\n",
    "created_at": "2008-01-20T05:05:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1859#issuecomment-11767",
    "user": "was"
}
```

AWESOME!!

Just playing around

```
sage: var('x y'); p1 = parametric_plot3d((x,y,0), (x,-2,2), (y,-2,2), color='red', opacity=0.5)
(x, y)
sage: p2 = plot(sin(x),(-2,2)).plot3d().translate(0,0,0.1)
sage: p1 + p2 + sphere((0,0,1),0.01) + polygon([(0,0), (0,1), (1,2), (2,0)]).plot3d().translate((0,0,-0.1)) + sphere((0,0,-1),0.1)

```




---

archive/issue_comments_011768.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha0",
    "created_at": "2008-01-20T05:24:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1859#issuecomment-11768",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.1.alpha0



---

archive/issue_comments_011769.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-20T05:24:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1859#issuecomment-11769",
    "user": "mabshoff"
}
```

Resolution: fixed
