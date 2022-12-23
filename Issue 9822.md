# Issue 9822: desolve_system is broken for a system of one equation

Issue created by migration from https://trac.sagemath.org/ticket/9823

Original creator: rhinton

Original creation time: 2010-08-27 16:40:56

Assignee: burcin

CC:  robert.marik

Keywords: calculus, maxima, symbolics

desolve_system fails for a system with only one equation:


```
sage: t = var('t')
sage: x = function('x', t)
sage: de1 = diff(x,t) + 1 == 0
sage: desolve_system([de1], [x]) 
```



---

Comment by robert.marik created at 2010-08-29 20:14:32

Changing status from new to needs_review.


---

Comment by robert.marik created at 2010-08-29 20:14:32

The patch solves the problem by passing to desolve_laplace. Both desoove_laplace and desolve_system use function desolve from Maxima and perhaps bouth could be merged into one function. Perhaps when solving #9824 ?

Also removes unnecessary spawned Maxima processes.

Install after the patch for #9835.


---

Comment by robert.marik created at 2010-08-30 06:27:21

Depends on Ticket #9835


---

Attachment

Updated the patch - removed plotting picture from testing, since Sage complains 

```
verbose 0 (3495: plot.py, generate_plot_points) WARNING: When plotting, failed to evaluate function at 200 points.
```

on one of my computers (Debian, AMD 64 bit).


---

Comment by wdj created at 2010-08-30 16:03:43

Does this really depend on 9835? It seemed to apply and test fine for me without it.


---

Comment by robert.marik created at 2010-08-30 16:52:45

You are right, thanks. Both patches touch different part of the same file and I expected numbers from the patch utility. But both patches are independent and #9835 can be installed on the top of this patch. Thanks for mentioning this.


---

Comment by wdj created at 2010-08-30 17:11:39

I have tested this without 9835 and it passes fine. Also, the patch is very simple and does as it says and also adds a doctest illustrating the new fix.

Positive review from me, without 9835. I am currently also testing it with 9835.


---

Comment by wdj created at 2010-08-30 19:23:00

All tests passes even with 9835.

Positive review from me but maybe rhinton should look at it?


---

Comment by rhinton created at 2010-08-31 03:02:58

Changing status from needs_review to positive_review.


---

Comment by rhinton created at 2010-08-31 03:02:58

Looks great to me!


---

Comment by mpatel created at 2010-09-29 08:38:49

Resolution: fixed
