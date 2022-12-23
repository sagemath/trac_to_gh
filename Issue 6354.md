# Issue 6354: [with patch, needs review] Advertise and improve sage -fixdoctest

Issue created by migration from https://trac.sagemath.org/ticket/6354

Original creator: nthiery

Original creation time: 2009-06-18 05:51:15

Assignee: nthiery

CC:  sage-combinat mhansen rlm

Keywords: fix doctests

After this patch, sage -fixdoctest handles multiline doctests,
and use the line number info of sage -t to be more robust (handles
multiple doctests with the same expected output in the same file).

By the way, sage -advanced advertises sage -fixdoctest.


---

Attachment

Looks good to me.


---

Comment by rlm created at 2009-06-24 10:02:15

Resolution: fixed


---

Comment by nthiery created at 2009-11-17 20:25:07

Resolution changed from fixed to 


---

Comment by nthiery created at 2009-11-17 20:25:07

Replying to [comment:2 rlm]:

Err, I don't see it in sage-4.2.1; was it somehow lost?


---

Comment by nthiery created at 2009-11-17 20:25:07

Changing status from closed to new.


---

Comment by rlm created at 2009-11-17 23:08:16

Sorry, it must have gotten lost during merging....


---

Comment by nthiery created at 2009-11-17 23:32:42

Changing status from new to needs_review.


---

Comment by nthiery created at 2009-11-17 23:32:42

Replying to [comment:4 rlm]:
> Sorry, it must have gotten lost during merging....

No worry :-) I set it back to positive review so that it get merged in 4.3.


---

Comment by nthiery created at 2009-11-17 23:32:51

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-11-19 17:37:58

Resolution: fixed
