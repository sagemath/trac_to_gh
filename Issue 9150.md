# Issue 9150: add colorbars to density plots

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2010-06-05 16:54:10

Assignee: jason, was

CC:  kcrisman

See #8368 for the contour plot patch; probably much of it can be recycled for density plots.


---

Comment by jason created at 2011-04-07 17:01:26

Kirill Vankov (on sage-devel just now) also asked that colorbars be added as an option to matrix plots as well, which would be straightforward once they were added to density plots.


---

Comment by kcrisman created at 2012-10-24 02:26:34

[This ask.sagemath.org question](http://ask.sagemath.org/question/1902/colorbar-for-density-plots) asks for exactly the same thing, and user "Shashank" has a nice mpl example of it.


---

Comment by ppurka created at 2012-10-28 16:47:18

The `Colorbar` class in mpl is a bit strange. It doesn't take in all the options for all kinds of figures. The way it is used in `contour_plot` in Sage works only for that case.
