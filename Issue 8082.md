# Issue 8082: correct point and line behavior with complex numbers

Issue created by migration from https://trac.sagemath.org/ticket/8082

Original creator: vdelecroix

Original creation time: 2010-01-26 18:37:49

Assignee: vdelecroix

Keywords: plot

We have a strange behavior


```
sage: point(CC(0))  # plot a point with coordinates (0, 0)
sage: point(CC(1))  # plot a point with coordinates (1, 0)
sage: point([CC(0),CC(1)])  # plot a point with coordinates (0, 1)
```


This patch add a line in sage.plot to correct this and get the two points (0,0) and (1,0) when doing


```
sage: point([CC(0), CC(1)])
```



---

Attachment


---

Comment by vdelecroix created at 2010-01-26 18:47:16

Changing status from new to needs_review.


---

Comment by vdelecroix created at 2010-01-26 18:47:16

Changing keywords from "plot" to "plot, complex numbers".


---

Comment by vdelecroix created at 2010-01-27 17:22:47

Changing status from needs_review to needs_work.


---

Comment by vdelecroix created at 2010-01-29 22:29:27

Changing status from needs_work to needs_review.


---

Comment by rossk created at 2010-01-31 10:28:12

Changing status from needs_review to positive_review.


---

Comment by rossk created at 2010-01-31 10:28:12

Works as advertised


```
# (1) pre-patch, this plotted a point with coordinates (0, 1)
# (2) post-patch, this plots 2 points at (0,0) and (1,0) as designed
sage: point([CC(0),CC(1)])

# plot the 8 vertices of an octagon
sage: point([CC(cos(theta)+I*sin(theta)) for theta in srange(0, 2*pi, pi/4)],aspect_ratio=1)
```



---

Comment by mpatel created at 2010-02-10 15:25:46

The patch commit string is insufficiently descriptive. I've refreshed it to `#8082: Correct point and line behavior with complex numbers` in the queue for 4.3.3.alpha0.


---

Comment by mpatel created at 2010-02-11 14:57:40

Resolution: fixed
