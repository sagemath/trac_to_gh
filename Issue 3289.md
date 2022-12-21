# Issue 3289: linear_code -- segfaults on ubuntu linux

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-05-23 17:34:30

Assignee: rlm

This might be related to #3288


This is on an ubuntu 32-bit linux box with 512MB RAM.

```
 ./sage -t --verbose devel/sage/sage/coding/linear_code.py
...
Trying:
    for B in self_orthogonal_binary_codes(Integer(7),Integer(3)):###line 402:_sage_    >>> for B in self_orthogonal_binary_codes(7,3):
       print B
Expecting:
    Linear code of length 2, dimension 1 over Finite Field of size 2
    Linear code of length 4, dimension 2 over Finite Field of size 2
    Linear code of length 6, dimension 3 over Finite Field of size 2
    Linear code of length 4, dimension 1 over Finite Field of size 2
    Linear code of length 6, dimension 2 over Finite Field of size 2
    Linear code of length 6, dimension 2 over Finite Field of size 2
    Linear code of length 7, dimension 3 over Finite Field of size 2
    Linear code of length 6, dimension 1 over Finite Field of size 2
*** glibc detected *** /home/was/build/sage-3.0.2.rc0/local/bin/python: free(): invalid next size (fast): 0x09d2a578 ***
======= Backtrace: =========
/lib/tls/i686/cmov/libc.so.6[0xb7e297cd]
/lib/tls/i686/cmov/libc.so.6(cfree+0x90)[0xb7e2ce30]
/home/was/build/sage-3.0.2.rc0/local/lib/python/site-packages/sage/coding/binary_code.so[0xb2b8672f]
/home/was/build/sage-3.0.2.rc0/local/bin/python(PyEval_EvalFrameEx+0x66f9)[0x80c97c9]
/home/was/build/sage-3.0.2.rc0/local/bin/python[0x810f87d]
/home/was/build/sage-3.0.2.rc0/local/bin/python(PyEval_EvalFrameEx+0xa1a)[0x80c3aea]
/home/was/build/sage-3.0.2.rc0/local/bin/python[0x810f87d]
/home/was/build/sage-3.0.2.rc0/local/bin/python(PyEval_EvalFrameEx+0xa1a)[0x80c3aea]
/home/was/build/sage-3.0.2.rc0/local/bin/python[0x810f87d]
/home/was/build/sage-3.0.2.rc0/local/bin/python(PyEval_EvalFrameEx+0xa1a)[0x80c3aea]
/home/was/build/sage-3.0.2.rc0/local/bin/python(PyEval_EvalCodeEx+0x785)[0x80c9ff5]
/home/was/build/sage-3.0.2.rc0/local/bin/python(PyEval_EvalFrameEx+0x5c0b)[0x80c8cdb]
/home/was/build/sage-3.0.2.rc0/local/bin/python(PyEval_EvalCodeEx+0x785)[0x80c9ff5]
/home/was/build/sage-3.0.2.rc0/local/bin/python(PyEval_EvalFrameEx+0x52f5)[0x80c83c5]
/home/was/build/sage-3.0.2.rc0/local/bin/python(PyEval_EvalCodeEx+0x785)[0x80c9ff5]
/home/was/build/sage-3.0.2.rc0/local/bin/python(PyEval_EvalFrameEx+0x52f5)[0x80c83c5]
/home/was/build/sage-3.0.2.rc0/local/bin/python(PyEval_EvalCodeEx+0x785)[0x80c9ff5]
/home/was/build/sage-3.0.2.rc0/local/bin/python(PyEval_EvalFrameEx+0x52f5)[0x80c83c5]
/home/was/build/sage-3.0.2.rc0/local/bin/python(PyEval_EvalCodeEx+0x785)[0x80c9ff5]
/home/was/build/sage-3.0.2.rc0/local/bin/python(PyEval_EvalCode+0x57)[0x80ca067]
/home/was/build/sage-3.0.2.rc0/local/bin/python(PyRun_FileExFlags+0xf8)[0x80e9328]
/home/was/build/sage-3.0.2.rc0/local/bin/python(PyRun_SimpleFileExFlags+0x187)[0x80e95b7]
/home/was/build/sage-3.0.2.rc0/local/bin/python(Py_Main+0x9aa)[0x80592da]
/home/was/build/sage-3.0.2.rc0/local/bin/python(main+0x22)[0x8058822]
/lib/tls/i686/cmov/libc.so.6(__libc_start_main+0xdc)[0xb7dd7ebc]
/home/was/build/sage-3.0.2.rc0/local/bin/python[0x8058771]
======= Memory map: ========
08048000-0813e000 r-xp 00000000 08:01 444247     /home/was/build/sage-3.0.2.rc0/local/bin/python
0813e000-08163000 rwxp 000f5000 08:01 444247     /home/was/build/sage-3.0.2.rc0/local/bin/python
08163000-0a905000 rwxp 08163000 00:00 0          [heap]
b2800000-b2821000 rwxp b2800000 00:00 0
b2821000-b2900000 ---p b2821000 00:00 0
b2953000-b2b68000 rwxp b2953000 00:00 0
b2b68000-b2b9c000 r-xp 00000000 08:01 540553     /home/was/build/sage-3.0.2.rc0/devel/sage-main/build/sage/coding/binary_code.so
b2b9c000-b2ba9000 rwxp 00033000 08:01 540553     /home/was/build/sage-3.0.2.rc0/devel/sage-main/build/sage/coding/binary_code.so
b2ba9000-b2baa000 rwxp b2ba9000 00:00 0
b2baa000-b2bc0000 r-xp 00000000 08:01 540885     /home/was/build/sage-3.0.2.rc0/devel/sage-main/build/sage/matrix/strassen.so
b2bc0000-b2bc2000 rwxp 00015000 08:01 540885     /home/was/build/sage-3.0.2.rc0/devel/sage-main/build/sage/matrix/strassen.so
b2bc2000-b2bce000 r-xp 00000000 08:01 540912     /home/was/build/sage-3.0.2.rc0/devel/sage-main/build/sage/matrix/action.so
b2bce000-b2bd0000 rwxp 0000c000 08:01 540912     /home/was/build/sage-3.0.2.rc0/devel/sage-main/build/sage/matrix/action.so
b2bd0000-b2bd7000 r-xp 00000000 08:01 540923     /home/was/build/sage-3.0.2.rc0/devel/sage-main/build/sage/ext/interactive_constructors_c.so
b2bd7000-b2bd9000 rwxp 00007000 08:01 540923     /home/was/build/sage-3.0.2.rc0/devel/sage-main/build/sage/ext/interactive_constructors_c.so
b2bd9000-b2bee000 r-xp 00000000 08:01 540952     /home/was/build/sage-3.0.2.rc0/devel/sage-main/build/sage/gsl/probability_distribution.so
b2bee000-b2bf0000 rwxp 00014000 08:01 540952     /home/was/build/sage-3.0.2.rc0/devel/sage-main/build/sage/gsl/probability_distribution.so
b2bf0000-b2bf1000 rwxp b2bf0000 00:00 0
b2bf1000-b2c02000 r-xp 00000000 08:01 540949     /home/was/build/sage-3.0.2.rc0/devel/sage-main/build/sage/gsl/ode.so
b2c02000-b2c05000 rwxp 00011000 08:01 540949     /home/was/build/sage-3.0.2.rc0/devel/sage-main/build/sage/gsl/ode.so
b2c05000-b2c08000 r-xp 00000000 08:01 540953     /home/was/build/sage-3.0.2.rc0/devel/sage-main/build/sage/gsl/gsl_array.so
b2c08000-b2c09000 rwxp 00002000 08:01 540953     /home/was/build/sage-3.0.2.rc0/devel/sage-main/build/sage/gsl/gsl_array.so
b2c09000-b2c0f000 r-xp 00000000 08:01 540945     /home/was/build/sage-3.0.2.rc0/devel/sage-main/build/sage/gsl/dwt.so
b2c0f000-b2c11000 rwxp 00005000 08:01 540945     /home/was/build/sage-3.0.2.rc0/devel/sage-main/build/sage/gsl/dwt.so
b2c11000-b2c1b000 r-xp 00000000 08:01 540950     /home/was/build/sage-3.0.2.rc0/devel/sage-main/build/sage/gsl/fft.so
b2c1b000-b2c1d000 rwxp 00009000 08:01 540950     /home/was/build/sage-3.0.2.rc0/devel/sage-main/build/sage/gsl/fft.so
b2c1d000-b2c26000 r-xp 00000000 08:01 541024     /home/was/build/sage-3.0.2.rc0/devel/sage-main/build/sage/combinat/matrices/dancing_links.so

```



