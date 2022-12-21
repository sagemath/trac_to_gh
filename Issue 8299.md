# Issue 8299: coercion and the bool type

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2010-02-18 22:28:12

Assignee: robertwb

Clearly this is undesirable:


```
sage: 5r + True
6
sage: 5 + True
2
```



---

Attachment


---

Comment by robertwb created at 2010-02-18 22:30:21

Changing status from new to needs_review.


---

Comment by rossk created at 2010-02-26 11:13:31

Changing status from needs_review to positive_review.


---

Comment by rossk created at 2010-02-26 11:13:31

All good Robert. This patch treats True as 1, False as 0 for arithmetic with non-complex types.

```
sage: [k+True for k in (3, 3r, 3.0, 3.0r, 1/3, 3*I+5)]
[4, 4, 4.00000000000000, 4.0, 4/3, 2]

sage: [k+False for k in (3, 3r, 3.0, 3.0r, 1/3, 3*I+5)]
[3, 3, 3.00000000000000, 3.0, 1/3, 1]

sage: [k*True for k in (3, 3r, 3.0, 3.0r, 1/3, 3*I+5)]
[3, 3, 3.00000000000000, 3.0, 1/3, 1]

sage: [k*False for k in (3, 3r, 3.0, 3.0r, 1/3, 3*I+5)]
[0, 0, 0.000000000000000, 0.0, 0, 0]
```



---

Comment by mvngu created at 2010-03-02 21:15:38

Resolution: fixed
