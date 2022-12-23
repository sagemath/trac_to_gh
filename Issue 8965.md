# Issue 8965: decorate.py: clarify normalize_input, Parallel and parallel

Issue created by migration from https://trac.sagemath.org/ticket/8965

Original creator: jdc

Original creation time: 2010-05-14 18:01:22

Assignee: mvngu

CC:  was

Clarify documentation, add some doctests, and slightly simplify the implementation of Parallel.__call__.


---

Attachment

Found a typo in comment; apply both patches


---

Attachment

folded the previous two patches into one patch; based on Sage 4.4.2.rc0


---

Comment by mvngu created at 2010-05-15 02:41:31

The patch [trac_8965-decorate-folded.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8965/trac_8965-decorate-folded.patch) folds the other two patches into one. That way, it would be easier for reviewers to see what changes are proposed, instead of having to inspect two different patches.


---

Comment by mvngu created at 2010-05-15 02:41:31

Changing status from new to needs_review.


---

Comment by jdc created at 2010-05-15 13:28:32

Thanks for merging the patches.  I realized last night that my "simplificiation" of the __call__ method is incorrect.  I'll upload a better patch (with an additional doctest) later today.


---

Comment by jdc created at 2010-05-15 13:28:32

Changing status from needs_review to needs_work.


---

Comment by jdc created at 2010-05-16 00:24:21

single patch, ready for review


---

Attachment

The only patch needed now is trac_8965_decorate.patch.  (I couldn't figure out how to delete the others.)  It reverts to the original implementation of Parallel.__call__, since the simpler one didn't handle the case where the function being wrapped can be called with no arguments.  The latest patch includes doctests for this situation.

The latest patch only changes documentation or comments, besides one whitespace change to the code.


---

Comment by jdc created at 2010-05-16 00:29:13

Changing status from needs_work to needs_review.


---

Comment by cmullan created at 2010-07-21 15:00:10

Changing status from needs_review to needs_work.


---

Comment by cmullan created at 2010-07-21 15:00:10

EXAMPLES: should be EXAMPLES::
