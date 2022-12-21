# Issue 8231: Place cursor in new input cell in notebook

Issue created by migration from Trac.

Original creator: schymans

Original creation time: 2010-02-10 15:27:31

Assignee: was

CC:  jhpalmieri was robert.marik

Since the upgrade to sage 4.3.2, when one creates a new input cell in the notebook, the cursor is not automatically placed in the new input cell. It is fair to assume that a user that creates a new input cell wants to type in it straight away, so time would be saved if the cursor was put there automatically, as was the case in previous versions of the notebook.


---

Comment by was created at 2010-02-13 00:24:33

In fact, there are a *bunch* of situations where suddenly no cell has focus.  I say that there should be *no possible way* to ever make it so that no cell has focus, except maybe something involving `@`interact.


---

Comment by mpatel created at 2010-02-14 01:39:44

Changing priority from major to blocker.


---

Comment by mpatel created at 2010-02-14 01:58:43

Revert and fix #4450.  sagenb repo.


---

Comment by mpatel created at 2010-02-14 02:01:48

Changing status from new to needs_review.


---

Attachment

The patch should restore the earlier behavior and fix the cursor-wraps-around-the-last-compute-cell problem.  If not, let me know.


---

Comment by jhpalmieri created at 2010-02-17 04:26:54

This works for me, but I don't know javascript, and this is also an important issue, so other people should take a good look, too.


---

Comment by was created at 2010-02-21 19:57:46

Changing status from needs_review to positive_review.


---

Comment by was created at 2010-02-21 19:57:46

Positive review.


---

Comment by mvngu created at 2010-02-22 03:59:38

Merged [sagenb-0.7.5.1.spkg](http://sage.math.washington.edu/home/wstein/patches/sagenb/sagenb-0.7.5.1.spkg) in standard spkg repository.


---

Comment by mvngu created at 2010-02-22 03:59:38

Resolution: fixed
