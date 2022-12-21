# Issue 9981: Allow plotting more complex points

Issue created by migration from Trac.

Original creator: kcrisman

Original creation time: 2010-09-23 18:21:33

Assignee: jason, was

CC:  jason vdelecroix

See #4838 and #8082 for the first addition of this.  Unfortunately, it only supports things like `CC`:


```
sage: point([CC(1.00000000000000 + 0.500000000000000*I)]) # works
sage: point([1.00000000000000 + 0.500000000000000*I]) # nope
```


A little experimentation suggests that Python complexes also aren't supported.  Fixing this should also allow plotting `line`s in the complex plane pretty easily.

I'm labeling this a defect rather than enhancement because it would be confusing not to have both.


---

Comment by kcrisman created at 2012-07-07 03:49:53

Notice that 

```
sage: list_plot([1.00000000000000 + 0.500000000000000*I])
```

does work.


---

Comment by vdelecroix created at 2013-05-24 20:48:53

That's great that you cced me ! I would like to mention that the result of the two following commands are different (and should not be)

```
sage: point2d([CC(0),CC(1)])      # two points at coordinates (0,0) and (1,0)
sage: point2d([CDF(0),CDF(1)])    # one point at coordinate (0,1)
```

Perhaps that will be resolved with this ticket.
