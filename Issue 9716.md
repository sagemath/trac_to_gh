# Issue 9716: tachyon 3d plotting of graphs is still screwy

Issue created by migration from https://trac.sagemath.org/ticket/9716

Original creator: was

Original creation time: 2010-08-10 04:28:12

Assignee: jason, ncohen, rlm

CC:  mhampton

This looks like crap:

```
g = graphs.DodecahedralGraph()
g.plot3d(viewer='tachyon')
```

but this looks good:

```
g = graphs.DodecahedralGraph()
show(g.plot3d(engine='tachyon'))
```

Also, this doesn't work (show a plot) at all:

```
g = graphs.DodecahedralGraph()
g.plot3d(engine='tachyon')
```


That's at least 2 bugs / sloppinesses. 




---

Comment by jason created at 2010-09-03 20:43:21

first example


---

Attachment

second example


---

Comment by jason created at 2010-09-03 20:45:02

I've uploaded the outputs (for me) of the examples.

plot1.png:

```
g = graphs.DodecahedralGraph()
g.plot3d(viewer='tachyon')
```


plot2.png:

```
g = graphs.DodecahedralGraph()
show(g.plot3d(engine='tachyon'))
```


Why is the first plot way worse than the second?


---

Comment by chapoton created at 2018-01-02 11:03:05

no problem, I would say


---

Comment by chapoton created at 2018-01-02 11:03:05

Changing status from new to needs_review.


---

Comment by kcrisman created at 2018-01-06 03:07:49

Agreed, this should be closed.


---

Comment by chapoton created at 2018-01-06 17:32:18

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2018-01-06 17:32:18

ok, then let us set this to positive


---

Comment by vdelecroix created at 2018-05-18 17:16:26

closing positively reviewed duplicates


---

Comment by vdelecroix created at 2018-05-18 17:16:26

Resolution: wontfix
