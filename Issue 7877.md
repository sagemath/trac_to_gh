# Issue 7877: matrix indexing should be explained in the manual

Issue created by migration from https://trac.sagemath.org/ticket/7877

Original creator: jason

Original creation time: 2010-01-09 17:51:19

Assignee: mvngu

CC:  rbeezer mvngu

A lot of the great stuff in the docstrings for the matrix __getitem__ and __setitem__ functions should be in the reference manual somewhere, maybe http://sagemath.org/doc/reference/sage/matrix/docs.html.


---

Comment by jason created at 2010-01-20 07:05:49

Changing status from new to needs_review.


---

Attachment


---

Comment by robertwb created at 2010-01-20 09:43:05

Depends on #8008, but otherwise, excellent!


---

Comment by robertwb created at 2010-01-20 09:43:05

Changing status from needs_review to positive_review.


---

Attachment

apply on top of previous


---

Comment by mvngu created at 2010-01-20 09:52:39

Changing status from positive_review to needs_work.


---

Comment by mvngu created at 2010-01-20 09:53:22

Changing status from needs_work to needs_review.


---

Comment by mvngu created at 2010-01-20 09:53:22

Here's a typo in the patch:

```
96	Get the second column of M:: 
97	         
98	    sage: M[1:,0] 
99	    [ 1] 
100	    [ 1] 
101	    [-1]
```

The code should be:

```
sage: M[:,1]
[-2]
[ 8]
[ 1]
[ 2]
```

I have attached patch for this, which needs some review. Otherwise the whole ticket looks good.


---

Attachment


---

Comment by jason created at 2010-01-20 10:12:40

Changing status from needs_review to positive_review.


---

Comment by jason created at 2010-01-20 10:12:40

positive review for Minh's patch; I attached the same patch for the __getitem__ docstring in matrix0.pyx.


---

Comment by jason created at 2010-01-20 10:13:08

(apply trac-7877-doc-error.patch on top of all previous patches)


---

Comment by mvngu created at 2010-03-02 21:59:54

Resolution: fixed


---

Comment by mvngu created at 2010-03-02 21:59:54

Merged in this order:

 1. [trac-7877-doc-matrix-indexing.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7877/trac-7877-doc-matrix-indexing.patch)
 1. [trac_7877-reviewer.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7877/trac_7877-reviewer.patch)
 1. [trac-7877-doc-error.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7877/trac-7877-doc-error.patch)

Jason: You should put a sensible commit message in your patch, together with the ticket number.
