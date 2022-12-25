# Issue 1919: improve base fields of DualAbelainGroup

archive/issues_001919.json:
```json
{
    "body": "Assignee: joyner\n\nCC:  @tscrim @jhpalmieri\n\nIn sage/groups/abelian_gps/dual_abelian_group_element.py, the __call__\nmethod uses some code which must be modified if the base field is finite.\nSpecifically, \"zeta = F.gen()\" must be changed.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1919\n\n",
    "created_at": "2008-01-25T02:41:58Z",
    "labels": [
        "component: group theory",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-8.1",
    "title": "improve base fields of DualAbelainGroup",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1919",
    "user": "https://github.com/wdjoyner"
}
```
Assignee: joyner

CC:  @tscrim @jhpalmieri

In sage/groups/abelian_gps/dual_abelian_group_element.py, the __call__
method uses some code which must be modified if the base field is finite.
Specifically, "zeta = F.gen()" must be changed.

Issue created by migration from https://trac.sagemath.org/ticket/1919





---

archive/issue_events_004619.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2017-09-13T19:15:02Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1919",
    "milestone": "sage-8.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1919#event-4619"
}
```



---

archive/issue_comments_012133.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2017-09-13T19:15:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1919#issuecomment-12133",
    "user": "https://github.com/fchapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_012134.json:
```json
{
    "body": "New commits:",
    "created_at": "2017-09-13T19:15:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1919#issuecomment-12134",
    "user": "https://github.com/fchapoton"
}
```

New commits:



---

archive/issue_comments_012135.json:
```json
{
    "body": "another interesting one, simple enough",
    "created_at": "2017-09-20T18:15:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1919#issuecomment-12135",
    "user": "https://github.com/fchapoton"
}
```

another interesting one, simple enough



---

archive/issue_comments_012136.json:
```json
{
    "body": "LGTM.",
    "created_at": "2017-09-20T21:06:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1919#issuecomment-12136",
    "user": "https://github.com/tscrim"
}
```

LGTM.



---

archive/issue_comments_012137.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2017-09-20T21:06:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1919#issuecomment-12137",
    "user": "https://github.com/tscrim"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_004620.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2017-09-24T13:04:01Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1919",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1919#event-4620"
}
```



---

archive/issue_comments_012138.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2017-09-24T13:04:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1919#issuecomment-12138",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
