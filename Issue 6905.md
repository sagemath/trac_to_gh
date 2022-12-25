# Issue 6905: [with patch, positive review] real(0.0r) is broken

archive/issues_006905.json:
```json
{
    "body": "Assignee: @mwhansen\n\nKeywords: real, symbolic, plot\n\nImplement:\n\nsage: real(0.0r)\n\nNote: imag(0.0r) seems to readily work (using Maxima if I read it well)!\n\n\nFound after getting the following bug report from Francois Maltey:\n\nsage: parametric_plot ((real(exp(i*a)),imag(exp(i*a))),(a,-5,5))\n\nRaises the following warning:\n\nverbose 0 (2999: plot.py, generate_plot_points) WARNING: When plotting, failed to evaluate function at 200 points.\nverbose 0 (2999: plot.py, generate_plot_points) Last error message: ''float' object is not callable'\n\nand yield an empty plot. Investing this further, I got that\n\nsage: var('a'); f = fast_float(real(exp(i*a)),a)\n\nYields a non callable object. Finally Mike H traced it back on IRC to real(0.0r) being broken, because 0.0r.real is an attribute, not a\nmethod.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6905\n\n",
    "closed_at": "2009-09-11T17:30:58Z",
    "created_at": "2009-09-08T21:09:22Z",
    "labels": [
        "component: symbolics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "[with patch, positive review] real(0.0r) is broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6905",
    "user": "https://github.com/nthiery"
}
```
Assignee: @mwhansen

Keywords: real, symbolic, plot

Implement:

sage: real(0.0r)

Note: imag(0.0r) seems to readily work (using Maxima if I read it well)!


Found after getting the following bug report from Francois Maltey:

sage: parametric_plot ((real(exp(i*a)),imag(exp(i*a))),(a,-5,5))

Raises the following warning:

verbose 0 (2999: plot.py, generate_plot_points) WARNING: When plotting, failed to evaluate function at 200 points.
verbose 0 (2999: plot.py, generate_plot_points) Last error message: ''float' object is not callable'

and yield an empty plot. Investing this further, I got that

sage: var('a'); f = fast_float(real(exp(i*a)),a)

Yields a non callable object. Finally Mike H traced it back on IRC to real(0.0r) being broken, because 0.0r.real is an attribute, not a
method.


Issue created by migration from https://trac.sagemath.org/ticket/6905





---

archive/issue_comments_056942.json:
```json
{
    "body": "Attachment [trac_6905.patch](tarball://root/attachments/some-uuid/ticket6905/trac_6905.patch) by @mwhansen created at 2009-09-08 21:13:04",
    "created_at": "2009-09-08T21:13:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6905#issuecomment-56942",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_6905.patch](tarball://root/attachments/some-uuid/ticket6905/trac_6905.patch) by @mwhansen created at 2009-09-08 21:13:04



---

archive/issue_comments_056943.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-09-08T21:13:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6905#issuecomment-56943",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_056944.json:
```json
{
    "body": "Set assignee to @mwhansen.",
    "created_at": "2009-09-08T21:13:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6905#issuecomment-56944",
    "user": "https://github.com/mwhansen"
}
```

Set assignee to @mwhansen.



---

archive/issue_comments_056945.json:
```json
{
    "body": "This trivial patch applies smoothly, passes all test in sage/functions (and most likely elsewhere).\n\nI am no expert of this part of sage, and from the outside it sounds a bit like a workaround. In the long run, it would sound better to fix float to have a \"real\" method,\nand have a consistent implementation of real and imag.\nBut it is simple enough to be safe,and it solves the original problem which hurts casual users. So I put a positive review.\nIf anyone cares, please create a new ticket.",
    "created_at": "2009-09-11T15:27:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6905#issuecomment-56945",
    "user": "https://github.com/nthiery"
}
```

This trivial patch applies smoothly, passes all test in sage/functions (and most likely elsewhere).

I am no expert of this part of sage, and from the outside it sounds a bit like a workaround. In the long run, it would sound better to fix float to have a "real" method,
and have a consistent implementation of real and imag.
But it is simple enough to be safe,and it solves the original problem which hurts casual users. So I put a positive review.
If anyone cares, please create a new ticket.



---

archive/issue_comments_056946.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-11T17:30:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6905#issuecomment-56946",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_016232.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-11T17:30:58Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6905",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6905#event-16232"
}
```
