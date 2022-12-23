# Issue 9516: numerical noise in sage-4.5.rc1 on PowerPC OS X

Issue created by migration from https://trac.sagemath.org/ticket/9516

Original creator: was

Original creation time: 2010-07-16 09:38:53

Assignee: mvngu


```
sage -t  -long "devel/sage/sage/plot/plot3d/parametric_surface.pyx"
**********************************************************************
File "/Users/wstein/build/sage-4.5.rc1/devel/sage/sage/plot/plot3d/parametric_surface.pyx", line 311:
    sage: M.bounding_box()
Expected:
    ((-10.0, -7.5390734925047846, -2.9940801852848145), (10.0, 7.5390734925047846, 2.9940801852848145))
Got:
    ((-10.0, -7.5390734925047855, -2.9940801852848145), (10.0, 7.5390734925047846, 2.9940801852848145))
**********************************************************************
1 items had failures:
   1 of   5 in __main__.example_11
***Test Failed*** 1 failures.
For whitespace errors, see the file /Users/wstein/.sage//tmp/.doctest
```



---

Comment by was created at 2010-07-16 09:44:46

Changing status from new to needs_review.


---

Attachment


---

Comment by rlm created at 2010-07-16 09:46:51

Changing status from needs_review to positive_review.


---

Comment by ddrake created at 2010-07-22 02:52:12

This ticket seems the same as #9002...


---

Comment by ddrake created at 2010-07-22 02:54:14

Resolution: duplicate


---

Comment by ddrake created at 2010-07-22 02:54:14

The patches here and at #9002 are identical, but Karl-Dieter beat out William by two months, so I'm closing this ticket and will merge #9002.
