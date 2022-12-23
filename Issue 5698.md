# Issue 5698: Sage 3.4.1.rc1: doctest failure in schemes/elliptic_curves/monsky_washnitzer.py

Issue created by migration from https://trac.sagemath.org/ticket/5698

Original creator: mabshoff

Original creation time: 2009-04-06 19:03:44

Assignee: mabshoff

The following happens all the sudden when updating FLINT:

```
sage -t -long "devel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py"
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.rc2/devel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py", line 1487:
    sage: B = A.change_ring(Integers(p**prec)); B               # long time
Expected:
    [74311982 57996908]
    [95877067 25828133]
Got:
    [54572546 87269244]
    [10839343 79974813]
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.rc2/devel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py", line 1490:
    sage: B.det()                                               # long time
Expected:
    10007
Got:
    29700776
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.rc2/devel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py", line 1492:
    sage: B.trace()                                             # long time
Expected:
    66
Got:
    34407310
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.rc2/devel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py", line 1562:
    sage: B.det()                                               # long time
Expected:
    11 + 484*t^2 + 451*t^3 + O(t^4)
Got:
    245 + 240*t + 724*t^2 + 808*t^3 + O(t^4)
**********************************************************************
```

But it is unclear if FLINT is the cause here. Downgrading FLINT makes it disappear, but the cause could be and likely is in some other patch. Note also the following issue valgrind found:

```
==30646== Conditional jump or move depends on uninitialised value(s)
==30646==    at 0x8F302EC: gdiv (in /scratch/mabshoff/sage-3.4.1.rc0/local/lib/libpari-gmp.so.2)
==30646==    by 0x828FAFE: QQ_to_t_FRAC (in /scratch/mabshoff/sage-3.4.1.rc0/devel/sage-main/c_lib/libcsage.so)
==30646==    by 0x22EB14E7: __pyx_f_4sage_6matrix_21matrix_rational_dense_pari_GEN (matrix_rational_dense.c:25089)
==30646==    by 0x22EE0D3C: __pyx_pf_4sage_6matrix_21matrix_rational_dense_21Matrix_rational_dense__invert_pari (matrix_rational_dense.c:24157)
==30646==    by 0x417E92: PyObject_Call (abstract.c:1861)
==30646==    by 0x22ED954D: __pyx_pf_4sage_6matrix_21matrix_rational_dense_21Matrix_rational_dense___invert__main (matrix_rational_dense.c:9542)
==30646==    by 0x417E92: PyObject_Call (abstract.c:1861)
==30646==    by 0x22EAF80A: __pyx_pf_4sage_6matrix_21matrix_rational_dense_21Matrix_rational_dense___invert__ (matrix_rational_dense.c:8933)
==30646==    by 0x216C1751: __pyx_pf_4sage_6matrix_7matrix0_6Matrix___invert__ (matrix0.c:22763)
==30646==    by 0xEDAA1DA: __pyx_f_4sage_9structure_7element_generic_power_c (element.c:23281)
==30646==    by 0xEDAC821: __pyx_pf_4sage_9structure_7element_11RingElement___pow__ (element.c:10954)
==30646==    by 0x457FBC: wrap_ternaryfunc (typeobject.c:3621)
==30646==    by 0x417E92: PyObject_Call (abstract.c:1861)
==30646==    by 0x4816E1: PyEval_CallObjectWithKeywords (ceval.c:3442)
==30646==    by 0x4D0F9D: wrapperdescr_call (descrobject.c:304)
==30646==    by 0x417E92: PyObject_Call (abstract.c:1861)
==30646==    by 0x216C13C0: __pyx_pf_4sage_6matrix_7matrix0_6Matrix___pow__ (matrix0.c:23157)
==30646==    by 0x418AC4: ternary_op (abstract.c:518)
==30646==    by 0x4850BD: PyEval_EvalFrameEx (ceval.c:1063)
==30646==    by 0x489A95: PyEval_EvalCodeEx (ceval.c:2836)
==30646==    by 0x4D40D7: function_call (funcobject.c:517)
==30646==    by 0x417E92: PyObject_Call (abstract.c:1861)
==30646==    by 0x41E6CE: instancemethod_call (classobject.c:2519)
==30646==    by 0x417E92: PyObject_Call (abstract.c:1861)
==30646==    by 0x45A257: slot_tp_init (typeobject.c:4943)
==30646== 
==30646== Conditional jump or move depends on uninitialised value(s)
==30646==    at 0x8F3004B: gdiv (in /scratch/mabshoff/sage-3.4.1.rc0/local/lib/libpari-gmp.so.2)
==30646==    by 0x8E67C57: gauss_intern (in /scratch/mabshoff/sage-3.4.1.rc0/local/lib/libpari-gmp.so.2)
==30646==    by 0x8E67F45: gauss (in /scratch/mabshoff/sage-3.4.1.rc0/local/lib/libpari-gmp.so.2)
==30646==    by 0x22EE0D9C: __pyx_pf_4sage_6matrix_21matrix_rational_dense_21Matrix_rational_dense__invert_pari (matrix_rational_dense.c:24218)
==30646==    by 0x417E92: PyObject_Call (abstract.c:1861)
==30646==    by 0x22ED954D: __pyx_pf_4sage_6matrix_21matrix_rational_dense_21Matrix_rational_dense___invert__main (matrix_rational_dense.c:9542)
==30646==    by 0x417E92: PyObject_Call (abstract.c:1861)
==30646==    by 0x22EAF80A: __pyx_pf_4sage_6matrix_21matrix_rational_dense_21Matrix_rational_dense___invert__ (matrix_rational_dense.c:8933)
==30646==    by 0x216C1751: __pyx_pf_4sage_6matrix_7matrix0_6Matrix___invert__ (matrix0.c:22763)
==30646==    by 0xEDAA1DA: __pyx_f_4sage_9structure_7element_generic_power_c (element.c:23281)
==30646==    by 0xEDAC821: __pyx_pf_4sage_9structure_7element_11RingElement___pow__ (element.c:10954)
==30646==    by 0x457FBC: wrap_ternaryfunc (typeobject.c:3621)
==30646==    by 0x417E92: PyObject_Call (abstract.c:1861)
==30646==    by 0x4816E1: PyEval_CallObjectWithKeywords (ceval.c:3442)
==30646==    by 0x4D0F9D: wrapperdescr_call (descrobject.c:304)
==30646==    by 0x417E92: PyObject_Call (abstract.c:1861)
==30646==    by 0x216C13C0: __pyx_pf_4sage_6matrix_7matrix0_6Matrix___pow__ (matrix0.c:23157)
==30646==    by 0x418AC4: ternary_op (abstract.c:518)
==30646==    by 0x4850BD: PyEval_EvalFrameEx (ceval.c:1063)
==30646==    by 0x489A95: PyEval_EvalCodeEx (ceval.c:2836)
==30646==    by 0x4D40D7: function_call (funcobject.c:517)
==30646==    by 0x417E92: PyObject_Call (abstract.c:1861)
==30646==    by 0x41E6CE: instancemethod_call (classobject.c:2519)
==30646==    by 0x417E92: PyObject_Call (abstract.c:1861)
==30646==    by 0x45A257: slot_tp_init (typeobject.c:4943)
```

