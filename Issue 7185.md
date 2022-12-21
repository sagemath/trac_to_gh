# Issue 7185: bug in FFT object in Sage -- segfault

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-10-10 18:41:18

Assignee: cwitty


```
wstein`@`sage:~/build/sage-4.1.2.rc1.alpha3$ ./sage -gdb
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
/scratch/wstein/build/sage-4.1.2.rc1.alpha3/local/bin/sage-ipython
GNU gdb 6.8-debian
Copyright (C) 2008 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu"...
[Thread debugging using libthread_db enabled]
Python 2.6.2 (r262:71600, Oct  4 2009, 20:46:22) 
[GCC 4.2.4 (Ubuntu 4.2.4-1ubuntu4)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
[New Thread 0x7fba1065f6e0 (LWP 12034)]
sage: FFT(1024).inverse_transform()
| Sage Version 4.1.2.rc1.alpha3, Release Date: 2009-10-04            |
| Type notebook() for the GUI, and license() for information.        |
Program received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0x7fba1065f6e0 (LWP 12034)]
gsl_fft_complex_transform (data=0x44d4490, stride=1, n=1024, wavetable=0x1, work=0x1, sign=gsl_fft_backward) at c_main.c:86
86      c_main.c: No such file or directory.
        in c_main.c
(gdb) bt
#0  gsl_fft_complex_transform (data=0x44d4490, stride=1, n=1024, wavetable=0x1, work=0x1, sign=gsl_fft_backward) at c_main.c:86
#1  0x00007fba06437178 in gsl_fft_complex_inverse (data=0x44d4490, stride=1, n=1024, wavetable=0x1, work=0x1) at c_main.c:57
#2  0x00007fb9e64a6574 in __pyx_pf_4sage_3gsl_3fft_28FastFourierTransform_complex_inverse_transform (__pyx_v_self=0x44e8260, 
    unused=<value optimized out>) at sage/gsl/fft.c:2598
#3  0x00000000004966f4 in PyEval_EvalFrameEx (f=0x44d3df0, throwflag=<value optimized out>) at Python/ceval.c:3690
#4  0x00000000004979a1 in PyEval_EvalCodeEx (co=0x43e8a08, globals=<value optimized out>, locals=<value optimized out>, args=0x0, argcount=0, kws=0x0, 
    kwcount=0, defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:2968
#5  0x00000000004964ae in PyEval_EvalFrameEx (f=0x44c67d0, throwflag=<value optimized out>) at Python/ceval.c:522
#6  0x00000000004979a1 in PyEval_EvalCodeEx (co=0xac4a80, globals=<value optimized out>, locals=<value optimized out>, args=0x4403040, argcount=2, 
    kws=0x4403050, kwcount=0, defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:2968

```



---

Comment by lftabera created at 2013-03-06 12:05:51

Changing status from new to needs_review.


---

Comment by lftabera created at 2013-03-06 12:05:51

This is a duplicate of #10058


---

Comment by tscrim created at 2013-03-20 23:13:40

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-03-29 18:56:15

Resolution: duplicate
