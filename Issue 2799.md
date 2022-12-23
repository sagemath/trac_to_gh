# Issue 2799: matrix's __getitem__ doesn't respect slice object's step attribute

Issue created by migration from https://trac.sagemath.org/ticket/2799

Original creator: dfdeshom

Original creation time: 2008-04-04 19:09:31

Assignee: dfdeshom

Ex: ` A[:,0:4:2]` should return the 0th and 2nd column of A, if possible:


```
age: A = matrix(ZZ,3,4, [3, 2, -5, 0, 1, -1, 1, -4, 1, 0, 1, -3]); A
[ 3  2 -5  0]
[ 1 -1  1 -4]
[ 1  0  1 -3]

sage: A[:,0:4:2]
[ 3  2 -5  0]
[ 1 -1  1 -4]
[ 1  0  1 -3]

```



---

Attachment


---

Comment by dfdeshom created at 2008-04-04 22:05:29

I've added a patch which should allow people to do more flexible things such as 
`A[2:-1:-1,3:1:-1] `.


---

Comment by mhansen created at 2008-04-05 10:36:53

Looks good to me.


---

Comment by mabshoff created at 2008-04-05 16:56:53

Resolution: fixed


---

Comment by mabshoff created at 2008-04-05 16:56:53

Merged in Sage 3.0.alpha2
