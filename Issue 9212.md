# Issue 9212: top-level identity_matrix and zero_matrix functions should return mutable matrices

Issue created by migration from https://trac.sagemath.org/ticket/9212

Original creator: jason

Original creation time: 2010-06-11 07:15:15

Assignee: jason, was

CC:  rbeezer florent

After #8276, the top-level identity_matrix and zero_matrix functions return immutable matrices, which is a backwards-incompatible change that is inconvenient in many cases (when code starts with those matrices as the base and then modifies them).

This patch makes these matrices mutable.


---

Comment by jason created at 2010-06-11 07:17:30

Changing status from new to needs_review.


---

Attachment


---

Comment by was created at 2010-06-11 07:44:18

I'm closing this as won't fix, on account of #8276.


---

Comment by was created at 2010-06-11 07:44:18

Resolution: wontfix


---

Comment by jason created at 2010-06-11 08:34:09

The discussion there didn't discuss the top-level identity_matrix or zero_matrix functions.  In fact, they made a big change to those functions without deprecations.  The attached patch does *not* revert the changes in #8276.  It just restricts the changes to exactly what was discussed (i.e., this patch takes care of what I see as an unintended ramification of the changes in #8276).

I won't reopen this, as that's pushing things.  But I think you're cutting off the discussion way too soon.


---

Comment by jason created at 2010-06-11 08:37:39

Replying to [comment:4 jason]:

> I won't reopen this, as that's pushing things.  But I think you're cutting off the discussion way too soon.

(I mean, I won't personally reopen this right now, but I really wish you would revert your decision to shut it down so abruptly, especially considering that this ticket does *not* revert the changes in #8276, and in fact makes #8276 not break the deprecation policy).


---

Comment by jason created at 2010-06-11 09:11:54

Yet another reason for making identity_matrix and zero_matrix behave as they always have behaved and return mutable matrices: every top-level constructor from matrix/constructor.py (e.g., matrix(...), random_matrix(...), block_matrix(...), etc.) used to return a mutable matrix, so they were consistent with each other.  But now, #8276 made the top-level identity_matrix and zero_matrix constructors behave unlike the others (again, without deprecation and without discussion of the top-level function behavior).


---

Comment by jason created at 2010-06-13 04:48:47

I posted a call for a vote to sage-devel:

http://groups.google.com/group/sage-devel/browse_thread/thread/b3743044a4579376

because clearly if the confusion above stemmed from a discussion on sage-devel, the appropriate place to resolve things is on sage-devel.


---

Comment by rbeezer created at 2010-06-14 05:45:18

Hey Jason,

Following test in sage/misc/sagedoc.py (line 1089) is now broken.


```
sage: browse_sage_doc(identity_matrix, 'rst')[-60:-5]
```


You did run full tests before posting this, didn't you?  ;-)  More commentary in the morning.

Rob


---

Comment by rbeezer created at 2010-06-14 15:58:23

I have a review of this ready to go, and the only change needed is to fix the doctest doctest failure noted above.  Once you are satisfied with the vote on sage-devel, note the result here and I'll proceed accordingly.

Rob


---

Comment by jason created at 2010-06-14 16:11:48

Resolution changed from wontfix to 


---

Comment by jason created at 2010-06-14 16:11:48

I'm satisfied with the vote enough to reopen this ticket.


---

Comment by jason created at 2010-06-14 16:11:48

Changing status from closed to new.


---

Comment by jason created at 2010-06-14 16:13:42

Changing status from new to needs_review.


---

Comment by jason created at 2010-06-14 16:13:42

Replying to [comment:8 rbeezer]:
> Hey Jason,
> 
> Following test in sage/misc/sagedoc.py (line 1089) is now broken.
> 
> {{{
> sage: browse_sage_doc(identity_matrix, 'rst')[-60:-5]
> }}}
> 
> You did run full tests before posting this, didn't you?  ;-)  

No, I didn't run full doctests before posting the patch, so thanks for catching this!  I believe I tested the matrix directory, though.

When you say you have a review ready to go, do you mean that you have a reviewer patch to fix the doctest error, or should I do that?


---

Comment by rbeezer created at 2010-06-14 16:39:58

I have a "positive review" report, but no reviewer patch to make it happen.  So make/update a patch, and I'll issue a review.


---

Attachment

apply on top of previous patches


---

Comment by jason created at 2010-06-14 20:35:43

Okay, doctest is fixed.


---

Comment by rbeezer created at 2010-06-14 20:57:12

This all looks good, passes tests on 4.4.4.alpha0 and HTML documentation looks fine coming from matrix/constructor.py

Positive review.


---

Comment by rbeezer created at 2010-06-14 20:57:12

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-07-20 08:20:50

Resolution: fixed
