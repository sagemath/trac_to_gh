# Issue 2233: [with patch] "valuation too large" in padics on 64bit

Issue created by migration from Trac.

Original creator: wjp

Original creation time: 2008-02-20 15:00:48

Assignee: was


```
sage: K = Qp(19, 5, 'capped-rel','series')
sage: K(5,3)^19
<type 'exceptions.ValueError'>: Valuation too large
```


This is caused by an int constant 1 being left-shifted by 62 and overflowing. Changing this constant to a long constant seems to fix it. See attached patch.


---

Attachment


---

Attachment


---

Comment by mabshoff created at 2008-02-20 17:20:03

Resolution: fixed


---

Attachment

Merged all three patches in Sage 2.10.2.alpha2
