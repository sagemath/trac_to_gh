# Issue 6905: real(0.0r) is broken

Issue created by migration from Trac.

Original creator: nthiery

Original creation time: 2009-09-08 21:09:22

Keywords: real, symbolic, plot

Implement:

   sage: real(0.0r)

Note: imag(0.0r) seems to readily work (using Maxima if I read it well)!


Found after getting the following bug report from Francois Maltey:

	sage: parametric_plot ((real(exp(i*a)),imag(exp(i*a))),(a,-5,5))

Raises the following warning:

	verbose 0 (2999: plot.py, generate_plot_points) WARNING: When plotting, failed to evaluate function at 200 points.
	verbose 0 (2999: plot.py, generate_plot_points) Last error message: ''float' object is not callable'

and yield an empty plot. Investing this further, I got that

	sage: var('a'); f = fast_float(real(exp(i*a)),a)

Yields a non callable object. Finally Mike H traced it back on IRC to real(0.0r) being broken, because 0.0r.real is an attribute, not a
method.


---

Attachment


---

Comment by mhansen created at 2009-09-08 21:13:21

Changing status from new to assigned.


---

Comment by mhansen created at 2009-09-08 21:13:21

Set assignee to mhansen.


---

Comment by nthiery created at 2009-09-11 15:27:44

This trivial patch applies smoothly, passes all test in sage/functions (and most likely elsewhere).

I am no expert of this part of sage, and from the outside it sounds a bit like a workaround. In the long run, it would sound better to fix float to have a "real" method,
and have a consistent implementation of real and imag.
But it is simple enough to be safe,and it solves the original problem which hurts casual users. So I put a positive review.
If anyone cares, please create a new ticket.


---

Comment by mvngu created at 2009-09-11 17:30:58

Resolution: fixed
