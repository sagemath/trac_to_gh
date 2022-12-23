# Issue 8366: make contour plot labels and linestyles work when fill=True

Issue created by migration from https://trac.sagemath.org/ticket/8366

Original creator: jason

Original creation time: 2010-02-25 17:24:26

Assignee: was

CC:  kcrisman wcauchois robert.marik

We have an artificial limitation in that contour labels and linestyles don't work when fill=True.  This patch lets these options work with filling.  Furthermore, it draws the contour lines on top of filled plots by default, which (at least I think) makes the plot look a little nicer anyway.


---

Attachment


---

Comment by jason created at 2010-02-25 17:26:14

Changing status from new to needs_review.


---

Comment by robert.marik created at 2010-03-04 16:17:55

apply after previous patch, this patch fixes docstrings


---

Comment by robert.marik created at 2010-03-04 16:33:22

Changing status from needs_review to needs_work.


---

Attachment

Works as advertaised, but region_plot gives error after installing this patch.

```
sage: x,y=var('x y')
sage: region_plot(cos(x^2+y^2) <= 0, (x, -3, 3), (y, -3, 3))

Traceback (click to the left of this block for traceback)
...
KeyError: 'linewidths'
```


did you try this?

```
./sage -t devel/sage/sage/plot/contour_plot.py
```


My patch fixes long lines (which make help for contour_plot too wide for typical screen) and split contour_plot exmaples into groups (this allows to try commands immediatelly when reading live reference manual).

One suggestion: could we set label_colors to something resonable (gray? red? blue?) when both fill and labels are True, but label_color is not specified?


---

Comment by robert.marik created at 2010-03-04 16:44:45

Jason, thank you for this patch and thank you also for the patch to #8368. I hope that the issue above could be fixed easily. I suggest you to include the ticket #8368 to this one -- this could make the life of our release manager easier :)


---

Comment by jason created at 2010-03-04 18:34:24

Replying to [comment:3 robert.marik]:
> Jason, thank you for this patch and thank you also for the patch to #8368. I hope that the issue above could be fixed easily. I suggest you to include the ticket #8368 to this one -- this could make the life of our release manager easier :) 

I'm afraid I would get in trouble with our (wonderfully!) picky release manager for combining tickets which arguably have different issues.  (I really appreciate Minh's reminders about the details we need to follow!)


---

Attachment

apply on top of previous patches


---

Comment by jason created at 2010-04-15 03:28:16

Changing status from needs_work to needs_review.


---

Comment by jason created at 2010-04-15 03:28:16

Replying to [comment:2 robert.marik]:
> did you try this?
> {{{
> ./sage -t devel/sage/sage/plot/contour_plot.py
> }}}


Weird---I thought I did.  Well, the new patch fixes this error.

> One suggestion: could we set label_colors to something resonable (gray? red? blue?) when both fill and labels are True, but label_color is not specified?

The new patch addresses this issue as well.

Can you look at this and review it again?

Thanks


---

Comment by robert.marik created at 2010-04-15 09:49:21

Changing status from needs_review to positive_review.


---

Comment by robert.marik created at 2010-04-15 09:49:21

Thanks for fixing - the patch introduces new functionality, tests passed now. Positive review.

Release manager: apply all three patches:  trac-8366-label-filled-contours.patch, trac-8366-fixed-docstrings.patch, trac-8366-fix-code.patch


---

Comment by robert.marik created at 2010-04-15 09:49:21

Changing keywords from "" to "contour,plot".


---

Comment by jhpalmieri created at 2010-04-15 23:44:44

Resolution: fixed


---

Comment by jhpalmieri created at 2010-04-15 23:44:44

Merged into 4.4.alpha0:
 - trac-8366-label-filled-contours.patch
 - trac-8366-fixed-docstrings.patch
 - trac-8366-fix-code.patch
