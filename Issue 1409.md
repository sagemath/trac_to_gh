# Issue 1409: multi_polynomial_ideal.py segfaults on 2.8.15

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2007-12-06 06:26:54

Assignee: malb

It segfaults on the example from the Magma handbook.  Here is the backtrace:


```
#0  nSetChar (r=0x2ae10602f1f8) at numbers.cc:127
#1  0x00002ae105c740d3 in rChangeCurrRing (r=0xb5) at ring.cc:108
#2  0x00002ae105891ca9 in __pyx_tp_dealloc_4sage_5rings_10polynomial_28multi_polynomial_libsingular_MPolynomialRing_libsingular (o=0x2df7280)
    at sage/rings/polynomial/multi_polynomial_libsingular.cpp:3910
#3  0x00000000004b3e4f in collect (generation=<value optimized out>)
    at Modules/gcmodule.c:714
#4  0x00000000004b4575 in _PyObject_GC_New (tp=0x726dc0) at Modules/gcmodule.c:897
#5  0x00000000004358c0 in PyList_New (size=5) at Objects/listobject.c:103
#6  0x00002ae0f7454d1f in do_append (self=<value optimized out>, x=36)
    at /opt/sage/spkg/build/python-2.5.1.p9/src/Modules/cPickle.c:298
#7  0x00002ae0f745ce76 in load (self=0x29b5f68)
    at /opt/sage/spkg/build/python-2.5.1.p9/src/Modules/cPickle.c:4219
#8  0x000000000048733c in PyEval_EvalFrameEx (f=0x2ec59d0, throwflag=<value optimized out>)
    at Python/ceval.c:3548
#9  0x0000000000487b7e in PyEval_EvalFrameEx (f=0x2ec57f0, throwflag=<value optimized out>)
    at Python/ceval.c:3650
#10 0x0000000000487b7e in PyEval_EvalFrameEx (f=0x2ec55f0, throwflag=<value optimized out>)
    at Python/ceval.c:3650
#11 0x0000000000487b7e in PyEval_EvalFrameEx (f=0x2ec5400, throwflag=<value optimized out>)
    at Python/ceval.c:3650
...
```


This is on 64-bit Linux.  Here is gcc --version:

```
gcc (GCC) 4.1.3 20070929 (prerelease) (Ubuntu 4.1.2-16ubuntu2)
Copyright (C) 2006 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

```




---

Comment by mhansen created at 2007-12-06 07:06:56

This goes away for me after reverting #1257 .


---

Comment by was created at 2007-12-06 15:03:30

Hey, post the input that causes the problem.  What is "the example from the Magma handbook"?


---

Comment by mabshoff created at 2007-12-06 15:04:52


```
[07:19] <mabshoff> Which doctest in multi_polynomial_ideal.py fails? 
[07:19] <mhansen> Will do.  In that case, I'll add my patch for http://trac.sagemath.org/sage_trac/ticket/1406
[07:19] <mabshoff> ok, excellent
[07:20] <mhansen> It's the "example from the MAGMA Handbook" one.
[07:20] <mabshoff> ok
```


Cheers,

Michael


---

Comment by mhansen created at 2007-12-06 19:48:09

It fails on this: 


```
            sage: K.<w> = GF(27) # this example is from the MAGMA handbook
            sage: P.<x, y> = PolynomialRing(K, 2, order='lex')
            sage: I = Ideal([ x^8 + y + 2, y^6 + x*y^5 + x^2 ])
            sage: I = Ideal(I.groebner_basis()); I
            Ideal (y^48 + y^41 - y^40 + y^37 - y^36 - y^33 + y^32 - y^29 + y^28 -
            y^25 + y^24 + y^2 + y + 1, x - y^47 - y^45 + y^44 - y^43 + y^41 - y^39 -
            y^38 - y^37 - y^36 + y^35 - y^34 - y^33 + y^32 - y^31 + y^30 + y^28 +
            y^27 + y^26 + y^25 - y^23 + y^22 + y^21 - y^19 - y^18 - y^16 + y^15 +
            y^13 + y^12 - y^10 + y^9 + y^8 + y^7 - y^6 + y^4 + y^3 + y^2 + y - 1) of
            Multivariate Polynomial Ring in x, y over Finite Field in w of size 3^3
```

but only when I'm running the doctest.  It passes fine if you just enter it into the interpreter.


---

Comment by ncalexan created at 2008-01-19 22:16:12

Works for me, OS X 10.4, MacBook Pro Core2 Duo, sage-2.9.3.


---

Comment by AlexGhitza created at 2008-01-31 04:30:31

Works on sage-2.10, Gentoo Core2 Duo.


---

Comment by mabshoff created at 2008-02-15 23:16:12

Nobody has been able to reproduce this with any recent Sage release. 2.8.15 has been a while, so we can reopen if it pops up again.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-15 23:16:12

Resolution: fixed
