# Issue 5102: eisenstein_series_qexp broken over finite fields

Issue created by migration from Trac.

Original creator: AlexGhitza

Original creation time: 2009-01-26 04:45:32

Assignee: AlexGhitza

CC:  craigcitro


```
sage: eisenstein_series_qexp(10, 15, GF(17))
15 + q + 3*q^2 + 15*q^3 + 7*q^4 + 13*q^5 + 11*q^6 + 11*q^7 + 15*q^8 + 7*q^9 + 5*q^10 + 7*q^11 + 2*q^12 + 12*q^13 + 12*q^14 + O(q^15)
```


is wrong, whereas


```
sage: eisenstein_series_qexp(10, 15).change_ring(GF(17))
15 + q + 3*q^2 + 15*q^3 + 7*q^4 + 13*q^5 + 11*q^6 + 11*q^7 + 15*q^8 + 7*q^9 + 5*q^10 + 7*q^11 + 3*q^12 + 14*q^13 + 16*q^14 + O(q^15)
```


is right.  We tracked this down to a change in the polynomials over finite fields constructor when `check=False`.  We'll quickly fix this at the cost of making it slower; better fix will come soon.



---

Attachment

Credit to Craig Citro and Alex Ghitza.


---

Comment by AlexGhitza created at 2009-01-26 04:55:21

Changing priority from major to blocker.


---

Comment by mhansen created at 2009-01-30 23:17:34

This gets a positive review from William.


---

Comment by mabshoff created at 2009-02-02 02:45:56

Resolution: fixed


---

Comment by mabshoff created at 2009-02-02 02:45:56

Merged in Sage 3.3.alpha4.

Cheers,

Michael
