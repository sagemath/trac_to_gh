# Issue 8487: Use use_grobner in to_poly_solve

Issue created by migration from https://trac.sagemath.org/ticket/8487

Original creator: robert.marik

Original creation time: 2010-03-10 10:05:03

Assignee: burcin

Sage returns no solution 

```
x,y=var('x y')
c1(x,y)=(x-5)^2+y^2-16; c2(x,y)=(y-3)^2+x^2-9
solve([c1(x,y),c2(x,y)],[x,y])
```


reported on [sage-support](http://groups.google.cz/group/sage-support/browse_thread/thread/40eda7084856aa3e)


---

Attachment


---

Comment by robert.marik created at 2010-03-10 10:11:59

Changing status from new to needs_review.


---

Comment by AlexGhitza created at 2010-04-02 05:48:35

The patch applies cleanly to sage-4.3.5 and passes long doctests.


---

Comment by AlexGhitza created at 2010-04-02 05:48:35

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-16 17:28:47

Merged into 4.4.alpha0.


---

Comment by jhpalmieri created at 2010-04-16 17:28:47

Resolution: fixed
