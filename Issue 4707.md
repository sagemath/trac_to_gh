# Issue 4707: magma/sage interface -- another trivial easy-to-fix failure hopefully

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-12-05 02:28:26

Assignee: was


```
sage: E = EllipticCurve(GF(25,'a'), [0,0,1,4,0])
sage: magma(E)
boom
```



---

Attachment


---

Attachment

Works for me.  Apply both patches.  We will open a separate ticket for the corresponding magma -> sage conversion.


---

Comment by was created at 2008-12-11 04:58:07

fix typo in title


---

Comment by mabshoff created at 2008-12-11 11:09:55

Merged both patches in Sage 3.2.2.alpha2


---

Comment by mabshoff created at 2008-12-11 11:09:55

Resolution: fixed
