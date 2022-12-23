# Issue 7327: Make integrate accept a variable range as a tuple

Issue created by migration from https://trac.sagemath.org/ticket/7327

Original creator: jason

Original creation time: 2009-10-28 00:24:05

Assignee: burcin

CC:  kcrisman

It is inconsistent with plot and other functions that this just hangs:


```
integrate(sin(x), (x,0,1))
```


This patch takes care of this.



---

Attachment


---

Comment by kcrisman created at 2009-10-28 01:14:33

This is a duplicate of #6816.  The tests for one of these should be incorporated in the other - probably in this one, since it has some doc upgrades - and probably also the check for too many arguments in the tuple.


---

Comment by kcrisman created at 2009-10-28 01:14:33

Changing status from new to needs_work.


---

Comment by kcrisman created at 2009-11-05 17:43:31

Based on Sage 4.2


---

Attachment

Updated patch includes the issues mentioned in previous comment, is ready for review.  Positive review to the parts I didn't write.


---

Comment by kcrisman created at 2009-11-05 17:45:16

Changing status from needs_work to needs_review.


---

Comment by mhansen created at 2009-11-06 05:10:19

Looks good to me.


---

Comment by mhansen created at 2009-11-06 05:10:19

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-11-06 05:10:58

Resolution: fixed


---

Comment by kcrisman created at 2009-12-22 16:29:15

Just an update - it turns out the original integral reported in #6816 is not, in fact, convergent.  Fixing this doctest so something mathematically correct happens will be done in #7745, since Maxima 5.20.1 simply returns that integral now, as opposed to giving 0.
