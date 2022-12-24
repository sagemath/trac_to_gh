# Issue 9716: tachyon 3d plotting of graphs is still screwy

archive/issues_009716.json:
```json
{
    "body": "Assignee: jason, ncohen, rlm\n\nCC:  mhampton\n\nThis looks like crap:\n\n```\ng = graphs.DodecahedralGraph()\ng.plot3d(viewer='tachyon')\n```\n\nbut this looks good:\n\n```\ng = graphs.DodecahedralGraph()\nshow(g.plot3d(engine='tachyon'))\n```\n\nAlso, this doesn't work (show a plot) at all:\n\n```\ng = graphs.DodecahedralGraph()\ng.plot3d(engine='tachyon')\n```\n\n\nThat's at least 2 bugs / sloppinesses. \n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9716\n\n",
    "created_at": "2010-08-10T04:28:12Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "tachyon 3d plotting of graphs is still screwy",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9716",
    "user": "@williamstein"
}
```
Assignee: jason, ncohen, rlm

CC:  mhampton

This looks like crap:

```
g = graphs.DodecahedralGraph()
g.plot3d(viewer='tachyon')
```

but this looks good:

```
g = graphs.DodecahedralGraph()
show(g.plot3d(engine='tachyon'))
```

Also, this doesn't work (show a plot) at all:

```
g = graphs.DodecahedralGraph()
g.plot3d(engine='tachyon')
```


That's at least 2 bugs / sloppinesses. 



Issue created by migration from https://trac.sagemath.org/ticket/9716





---

archive/issue_comments_094795.json:
```json
{
    "body": "first example",
    "created_at": "2010-09-03T20:43:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9716#issuecomment-94795",
    "user": "@jasongrout"
}
```

first example



---

archive/issue_comments_094796.json:
```json
{
    "body": "Attachment [plot2.png](tarball://root/attachments/some-uuid/ticket9716/plot2.png) by @jasongrout created at 2010-09-03 20:43:33\n\nsecond example",
    "created_at": "2010-09-03T20:43:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9716#issuecomment-94796",
    "user": "@jasongrout"
}
```

Attachment [plot2.png](tarball://root/attachments/some-uuid/ticket9716/plot2.png) by @jasongrout created at 2010-09-03 20:43:33

second example



---

archive/issue_comments_094797.json:
```json
{
    "body": "I've uploaded the outputs (for me) of the examples.\n\nplot1.png:\n\n```\ng = graphs.DodecahedralGraph()\ng.plot3d(viewer='tachyon')\n```\n\n\nplot2.png:\n\n```\ng = graphs.DodecahedralGraph()\nshow(g.plot3d(engine='tachyon'))\n```\n\n\nWhy is the first plot way worse than the second?",
    "created_at": "2010-09-03T20:45:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9716#issuecomment-94797",
    "user": "@jasongrout"
}
```

I've uploaded the outputs (for me) of the examples.

plot1.png:

```
g = graphs.DodecahedralGraph()
g.plot3d(viewer='tachyon')
```


plot2.png:

```
g = graphs.DodecahedralGraph()
show(g.plot3d(engine='tachyon'))
```


Why is the first plot way worse than the second?



---

archive/issue_comments_094798.json:
```json
{
    "body": "no problem, I would say",
    "created_at": "2018-01-02T11:03:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9716#issuecomment-94798",
    "user": "@fchapoton"
}
```

no problem, I would say



---

archive/issue_comments_094799.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2018-01-02T11:03:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9716#issuecomment-94799",
    "user": "@fchapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_094800.json:
```json
{
    "body": "Agreed, this should be closed.",
    "created_at": "2018-01-06T03:07:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9716#issuecomment-94800",
    "user": "@kcrisman"
}
```

Agreed, this should be closed.



---

archive/issue_comments_094801.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2018-01-06T17:32:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9716#issuecomment-94801",
    "user": "@fchapoton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_094802.json:
```json
{
    "body": "ok, then let us set this to positive",
    "created_at": "2018-01-06T17:32:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9716#issuecomment-94802",
    "user": "@fchapoton"
}
```

ok, then let us set this to positive



---

archive/issue_comments_094803.json:
```json
{
    "body": "closing positively reviewed duplicates",
    "created_at": "2018-05-18T17:16:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9716#issuecomment-94803",
    "user": "@videlec"
}
```

closing positively reviewed duplicates



---

archive/issue_comments_094804.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2018-05-18T17:16:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9716#issuecomment-94804",
    "user": "@videlec"
}
```

Resolution: wontfix
