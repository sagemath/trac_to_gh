# Issue 242: finite field arithmetic crash

Issue created by migration from https://trac.sagemath.org/ticket/242

Original creator: was

Original creation time: 2007-02-03 19:13:42

Assignee: somebody


```
Here's one which must be an incorrect boundary check:
 
----------------------------------------------------------------------
----------------------------------------------------------------------
 
sage: p = 2^32+15
sage: FF = FiniteField(p)
sage: a = FF(2)
sage: a^0
 
------------------------------------------------------------
Unhandled SIGBUS: A bus error occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
```



---

Comment by robertwb created at 2007-02-07 10:32:11

Resolution: fixed


---

Comment by robertwb created at 2007-02-07 10:32:11

mpz_init wasn't being called on new integermod_gmp objects. Fixed, see patch at 

http://sage.math.washington.edu/home/robertwb/patches/2007-02-06-modint_fix.diff
