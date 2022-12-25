# Issue 3717: implement _latex_ method for formal derivative function (in symbolic calculus)

archive/issues_003717.json:
```json
{
    "body": "Assignee: @garyfurnish\n\nKeywords: latex, calculus\n\n```\n> sage: var('c x y t')\n> (c, x, y, t)\n> sage: x=function('x',t)\n> sage: y=function('y',t)\n> sage: f=c*x*y\n> sage: diff(f,t)\n> c*x(t)*diff(y(t), t, 1) + c*y(t)*diff(x(t), t, 1)\n>\n> In the above example, x and y are some functions of t while c is\n> independent of t. If I take the derivative of f=c*x(t)*y(t), I\n> correctly obtain diff(f(t),t)=c*x(t)*diff(y(t), t) + c*y(t)*diff(x(t),\n> t), but for the result looks a bit ugly and does not show well in\n> latex. Can diff(x(t), t) be expressed in a shorter way, such as x'(t),\n> similarly to Mathematica?\n\nTry using \"print\" for a much nicer \"ascii art\" view of symbolic expressions:\n\nsage: print diff(f,t)\n\n                           d                    d\n                   c x(t) (-- (y(t))) + c y(t) (-- (x(t)))\n                           dt                   dt\n\n(Hopefully the \"rich text formatting\" of this email works for you... or\njust try it out.)\n\n> Is there a way of getting derivatives\n> translated into latex code?\n\nYes, this would be easy for us to implement.\n\n\n> Something similar would apply to integrals.\n\nYep, same with my comments.\n\nWilliam\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/3717\n\n",
    "closed_at": "2009-01-18T04:12:28Z",
    "created_at": "2008-07-24T10:06:46Z",
    "labels": [
        "component: calculus"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "implement _latex_ method for formal derivative function (in symbolic calculus)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3717",
    "user": "https://github.com/williamstein"
}
```
Assignee: @garyfurnish

Keywords: latex, calculus

```
> sage: var('c x y t')
> (c, x, y, t)
> sage: x=function('x',t)
> sage: y=function('y',t)
> sage: f=c*x*y
> sage: diff(f,t)
> c*x(t)*diff(y(t), t, 1) + c*y(t)*diff(x(t), t, 1)
>
> In the above example, x and y are some functions of t while c is
> independent of t. If I take the derivative of f=c*x(t)*y(t), I
> correctly obtain diff(f(t),t)=c*x(t)*diff(y(t), t) + c*y(t)*diff(x(t),
> t), but for the result looks a bit ugly and does not show well in
> latex. Can diff(x(t), t) be expressed in a shorter way, such as x'(t),
> similarly to Mathematica?

Try using "print" for a much nicer "ascii art" view of symbolic expressions:

sage: print diff(f,t)

                           d                    d
                   c x(t) (-- (y(t))) + c y(t) (-- (x(t)))
                           dt                   dt

(Hopefully the "rich text formatting" of this email works for you... or
just try it out.)

> Is there a way of getting derivatives
> translated into latex code?

Yes, this would be easy for us to implement.


> Something similar would apply to integrals.

Yep, same with my comments.

William
```

Issue created by migration from https://trac.sagemath.org/ticket/3717





---

archive/issue_comments_026318.json:
```json
{
    "body": "Changing keywords from \"\" to \"latex, calculus\".",
    "created_at": "2008-10-31T03:19:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3717#issuecomment-26318",
    "user": "https://github.com/jhpalmieri"
}
```

Changing keywords from "" to "latex, calculus".



---

archive/issue_comments_026319.json:
```json
{
    "body": "With f as above, if I do `latex(diff(f,t))`, I get\n\n```\n{{c x\\left(t\\right)} {{d}\\over{d\\,t}}\\,y\\left(t\\right)} + {{c y\\left(t\\right)} {{d}\\over{d\\,t}}\\,x\\left(t\\right)}\n```\nSo is there anything to be done here?  I suppose one could quibble about the spacing between the \"d\" and the \"t\", but otherwise, it already looks okay to me.",
    "created_at": "2008-10-31T03:19:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3717#issuecomment-26319",
    "user": "https://github.com/jhpalmieri"
}
```

With f as above, if I do `latex(diff(f,t))`, I get

```
{{c x\left(t\right)} {{d}\over{d\,t}}\,y\left(t\right)} + {{c y\left(t\right)} {{d}\over{d\,t}}\,x\left(t\right)}
```
So is there anything to be done here?  I suppose one could quibble about the spacing between the "d" and the "t", but otherwise, it already looks okay to me.



---

archive/issue_comments_026320.json:
```json
{
    "body": "See #4202 for the ticket that enabled the behavior in the comment.  I believe this ticket can be closed because of #4202.",
    "created_at": "2009-01-18T02:05:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3717#issuecomment-26320",
    "user": "https://github.com/jasongrout"
}
```

See #4202 for the ticket that enabled the behavior in the comment.  I believe this ticket can be closed because of #4202.



---

archive/issue_comments_026321.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-18T04:12:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3717#issuecomment-26321",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_008506.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-18T04:12:28Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3717",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3717#event-8506"
}
```



---

archive/issue_comments_026322.json:
```json
{
    "body": "With Sage 3.3.alpha0 this now works:\n\n```\nsage: k\nc*x(t)*diff(y(t), t, 1) + c*y(t)*diff(x(t), t, 1)\nsage: print(k)\n\n                            d                    d\n                    c x(t) (-- (y(t))) + c y(t) (-- (x(t)))\n                            dt                   dt\nsage: latex(k)\n{{c x\\left(t\\right)} {{{\\it \\partial}}\\over{{\\it \\partial}\\,t}}\\,y\\left(t\\right)} + \n{{c y\\left(t\\right)} {{{\\it \\partial}}\\over{{\\it \\partial}\\,t}}\\,x\\left(t\\right)}\n```\n\nI am closing this ticket as fixed. \n\nCheers,\n\nMichael",
    "created_at": "2009-01-18T04:12:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3717#issuecomment-26322",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

With Sage 3.3.alpha0 this now works:

```
sage: k
c*x(t)*diff(y(t), t, 1) + c*y(t)*diff(x(t), t, 1)
sage: print(k)

                            d                    d
                    c x(t) (-- (y(t))) + c y(t) (-- (x(t)))
                            dt                   dt
sage: latex(k)
{{c x\left(t\right)} {{{\it \partial}}\over{{\it \partial}\,t}}\,y\left(t\right)} + 
{{c y\left(t\right)} {{{\it \partial}}\over{{\it \partial}\,t}}\,x\left(t\right)}
```

I am closing this ticket as fixed. 

Cheers,

Michael



---

archive/issue_events_008507.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-18T04:12:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3717",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3717#event-8507"
}
```
