# Issue 9801: Add random diagonalizable matrix to matrix/constructor.py

Issue created by migration from Trac.

Original creator: bwonderly

Original creation time: 2010-08-25 18:45:05

Assignee: jason, was

CC:  rbeezer wdj

This depends on #9720, so first apply the v3 patch from there.  This method generates random diagonalizable matrices whose eigenvectors, if computed by hand, have only integer values. This routine is designed as educational tool, generating exam and homework problems, and problem generating interacts.


---

Attachment


---

Comment by bwonderly created at 2010-08-25 18:47:30

Changing status from new to needs_review.


---

Attachment

revised to fit generalization of random_matrix constructor. Apply v4 from #9720 and v2 from #9803 and go from there. This patch is independent from #9754, but will be rebased as soon as either one gets a positive review


---

Comment by bwonderly created at 2010-08-28 17:39:15

The v2 patch is independent of #9754. There are revisions to the documentation of the random_diagonalizable_matrix routine, as well as to the random_matrix routine.  The code is revised to fit with the generalization of the random_matrix constructor.  First apply v4 from #9720, and then v2 from #9803 and go from there.


---

Comment by wdj created at 2010-08-28 21:58:26

This (with the other patches, as indicated above) applied fine to 4.5.1 and passed sage -testall.

Positive review, as far as I am concerned (and will be useful for me teaching linear algebra later in the semester!). Perhaps Mike Hansen should have the final say?

Thanks Rob and bwonderly!


---

Comment by rbeezer created at 2010-09-02 02:20:15

Changing status from needs_review to positive_review.


---

Comment by rbeezer created at 2010-09-02 02:20:15

Mike Hansen looked in on #9803, so I've marked this as ready to go based on comments above.  Thanks, David.


---

Comment by bwonderly created at 2010-09-03 06:28:42

## Release Manager

#9720, #9803, #9802, #9754 is each dependent on the predecessor, merge in this
order.


---

Comment by mpatel created at 2010-09-15 09:53:42

Resolution: fixed
