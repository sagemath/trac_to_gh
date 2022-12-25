# Issue 9408: relativize in number fields is broken

archive/issues_009408.json:
```json
{
    "body": "Assignee: @loefflerd\n\nKeywords: relativize\n\nDoes not work due to (maybe) denominators\n\n```\nsage: K.<a> = NumberField(x^4-4*x^3+12*x^2-16*x+8)\nsage: L.<u,v> = K.relativize(3*a**3 - 9*a**2 + 24*a -16)\nsage:#This seems OK\nsage: L2.<u2,v2> = K.relativize((3/4)*a**3 - (9/4)*a**2 + 6*a -4)\n```\nPariError:  (8)\n\nSimpler example\n\n```\nsage: L.<a,b> = QQ[i].relativize(1) #Ok\nsage: L.<a,b> = QQ[i].relativize(1/2) #PariError\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/9408\n\n",
    "created_at": "2010-07-02T16:04:23Z",
    "labels": [
        "component: number fields",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "relativize in number fields is broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9408",
    "user": "https://github.com/lftabera"
}
```
Assignee: @loefflerd

Keywords: relativize

Does not work due to (maybe) denominators

```
sage: K.<a> = NumberField(x^4-4*x^3+12*x^2-16*x+8)
sage: L.<u,v> = K.relativize(3*a**3 - 9*a**2 + 24*a -16)
sage:#This seems OK
sage: L2.<u2,v2> = K.relativize((3/4)*a**3 - (9/4)*a**2 + 6*a -4)
```
PariError:  (8)

Simpler example

```
sage: L.<a,b> = QQ[i].relativize(1) #Ok
sage: L.<a,b> = QQ[i].relativize(1/2) #PariError
```

Issue created by migration from https://trac.sagemath.org/ticket/9408





---

archive/issue_comments_089521.json:
```json
{
    "body": "This ticket should be closed as duplicate of #252",
    "created_at": "2010-07-06T10:58:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9408#issuecomment-89521",
    "user": "https://github.com/lftabera"
}
```

This ticket should be closed as duplicate of #252



---

archive/issue_comments_089522.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2010-07-06T10:58:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9408#issuecomment-89522",
    "user": "https://github.com/lftabera"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_089523.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2011-06-07T08:58:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9408#issuecomment-89523",
    "user": "https://github.com/lftabera"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_events_023236.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-10-15T12:50:47Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9408",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9408#event-23236"
}
```



---

archive/issue_comments_089524.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-10-15T12:50:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9408#issuecomment-89524",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_023237.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-11-15T09:21:27Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9408",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9408#event-23237"
}
```



---

archive/issue_comments_089525.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2011-11-15T09:21:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9408#issuecomment-89525",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate
