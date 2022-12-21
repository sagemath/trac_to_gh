# Issue 1639: missing documentation P.completion()

Issue created by migration from Trac.

Original creator: schilly

Original creation time: 2007-12-30 13:35:00

Assignee: tba

How works completion?



```
P.<x> = PolynomialRing(QQ); P.completion?
```



tells me


```
File:        /opt/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py
Type:        <type 'instancemethod'>
Definition:  P.completion(p, prec, extras)
Docstring: 
x.__init__(...) initializes x; see x.__class__.__doc__ for signature
```



what's the p and examples are missing...


---

Comment by AlexGhitza created at 2008-02-03 17:07:05

Changing assignee from tba to failure.


---

Comment by AlexGhitza created at 2008-02-03 17:07:05

Changing component from documentation to doctest.


---

Attachment

adds docstring and examples


---

Comment by cremona created at 2008-02-17 22:45:35

The attached patch adds docstring and tests.

This ticket should perhaps be kept open in another form so that someone could implement the completion function for irreducuble polynomials other than just x.  I am happy to be the owner of that.


---

Comment by mhansen created at 2008-02-27 23:53:18

Applies to 2.10.3.alpha0 and passes tests for me.


---

Comment by mabshoff created at 2008-02-28 06:52:34

Resolution: fixed


---

Comment by mabshoff created at 2008-02-28 06:52:34

Merged in Sage 2.10.3.rc0
