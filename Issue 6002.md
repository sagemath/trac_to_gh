# Issue 6002: parametric_plot3d appears not to give the correct axes values

archive/issues_006002.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  mvngu\n\nAlden Walker describes the bug in a sage-support thread:\n> When I run:\n\n> `parametric_plot( (cos(t), sqrt(2)*sin(t)) , (t,0,2*pi))`\n\n> I get a nice 2d parametric plot, with the top of the ellipse clearly\n> hitting close to 1.5 on the y-axis.  When I run:\n\n> `parametric_plot3d( (cos(t), 1 , sqrt(2)*sin(t)), (t,0,2*pi))`\n\n> The top of the ellipse really looks like it's at z=1, and the whole\n> thing looks a lot like a circle.\n\nEven though the bounding box is reported to be `((-1.0, 1.0, -1.41293...), (1.0, 1.0, 1.41293...))`, jmol labels the axes as (-1, 1), (-1, 1), and (0, 2).\n\nIf we construct the curve manually:\n\n\n```\nvar('t')\nfrom sage.plot.plot import var_and_list_of_values\n_, vals = var_and_list_of_values((0, 2*pi), 75)\nw = []\nfor t in vals:\n    w.append(map(float, (cos(t), 1, sqrt(2)*sin(t))))\n```\n\n\nThen notice that while `line3d(w)` is still incorrect, `line3d(w[0:43])` looks correct -- that is, plotting only part of the graph eliminates the error somehow. Quite curious!\n\nIssue created by migration from https://trac.sagemath.org/ticket/6002\n\n",
    "created_at": "2009-05-07T06:31:27Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "parametric_plot3d appears not to give the correct axes values",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6002",
    "user": "wcauchois"
}
```
Assignee: @williamstein

CC:  mvngu

Alden Walker describes the bug in a sage-support thread:
> When I run:

> `parametric_plot( (cos(t), sqrt(2)*sin(t)) , (t,0,2*pi))`

> I get a nice 2d parametric plot, with the top of the ellipse clearly
> hitting close to 1.5 on the y-axis.  When I run:

> `parametric_plot3d( (cos(t), 1 , sqrt(2)*sin(t)), (t,0,2*pi))`

> The top of the ellipse really looks like it's at z=1, and the whole
> thing looks a lot like a circle.

Even though the bounding box is reported to be `((-1.0, 1.0, -1.41293...), (1.0, 1.0, 1.41293...))`, jmol labels the axes as (-1, 1), (-1, 1), and (0, 2).

If we construct the curve manually:


```
var('t')
from sage.plot.plot import var_and_list_of_values
_, vals = var_and_list_of_values((0, 2*pi), 75)
w = []
for t in vals:
    w.append(map(float, (cos(t), 1, sqrt(2)*sin(t))))
```


Then notice that while `line3d(w)` is still incorrect, `line3d(w[0:43])` looks correct -- that is, plotting only part of the graph eliminates the error somehow. Quite curious!

Issue created by migration from https://trac.sagemath.org/ticket/6002





---

archive/issue_comments_047755.json:
```json
{
    "body": "#6930 fixes this.",
    "created_at": "2009-09-24T18:11:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6002#issuecomment-47755",
    "user": "@jasongrout"
}
```

#6930 fixes this.



---

archive/issue_comments_047756.json:
```json
{
    "body": "Close as duplicate of #6930.",
    "created_at": "2009-09-25T08:20:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6002#issuecomment-47756",
    "user": "mvngu"
}
```

Close as duplicate of #6930.



---

archive/issue_comments_047757.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-09-25T08:20:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6002#issuecomment-47757",
    "user": "mvngu"
}
```

Resolution: duplicate