---

Comment by was created at 2008-05-23 17:53:45

Here's a clean backtrace of the above run under gdb.  


```
Type "help", "copyright", "credits" or "license" for more information.

----------------------------------------------------------------------
----------------------------------------------------------------------
sage: list(self_orthogonal_binary_codes(Integer(7),Integer(3)))      
| SAGE Version 3.0.2.rc0, Release Date: 2008-05-23                   |
| Type notebook() for the GUI, and license() for information.        |
Program received signal SIGSEGV, Segmentation fault.
[Switching to Thread -1210111792 (LWP 29301)]
0xb7e5899f in ?? () from /lib/tls/i686/cmov/libc.so.6
(gdb) bt
#0  0xb7e5899f in ?? () from /lib/tls/i686/cmov/libc.so.6
#1  0x00000004 in ?? ()
#2  0x084d6b0c in ?? ()
#3  0x085986bc in ?? ()
#4  0x08594530 in ?? ()
#5  0x00000007 in ?? ()
#6  0xb7f166aa in ?? () from /lib/tls/i686/cmov/libc.so.6
#7  0x094efe3c in ?? ()
#8  0xb7f166aa in ?? () from /lib/tls/i686/cmov/libc.so.6
#9  0xb7f31120 in ?? () from /lib/tls/i686/cmov/libc.so.6
#10 0x00000019 in ?? ()
#11 0xb7f3112c in ?? () from /lib/tls/i686/cmov/libc.so.6
#12 0xb7f31144 in ?? () from /lib/tls/i686/cmov/libc.so.6
#13 0x0a234408 in ?? ()
#14 0xb7f31150 in ?? () from /lib/tls/i686/cmov/libc.so.6
#15 0x00000030 in ?? ()
#16 0xb7e5bf74 in ?? () from /lib/tls/i686/cmov/libc.so.6
#17 0xb7f31120 in ?? () from /lib/tls/i686/cmov/libc.so.6
#18 0x09de5878 in ?? ()
#19 0x00000000 in ?? ()
(gdb) 
```


