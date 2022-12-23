# Issue 9685: constructor for the all ones matrix

Issue created by migration from https://trac.sagemath.org/ticket/9685

Original creator: rlm

Original creation time: 2010-08-04 13:30:38

Assignee: was

CC:  jdemeyer




---

Attachment


---

Comment by rlm created at 2010-08-04 13:34:58

Changing status from new to needs_review.


---

Comment by flawrence created at 2010-11-03 05:46:25

Worked for me and behaves consistently with similar functions such as zero_matrix().  The sparse matrix option is not too useful here (since the matrix gets filled with ones), but I guess it's best to be consistent with similar functions, which the patch is.


---

Comment by flawrence created at 2010-11-03 05:46:25

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2010-11-03 10:47:00

When applying this to sage-4.6.1.alpha0, I get

```
patching file sage/matrix/constructor.py
Hunk #1 succeeded at 1348 with fuzz 2 (offset 363 lines).
```

So the patch succeeds, but it's probably better if it gets rebased properly.


---

Comment by jdemeyer created at 2010-11-03 10:47:00

Changing status from positive_review to needs_work.


---

Comment by flawrence created at 2010-11-04 01:13:32

If I rebased it, would someone else then have to review it?


---

Comment by jdemeyer created at 2010-11-04 08:22:43

Replying to [comment:4 flawrence]:
> If I rebased it, would someone else then have to review it?

I could easily review your rebasing.


---

Comment by flawrence created at 2010-11-04 10:17:35

rebased version of original patch


---

Comment by flawrence created at 2010-11-04 10:17:55

Changing status from needs_work to needs_review.


---

Attachment


---

Comment by jdemeyer created at 2010-11-04 15:46:35

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2010-11-10 22:19:59

Resolution: fixed
