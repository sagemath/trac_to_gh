# Issue 4346: segmentation fault with set_block

Issue created by migration from https://trac.sagemath.org/ticket/4346

Original creator: zimmerma

Original creation time: 2008-10-23 09:07:15

Assignee: was


```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.1.4, Release Date: 2008-10-16                       |
| Type notebook() for the GUI, and license() for information.        |
sage: M=Matrix([1])
sage: M.set_block(0,1,matrix([1]))


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

Attachment

The attached patch fixes the problem.  However, there are two additional issues, which should be addressed as new tickets.   

 1. After applying this patch and doctesting all sage, there are a bunch of failures in the modular abelian varieties code:

```
	sage -t  devel/sage-main/sage/modular/abvar/abvar_ambient_jacobian.py # 3 doctests failed
	sage -t  devel/sage-main/sage/modular/abvar/abvar_newform.py # 3 doctests failed
	sage -t  devel/sage-main/sage/modular/abvar/morphism.py # 3 doctests failed
	sage -t  devel/sage-main/sage/modular/abvar/homspace.py # 34 doctests failed
	sage -t  devel/sage-main/sage/modular/abvar/abvar.py # 11 doctests failed
```


These are because of bugs in that code exposed by doing proper bounds checking.
This is now trac #4351, and must also be fixed before #4346 can go into Sage.  

2. In this patch, matrix_window does *not* do bounds checking by default.  This is because there is a bunch of internal usage of matrix_window for strassen algorithms, which actually relies on matrix_window not being bounds checked (it's ok as used by those algorithms).  However, a bunch of code would have to be changed to make bounds checking of matrix_window the default.  That said it is currently easy (even with this patch) to segfault sage interactively:

```
sage: a = matrix([1]).matrix_window(1,1,1,1)
sage: a

Matrix window of size 1 x 1 at (1,1):
[1]
sage: a[0,0] = 1


------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------
```


This is now trac #4350.


---

Comment by was created at 2008-10-23 20:21:52

NOTE: There is an off-by-one mistake in this patch, which is addressed by the second patch to #4350.  Thus #4346 and #4350 should be refereed together.


---

Comment by was created at 2008-10-23 20:28:48

Also, the fixes in #4350 fix the non-issue that caused me to open #4351.


---

Comment by craigcitro created at 2008-10-23 22:31:49

Looks good, as long as you also apply the patches at #4350.


---

Comment by mabshoff created at 2008-10-26 02:26:02

Resolution: fixed


---

Comment by mabshoff created at 2008-10-26 02:26:02

Merged in Sage 3.2.alpha1
