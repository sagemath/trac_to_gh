# Issue 8393: bring plot3d.py to 100% coverage

archive/issues_008393.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @kcrisman\n\nKeywords: coverage, doctests, plot3d\n\nplot3d.py is only missing three doctests to get to 100%:\n\n```\nsage -coverage devel/sage-p1/sage/plot/plot3d/plot3d.py \n----------------------------------------------------------------------\ndevel/sage-p1/sage/plot/plot3d/plot3d.py\nERROR: Please add a `TestSuite(s).run()` doctest.\nSCORE devel/sage-p1/sage/plot/plot3d/plot3d.py: 81% (13 of 16)\n\nMissing documentation:\n * triangle(self, a, b, c, color = None):\n * smooth_triangle(self, a, b, c, da, db, dc, color = None):\n * axes(scale=1, radius=None, **kwds):\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/8393\n\n",
    "closed_at": "2012-07-17T08:33:35Z",
    "created_at": "2010-02-28T14:36:59Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "bring plot3d.py to 100% coverage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8393",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```
Assignee: @williamstein

CC:  @kcrisman

Keywords: coverage, doctests, plot3d

plot3d.py is only missing three doctests to get to 100%:

```
sage -coverage devel/sage-p1/sage/plot/plot3d/plot3d.py 
----------------------------------------------------------------------
devel/sage-p1/sage/plot/plot3d/plot3d.py
ERROR: Please add a `TestSuite(s).run()` doctest.
SCORE devel/sage-p1/sage/plot/plot3d/plot3d.py: 81% (13 of 16)

Missing documentation:
 * triangle(self, a, b, c, color = None):
 * smooth_triangle(self, a, b, c, da, db, dc, color = None):
 * axes(scale=1, radius=None, **kwds):
```

Issue created by migration from https://trac.sagemath.org/ticket/8393





---

archive/issue_comments_075081.json:
```json
{
    "body": "```\n\n$ ../../sage -coverage sage/plot/plot3d/plot3d.py \n----------------------------------------------------------------------\nsage/plot/plot3d/plot3d.py\nERROR: Please add a `TestSuite(s).run()` doctest.\nSCORE sage/plot/plot3d/plot3d.py: 100% (18 of 18)\n----------------------------------------------------------------------\n```\nThis was fixed by #12491.",
    "created_at": "2012-07-07T03:35:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8393",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8393#issuecomment-75081",
    "user": "https://github.com/kcrisman"
}
```

```

$ ../../sage -coverage sage/plot/plot3d/plot3d.py 
----------------------------------------------------------------------
sage/plot/plot3d/plot3d.py
ERROR: Please add a `TestSuite(s).run()` doctest.
SCORE sage/plot/plot3d/plot3d.py: 100% (18 of 18)
----------------------------------------------------------------------
```
This was fixed by #12491.



---

archive/issue_comments_075082.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-07-07T03:35:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8393",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8393#issuecomment-75082",
    "user": "https://github.com/kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_075083.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-07-07T03:35:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8393",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8393#issuecomment-75083",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_020128.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-07-08T13:59:48Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8393",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8393#event-20128"
}
```



---

archive/issue_comments_075084.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2012-07-17T08:33:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8393",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8393#issuecomment-75084",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate



---

archive/issue_events_020129.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-07-17T08:33:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8393",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8393#event-20129"
}
```
