# Issue 6035: [with patch, needs review] Don't draw vertical asympotes

Issue created by migration from https://trac.sagemath.org/ticket/6035

Original creator: whuss

Original creation time: 2009-05-13 16:43:42

Assignee: whuss

The attached patch adds an option "detect_poles" to the plot command,
which if True detects vertical asymptotes of the plotted function.


```
sage: plot(gamma(x), (x, -3, 4), detect_poles = True).show(ymin = -5, ymax = 5)
```




---

Attachment

This seems to work pretty well, and since its an optional argument I don't see it interfering with any existing code.  The added documentation looks good.


---

Comment by mabshoff created at 2009-05-21 02:07:47

Merged in Sage 4.0.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-21 02:07:47

Resolution: fixed
