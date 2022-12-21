# Issue 7296: set_aspect_ratio fails with a type error for asymptote

Issue created by migration from Trac.

Original creator: fmaltey

Original creation time: 2009-10-25 11:27:38

Assignee: was

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

