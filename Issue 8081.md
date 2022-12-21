# Issue 8081: documentation bug on new gale_ryser_theorem()

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2010-01-26 18:01:53

Assignee: mvngu

CC:  ncohen wdj

In the module `sage/combinat/integer_vector.py`, the documentation for the function `gale_ryser_theorem()` should be fixed as per the following suggestion:

```
On the recently added
gale_ryser_theorem()
there's a documentation bug (also present on the changelog)

"The Gale Ryser theorem asserts that if p1;p2  are two partitions of
n  of respective lengths k1;k2 , then there is a binary k1Âk2  matrix
M  such that p1  is the vector of row sums and p2  is the vector of
column sums of M , if and only if p2  dominates p1 ."

At the end it should say

"p2  conjugate (transpose) dominates p1"

The theorem is mis-stated yet the function seems to be working
```

See this [sage-devel thread](http://groups.google.com/group/sage-devel/browse_thread/thread/5014758cac3b9e5d) for the original bug report.


---

Comment by ncohen created at 2010-01-28 11:48:45

Changing status from new to needs_review.


---

Comment by ncohen created at 2010-01-28 11:48:45

Here it is !!!


---

Comment by wdj created at 2010-01-28 14:15:02

Changing status from needs_review to positive_review.


---

Attachment

Applies fine to 4.3.2.a0 and passes all but the 2 tests that failed previously on a mac 10.6.2.

Good docstring patch. Thanks Nathann!

Positive review.


---

Comment by mvngu created at 2010-01-29 22:51:18

Nathann, the ticket number is very useful for tracking down changes. You might consider putting it in your commit message. See [this section](http://www.sagemath.org/doc/developer/producing_patches.html#quick-mercurial-tutorial-for-sage) of the Developers' Guide.


---

Comment by mvngu created at 2010-01-31 00:14:19

Resolution: fixed
