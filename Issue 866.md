# Issue 866: [with patch] big NTL patch

Issue created by migration from Trac.

Original creator: craigcitro

Original creation time: 2007-10-12 21:11:38

Assignee: craigcitro

Keywords: ntl

This is the big NTL patch that several people were working on during SD5. There's a ton of code in here, due to Joel Mohler, Craig Citro, Robert Bradshaw, David Harvey, and probably several more people I've forgotten. 


---

Comment by craigcitro created at 2007-10-12 21:11:57

Changing status from new to assigned.


---

Attachment


---

Comment by mabshoff created at 2007-10-13 01:27:03

Hello,

I ran Ifti's code with 3 iterations (see ticket #501) and there is a problem in __repr__:

```
==6721== 1,337,726 bytes in 97,087 blocks are definitely lost in loss record 2,181 of 2,187
==6721==    at 0x4A1BFE4: operator new[](unsigned long) (vg_replace_malloc.c:271)
==6721==    by 0x5FE0769: ZZ_pX_repr (in /tmp/Work-mabshoff/sage-2.8.6/devel/sage-main/c_lib/libcsage.so)
==6721==    by 0xCBE62C0: __pyx_f_9ntl_ZZ_pX_9ntl_ZZ_pX___repr__(_object*) (ntl_ZZ_pX.cpp:1020)
==6721==    by 0x443299: _PyObject_Str (object.c:406)
==6721==    by 0x44333A: PyObject_Str (object.c:426)
==6721==    by 0x44DC7F: string_new (stringobject.c:3892)
==6721==    by 0x459172: type_call (typeobject.c:422)
==6721==    by 0x415522: PyObject_Call (abstract.c:1860)
==6721==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)
==6721==    by 0xF1773F3: __pyx_f_25polynomial_modn_dense_ntl_22Polynomial_dense_mod_n_int_list(_object*, _object*) (polynom
ial_modn_dense_ntl.cpp:1831)
==6721==    by 0x415522: PyObject_Call (abstract.c:1860)
==6721==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)
```


Cheers,

Michael


---

Comment by mabshoff created at 2007-10-13 02:02:42

Hello,

__repr__ in ntl_ZZ_pX.pyx leaks. With the following (ugly) patch this problem is solved:

```
==7976== LEAK SUMMARY:
==7976==    definitely lost: 616 bytes in 50 blocks.
==7976==      possibly lost: 325,454 bytes in 776 blocks.
==7976==    still reachable: 36,843,962 bytes in 19,920 blocks.
==7976==         suppressed: 0 bytes in 0 blocks.
```

It was only one round instead of three, but the problem is gone.

Cheers,

Michael


---

Attachment

fiix the __repr__ leak


---

Comment by was created at 2007-10-13 07:34:00

Resolution: fixed
