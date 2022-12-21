# Issue 9069: weak popov form

Issue created by migration from Trac.

Original creator: cjh

Original creation time: 2010-05-28 00:25:47

Assignee: jason, was

CC:  burcin mderickx minz

Implement weak Popov form for a matrix over a rational function field k(t)


---

Comment by cjh created at 2010-05-28 00:40:44

Changing status from new to needs_review.


---

Comment by cremona created at 2010-06-05 15:42:56

My student David Roberts implemented  this in Magma, following the Mulders & Storjohann paper, and used it in the implementation of a lattice-based method for point-finding on curves over function fields F_q(T).  So I am familiar with the algorithm.  But when I gave a talk about the method in Leiden in 2006, I found that Hendrik Lenstra had never heard of Weak Popov Form, though his brother Arjen Lenstra's thesis (which dates back to the original LLL paper, so they could factor multivariate polynomials) had something entirely equivalent under another name.  From what I remember, the upshot is that for most constant fields one might be better off using theory to bound degrees and then using linear algebra over the ground field.

The patch applies fine to 4.4.3 and long tests in the two files touched pass.

   1. line 4545: typo, C should be N?  Same i nthe other file & docstring.
   2. In lines 99-105, why not just use an identity matrix?
   3. There is a slight inconsistency in the output for input a zero matrix, since it only has two components.  For consistency, also output the third thing, even if it is just a tuple of -Infinity's.

Otherwise it looks ok to me, given that the tests work, but I have not had time to go through the important part of the code in great detail and have no more time right now.


---

Comment by cremona created at 2010-06-05 15:42:56

Changing status from needs_review to needs_work.


---

Attachment


---

Comment by cjh created at 2010-06-07 10:17:38

Changing status from needs_work to needs_review.


---

Comment by cjh created at 2010-06-07 10:17:38

Latest version of the patch incorporates minor changes made in response to Cremona's comments.  Specifically, responses to his respective comments are:

1. Yes, C should be N.  Both docstrings corrected.
2. We now construct N using an identity matrix.  Note, the rest of the code expects N to be a list of tuples, hence N isn't an actual matrix.
3. The output for a zero matrix is now consistent with the documentation.


---

Comment by cremona created at 2010-06-23 16:22:14

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2010-06-23 16:22:14

Fine!  Patch applies fine to 4.4.4.alpha1.


---

Comment by mpatel created at 2010-07-20 08:20:29

Resolution: fixed


---

Comment by chapoton created at 2017-07-19 08:43:26

unique name please
