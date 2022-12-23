# Issue 1374: segfault in coercion with matrices and ints

Issue created by migration from https://trac.sagemath.org/ticket/1374

Original creator: craigcitro

Original creation time: 2007-12-02 19:23:51

Assignee: somebody

This is the bug that was causing #1231; the fix there was easy, but as cwitty points out, the underlying bug is still there. It's something specifically to do with an entry becoming 0 in a matrix. I haven't looked into this at all; it's probably easy pickings for someone who knows the coercion code.

Here's a sample session:


```
sage: M = MatrixSpace(GF(5),2,2)

sage: A = M([1,0,0,1])

sage: A - int(-1)
 
[2 0]
[0 2]

sage: B = M([4,0,0,1])

sage: B - int(-1)


------------------------------------------------------------
Unhandled SIGBUS: A bus error occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------


```



---

Comment by craigcitro created at 2007-12-02 19:26:02

Changing assignee from somebody to robertwb.


---

Comment by craigcitro created at 2007-12-02 19:26:02

Changing component from basic arithmetic to coercion.


---

Comment by was created at 2007-12-02 19:32:51

First obvious thing to do (on sage.math):


```
sage: matrix(GF(5), 2, [4,0,0,1]) - int(-1)

Program received signal SIGSEGV, Segmentation fault.
[Switching to Thread 47703056093024 (LWP 5657)]
__pyx_f_4sage_5rings_11integer_mod_15NativeIntStruct_lookup (__pyx_v_self=0x2b62cd298e30, __pyx_v_value=5)
    at sage/rings/integer_mod.c:2750
2750      Py_INCREF(__pyx_1);
```



---

Comment by was created at 2007-12-02 21:20:02

Changing priority from major to critical.


---

Comment by was created at 2007-12-02 21:26:23

The problem is very likely related to this:


```
sage: matrix(GF(5),2, [4,0,0,1]).parent()(int(6))
[6 0]
[0 6]
```


This is over GF(5), so we should not see 6!


---

Comment by was created at 2007-12-02 21:27:30


```
sage: m = matrix(GF(5),2, [4,0,0,1])
sage: a = matrix(GF(5),2, [4,0,0,1]).parent()(int(7))
sage: m[1,1]
1
sage: a[1,1]
7
sage: m[1,1] - a[1,1]


------------------------------------------------------------
Unhandled SIGBUS: A bus error occured in SAGE.
```



---

Attachment


---

Comment by mabshoff created at 2007-12-02 21:37:37

Merged in 2.8.15.rc0.


---

Comment by mabshoff created at 2007-12-02 21:37:37

Resolution: fixed


---

Attachment


---

Comment by cwitty created at 2007-12-02 23:20:43

Resolution changed from fixed to 


---

Comment by cwitty created at 2007-12-02 23:20:43

Changing status from closed to reopened.


---

Comment by cwitty created at 2007-12-02 23:20:43

It's good that we don't crash any more; but maybe we should also give the right answer? :)

I think we also need to apply my 1374-part2.patch


---

Comment by mabshoff created at 2007-12-03 00:28:03

Merged cwitty's patch in 2.8.15.rc0. All doctests pass.

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-03 00:28:03

Resolution: fixed
