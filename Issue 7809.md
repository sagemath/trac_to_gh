# Issue 7809: region_plot does not respect the passed variable order

Issue created by migration from https://trac.sagemath.org/ticket/7809

Original creator: jason

Original creation time: 2010-01-01 18:44:22

Assignee: was

The call `region_plot(2/x + 1/y > 1/x * 1/y, (x,-10,10), (y,-10,10))` passes the following function to setup_for_eval_on_grid: `(y, x) |--> -2/x - 1/y + 1/(x*y)`, but passes the variables in the order (x,y).  The problem is the equify function.  This patch simplifies the code in equify to not try to put an ordering on the variables, but to just pass back an expression (not a function).

In practice, since variables would be substituted by name, I don't think this will make a difference.  But it does make the code cleaner and more correct.


---

Comment by jason created at 2010-01-01 18:55:44

Changing status from new to needs_review.


---

Attachment


---

Comment by kcrisman created at 2010-01-04 16:11:51

Looks like this is the only place equify is used, so I think this does not require any deprecation for the removed optional argument.  There should be another doctest in to show this works, though, like

```
sage: region_plot([y>.3, x>0, x^2+y^2<1], (x,-1.1, 1.1), (y,-1.1, 1.1), plot_points = 400).show(aspect_ratio=1)
sage: region_plot([y>.3, x>0, x^2+y^2<1], (y,-1.1, 1.1), (x,-1.1, 1.1), plot_points = 400).show(aspect_ratio=1)
```

Also, the example in the description fails!  Though, to be fair, it failed before as well - but I figure I should mention it in case it's related to this ticket after all.  Or was the syntax wrong?

```
sage: region_plot(2/x + 1/y > 1/x * 1/y, (x,-10,10), (y,-10,10))
TypeError: reduce() of empty sequence with no initial value
```



---

Comment by kcrisman created at 2010-01-04 16:11:51

Changing status from needs_review to needs_work.


---

Comment by jason created at 2010-01-04 16:15:46

Replying to [comment:2 kcrisman]:
> Looks like this is the only place equify is used, so I think this does not require any deprecation for the removed optional argument.  There should be another doctest in to show this works, though, like
> {{{
> sage: region_plot([y>.3, x>0, x<sup>2+y</sup>2<1], (x,-1.1, 1.1), (y,-1.1, 1.1), plot_points = 400).show(aspect_ratio=1)
> sage: region_plot([y>.3, x>0, x<sup>2+y</sup>2<1], (y,-1.1, 1.1), (x,-1.1, 1.1), plot_points = 400).show(aspect_ratio=1)
> }}}


Does this actually produce an incorrect plot before the patch?  I'll check, but I'm pretty sure it should work.


> Also, the example in the description fails!  Though, to be fair, it failed before as well - but I figure I should mention it in case it's related to this ticket after all.  Or was the syntax wrong?
> {{{
> sage: region_plot(2/x + 1/y > 1/x * 1/y, (x,-10,10), (y,-10,10))
> TypeError: reduce() of empty sequence with no initial value
> }}}

This is not related to this ticket.  The error is caused by a bug in fast_callable--see #7810.


---

Comment by kcrisman created at 2010-01-04 16:19:36

Replying to [comment:3 jason]:
> Replying to [comment:2 kcrisman]:
> > Looks like this is the only place equify is used, so I think this does not require any deprecation for the removed optional argument.  There should be another doctest in to show this works, though, like
> > {{{
> > sage: region_plot([y>.3, x>0, x<sup>2+y</sup>2<1], (x,-1.1, 1.1), (y,-1.1, 1.1), plot_points = 400).show(aspect_ratio=1)
> > sage: region_plot([y>.3, x>0, x<sup>2+y</sup>2<1], (y,-1.1, 1.1), (x,-1.1, 1.1), plot_points = 400).show(aspect_ratio=1)
> > }}}
> 
> 
> Does this actually produce an incorrect plot before the patch?  I'll check, but I'm pretty sure it should work.
> 

I didn't bother to check, but it seems like this was the concern, or?  At any rate there should be something documented that didn't work before and now does.  Otherwise I don't quite get why we are removing the potential for passing in the variables here.


---

Comment by jason created at 2010-01-04 16:24:13

