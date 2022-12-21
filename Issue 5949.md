# Issue 5949: memory leak expose by elliptic curve code

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-04-30 21:45:51

Assignee: mabshoff

CC:  robertwb malb jpflori

The following code consumes inordinate amounts of memory while Magma can do it with 14 MB :)

```
p=30

 def FindGroupOrder(p,s):
   K = GF(p)
   v = K(4*s)
   u = K(s**2-5)
   x = u**3
   b = 4*x*v
   a = (v-u)**3*(3*u+v)
   A = a/b-2
   x = x/v**3
   b = x**3 + A*x**2 + x
   E = EllipticCurve(K,[0,b*A,0,b**2,0])
   return factor(E.cardinality())

while p<134217689:
        p=next_prime(p)
        g=FindGroupOrder(p,11)
        print g 
```


Valgrind pretty much points at libSingular (This was for running up to 2^12 or so):

```
==26879== 2,109,920 bytes in 469 blocks are possibly lost in loss record 14,860 of 14,862
==26879==    at 0x4C22FEB: malloc (vg_replace_malloc.c:207)
==26879==    by 0x1F1D0B3F: omAllocFromSystem (omAllocSystem.c:186)
==26879==    by 0x1F1D0CC1: omAllocLarge (omAllocSystem.c:41)
==26879==    by 0x1F0A0C2A: npInitChar(int, sip_sring*) (omalloc.h:2354)
==26879==    by 0x1F0B817A: nInitChar(sip_sring*) (numbers.cc:506)
==26879==    by 0x1F0C7197: rComplete(sip_sring*, int) (ring.cc:2922)
==26879==    by 0x1ECBD1C7: __pyx_pf_4sage_5rings_10polynomial_28multi_polynomial_libsingular_27MPolynomialRing_libsingular___init__(_object*, _object*, _object*) (multi_polynomial_libsingular.cpp:4995)
==26879==    by 0x45C040: type_call (typeobject.c:436)
==26879==    by 0x417E92: PyObject_Call (abstract.c:1861)
==26879==    by 0x485809: PyEval_EvalFrameEx (ceval.c:3784)
==26879==    by 0x488296: PyEval_EvalFrameEx (ceval.c:3659)
==26879==    by 0x489A95: PyEval_EvalCodeEx (ceval.c:2836)
==26879==    by 0x487704: PyEval_EvalFrameEx (ceval.c:3669)
==26879==    by 0x488296: PyEval_EvalFrameEx (ceval.c:3659)
==26879==    by 0x489A95: PyEval_EvalCodeEx (ceval.c:2836)
==26879==    by 0x4D40D7: function_call (funcobject.c:517)
==26879==    by 0x417E92: PyObject_Call (abstract.c:1861)
==26879==    by 0x41E6CE: instancemethod_call (classobject.c:2519)
==26879==    by 0x417E92: PyObject_Call (abstract.c:1861)
==26879==    by 0x485809: PyEval_EvalFrameEx (ceval.c:3784)
==26879==    by 0x489A95: PyEval_EvalCodeEx (ceval.c:2836)
==26879==    by 0x4D40D7: function_call (funcobject.c:517)
==26879==    by 0x417E92: PyObject_Call (abstract.c:1861)
==26879==    by 0x41E6CE: instancemethod_call (classobject.c:2519)
==26879==    by 0x417E92: PyObject_Call (abstract.c:1861)
```

The above leak gets larger and larger depending on how I pick the upper bound. 

This translates to rings/polynomial/multi_polynomial_libsingular.pyx +359, more specifically the rComplete() line in 

```
        self._ring.order[nblcks] = ringorder_C

        rComplete(self._ring, 1)
        self._ring.ShortOut = 0
```

From src/kernel/ring.h:

```
// this needs to be called whenever a new ring is created: new fields
// in ring are created (like VarOffset), unless they already exist
// with force == 1, new fields are _always_ created (overwritten),
// even if they exist
BOOLEAN rComplete(ring r, int force = 0); 
```

Changing rComplete() to use 0 instead of 1 does not fix the problem.

Cheers,

Michael


---

Comment by AlexGhitza created at 2009-05-03 01:01:20

See also the discussion thread at http://groups.google.com/group/sage-support/t/ef01dae47c835137 .


---

Comment by was created at 2009-06-15 23:29:03

If we've released for 2 months without fixing this, it doesn't make sense to keep it as a blocker. Note that the lisp interface is in fact 100% completely broken right now.


---

Comment by was created at 2009-06-15 23:29:03

Changing priority from blocker to critical.


---

Comment by jdemeyer created at 2010-11-13 13:47:18

Changing priority from critical to major.


---

Comment by jdemeyer created at 2010-11-13 13:47:18

Confirmed on sage-4.6.1.alpha1


---

Comment by malb created at 2011-06-22 16:33:15

Just to confirm it is not an upstream bug:


```c
while (1) { def p = prime(random(2,2^30)); ring r = p,(x,y),dp; };
```


does not seem to leak memory as we do.


---

Comment by jpflori created at 2011-06-22 18:42:03

I guess one of the problems here is that polynomial rings are cached.

See #5970

There is however memleaks involved.
