# Issue 6292: Converting elements in AbelianGroup to gap element

archive/issues_006292.json:
```json
{
    "body": "Assignee: joyner\n\nKeywords: AbelianGroup\n\nSome trouble in converting elements in AbelianGroup to gap elements\nFor example we can do this;\n\n```\nsage: G = SymmetricGroup(5)\nsage: g = G.list()[2]\nsage: H = gap(G)\nsage: g in H\nTrue\n```\n\nBut not this;\n\n```\nsage: G = AbelianGroup([2,2])\nsage: g = G.list()[2]\nsage: H = gap(G)\nsage: g in H\n[...]\nTypeError: Gap produced error output\nVariable: 'f0' must have a value\n```\n\n\n\nSimilarly we can't go back the other way around.\nThat is we can do this;\n\n```\nsage: G = SymmetricGroup(5)\nsage: H = gap(G)\nsage: r = H.ConjugacyClasses()[2].Representative()\nsage: type(r)\n<class 'sage.interfaces.gap.GapElement'>\nsage: r in G\nTrue\nsage: G(r)\n(1,2)\n```\n\n\nBut not this\n\n```\nsage: G = AbelianGroup([2,2])\nsage: H = gap(G)\nsage: r = H.ConjugacyClasses()[2].Representative()\nsage: r\nf1\nsage: r in G\nFalse\nsage: G(r)\n[...]\nTypeError: Argument x (= f1) is of wrong type.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6292\n\n",
    "created_at": "2009-06-15T04:08:59Z",
    "labels": [
        "component: group theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Converting elements in AbelianGroup to gap element",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6292",
    "user": "https://trac.sagemath.org/admin/accounts/users/jlefebvre"
}
```
Assignee: joyner

Keywords: AbelianGroup

Some trouble in converting elements in AbelianGroup to gap elements
For example we can do this;

```
sage: G = SymmetricGroup(5)
sage: g = G.list()[2]
sage: H = gap(G)
sage: g in H
True
```

But not this;

```
sage: G = AbelianGroup([2,2])
sage: g = G.list()[2]
sage: H = gap(G)
sage: g in H
[...]
TypeError: Gap produced error output
Variable: 'f0' must have a value
```



Similarly we can't go back the other way around.
That is we can do this;

```
sage: G = SymmetricGroup(5)
sage: H = gap(G)
sage: r = H.ConjugacyClasses()[2].Representative()
sage: type(r)
<class 'sage.interfaces.gap.GapElement'>
sage: r in G
True
sage: G(r)
(1,2)
```


But not this

```
sage: G = AbelianGroup([2,2])
sage: H = gap(G)
sage: r = H.ConjugacyClasses()[2].Representative()
sage: r
f1
sage: r in G
False
sage: G(r)
[...]
TypeError: Argument x (= f1) is of wrong type.
```


Issue created by migration from https://trac.sagemath.org/ticket/6292





---

archive/issue_events_014707.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6292",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6292#event-14707"
}
```



---

archive/issue_events_014708.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6292",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6292#event-14708"
}
```



---

archive/issue_events_014709.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6292",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6292#event-14709"
}
```



---

archive/issue_events_014710.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6292",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6292#event-14710"
}
```



---

archive/issue_events_014711.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6292",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6292#event-14711"
}
```



---

archive/issue_events_014712.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6292",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6292#event-14712"
}
```



---

archive/issue_events_014713.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6292",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6292#event-14713"
}
```
