# Issue 5916: [with patch, needs review] show mathematica expression using jsmath

Issue created by migration from Trac.

Original creator: whuss

Original creation time: 2009-04-28 08:35:25

Assignee: whuss

CC:  jason

Show mathematica expressions in the notebook using jsmath.


---

Attachment


---

Comment by jason created at 2009-05-30 06:21:14

This works great and passes doctests in the file.  Positive review.


---

Comment by mhansen created at 2009-06-01 01:09:49

Merged in 4.0.1.alpha0.


---

Comment by mhansen created at 2009-06-01 01:09:49

Resolution: fixed


---

Comment by mvngu created at 2009-06-04 13:56:59

It looks like we can use a screenshot to show the feature this patch introduces. If I'm not mistaken, can someone please upload such a screenshot so it can be put in the release tour.


---

Attachment

Replying to [comment:4 mvngu]:
> It looks like we can use a screenshot to show the feature this patch introduces. If I'm not mistaken, can someone please upload such a screenshot so it can be put in the release tour.

I attached the image which is produced by:


```
m = mathematica("Product[(3/2)^i, {i, 1, n}]")
show(m)
```

