# Issue 9364: add is_symmetric in BooleanFunction

Issue created by migration from Trac.

Original creator: ylchapuy

Original creation time: 2010-06-28 20:15:19

Assignee: mvngu

test if a given Boolean function is invariant under permutation of its inputs.


---

Comment by ylchapuy created at 2010-06-28 20:17:26

based on 4.5.alpha0


---

Comment by ylchapuy created at 2010-06-28 20:19:15

Changing status from new to needs_review.


---

Attachment

The patch is longer than necessary because it also strips some whitespaces at EOL.


---

Comment by malb created at 2010-06-29 10:22:01

Looks good, applies cleanly, doctests pass.


---

Comment by malb created at 2010-06-29 10:22:23

Changing status from needs_review to positive_review.


---

Attachment

Version without tabs - apply only this patch


---

Comment by davidloeffler created at 2010-06-30 17:23:44

The patch `trac9364-BooleanFunction_is_symmetric.patch` uses tabs for indentation, which is against sage coding conventions. I have uploaded a version with spaces instead of tabs.


---

Comment by mpatel created at 2010-07-20 10:07:21

Resolution: fixed
