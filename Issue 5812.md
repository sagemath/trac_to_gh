# Issue 5812: option zorder has no effect for point() and polygon()

Issue created by migration from https://trac.sagemath.org/ticket/5812

Original creator: whuss

Original creation time: 2009-04-17 16:38:25

Assignee: whuss

Currently setting the zorder for points and polygons has no effect although zorder is listed as an allowed option.


```
sage: g = polygon([(0,0), (0,1), (1,1), (1,0)], rgbcolor = 'red', zorder = 0)
sage: g += point((1,1), rgbcolor = 'green', pointsize = 1000, zorder = 1)
sage: g.show()
```



```
sage: g = polygon([(0,0), (0,1), (1,1), (1,0)], rgbcolor = 'red', zorder = 1)
sage: g += point((1,1), rgbcolor = 'green', pointsize = 1000, zorder = 0)
sage: g.show()
```


Both of the above commands currently give the same output.


---

Attachment


---

Comment by kcrisman created at 2009-04-28 20:28:50

Seems to work as advertised - a nice addition!   One question: if I manually set zorder, usually what you expect to happen happens.  But doesn't the order in which the objects are created matter otherwise, if everything has the same zorder?  For instance:

```
sage: p = polygon([(0,0),(0,1),(1,1)])
sage: p+= polygon([(0,0),(0,2),(2,2)],rgbcolor='red')
sage: p.show()
```

gives only a red triangle, while

```
sage: p = polygon([(0,0),(0,2),(2,2)],rgbcolor='red')
sage: p+= polygon([(0,0),(0,1),(1,1)])
sage: p.show()
```

shows the blue triangle on top of the red one.  But

```
sage: g = polygon([(0,0), (0,1), (1,1), (1,0)], rgbcolor = 'red', zorder = 0)
sage: g += point((1,1), rgbcolor = 'green', pointsize = 1000)
sage: g.show()
```

and 

```
sage: g = point((1,1), rgbcolor = 'green', pointsize = 1000)
sage: g += polygon([(0,0), (0,1), (1,1), (1,0)], rgbcolor = 'red', zorder = 0)
sage: g.show()
```

give the same thing, even though they should also have the same zorder at this point, if I understand the code correctly.  Or does the polygon somehow take precedence naturally in matplotlib?

REVIEW

Positive review of fixing the example given.  With regards to the comments above:

If this is a bug or design in matplotlib, positive review.

If it's possible to fix this in one of these files so that the order plots are added behaves consistently, needs work.  

If it's not possible to do that within these files, but it needs to be done in plot.py or show or something, positive review but please open another ticket.


---

Comment by vbraun created at 2009-10-08 19:34:23

I also just tripped over this bug. I checked that the no-brainer patch fixes it. There is no easy way to doctest the graphical output. 

Since the correct patch just sat around for half a year, I will change it to "positive review" in hopes that the patch will be applied.

In case the philosophical issue of how to handle equal zorders ever gets sorted out, please report in bug #6249. But this bug has served its purpose and the patch should be applied asap.


---

Comment by kcrisman created at 2009-10-08 19:37:58

Dear vbraun,

Can you put your full name here?  The release managers like that, as it makes things easier.


---

Comment by kcrisman created at 2009-10-08 19:37:58

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2009-10-08 19:38:44

Then you can also move it to the "positive review" button below.  The new trac workflow will take some getting used to, it's true...


---

Comment by vbraun created at 2009-10-08 19:46:28

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-10-15 16:17:18

Resolution: fixed
