# Issue 8676: document breadth-first and depth-first search methods of C graph

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2010-04-12 06:51:44

Assignee: mvngu

As the subject says. Also make sure to cross-reference the DFS and BFS of C graph and generic graph implementations.


---

Comment by mvngu created at 2010-04-12 06:55:09

Changing status from new to needs_review.


---

Comment by ncohen created at 2010-04-12 08:03:13

Hello !!!

I'm halfway through the review of this patch, and I have two remarks :

 * It may be a mistale from my part, but even though I can see you added generic_graph to the .rst file, I do not see it in the reference manual even though I can see your updates to the c_graph documentation.

 * path #8513 already adds this line, so your patch may have to be rebased on this one. I do not know whether the other modifications of #8513 could create conflicts, by the way

Reviewing your patches remains my preferred way of learning how to use Sage/Sphinx ;-)

Nathann


---

Comment by ncohen created at 2010-04-12 08:03:13

Changing status from needs_review to needs_info.


---

Attachment

based on Sage 4.3.5; require #8513


---

Comment by mvngu created at 2010-04-13 01:02:06

Replying to [comment:2 ncohen]:
>  * It may be a mistale from my part, but even though I can see you added generic_graph to the .rst file, I do not see it in the reference manual even though I can see your updates to the c_graph documentation.

This usually happens. What I would do is this. Take the latest Sage version, e.g. the binary version of Sage 4.3.5, and delete the `output` directory:

```
rm -rf SAGE_ROOT/devel/sage-main/doc/output/
```

Then apply necessary patches. When all such patches apply without problems, rebuild the reference manual, or indeed the whole Sage documentation.





>  * path #8513 already adds this line, so your patch may have to be rebased on this one. I do not know whether the other modifications of #8513 could create conflicts, by the way

I have rebased my patch on top of those at #8513. So now apply patches in this order:

 1. #8513
 1. [trac_8676-document-cgraph.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8676/trac_8676-document-cgraph.patch)


---

Comment by mvngu created at 2010-04-13 01:02:06

Changing status from needs_info to needs_review.


---

Comment by ncohen created at 2010-04-14 11:53:16

Yet another of Minh's patches. 

No mistake that I could notice, the patches are nicely imported, no warning of any kind during the generation of the documentation, the touched files pass all tests, and I learned new ways to use Sphynx. Positive review, and thank you again for your work ! :-)

Nathann


---

Comment by ncohen created at 2010-04-14 11:53:16

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-16 18:46:39

Resolution: fixed


---

Comment by jhpalmieri created at 2010-04-16 18:46:39

Merged "trac_8676-document-cgraph.patch" in 4.4.alpha0.
