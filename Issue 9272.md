# Issue 9272: make -only-optional=... case-insensitive

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2010-06-19 02:54:35

Assignee: mvngu

Some doctests in sage/homology/tests.py are marked `# optional - CHomP` (or they should be marked this way: see #9270 and #9271).  Running `sage -t -only-optional=chomp tests.py` runs those tests, but running `sage -t -only-optional=CHomP tests.py` does not.



---

Comment by jhpalmieri created at 2010-06-19 03:02:42

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2010-06-19 03:02:42

Here's a patch for the scripts repo.  During parsing, the line being doctested gets converted to lower-case (line 245 in sage-doctest), but the arguments for "-only-optional" were not being converted.  The patch fixes this.


---

Comment by jhpalmieri created at 2010-06-19 03:02:55

scripts repo


---

Comment by rlm created at 2010-06-20 22:55:27

Changing status from needs_review to positive_review.


---

Attachment

Looks good to me!


---

Comment by rlm created at 2010-06-25 15:43:15

Resolution: fixed
