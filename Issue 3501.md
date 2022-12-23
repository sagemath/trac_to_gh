# Issue 3501: [with patch, needs review] charpoly of zero matrix over a cyclotomic field fails

Issue created by migration from https://trac.sagemath.org/ticket/3501

Original creator: craigcitro

Original creation time: 2008-06-24 07:51:07

Assignee: craigcitro

This is broken:


```
sage: Matrix(CyclotomicField(13),3).charpoly()
```


The attached patch fixes it.


---

Attachment


---

Comment by cpernet created at 2008-06-24 23:12:28

This patch looks good and fixes the bug. 
I have run the doctest on 3.0.4alpha1, and they pass.


---

Comment by mabshoff created at 2008-06-25 01:09:23

Resolution: fixed


---

Comment by mabshoff created at 2008-06-25 01:09:23

Merged in Sage 3.0.4.alpha1
