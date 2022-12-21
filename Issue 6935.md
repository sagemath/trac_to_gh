# Issue 6935: Improve documentation for plots with new axis code

Issue created by migration from Trac.

Original creator: kcrisman

Original creation time: 2009-09-15 17:39:04

Assignee: was

CC:  jason

There are a few issues that are left over from #5448, which at the very least should be documented.  None of them are major.

Contour plot - if fill=False and contours are grayscale, the axes could be misinterpreted

Contour plot - show(axes=False) and show(axes=True) seem to be identical on the last example

Plotting - how well documented is the new axis behavior, where it does NOT intersect? This should be clear, e.g. the Riemann zeta example in plot.py looks funny, until you realize it's from 1 to 27. It still seems weird to me when it's that close, but I suppose it's okay as long as it is very very clear in documentation.

Axis labels - should point out difference between ['x','y'] and ['$x$','$y$']. Some people might not like the LaTeXed? version

When scientific notation comes into play is not always clear, and should be in the documentation - compare plot(x**2, 490,500) and plot(x**2,-490,500), which have the same "height" but only one gets e, presumably since it covers a larger range


---

Comment by kcrisman created at 2009-10-05 18:05:01

The first issue is dealt with in #6996, but needed a bit more documentation.  The second issue turned out not to be an issue.

Otherwise documentation has been updated for all these things as appropriate.


---

Attachment

Based on 4.1.2.alpha4


---

Comment by jason created at 2009-10-06 20:46:58

Changing status from needs_review to positive_review.


---

Comment by jason created at 2009-10-06 20:46:58

Looks great!


---

Comment by jason created at 2009-10-06 20:49:55

When we merged #6996, it was understood that this documentation should make it into the same release so that people wouldn't be really confused by the new axes behavior.


---

Comment by mhansen created at 2009-10-19 05:56:45

Resolution: fixed
