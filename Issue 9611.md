# Issue 9611: Truncated numbers on axes in plotting

archive/issues_009611.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  @jasongrout\n\nReported by Henryk Trappmann on sage-support:\n\n```\nTake for example the following code: \nsage: f = {0:1} \nsage: for n in range(100): f[n+1] = sqrt(2.0)**f[n] \nsage: line([(n,f[n]) for n in range(50,100)]) \nThen on the y-Axis every tick number is \"2e\" except the topmost is \n\"2\". \nOne can not distinguish y values by their displayed numbers. \nAnother plot issue: \nIf you change the aspect ratio, then the displayed numbers (i.e. the \nfont) get also scaled, and makes it often unreadable. \nThis can be seen with this code: \nsage: l=line([(1,0.5),(2,0.6)]) \nsage: l.set_aspect_ratio(1) \nsage: l \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9611\n\n",
    "created_at": "2010-07-27T17:38:52Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Truncated numbers on axes in plotting",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9611",
    "user": "https://github.com/kcrisman"
}
```
Assignee: jason, was

CC:  @jasongrout

Reported by Henryk Trappmann on sage-support:

```
Take for example the following code: 
sage: f = {0:1} 
sage: for n in range(100): f[n+1] = sqrt(2.0)**f[n] 
sage: line([(n,f[n]) for n in range(50,100)]) 
Then on the y-Axis every tick number is "2e" except the topmost is 
"2". 
One can not distinguish y values by their displayed numbers. 
Another plot issue: 
If you change the aspect ratio, then the displayed numbers (i.e. the 
font) get also scaled, and makes it often unreadable. 
This can be seen with this code: 
sage: l=line([(1,0.5),(2,0.6)]) 
sage: l.set_aspect_ratio(1) 
sage: l 
```


Issue created by migration from https://trac.sagemath.org/ticket/9611


