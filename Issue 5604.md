# Issue 5604: average Color objects when adding them together

archive/issues_005604.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  mvngu\n\nThis would make it easy to create purple, for example, as red+blue.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5604\n\n",
    "created_at": "2009-03-24T21:30:49Z",
    "labels": [
        "component: graphics",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.2",
    "title": "average Color objects when adding them together",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5604",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

CC:  mvngu

This would make it easy to create purple, for example, as red+blue.

Issue created by migration from https://trac.sagemath.org/ticket/5604





---

archive/issue_comments_043656.json:
```json
{
    "body": "This is done now:\n\n\n```\nsage: sage.plot.colors.red+sage.plot.colors.blue\nRGB color (0.5, 0.0, 0.5)\n\n```\n\n\nSo this ticket should be closed.",
    "created_at": "2010-05-11T20:34:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5604#issuecomment-43656",
    "user": "https://github.com/jasongrout"
}
```

This is done now:


```
sage: sage.plot.colors.red+sage.plot.colors.blue
RGB color (0.5, 0.0, 0.5)

```


So this ticket should be closed.



---

archive/issue_events_013195.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-05-11T20:49:39Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5604",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5604#event-13195"
}
```



---

archive/issue_comments_043657.json:
```json
{
    "body": "This looks like fixed, but the averaging operator \"+\" is binary:\n\n```\n[mvngu@sage ~]$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: r = sage.plot.colors.red\nsage: g = sage.plot.colors.green\nsage: b = sage.plot.colors.blue\nsage: r; g; b\nRGB color (1.0, 0.0, 0.0)\nRGB color (0.0, 0.50196078431372548, 0.0)\nRGB color (0.0, 0.0, 1.0)\nsage: r + g; r + b\nRGB color (0.5, 0.25098039215686274, 0.0)\nRGB color (0.5, 0.0, 0.5)\nsage: (r + g) + b; r + g + b\nRGB color (0.25, 0.12549019607843137, 0.5)\nRGB color (0.25, 0.12549019607843137, 0.5)\nsage: (r + b) + g; r + b + g\nRGB color (0.25, 0.25098039215686274, 0.25)\nRGB color (0.25, 0.25098039215686274, 0.25)\nsage: (g + b) + r; g + b + r\nRGB color (0.5, 0.12549019607843137, 0.25)\nRGB color (0.5, 0.12549019607843137, 0.25)\n```\n\nFor more than two operands, I thought that \"+\" would average over the number of operands. Instead, \"+\" averages the first two, then average the result with the last operand.",
    "created_at": "2010-05-11T20:49:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5604#issuecomment-43657",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

This looks like fixed, but the averaging operator "+" is binary:

```
[mvngu@sage ~]$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: r = sage.plot.colors.red
sage: g = sage.plot.colors.green
sage: b = sage.plot.colors.blue
sage: r; g; b
RGB color (1.0, 0.0, 0.0)
RGB color (0.0, 0.50196078431372548, 0.0)
RGB color (0.0, 0.0, 1.0)
sage: r + g; r + b
RGB color (0.5, 0.25098039215686274, 0.0)
RGB color (0.5, 0.0, 0.5)
sage: (r + g) + b; r + g + b
RGB color (0.25, 0.12549019607843137, 0.5)
RGB color (0.25, 0.12549019607843137, 0.5)
sage: (r + b) + g; r + b + g
RGB color (0.25, 0.25098039215686274, 0.25)
RGB color (0.25, 0.25098039215686274, 0.25)
sage: (g + b) + r; g + b + r
RGB color (0.5, 0.12549019607843137, 0.25)
RGB color (0.5, 0.12549019607843137, 0.25)
```

For more than two operands, I thought that "+" would average over the number of operands. Instead, "+" averages the first two, then average the result with the last operand.



---

archive/issue_comments_043658.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-11T20:49:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5604#issuecomment-43658",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_043659.json:
```json
{
    "body": "That's because the blending is not associative.  We are just providing a simple way to blend colors together.  That's a limitation of the method---is there a reason why we should insist on the addition being associative?\n\nMixing colors and color theory in general is a very involved topic; we are just scratching the surface here with suboptimal, but still useful, methods and shortcuts.",
    "created_at": "2010-05-11T21:10:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5604#issuecomment-43659",
    "user": "https://github.com/jasongrout"
}
```

That's because the blending is not associative.  We are just providing a simple way to blend colors together.  That's a limitation of the method---is there a reason why we should insist on the addition being associative?

Mixing colors and color theory in general is a very involved topic; we are just scratching the surface here with suboptimal, but still useful, methods and shortcuts.



---

archive/issue_comments_043660.json:
```json
{
    "body": "Replying to [comment:4 jason]:\n> That's because the blending is not associative.  We are just providing a simple way to blend colors together.  That's a limitation of the method---is there a reason why we should insist on the addition being associative?\n\nNo reason I can think of. My surprise as expressed above has more to do with my lack of understanding.",
    "created_at": "2010-05-11T21:14:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5604#issuecomment-43660",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:4 jason]:
> That's because the blending is not associative.  We are just providing a simple way to blend colors together.  That's a limitation of the method---is there a reason why we should insist on the addition being associative?

No reason I can think of. My surprise as expressed above has more to do with my lack of understanding.
