# Issue 7559: replace all the deprecation warning using deprecated_function_alias whenever possible

Issue created by migration from https://trac.sagemath.org/ticket/7559

Original creator: hivert

Original creation time: 2009-11-30 12:23:50

Assignee: tbd

CC:  ncohen hivert

This was suggested by Nathann Cohen. This is a followup of #7515 where a short mantra for deprecated function aliases is set-up.

I'll not have the time to do this right now so any volunteer is welcome. 

Cheers

Florent 




---

Comment by vbraun created at 2012-06-14 14:14:59

Changing status from new to needs_review.


---

Comment by vbraun created at 2012-06-14 14:14:59

This ticket isn't really a precise task. I think with #13109 any non-optimal use of deprecation should just die out eventually.

I propose we close this ticket as invalid.


---

Comment by kcrisman created at 2012-06-14 14:45:30

Changing priority from major to minor.


---

Comment by kcrisman created at 2012-06-14 14:45:30

I don't know about this being imprecise.  It says to replace `deprecation` with `deprecation_function_alias` wherever possible.   It's true that they will be removed someday, so this isn't a very high priority ticket!  But given that many of them haven't been removed yet, if someone really wanted to, this would be an ok thing to do by someone wanting to learn how to develop for Sage.

I'm downgrading and turning this into an enhancement, since this is not really a bug at all.   Once older deprecations are removed one could also closed this ticket.


---

Comment by kcrisman created at 2012-06-14 14:45:30

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2012-06-14 14:45:30

Changing type from defect to enhancement.


---

Comment by vbraun created at 2012-06-14 14:50:33

Any volunteers for beautifying the deprecations so that they'll look really good when we delete them next year? No? Thought so!


---

Comment by kcrisman created at 2012-06-14 15:27:46

Changing priority from minor to trivial.


---

Comment by kcrisman created at 2012-06-14 15:27:46

> Any volunteers for beautifying the deprecations so that they'll look really good when we delete them next year? No? Thought so!
Obviously.  However, there haven't even been any volunteers for deleting some of the deprecations in question - some of which are nearly three years old!  Just because a ticket is fairly pointless doesn't mean it isn't valid, if you take my meaning :)  Downgrading to trivial.
