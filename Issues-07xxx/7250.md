# Issue 7250: cached_function broken for builtin functions

archive/issues_007250.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  @craigcitro boothby @rlmill\n\nKeywords: cached function\n\nThis used to work before #6937:\n\n```\n    sage: f = cached_function(sage.structure.element.is_RingElement)\n    sage: f(1)\n    True\n```\n\nThat's used at one spot in the category code (but we can disable it temporarily)\n\nIssue created by migration from https://trac.sagemath.org/ticket/7250\n\n",
    "closed_at": "2013-07-23T15:41:21Z",
    "created_at": "2009-10-19T21:43:40Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "cached_function broken for builtin functions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7250",
    "user": "https://github.com/nthiery"
}
```
Assignee: cwitty

CC:  @craigcitro boothby @rlmill

Keywords: cached function

This used to work before #6937:

```
    sage: f = cached_function(sage.structure.element.is_RingElement)
    sage: f(1)
    True
```

That's used at one spot in the category code (but we can disable it temporarily)

Issue created by migration from https://trac.sagemath.org/ticket/7250





---

archive/issue_comments_060116.json:
```json
{
    "body": "On 5.6b1 I get\n\n```\nsage: f = cached_function(sage.structure.element.is_RingElement)\nsage: f(1)\nTrue\nsage: f(False)\nFalse\nsage: f(True)\nTrue\nsage: f(x)\nTrue\nsage: f(0)\nFalse\nsage: f.get_cache()\n{((1,), ()): True, ((x,), ()): True, ((False,), ()): False}\n```\nso it seems to work well enough now. Of course, `f(0)` and `f(True)` give funny answers because this the computed value is not a function on equality classes of the inputs (i.e., `0==False` and `1==True`, but `is_RingElement` doesn't have the same value on them).\n\nThe documentation of `cached_function` could do a better job of pointing out this gotcha (it mentions arguments should be hashable, but not that different but equal arguments will trigger cache use).\n\nAnyway, I guess this ticket can be closed or be used to improve the documentation.",
    "created_at": "2013-01-09T21:03:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7250#issuecomment-60116",
    "user": "https://github.com/nbruin"
}
```

On 5.6b1 I get

```
sage: f = cached_function(sage.structure.element.is_RingElement)
sage: f(1)
True
sage: f(False)
False
sage: f(True)
True
sage: f(x)
True
sage: f(0)
False
sage: f.get_cache()
{((1,), ()): True, ((x,), ()): True, ((False,), ()): False}
```
so it seems to work well enough now. Of course, `f(0)` and `f(True)` give funny answers because this the computed value is not a function on equality classes of the inputs (i.e., `0==False` and `1==True`, but `is_RingElement` doesn't have the same value on them).

The documentation of `cached_function` could do a better job of pointing out this gotcha (it mentions arguments should be hashable, but not that different but equal arguments will trigger cache use).

Anyway, I guess this ticket can be closed or be used to improve the documentation.



---

archive/issue_events_017162.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2013-07-23T15:41:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7250",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7250#event-17162"
}
```



---

archive/issue_comments_060117.json:
```json
{
    "body": "I would say that it can be closed.",
    "created_at": "2013-07-23T15:41:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7250#issuecomment-60117",
    "user": "https://github.com/mwhansen"
}
```

I would say that it can be closed.



---

archive/issue_comments_060118.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2013-07-23T15:41:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7250#issuecomment-60118",
    "user": "https://github.com/mwhansen"
}
```

Resolution: invalid



---

archive/issue_events_017163.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2013-07-23T15:41:21Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7250",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7250#event-17163"
}
```
