# Issue 6163: pynac -- segfault probably caused by cmp somehow and using intervals

Issue created by migration from https://trac.sagemath.org/ticket/6163

Original creator: was

Original creation time: 2009-05-31 02:01:25

Assignee: burcin

CC:  cwitty mhansen robertwb

This segfaults Sage-4.0:

```
sage: theta1,theta2=var('theta1,theta2'); theta1.subs(theta1=1,theta2=0)
```



```
wstein@sage:~/build/sage-4.0.rc1$ ./sage -gdb
----------------------------------------------------------------------
----------------------------------------------------------------------
/scratch/wstein/build/sage-4.0.rc1/local/bin/sage-ipython
GNU gdb 6.8-debian
Copyright (C) 2008 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu"...
[Thread debugging using libthread_db enabled]
Python 2.5.4 (r254:67916, May 29 2009, 07:08:12) 
[GCC 4.2.4 (Ubuntu 4.2.4-1ubuntu3)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
[New Thread 0x7fe5414a06e0 (LWP 25611)]
sage: theta1,theta2=var('theta1,theta2'); theta1.subs(theta1=1,theta2=0)
| Sage Version 4.0.rc1, Release Date: 2009-05-28                     |
| Type notebook() for the GUI, and license() for information.        |
Program received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0x7fe5414a06e0 (LWP 25611)]
import_submodule (mod=0xbbcde0, subname=0x7fff48cb9fbb "sage", fullname=0x7fff48cb9fb0 "sage.rings.sage") at Python/import.c:2360
2360	Python/import.c: No such file or directory.
	in Python/import.c
(gdb) bt
#0  import_submodule (mod=0xbbcde0, subname=0x7fff48cb9fbb "sage", fullname=0x7fff48cb9fb0 "sage.rings.sage") at Python/import.c:2360
#1  0x00000000004a1a1b in load_next (mod=0xbbcde0, altmod=0x72bdc0, p_name=<value optimized out>, buf=0x7fff48cb9fb0 "sage.rings.sage", 
    p_buflen=0x7fff48cb9fa8) at Python/import.c:2220
#2  0x00000000004a1c5a in import_module_level (name=0xb0b679 "rings.qqbar", globals=0x75a010, locals=<value optimized out>, 
    fromlist=0x4577998, level=<value optimized out>) at Python/import.c:2001
#3  0x00000000004a2105 in PyImport_ImportModuleLevel (name=0xb0b674 "sage.rings.qqbar", globals=0x1287f80, locals=0x898400, 
    fromlist=0x4577998, level=-1) at Python/import.c:2072
#4  0x0000000000481849 in builtin___import__ (self=<value optimized out>, args=<value optimized out>, kwds=<value optimized out>)
    at Python/bltinmodule.c:47
#5  0x000000000041abbd in PyObject_CallFunctionObjArgs (callable=0x7fe54146d5f0) at Objects/abstract.c:1861
#6  0x00007fe52d05bac8 in __Pyx_Import (name=0xb0b650, from_list=0x4577998) at sage/rings/real_mpfi.c:20944
#7  0x00007fe52d07dfcf in __pyx_pf_4sage_5rings_9real_mpfi_24RealIntervalFieldElement___init__ (__pyx_v_self=0x26320d8, 
    __pyx_args=<value optimized out>, __pyx_kwds=<value optimized out>) at sage/rings/real_mpfi.c:6654
#8  0x000000000045cf81 in type_call (type=0x7fe52d29ed60, args=0x7fe5413aaf00, kwds=0x0) at Objects/typeobject.c:436
#9  0x0000000000417eb3 in PyObject_Call (func=0xbbcde0, arg=0x7fff48cb9fbb, kw=0x7fff48cb9fb0) at Objects/abstract.c:1861
#10 0x00007fe52d06e47e in __pyx_pf_4sage_5rings_9real_mpfi_23RealIntervalField_class___call__ (__pyx_v_self=0x120f450, 
    __pyx_args=<value optimized out>, __pyx_kwds=0x7fe5413aaf00) at sage/rings/real_mpfi.c:4323
#11 0x0000000000417eb3 in PyObject_Call (func=0xbbcde0, arg=0x7fff48cb9fbb, kw=0x7fff48cb9fb0) at Objects/abstract.c:1861
#12 0x00007fe52b7c44ec in __pyx_pf_4sage_5rings_16complex_interval_27ComplexIntervalFieldElement___init__ (__pyx_v_self=<value optimized out>, 
    __pyx_args=<value optimized out>, __pyx_kwds=<value optimized out>) at sage/rings/complex_interval.c:3059
#13 0x000000000045cf81 in type_call (type=0x7fe52b9d3ac0, args=0x7fe5413aaf50, kwds=0x0) at Objects/typeobject.c:436
#14 0x0000000000417eb3 in PyObject_Call (func=0xbbcde0, arg=0x7fff48cb9fbb, kw=0x7fff48cb9fb0) at Objects/abstract.c:1861
#15 0x0000000000486592 in PyEval_EvalFrameEx (f=0x18683a0, throwflag=<value optimized out>) at Python/ceval.c:3823
#16 0x0000000000489fd4 in PyEval_EvalCodeEx (co=0x1366c60, globals=<value optimized out>, locals=<value optimized out>, args=0x4577728, 
    argcount=2, kws=0x0, kwcount=0, defs=0x1368b68, defcount=1, closure=0x0) at Python/ceval.c:2875
#17 0x00000000004d4c0a in function_call (func=0x1369b90, arg=0x4577710, kw=0x0) at Objects/funcobject.c:517
```



