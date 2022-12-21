# Issue 5476: dimension of jacobian of curves broken

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-03-10 22:02:08

Assignee: was


```
sage: k.<a> = GF(9); R.<x> = k[]
sage: HyperellipticCurve(x^3 + x - 1, x+a).jacobian().dimension()
boom!
```


This was found during Alex G.'s talk at Sage Days 14.


---

Attachment


---

Comment by mhansen created at 2009-03-11 03:30:48

Looks good to me.


---

Comment by mabshoff created at 2009-03-11 03:45:19

Resolution: fixed


---

Comment by mabshoff created at 2009-03-11 03:45:19

Merged in Sage 3.4.final.

Cheers,

Michael
