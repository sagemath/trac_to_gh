# Issue 3546: line3d with jmol draws curves instead of straight lines

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2008-07-03 21:27:23

Assignee: was

CC:  slelievre


```
sage: line3d([[0,0,0], [1,0,0], [1,1,0], [.5,1.5,0], [0,1,0], [0,0,0]])
```


When rendered with jmol, the lines produced are curves.


---

Comment by mhansen created at 2012-03-28 23:41:31

From the jmol documentation, I don't know if there is anyway to tell it to draw a straight line (instead of a curve).  See http://chemapps.stolaf.edu/jmol/docs/#draw


---

Comment by slelievre created at 2021-04-27 22:00:24

Less important now that the default 3d rendering engine
is Three.js, but still quite puzzling.

One would think `polygon3d` would provide a workaround,
but it lacks `polygon2d`'s options to decide whether
or not to plot the relative interior of the polygon,
the edges, the vertices, and in what colors.


---

Comment by slelievre created at 2021-04-27 22:08:28

Related:

- #3861: Prevent or document automatic line3d smoothing
