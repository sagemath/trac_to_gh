# Issue 8580: Bug in coercing into a 0-dimensional qotient vector space

Issue created by migration from https://trac.sagemath.org/ticket/8580

Original creator: was

Original creation time: 2010-03-22 21:39:50

Assignee: was


```
wstein@boxen:~$ /usr/local/bin/sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: V = GF(2)^3
sage: (V/V)(V.0)
| Sage Version 4.3.4, Release Date: 2010-03-19                       |
| Type notebook() for the GUI, and license() for information.        |

------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------
```



---

Comment by was created at 2010-03-22 21:43:12

With GDB:

```
This GDB was configured as "x86_64-linux-gnu"...                             
[Thread debugging using libthread_db enabled]                                
Python 2.6.4 (r264:75706, Mar 20 2010, 18:30:21)                             
[GCC 4.2.4 (Ubuntu 4.2.4-1ubuntu4)] on linux2                                
Type "help", "copyright", "credits" or "license" for more information.       
[New Thread 0x7fd3670706e0 (LWP 623)]                                        
sage: V = GF(2)^3                                                            
sage: (V/V)(V.0)                                                             

Program received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0x7fd3670706e0 (LWP 623)]      
mzd_submatrix (S=0x41f5410, M=0x0, startrow=0, startcol=0, endrow=1, endcol=0) at src/packedmatrix.c:810
810     src/packedmatrix.c: No such file or directory.                                                  
        in src/packedmatrix.c                                                                           
(gdb)                                                                                                   
(gdb)                                                                                                   
(gdb) bt                                                                                                
#0  mzd_submatrix (S=0x41f5410, M=0x0, startrow=0, startcol=0, endrow=1, endcol=0)
    at src/packedmatrix.c:810
#1  0x00007fd3471bf48a in __pyx_pf_4sage_6matrix_17matrix_mod2_dense_17Matrix_mod2_dense_row (
    __pyx_v_self=0x7fd366ec82f8, __pyx_args=<value optimized out>, __pyx_kwds=<value optimized out>)
    at sage/matrix/matrix_mod2_dense.c:4478
#2  0x000000000041a27d in PyObject_Call (func=0x4308758, arg=0xe9c050, kw=0x0)
    at Objects/abstract.c:2492
#3  0x00007fd34a198f6f in __pyx_pf_4sage_6matrix_7matrix1_6Matrix_dense_rows (
    __pyx_v_self=0x7fd366ec82f8, __pyx_args=<value optimized out>, __pyx_kwds=<value optimized out>)
    at sage/matrix/matrix1.c:5524
#4  0x000000000041a27d in PyObject_Call (func=0x422dfc8, arg=0x7fd367030050, kw=0x4356d80)
    at Objects/abstract.c:2492
#5  0x00000000004907c6 in PyEval_CallObjectWithKeywords (func=0x422dfc8, arg=0x7fd367030050,
    kw=0x4356d80) at Python/ceval.c:3575
#6  0x00007fd34a19b316 in __pyx_pf_4sage_6matrix_7matrix1_6Matrix_rows (__pyx_v_self=0x7fd366ec82f8,
    __pyx_args=<value optimized out>, __pyx_kwds=<value optimized out>) at sage/matrix/matrix1.c:4990
#7  0x000000000041a27d in PyObject_Call (func=0x43087a0, arg=0x7fd367030050, kw=0x4356530)
    at Objects/abstract.c:2492
#8  0x00000000004907c6 in PyEval_CallObjectWithKeywords (func=0x43087a0, arg=0x7fd367030050,
    kw=0x4356530) at Python/ceval.c:3575
```



---

Comment by was created at 2010-03-22 21:43:24

Changing assignee from was to malb.


---

Attachment


---

Comment by malb created at 2010-03-22 23:12:02

Changing status from new to needs_review.


---

Comment by was created at 2010-03-29 23:49:14

Changing status from needs_review to positive_review.


---

Comment by was created at 2010-03-29 23:49:14

Looks good.  Thanks!


---

Comment by jhpalmieri created at 2010-04-16 18:48:42

Merged "vector_mod2_dense_zero.patch" in 4.4.alpha0


---

Comment by jhpalmieri created at 2010-04-16 18:48:42

Resolution: fixed
