# Issue 7898: Change common variables to names in singular

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-01-12 03:12:28

Assignee: GeorgSWeber

CC:  jsp

It was agreed recently that variables would not be used for very common commands like MV, MKDIR etc. 

http://groups.google.com/group/sage-devel/browse_thread/thread/bd7ae07a1157bead/970aa0dc8fa56ab7?lnk=raot

#7818 usets these, so this package will break. The fix is to simply replace things like 

$LN with 'ln'

An updated .spkg can be found at

http://boxen.math.washington.edu/home/kirkby/portability/singular-3-1-0-4-20090818.p3/singular-3-1-0-4-20090818.p3.spkg




---

Comment by drkirkby created at 2010-01-12 03:13:53

Replace all things like $MKDIR with mkdir


---

Attachment

Note, $CP is purposely left as '$CP', since the GNU version of 'cp' have an extra option which can be useful.


---

Comment by drkirkby created at 2010-01-12 03:41:04

Changing status from new to needs_review.


---

Comment by jsp created at 2010-01-12 10:24:20

Changing status from needs_review to positive_review.


---

Comment by jsp created at 2010-01-12 10:24:20

The new spkg looks good. Checked on Fedora and Open Solaris.

Positive review.

Jaap


---

Comment by rlm created at 2010-01-14 02:50:33

Resolution: fixed


---

Comment by rlm created at 2010-01-14 06:35:28

Resolution changed from fixed to 


---

Comment by rlm created at 2010-01-14 06:35:28

Changing status from closed to new.


---

Comment by rlm created at 2010-01-14 06:36:28

Changing status from new to needs_work.


---

Comment by rlm created at 2010-01-14 06:36:28

Sage did not start after building this spkg on boxen:

```
rlmill`@`boxen:/scratch/rlm/sage-4.3.1.rc0/devel/sage-main$ ../../sage
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)
| Sage Version 4.3.1.alpha2, Release Date: 2010-01-13                |
| Type notebook() for the GUI, and license() for information.        |
/virtual/scratch/rlm/sage-4.3.1.rc0/local/lib/python2.6/site-packages/IPython/ipmaker.pyc
in force_import(modname)
    64         reload(sys.modules[modname])
    65     else:
---> 66         __import__(modname)
    67
    68

/virtual/scratch/rlm/sage-4.3.1.rc0/local/bin/ipy_profile_sage.py in <module>()
     5     preparser(True)
     6
----> 7     import sage.all_cmdline
     8     sage.all_cmdline._init_cmdline(globals())
     9

/virtual/scratch/rlm/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/all_cmdline.py
in <module>()
    12 try:
    13
---> 14     from sage.all import *
    15     from sage.calculus.predefined import x
    16     preparser(on=True)

/virtual/scratch/rlm/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/all.py
in <module>()
    70 get_sigs()
    71
---> 72 from sage.rings.all      import *
    73 from sage.matrix.all     import *
    74

/virtual/scratch/rlm/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/rings/all.py
in <module>()
    92
    93 # Algebraic numbers

---> 94 from qqbar import (AlgebraicRealField, is_AlgebraicRealField, AA,
    95                    AlgebraicReal, is_AlgebraicReal,
    96                    AlgebraicField, is_AlgebraicField, QQbar,

/virtual/scratch/rlm/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/rings/qqbar.py
in <module>()
  1414 QQy = QQ['y']
  1415 QQy_y = QQy.gen()
-> 1416 QQxy = QQ['x', 'y']
  1417 QQxy_x = QQxy.gen(0)
  1418 QQxy_y = QQxy.gen(1)

/virtual/scratch/rlm/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/rings/ring.so
in sage.rings.ring.Ring.__getitem__ (sage/rings/ring.c:2685)()

/virtual/scratch/rlm/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_ring_constructor.pyc
in PolynomialRing(base_ring, arg1, arg2, sparse, order, names, name,
implementation)
   353             names = arg1
   354             n = len(names)
--> 355             R = _multi_variate(base_ring, names, n, sparse, order)
   356
   357     if arg1 is None and arg2 is None:

/virtual/scratch/rlm/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_ring_constructor.pyc
in _multi_variate(base_ring, names, n, sparse, order)
   451         return R
   452
--> 453     from sage.rings.polynomial.multi_polynomial_libsingular
import MPolynomialRing_libsingular
   454     if m.integral_domain.is_IntegralDomain(base_ring):
   455         if n < 1:

/virtual/scratch/rlm/sage-4.3.1.rc0/local/bin/multi_polynomial_libsingular.pyx
in init sage.rings.polynomial.multi_polynomial_libsingular
(sage/rings/polynomial/multi_polynomial_libsingular.cpp:29460)()

/virtual/scratch/rlm/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/libs/singular/__init__.py
in <module>()
     6
     7 ## We predefine a couple of often used functions here to avoid
the fetch overhead ##

----> 8 groebner = singular_function('groebner')
     9
    10

/virtual/scratch/rlm/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/libs/singular/function.so
in sage.libs.singular.function.singular_function
(sage/libs/singular/function.cpp:11103)()

/virtual/scratch/rlm/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/libs/singular/function.so
in sage.libs.singular.function.SingularKernelFunction.__init__
(sage/libs/singular/function.cpp:10853)()

/virtual/scratch/rlm/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/libs/singular/function.so
in sage.libs.singular.function.SingularFunction.get_call_handler
(sage/libs/singular/function.cpp:9141)()

NotImplementedError:
Error importing ipy_profile_sage - perhaps you should run %upgrade?
WARNING: Loading of ipy_profile_sage failed.
```



---

Comment by drkirkby created at 2010-01-14 07:14:17

I'm totally baffled how on earth changing 

 * $CHMOD to 'chmod'
 * $RM to 'rm'
 * $LN to 'ln'

in singular's spkg-install file can break the singular package. All the variables were defined elsewhere (sage-env) to be just the command - no options were given. 

I can't help feel there must be some other explanation, but I'll certainly take a closer look at this. 

Dave


---

Comment by rlm created at 2010-01-16 01:01:01

This looks like the other errors we got from #7818. I'll give this one another try for rc0.


---

Comment by rlm created at 2010-01-16 02:29:09

Resolution: fixed
