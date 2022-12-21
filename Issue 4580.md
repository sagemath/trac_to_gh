# Issue 4580: [with patch, needs review] move mpfr declarations to a pxd

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2008-11-22 01:36:22

Assignee: somebody

for consistency and in preparation for further cython optimizations


---

Attachment


---

Comment by robertwb created at 2008-11-22 01:39:58

Followup to #846


---

Comment by cwitty created at 2008-11-23 04:57:41

I can't get this to compile; see #4592 for what I think is going wrong.


---

Comment by cwitty created at 2008-11-23 16:34:25

This patch looks good, but exposes a bug in setup.py (see #4597).  I think that if this patch were applied without fixing setup.py, then `sage -upgrade` would fail, unless the user removed the .cython_deps file (or unless `sage -upgrade` automatically removes that file).

So, positive review on this patch itself, but we might want to hold off applying it until #4597 is fixed.


---

Comment by cwitty created at 2008-11-25 01:41:32

OK, there's a patch up for #4597 with a positive review.


---

Comment by mabshoff created at 2008-11-25 02:42:37

I had to rebase the following hunk from the above patch:

```
***************
*** 10,24 ****
  from sage.structure.element cimport Element, ModuleElement, RingElement
  from sage.structure.element import parent
  
- # import the mpfr stuff from RealNumber becase it's included, not cimported
- from sage.rings.real_mpfr cimport mpfr_t, mp_rnd_t
- from sage.rings.real_mpfr cimport *
- 
- cdef extern from "mpfr.h":
-     int mpfr_mul_ui (mpfr_t rop, mpfr_t op1, unsigned long int op2, mp_rnd_t rnd)
-     int mpfr_div_ui (mpfr_t rop, mpfr_t op1, unsigned long int op2, mp_rnd_t rnd)
-     int mpfr_cmp_si (mpfr_t op1, signed long int op2)
-     int mpfr_cmpabs (mpfr_t op1, mpfr_t op2)
          
  cdef class PolynomialRealDense(Polynomial):
      
--- 13,19 ----
  from sage.structure.element cimport Element, ModuleElement, RingElement
  from sage.structure.element import parent
  
+ from sage.libs.mpfr cimport *
          
  cdef class PolynomialRealDense(Polynomial):
```


Other than that everything looks fine. 

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-25 02:42:52

Resolution: fixed


---

Comment by mabshoff created at 2008-11-25 02:42:52

Merged in Sage 3.2.1.alpha1
