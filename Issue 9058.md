# Issue 9058: Compute cores to improve subgraph_search

Issue created by migration from https://trac.sagemath.org/ticket/9058

Original creator: ncohen

Original creation time: 2010-05-26 22:30:27

Assignee: jason, ncohen, rlm

CC:  mvngu

If one is looking for H in G, then we may assume the minimum degree of G is larger than the minimum degree of H. We can assume the same for the complement when computing an induced subgraph. Take care of directed graphs.

requires #8922

Nathann


---

Comment by ncohen created at 2010-06-06 11:01:10

Changing status from new to needs_work.


---

Comment by ncohen created at 2010-08-02 15:16:16

Changing status from needs_work to needs_review.


---

Comment by lsampaio created at 2010-10-06 12:48:59

Changing status from needs_review to positive_review.


---

Attachment

I verified the patch and I believe it is ok to be merged.


---

Comment by ncohen created at 2010-10-06 12:52:27

cool ! Thanks `;-)`

Nathann


---

Comment by mpatel created at 2010-10-08 21:39:19

Don't forget to update the author and reviewer fields.  lsampaio, could you add yourself to [the account name-real name map](http://trac.sagemath.org/sage_trac/wiki/WikiStart#AccountNamesmappedtoRealNames)?


---

Comment by lsampaio created at 2010-10-08 21:49:15

ok, I did it =)
thank you for pointing this!


---

Comment by mpatel created at 2010-10-08 22:31:35

Resolution: fixed
