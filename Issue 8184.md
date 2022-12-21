# Issue 8184: eclib upgrade and bugfix

Issue created by migration from Trac.

Original creator: cremona

Original creation time: 2010-02-04 14:27:17

Assignee: cremona

Keywords: eclib

We provide an upgrade to eclib to patch-level 9, i.e. eclib-20080310.p9.spkg.  This does two things:

    1. Fixes a bug (found by Edray Goins and Jamie Wiegandt) in which second descent quartics were not tested for real-solubility, and so sometimes the rank bounds (and related selmer ranks) could be too high.

    2. Enhances the data available from the two_descent class so that the rank_bound and selmer_rank are separated, and both available.

The second item necessitated changes to the interface, which are here included in the patch.  In turn, some changes were needed in sage/schemes/elliptic_curve/

Note that this affects #7575.


---

Attachment


---

Comment by cremona created at 2010-02-04 14:31:39

Changing status from new to needs_review.


---

Comment by wuthrich created at 2010-02-04 15:43:59

I fear you uploaded the wrong patch.

I am not certain how to review packages and I will read up on it; but someone might be faster at it.

Chris.


---

Comment by cremona created at 2010-02-04 15:56:51

Applies to 4.3.2.alpha1


---

Attachment

Sorry -- try this one.

NB After building the new spkg with "sage -f" the patch is required before Sage will work properly.  Even in a clone, you'll be stuck with the new spkg.  I am not sure how to revert back to the old eclib (if you want to).

So I would recommend tetsing this on (say) 4.3.2.alpha1 if you have it, and if all goes wrong you can build 4.3.2.rc0 which is out!


---

Comment by rlm created at 2010-02-04 19:08:21

Apply on top of trac_8184-eclib.patch


---

Attachment

I added a patch which replaces tabs with single spaces (it looks like your editor sees tabs as eight spaces... mine only sees them as four).


---

Comment by rlm created at 2010-02-04 20:04:47

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-02-04 20:04:47

I've tested this on 32-bit OS X and 64-bit Linux, and there are no problems. Looks great!


---

Comment by wuthrich created at 2010-02-05 10:07:20

I knew someone would be faster. Thanks.


---

Comment by mpatel created at 2010-02-10 11:24:19

The indentation patch seems to be missing the committer's name and email address, and the commit string does not contain the ticket number.  I've refreshed the patch and applied it to 4.3.3.alpha0.


---

Comment by mpatel created at 2010-02-11 14:30:31

Resolution: fixed
