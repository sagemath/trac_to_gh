# Issue 7836: Clean up the CRT_* functions

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2010-01-03 21:37:37

Assignee: AlexGhitza

CC:  cremona rlm

From #7595:

Replying to [comment:10 cremona]:
> I have some problems with the CRT* functions though.
> 
>    1. CRT_list does not check that the two lists have the same length;  if the moduli list is shorter you get an IndexError, but it would be better to catch that and raise a more informative error.
> 
>    2. CRT_basis is rather silly.   It calls CRT_list n times with the same moduli, which must be wasteful.  It would be better to call plain CRT n times with suitable moduli (exercise for the reader).
> 
> Of course, I don't think that these issues should delay the current patch, but deserve a ticket of their own to make sure they are tided up.
}}}


---

Comment by cremona created at 2010-01-04 17:21:29

Applies to 4.3 + patches at #7595


---

Attachment

The attached patch is based on 4.3 + the patches at #7595.  I tested all files which use either CRT_list or CRT_basis.


---

Comment by cremona created at 2010-01-04 17:22:50

Changing status from new to needs_review.


---

Comment by cremona created at 2010-01-04 17:22:50

Changing priority from major to minor.


---

Comment by rlm created at 2010-01-04 18:37:54

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-01-04 18:37:54

I've tested in `sage/rings`, and the changes look good to me.


---

Comment by rlm created at 2010-01-13 05:22:34

Resolution: fixed
