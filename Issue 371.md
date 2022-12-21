# Issue 371: implement sage -t -gdb foo.py

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-05-19 15:20:59

Assignee: was

Make it so one can do 
   sage -t -gdb foo.py
and it runs the doctests under gdb.  Here's a hint:

```
Hi,

Several files break when doctesting them because of issues with libsingular
on OS X PPC.  Everything works fine on Linux and Intel PPC.   Basically
several files segfault only when being doctested.

I moved the .doctest_ring.py file to r.py, then made it always run
the doctests on load, then did "sage -gdb" followed by "import rings.r",
and was able to get a traceback:

155 tests in 89 items....

Program received signal EXC_BAD_ACCESS, Could not access memory.
Reason: KERN_PROTECTION_FAILURE at address: 0x00000004
0x09f04770 in __pyx_tp_dealloc_28multi_polynomial_libsingular_MPolynomial_libsingular
(o=0xc10f9b8) at
/Users/was/sage-sage-2.5.1.alpha1/local//include/singular/pInline2.h:412
412       r->p_Procs->p_Delete(p, r);
Current language:  auto; currently c++
(gdb)

Any ideas?
```



---

Comment by was created at 2007-08-19 06:59:28

Resolution: fixed
