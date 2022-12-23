# Issue 9091: check_file() in latex.py spits out warnings every time

Issue created by migration from https://trac.sagemath.org/ticket/9091

Original creator: rbeezer

Original creation time: 2010-05-30 02:22:52

Assignee: jason

CC:  nthiery jhpalmieri

In `sage/misc/latex.py` the `check_file()` routine has a mis-aligned block which will issue the `more_info` string whenever it is called, even if the file exists.


---

Attachment


---

Comment by rbeezer created at 2010-05-30 02:27:42

Changing status from new to needs_review.


---

Comment by nthiery created at 2010-06-01 09:27:12

Hi Robert,

Oops, how did that one get through without breaking the tests?

I am all for the change. Please add a test exhibiting the (now fixed)
problem to avoid later regression; then, if all test pass, you may set
a positive review on my behalf.


---

Comment by nthiery created at 2010-06-01 09:27:12

Changing status from needs_review to needs_work.


---

Comment by rbeezer created at 2010-06-01 17:43:04

Replying to [comment:2 nthiery]:
> Oops, how did that one get through without breaking the tests?

I think almost everywhere it gets exercised, it is marked "# random."  I did have it messing up on my doctests on the latex() routines, which is how I caught it.

> Please add a test exhibiting the (now fixed)
> problem to avoid later regression; then, if all test pass, you may set
> a positive review on my behalf.

I knew that was too easy - totally forgot to add a test against the bug.  ;-)  Will do in the next day or two.  Thanks for the review and the reminder.

Rob


---

Attachment


---

Comment by rbeezer created at 2010-06-01 21:37:17

Version 2 self-contained patch contains a test with a file that should be in every latex distribution, plus a `more_info` string.  So prior to this fix, the info string (and only the info string) would have printed if someone ran the optional tests and had latex installed.

As requested by the reviewer, I've marked this "positive review."

Release manager: just apply the v2 patch only.


---

Comment by rbeezer created at 2010-06-01 21:37:17

Changing status from needs_work to needs_review.


---

Comment by rbeezer created at 2010-06-01 21:37:33

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-06-06 07:27:01

Resolution: fixed
