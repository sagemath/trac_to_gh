# Issue 1884: memory leak in real numbers

Issue created by migration from https://trac.sagemath.org/ticket/1884

Original creator: dmharvey

Original creation time: 2008-01-22 02:53:16

Assignee: mabshoff

This leaks like a sieve in 2.10:


```
t = 0.0
while True:
    t = t * 2.0
```




---

Comment by mabshoff created at 2008-01-22 03:25:31

I ran 10000 loops with 2.9.3 and I got:

```
==5050== 2,807,000 bytes in 10,025 blocks are still reachable in loss record 8,029 of 8,033
==5050==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)
==5050==    by 0x4B0079: _PyObject_GC_Malloc (gcmodule.c:1321)
==5050==    by 0x4B01AC: _PyObject_GC_New (gcmodule.c:1343)
==5050==    by 0x441339: PyDict_New (dictobject.c:216)
==5050==    by 0x964A11F: __pyx_pf_4sage_9structure_6parent_6Parent___init__ (parent.c:404)
==5050==    by 0x453A9B: wrap_init (typeobject.c:3962)
==5050==    by 0x415542: PyObject_Call (abstract.c:1860)
==5050==    by 0x47C480: PyEval_CallObjectWithKeywords (ceval.c:3433)
==5050==    by 0x4CAF84: wrapperdescr_call (descrobject.c:304)
==5050==    by 0x415542: PyObject_Call (abstract.c:1860)
==5050==    by 0x47C480: PyEval_CallObjectWithKeywords (ceval.c:3433)
==5050==    by 0x9537A94: __pyx_pf_4sage_9structure_11parent_base_14ParentWithBase___init__ (parent_base.c:388)
==5050==
==5050== 2,807,560 bytes in 10,027 blocks are still reachable in loss record 8,030 of 8,033
==5050==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)
==5050==    by 0x4B0079: _PyObject_GC_Malloc (gcmodule.c:1321)
==5050==    by 0x4B01AC: _PyObject_GC_New (gcmodule.c:1343)
==5050==    by 0x441339: PyDict_New (dictobject.c:216)
==5050==    by 0x964A873: __pyx_pf_4sage_9structure_6parent_6Parent___init__ (parent.c:553)
==5050==    by 0x453A9B: wrap_init (typeobject.c:3962)
==5050==    by 0x415542: PyObject_Call (abstract.c:1860)
==5050==    by 0x47C480: PyEval_CallObjectWithKeywords (ceval.c:3433)
==5050==    by 0x4CAF84: wrapperdescr_call (descrobject.c:304)
==5050==    by 0x415542: PyObject_Call (abstract.c:1860)
==5050==    by 0x47C480: PyEval_CallObjectWithKeywords (ceval.c:3433)
==5050==    by 0x9537A94: __pyx_pf_4sage_9structure_11parent_base_14ParentWithBase___init__ (parent_base.c:388)
==5050==
==5050==
==5050== 2,812,600 bytes in 10,045 blocks are still reachable in loss record 8,031 of 8,033
==5050==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)
==5050==    by 0x4B0079: _PyObject_GC_Malloc (gcmodule.c:1321)
==5050==    by 0x4B01AC: _PyObject_GC_New (gcmodule.c:1343)
==5050==    by 0x441339: PyDict_New (dictobject.c:216)
==5050==    by 0x98C03B6: __pyx_pf_4sage_9structure_11parent_gens_14ParentWithGens___init__ (parent_gens.c:1552)
==5050==    by 0x453A9B: wrap_init (typeobject.c:3962)
==5050==    by 0x415542: PyObject_Call (abstract.c:1860)
==5050==    by 0x47C480: PyEval_CallObjectWithKeywords (ceval.c:3433)
==5050==    by 0x4CAF84: wrapperdescr_call (descrobject.c:304)
==5050==    by 0x415542: PyObject_Call (abstract.c:1860)
==5050==    by 0x47C480: PyEval_CallObjectWithKeywords (ceval.c:3433)
==5050==    by 0xBD5AF19: __pyx_pf_4sage_5rings_9real_mpfr_9RealField___init__ (real_mpfr.c:2798)
```


I am running the same code under omega now, but that might take an hour or two.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-22 03:29:28

Hmm, this might be the real culprit:

