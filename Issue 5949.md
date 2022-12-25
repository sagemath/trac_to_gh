# Issue 5949: memory leak expose by elliptic curve code

archive/issues_005949.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @robertwb @malb jpflori\n\nThe following code consumes inordinate amounts of memory while Magma can do it with 14 MB :)\n\n```\np=30\n\n def FindGroupOrder(p,s):\n   K = GF(p)\n   v = K(4*s)\n   u = K(s**2-5)\n   x = u**3\n   b = 4*x*v\n   a = (v-u)**3*(3*u+v)\n   A = a/b-2\n   x = x/v**3\n   b = x**3 + A*x**2 + x\n   E = EllipticCurve(K,[0,b*A,0,b**2,0])\n   return factor(E.cardinality())\n\nwhile p<134217689:\n        p=next_prime(p)\n        g=FindGroupOrder(p,11)\n        print g \n```\n\n\nValgrind pretty much points at libSingular (This was for running up to 2^12 or so):\n\n```\n==26879== 2,109,920 bytes in 469 blocks are possibly lost in loss record 14,860 of 14,862\n==26879==    at 0x4C22FEB: malloc (vg_replace_malloc.c:207)\n==26879==    by 0x1F1D0B3F: omAllocFromSystem (omAllocSystem.c:186)\n==26879==    by 0x1F1D0CC1: omAllocLarge (omAllocSystem.c:41)\n==26879==    by 0x1F0A0C2A: npInitChar(int, sip_sring*) (omalloc.h:2354)\n==26879==    by 0x1F0B817A: nInitChar(sip_sring*) (numbers.cc:506)\n==26879==    by 0x1F0C7197: rComplete(sip_sring*, int) (ring.cc:2922)\n==26879==    by 0x1ECBD1C7: __pyx_pf_4sage_5rings_10polynomial_28multi_polynomial_libsingular_27MPolynomialRing_libsingular___init__(_object*, _object*, _object*) (multi_polynomial_libsingular.cpp:4995)\n==26879==    by 0x45C040: type_call (typeobject.c:436)\n==26879==    by 0x417E92: PyObject_Call (abstract.c:1861)\n==26879==    by 0x485809: PyEval_EvalFrameEx (ceval.c:3784)\n==26879==    by 0x488296: PyEval_EvalFrameEx (ceval.c:3659)\n==26879==    by 0x489A95: PyEval_EvalCodeEx (ceval.c:2836)\n==26879==    by 0x487704: PyEval_EvalFrameEx (ceval.c:3669)\n==26879==    by 0x488296: PyEval_EvalFrameEx (ceval.c:3659)\n==26879==    by 0x489A95: PyEval_EvalCodeEx (ceval.c:2836)\n==26879==    by 0x4D40D7: function_call (funcobject.c:517)\n==26879==    by 0x417E92: PyObject_Call (abstract.c:1861)\n==26879==    by 0x41E6CE: instancemethod_call (classobject.c:2519)\n==26879==    by 0x417E92: PyObject_Call (abstract.c:1861)\n==26879==    by 0x485809: PyEval_EvalFrameEx (ceval.c:3784)\n==26879==    by 0x489A95: PyEval_EvalCodeEx (ceval.c:2836)\n==26879==    by 0x4D40D7: function_call (funcobject.c:517)\n==26879==    by 0x417E92: PyObject_Call (abstract.c:1861)\n==26879==    by 0x41E6CE: instancemethod_call (classobject.c:2519)\n==26879==    by 0x417E92: PyObject_Call (abstract.c:1861)\n```\n\nThe above leak gets larger and larger depending on how I pick the upper bound. \n\nThis translates to rings/polynomial/multi_polynomial_libsingular.pyx +359, more specifically the rComplete() line in \n\n```\n        self._ring.order[nblcks] = ringorder_C\n\n        rComplete(self._ring, 1)\n        self._ring.ShortOut = 0\n```\n\nFrom src/kernel/ring.h:\n\n```\n// this needs to be called whenever a new ring is created: new fields\n// in ring are created (like VarOffset), unless they already exist\n// with force == 1, new fields are _always_ created (overwritten),\n// even if they exist\nBOOLEAN rComplete(ring r, int force = 0); \n```\n\nChanging rComplete() to use 0 instead of 1 does not fix the problem.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5949\n\n",
    "created_at": "2009-04-30T21:45:51Z",
    "labels": [
        "component: memleak",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "memory leak expose by elliptic curve code",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5949",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

CC:  @robertwb @malb jpflori

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

Issue created by migration from https://trac.sagemath.org/ticket/5949





---

archive/issue_comments_046977.json:
```json
{
    "body": "See also the discussion thread at http://groups.google.com/group/sage-support/t/ef01dae47c835137 .",
    "created_at": "2009-05-03T01:01:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5949#issuecomment-46977",
    "user": "https://github.com/aghitza"
}
```

See also the discussion thread at http://groups.google.com/group/sage-support/t/ef01dae47c835137 .



---

archive/issue_comments_046978.json:
```json
{
    "body": "If we've released for 2 months without fixing this, it doesn't make sense to keep it as a blocker. Note that the lisp interface is in fact 100% completely broken right now.",
    "created_at": "2009-06-15T23:29:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5949#issuecomment-46978",
    "user": "https://github.com/williamstein"
}
```

If we've released for 2 months without fixing this, it doesn't make sense to keep it as a blocker. Note that the lisp interface is in fact 100% completely broken right now.



---

archive/issue_comments_046979.json:
```json
{
    "body": "Changing priority from blocker to critical.",
    "created_at": "2009-06-15T23:29:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5949#issuecomment-46979",
    "user": "https://github.com/williamstein"
}
```

Changing priority from blocker to critical.



---

archive/issue_comments_046980.json:
```json
{
    "body": "Confirmed on sage-4.6.1.alpha1",
    "created_at": "2010-11-13T13:47:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5949#issuecomment-46980",
    "user": "https://github.com/jdemeyer"
}
```

Confirmed on sage-4.6.1.alpha1



---

archive/issue_comments_046981.json:
```json
{
    "body": "Just to confirm it is not an upstream bug:\n\n\n```c\nwhile (1) { def p = prime(random(2,2^30)); ring r = p,(x,y),dp; };\n```\n\n\ndoes not seem to leak memory as we do.",
    "created_at": "2011-06-22T16:33:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5949#issuecomment-46981",
    "user": "https://github.com/malb"
}
```

Just to confirm it is not an upstream bug:


```c
while (1) { def p = prime(random(2,2^30)); ring r = p,(x,y),dp; };
```


does not seem to leak memory as we do.



---

archive/issue_comments_046982.json:
```json
{
    "body": "I guess one of the problems here is that polynomial rings are cached.\n\nSee #5970\n\nThere is however memleaks involved.",
    "created_at": "2011-06-22T18:42:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5949#issuecomment-46982",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

I guess one of the problems here is that polynomial rings are cached.

See #5970

There is however memleaks involved.



---

archive/issue_events_013938.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5949",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5949#event-13938"
}
```



---

archive/issue_events_013939.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5949",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5949#event-13939"
}
```



---

archive/issue_events_013940.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5949",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5949#event-13940"
}
```



---

archive/issue_events_013941.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5949",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5949#event-13941"
}
```



---

archive/issue_events_013942.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5949",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5949#event-13942"
}
```



---

archive/issue_events_013943.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5949",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5949#event-13943"
}
```



---

archive/issue_events_013944.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5949",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5949#event-13944"
}
```
