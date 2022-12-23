# Issue 61: hanke -- disturbing matrix constructor issue involving rows versus columns

Issue created by migration from https://trac.sagemath.org/ticket/61

Original creator: was

Original creation time: 2006-09-14 22:26:29

Assignee: somebody

Hi William,
 
I just found a disturbing trait about Matrix constructions, and was
wondering if you could include a rows/columns flag to address it.
 

When a matrix is constructed from tuples, it assumes that you want to
use these numbers as *rows*, regardless of whether the tuples are
appropriately sized.  Since there is no way of deciding which is meant
for square matrices, it seems reasonable to add an extra (mandatory)
flag to the constructor for a list of tuples to ask which is meant.
 


I hope your semster is going well.   See you,
 
						-Jon (Hanke)
						 

```
--------------------------------------------------------------------
 
sage: M2 = MatrixSpace(ZZ,2,4)(range(8)); M2
[0 1 2 3]
[4 5 6 7]
 
sage: M2.columns()
 [(0, 4), (1, 5), (2, 6), (3, 7)]
 
sage: MatrixSpace(ZZ,2,4)(M2.columns())
[0 4 1 5]
[2 6 3 7]
 
sage: M2 == MatrixSpace(ZZ,2,4)(M2.columns())
 False
 
sage: M2 == MatrixSpace(ZZ,2,4)(M2.rows())
 True
```



---

Comment by mabshoff created at 2007-08-23 11:11:39

This is still a problem with Sage 2.8.2. The 2.8.3 release might cut it a little close because there are still a large number of tickets left (to be fixed in roughly 1 day).

Cheers,

Michael


---

Comment by mhansen created at 2007-09-21 05:23:09

Changing assignee from somebody to mhansen.


---

Comment by mhansen created at 2007-11-03 18:11:46

Changing status from new to assigned.


---

Attachment


---

Comment by was created at 2007-11-03 23:46:08

Resolution: fixed


---

Attachment
