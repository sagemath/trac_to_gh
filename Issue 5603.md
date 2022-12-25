# Issue 5603: make a .mix() method for Sage color objects

archive/issues_005603.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  mvngu\n\nSee the end of http://groups.google.com/group/sage-support/browse_thread/thread/44971aa416574675\n\nWe could also call it .blend() to agree with MMA's terminology:\n\nhttp://reference.wolfram.com/mathematica/ref/Blend.html\n\nIssue created by migration from https://trac.sagemath.org/ticket/5603\n\n",
    "created_at": "2009-03-24T21:29:56Z",
    "labels": [
        "component: graphics",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.2",
    "title": "make a .mix() method for Sage color objects",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5603",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

CC:  mvngu

See the end of http://groups.google.com/group/sage-support/browse_thread/thread/44971aa416574675

We could also call it .blend() to agree with MMA's terminology:

http://reference.wolfram.com/mathematica/ref/Blend.html

Issue created by migration from https://trac.sagemath.org/ticket/5603





---

archive/issue_comments_043653.json:
```json
{
    "body": "This is now implemented as \"blend\":\n\n\n```\nsage: sage.plot.colors.red.blend(sage.plot.colors.blue)\nRGB color (0.5, 0.0, 0.5)\n\n```\n\n\nSo this ticket should be closed.",
    "created_at": "2010-05-11T20:33:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5603#issuecomment-43653",
    "user": "https://github.com/jasongrout"
}
```

This is now implemented as "blend":


```
sage: sage.plot.colors.red.blend(sage.plot.colors.blue)
RGB color (0.5, 0.0, 0.5)

```


So this ticket should be closed.



---

archive/issue_comments_043654.json:
```json
{
    "body": "Close as fixed:\n\n\n```\n[mvngu@sage ~]$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: b = sage.plot.colors.blue\nsage: r = sage.plot.colors.red\nsage: g = sage.plot.colors.green\nsage: b.blend(r)\nRGB color (0.5, 0.0, 0.5)\nsage: r.blend(b)\nRGB color (0.5, 0.0, 0.5)\nsage: r.blend(g)\nRGB color (0.5, 0.25098039215686274, 0.0)\nsage: g.blend(r)\nRGB color (0.5, 0.25098039215686274, 0.0)\nsage: g.blend(b)\nRGB color (0.0, 0.25098039215686274, 0.5)\nsage: b.blend(g)\nRGB color (0.0, 0.25098039215686274, 0.5)\n```\n",
    "created_at": "2010-05-11T20:39:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5603#issuecomment-43654",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Close as fixed:


```
[mvngu@sage ~]$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: b = sage.plot.colors.blue
sage: r = sage.plot.colors.red
sage: g = sage.plot.colors.green
sage: b.blend(r)
RGB color (0.5, 0.0, 0.5)
sage: r.blend(b)
RGB color (0.5, 0.0, 0.5)
sage: r.blend(g)
RGB color (0.5, 0.25098039215686274, 0.0)
sage: g.blend(r)
RGB color (0.5, 0.25098039215686274, 0.0)
sage: g.blend(b)
RGB color (0.0, 0.25098039215686274, 0.5)
sage: b.blend(g)
RGB color (0.0, 0.25098039215686274, 0.5)
```




---

archive/issue_comments_043655.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-11T20:39:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5603#issuecomment-43655",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_013194.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-05-11T20:39:29Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5603",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5603#event-13194"
}
```
