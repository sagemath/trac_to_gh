# Issue 4263: elliptic curves -- point height serious stupid bug in raising error

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-10-11 08:46:08

Assignee: was

This is dumb (first thing I tried broke):

```
sage: E = EllipticCurve('5077a1')
sage: F = E.change_ring(QuadraticField(-3,'a'))
sage: P = F([-2,3,1])
sage: s = P.height(); s
sage: type(s)
<type 'NoneType'>
```





---

Attachment


---

Comment by malb created at 2008-10-11 10:01:52

looks good to me.


---

Comment by mabshoff created at 2008-10-11 12:13:11

Resolution: fixed


---

Comment by mabshoff created at 2008-10-11 12:13:11

Merged in Sage 3.1.3.rc0
