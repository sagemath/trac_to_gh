# Issue 5434: [with patch, needs review] .shift() of a zero polynomial is broken

Issue created by migration from https://trac.sagemath.org/ticket/5434

Original creator: cwitty

Original creation time: 2009-03-04 04:02:25

Assignee: cwitty


```
sage: K.<x> = RDF[]
sage: K(0).shift(3).is_zero()
False
sage: K.<x> = RR[]
sage: K(0).shift(3).is_zero()
False
sage: K.<x> = AA[]
sage: K(0).shift(3).is_zero()
False
```




---

Attachment

Excellent.  Thanks!


---

Comment by mabshoff created at 2009-03-05 00:07:32

Resolution: fixed


---

Comment by mabshoff created at 2009-03-05 00:07:32

Merged in Sage 3.4.rc1.

Cheers,

Michael
