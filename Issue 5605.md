# Issue 5605: Construct Color objects using hsl and hsv values

archive/issues_005605.json:
```json
{
    "body": "Assignee: was\n\nCC:  mvngu\n\nSee http://en.wikipedia.org/wiki/HSL_and_HSV\n\nSee also this thread, where the idea came up: http://groups.google.com/group/sage-support/browse_thread/thread/44971aa416574675\n\nIssue created by migration from https://trac.sagemath.org/ticket/5605\n\n",
    "created_at": "2009-03-24T21:36:56Z",
    "labels": [
        "graphics",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.2",
    "title": "Construct Color objects using hsl and hsv values",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5605",
    "user": "jason"
}
```
Assignee: was

CC:  mvngu

See http://en.wikipedia.org/wiki/HSL_and_HSV

See also this thread, where the idea came up: http://groups.google.com/group/sage-support/browse_thread/thread/44971aa416574675

Issue created by migration from https://trac.sagemath.org/ticket/5605





---

archive/issue_comments_043745.json:
```json
{
    "body": "On the RGB converters:\n\n```python\nsage: from sage.plot.colors import rgbcolor, to_mpl_color\nsage: rgbcolor('#ffffff')\n(0.99609375, 0.99609375, 0.99609375)\nsage: to_mpl_color('#ffffff')\n(1.0, 1.0, 1.0)\n```\n\nBoth\n\n```\nColor(rgbcolor(hx)).html_color() == hx\nColor(to_mpl_color(hx)).html_color() == hx\n```\n\nare `True` for all hex colors `hx`, but we should fix `rgbcolor` and/or unify it with `to_mpl_color`.  I'll do this as part of #5601's patch, which may also cover #5602 and, perhaps, this ticket.",
    "created_at": "2009-11-16T05:39:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5605",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5605#issuecomment-43745",
    "user": "mpatel"
}
```

On the RGB converters:

```python
sage: from sage.plot.colors import rgbcolor, to_mpl_color
sage: rgbcolor('#ffffff')
(0.99609375, 0.99609375, 0.99609375)
sage: to_mpl_color('#ffffff')
(1.0, 1.0, 1.0)
```

Both

```
Color(rgbcolor(hx)).html_color() == hx
Color(to_mpl_color(hx)).html_color() == hx
```

are `True` for all hex colors `hx`, but we should fix `rgbcolor` and/or unify it with `to_mpl_color`.  I'll do this as part of #5601's patch, which may also cover #5602 and, perhaps, this ticket.



---

archive/issue_comments_043746.json:
```json
{
    "body": "See the patch at #5601.",
    "created_at": "2009-11-18T04:42:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5605",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5605#issuecomment-43746",
    "user": "mpatel"
}
```

See the patch at #5601.



---

archive/issue_comments_043747.json:
```json
{
    "body": "This works now.  From the doctests of sage.plot.colors.Color:\n\n\n```\n          sage: Color(0.5, 1.0, 1, space='hsv')\n          RGB color (0.0, 1.0, 1.0)\n          sage: Color(0.25, 0.5, 0.5, space='hls')\n          RGB color (0.50000000000000011, 0.75, 0.25)\n```\n\n\nSo this should be closed.",
    "created_at": "2010-05-11T20:37:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5605",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5605#issuecomment-43747",
    "user": "jason"
}
```

This works now.  From the doctests of sage.plot.colors.Color:


```
          sage: Color(0.5, 1.0, 1, space='hsv')
          RGB color (0.0, 1.0, 1.0)
          sage: Color(0.25, 0.5, 0.5, space='hls')
          RGB color (0.50000000000000011, 0.75, 0.25)
```


So this should be closed.



---

archive/issue_comments_043748.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-11T20:53:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5605",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5605#issuecomment-43748",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_043749.json:
```json
{
    "body": "Close as fixed:\n\n\n```\n[mvngu@sage ~]$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: Color(0.5, 1.0, 1, space='hsv')\nRGB color (0.0, 1.0, 1.0)\nsage: Color(0.5, 1.0, 1, space='hls')\nRGB color (1.0, 1.0, 1.0)\nsage: Color(0.25, 0.5, 0.5, space='hls')\nRGB color (0.50000000000000011, 0.75, 0.25)\nsage: Color(0.25, 0.5, 0.5, space='hsv')\nRGB color (0.375, 0.5, 0.25)\n```\n",
    "created_at": "2010-05-11T20:53:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5605",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5605#issuecomment-43749",
    "user": "mvngu"
}
```

Close as fixed:


```
[mvngu@sage ~]$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: Color(0.5, 1.0, 1, space='hsv')
RGB color (0.0, 1.0, 1.0)
sage: Color(0.5, 1.0, 1, space='hls')
RGB color (1.0, 1.0, 1.0)
sage: Color(0.25, 0.5, 0.5, space='hls')
RGB color (0.50000000000000011, 0.75, 0.25)
sage: Color(0.25, 0.5, 0.5, space='hsv')
RGB color (0.375, 0.5, 0.25)
```

