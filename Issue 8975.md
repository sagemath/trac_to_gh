# Issue 8975: Methods missing for reducible root systems

archive/issues_008975.json:
```json
{
    "body": "Assignee: @aghitza\n\nThe class sage.combinat.root_system.type_reducible.CartanType\nis missing an is_crystalographic and is_simply_laced\n\n\n```\n sage: R = CartanType(\"D4xA5\")\n sage: R.is_crystalographic()\n sage: R.is_simply_laced()\n```\n\n\nThese both give False which is incorrect.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8975\n\n",
    "created_at": "2010-05-15T21:25:22Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Methods missing for reducible root systems",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8975",
    "user": "https://github.com/BruceWestbury"
}
```
Assignee: @aghitza

The class sage.combinat.root_system.type_reducible.CartanType
is missing an is_crystalographic and is_simply_laced


```
 sage: R = CartanType("D4xA5")
 sage: R.is_crystalographic()
 sage: R.is_simply_laced()
```


These both give False which is incorrect.

Issue created by migration from https://trac.sagemath.org/ticket/8975





---

archive/issue_comments_082670.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-05-12T13:31:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8975",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8975#issuecomment-82670",
    "user": "https://github.com/tscrim"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_082671.json:
```json
{
    "body": "Changing keywords from \"\" to \"days38\".",
    "created_at": "2012-05-12T13:31:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8975",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8975#issuecomment-82671",
    "user": "https://github.com/tscrim"
}
```

Changing keywords from "" to "days38".



---

archive/issue_comments_082672.json:
```json
{
    "body": "This has been taken care of (probably in #6588).\n\n\n```\nsage: R = CartanType(\"D5xA4\")\nsage: R.is_crystalographic()\nTrue\nsage: R.is_simply_laced()\nTrue\n```\n\n\nI'm requesting that this ticket be closed.",
    "created_at": "2012-05-12T13:31:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8975",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8975#issuecomment-82672",
    "user": "https://github.com/tscrim"
}
```

This has been taken care of (probably in #6588).


```
sage: R = CartanType("D5xA4")
sage: R.is_crystalographic()
True
sage: R.is_simply_laced()
True
```


I'm requesting that this ticket be closed.



---

archive/issue_comments_082673.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-05-16T14:03:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8975",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8975#issuecomment-82673",
    "user": "https://github.com/kini"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_082674.json:
```json
{
    "body": "When you want the release manager to close a ticket, you should set it to positive_review, so he will see it.",
    "created_at": "2012-05-16T14:03:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8975",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8975#issuecomment-82674",
    "user": "https://github.com/kini"
}
```

When you want the release manager to close a ticket, you should set it to positive_review, so he will see it.



---

archive/issue_events_021943.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-05-21T07:51:18Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8975",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8975#event-21943"
}
```



---

archive/issue_events_021944.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-05-21T08:06:48Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8975",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8975#event-21944"
}
```



---

archive/issue_comments_082675.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2012-05-21T08:06:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8975",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8975#issuecomment-82675",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: worksforme
