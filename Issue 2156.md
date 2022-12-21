# Issue 2156: [with spkg, needs review] Cython 0.9.6.12

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2008-02-14 04:32:28

Assignee: mabshoff

Get the spkg in http://sage.math.washington.edu/home/robertwb/cython/ 

sage -ba; sage -testall works on intel OS X 10.4. 

The most significant change is more flexible c(p)def functions and overriding. Specifically, c(p)def functions can now:
 * have optional arguments (which may grow)
 * be defined in the module scope
 * are always cimport-able if defined in the .pxd (i.e. "api" by default)
 * declare narrower return types than the superclass
 * cpdef can override cdef

There are also better conversions (<type?> does a type-checked cast, <int>x does the right thing), and numerous optimizations (especially with regard to tuple unpacking) and bugfixes. 



---

Comment by mabshoff created at 2008-02-14 12:58:18

Two things
 * the name of the spkg needs to be lower case, i.e. `Cython` vs. `cython`
 * A `sage -ba` works fine on sage.math, but upon startup I get:

```
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-2.10.2.alpha0$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.10.1, Release Date: 2008-02-02                      |
| Type notebook() for the GUI, and license() for information.        |
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/scratch/mabshoff/release-cycle/sage-2.10.2.alpha0/local/bin/<ipython console> in <module>()

/scratch/mabshoff/release-cycle/sage-2.10.2.alpha0/local/lib/python2.5/site-packages/sage/all_cmdline.py in <module>()
     12 try:
     13
---> 14     from sage.all import *
     15     from sage.calculus.predefined import x
     16     preparser(on=True)

/scratch/mabshoff/release-cycle/sage-2.10.2.alpha0/local/lib/python2.5/site-packages/sage/all.py in <module>()
     59 get_sigs()
     60
---> 61 from sage.rings.all      import *
     62 from sage.matrix.all     import *
     63

/scratch/mabshoff/release-cycle/sage-2.10.2.alpha0/local/lib/python2.5/site-packages/sage/rings/all.py in <module>()
     90
     91 # Algebraic numbers
---> 92 from qqbar import (AlgebraicRealField, is_AlgebraicRealField, AA,
     93                    AlgebraicReal, is_AlgebraicReal,
     94                    AlgebraicField, is_AlgebraicField, QQbar,

/scratch/mabshoff/release-cycle/sage-2.10.2.alpha0/local/lib/python2.5/site-packages/sage/rings/qqbar.py in <module>()
   4038
   4039
-> 4040 RR_1_10 = RR(ZZ(1)/10)
   4041 QQ_0 = QQ(0)
   4042 QQ_1 = QQ(1)

/scratch/mabshoff/release-cycle/sage-2.10.2.alpha0/local/bin/element.pyx in sage.structure.element.RingElement.__div__()

/scratch/mabshoff/release-cycle/sage-2.10.2.alpha0/local/bin/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.bin_op_c()

/scratch/mabshoff/release-cycle/sage-2.10.2.alpha0/local/bin/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.get_action_c()

/scratch/mabshoff/release-cycle/sage-2.10.2.alpha0/local/bin/coerce_dict.pyx in sage.structure.coerce_dict.TripleDict.get()

<type 'exceptions.TypeError'>: 'sage.rings.integer_ring.IntegerRing_class' object cannot be interpreted as an index
sage:
```


Cheers,

Michael


---

Comment by robertwb created at 2008-02-14 18:12:25

Changing the case is easy enough. I'll look into what's going wrong on sage.math.


---

Comment by mabshoff created at 2008-02-14 18:16:37

About the case: sure, I ended up doing that when I looked into the spkg and made sure there was no "junk" in it due to the increased size.

An interesting data point: After installing the old cython.spkg (0.9.6.11b) and doing a `sage -ba` I still go the same error. Only after deleting the installed Cython in `site-packages`, doing another install of 0.9.6.11b and then `sage -ba` did the error disappear.

Cheers,

Michael


---

Comment by robertwb created at 2008-02-14 18:25:04

I thing the above may be a case issue (cython didn't overwrite Cython) but I know what the issue is--there's a patch that needs to be installed because <int>x no longer returns the address of x (which is used in `coerce_dict.TripleDict.get()`.


---

Attachment

I've uploaded a new spkg with a lowercase 'c' to the same directory as before. With the attached patch, things should work fine.


---

Comment by mabshoff created at 2008-02-14 20:39:43

Good news: the updated spkg and the additional patch make sage start after a `sage -ba`. Ergo positive review, running `-testall` to make sure everything is still working.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-14 21:29:08

Resolution: fixed


---

Comment by mabshoff created at 2008-02-14 21:29:08

Merged in Sage 2.10.2.alpha0
