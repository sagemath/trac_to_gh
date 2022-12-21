# Issue 1154: lost precision in RQDF -> RealField conversion

Issue created by migration from Trac.

Original creator: zimmerma

Original creation time: 2007-11-12 14:36:07

Assignee: jkantor


```
sage: R = RealField(206)
sage: a = R(5292635226105886036954352397762172773270339156347702272822435/2^205)
sage: b = RQDF(a)
sage: c = R(b)
self= 0.102925468350634334254648605229306925849343943655945448198193123
sage: a - c
1.215432671457254239676575010503930515740283626703352955683812e-63
```


I checked with b.get_doubles() that b == a, but was unable to find the routine which performs
the conversion from b (RQDF) to c (RealField). It seems R._set_from_qd is not used.


---

Comment by cwitty created at 2007-12-02 06:33:51

Resolution: duplicate


---

Comment by cwitty created at 2007-12-02 06:33:51

This is one of the issues that's covered by the patch at #1162.
