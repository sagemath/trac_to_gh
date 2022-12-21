# Issue 5121: major bug in plot command

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-01-28 20:07:18

Assignee: was


```
sage: E = EllipticCurve('37a')
sage: plot(E)
sage: plot(E, xmin=25,xmax=25)
Traceback (most recent call last):
...
AttributeError: 'SymbolicEquation' object has no attribute '_fast_float_'
```


This broke David Hansen's thesis.  It also caused me a lot of embarasement during my talk at Sage Days 12!!!

It is a new bug introduced by some plot refactoring recently. 


---

Comment by jason created at 2009-01-28 21:19:07

Apparently a block of code was not indented correctly.  I'll post up a patch momentarily.


---

Comment by jason created at 2009-01-28 21:56:01

This broke in the commit http://www.sagemath.org/hg/sage-main/diff/ed11b267ec9f/sage/plot/plot.py


---

Attachment


---

Comment by mabshoff created at 2009-01-29 00:27:53

Merged in Sage 3.3.alpha3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-29 00:27:53

Resolution: fixed
