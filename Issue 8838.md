# Issue 8838: make "arrow()" take 3d vectors

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2010-05-01 19:25:58

Assignee: jason, was

CC:  kcrisman ryan

A convention we have is that graphics commands do the right thing depending on if 2d or 3d input is passed.  We should make arrow() take 3-tuples to produce a 3d plot (by calling arrow3d).


---

Comment by jason created at 2010-05-26 15:32:18

Changing keywords from "" to "beginner".


---

Comment by jason created at 2010-08-26 22:40:37

In other words, this should work:


```
sage: arrow(vector([1,2,3]), vector([2,3,4]))
```


and should draw a 3d arrow.


---

Attachment

make arrow() behave more like line()


---

Comment by ryan created at 2010-08-28 02:59:38

here is a patch that changes the behavior of arrow() to be more like line().  

If 2d coordinates are passed, arrow() returns an arrow2d() (the old arrow() function).  If 3d coordinates are passed, arrow() will now return an arrow3d().


---

Comment by ryan created at 2010-08-28 02:59:38

Changing status from new to needs_review.


---

Comment by jason created at 2010-08-29 02:59:17

Changing status from needs_review to needs_work.


---

Comment by jason created at 2010-08-29 02:59:17

This looks great.  However, for backwards compatibility, could you name the arguments to arrow() "tailpoint" and "headpoint".  Now, this command won't work, whereas before it would:


```
arrow(tailpoint=(0,1), headpoint=(2,3))
```


We should keep our API unless there is a very good reason to change it.


---

Comment by ryan created at 2010-09-11 05:19:12

Updated patch (with Sage 4.5.3)


---

Attachment


---

Comment by ryan created at 2010-09-11 05:25:40

Changing status from needs_work to needs_review.


---

Comment by jason created at 2010-09-11 16:09:24

Looks good! Thanks!

Apply only trac_8838_arrow2d_arrow3d.patch


---

Comment by jason created at 2010-09-11 16:09:24

Changing status from needs_review to positive_review.


---

Comment by jason created at 2010-09-11 16:23:13

Note that this is Ryan's first contribution (along with #9199 and #7154)


---

Comment by mpatel created at 2010-09-15 10:40:32

Resolution: fixed
