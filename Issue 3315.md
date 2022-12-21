# Issue 3315: parametric plot should accept a function that returns a tuple

Issue created by migration from Trac.

Original creator: mhampton

Original creation time: 2008-05-27 19:06:22

Assignee: was

Keywords: parametric_plot

Subject says it all.  I (Marshall Hampton) will work on this if I have time; should be pretty easy.  Currently parametric_plot wants a tuple of functions; I think it should do that OR accept a function that returns a tuple.


---

Comment by jason created at 2009-03-06 21:35:52

See also #3313 for another input format parametric_plot should take: vectors.


---

Comment by jason created at 2009-03-06 21:37:03

Really, parametric_plot should take functions returning any of the allowed types (tuple, list, or with #3313, vectors).


---

Comment by jason created at 2010-05-11 20:43:36

Replying to [comment:1 jason]:
> See also #3313 for another input format parametric_plot should take: vectors.

#3313 has nothing to do with vectors.  And now, parametric_plot takes vectors anyway:


```
sage: r(t)=[t,t+1]
sage: parametric_plot(r, (t,0,1))

sage: parametric_plot(r(t), (t,0,1))

```