Replying to [comment:2 kcrisman]:
> Looks like this is the only place equify is used, so I think this does not require any deprecation for the removed optional argument.  There should be another doctest in to show this works, though, like
> {{{
> sage: region_plot([y>.3, x>0, x<sup>2+y</sup>2<1], (x,-1.1, 1.1), (y,-1.1, 1.1), plot_points = 400).show(aspect_ratio=1)
> sage: region_plot([y>.3, x>0, x<sup>2+y</sup>2<1], (y,-1.1, 1.1), (x,-1.1, 1.1), plot_points = 400).show(aspect_ratio=1)
> }}}

Actually, the second example above produces the wrong image even after the patch is applied!


---

Comment by kcrisman created at 2010-01-04 16:30:33

Are you sure?  Are we always putting x on the horizontal axis?  This seems okay to me.


---

Comment by jason created at 2010-01-04 16:32:26

no, x shouldn't be on the horizontal axis always.  The first variable specified should be on the horizontal axis.  That would then be consistent.


---

Comment by kcrisman created at 2010-01-04 16:54:14

Right, and in the second plot the first variable is on the horizontal axis - see attached graphic.   By the way, note the one-pixel issue still - aargh!  I wonder what the heck is causing that.


---

Attachment

Oh, you're right.  It is correct.

Well, I just rewrote the mangle_neg part anyway.  I'll attach a patch in a second.


---

Comment by jason created at 2010-01-04 18:05:43

Before the simplify-negative-code:


```
sage: %time region_plot([y>.3, x>0, x^2+y^2<1], (y,-1.1, 1.1), (x,-.5, 1.1)).show(aspect_ratio=1)
CPU times: user 1.96 s, sys: 0.08 s, total: 2.04 s
Wall time: 2.38 s
sage: %time region_plot([y>.3, x>0, x^2+y^2<1], (y,-1.1, 1.1), (x,-.5, 1.1),plot_points=400).show(aspect_ratio=1)
CPU times: user 5.92 s, sys: 0.08 s, total: 5.99 s
Wall time: 6.30 s
```


After:


```
sage: %time region_plot([y>.3, x>0, x^2+y^2<1], (y,-1.1, 1.1), (x,-.5, 1.1)).show(aspect_ratio=1)
CPU times: user 1.27 s, sys: 0.02 s, total: 1.29 s
Wall time: 1.36 s
sage: %time region_plot([y>.3, x>0, x^2+y^2<1], (y,-1.1, 1.1), (x,-.5, 1.1),plot_points=400).show(aspect_ratio=1)
CPU times: user 2.49 s, sys: 0.04 s, total: 2.53 s
Wall time: 2.67 s
```



---

Comment by jason created at 2010-01-04 18:14:23

apply on top of previous patch


---

Attachment

Too bad about mangle_neg, but it was almost more confusing that way than in the code, I think you are right.  

Be sure to include some test where the order of coordinates is switched.  Incidentally, you should also remove the #long time flag from that one test; it only takes one second on my machine, which I don't think counts as a long time any more.  The file takes nearly a half minute to test for me, though!

Other than that, positive review.


---

Comment by jason created at 2010-01-04 19:11:38

Replying to [comment:11 kcrisman]:

> Be sure to include some test where the order of coordinates is switched. 

The old code gave the correct result too, I think.  I consider this patch more a refactoring of code.  The error that I corrected didn't show up because I think we were more careful in another part of the code.

Jason


---

Attachment

apply on top of previous patch


---

Comment by jason created at 2010-01-04 19:19:44

Okay, I made the changes you requested to the doctests and attached a patch.  Can you mark this as positively reviewed?


---

Comment by jason created at 2010-01-04 19:19:50

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2010-01-04 19:25:33

Looks good.  The use of s and t is good because then it's not so clear to the user from convention which one "should" be horizontal.  Positive review; apply in the order simplify-equify, simplify-negative-code, variable-order.


---

Comment by kcrisman created at 2010-01-04 19:25:33

Changing status from needs_review to positive_review.


---

Comment by jason created at 2010-01-09 05:35:55

This ticket also fixes #5885, so that should be closed when this is.

(the deprecation warning is now printed).


---

Comment by rlm created at 2010-01-13 11:24:24

Resolution: fixed
