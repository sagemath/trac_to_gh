# Issue 3495: [with patch, needs review] bug in cyclotomic charpoly for 1x1 matrices

Issue created by migration from Trac.

Original creator: craigcitro

Original creation time: 2008-06-23 18:53:49

Assignee: craigcitro

The following will crash in sage:


```
sage: Matrix(CyclotomicField(3), 1, [0]).charpoly()
```


The attached patch fixes it.


---

Attachment


---

Comment by was created at 2008-06-23 19:17:54

REFEREE REPORT:

  * +1; this works as advertised

Reminder -- need to also fix 0x0 as another ticket...


---

Comment by craigcitro created at 2008-06-23 19:22:01

The 0x0 is #3496.


---

Comment by mabshoff created at 2008-06-23 23:10:22

Merged in Sage 3.0.4.alpha1


---

Comment by mabshoff created at 2008-06-23 23:10:22

Resolution: fixed
