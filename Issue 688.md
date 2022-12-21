# Issue 688: conversion to Singular for QuotientRingElements broken

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2007-09-18 13:09:54

Assignee: was

Consider:


```
sage: P.<x,y>  = PolynomialRing(GF(2),2)
sage: I = sage.rings.ideal.FieldIdeal(P)
sage: Q = P.quo(I)
sage: Q._singular_()

//   characteristic : 2
//   number of vars : 2
//        block   1 : ordering dp
//                  : names    x y
//        block   2 : ordering C
// quotient ring from ideal
_[1]=x2+x
_[2]=y2+y
sage: Q(x)
xbar
sage: Q(x)._singular_()
--------------------------------------------------------------
<type 'exceptions.TypeError'> Traceback (most recent call last)
...
<type 'exceptions.TypeError'>: Singular error:
   ? `xbar` is undefined
   ? error occurred in STDIN line 185: `def sage69=xbar;`
```



---

Comment by was created at 2007-09-21 00:25:56

Did this ever work?  Is this really a feature request?


---

Attachment


---

Comment by malb created at 2007-10-20 21:46:03

Changing status from new to assigned.


---

Comment by malb created at 2007-10-20 21:46:03

Changing assignee from was to malb.


---

Comment by malb created at 2007-10-20 21:46:03

Fixed in attached patch.


---

Comment by was created at 2007-10-20 21:48:59

Resolution: fixed


---

Comment by was created at 2007-10-20 21:52:46

inst.tex.hg is a bundle against hg_sage.  You accidently did hg_sage.send('...') instead of
hg_doc.send('...').  Please create a bundle against the docs.


---

Comment by was created at 2007-10-20 21:52:59

That comment was meant for a different ticket. Sorry.
