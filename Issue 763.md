# Issue 763: serious bug latexing p-adic L-series

archive/issues_000763.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe following are the same L-series twice, but the latex print version is missing the alphas!!\n\n\n```\nsage: E = EllipticCurve('37a')\nsage: L = E.padic_lseries(3)\nsage: L.series(4)\n(O(3^1))*alpha + (O(3^2)) + ((O(3^-1))*alpha + (2*3^-1 + O(3^0)))*T + ((O(3^-1))*alpha + (2*3^-1 + O(3^0)))*T^2 + ((O(3^-2))*alpha + (O(3^-1)))*T^3 + ((O(3^-1))*alpha + (3^-1 + O(3^0)))*T^4 + O(T^5)\nsage: latex(L.series(4))\n\\left(2 \\cdot 3^{-1} + O(3^{0})\\right)T + \\left(2 \\cdot 3^{-1} + O(3^{0})\\right)T^{2} + \\left(3^{-1} + O(3^{0})\\right)T^{4} + O(\\left(1 + O(3^{5})\\right)T^{5})\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/763\n\n",
    "created_at": "2007-09-30T05:26:46Z",
    "labels": [
        "component: number theory",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.6",
    "title": "serious bug latexing p-adic L-series",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/763",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

The following are the same L-series twice, but the latex print version is missing the alphas!!


```
sage: E = EllipticCurve('37a')
sage: L = E.padic_lseries(3)
sage: L.series(4)
(O(3^1))*alpha + (O(3^2)) + ((O(3^-1))*alpha + (2*3^-1 + O(3^0)))*T + ((O(3^-1))*alpha + (2*3^-1 + O(3^0)))*T^2 + ((O(3^-2))*alpha + (O(3^-1)))*T^3 + ((O(3^-1))*alpha + (3^-1 + O(3^0)))*T^4 + O(T^5)
sage: latex(L.series(4))
\left(2 \cdot 3^{-1} + O(3^{0})\right)T + \left(2 \cdot 3^{-1} + O(3^{0})\right)T^{2} + \left(3^{-1} + O(3^{0})\right)T^{4} + O(\left(1 + O(3^{5})\right)T^{5})
```


Issue created by migration from https://trac.sagemath.org/ticket/763





---

archive/issue_comments_004503.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-04T00:46:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/763#issuecomment-4503",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to assigned.



---

archive/issue_events_000860.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2007-10-04T03:25:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/763",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/763#event-860"
}
```



---

archive/issue_comments_004504.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-04T03:25:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/763#issuecomment-4504",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
