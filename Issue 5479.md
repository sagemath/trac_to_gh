# Issue 5479: schemes/generic/spec.py: Spec.__call__ is basically not implemented

Issue created by migration from https://trac.sagemath.org/ticket/5479

Original creator: AlexGhitza

Original creation time: 2009-03-11 04:09:10

Assignee: was

Roi Docampo found this:

```
sage: S = Spec(ZZ)
sage: S
Spectrum of Integer Ring
sage: S(3)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/aghitza/.sage/temp/cartan/6737/_home_aghitza__sage_init_sage_0.py in <module>()

/opt/sage/local/lib/python2.5/site-packages/sage/schemes/generic/spec.pyc in __call__(self, x)
    112         Create a point of this scheme.
    113         """
--> 114         return point.SchemePoint_spec(self, x)
    115 
    116     def coordinate_ring(self):

AttributeError: 'module' object has no attribute 'SchemePoint_spec'
```



---

Comment by AlexGhitza created at 2009-04-25 11:12:53

Changing status from new to assigned.


---

Comment by AlexGhitza created at 2009-04-25 11:12:53

Changing assignee from was to AlexGhitza.


---

Comment by AlexGhitza created at 2009-04-25 11:12:53

The attached patch implements the `__call__` method.  For this I needed to fix a few things in `schemes/generic/point.py` (which has 0 doctests!).  I doctested the methods that I touched there, and I'll improve the doctest coverage further in another patch.


---

Comment by AlexGhitza created at 2009-04-25 11:12:53

Changing keywords from "" to "spectrum ring call".


---

Attachment

David Roe pointed out in IRC that "generic point" has a well-defined technical meaning so it shouldn't be used in the `_repr_` method of `SchemeMorphism`.  So I've attached an updated patch that fixes the handful of occurrences of "Generic point".


---

Comment by roed created at 2009-04-29 18:04:31

Looks good now.


---

Comment by mabshoff created at 2009-04-30 01:17:47

Merged in Sage 3.4.2.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-30 01:17:47

Resolution: fixed
