# Issue 3500: [with patch, needs review] bug in cyclotomic linear algebra code

Issue created by migration from https://trac.sagemath.org/ticket/3500

Original creator: craigcitro

Original creation time: 2008-06-24 06:49:15

Assignee: craigcitro

Wow, here's an embarrassing bug in the cyclotomic linear algebra code:


```
sage: cf4 = CyclotomicField(4) ; z4 = cf4.0
sage: A = Matrix(cf4, 1, 2, [-z4, 1])
sage: A.echelon_form()

[1 0]
[0 1]
```


The attached patch fixes it. 


---

Attachment

This patch looks correct and fixes the bug. 
The docstrings pass on 3.0.4alpha1.


---

Comment by mabshoff created at 2008-06-25 01:09:10

Merged in Sage 3.0.4.alpha1


---

Comment by mabshoff created at 2008-06-25 01:09:10

Resolution: fixed
