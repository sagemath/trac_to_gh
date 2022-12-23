# Issue 9611: Truncated numbers on axes in plotting

Issue created by migration from https://trac.sagemath.org/ticket/9611

Original creator: kcrisman

Original creation time: 2010-07-27 17:38:52

Assignee: jason, was

CC:  jason

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

