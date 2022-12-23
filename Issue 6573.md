# Issue 6573: fix docstring from #5651

Issue created by migration from https://trac.sagemath.org/ticket/6573

Original creator: mvngu

Original creation time: 2009-07-20 20:55:23

Assignee: tba

CC:  wcauchois davidloeffler

That rebased patch at #5651 contains doctrings that doesn't conform with conventions for formatting docstrings. In particular, in sage/plot/bar_chart.py:

```
131	    Extra options will get passed on to show(), as long as they are valid:
```

In sage/plot/bezier_path.py:

```
171	    Extra options will get passed on to show(), as long as they are valid:
```

In sage/plot/matrix_plot.py:

```
58	    Extra options will get passed on to show(), as long as they are valid:
62	    Extra options will get passed on to show(), as long as they are valid:
```

In sage/plot/polygon.py:

```
255	    Extra options will get passed on to show(), as long as they are valid:
```



---

Comment by mvngu created at 2009-07-21 14:26:38

based on Sage 4.1.1.alpha0


---

Attachment

David: Can I ask you to review this?


---

Attachment


---

Comment by davidloeffler created at 2009-07-21 15:01:27

Looks fine to me; but it looks like the Bezier paths module isn't in the reference manual. I've uploaded a tiny patch that fixes this.


---

Comment by mvngu created at 2009-07-23 05:09:57

Resolution: fixed


---

Comment by mvngu created at 2009-07-23 05:09:57

Merged both patches.
