# Issue 4527: Exception in 'sage.matrix.matrix_integer_dense.Matrix_integer_dense._hnf_modn_impl'

Issue created by migration from https://trac.sagemath.org/ticket/4527

Original creator: syazdani

Original creation time: 2008-11-14 20:13:29

Assignee: tbd

Hi, 

the following code raises an exception that crashes sage on my computer:

```
cond=206
J=J0(206)
D=J.new_subvariety().decomposition()
Jp=J.old_subvariety(2)
Jpc=Jp.cuspidal_subgroup()
Ac=D[3].cuspidal_subgroup()
Ac.intersection(Jpc)
```


The error I get (running it through the notebook) is

```
          	

Exception  in
'sage.matrix.matrix_integer_dense.Matrix_integer_dense._hnf_modn_impl'
ignored


------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------

```


This seems very sensitive to the set of inputs, but it is consistent on my computer.
I'm running sage 3.1.4 (release date 2008-10-20), on mandriva, compiled with gcc 4.2.2 20071128.

Soroosh


---

Comment by mabshoff created at 2008-11-14 20:22:20

Changing keywords from "" to "segfault".


---

Comment by mabshoff created at 2008-11-14 20:22:20

I can reproduce this with the latest and greatest Sage. Gdb says:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/bin/sage-ipython
GNU gdb 6.4.90-debian
Copyright (C) 2006 Free Software Foundation, Inc.
GDB is free software, covered by the GNU General Public License, and you are
welcome to change it and/or distribute copies of it under certain conditions.
Type "show copying" to see the conditions.
There is absolutely no warranty for GDB.  Type "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu"...Using host libthread_db library "/lib/libthread_db.so.1".
| Sage Version 3.2.rc0, Release Date: 2008-11-10                     |
| Type notebook() for the GUI, and license() for information.        |
[Thread debugging using libthread_db enabled]
[New Thread 47755945320288 (LWP 13573)]
Python 2.5.2 (r252:60911, Nov 10 2008, 22:40:35) 
[GCC 4.1.2 20061115 (prerelease) (Debian 4.1.1-21)] on linux2
Type "help", "copyright", "credits" or "license" for more information.

sage: cond=206
sage: J=J0(206)
sage: D=J.new_subvariety().decomposition()
sage: Jp=J.old_subvariety(2)
sage: Jpc=Jp.cuspidal_subgroup()
sage: Ac=D[3].cuspidal_subgroup()
sage: Ac.intersection(Jpc)
Exception  in 'sage.matrix.matrix_integer_dense.Matrix_integer_dense._hnf_modn_impl' ignored

Program received signal SIGSEGV, Segmentation fault.
[Switching to Thread 47755945320288 (LWP 13573)]
0x00002b6f1c26f88d in __pyx_f_4sage_6matrix_20matrix_integer_dense_20Matrix_integer_dense__hnf_modn (
    __pyx_v_self=0x2b6f2485a560, __pyx_v_res=0x2b6f2485a830, __pyx_v_det=<value optimized out>)
    at sage/matrix/matrix_integer_dense.c:26964
26964	      mpz_init_set_si(((__pyx_v_res->_matrix[__pyx_v_i])[__pyx_v_j]), (__pyx_v_res_l[__pyx_v_k]));
(gdb) bt
#0  0x00002b6f1c26f88d in __pyx_f_4sage_6matrix_20matrix_integer_dense_20Matrix_integer_dense__hnf_modn (
    __pyx_v_self=0x2b6f2485a560, __pyx_v_res=0x2b6f2485a830, __pyx_v_det=<value optimized out>)
    at sage/matrix/matrix_integer_dense.c:26964
#1  0x00002b6f1c2ac2e7 in __pyx_pf_4sage_6matrix_20matrix_integer_dense_20Matrix_integer_dense__hnf_mod (
    __pyx_v_self=0x2b6f2485a560, __pyx_v_D=0x7451450) at sage/matrix/matrix_integer_dense.c:26853
#2  0x0000000000484afc in PyEval_EvalFrameEx (f=0xd7283d0, throwflag=<value optimized out>) at Python/ceval.c:3561
#3  0x0000000000486182 in PyEval_EvalCodeEx (co=0x2b6f0cf973f0, globals=<value optimized out>, 
    locals=<value optimized out>, args=0x2b6f11211d80, argcount=1, kws=0xd770a78, kwcount=1, defs=0x0, defcount=0, 
    closure=0x0) at Python/ceval.c:2836
#4  0x0000000000484347 in PyEval_EvalFrameEx (f=0xd770810, throwflag=<value optimized out>) at Python/ceval.c:3669
#5  0x0000000000486182 in PyEval_EvalCodeEx (co=0x2b6f0c8afe40, globals=<value optimized out>, 
    locals=<value optimized out>, args=0x2b6f11211d80, argcount=1, kws=0xd6fd708, kwcount=2, defs=0x0, defcount=0, 
    closure=0x0) at Python/ceval.c:2836
<SNIP>
```


I am running the computation under valgrind now if it catches anything.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-14 20:22:20

Changing assignee from tbd to craigcitro.


---

Comment by mabshoff created at 2008-11-14 20:22:20

Changing component from algebra to modular forms.


---

Comment by was created at 2008-11-15 01:32:10

this should fix it.  the main bug was an off by a factor of two overflow.


---

Attachment


---

Comment by mabshoff created at 2008-11-15 07:22:44

With the patch applied:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.rc1$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| Sage Version 3.2.rc0, Release Date: 2008-11-10                     |
| Type notebook() for the GUI, and license() for information.        |
sage: cond=206
sage: J=J0(206)
sage: D=J.new_subvariety().decomposition()
sage: Jp=J.old_subvariety(2)
sage: Jpc=Jp.cuspidal_subgroup()
sage: Ac=D[3].cuspidal_subgroup()
sage: Ac.intersection(Jpc)
Finite subgroup with invariants [] over QQ of Simple abelian subvariety 206d(1,206) of dimension 4 of J0(206)
```

I am currently running doctests.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-15 07:47:03

With the patch applied doctests with "-long" pass. Note that the example posted that exposes the problem takes about 30 seconds CPU time, so we should add it as a "#long time" example unless someone comes up with a shorter one.

Cheers,

Michael


---

Attachment

Looks good. I added a doctest based on Soroosh's original example in the extra patch above.


---

Comment by mabshoff created at 2008-11-15 09:52:46

Merged in Sage 3.2.rc1


---

Comment by mabshoff created at 2008-11-15 09:52:46

Resolution: fixed