Also, note that *sometimes* the crash happens on exit only:


```
was`@`ubuntu:~/build/sage-3.0.2.rc0$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.0.2.rc0, Release Date: 2008-05-23                   |
| Type notebook() for the GUI, and license() for information.        |
sage: list(self_orthogonal_binary_codes(Integer(7),Integer(3)))

[Linear code of length 2, dimension 1 over Finite Field of size 2,
 Linear code of length 4, dimension 2 over Finite Field of size 2,
 Linear code of length 6, dimension 3 over Finite Field of size 2,
 Linear code of length 4, dimension 1 over Finite Field of size 2,
 Linear code of length 6, dimension 2 over Finite Field of size 2,
 Linear code of length 6, dimension 2 over Finite Field of size 2,
 Linear code of length 7, dimension 3 over Finite Field of size 2,
 Linear code of length 6, dimension 1 over Finite Field of size 2]
sage:                                                                                                                                                                                                                                                         
Exiting SAGE (CPU time 0m1.68s, Wall time 0m13.86s).
Exiting spawned Gap process.
*** glibc detected *** sage.bin: free(): invalid next size (fast): 0x09b62128 ***
======= Backtrace: =========
/lib/tls/i686/cmov/libc.so.6[0xb7e5a7cd]
/lib/tls/i686/cmov/libc.so.6(cfree+0x90)[0xb7e5de30]
/home/was/build/sage-3.0.2.rc0/local/lib/python2.5/site-packages/sage/rings/memory.so[0xb73a7f0d]
/home/was/build/sage-3.0.2.rc0/local/lib/libgmp.so.3(__gmpz_clear+0x2c)[0xb78bf2fc]
/home/was/build/sage-3.0.2.rc0/local/lib/python2.5/site-packages/sage/rings/integer.so[0xb6c5db3c]
sage.bin(PyEval_EvalFrameEx+0x62e7)[0x80c93b7]
sage.bin(PyEval_EvalCodeEx+0x785)[0x80c9ff5]
sage.bin(PyEval_EvalFrameEx+0x52f5)[0x80c83c5]
sage.bin(PyEval_EvalCodeEx+0x785)[0x80c9ff5]
sage.bin(PyEval_EvalFrameEx+0x52f5)[0x80c83c5]
sage.bin(PyEval_EvalCodeEx+0x785)[0x80c9ff5]
sage.bin(PyEval_EvalFrameEx+0x52f5)[0x80c83c5]
sage.bin(PyEval_EvalCodeEx+0x785)[0x80c9ff5]
sage.bin(PyEval_EvalFrameEx+0x52f5)[0x80c83c5]
sage.bin(PyEval_EvalCodeEx+0x785)[0x80c9ff5]
sage.bin(PyEval_EvalFrameEx+0x52f5)[0x80c83c5]
sage.bin(PyEval_EvalCodeEx+0x785)[0x80c9ff5]
sage.bin(PyEval_EvalCode+0x57)[0x80ca067]
sage.bin(PyRun_FileExFlags+0xf8)[0x80e9328]
sage.bin(PyRun_SimpleFileExFlags+0x187)[0x80e95b7]
sage.bin(Py_Main+0x9aa)[0x80592da]
sage.bin(main+0x22)[0x8058822]
/lib/tls/i686/cmov/libc.so.6(__libc_start_main+0xdc)[0xb7e08ebc]
sage.bin[0x8058771]
======= Memory map: ========
08048000-0813e000 r-xp 00000000 08:01 444247     /home/was/build/sage-3.0.2.rc0/local/bin/python
0813e000-08163000 rwxp 000f5000 08:01 444247     /home/was/build/sage-3.0.2.rc0/local/bin/python
08163000-0a4fd000 rwxp 08163000 00:00 0          [heap]
b29eb000-b2c00000 rwxp b29eb000 00:00 0 
b2c00000-b2c34000 r-xp 00000000 08:01 540553     /home/was/build/sage-3.0.2.rc0/devel/sage-main/build/sage/coding/binary_code.so
b2c34000-b2c41000 rwxp 00033000 08:01 540553     /home/was/build/sage-3.0.2.rc0/devel/sage-main/build/sage/coding/binary_code.so
b2c41000-b2c42000 rwxp b2c41000 00:00 0 
b2c42000-b2c49000 r-xp 00000000 08:01 540923     /home/was/build/sage-3.0.2.rc0/devel/sage-main/build/sage/ext/interactive_constructors_c.so
b2c49000-b2c4b000 rwxp 00007000 08:01 540923     /home/was/build/sage-3.0.2.rc0/devel/sage-main/build/sage/ext/interactive_constructors_c.so
b2c4b000-b2c60000 r-xp 00000000 08:01 540952     /home/was/build/sage-3.0.2.rc0/devel/sage-main/build/sage/gsl/probability_distribution.so
b2c60000-b2c62000 rwxp 00014000 08:01 540952     /home/was/build/sage-3.0.2.rc0/devel/sage-main/build/sage/gsl/probability_distribution.so
b2c62000-b2c63000 rwxp b2c62000 00:00 0 
b2c63000-b2c74000 r-xp 00000000 08:01 540949     /home/was/build/sage-3.0.2.rc0/devel/sage-main/build/sage/gsl/ode.so
b2c74000-b2c77000 rwxp 00011000 08:01 540949     /home/was/build/sage-3.0.2.rc0/devel/sage-main/build/sage/gsl/ode.so
b2c77000-b2c7a000 r-xp 00000000 08:01 540953     /home/was/build/sage-3.0.2.rc0/devel/sage-main/build/sage/gsl/gsl_array.so
b2c7a000-b2c7b000 rwxp 00002000 08:01 540953     /home/was/build/sage-3.0.2.rc0/devel/sage-main/build/sage/gsl/gsl_array.so
b2c7b000-b2c81000 r-xp 00000000 08:01 540945     /home/was/build/sage-3.0.2.rc0/devel/sage-main/build/sage/gsl/dwt.so
b2c81000-b2c83000 rwxp 00005000 08:01 540945     /home/was/build/sage-3.0.2.rc0/devel/sage-main/build/sage/gsl/dwt.so
b2c83000-b2c8d000 r-xp 00000000 08:01 540950     /home/was/build/sage-3.0.2.rc0/devel/sage-main/build/sage/gsl/fft.so
b2c8d000-b2c8f000 rwxp 00009000 08:01 540950     /home/was/build/sage-3.0.2.rc0/devel/sage-main/build/sage/gsl/fft.so
b2c8f000-b2c98000 r-xp 00000000 08:01 541024     /home/was/build/sage-3.0.2.rc0/devel/sage-main/build/sage/combinat/matrices/dancing_links.so
b2c98000-b2c9a000 rwxp 00008000 08:01 541024     /home/was/build/sage-3.0.2.rc0/devel/sage-main/build/sage/combinat/matrices/dancing_links.so
b2c9a000-b2ca1000 r-xp 00000000 08:01 541077     /home/was/build/sage-3.0.2.rc0/devel/sage-main/build/sage/combinat/expnums.so
b2ca1000-b2ca2000 rwxp 00007000 08:01 541077     /home/was/build/sage-3.0.2.rc0/devel/sage-main/build/sage/combinat/expnums.so
b2ca/home/was/build/sage-3.0.2.rc0/local/bin/sage-sage: line 214: 29511 Aborted                 sage-ipython "$`@`" -c "$SAGE_STARTUP_COMMAND;"
was`@`ubuntu:~/build/sage-3.0.2.rc0$ 

```



