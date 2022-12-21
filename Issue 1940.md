# Issue 1940: Segmentation fault when comparing two empty ideals

Issue created by migration from Trac.

Original creator: SimonKing

Original creation time: 2008-01-26 15:40:43

Assignee: malb

The following three lines produce a segmentation fault.

```
sage: R=PolynomialRing(QQ,'x,y,z')
sage: I=R.ideal()
sage: I==R.ideal()
```


mabshoff gives the following information:
libSingular is not surprisingly  involved: 

```
(gdb) bt 
#0 
__pyx_pf_4sage_5rings_10polynomial_34multi_polynomial_ideal_libsingular_int­erred_libsingular 
( 
    __pyx_self=<value optimized out>, __pyx_v_I=0x2af2cff2eaf0) 
    at sage/rings/polynomial/multi_polynomial_ideal_libsingular.cpp: 
3059 
#1  0x0000000000484326 in PyEval_EvalFrameEx (f=0x1a6a310, 
throwflag=<value optimized out>) at Python/ceval.c:3552 
#2  0x000000000048403b in PyEval_EvalFrameEx (f=0x1a623a0, 
throwflag=<value optimized out>) at Python/ceval.c:3650 
#3  0x0000000000484f3b in PyEval_EvalCodeEx (co=0x2af2c2b2db70, 
globals=<value optimized out>, 
    locals=<value optimized out>, args=0x2af2cff25380, argcount=2, 
kws=0x0, kwcount=0, defs=0x0, defcount=0, closure=0x0) 
    at Python/ceval.c:2831 
#4  0x00000000004ce528 in function_call (func=0x2af2c2b36cf8, 
arg=0x2af2cff25368, kw=0x0) at Objects/funcobject.c:517 
#5  0x0000000000415523 in PyObject_Call (func=0x1a6b890, arg=0x1, 
kw=0x7fffefddfec0) at Objects/abstract.c:1860 
#6  0x000000000041bc43 in instancemethod_call (func=<value optimized 
out>, arg=0x2af2cff25368, kw=0x0) 
    at Objects/classobject.c:2497 
#7  0x0000000000415523 in PyObject_Call (func=0x1a6b890, arg=0x1, 
kw=0x7fffefddfec0) at Objects/abstract.c:1860 
#8  0x000000000047c851 in PyEval_CallObjectWithKeywords 
(func=0x2af2cf8c4320, arg=0x2af2cf8a5d50, kw=0x0) 
    at Python/ceval.c:3433 
```





---

Comment by mabshoff created at 2008-01-27 07:23:34

Changing priority from major to blocker.


---

Attachment


---

Comment by mabshoff created at 2008-01-27 20:27:00

Doctests are added for the segfault case, patch looks good to me.


---

Comment by mabshoff created at 2008-01-27 20:30:05

Merged in Sage 2.10.1.rc2


---

Comment by mabshoff created at 2008-01-27 20:30:05

Resolution: fixed
