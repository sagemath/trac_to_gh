# Issue 1443: cannot define function variables?

archive/issues_001443.json:
```json
{
    "body": "Assignee: @williamstein\n\nIt seems not possible to create a functional variable in SAGE. This gives strange things:\n\n```\nsage: var('f');\nsage: f(x)\nx\n```\n\nIdeally one should be able to do the following, to compute the formal derivative of f(g(x)):\n\n```\nsage: var('f,g');\nsage: diff(f(g(x)), x)\n```\n\n(Currently this gives 1 due to the above strange simplification f(x) -> x.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/1443\n\n",
    "created_at": "2007-12-09T21:49:26Z",
    "labels": [
        "component: calculus",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "cannot define function variables?",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1443",
    "user": "https://github.com/zimmermann6"
}
```
Assignee: @williamstein

It seems not possible to create a functional variable in SAGE. This gives strange things:

```
sage: var('f');
sage: f(x)
x
```

Ideally one should be able to do the following, to compute the formal derivative of f(g(x)):

```
sage: var('f,g');
sage: diff(f(g(x)), x)
```

(Currently this gives 1 due to the above strange simplification f(x) -> x.)

Issue created by migration from https://trac.sagemath.org/ticket/1443





---

archive/issue_comments_009286.json:
```json
{
    "body": "\n```\nsage: f = function('f')\nsage: f(x)\nf(x)\nsage: g = function('g')\nsage: f(g(x))\nf(g(x))\nsage: diff(f(g(x)),x)\ndiff(f(g(x)), x, 1)\n```\n",
    "created_at": "2007-12-10T07:45:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1443",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1443#issuecomment-9286",
    "user": "https://github.com/mwhansen"
}
```


```
sage: f = function('f')
sage: f(x)
f(x)
sage: g = function('g')
sage: f(g(x))
f(g(x))
sage: diff(f(g(x)),x)
diff(f(g(x)), x, 1)
```




---

archive/issue_comments_009287.json:
```json
{
    "body": "Changing assignee from @williamstein to @mwhansen.",
    "created_at": "2007-12-10T07:45:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1443",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1443#issuecomment-9287",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from @williamstein to @mwhansen.



---

archive/issue_comments_009288.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-10T07:45:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1443",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1443#issuecomment-9288",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_009289.json:
```json
{
    "body": "Use function, as mentioned above:\n\n\n```\nsage: function('f, g')\n(f, g)\nsage: diff(f(g(x)), x)\ndiff(f(g(x)), x, 1)\n```\n",
    "created_at": "2007-12-15T23:39:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1443",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1443#issuecomment-9289",
    "user": "https://github.com/williamstein"
}
```

Use function, as mentioned above:


```
sage: function('f, g')
(f, g)
sage: diff(f(g(x)), x)
diff(f(g(x)), x, 1)
```




---

archive/issue_events_003695.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-12-15T23:40:36Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1443",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1443#event-3695"
}
```



---

archive/issue_comments_009290.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2007-12-15T23:40:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1443",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1443#issuecomment-9290",
    "user": "https://github.com/williamstein"
}
```

Resolution: invalid