```
==5050== 800,000 bytes in 10,000 blocks are still reachable in loss record 8,010 of 8,033
==5050==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)
==5050==    by 0x4B0079: _PyObject_GC_Malloc (gcmodule.c:1321)
==5050==    by 0x454C29: PyType_GenericAlloc (typeobject.c:454)
==5050==    by 0x9762350: __pyx_tp_new_4sage_9structure_7element_Element (element.c:22358)
==5050==    by 0x9D27AF0: __pyx_tp_new_4sage_10categories_8morphism_Morphism (morphism.c:4733)
==5050==    by 0x9D27F30: __pyx_tp_new_4sage_10categories_8morphism_CallMorphism (morphism.c:5232)
==5050==    by 0x458D92: type_call (typeobject.c:422)
==5050==    by 0x415542: PyObject_Call (abstract.c:1860)
==5050==    by 0x47C480: PyEval_CallObjectWithKeywords (ceval.c:3433)
==5050==    by 0x9647DE9: __pyx_f_4sage_9structure_6parent_6Parent_coerce_map_from_c (parent.c:1015)
==5050==    by 0x99E25B4: __pyx_f_4sage_9structure_6coerce_24CoercionModel_cache_maps_discover_coercion_c (coerce.c:7583)
==5050==    by 0x99DBBD5: __pyx_f_4sage_9structure_6coerce_24CoercionModel_cache_maps_coercion_maps_c (coerce.c:7350)
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-01-23 09:27:37

Changing priority from major to blocker.


---

Comment by robertwb created at 2008-01-23 18:19:53

I'll try to look into this today. Is the above from omega, or if not what did that tell you?


---

Comment by mabshoff created at 2008-01-23 21:27:57

Hi Robert,

the above is from memcheck. I hadn't had time to try the same under omega, but since the above is "still reachable" memory omega wouldn't help in that case anyway since it only prints out messages about "definitely lost" memory. There were a variety of places in the code where about 10.000 buffers were lost, some of which are on the first comment. Only later I did discover that there was one buffer with the exact number of 10,000 losses, so it became my prime candidate. The complere log (6.8MB) is at 

http://sage.math.washington.edu/home/mabshoff/sage-memcheck-1884.log

I should be in IRC if you want to discuss this issue or any input from my end. Note that the memcheck log was created with 2.9.3, so in 2.10 the number might be off.

Cheers,

Michael


---

Comment by robertwb created at 2008-01-29 19:44:33

Changing status from new to assigned.


---

Comment by robertwb created at 2008-01-29 19:44:33

Changing assignee from mabshoff to robertwb.


---

Comment by robertwb created at 2008-01-29 19:44:33

This is due to non-uniqueness of real fields. 


```
sage: parent(2.0) == parent(2.0)
True
sage: parent(2.0) is parent(2.0)
False
```


It's making a new parent for the constant in the loop, and adding it to the coercion model. I will fix this now.


---

Attachment


---

Attachment


---

Comment by robertwb created at 2008-01-29 20:54:34

The first patch fixes the issue (with a doctest), and the second ensures uniqueness in a couple of places that imported RealField directly.


---

Comment by mabshoff created at 2008-01-30 04:25:53

Ok, after applying both patches I get 

```
Exiting SAGE (CPU time 0m0.00s, Wall time 0m1.00s).
*** glibc detected *** double free or corruption (out): 0x0000000000ec69a0 ***
```

on exit each time I start Sage. The valgrind log points to #1337.

Cheers,

Michael


---

Comment by robertwb created at 2008-01-30 06:05:10

I have no idea--this must be exposing some previously undetected bug. I don't allocate or free anything here, in fact most of the patch is Python code...


---

Comment by mabshoff created at 2008-01-30 06:08:50

Replying to [comment:10 robertwb]:
> I have no idea--this must be exposing some previously undetected bug. I don't allocate or free anything here, in fact most of the patch is Python code...

I agree that the bug is not in your patches, but it is exposed by the code. I have attempted to track this issue, i.e. #1337 before, but failed. Maybe we can sit down at SD7 and see if we can come up with a solution.

Cheers,

Michael


---

Comment by robertwb created at 2008-01-30 09:32:07

It's certainly an elusive bug. OK, I'll spend some time on it with you at SD7.


---

Comment by mabshoff created at 2008-03-09 05:08:52

Resolution: fixed


---

Comment by mabshoff created at 2008-03-09 05:08:52

Merged both patches in Sage 2.10.3.rc3
