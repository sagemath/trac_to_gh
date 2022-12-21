# Issue 4093: [with patch, needs review] fix numerical fuzz in period_lattice for 3.1.2

Issue created by migration from Trac.

Original creator: cremona

Original creation time: 2008-09-09 19:28:19

Assignee: cremona

Keywords: elliptic curve period lattice

3.1.2.rc1 has this doctest failure:

```
File "/home/john/sage-3.1.2.rc1/tmp/period_lattice.py", line 281:
    sage: EllipticCurve('389a1').period_lattice().sigma(CC(2,1))
Expected:
    2.609121635701083769 - 0.20086508082458695134*I
Got:
    2.609121635701083769 - 0.20086508082458695200*I
```


The patch fixes this by replacin the last 3 digits above by "...".



---

Attachment


---

Comment by mabshoff created at 2008-09-09 19:32:51

Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-10 01:10:55

Resolution: fixed


---

Comment by mabshoff created at 2008-09-10 01:10:55

Merged in Sage 3.1.2.rc2
