# Issue 6397: [with patch, needs work] implement general Newton's method root finding for power series rings

archive/issues_006397.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  @robertwb @williamstein\n\nKeywords: power series root newton method\n\nExtracting a square root of a power series is implemented in `power_series_ring_element.pyx`.  Could we have the more general \"improving a root of a polynomial\" Newton's method?\n\nMy use case is calculating Puiseaux expansions around points of algebraic curves.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6397\n\n",
    "created_at": "2009-06-24T18:13:21Z",
    "labels": [
        "component: commutative algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-feature",
    "title": "[with patch, needs work] implement general Newton's method root finding for power series rings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6397",
    "user": "https://github.com/ncalexan"
}
```
Assignee: @malb

CC:  @robertwb @williamstein

Keywords: power series root newton method

Extracting a square root of a power series is implemented in `power_series_ring_element.pyx`.  Could we have the more general "improving a root of a polynomial" Newton's method?

My use case is calculating Puiseaux expansions around points of algebraic curves.

Issue created by migration from https://trac.sagemath.org/ticket/6397





---

archive/issue_comments_051299.json:
```json
{
    "body": "Here's a stand-alone implementation that needs to be plugged into the hell that is `polynomial.roots()`.",
    "created_at": "2009-06-24T20:06:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6397",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6397#issuecomment-51299",
    "user": "https://github.com/ncalexan"
}
```

Here's a stand-alone implementation that needs to be plugged into the hell that is `polynomial.roots()`.