---

Comment by mabshoff created at 2008-05-23 18:10:00

Valgrind says:

```
==23674== Memcheck, a memory error detector.
==23674== Copyright (C) 2002-2007, and GNU GPL'd, by Julian Seward et al.
==23674== Using LibVEX rev 1804, a library for dynamic binary translation.
==23674== Copyright (C) 2004-2007, and GNU GPL'd, by OpenWorks LLP.
==23674== Using valgrind-3.3.0, a dynamic binary instrumentation framework.
==23674== Copyright (C) 2000-2007, and GNU GPL'd, by Julian Seward et al.
==23674== For more details, rerun with: -v
==23674== 
==23674== My PID = 23674, parent PID = 23660.  Prog and args are:
==23674==    /scratch/mabshoff/release-cycle/sage-3.0.2.rc1/local/bin/python
==23674==    /scratch/mabshoff/release-cycle/sage-3.0.2.rc1/tmp/.doctest_linear_code.py
==23674== 
--23674-- DWARF2 CFI reader: unhandled CFI instruction 0:10
--23674-- DWARF2 CFI reader: unhandled CFI instruction 0:10
==23674== Conditional jump or move depends on uninitialised value(s)
==23674==    at 0x235EE139: __pyx_f_4sage_6coding_11binary_code_20BinaryCodeClassifier_aut_gp_and_can_label (binary_code.c:22181)
==23674==    by 0x235E4EA1: __pyx_pf_4sage_6coding_11binary_code_20BinaryCodeClassifier__aut_gp_and_can_label (binary_code.c:19523)
==23674==    by 0x483E46: PyEval_EvalFrameEx (ceval.c:3573)
==23674==    by 0x48491B: PyEval_EvalFrameEx (ceval.c:3659)
==23674==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==23674==    by 0x484AF1: PyEval_EvalFrameEx (ceval.c:494)
==23674==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==23674==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==23674==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==23674==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==23674==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==23674==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==23674== 
==23674== Invalid write of size 4
==23674==    at 0x235CE5B1: __pyx_f_4sage_6coding_11binary_code_expand_to_ortho_basis (binary_code.c:5485)
==23674==    by 0x235D8F8F: __pyx_pf_4sage_6coding_11binary_code_20BinaryCodeClassifier_generate_children (binary_code.c:24336)
==23674==    by 0x483E46: PyEval_EvalFrameEx (ceval.c:3573)
==23674==    by 0x4CD076: gen_send_ex (genobject.c:82)
==23674==    by 0x47EFBC: PyEval_EvalFrameEx (ceval.c:2169)
==23674==    by 0x4CD076: gen_send_ex (genobject.c:82)
==23674==    by 0x47EFBC: PyEval_EvalFrameEx (ceval.c:2169)
==23674==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==23674==    by 0x484AF1: PyEval_EvalFrameEx (ceval.c:494)
==23674==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==23674==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==23674==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==23674==  Address 0x12b5d5dc is 0 bytes after a block of size 12 alloc'd
==23674==    at 0x4A1BDEB: malloc (vg_replace_malloc.c:207)
==23674==    by 0x235CE4C8: __pyx_f_4sage_6coding_11binary_code_expand_to_ortho_basis (binary_code.c:5186)
==23674==    by 0x235D8F8F: __pyx_pf_4sage_6coding_11binary_code_20BinaryCodeClassifier_generate_children (binary_code.c:24336)
==23674==    by 0x483E46: PyEval_EvalFrameEx (ceval.c:3573)
==23674==    by 0x4CD076: gen_send_ex (genobject.c:82)
==23674==    by 0x47EFBC: PyEval_EvalFrameEx (ceval.c:2169)
==23674==    by 0x4CD076: gen_send_ex (genobject.c:82)
==23674==    by 0x47EFBC: PyEval_EvalFrameEx (ceval.c:2169)
==23674==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==23674==    by 0x484AF1: PyEval_EvalFrameEx (ceval.c:494)
==23674==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==23674==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==23674== 
==23674== Conditional jump or move depends on uninitialised value(s)
==23674==    at 0x235EE139: __pyx_f_4sage_6coding_11binary_code_20BinaryCodeClassifier_aut_gp_and_can_label (binary_code.c:22181)
==23674==    by 0x235E4EA1: __pyx_pf_4sage_6coding_11binary_code_20BinaryCodeClassifier__aut_gp_and_can_label (binary_code.c:19523)
==23674==    by 0x415832: PyObject_Call (abstract.c:1861)
==23674==    by 0x235D8FEE: __pyx_pf_4sage_6coding_11binary_code_20BinaryCodeClassifier_generate_children (binary_code.c:24349)
==23674==    by 0x483E46: PyEval_EvalFrameEx (ceval.c:3573)
==23674==    by 0x4CD076: gen_send_ex (genobject.c:82)
==23674==    by 0x47EFBC: PyEval_EvalFrameEx (ceval.c:2169)
==23674==    by 0x4CD076: gen_send_ex (genobject.c:82)
==23674==    by 0x47EFBC: PyEval_EvalFrameEx (ceval.c:2169)
==23674==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==23674==    by 0x484AF1: PyEval_EvalFrameEx (ceval.c:494)
==23674==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==23674== 
==23674== Conditional jump or move depends on uninitialised value(s)
==23674==    at 0x235EE139: __pyx_f_4sage_6coding_11binary_code_20BinaryCodeClassifier_aut_gp_and_can_label (binary_code.c:22181)
==23674==    by 0x235E4EA1: __pyx_pf_4sage_6coding_11binary_code_20BinaryCodeClassifier__aut_gp_and_can_label (binary_code.c:19523)
==23674==    by 0x415832: PyObject_Call (abstract.c:1861)
==23674==    by 0x235DAF08: __pyx_pf_4sage_6coding_11binary_code_20BinaryCodeClassifier_generate_children (binary_code.c:25146)
==23674==    by 0x483E46: PyEval_EvalFrameEx (ceval.c:3573)
==23674==    by 0x4CD076: gen_send_ex (genobject.c:82)
==23674==    by 0x47EFBC: PyEval_EvalFrameEx (ceval.c:2169)
==23674==    by 0x4CD076: gen_send_ex (genobject.c:82)
==23674==    by 0x47EFBC: PyEval_EvalFrameEx (ceval.c:2169)
==23674==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==23674==    by 0x484AF1: PyEval_EvalFrameEx (ceval.c:494)
==23674==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==23674== 
==23674== Invalid read of size 4
==23674==    at 0x235CB0AC: __pyx_f_4sage_6coding_11binary_code_create_array_word_perm (binary_code.c:3483)
==23674==    by 0x235DB1DE: __pyx_pf_4sage_6coding_11binary_code_20BinaryCodeClassifier_generate_children (binary_code.c:4693)
==23674==    by 0x483E46: PyEval_EvalFrameEx (ceval.c:3573)
==23674==    by 0x4CD076: gen_send_ex (genobject.c:82)
==23674==    by 0x47EFBC: PyEval_EvalFrameEx (ceval.c:2169)
==23674==    by 0x4CD076: gen_send_ex (genobject.c:82)
==23674==    by 0x47EFBC: PyEval_EvalFrameEx (ceval.c:2169)
==23674==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==23674==    by 0x484AF1: PyEval_EvalFrameEx (ceval.c:494)
==23674==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==23674==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==23674==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==23674==  Address 0x12d5cc00 is 0 bytes after a block of size 16 alloc'd
==23674==    at 0x4A1BDEB: malloc (vg_replace_malloc.c:207)
==23674==    by 0x235DB138: __pyx_pf_4sage_6coding_11binary_code_20BinaryCodeClassifier_generate_children (binary_code.c:4624)
==23674==    by 0x483E46: PyEval_EvalFrameEx (ceval.c:3573)
==23674==    by 0x4CD076: gen_send_ex (genobject.c:82)
==23674==    by 0x47EFBC: PyEval_EvalFrameEx (ceval.c:2169)
==23674==    by 0x4CD076: gen_send_ex (genobject.c:82)
==23674==    by 0x47EFBC: PyEval_EvalFrameEx (ceval.c:2169)
==23674==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==23674==    by 0x484AF1: PyEval_EvalFrameEx (ceval.c:494)
==23674==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==23674==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==23674==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==23674== 
==23674== Invalid read of size 4
==23674==    at 0x235CB0BD: __pyx_f_4sage_6coding_11binary_code_create_array_word_perm (binary_code.c:3483)
==23674==    by 0x235DB1DE: __pyx_pf_4sage_6coding_11binary_code_20BinaryCodeClassifier_generate_children (binary_code.c:4693)
==23674==    by 0x483E46: PyEval_EvalFrameEx (ceval.c:3573)
==23674==    by 0x4CD076: gen_send_ex (genobject.c:82)
==23674==    by 0x47EFBC: PyEval_EvalFrameEx (ceval.c:2169)
==23674==    by 0x4CD076: gen_send_ex (genobject.c:82)
==23674==    by 0x47EFBC: PyEval_EvalFrameEx (ceval.c:2169)
==23674==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==23674==    by 0x484AF1: PyEval_EvalFrameEx (ceval.c:494)
==23674==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==23674==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==23674==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==23674==  Address 0x12d5cc04 is 4 bytes after a block of size 16 alloc'd
==23674==    at 0x4A1BDEB: malloc (vg_replace_malloc.c:207)
==23674==    by 0x235DB138: __pyx_pf_4sage_6coding_11binary_code_20BinaryCodeClassifier_generate_children (binary_code.c:4624)
==23674==    by 0x483E46: PyEval_EvalFrameEx (ceval.c:3573)
==23674==    by 0x4CD076: gen_send_ex (genobject.c:82)
==23674==    by 0x47EFBC: PyEval_EvalFrameEx (ceval.c:2169)
==23674==    by 0x4CD076: gen_send_ex (genobject.c:82)
==23674==    by 0x47EFBC: PyEval_EvalFrameEx (ceval.c:2169)
==23674==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==23674==    by 0x484AF1: PyEval_EvalFrameEx (ceval.c:494)
==23674==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==23674==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==23674==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==23674== 
==23674== Invalid read of size 4
==23674==    at 0x235CB0D1: __pyx_f_4sage_6coding_11binary_code_create_array_word_perm (binary_code.c:3483)
==23674==    by 0x235DB1DE: __pyx_pf_4sage_6coding_11binary_code_20BinaryCodeClassifier_generate_children (binary_code.c:4693)
==23674==    by 0x483E46: PyEval_EvalFrameEx (ceval.c:3573)
==23674==    by 0x4CD076: gen_send_ex (genobject.c:82)
==23674==    by 0x47EFBC: PyEval_EvalFrameEx (ceval.c:2169)
==23674==    by 0x4CD076: gen_send_ex (genobject.c:82)
==23674==    by 0x47EFBC: PyEval_EvalFrameEx (ceval.c:2169)
==23674==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==23674==    by 0x484AF1: PyEval_EvalFrameEx (ceval.c:494)
==23674==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==23674==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==23674==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==23674==  Address 0x12d5cc08 is 8 bytes after a block of size 16 alloc'd
==23674==    at 0x4A1BDEB: malloc (vg_replace_malloc.c:207)
==23674==    by 0x235DB138: __pyx_pf_4sage_6coding_11binary_code_20BinaryCodeClassifier_generate_children (binary_code.c:4624)
==23674==    by 0x483E46: PyEval_EvalFrameEx (ceval.c:3573)
==23674==    by 0x4CD076: gen_send_ex (genobject.c:82)
==23674==    by 0x47EFBC: PyEval_EvalFrameEx (ceval.c:2169)
==23674==    by 0x4CD076: gen_send_ex (genobject.c:82)
==23674==    by 0x47EFBC: PyEval_EvalFrameEx (ceval.c:2169)
==23674==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==23674==    by 0x484AF1: PyEval_EvalFrameEx (ceval.c:494)
==23674==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==23674==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==23674==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==23674== 
==23674== Invalid read of size 4
==23674==    at 0x235CB0E5: __pyx_f_4sage_6coding_11binary_code_create_array_word_perm (binary_code.c:3483)
==23674==    by 0x235DB1DE: __pyx_pf_4sage_6coding_11binary_code_20BinaryCodeClassifier_generate_children (binary_code.c:4693)
==23674==    by 0x483E46: PyEval_EvalFrameEx (ceval.c:3573)
==23674==    by 0x4CD076: gen_send_ex (genobject.c:82)
==23674==    by 0x47EFBC: PyEval_EvalFrameEx (ceval.c:2169)
==23674==    by 0x4CD076: gen_send_ex (genobject.c:82)
==23674==    by 0x47EFBC: PyEval_EvalFrameEx (ceval.c:2169)
==23674==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==23674==    by 0x484AF1: PyEval_EvalFrameEx (ceval.c:494)
==23674==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==23674==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==23674==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==23674==  Address 0x12d5cc0c is 12 bytes after a block of size 16 alloc'd
==23674==    at 0x4A1BDEB: malloc (vg_replace_malloc.c:207)
==23674==    by 0x235DB138: __pyx_pf_4sage_6coding_11binary_code_20BinaryCodeClassifier_generate_children (binary_code.c:4624)
==23674==    by 0x483E46: PyEval_EvalFrameEx (ceval.c:3573)
==23674==    by 0x4CD076: gen_send_ex (genobject.c:82)
==23674==    by 0x47EFBC: PyEval_EvalFrameEx (ceval.c:2169)
==23674==    by 0x4CD076: gen_send_ex (genobject.c:82)
==23674==    by 0x47EFBC: PyEval_EvalFrameEx (ceval.c:2169)
==23674==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==23674==    by 0x484AF1: PyEval_EvalFrameEx (ceval.c:494)
==23674==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==23674==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==23674==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==23674== 
==23674== Conditional jump or move depends on uninitialised value(s)
==23674==    at 0x235EE139: __pyx_f_4sage_6coding_11binary_code_20BinaryCodeClassifier_aut_gp_and_can_label (binary_code.c:22181)
==23674==    by 0x235E4EA1: __pyx_pf_4sage_6coding_11binary_code_20BinaryCodeClassifier__aut_gp_and_can_label (binary_code.c:19523)
==23674==    by 0x415832: PyObject_Call (abstract.c:1861)
==23674==    by 0x235DBD4E: __pyx_pf_4sage_6coding_11binary_code_20BinaryCodeClassifier_generate_children (binary_code.c:25635)
==23674==    by 0x483E46: PyEval_EvalFrameEx (ceval.c:3573)
==23674==    by 0x4CD076: gen_send_ex (genobject.c:82)
==23674==    by 0x47EFBC: PyEval_EvalFrameEx (ceval.c:2169)
==23674==    by 0x4CD076: gen_send_ex (genobject.c:82)
==23674==    by 0x47EFBC: PyEval_EvalFrameEx (ceval.c:2169)
==23674==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==23674==    by 0x484AF1: PyEval_EvalFrameEx (ceval.c:494)
==23674==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==23674== 
==23674== ERROR SUMMARY: 1415 errors from 9 contexts (suppressed: 559 from 2)
==23674== malloc/free: in use at exit: 36,525,652 bytes in 227,271 blocks.
==23674== malloc/free: 16,184,639 allocs, 15,957,368 frees, 2,452,463,805 bytes allocated.
==23674== For counts of detected errors, rerun with: -v
==23674== searching for pointers to 227,271 not-freed blocks.
==23674== checked 41,055,744 bytes.
==23674== 
==23674== LEAK SUMMARY:
==23674==    definitely lost: 245,231 bytes in 4,071 blocks.
==23674==      possibly lost: 485,538 bytes in 1,282 blocks.
==23674==    still reachable: 35,794,883 bytes in 221,918 blocks.
==23674==         suppressed: 0 bytes in 0 blocks.
==23674== Rerun with --leak-check=full to see details of leaked memory.
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-05-24 00:32:47

Fixed by merging #3285 in Sage 3.0.2.rc3. This doctest valgrinds clean after merging the patch at #3285.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-24 00:32:47

Resolution: fixed