---

Comment by burcin created at 2009-05-31 13:23:26

Changing status from new to assigned.


---

Comment by burcin created at 2009-05-31 13:23:26

Shorter snippet:


```
sage: var('theta1,theta2')
var('theta1,theta2')
sage: (theta1 == theta2).test_relation()
/home/burcin/sage/sage-4.0.rc1/local/bin/sage-sage: line 198:  8823 Segmentation fault      sage-ipython "$@" -i
```


This doesn't have a problem:


```
sage: var('t1,t2')
(t1, t2)
sage: (t1 == t2).test_relation()
False
```


This is caused by the fact that theta1 and theta2 have the same hash (as all symbolic variables which have the same 4 characters in their name), and trying to put them as keys in a dictionary calls `__nonzero__`() and test_relation() in turn, causing an infinite loop.


```
sage: hash(theta1) == hash(theta2)
True
sage: hash(t1) == hash(t2)
False
```



---

Comment by burcin created at 2009-05-31 16:48:56

This is easily fixed by reverting symbol::calchash to the original code in pynac. Since we use the symbol name for comparison in symbol::compare_same_type, this change doesn't effect the printing order. However, it makes the hash values random.

I can't see anything wrong with having random hash values. Are there any objections to this?


---

Comment by mhansen created at 2009-05-31 19:15:13

Burcin, that sounds good to me.


---

Comment by robertwb created at 2009-06-01 23:45:37

We should probably special-case single-variable expression hashing and equality given how often they're used (e.g. in dictionaries) and how infrequently they're equal.


---

Attachment


---

Comment by burcin created at 2009-06-04 10:12:43

New pynac package here reverts to the original `symbol::calchash` and fixes this issue:

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.8.spkg

Attached patch makes the necessary doctest changes.

The new package also contains a fix for #6144, so these tickets should be merged together.


---

Comment by was created at 2009-06-04 21:07:32

Changing priority from major to blocker.


---

Comment by mhansen created at 2009-06-05 02:01:57

Resolution: fixed


---

Comment by mhansen created at 2009-06-05 02:01:57

The changes look good to me and all doctests pass.

Merged in 4.0.1.rc2.
