# Issue 3875: matrix/matrix_cyclo_dense.pyx segfault

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-08-15 17:38:27

Assignee: mabshoff


```
jec`@`host-57-29%./sage -t  devel/sage/sage/matrix/matrix_cyclo_dense.pyx 
sage -t  devel/sage/sage/matrix/matrix_cyclo_dense.pyx      sh: line 
1: 16845 Segmentation fault 
/home/jec/sage-3.1.rc0/local/bin/python 
/home/jec/sage-3.1.rc0/tmp/.doctest_matrix_cyclo_dense.py 
>/tmp/tmp8q1GmM 2>/tmp/tmpHrJVlH 

A mysterious error (perphaps a memory error?) occurred, which may have 
crashed doctest. 
         [6.5 s] 
exit code: 768 
```



---

Comment by mabshoff created at 2008-08-15 17:38:37

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-08-16 19:16:33

Valgrind says:

```
Trying:
    A###line 170:_sage_    >>> A
Expecting:
    [         109308420 -a^3 - a^2 - a - 1             -a + 1]
    [                 a             -2/3*a -a^3 - a^2 - a - 1]
ok
Trying:
    set_random_seed(0L)
Expecting nothing
ok
Trying:
    W = CyclotomicField(Integer(3),names=('z',)); (z,) = W._first_ngens(Integer(1))###line 1182:_sage_    >>> W.<z> = CyclotomicField(3)
Expecting nothing
ok
Trying:
    A = matrix(W, Integer(2), Integer(3), [Integer(1)+z, Integer(2)/Integer(3), Integer(9)*z+Integer(7), -Integer(3) + Integer(4)*z, z, -Integer(7)*z]); A###line 1183:_sage_    >>> A = matrix(W, 2, 3, [1+z, 2/3, 9*z+7, -3 + 4*z, z, -7*z]); A
Expecting:
    [  z + 1     2/3 9*z + 7]
    [4*z - 3       z    -7*z]
ok
Trying:
    A._echelon_form_multimodular(Integer(10))###line 1186:_sage_    >>> A._echelon_form_multimodular(10)
Expecting:
    [                  1                   0  -192/97*z - 361/97]
    [                  0                   1 1851/97*z + 1272/97]
ok
Trying:
    A = matrix(CyclotomicField(Integer(5)),Integer(0)); A###line 1192:_sage_    >>> A = matrix(CyclotomicField(5),0); A
Expecting:
    []
ok
Trying:
    A._echelon_form_multimodular(Integer(10))###line 1194:_sage_    >>> A._echelon_form_multimodular(10)
Expecting:
    []
==13670== Invalid write of size 8
==13670==    at 0x15C19790: __pyx_pf_4sage_6matrix_17matrix_modn_dense_17Matrix_modn_dense___init__ (matrix_modn_dense.c:3084)
==13670==    by 0x459350: type_call (typeobject.c:436)
==13670==    by 0x415832: PyObject_Call (abstract.c:1861)
==13670==    by 0x482DB9: PyEval_EvalFrameEx (ceval.c:3784)
==13670==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==13670==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==13670==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==13670==    by 0x4CF3F7: function_call (funcobject.c:517)
==13670==    by 0x415832: PyObject_Call (abstract.c:1861)
==13670==    by 0x41BF6C: instancemethod_call (classobject.c:2519)
==13670==    by 0x415832: PyObject_Call (abstract.c:1861)
==13670==    by 0x4569A8: slot_tp_call (typeobject.c:4714)
==13670==  Address 0x9ad7938 is 0 bytes after a block of size 0 alloc'd
==13670==    at 0x4A1BDEB: malloc (vg_replace_malloc.c:207)
==13670==    by 0x15C157E7: __pyx_pf_4sage_6matrix_17matrix_modn_dense_17Matrix_modn_dense___new__ (matrix_modn_dense.c:2693)
==13670==    by 0x15C15F56: __pyx_tp_new_4sage_6matrix_17matrix_modn_dense_Matrix_modn_dense (matrix_modn_dense.c:11163)
==13670==    by 0x4592A2: type_call (typeobject.c:422)
==13670==    by 0x415832: PyObject_Call (abstract.c:1861)
==13670==    by 0x482DB9: PyEval_EvalFrameEx (ceval.c:3784)
==13670==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==13670==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==13670==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==13670==    by 0x4CF3F7: function_call (funcobject.c:517)
==13670==    by 0x415832: PyObject_Call (abstract.c:1861)
==13670==    by 0x41BF6C: instancemethod_call (classobject.c:2519)
```

Poking around ....

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-16 20:24:14

Here is the real cuplrit:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: A = matrix(CyclotomicField(5),0); A
[]
sage: A._echelon_form_multimodular(10)
==14830== Invalid write of size 8
==14830==    at 0x15C19790: __pyx_pf_4sage_6matrix_17matrix_modn_dense_17Matrix_modn_dense___init__ (matrix_modn_dense.c:3084)
==14830==    by 0x459350: type_call (typeobject.c:436)
==14830==    by 0x415832: PyObject_Call (abstract.c:1861)   
==14830==    by 0x482DB9: PyEval_EvalFrameEx (ceval.c:3784) 
==14830==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)  
==14830==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669) 
==14830==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)  
==14830==    by 0x4CF3F7: function_call (funcobject.c:517)  
==14830==    by 0x415832: PyObject_Call (abstract.c:1861)   
==14830==    by 0x41BF6C: instancemethod_call (classobject.c:2519)
==14830==    by 0x415832: PyObject_Call (abstract.c:1861)   
==14830==    by 0x4569A8: slot_tp_call (typeobject.c:4714)  
==14830==  Address 0x123a85d8 is 0 bytes after a block of size 0 alloc'd
==14830==    at 0x4A1BDEB: malloc (vg_replace_malloc.c:207) 
==14830==    by 0x15C157E7: __pyx_pf_4sage_6matrix_17matrix_modn_dense_17Matrix_modn_dense___new__ (matrix_modn_dense.c:2693)
==14830==    by 0x15C15F56: __pyx_tp_new_4sage_6matrix_17matrix_modn_dense_Matrix_modn_dense (matrix_modn_dense.c:11163)
==14830==    by 0x4592A2: type_call (typeobject.c:422)
==14830==    by 0x415832: PyObject_Call (abstract.c:1861)   
==14830==    by 0x482DB9: PyEval_EvalFrameEx (ceval.c:3784) 
==14830==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)  
==14830==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669) 
==14830==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)  
==14830==    by 0x4CF3F7: function_call (funcobject.c:517)  
==14830==    by 0x415832: PyObject_Call (abstract.c:1861)   
==14830==    by 0x41BF6C: instancemethod_call (classobject.c:2519)
[]
sage: 
```

| SAGE Version 3.1.rc0, Release Date: 2008-08-15                     |
| Type notebook() for the GUI, and license() for information.        |
Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2008-08-16 20:46:10

Patch looks good to me. With the patch applied:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: A = matrix(CyclotomicField(5),0); A
| SAGE Version 3.1.rc0, Release Date: 2008-08-15                     |
| Type notebook() for the GUI, and license() for information.        |
[]
sage: 
sage: A._echelon_form_multimodular(10)
[]
sage: 
Exiting SAGE (CPU time 0m6.86s, Wall time 0m20.69s).
==16630== 
==16630== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 566 from 2)
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-08-16 21:49:17

Merged in Sage 3.1.final


---

Comment by mabshoff created at 2008-08-16 21:49:17

Resolution: fixed
