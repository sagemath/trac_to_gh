# Issue 5589: binomial() doesn't work with negative integers

Issue created by migration from Trac.

Original creator: ddrake

Original creation time: 2009-03-23 09:35:20

Assignee: mhansen

CC:  sage-combinat

Keywords: combinat, binomial coefficients

binomial() returns zero when its "numerator" is a negative integer, but gets it right for floating point numbers:

```
sage: binomial(-1, 5)
0
sage: binomial(-2, 5)
0
sage: binomial(-2.0, 5)
-6.00000000000000
sage: binomial(-1.0, 5)
-1.00000000000000
sage: binomial(-7, 5)  
0
sage: binomial(-7.0, 5)
-462.000000000000
```



---

Attachment


---

Comment by cwitty created at 2009-03-26 00:52:27

All doctests pass, the code looks reasonable, the documentation fixes are nice.  Positive review.


---

Comment by mabshoff created at 2009-03-26 01:13:16

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-26 01:13:16

Resolution: fixed
