# Issue 7147: Change settings for INCLUDE_MPFR_PATCH from "1"  or "0" to "yes" or "no"

Issue created by migration from https://trac.sagemath.org/ticket/7147

Original creator: drkirkby

Original creation time: 2009-10-07 18:06:42

Assignee: tbd

CC:  david.kirkby@onetel.ne

Due to a bug in Solaris, MPFR can fail tests on sun4v machines.

We have solved this (#6453) some months back.,I added some code to a shell script that could apply the patch or not depending on whether INCLUDE_MPFR_PATCH was set to 1 (apply patch) or 0 (do not apply). Given other variable in Sage use "yes" or "no", it would be sensible this was changed to be consistent. Clearly this is a very trivial patch, 


---

Comment by AlexGhitza created at 2009-10-19 04:09:56

Changing status from new to needs_review.


---

Comment by AlexGhitza created at 2009-10-19 04:11:02

Where's the patch?


---

Comment by AlexGhitza created at 2009-10-19 04:11:02

Changing status from needs_review to needs_info.


---

Comment by drkirkby created at 2009-12-03 04:51:02

I'm closing this as invalid, as the variable can take on 3 values - 0, 1 and 2, not a yes/no.


---

Comment by drkirkby created at 2009-12-03 04:51:02

Resolution: invalid
