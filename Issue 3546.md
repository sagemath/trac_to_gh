# Issue 3546: line3d with jmol draws curves instead of straight lines

archive/issues_003546.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @slel\n\n\n```\nsage: line3d([[0,0,0], [1,0,0], [1,1,0], [.5,1.5,0], [0,1,0], [0,0,0]])\n```\n\n\nWhen rendered with jmol, the lines produced are curves.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3546\n\n",
    "created_at": "2008-07-03T21:27:23Z",
    "labels": [
        "component: graphics",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-wishlist",
    "title": "line3d with jmol draws curves instead of straight lines",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3546",
    "user": "https://github.com/mwhansen"
}
```
Assignee: @williamstein

CC:  @slel


```
sage: line3d([[0,0,0], [1,0,0], [1,1,0], [.5,1.5,0], [0,1,0], [0,0,0]])
```


When rendered with jmol, the lines produced are curves.

Issue created by migration from https://trac.sagemath.org/ticket/3546





---

archive/issue_comments_025034.json:
```json
{
    "body": "From the jmol documentation, I don't know if there is anyway to tell it to draw a straight line (instead of a curve).  See http://chemapps.stolaf.edu/jmol/docs/#draw",
    "created_at": "2012-03-28T23:41:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3546",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3546#issuecomment-25034",
    "user": "https://github.com/mwhansen"
}
```

From the jmol documentation, I don't know if there is anyway to tell it to draw a straight line (instead of a curve).  See http://chemapps.stolaf.edu/jmol/docs/#draw



---

archive/issue_comments_025035.json:
```json
{
    "body": "Less important now that the default 3d rendering engine\nis Three.js, but still quite puzzling.\n\nOne would think `polygon3d` would provide a workaround,\nbut it lacks `polygon2d`'s options to decide whether\nor not to plot the relative interior of the polygon,\nthe edges, the vertices, and in what colors.",
    "created_at": "2021-04-27T22:00:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3546",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3546#issuecomment-25035",
    "user": "https://github.com/slel"
}
```

Less important now that the default 3d rendering engine
is Three.js, but still quite puzzling.

One would think `polygon3d` would provide a workaround,
but it lacks `polygon2d`'s options to decide whether
or not to plot the relative interior of the polygon,
the edges, the vertices, and in what colors.



---

archive/issue_comments_025036.json:
```json
{
    "body": "Related:\n\n- #3861: Prevent or document automatic line3d smoothing",
    "created_at": "2021-04-27T22:08:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3546",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3546#issuecomment-25036",
    "user": "https://github.com/slel"
}
```

Related:

- #3861: Prevent or document automatic line3d smoothing
