# Issue 7296: set_aspect_ratio fails with a type error for asymptote

archive/issues_007296.json:
```json
{
    "body": "Assignee: @williamstein\n\nI test plot for usual functions with set_aspect_ratio(1) to get \"the right plot\".\n\n```\nres=plot(tan(x),x,0,pi/2-0.01)\nres.set_aspect_ratio(1)\nres\n```\n\n\nThis graph isn't pretty but it's the pertinent plot.\n\nThen I plot a new graph closer at x=pi/2 \n\n```\nres=plot(tan(x),x,0,pi/2-0.0001)\nres                          # is right \nres.set_aspect_ratio(1)\nres # I get a system error with a trace \n```\n\n\nIt seems it's an overflow error with a plot too thin.\nheight / width = 10000. \nI expect a warning or an standard error, not this break.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7296\n\n",
    "created_at": "2009-10-25T11:27:38Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "set_aspect_ratio fails with a type error for asymptote",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7296",
    "user": "fmaltey"
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


