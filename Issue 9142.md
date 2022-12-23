# Issue 9142: construct "fuzzy ball" graphs

Issue created by migration from https://trac.sagemath.org/ticket/9142

Original creator: jason

Original creation time: 2010-06-04 21:18:55

Assignee: jason, ncohen, rlm

CC:  ncohen rlm

The Fuzzy Ball graphs are cospectral with respect to the normalized laplacian matrix.  This patch makes a function to construct such graphs.  I will be adding a reference in a separate patch once we publish our paper :).


---

Attachment


---

Comment by jason created at 2010-06-04 21:25:56

Changing status from new to needs_review.


---

Comment by ncohen created at 2010-06-04 21:55:31

Changing status from needs_review to positive_review.


---

Comment by ncohen created at 2010-06-04 21:55:31

Positive review to this patch, which will be nicer with a reference :-)

I add a small patch with minor corrections : some math formulas were written plain text, which reflects badly on the indices. "Anyone but me can review this patch", as Minh says !

Nathann


---

Comment by ncohen created at 2010-06-04 21:56:14

Changing status from positive_review to needs_work.


---

Comment by ncohen created at 2010-06-04 21:56:20

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2010-06-04 22:07:54

Please forget about my patch, as it makes no difference. I can not see why, though O_o


---

Comment by ncohen created at 2010-06-04 22:11:30

Only because dvipng was not installed on my machine. Please consider my patch anew, and my excuses for this mistake :-)

Nathann


---

Comment by ncohen created at 2010-06-04 22:14:55

I had forgotten to add the "r" in front of """. Updated !

Nathann


---

Attachment

apply on top of previous patches


---

Attachment

Positive review to your patch.  Can you look at my minor change in the explanation, to make it clear that you pass a list instead of a sum in for the partition?


---

Comment by ncohen created at 2010-06-04 22:20:02

Agreed :-)

Nathann


---

Comment by ncohen created at 2010-06-04 22:20:02

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-06-06 07:21:51

Resolution: fixed
