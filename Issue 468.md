# Issue 468: quaddouble wrapper sets fpu precision to 53 bits for entire sage session

Issue created by migration from https://trac.sagemath.org/ticket/468

Original creator: bober

Original creation time: 2007-08-20 20:58:22

Assignee: bober

Keywords: quaddouble, fpu, ReadQuadDouble

sage/rings/real_rqdf.pyx contains the following code:


```
cdef class RealQuadDoubleField_class(Field):
    """
    Real Quad Double Field
    """

    def __init__(self):
        fpu_fix_start(self.cwf)        

    def __dealloc__(self):
        fpu_fix_end(self.cwf)
```


On systems where `fpu_fix_start()` does something, it sets the fpu precision to 53 bits. A poor side effect of this is that the type `long double` ought to have 64 bits of precision on some systems, but it doesn't when it is used in code run from SAGE.

The short term fix will be to rewrite the wrapper to have an fpu_fix_start() and fpu_fix_end() call before and after every arithmetic operation on a `RealQuadDouble` element, and nowhere else, to make sure that the quaddouble wrapper doesn't ever unexpected change the fpu precision.

It would also be nice to have a doctest that can check the fpu precision, so it can be checked that nothing ever changes it unexpectedly.


---

Attachment

This patch should fix this issue.


---

Comment by bober created at 2007-08-23 18:23:04

x86 specific fpu stuff -- see ticket discussion (this should NOT be included in sage)


---

Attachment

The attachment `5835-fpu-status.patch` provides a module for checking/setting the fpu precision on an x86 processor, which can be useful for debugging problems like this one. Some example usage of this patch:


```
sage: import sage.misc.fpu as fpu
sage: fpu.get_precision()
'extended'
sage: fpu.set_double_precision()
sage: fpu.get_precision()
'double'
sage: fpu.set_single_precision()
sage: fpu.get_precision()
'single'
sage: fpu.set_extended_precision()
sage: fpu.get_precision()
'extended'
```


This patch should NOT be included in sage currently, as it relies on an x86 processor to function, and also just isn't written very nicely in general.


---

Comment by bober created at 2007-08-23 18:29:30

Changing component from algebraic geometry to basic arithmetic.


---

Comment by was created at 2007-10-13 06:42:29

Resolution: fixed
