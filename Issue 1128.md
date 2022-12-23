# Issue 1128: Coercion of complex numbers

Issue created by migration from https://trac.sagemath.org/ticket/1128

Original creator: robertwb

Original creation time: 2007-11-08 05:44:47

Assignee: somebody


```
sage: ComplexField(200)(1) + RealField(100)(1)
<type 'exceptions.TypeError'>: unsupported operand parent(s) for '+': 'Complex Field with 200 bits of precision' and 'Real Field with 100 bits of precision'
```

Should return an element of ComplexField(100)

This should be an easy fix, see 

http://groups.google.com/group/sage-devel/browse_thread/thread/5bc6c9190a3da63e/597d0eb7a45dae11?lnk=gst&q=complexfield#597d0eb7a45dae11




---

Comment by roed created at 2007-12-02 06:13:19

Changing assignee from somebody to roed.


---

Attachment

Adds algebraic completion functor


---

Comment by robertwb created at 2007-12-02 07:29:39

cleaner patch


---

Attachment

Yep, works great.


---

Comment by mabshoff created at 2007-12-02 08:07:26

Resolution: fixed


---

Comment by mabshoff created at 2007-12-02 08:07:26

Merged in 2.8.15.alpha2. I did merge trac1128.2.patch.