This is likely caused by the Brandt module patch when William optimized the "small LA" cases.

Cheers,

Michael


---

Comment by was created at 2009-04-09 02:46:36

This is a bug in FLINT:

```
sage: R.<t> = Zmod(next_prime(8000^3))[]
sage: f = R.random_element(degree=3200)
sage: pari(f)*pari(f) == pari(f*f)
False
```


This happens for most numbers > 8000 above, but not for smaller numbers. If we downgrade to the previous FLINT, the problem goes away. 

This is an "aliasing problem". 


```
wstein@sage:/scratch/mabshoff/sage-3.4.1.rc1$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: R.<t> = Zmod(next_prime(8000^3))[]
sage: f = R.random_element(degree=3200)
sage: pari(f)*pari(f) == pari(f*f)
| Sage Version 3.4.1.rc1, Release Date: 2009-04-05                   |
| Type notebook() for the GUI, and license() for information.        |
sage: sage: R.<t> = Zmod(next_prime(8000^3))[]
sage: sage: f = R.random_element(degree=3200)
sage: sage: pari(f)*pari(f) == pari(f*f)
False
sage: 
sage: g = f+1
sage: pari(f)*pari(g) == pari(f*g)
True
sage: g = f+2
sage: pari(f)*pari(g) == pari(f*g)
True
sage: pari(f)*pari(g-2) == pari(f*(g-2))
True
sage: pari(f)*pari(f) == pari(f*f)
False
sage: pari(f)*pari(f+1-1) == pari(f*(f+1-1))
True
```


Turning off using David Harvey's znpoly fixes this problem.  The spkg up here turns off znpoly.  With this the whole test suite passes fine:

http://sage.math.washington.edu/home/wstein/patches/flint-1.2.4.p1.spkg


---

Comment by mabshoff created at 2009-04-09 05:36:43

After turning on the test suite again I did doctest this on all of SkyNet and monsky now passes. Positive review. The valgrind issue should be moved to its own followup ticket.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-09 05:51:40

Resolution: fixed


---

Comment by mabshoff created at 2009-04-09 05:51:40

Merged in Sage 3.4.1.rc2.

Cheers,

Michael


---

Comment by dmharvey created at 2009-04-12 12:35:05

For the record, I believe this is due to a bug in `zn_poly` 0.8 which was fixed in `zn_poly` 0.9 (released about 6 months ago). FLINT still includes `zn_poly` 0.8. If FLINT upgrades to 0.9, I expect this problem will go away.
