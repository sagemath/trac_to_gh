# Issue 3610: __contains__ for RealIntervalFields does not work correctly.

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2008-07-08 17:41:30

Assignee: somebody


```
sage: (R(2.1) + R(2.2))^2 in R
False
sage: R = RealIntervalField(32)
sage: a = (R(2.1) + R(2.2))^2 
sage: a
[18.489999987 .. 18.490000010]
sage: a in R
False
sage: a.parent()
Real Interval Field with 32 bits of precision
sage: a == a
False
```


This is caused by the following code in which gets inherited from parent.pyx:

```
        try:
            x2 = self(x)
            return bool(x2 == x)
        except TypeError:
            return False
```


Since equality is not reflexive for RealIntervals, this doesn't work as intended.


---

Attachment


---

Comment by robertwb created at 2009-01-24 04:28:49

Looks good to me, and is probably an worthwhile optimization as well.


---

Comment by mabshoff created at 2009-01-24 19:31:24

Resolution: fixed


---

Comment by mabshoff created at 2009-01-24 19:31:24

Merged in Sage 3.3.alpha2

Cheers,

Michael
