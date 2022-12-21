# Issue 9892: Make PARI *not* catch signals

Issue created by migration from Trac.

Original creator: jdemeyer

Original creation time: 2010-09-10 21:59:30

Assignee: tba

CC:  leif robertwb

In Sage, there is no reason for the PARI library to catch signals (by default, it catches SIGBUS, SIGFPE, SIGINT, SIGBREAK, SIGPIPE, SIGSEGV).


---

Comment by jdemeyer created at 2010-09-12 08:35:45

Changing component from c_lib to interfaces.


---

Comment by jdemeyer created at 2010-09-12 08:35:45

Changing assignee from tba to was.


---

Comment by jdemeyer created at 2010-09-12 09:37:18

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2010-09-26 17:26:03

This seems to influence #10018, so both #9893 and #10018 should probably be handled together.


---

Comment by jdemeyer created at 2010-09-26 17:26:03

Changing status from needs_review to needs_work.


---

Comment by jdemeyer created at 2010-09-27 09:00:19

Changing status from needs_work to needs_review.


---

Comment by davidloeffler created at 2010-09-29 07:26:21

Changing status from needs_review to positive_review.


---

Comment by davidloeffler created at 2010-09-29 07:26:21

Positive review of the proposal to close as duplicate.


---

Comment by mpatel created at 2010-10-03 09:37:51

Resolution: duplicate


---

Comment by mpatel created at 2010-10-03 09:37:51

I'm closing this now.  Feel free to reopen it, if #10018 ultimately does not subsume this.


---

Comment by jdemeyer created at 2010-10-17 08:39:22

Changing status from closed to needs_work.


---

Comment by jdemeyer created at 2010-10-17 08:39:22

Reopening this to collect the minimal changes required in PARI to make #9678 work.  This patch here will then become a prerequisite for #9678.


---

Comment by jdemeyer created at 2010-10-17 08:39:22

Changing priority from minor to major.


---

Comment by jdemeyer created at 2010-10-17 08:39:22

Changing keywords from "" to "pari signals".


---

Comment by jdemeyer created at 2010-10-19 20:46:32

Changing status from needs_work to needs_review.


---

Comment by jdemeyer created at 2010-10-19 20:46:32

All long doctests pass on a 32-bit PPC OS X 10.4 and on a 64-bit Intel Linux.  This patch was first included in #10018, then in #9678 and now I have separated it again in order to make #9678 not too much of a patch bomb.  The current version of the patch is pretty much the same as the old version of 5 weeks ago.  The patch makes sense by itself, but of course it is partially motivated by #9678.  Remark also that currently all tests in `sage/libs/pari` pass with #9678, #10061 and #10030 applied.


---

Comment by robertwb created at 2010-10-22 05:16:20

In general I'm a fan of using try...finally to handle sig_on/sig_off where there are many exits to a function, especially if exceptions are involved. (It can also alleviate the use of temporary variables to return something, but that's a matter of taste.)

Speed is important for new_gen_from_mpz_t, which is why we don't set up signals for "small" values. This behavior should be preserved.


---

Comment by robertwb created at 2010-10-22 05:16:20

Changing status from needs_review to needs_work.


---

Attachment


---

Comment by jdemeyer created at 2010-10-22 13:20:38

Changing status from needs_work to needs_review.


---

Comment by jdemeyer created at 2010-10-26 12:03:02

New patch still needs review....


---

Comment by robertwb created at 2010-11-05 03:51:17

Changing status from needs_review to positive_review.


---

Comment by robertwb created at 2010-11-05 03:51:17

Looks good to me, though I haven't had time to run all tests yet.


---

Comment by jdemeyer created at 2010-11-05 08:28:23

Replying to [comment:15 robertwb]:
> Looks good to me
Thanks!


---

Comment by jdemeyer created at 2010-11-10 22:20:30

Resolution changed from duplicate to fixed


---

Comment by jdemeyer created at 2010-11-12 13:24:49

Resolution changed from fixed to 


---

Comment by jdemeyer created at 2010-11-12 13:24:49

Changing status from closed to new.


---

Comment by jdemeyer created at 2010-11-12 13:24:56

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2010-11-12 13:25:03

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2010-11-13 10:51:30

I decided not to merge this in sage-4.6.1.alpha1 because I thought it might be the cause for #9163 (it turns out that's not the case).


---

Comment by jdemeyer created at 2010-11-15 23:26:38

Resolution: fixed
