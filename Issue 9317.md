# Issue 9317: prime_to_S_part, is_S_unit, is_S_integral

Issue created by migration from Trac.

Original creator: aly.deines

Original creation time: 2010-06-23 05:46:39

Assignee: davidloeffler

CC:  cremona rkirov

Keywords: S_part

This contains the functions prime_to_S_part, is_S_unit, is_S_integral for number field ideals.


---

Comment by robertwb created at 2010-06-23 05:56:08

Changing status from new to needs_review.


---

Attachment


---

Comment by mhansen created at 2010-06-23 06:39:36

Shouldn't these be like ` is_s_unit `  instead of the capital s?


---

Attachment

Apply after previous patch


---

Comment by cremona created at 2010-06-23 07:11:32

The code looks good and applies to 4.4.4.alpha1.  There were several glitches in the formatting of the docstrings, which I have fixed in the second patch (which needs to be applied after the first).

Note:  to test the syntax of the docstrings, do "sage -docbuild reference html" which should rebuild the reference manual pages for files which have been modified.  Look out for Warnings and Errors.  Also, look at the html output to see if it looks right!

Reply to mhansen:   The capital S is standard mathematical notation.  This also matches the functions sage.rings.rational.Rational.is_S_integral and sage.rings.rational.Rational.is_S_unit (which I wrote so this is not an independent test!)

Note:  this patch was written by some of the students at Sage Days 22, and the intention is that some other students in the same group will review it on Wednesday June 23 as part of their Sage training!


---

Comment by mhansen created at 2010-06-23 07:27:29

Replying to [comment:3 cremona]:
> Reply to mhansen:   The capital S is standard mathematical notation.  This also matches the functions sage.rings.rational.Rational.is_S_integral and sage.rings.rational.Rational.is_S_unit (which I wrote so this is not an independent test!)

On the other hand, we don't capitalize things like Eulerian in `is_eulerian`.  Whatever is decided, it should be consistent :-)


---

Attachment


---

Comment by aly.deines created at 2010-06-23 16:13:46

I found and fixed error in the doctest.


---

Comment by annahaensch created at 2010-06-24 23:09:06

We applied the patch, ran the doctests, and everything looks good to us!


---

Comment by annahaensch created at 2010-06-24 23:09:06

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-07-20 07:53:32

Resolution: fixed
