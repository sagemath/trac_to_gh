# Issue 5553: allow vertical vectors in vector field plots

Issue created by migration from https://trac.sagemath.org/ticket/5553

Original creator: kcrisman

Original creation time: 2009-03-17 20:59:17

Assignee: was

This is a followup to #4104, where the following discussion occurs about slope/vector field plots:

joyner: A question for possibly a future patch: it will not plot

```
plot_slope_field(x/y, (x,-3,3), (y,-3,3)).show(aspect_ratio=1)
```

because of the problem at y=0. However, should it? A slope of plus or minus infinity has a well-defined meaning. Should one try to trap singularities like that and just plot them as vertical direction fields in the future?

jason:  I'm aware of the problem, but decided to post the patch anyway when I saw that plot_vector_field had the same problem: the plot is blank when an evaluation is undefined.  I thought about trapping these things and plotting them as vertical lines, but really we ought to do something in plot_vector_field to take care of things when a vector has an infinite or NaN coordinate.  I ran out of time to fix plot_vector_field.


---

Comment by jason created at 2009-03-18 07:04:43

plot_vector_field is already fixed.  See #5259.


---

Comment by jason created at 2009-03-18 07:07:38

That said, it'd be great to fix plot_slope_field to detect when you have a vertical slope and have it change things accordingly.  I think this should be easy: just see what vectors have finite X, infinite Y, and set them to be zero X, one Y.


---

Comment by kcrisman created at 2009-03-18 14:23:48

I see, I thought that there was also a question of allowing infinite vectors, which I thought was weird.  I didn't realize it didn't return a plot at _all_ before!

Yes, so I will change the summary and description of this to fixing plot_slope_field.  The problem is that it will be a sort of messy hack, unless it's dealt with in the plot_vector_field code using a keyword (I attempted to start this), but then you are trying to catch something that looks like (1/inf,inf/inf=NaN), which is a little tricky.  But doing it in plot_slope_field means you might as well just do all the stuff in plot_vector_field there, since you'll have to catch individual vectors anyway - which is annoying, since it seems redundant.


---

Comment by jason created at 2010-03-17 05:28:41

Changing type from defect to enhancement.
