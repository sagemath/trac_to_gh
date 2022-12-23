# Issue 5467: The sage/macaulay2 interface doesn't work at all on large input

Issue created by migration from https://trac.sagemath.org/ticket/5467

Original creator: was

Original creation time: 2009-03-10 18:03:16

Assignee: mhansen

ON OS X and Linux with Macaulay 1.2.


```
teragon:~ wstein$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: macaulay2(10^10000)
sage0
sage: macaulay2(10^10000)
sage1
sage: macaulay2(10^10000)
sage2
```



---

Comment by novoselt created at 2010-01-09 07:29:19

This is a trivial fix - the problem was in a wrong file loading command passed to Macaulay2.

The tests in the modified function pass (although optional tests for the whole file give a bunch of unrelated mistakes).


---

Comment by novoselt created at 2010-01-09 07:29:19

Changing status from new to needs_review.


---

Comment by novoselt created at 2010-01-09 20:41:25

Must be applied after the first patch.


---

Attachment

I managed to make a trivial mistake in this trivial fix - one of the test lines was not marked with #optional. Now it is.


---

Comment by novoselt created at 2010-01-31 23:02:17

Converged patches into a single one and made the commit message of standard form.


---

Comment by novoselt created at 2010-01-31 23:04:22

Only this patch should be applied.


---

Attachment


---

Comment by mhansen created at 2010-07-09 01:03:06

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-07-09 01:03:06

Looks good to me.


---

Comment by mpatel created at 2010-07-21 03:30:21

Resolution: fixed
