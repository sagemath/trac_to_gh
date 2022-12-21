# Issue 2972: libSingular related segfault in laurent_polynomial_ring.py

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-04-20 07:28:17

Assignee: malb

Running of what will be 3.0.rc0 shortly on sage.math leads to:

```
mabshoff`@`sage:sage-3.0.rc0$ ./sage -t -gdb -long devel/sage/sage/rings/polynomial/laurent_polynomial_ring.py
sage -t -gdb -long devel/sage/sage/rings/polynomial/laurent_polynomial_ring.py
********************************************************************************
Type r at the (gdb) prompt to run the doctests.
Type bt if there is a crash to see a traceback.
********************************************************************************
GNU gdb 6.4.90-debian
Copyright (C) 2006 Free Software Foundation, Inc.
GDB is free software, covered by the GNU General Public License, and you are
welcome to change it and/or distribute copies of it under certain conditions.
Type "show copying" to see the conditions.
There is absolutely no warranty for GDB.  Type "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu"...Using host libthread_db library "/lib/libthread_db.so.1".

(gdb) r
Starting program: /scratch/mabshoff/release-cycle/sage-3.0.rc0/local/bin/python /scratch/mabshoff/release-cycle/sage-3.0.rc0/tmp/.doctest_laurent_polynomial_ring.py
[Thread debugging using libthread_db enabled]
[New Thread 47563467300704 (LWP 11542)]

Program received signal SIGSEGV, Segmentation fault.
[Switching to Thread 47563467300704 (LWP 11542)]
nSetChar (r=0x2b424b843880) at numbers.cc:131
131     numbers.cc: No such file or directory.
        in numbers.cc
Current language:  auto; currently c++
(gdb) bt
#0  nSetChar (r=0x2b424b843880) at numbers.cc:131
#1  0x00002b424b5a4293 in rChangeCurrRing (r=0x3) at ring.cc:108
#2  0x00002b424b2c007d in __pyx_tp_dealloc_4sage_5rings_10polynomial_28multi_polynomial_libsingular_MPolynomialRing_libsingular (o=0x1fd4e90) at sage/rings/polynomial/multi_polynomial_libsingular.cpp:3333
#3  0x00000000004b14e3 in collect (generation=<value optimized out>) at Modules/gcmodule.c:714
#4  0x00000000004b1834 in PyGC_Collect () at Modules/gcmodule.c:1265
#5  0x00000000004a758d in Py_Finalize () at Python/pythonrun.c:389
#6  0x00000000004a70db in handle_system_exit () at Python/pythonrun.c:1618
#7  0x00000000004a72d9 in PyErr_PrintEx (set_sys_last_vars=1) at Python/pythonrun.c:1064
#8  0x00000000004a7ae7 in PyRun_SimpleFileExFlags (fp=0x0, filename=<value optimized out>, closeit=1, flags=0x7fff6f971740)
    at Python/pythonrun.c:978
#9  0x0000000000412160 in Py_Main (argc=<value optimized out>, argv=0x7fff6f971858) at Modules/main.c:523
#10 0x00002b423b7094ca in __libc_start_main () from /lib/libc.so.6
#11 0x000000000041169a in _start () at ../sysdeps/x86_64/elf/start.S:113
(gdb) The program is running.  Exit anyway? (y or n) y
```

This is reproducible. Since I am a mean guy I assign this to malb ;)

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-20 07:34:07

In addition valgrind says:

```
==5321== Conditional jump or move depends on uninitialised value(s)
==5321==    at 0x6969F9D: longest_match (deflate.c:1121)
==5321==    by 0x696B368: deflate_slow (deflate.c:1595)
==5321==    by 0x6969462: deflate (deflate.c:790)
==5321==    by 0x8E81577: PyZlib_compress (zlibmodule.c:166)
==5321==    by 0x415542: PyObject_Call (abstract.c:1860)
==5321==    by 0x8D73CB0: __pyx_pf_4sage_9structure_11sage_object_10SageObject_dumps (sage_object.c:1406)
==5321==    by 0x415542: PyObject_Call (abstract.c:1860)
==5321==    by 0x8D76F89: __pyx_pf_4sage_9structure_11sage_object_dumps (sage_object.c:4895)
==5321==    by 0x4833C1: PyEval_EvalFrameEx (ceval.c:3564)
==5321==    by 0x4852CA: PyEval_EvalCodeEx (ceval.c:2831)
==5321==    by 0x484054: PyEval_EvalFrameEx (ceval.c:494)
==5321==    by 0x4852CA: PyEval_EvalCodeEx (ceval.c:2831)
```

I am not sure if this is related, but it could potentially have something to do with the crash.

Cheers,

Michael


---

Comment by was created at 2008-04-20 21:05:30

Here's a doctest failure probably related on 3.0.rc0


```
sage -t  devel/sage/sage/rings/polynomial/laurent_polynomial_ring.pySegmentation fault

A mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.
         [1.5 s]
```



---

Comment by was created at 2008-04-21 02:06:51

Interestingly, this seems to *only* crash if you redirect standout out to a file:

```
was`@`sage:~/build/sage-3.0.rc0/devel/sage/sage/rings/polynomial$ /home/was/build/sage-3.0.rc0/local/bin/python /home/was/build/sage-3.0.rc0/tmp/.doctest_laurent_polynomial_ring.py > a
Segmentation fault
```


but

```
was`@`sage:~/build/sage-3.0.rc0/devel/sage/sage/rings/polynomial$ /home/was/build/sage-3.0.rc0/local/bin/python /home/was/build/sage-3.0.rc0/tmp/.doctest_laurent_polynomial_ring.py
[no seg fault]
```



---

Attachment

I posted a patch that disables weakrefs, which appears to fix the problem.

This isn't too much of a tradeoff.


---

Comment by was created at 2008-04-21 03:17:05

By the way, I tested this on all the platforms where we had this doctest failure and it works.


---

Comment by mabshoff created at 2008-04-21 04:09:41

Patch looks good to me. Segfaults are fixed for me, so the trade off for a little memory leaked is well worth it.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-21 04:15:30

Resolution: fixed


---

Comment by mabshoff created at 2008-04-21 04:15:30

Merged in Sage 3.0.rc1
