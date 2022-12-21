# Issue 5901: [with patch, needs review] Avoid permission denied error message when testing with non-writeable sage install

Issue created by migration from Trac.

Original creator: tabbott

Original creation time: 2009-04-26 05:47:24

Assignee: tabbott

This is a patch to fix the fact that running sage tests prints a permission denied error writing to test.log when you don't have write access to the Sage installation.



---

Attachment

I don't think this is applicable anymore. As far as I know, the testing is done in the user's home folder. Making $SAGE_ROOT unwritable didn't give me any permission errors either.


---

Comment by timdumol created at 2010-06-23 11:11:57

My bad, I thought this was for sage-test. Looks good to me.


---

Comment by timdumol created at 2010-06-23 11:11:57

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-06-25 15:42:30

Resolution: fixed
