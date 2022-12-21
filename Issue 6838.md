# Issue 6838: error creating matrices over GF(2) from elements of QQ

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2009-08-28 21:05:10

Assignee: was

CC:  was rbradshaw malb

Yet another thing I can't understand:


```
sage: GF(2)(1/3)
1
sage: MatrixSpace(GF(2), 1, 1)([1/3])
[0]
```


For the record:


```
sage: MatrixSpace(Zmod(4), 1, 1)([1/3])
[3]
sage: Zmod(4)(1/3)
3
```


So it's not always broken.


---

Attachment


---

Comment by mhansen created at 2009-09-01 22:36:47

Changing status from new to assigned.


---

Comment by mhansen created at 2009-09-01 22:36:47

Changing assignee from was to mhansen.


---

Comment by malb created at 2009-09-02 00:06:50

Patch looks good.


---

Comment by mvngu created at 2009-09-02 16:50:06

Resolution: fixed
