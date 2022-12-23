# Issue 719: make pari.allocatemen() more clever

Issue created by migration from https://trac.sagemath.org/ticket/719

Original creator: mabshoff

Original creation time: 2007-09-20 20:39:36

Assignee: mabshoff

Doing the following 

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: pari.allocatemem()
Doubling the PARI stack.
sage: pari.allocatemem()
Doubling the PARI stack.
sage: pari.allocatemem()
Doubling the PARI stack.
sage: pari.allocatemem()
Doubling the PARI stack.
sage:
```

leads to 

```
==20507== 1,600,000,000 bytes in 1 blocks are still reachable in loss record 1,941 of 1,941
==20507==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)
==20507==    by 0xAA4BA6A: __pyx_f_3gen_init_stack (gen.c:25163)
==20507==    by 0xAA53894: __pyx_f_3gen_12PariInstance_ (gen.c:23106)
==20507==    by 0x483031: PyEval_EvalFrameEx (ceval.c:3564)
==20507==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==20507==    by 0x483CC4: PyEval_EvalFrameEx (ceval.c:494)
==20507==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==20507==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)
==20507==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==20507==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)
==20507==    by 0x48403A: PyEval_EvalFrameEx (ceval.c:3650)
==20507==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
```

You cannot get the memory back without restarting Sage. It also seems more than a little odd to start with 100,000,000 bytes. I would suggest something like 16MB (because that out to be enoughfor the casual user and if needed it would rapidly grown past the 100MB mark), double the amount of memory with each pari.allocatemen() up until you reach 0.5GB, and then increment by say 128MB. Bonus points for introducing an optional parameter to set the size for the libpari stack. Obviously documenting this behavior might also be a good idea.
| SAGE Version 2.8.4.2, Release Date: 2007-09-13                     |
| Type notebook() for the GUI, and license() for information.        |
Cheers,

Michael


---

Comment by was created at 2007-09-21 01:48:46

Resolution: wontfix


---

Comment by was created at 2007-09-21 01:48:46


```
no on #719.
[18:40] <mabshoff_> ok
[18:40] <william_stein> Lots of pari is unusable with < 100MB stack.
[18:40] <william_stein> And it's a *serious* pain to have to do it randomly in the middle of computations.
[18:40] <mabshoff_> really? That sucks.
[18:40] <william_stein> PARI doesn't automatically double the stack.
```



---

Comment by mabshoff created at 2007-10-03 17:26:41

Resolution changed from wontfix to 


---

Comment by mabshoff created at 2007-10-03 17:26:41

Changing status from closed to reopened.


---

Comment by mabshoff created at 2007-10-03 17:27:01

Resolution: fixed
