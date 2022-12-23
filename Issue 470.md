# Issue 470: libpari doesn't deallocate its 100,000,000 byte stack

Issue created by migration from https://trac.sagemath.org/ticket/470

Original creator: mabshoff

Original creation time: 2007-08-20 22:40:29

Assignee: was

Keywords: memory

Valgrinding Sage 2.8.2rc1 tells me:


```
==2609== 100,000,000 bytes in 1 blocks are still reachable in loss record 6,989 of 6,989
==2609==    at 0x4A05809: malloc (vg_replace_malloc.c:149)
==2609==    by 0xFEE00BA: __pyx_f_3gen_init_stack (gen.c:25497)
==2609==    by 0xFF0744D: __pyx_f_3gen_12PariInstance___init__ (gen.c:21006)
==2609==    by 0x459FB1: type_call (typeobject.c:436)
==2609==    by 0x4156B2: PyObject_Call (abstract.c:1860)
==2609==    by 0x47D801: PyEval_CallObjectWithKeywords (ceval.c:3433)
==2609==    by 0xFF096E8: initgen (gen.c:27669)
==2609==    by 0x49F3F2: _PyImport_LoadDynamicModule (importdl.c:53)
==2609==    by 0x49D2CE: import_submodule (import.c:2394)
==2609==    by 0x49D7A1: load_next (import.c:2214)
==2609==    by 0x49D9FE: import_module_level (import.c:2002)
==2609==    by 0x49DE34: PyImport_ImportModuleLevel (import.c:2066)
```


An empty start up & quit immediately Sage session under valgrind shows about 130 MB of memory still reachable at exit. The vast amount of that is the libpari stack.

William stated that this is non-trivial to fix and will probably require changes in libpari itself. 

I would like to state that any application that needs that much stack space should be considered "broken by design". 

Cheers,

Michael


---

Comment by mabshoff created at 2007-09-20 20:30:24

Ok, after looking at init_stack in the pari source code it might be as simple as doing a 

```
sage_free((void*)Bot)
```

upon exiting Sage. I haven't tried it, though.

Cheers,

Michael


---

Comment by tornaria created at 2007-09-21 02:05:01

Check out:

http://pari.math.u-bordeaux.fr/archives/pari-dev-0511/msg00037.html

and maybe (older and possibly obsoleted by the above)

http://pari.math.u-bordeaux.fr/archives/pari-users-0301/msg00021.html

Also the pari manual discusses initialization/deinitialization in section 5.1.

In principle,

```
pari_close()
```

should be enough to free everything.


---

Comment by mabshoff created at 2007-10-12 01:56:53

Resolution: fixed


---

Comment by mabshoff created at 2007-10-12 01:56:53

This was fixes by William and Gonzalo during the rewrite of the pari stack extension code.

Cheers,

Michael


---

Comment by mabshoff created at 2007-10-13 20:09:47

Resolution changed from fixed to 


---

Comment by mabshoff created at 2007-10-13 20:09:47

Changing status from closed to reopened.


---

Comment by mabshoff created at 2007-10-13 20:10:19

As it turned out the problem is still there with 2.8.7.alpha0:

```
==22424== 8,000,000 bytes in 1 blocks are still reachable in loss record 2,941 of 2,941
==22424==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)
==22424==    by 0xAC6CB91: __pyx_f_3gen_init_stack (gen.c:26102)
==22424==    by 0xAC94BA5: __pyx_f_py_3gen_12PariInstance___init__ (gen.c:21449)
==22424==    by 0x459220: type_call (typeobject.c:436)
==22424==    by 0x415522: PyObject_Call (abstract.c:1860)
==22424==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)
==22424==    by 0xAC973BA: initgen (gen.c:29113)
==22424==    by 0x49E54D: _PyImport_LoadDynamicModule (importdl.c:53)
==22424==    by 0x49C45D: import_submodule (import.c:2394)
==22424==    by 0x49C920: load_next (import.c:2214)
==22424==    by 0x49CB7D: import_module_level (import.c:2002)
==22424==    by 0x49CFC4: PyImport_ImportModuleLevel (import.c:2066)
```


Cheers,

Michael


---

Comment by mabshoff created at 2007-10-14 11:54:21

Resolution: fixed


---

Comment by mabshoff created at 2007-10-14 11:54:21

Well, there are some cases where the dealloc doesn't work, so close this for now and open a ticket when I find a reproducible case where it does happen.

Cheers,

Michael
