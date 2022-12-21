# Issue 9084: Move sage/gsl into libs directory.

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2010-05-29 08:46:10

Assignee: jason, jkantor




---

Comment by robertwb created at 2010-05-29 17:43:01

Bundle of file renaming.


---

Attachment

apply on top of previous


---

Comment by robertwb created at 2010-05-29 17:45:42

Should be an easy review, this just moved stuff around. I took the opportunity to change them from .pxi files to .pxd files, which they really should have been originally, so now they're cimported rather than included. 

Apply bundle with "hg pull /path/to/9084-move-gsl.hg". I've created a bundle to preserve the history across the file moves.


---

Comment by robertwb created at 2010-05-29 17:45:42

Changing status from new to needs_review.


---

Comment by klee created at 2011-04-01 07:49:36

Changing status from needs_review to needs_work.


---

Comment by klee created at 2011-04-01 07:49:36

This is unfortunate, but the patch does not apply cleanly for Sage 4.6.2. We missed the right time to review the patch...


---

Comment by klee created at 2016-11-10 20:02:41

Changing component from numerical to relocation.


---

Comment by klee created at 2016-11-10 20:02:41

Changing priority from major to minor.


---

Comment by git created at 2016-11-10 20:06:00

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by jdemeyer created at 2016-11-10 20:28:55

I disagree with the premise of this ticket.

I believe that `src/sage/libs` is a place purely for the library interface and nothing more. Making classes and implementing functionality using that library belongs somewhere else.

To use an example: a Sage `Integer` wraps a GMP/MPIR `mpz_t`. The GMP/MPIR library interface belongs in `src/sage/libs/gmp`, but the `Integer` class does not (because it does a lot more than strictly wrapping the GMP/MPIR library).


---

Comment by klee created at 2016-11-11 02:39:25

Replying to [comment:10 jdemeyer]:
> I disagree with the premise of this ticket.
> 
> I believe that `src/sage/libs` is a place purely for the library interface and nothing more. Making classes and implementing functionality using that library belongs somewhere else.
> 
> To use an example: a Sage `Integer` wraps a GMP/MPIR `mpz_t`. The GMP/MPIR library interface belongs in `src/sage/libs/gmp`, but the `Integer` class does not (because it does a lot more than strictly wrapping the GMP/MPIR library).

I understand that. But on the other hand, don't you agree that `gsl` is too specific to be placed just under `src/sage`, where all other subfolders  correspond to rather big (mathematical) themes?

And it seems to me that  there are already files under `src/sage/libs/xxx` that contain classes implementing functionality using the libraries. For example, look into `eclib`. No?

I think that `src/libs/gsl` is not an ideal place but less bad than just under `src/sage`. Could you suggest a better palce?


---

Comment by jdemeyer created at 2016-11-11 08:55:32

Replying to [comment:11 klee]:
> Could you suggest a better palce?

How about in `src/sage/calculus`?


---

Comment by git created at 2016-11-11 17:44:54

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2016-11-12 06:59:06

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by klee created at 2016-11-12 12:04:46

Changing status from needs_work to needs_review.


---

Comment by klee created at 2016-11-12 12:18:02

I owe a lot from Robert's old code.


---

Comment by klee created at 2016-11-14 08:51:07

I have nothing to do for the patchbot plugin failures.


---

Comment by git created at 2016-11-21 00:05:32

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2016-11-21 00:19:49

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2016-12-18 12:00:02

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2016-12-21 02:50:38

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by jdemeyer created at 2016-12-27 09:16:30

Changing status from needs_review to positive_review.


---

Comment by klee created at 2016-12-27 09:43:26

Thank you!


---

Comment by vbraun created at 2017-01-23 22:52:27

Resolution: fixed
