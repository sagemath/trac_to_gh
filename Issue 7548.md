# Issue 7548: modular form times scalar = boom

Issue created by migration from https://trac.sagemath.org/ticket/7548

Original creator: AlexGhitza

Original creation time: 2009-11-28 04:25:04

Assignee: craigcitro


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: M = CuspForms(Gamma0(5*3^2), 2)
sage: f = M.basis()[0]
sage: f
q - q^4 + O(q^6)
sage: 2*f
2*q - 2*q^4 + O(q^6)
sage: f*2
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
| Sage Version 4.2.1, Release Date: 2009-11-14                       |
| Type notebook() for the GUI, and license() for information.        |
/home/ghitza/.sage/temp/artin/19582/_home_ghitza__sage_init_sage_0.py in <module>()

/home/ghitza/sage-devel/local/lib/python2.6/site-packages/sage/modular/modform/element.pyc in __mul__(self, other)
    967         # boring case: scalar multiplication

    968         if not isinstance(other, ModularFormElement):
--> 969             return HeckeModuleElement.__mul__(self, other)
    970 
    971         # first ensure the levels are equal


NameError: global name 'HeckeModuleElement' is not defined
```




---

Comment by AlexGhitza created at 2010-01-03 07:23:35

Changing status from new to needs_review.


---

Comment by AlexGhitza created at 2010-01-03 07:23:35

Well, the fix was embarrassingly trivial.  Patch is attached.


---

Attachment


---

Comment by was created at 2010-01-03 18:22:59

Looks good.


---

Comment by was created at 2010-01-03 18:22:59

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-01-03 21:33:47

Resolution: fixed
