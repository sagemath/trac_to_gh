# Issue 1460: [with patch, with positive review] bug in float( ... ) conversion in calculus

archive/issues_001460.json:
```json
{
    "body": "Assignee: @williamstein\n\n```\nOn Dec 11, 2007 8:39 AM, Joel B. Mohler <joel@kiwistrawberry.us> wrote:\n>\n> Hi,\n>\n> I've noticed a very recent regression -- it worked 2 months ago.\n>\n> sage: t=var('t')\n> sage: f=t*cos(0)\n> sage: float(f(1))\n> 1.0\n> sage: f=t*sin(0)\n> sage: float(f(1))\n> Traceback...\n> <type 'exceptions.TypeError'>: float() argument must be a string or a number\n>\n> --\n\nIt is actually hard to decide how to fix this.   This is a result of\nseveral significant fixes\nand optimizations recently.  What is happening is that for t*sin(0)\nthe simplified\nform is 0, so (t*sin(0)).variables() is [].\n\nsage: t=var('t')\nsage: f = t*cos(0)\nsage: f.variables()\n(t,)\nsage: g = t*sin(0)\nsage: g.variables()\n()\nsage: float(f(1))\n1.0\nsage: float(g(t=1))\n0.0\n\nBoth f(1) and g(1) are formal products.  However:\n\nsage: g(1)._operands\n[t, 0]\nsage: f(1)._operands\n[1, 1]\n\nNotice the [t, 0].\n\nOne possible solution would be to call simplify before\ndoing float(...) -- but that could greatly slow symbolic calculus\ndown in some cases.   Another possibility would be to change\nthe definition of variables() to return all variables, even the ones\nthat are simplified away:\n\nsage: (x - x).variables()   # fake\n(x,)\n\nThat would be very confusing.\n\nA third possibility would be to make implicit calling use variables\nin the unsimplified expression if the simplified expression has\nno variables.  This would cleanly deal with your case above.\n\nThoughts?\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/1460\n\n",
    "closed_at": "2007-12-15T04:45:54Z",
    "created_at": "2007-12-11T16:55:44Z",
    "labels": [
        "component: calculus",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "[with patch, with positive review] bug in float( ... ) conversion in calculus",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1460",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

```
On Dec 11, 2007 8:39 AM, Joel B. Mohler <joel@kiwistrawberry.us> wrote:
>
> Hi,
>
> I've noticed a very recent regression -- it worked 2 months ago.
>
> sage: t=var('t')
> sage: f=t*cos(0)
> sage: float(f(1))
> 1.0
> sage: f=t*sin(0)
> sage: float(f(1))
> Traceback...
> <type 'exceptions.TypeError'>: float() argument must be a string or a number
>
> --

It is actually hard to decide how to fix this.   This is a result of
several significant fixes
and optimizations recently.  What is happening is that for t*sin(0)
the simplified
form is 0, so (t*sin(0)).variables() is [].

sage: t=var('t')
sage: f = t*cos(0)
sage: f.variables()
(t,)
sage: g = t*sin(0)
sage: g.variables()
()
sage: float(f(1))
1.0
sage: float(g(t=1))
0.0

Both f(1) and g(1) are formal products.  However:

sage: g(1)._operands
[t, 0]
sage: f(1)._operands
[1, 1]

Notice the [t, 0].

One possible solution would be to call simplify before
doing float(...) -- but that could greatly slow symbolic calculus
down in some cases.   Another possibility would be to change
the definition of variables() to return all variables, even the ones
that are simplified away:

sage: (x - x).variables()   # fake
(x,)

That would be very confusing.

A third possibility would be to make implicit calling use variables
in the unsimplified expression if the simplified expression has
no variables.  This would cleanly deal with your case above.

Thoughts?
```

Issue created by migration from https://trac.sagemath.org/ticket/1460





---

archive/issue_comments_009381.json:
```json
{
    "body": "Attachment [trac-1460.patch](tarball://root/attachments/some-uuid/ticket1460/trac-1460.patch) by @williamstein created at 2007-12-12 00:27:42",
    "created_at": "2007-12-12T00:27:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1460#issuecomment-9381",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac-1460.patch](tarball://root/attachments/some-uuid/ticket1460/trac-1460.patch) by @williamstein created at 2007-12-12 00:27:42



---

archive/issue_events_003722.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-12-12T00:27:42Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1460",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1460#event-3722"
}
```



---

archive/issue_comments_009382.json:
```json
{
    "body": "The attached patch also greatly improves doctests for the relevant functions.",
    "created_at": "2007-12-12T00:44:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1460#issuecomment-9382",
    "user": "https://github.com/williamstein"
}
```

The attached patch also greatly improves doctests for the relevant functions.



---

archive/issue_comments_009383.json:
```json
{
    "body": "Attachment [trac-1460-doctestnoise.patch](tarball://root/attachments/some-uuid/ticket1460/trac-1460-doctestnoise.patch) by cwitty created at 2007-12-15 04:09:06\n\nLooks good to me.  One of the doctests failed on my machine due to numerical noise; I attached a trivial doctest patch to fix it.  After my patch, all doctests pass in sage/calculus/ and sage/rings/.",
    "created_at": "2007-12-15T04:09:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1460#issuecomment-9383",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [trac-1460-doctestnoise.patch](tarball://root/attachments/some-uuid/ticket1460/trac-1460-doctestnoise.patch) by cwitty created at 2007-12-15 04:09:06

Looks good to me.  One of the doctests failed on my machine due to numerical noise; I attached a trivial doctest patch to fix it.  After my patch, all doctests pass in sage/calculus/ and sage/rings/.



---

archive/issue_events_003723.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-15T04:45:54Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1460",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1460#event-3723"
}
```



---

archive/issue_comments_009384.json:
```json
{
    "body": "Merged in 2.9.rc0.",
    "created_at": "2007-12-15T04:45:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1460#issuecomment-9384",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.9.rc0.



---

archive/issue_comments_009385.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-15T04:45:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1460#issuecomment-9385",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
