# Issue 1600: another weird coercion bug

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2007-12-26 17:29:30

Assignee: somebody

Haven't even started trying to track this one down yet:


```
sage: S.<s> = LaurentSeriesRing(GF(5))
sage: T.<t> = PowerSeriesRing(pAdicRing(5))
sage: 
sage: S(t)
(1 + O(5^20))*s
sage: parent(S(t))
Laurent Series Ring in s over Finite Field of size 5
sage: parent(S(t)[1])
5-adic Ring with capped relative precision 20
```


Pretty nasty.



---

Attachment


---

Comment by craigcitro created at 2008-01-21 09:38:30

Changing status from new to assigned.


---

Comment by craigcitro created at 2008-01-21 09:38:30

Changing assignee from somebody to craigcitro.


---

Comment by craigcitro created at 2008-01-21 09:38:30

Actually, this one turned out to be low-hanging fruit. The issue was that if the object being passed in to __call__ was already a power series, it didn't bother to try and coerce it -- obviously this is silly, since whenever the base_rings are different, some coercion needs to happen.


---

Comment by malb created at 2008-01-26 11:05:49

patch looks good, does what it is supposed to do, is documented. I say apply.


---

Comment by mabshoff created at 2008-01-26 11:16:50

Resolution: fixed


---

Comment by mabshoff created at 2008-01-26 11:16:50

Merged in Sage 2.10.1.rc0
