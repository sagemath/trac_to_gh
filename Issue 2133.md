# Issue 2133: running dimension_modular_forms on weight 0 should return 1 (trivial to fix)

Issue created by migration from Trac.

Original creator: AlexGhitza

Original creation time: 2008-02-09 22:44:29

Assignee: AlexGhitza

It should say 1, but now says


```
sage: dimension_modular_forms(1, 0)
---------------------------------------------------------------------------
<type 'exceptions.NotImplementedError'>   Traceback (most recent call last)

/home/ghitza/sage/eigensystems/<ipython console> in <module>()

/opt/sage/local/lib/python2.5/site-packages/sage/modular/dims.py in dimension_modular_forms(X, k)
   1004     if congroup.is_GammaH(X):
   1005         return dimension_modular_forms_H(X, k)
-> 1006     return dimension_cusp_forms(X, k) + dimension_eis(X, k)
   1007 
   1008 def sturm_bound(level, weight):

/opt/sage/local/lib/python2.5/site-packages/sage/modular/dims.py in dimension_eis(X, k)
    939     if k <= 1:
    940         # TODO
--> 941         raise NotImplementedError, "Dimension of weight <= 1 Eisenstein series not yet implemented."
    942     if isinstance(X, (int,long,Integer)):
    943         if k%2 == 1: return 0

<type 'exceptions.NotImplementedError'>: Dimension of weight <= 1 Eisenstein series not yet implemented.
```





---

Attachment


---

Comment by AlexGhitza created at 2008-02-17 01:41:04

... and the trivial fix is in the attached patch (together with a couple of trivial typos).


---

Attachment

apply this and the previous patch; this just adds a doctest


---

Comment by was created at 2008-02-19 16:07:44

Looks great; thanks for fixing the typos too.  I've added a doctest.


---

Comment by mabshoff created at 2008-02-19 16:21:30

Resolution: fixed


---

Comment by mabshoff created at 2008-02-19 16:21:30

Merged both patches in Sage 2.10.2.alpha1
