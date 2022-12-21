# Issue 2942: notebook -- new command line options: sage -n and sage -nb

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-04-16 11:34:55

Assignee: boothby

CC:  mpatel

After a vote, almost everybody (including me) agrees with the following:

sage -n:
   run the notebook -- equivalent to "sage -notebook"

sage -bn:
   build sage, then run the notebook -- equivalent to "sage -b; sage -n"


---

Attachment


---

Comment by TimothyClemans created at 2009-01-21 06:47:09

Changing type from defect to enhancement.


---

Comment by ncalexan created at 2009-01-21 19:15:59

This patch makes 'sage -b' run the notebook!  Not cool.


---

Comment by timdumol created at 2009-11-30 05:59:17

Added commands -n and -bn


---

Attachment

This patch should do the job.


---

Comment by timdumol created at 2009-11-30 06:00:19

Changing status from needs_work to needs_review.


---

Comment by was created at 2009-12-08 19:25:38

Changing status from needs_review to positive_review.


---

Comment by was created at 2009-12-08 19:25:38

Very, very nice.  It's especially nice how the build function is factored out.

I doubt people will ever use "sage -bn", since the notebook is no longer in the sage library.  However, it can't hurt to have it.  I think "sage -n" will be very useful. 

positive review.


---

Comment by was created at 2009-12-08 19:26:32

Note to release manager -- this gets applied to the Sage scripts repo, and has nothing to do with the sagenb spkg.  Hence I'm changing the component to "build".


---

Comment by was created at 2009-12-08 19:26:32

Changing component from notebook to build.


---

Comment by mhansen created at 2009-12-09 02:36:41

Resolution: fixed
