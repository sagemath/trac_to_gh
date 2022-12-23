# Issue 7476: Edge-disjoint spanning trees

Issue created by migration from https://trac.sagemath.org/ticket/7476

Original creator: ncohen

Original creation time: 2009-11-17 06:11:37

Assignee: rlm

CC:  jason

The theorem from Nash-Williams on the existence of k edge-disjoint spanning trees in a graph is both important, useful, and polynomial to compute. This could be implemented using the short proof described in the following article :

http://arxiv.org/abs/0911.2809

Or, if we achieve to eventually define in Sage a class Matroid, this could be done through the Matroid Union Theorem as presented in Schrijver's book.


---

Comment by ncohen created at 2010-02-23 10:11:06

Changing status from new to needs_review.


---

Comment by ncohen created at 2010-02-23 10:11:06

Finally, it was pretty quick to do it through LP :-)

Nathann


---

Comment by ncohen created at 2010-04-08 21:21:01

For an explanation of the Linear Program used to solve this problem, see the LP chapter from : http://code.google.com/p/graph-theory-algorithms-book/

Nathann


---

Comment by ncohen created at 2010-04-23 11:39:37

Patch rebased on top of #7608 !


---

Comment by rlm created at 2010-06-17 21:03:14

I'd much rather see the algorithm in the paper implemented, especially if it's polynomial time.


---

Comment by rlm created at 2010-06-17 21:03:14

Changing status from needs_review to needs_work.


---

Comment by ncohen created at 2010-06-18 11:24:00

What would you think of still putting this into Sage ? It would take much more time to write the other algorithm, and nothing says that LP would not be faster anyway...

Nathann


---

Comment by rlm created at 2010-06-18 14:58:09

If you indicate in the `ALGORITHM` section where the papers are regarding the poly-time algorithm, I'm fine with including this.


---

Comment by ncohen created at 2010-06-20 17:38:41

Updated !


---

Comment by ncohen created at 2010-06-20 17:38:41

Changing status from needs_work to needs_review.


---

Comment by rlm created at 2010-06-21 17:45:57

Revised version of Nathann's patch using the proper # optional syntax


---

Comment by rlm created at 2010-06-21 17:49:43

Changing status from needs_review to positive_review.


---

Attachment

Looks good to me.


---

Comment by rlm created at 2010-06-29 16:43:36

Resolution: fixed
