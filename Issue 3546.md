# Issue 3546: line3d with jmol draws curves instead of straight lines

archive/issues_003546.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @slel\n\nDefine a pentagon in three dimensions.\n\n```\nsage: pts = [[0,0,0], [1,0,0], [1,1,0], [.5,1.5,0], [0,1,0], [0,0,0]]\nsage: p = line3d(pts)\nsage: q = polygon3d(pts, color='teal', opacity=0.25)\nsage: pq = p + q\n```\nWith Three.js, the `line3d` renders\npolygonally as the outline of the pentagon.\n\n```\nsage: pq.show(viewer='threejs')\nLaunched jmol viewer for Graphics3d Object\n```\nWith Jmol, the `line3d` renders curved,\nin the shape of a shield.\n\n```\nsage: pq.show(viewer='jmol')\nLaunched jmol viewer for Graphics3d Object\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3546\n\n",
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

Define a pentagon in three dimensions.

```
sage: pts = [[0,0,0], [1,0,0], [1,1,0], [.5,1.5,0], [0,1,0], [0,0,0]]
sage: p = line3d(pts)
sage: q = polygon3d(pts, color='teal', opacity=0.25)
sage: pq = p + q
```
With Three.js, the `line3d` renders
polygonally as the outline of the pentagon.

```
sage: pq.show(viewer='threejs')
Launched jmol viewer for Graphics3d Object
```
With Jmol, the `line3d` renders curved,
in the shape of a shield.

```
sage: pq.show(viewer='jmol')
Launched jmol viewer for Graphics3d Object
```


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

archive/issue_events_008115.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3546",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3546#event-8115"
}
```



---

archive/issue_events_008116.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3546",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3546#event-8116"
}
```



---

archive/issue_events_008117.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3546",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3546#event-8117"
}
```



---

archive/issue_events_008118.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3546",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3546#event-8118"
}
```



---

archive/issue_events_008119.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3546",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3546#event-8119"
}
```



---

archive/issue_events_008120.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3546",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3546#event-8120"
}
```



---

archive/issue_events_008121.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3546",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3546#event-8121"
}
```



---

archive/issue_events_008122.json:
```json
{
    "actor": "https://github.com/slel",
    "created_at": "2021-04-27T22:00:24Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3546",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3546#event-8122"
}
```



---

archive/issue_events_008123.json:
```json
{
    "actor": "https://github.com/slel",
    "created_at": "2021-04-27T22:00:24Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3546",
    "milestone": "sage-wishlist",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3546#event-8123"
}
```



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
