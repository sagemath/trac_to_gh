# Issue 8877: New methods in partitions

Issue created by migration from Trac.

Original creator: aschilling

Original creation time: 2010-05-04 22:45:42

Assignee: sage-combinat

CC:  sage-combinat

We implement new methods in /combinat/partition.py which allow to go from k-bounded partitions to Grassmannian elements in the affine Weyl group of type A and the corresponding reduced word.


---

Comment by aschilling created at 2010-05-04 23:00:29

Changing status from new to needs_review.


---

Attachment


---

Comment by hivert created at 2010-05-05 04:04:40

The patch was needing to be untabified + there where some sphinx mistake in the references. I fixed those.


---

Comment by jbandlow created at 2010-05-05 13:16:57

Changing status from needs_review to positive_review.


---

Comment by jbandlow created at 2010-05-05 13:16:57

Doc now builds without errors and displays correctly.  The methods themselves look ok.  Positive review! Release manager, please merge only the second patch, trac_8877-k_bounded-as.2.patch .


---

Comment by mvngu created at 2010-05-08 21:44:49

Merged [trac_8877-k_bounded-as.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8877/trac_8877-k_bounded-as.2.patch).


---

Comment by mvngu created at 2010-05-08 21:44:49

Resolution: fixed
