# Issue 7760: sage -merge fails silently when applying patches with rejects

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2009-12-24 11:03:04

Assignee: GeorgSWeber

CC:  craigcitro

We need to make sure the hg qpush command is failing with the proper exit code and handle it appropriately.


---

Comment by mhansen created at 2010-01-16 17:46:05

Changing status from new to needs_review.


---

Attachment


---

Comment by craigcitro created at 2010-01-17 23:03:46

This is clearly the right fix for the problem Mike ran into, and I'm giving it a positive review. 

I'm happy to see this merged, but it brings up a question: why aren't we checking the exit code from mercurial? A quick check of the code reveals the issue: we use `os.popen3` inside the hg interface, which we can't easily use to get the return code. (Or, at least, I don't know how to do it.) Maybe we should file an enhancement ticket to rewrite those lines to use `subprocess.Popen`, and correctly give back the return code?


---

Comment by craigcitro created at 2010-01-17 23:03:46

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-01-17 23:18:05

Yep, I think that sounds good.  I don't know how to get it from os.popen3.


---

Comment by rlm created at 2010-01-19 00:42:51

Resolution: fixed
