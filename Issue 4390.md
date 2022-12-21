# Issue 4390: elliptic curves: heegner_index command broken

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-10-30 05:35:53

Assignee: was


```
sage: EllipticCurve('675b').heegner_index(-11)
Traceback (most recent call last):
...
TypeError: regulator() got an unexpected keyword argument 'verbose'
```



---

Attachment


---

Comment by craigcitro created at 2008-10-30 05:43:00

Looks good.


---

Comment by mabshoff created at 2008-10-30 05:46:19

Merged in Sage 3.2.alpha2


---

Comment by mabshoff created at 2008-10-30 05:46:19

Resolution: fixed
