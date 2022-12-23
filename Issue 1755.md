# Issue 1755: Hook block matrices into matrix(...) command

Issue created by migration from https://trac.sagemath.org/ticket/1755

Original creator: robertwb

Original creation time: 2008-01-11 03:17:59

Assignee: was

Add the ability to access the functionality of #1732 to the default matrix(...) constructor.


---

Comment by malb created at 2009-01-22 22:38:03

Changing type from defect to enhancement.


---

Comment by @black-stones created at 2018-05-13 15:49:14

Changing status from new to needs_review.


---

Comment by @black-stones created at 2018-05-13 15:49:14

This is already implemented as block_matrix()


```
sage: A = random_matrix(ZZ, 2)
sage: B = random_matrix(ZZ, 2)
sage: C = random_matrix(ZZ, 2)
sage: D = random_matrix(ZZ, 2)
sage: block_matrix( [[A, B], [C, D]] )
[  1  -3| -1  -1]
[  0   0|  1   1]
[-------+-------]
[  0   0| -5   1]
[ -1   0|-10  31]
```


I don't think matrix() should create block matrices. It's possible that one would want a matrix of matrices rather than to merge the matrices together.


---

Comment by mmezzarobba created at 2018-05-31 07:37:33

Changing status from needs_review to positive_review.


---

Comment by embray created at 2019-02-26 13:58:00

Presuming these are all correctly reviewed as either duplicate, invalid, or wontfix.


---

Comment by embray created at 2019-02-26 13:58:00

Resolution: invalid
