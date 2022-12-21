# Issue 2871: matrix: M[range(2,-1,-1),:] returns junk

Issue created by migration from Trac.

Original creator: dfdeshom

Original creation time: 2008-04-10 18:13:17

Assignee: dfdeshom

In the following example, A should be "upside down", but it's not

```
sage: A = random_matrix(ZZ,3); A

[ 1  3 -1]
[ 4 -3 -1]
[-1  0 -1]

sage: A[range(2,-1,-1),:]

[ 1  3 -1]
[ 4 -3 -1]
[-1  0 -1]

```


The problem is with `set()`, which doesn't preserve order.


---

Attachment

The code and doctests look good, and doctests pass in sage/matrix in Sage 2.11.  Unfortunately, applying the patch to Sage 3.0 alpha 2 (the latest I have at the moment) gives a rejected hunk.


---

Comment by dfdeshom created at 2008-04-12 04:48:37

patch against alpha2


---

Attachment

With the revised 2871-alpha2.patch, the patch applies and doctests pass in sage/matrix for sage 3.0 alpha2.

Didier, thanks for making the changes I requested on IRC!

Looks good, please apply.


---

Comment by mabshoff created at 2008-04-12 10:01:04

Merged 2871-alpha2.patch in Sage 3.0.alpha4


---

Comment by mabshoff created at 2008-04-12 10:01:04

Resolution: fixed
