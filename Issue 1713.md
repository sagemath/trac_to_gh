# Issue 1713: [with patch] fix SageElement._sage_

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-01-07 14:01:39

Assignee: malb

This didn't work, now it does:


```
sage: sr = mq.SR(allow_zero_inversions=True)
sage: F,s = sr.polynomial_system()
sage: F == sage0(F)._sage_()
True
```



---

Attachment


---

Comment by mhansen created at 2008-01-20 23:47:14

Works for me.


---

Comment by mabshoff created at 2008-01-21 02:04:09

Merged in Sage 2.10.1.alpha1


---

Comment by mabshoff created at 2008-01-21 02:04:09

Resolution: fixed
