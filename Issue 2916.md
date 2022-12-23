# Issue 2916: [with patch; needs review] invalid coercion between non-prime finite fields

Issue created by migration from https://trac.sagemath.org/ticket/2916

Original creator: wjp

Original creation time: 2008-04-14 14:57:13

Assignee: was

As reported by Kiran Kedlaya on sage-devel:


```
sage: F9.<a> = GF(9); F81.<b> = GF(81); F81(a)
0
```


This is caused by a missing 'else' in the `FiniteField_givaro` constructor. The attached patch throws a `TypeError` in this case and adds this example as a doctest.


---

Attachment


---

Comment by mabshoff created at 2008-04-14 20:26:10

The patch passes doctests on sage.math. Hopefully someone will review this soon.

Cheers,

Michael


---

Comment by malb created at 2008-04-14 20:27:42

Patch looks good and 


```
[21:20] <mabshoff> Can you referee #2916?
[21:20] <mabshoff> It passes doctests on sage.math
```


=> *positive review*


---

Comment by mabshoff created at 2008-04-14 20:36:21

Resolution: fixed


---

Comment by mabshoff created at 2008-04-14 20:36:21

Merged in Sage 3.0.alpha5
