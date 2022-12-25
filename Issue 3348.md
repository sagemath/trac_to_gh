# Issue 3348: Coercion problem: creating vectors from a mix of python and symbolic types

archive/issues_003348.json:
```json
{
    "body": "Assignee: @robertwb\n\nIn the following (isomorphic) cases, the first entry is floored\n\n```\nsage: vector(eval(\"[0.78, 1, 1 + 2.38 * I]\"))\n(0, 1, 2.38000000000000*I + 1)\nsage: vector([float(5.52), int(1), 1.3*x])\n(5, 1, 1.30000000000000*x)\n```\n\nNote: the order of the types here seems to have to be (float, int, symbolic ring) for this to occur.  If one uses proper Sage types, the problem goes away:\n\n```\nvector(sage_eval(\"[0.78, 1, 1 + 2.38 * I]\"))\n(0.780000000000000, 1.00000000000000, 2.38000000000000*I + 1)\n```\n\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3348\n\n",
    "created_at": "2008-06-01T20:22:01Z",
    "labels": [
        "component: coercion",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Coercion problem: creating vectors from a mix of python and symbolic types",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3348",
    "user": "https://github.com/NathanDunfield"
}
```
Assignee: @robertwb

In the following (isomorphic) cases, the first entry is floored

```
sage: vector(eval("[0.78, 1, 1 + 2.38 * I]"))
(0, 1, 2.38000000000000*I + 1)
sage: vector([float(5.52), int(1), 1.3*x])
(5, 1, 1.30000000000000*x)
```

Note: the order of the types here seems to have to be (float, int, symbolic ring) for this to occur.  If one uses proper Sage types, the problem goes away:

```
vector(sage_eval("[0.78, 1, 1 + 2.38 * I]"))
(0.780000000000000, 1.00000000000000, 2.38000000000000*I + 1)
```





Issue created by migration from https://trac.sagemath.org/ticket/3348





---

archive/issue_comments_023231.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-06-04T22:55:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3348",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3348#issuecomment-23231",
    "user": "https://github.com/mwhansen"
}
```

Resolution: invalid



---

archive/issue_comments_023232.json:
```json
{
    "body": "This has been fixed in the switch to Pynac symbolics:\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: sage: vector(eval(\"[0.78, 1, 1 + 2.38 * I]\"))\n(0.78, 1.0, 1.00000000000000 + 2.38000000000000*I)\nsage: _.parent()\nVector space of dimension 3 over Symbolic Ring\nsage: sage: vector([float(5.52), int(1), 1.3*x])\n(5.52, 1.0, 1.30000000000000*x)\nsage: _.parent()\nVector space of dimension 3 over Symbolic Ring\nsage: vector(sage_eval(\"[0.78, 1, 1 + 2.38 * I]\"))\n(0.780000000000000, 1.00000000000000, 1.00000000000000 + 2.38000000000000*I)\nsage: _.parent()\nVector space of dimension 3 over Symbolic Ring\n```\n",
    "created_at": "2009-06-04T22:55:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3348",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3348#issuecomment-23232",
    "user": "https://github.com/mwhansen"
}
```

This has been fixed in the switch to Pynac symbolics:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: sage: vector(eval("[0.78, 1, 1 + 2.38 * I]"))
(0.78, 1.0, 1.00000000000000 + 2.38000000000000*I)
sage: _.parent()
Vector space of dimension 3 over Symbolic Ring
sage: sage: vector([float(5.52), int(1), 1.3*x])
(5.52, 1.0, 1.30000000000000*x)
sage: _.parent()
Vector space of dimension 3 over Symbolic Ring
sage: vector(sage_eval("[0.78, 1, 1 + 2.38 * I]"))
(0.780000000000000, 1.00000000000000, 1.00000000000000 + 2.38000000000000*I)
sage: _.parent()
Vector space of dimension 3 over Symbolic Ring
```




---

archive/issue_events_003566.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2009-06-04T22:55:41Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3348",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3348#event-3566"
}
```
