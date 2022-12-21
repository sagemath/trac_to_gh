# Issue 7754: Weyl group optimizations

Issue created by migration from Trac.

Original creator: nthiery

Original creation time: 2009-12-23 23:13:29

Assignee: nthiery

CC:  bump

Keywords: Weyl groups

- faster hash method calling the hash of the underlying matrix
   (which is set as immutable for that purpose)
 - new __eq__ method
 - action on the weight lattice realization:
   optimization of the matrix multiplication


---

Comment by nthiery created at 2009-12-23 23:15:15

Changing status from new to needs_review.


---

Attachment


---

Comment by bump created at 2010-01-01 21:32:30

Changing status from needs_review to positive_review.


---

Comment by bump created at 2010-01-01 21:32:30

I tested this patch without #7753. I tested it with and without the
patch in #7751.

It is a very substantial speedup. It cuts a few 
seconds off `sage -t weyl_groups.py` but more importantly it about doubles the speed of computing the reduced word of a Weyl group element, which is the basis of most combinatorial algorithms.

There are three patch fragments, one replacing the hash method with the hash of the underlying matrix, one replacing the `__eq__` method, and
one unraveling some unnecessary complexity in the Weyl group action. I tested each patch fragment separately and found that they are all speedups, the last one being very significant.


---

Comment by nthiery created at 2010-01-03 15:39:38

Thanks Dan for the review!


---

Comment by mhansen created at 2010-01-03 21:45:14

Resolution: fixed


---

Comment by mvngu created at 2010-01-12 03:41:17

Replying to [comment:2 bump]:
> It is a very substantial speed-up. It cuts a few 
> seconds off `sage -t weyl_groups.py` but more importantly it about doubles the speed of computing the reduced word of a Weyl group element, which is the basis of most combinatorial algorithms.

Hi Dan and Nicolas,



I'm doing a release tour of the features of this ticket, see the [Sage wiki](http://wiki.sagemath.org/ReleaseTours/sage-4.3.1) page. Is there some sample code I could use to show the speed-up implemented by this ticket?


---

Comment by nthiery created at 2010-01-12 10:05:11

> Hi Dan and Nicolas,
> 


> I'm doing a release tour of the features of this ticket, see the [Sage wiki](http://wiki.sagemath.org/ReleaseTours/sage-4.3.1) page. Is there some sample code I could use to show the speed-up implemented by this ticket?

Yup, see the updated description!
