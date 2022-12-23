# Issue 9491: contour plot does not handle transparency

Issue created by migration from https://trac.sagemath.org/ticket/9491

Original creator: jason

Original creation time: 2010-07-13 14:43:19

Assignee: jason, was

CC:  slelievre

This patch enables an 'opacity' argument to the contour plot function.

Doctesting needs to be done, and a few examples need to be written.


---

Comment by jason created at 2010-07-13 14:46:35

Changing status from new to needs_work.


---

Attachment

This patch was done in a rush, so there may be bugs in it.


---

Comment by jason created at 2010-08-12 05:38:06

Comments from David Sanders on sage-support:

Firstly, with this code it seems not to be possible to make a
region_plot *without* specifying opacity -- it looks like a default
argument is missing somewhere.


---

Comment by jason created at 2010-09-07 02:56:54

Replying to [comment:2 jason]:
> Comments from David Sanders on sage-support:
> 
> Firstly, with this code it seems not to be possible to make a
> region_plot *without* specifying opacity -- it looks like a default
> argument is missing somewhere.

I think that is correct.


---

Comment by slelievre created at 2018-03-16 15:35:22

Changing keywords from "" to "alpha, transparency, opacity, plot, contour_plot, graphics".
