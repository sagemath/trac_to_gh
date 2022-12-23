# Issue 1862: implement at least some sort of useful rudimentary implicit 2d plotting function

Issue created by migration from https://trac.sagemath.org/ticket/1862

Original creator: was

Original creation time: 2008-01-20 07:52:09

Assignee: was

CC:  harald.schilly@gmail.com


```
{{{
On Jan 19, 2008 12:44 AM, Dagda <> wrote:
> 
> Hi,
> I was wondering if there was a way to plot relations implicitly, in 2D
> and/or 3D. A simple example would be to plot a circle with something
> like the following:
> 
> plot_implicit(x^2+y^2=1)

Here's how do this sort of thing using contour_plot in sage right now.
(Note -- for efficiency reasons, you definitely want to only plot a Python
function -- i.e., lambda -- at present.  This will change soon.)

First, define this function in Sage:

def implicit_plot(f, x_range, y_range, plot_points=100):
      return contour_plot(f, x_range, y_range, fill=False, contours=1, plot_points=plot_points)

Then use it:

sage: implicit_plot(lambda x,y: x^2 + y^2 - 1, (-2,2), (-2,2))
sage: implicit_plot(lambda x,y: x^3 + x*y^2 - 1, (-2,2), (-2,2))
sage: implicit_plot(lambda x,y: (x-y^2)*(y-x^3), (-2,2), (-2,2))

The input should be a function f of two variables, and implicit_plot as I've
defined it above graphs f(x,y) == 0 in the given region.

This could be turned into a first version of a genuine implicit plot at some point. 

Josh Kantor is also looking into some other more sophisticated related
approaches.    It would be good to understand precisely how Sage's
contour_plot function works (it builds mostly on matplotlib's functions)....

William
}}}


---

Comment by mabshoff created at 2008-01-26 13:55:26

Robert Bradshaw's bundle at #1938 includes this functionality.

Cheers,

Michael


---

Comment by was created at 2008-01-27 17:10:36

> Robert Bradshaw's bundle at #1938 includes this functionality.


I just refereed that patch and I can't find any implicit_plot functionality in it...


---

Attachment


---

Comment by cwitty created at 2008-03-02 18:33:25

This patch adds implicit_plot (based on contour_plot, as William suggests).  It also fixes some broken code (and adds doctests) elsewhere in plot.py .


---

Comment by wdj created at 2008-03-03 12:40:07

Some problems:

```
sage: x,y=var("x,y")
sage: implicit_plot(x^2+y^2-1,(-1,1),(-1,1))
```

takes a very long time (in fact, I tried to kill it using ctl-c repeatedly and had a hard time).
On the other hand,

```
sage: f = lambda x,y: x^2+y^2-1
sage: implicit_plot(f,(-1,1),(-1,1))
```

is almost instantaneous.
Can this be fixed or at least documented?


---

Comment by was created at 2008-03-03 13:53:50

> Can this be fixed or at least documented?

This should be trivial to fix by changing implicit_plot to call fast_float.  In fact, then the relevant part of your first example would be 10 times faster than the second.


---

Attachment

I've put up a version of the patch ( 1862.patch ) rebased against 2.10.4.alpha0.  That's the one that should be applied.  Other than that, looks good to me.


---

Comment by mabshoff created at 2008-03-16 02:53:05

Resolution: fixed


---

Comment by mabshoff created at 2008-03-16 02:53:05

Merged 1862.patch in Sage 2.10.4.rc0
