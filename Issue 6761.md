# Issue 6761: solve_left on a vector returns a matrix

Issue created by migration from https://trac.sagemath.org/ticket/6761

Original creator: robertwb

Original creation time: 2009-08-16 09:13:10

Assignee: was

CC:  jason

This is inconsistent with solve_right and contrary to the documentation. 


```
sage: A = random_matrix(ZZ, 5)
sage: b = vector(ZZ, range(5))
sage: A.solve_left(b)
[    47/630  -233/1170       2/65     34/819 -5269/8190]
sage: A.solve_left(b).parent()
Full MatrixSpace of 1 by 5 dense matrices over Rational Field
```



---

Attachment


---

Comment by klee created at 2009-11-06 08:19:47

Changing status from new to needs_review.


---

Comment by robertwb created at 2009-11-06 20:06:20

Changing status from needs_review to positive_review.


---

Comment by robertwb created at 2009-11-06 20:06:20

Thanks!


---

Comment by mhansen created at 2009-11-07 04:59:37

Resolution: fixed
