# Issue 8944: 32 vs. 64 bit issues in matrix1.pyx

Issue created by migration from https://trac.sagemath.org/ticket/8944

Original creator: mvngu

Original creation time: 2010-05-10 11:01:12

Assignee: tbd

From this [sage-devel](http://groups.google.com/group/sage-devel/msg/dbe5b953a06d1f39) report:


```
The first on seems to be a trivial 32-bit vs. 64-bit
issue (probably occurs on any 32-bit machine, even without the "long"
option):

sage -t -long "devel/sage/sage/matrix/matrix1.pyx"
**********************************************************************
File "/Users/Shared/sage/test/sage-4.4.2.alpha0/devel/sage/sage/matrix/
matrix1.pyx", line 460:
    sage: b.dtype
Expected:
    dtype('int64')
Got:
    dtype('int32')
********************************************************************** 
```


This also happens on the Skynet machine cicero, a 32-bit Fedora 12 machine.


---

Attachment

based on Sage 4.4.2.alpha0


---

Comment by mvngu created at 2010-05-10 11:20:28

Changing status from new to needs_review.


---

Comment by cremona created at 2010-05-11 13:06:12

Works fine on both 32 and 64 bit machines.


---

Comment by cremona created at 2010-05-11 13:06:12

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-05-12 22:43:49

Resolution: fixed
