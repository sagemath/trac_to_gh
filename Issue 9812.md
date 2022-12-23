# Issue 9812: parametric plot aspect ratio

Issue created by migration from https://trac.sagemath.org/ticket/9813

Original creator: jason

Original creation time: 2010-08-27 01:39:32

Assignee: jason, was

CC:  kcrisman rbeezer

I think parametric_plot should default to having an aspect ratio of 1.  Often we are plotting circles or other objects where we actually want to see the relationship between the two variables.

Besides, it seems like mma does this too.


---

Comment by jason created at 2010-08-27 01:39:49

Changing keywords from "" to "beginner".


---

Comment by jason created at 2010-08-27 01:55:57

Changing priority from major to minor.


---

Comment by jason created at 2010-08-27 01:55:57

Changing status from new to needs_review.


---

Comment by kcrisman created at 2010-08-27 02:38:13

Unfortunately I won't be reviewing much until I switch to wireless, or the semester proves easy... but I would point out that Minh has done some work trying to make sure we are unified in whether it's 2D or 2d or whatever.  I feel like his p.o.v. was 2D.  Look at things like `disk.py` or `circle.py`, where I believe this came into play when I upgraded the docs last year.


---

Comment by kcrisman created at 2010-08-27 02:40:38

Oh, and I should point out that I expect this patch will work as advertised!  Code and examples seem straightforward.  By the way, somewhere in the developer guide it should say that you need extra lines after plots for them to show up in the live doc - I didn't know that until quite recently, probably courtesy of you.


---

Attachment


---

Comment by ddrake created at 2010-09-06 04:23:07

tiny reviewer patch


---

Attachment

Looks good. I've added a little reviewer patch that adds in hyperlinks for the polar_plot docstring.


---

Comment by ddrake created at 2010-09-06 04:24:12

Changing status from needs_review to positive_review.


---

Comment by ddrake created at 2010-09-06 04:25:30

Release manager: apply attachment:trac-9813-parametric-aspect.patch and then attachment:trac_9813_reviewer.patch .


---

Comment by mpatel created at 2010-09-15 10:40:44

Resolution: fixed
