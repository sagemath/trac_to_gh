# Issue 2521: Bug in gauss_sum_numerical in degenerate case (probably easy to fix)

archive/issues_002521.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nsage: G = DirichletGroup(4)\nsage: G(1).gauss_sum_numerical()\nTraceback (most recent call last):\n...\nTypeError: 1 must be coercible into Cyclotomic Field of order 2 and degree 1 (and is not an element)\n```\n\n\nInstead the result should be 0:\n\n```\nsage: G(1).gauss_sum()\n0\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2521\n\n",
    "created_at": "2008-03-14T21:24:13Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "Bug in gauss_sum_numerical in degenerate case (probably easy to fix)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2521",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein


```
sage: G = DirichletGroup(4)
sage: G(1).gauss_sum_numerical()
Traceback (most recent call last):
...
TypeError: 1 must be coercible into Cyclotomic Field of order 2 and degree 1 (and is not an element)
```


Instead the result should be 0:

```
sage: G(1).gauss_sum()
0
```


Issue created by migration from https://trac.sagemath.org/ticket/2521





---

archive/issue_comments_017162.json:
```json
{
    "body": "This is fixed in sage-3.0.alpha2:\n\n\n```\nsage: G=DirichletGroup(4)\nsage: G(1).gauss_sum_numerical()\n-1.22464679914735e-16\n```\n\n\nI think it is due to Craig Citro's fixes in the cyclotomic fields code (see #2192).",
    "created_at": "2008-04-13T02:36:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2521#issuecomment-17162",
    "user": "https://github.com/aghitza"
}
```

This is fixed in sage-3.0.alpha2:


```
sage: G=DirichletGroup(4)
sage: G(1).gauss_sum_numerical()
-1.22464679914735e-16
```


I think it is due to Craig Citro's fixes in the cyclotomic fields code (see #2192).



---

archive/issue_comments_017163.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-13T02:53:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2521#issuecomment-17163",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_005920.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2008-04-13T02:53:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2521",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2521#event-5920"
}
```



---

archive/issue_comments_017164.json:
```json
{
    "body": "For the record:\n\n```\n[04:14] <mabshoff> wstein: can you confirm that #2521 is fixed and close it then?\n[04:16] <wstein> yep, is fixed.\n```\n",
    "created_at": "2008-04-13T03:00:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2521#issuecomment-17164",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

For the record:

```
[04:14] <mabshoff> wstein: can you confirm that #2521 is fixed and close it then?
[04:16] <wstein> yep, is fixed.
```

