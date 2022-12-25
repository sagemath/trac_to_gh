# Issue 7296: set_aspect_ratio fails with a type error for asymptote

archive/issues_007296.json:
```json
{
    "body": "Assignee: @williamstein\n\nI test plot for usual functions with set_aspect_ratio(1) to get \"the right plot\".\n\n```\nres=plot(tan(x),x,0,pi/2-0.01)\nres.set_aspect_ratio(1)\nres\n```\n\n\nThis graph isn't pretty but it's the pertinent plot.\n\nThen I plot a new graph closer at x=pi/2 \n\n```\nres=plot(tan(x),x,0,pi/2-0.0001)\nres                          # is right \nres.set_aspect_ratio(1)\nres # I get a system error with a trace \n```\n\n\nIt seems it's an overflow error with a plot too thin.\nheight / width = 10000. \nI expect a warning or an standard error, not this break.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7296\n\n",
    "created_at": "2009-10-25T11:27:38Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "set_aspect_ratio fails with a type error for asymptote",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7296",
    "user": "https://trac.sagemath.org/admin/accounts/users/fmaltey"
}
```
Assignee: @williamstein

I test plot for usual functions with set_aspect_ratio(1) to get "the right plot".

```
res=plot(tan(x),x,0,pi/2-0.01)
res.set_aspect_ratio(1)
res
```


This graph isn't pretty but it's the pertinent plot.

Then I plot a new graph closer at x=pi/2 

```
res=plot(tan(x),x,0,pi/2-0.0001)
res                          # is right 
res.set_aspect_ratio(1)
res # I get a system error with a trace 
```


It seems it's an overflow error with a plot too thin.
height / width = 10000. 
I expect a warning or an standard error, not this break.


Issue created by migration from https://trac.sagemath.org/ticket/7296





---

archive/issue_events_017259.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7296",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7296#event-17259"
}
```



---

archive/issue_events_017260.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7296",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7296#event-17260"
}
```



---

archive/issue_events_017261.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7296",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7296#event-17261"
}
```



---

archive/issue_events_017262.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7296",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7296#event-17262"
}
```



---

archive/issue_events_017263.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7296",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7296#event-17263"
}
```



---

archive/issue_events_017264.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7296",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7296#event-17264"
}
```



---

archive/issue_events_017265.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7296",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7296#event-17265"
}
```
