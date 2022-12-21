# Issue 7320: search_src and friends are case-sensitive

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2009-10-27 05:15:26

Assignee: jhpalmieri

CC:  mvngu

The functions `search_src`, `search_def`, and `search_src` are case-sensitive and have been for a while.  The documentation says that they're not.  This patch changes the documentation to reflect this, and adds one doctest to verify it.


---

Attachment


---

Comment by jhpalmieri created at 2009-10-27 05:16:17

Changing status from new to needs_review.


---

Comment by kcrisman created at 2009-10-29 18:31:07

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2009-10-29 18:31:07

Just out of curiosity, is it possible to change the behavior?  Obviously that would be a different ticket.  That could be useful (or not).  Maybe a function that is, and another one that isn't...

The new patch is just making the notation for "case-sensitive" uniformly with hyphen, which seemed to be the majority of references in the doc; however, usage in general seems quite variable.  One word for the adjective seems right, though.  Maybe mvngu will have a comment, so I'm cc:ing him on this.

I also added a little to the doctests to make sure we're really doctesting the right thing and compare the two possibilities.


---

Comment by kcrisman created at 2009-10-29 18:31:54

Fixes a few things, adds doctest - use this


---

Attachment

Replying to [comment:2 kcrisman]:
> Just out of curiosity, is it possible to change the behavior?  Obviously that would be a different ticket.  That could be useful (or not).  Maybe a function that is, and another one that isn't...

I think so: I think we can add a flag to the regular expression search to make it case-insensitive.  We could add a flag (like `ignore_case=False`) to the search functions so people could toggle this.  Of course, I haven't actually tried this, but the documentation for regular expression searches in Python suggests that it should be possible...


---

Comment by mvngu created at 2009-10-30 04:47:06

Replying to [comment:2 kcrisman]:
> Maybe mvngu will have a comment, so I'm cc:ing him on this.

Sometimes I want to search the source with case-sensitivity on. For example, I might be interested in knowing if the source has anything with the word "Euler" in it. As function and method names are lower-case, case-sensitivity search might not return the name of a function/method like "euler_phi". However, if the documentation for "euler_phi" has something like "Euler phi function" or "Euler totient function", then case-sensitivity search would pick up "Euler". Sometimes I want to do a case-insensitivity search. In that case (pun not intended), I would expect that both "euler_phi" and "Euler" be returned by the search. At the end of the day, one can make case-insensitivity search as default, but should also give people the option to do case-sensitivity search. My 2-cent.


---

Comment by mhansen created at 2009-10-31 15:50:45

Resolution: fixed
