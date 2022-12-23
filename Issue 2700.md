# Issue 2700: scaling y-axis of plots to fit the data

Issue created by migration from https://trac.sagemath.org/ticket/2700

Original creator: jason

Original creation time: 2008-03-28 17:13:40

Assignee: was


```
>>  I have tried to plot a graphic in the notebook with a small scale (<1)
>>  and it end up by showing up nothing:
>>    sage: var('x')
>>    sage: plot(sin(x), 0, 0.01)
>>
> 
> Try this:
> 
> sage: plot(sin(x), 0, 0.01).show(0,0.01, 0, 0.01)
> 
> The problem is plot's default scale isn't good enough.  using show you can force
> something more useful.


(turning this into a dev discussion :)

You know, we do evaluate the function for lots of points in the interval, so we ought to have a pretty intelligent idea of the max and min of the function.  This ought to let us get a pretty good guess at a ymin and ymax.  If we really wanted to get fancy, we could do a small statistical analysis to throw out outliers too.
```



---

Comment by mhansen created at 2008-09-02 19:49:18

Resolution: fixed


---

Comment by mhansen created at 2008-09-02 19:49:18

This was fixed by #3806.
