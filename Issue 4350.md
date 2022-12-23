# Issue 4350: matrix_window -- easy to segfault sage at command line

Issue created by migration from https://trac.sagemath.org/ticket/4350

Original creator: was

Original creation time: 2008-10-23 19:33:47

Assignee: was

See trac #4346 first and apply that patch.  

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



---

Attachment


---

Comment by was created at 2008-10-23 20:26:53

NOTE: In writing this patch, I discovered that there was an off-by-one bug in the patch for #4346, which is fixed here.  That was why the strassen code wasn't working.  Now by default everything uses bounds checking.  Very nice. 

Note: the bugs in modular abelian varieties homspaces (trac #4351) are also fixed.


---

Attachment


---

Comment by craigcitro created at 2008-10-23 22:33:28

Looks good. I've cleaned up a little bit of the code, and `cpdef`'d several of the functions in `sage/matrix/matrix_window.pyx`. I tested to see that this doesn't seem to slow down anything (such as matrix multiply), and now one can actually use the `matrix_window` class from the command line. (This is useful for debugging purposes in particular.)


---

Comment by mabshoff created at 2008-10-26 02:26:04

Merged all three patches in Sage 3.2.alpha1


---

Comment by mabshoff created at 2008-10-26 02:26:04

Resolution: fixed
