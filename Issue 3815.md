# Issue 3815: plot3d segfaults

Issue created by migration from https://trac.sagemath.org/ticket/3815

Original creator: wdj

Original creation time: 2008-08-12 12:38:45

Assignee: was

This was reported by Adrian:

I tried the following, and it did not work


```
x,y=var('x y')
def myarctan(x,y):
    if x>=0 and y>=0:
        return arctan(abs(y/x))
    if x<0 and y>=0:
        return pi-arctan(abs(y/x))
    if x<0 and y<0:
        return pi+arctan(abs(y/x))
    if x>=0 and y<0:
        return 2*pi-arctan(abs(y/x))
plot3d(myarctan(x,y),(x,-3,3),(y,-3,3))
```


However, the following does work:


```
plot3d(myarctan,(-3,3),(-3,3))
```


I guess both should work, so I guess this is a bug.

+++++++++++++++++++++++++++++++++++++++++++++++++

Reply by wdj:

Didn't work for me. I got a segfault:



```
sage: plot3d(myarctan(x,y),(-3,3),(-3,3))


------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------
```


This is not a division by zero problem either:


```
sage: plot3d(myarctan(x,y),(0.1,0.3),(0.1,0.3))


------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------
```


Strange. If you use


```
x,y=var('x, y')
def myarctan(u,v):
  if u>=0.0 and v>=0.0:
      return RR(arctan(abs(v/u)))
  if u<0.0 and v>=0.0:
      return RR(pi-arctan(abs(v/u)))
  if u<0.0 and v<0.0:
      return RR(pi+arctan(abs(v/u)))
  if u>=0.0 and v<0.0:
      return RR(2*pi-arctan(abs(v/u)))
  #return 0.0
```

you get a segfault (I'm using the command line, amd64 hardy heron machine).
However, if you uncomment the last line you don't get a segfault but
the 0 function is plotted.

I'm marking it as a blocker since it is a segfault. Hope that is not the wrong thing to do.





---

Comment by was created at 2008-08-12 13:32:11

The traceback

```

sage: plot3d(myarctan(x,y),(-3,3),(-3,3))

Program received signal SIGSEGV, Segmentation fault.
[Switching to Thread 47023105785696 (LWP 31014)]
0x00002ac46b67af74 in memcpy () from /lib/libc.so.6
(gdb) bt
#0  0x00002ac46b67af74 in memcpy () from /lib/libc.so.6
#1  0x00002ac46e7429a2 in __pyx_f_4sage_3ext_9fast_eval_binop (
   __pyx_v__left=<value optimized out>, __pyx_v__right=0x621b20,
__pyx_v_type=5 '\005')
   at sage/ext/fast_eval.c:6669
#2  0x00002ac46e745e1e in
__pyx_pf_4sage_3ext_9fast_eval_14FastDoubleFunc___add__ (
   __pyx_v_left=0x2ac482a1a380, __pyx_v_right=0x517000) at
sage/ext/fast_eval.c:4505
#3  0x0000000000415aed in binary_op1 (v=0x411556, w=0x517000, op_slot=0)
   at Objects/abstract.c:398
#4  0x0000000000415fb0 in PyNumber_Add (v=0x2ac482a1a380, w=0x517000)
   at Objects/abstract.c:638
#5  0x0000000000479c73 in builtin_sum (self=<value optimized out>,
   args=<value optimized out>) at Python/bltinmodule.c:2051
#6  0x0000000000484217 in PyEval_EvalFrameEx (f=0x1de47d0,
   throwflag=<value optimized out>) at Python/ceval.c:3573
#7  0x0000000000486182 in PyEval_EvalCodeEx (co=0x2ac47f4ce8a0,
   globals=<value optimized out>, locals=<value optimized out>,
args=0x1bdf378,
   argcount=2, kws=0x1bdf388, kwcount=0, defs=0x2ac47f4c9ca8,
defcount=1, closure=0x0)
   at Python/ceval.c:2836
#8  0x0000000000484347 in PyEval_EvalFrameEx (f=0x1bdf190,
   throwflag=<value optimized out>) at Python/ceval.c:3669
#9  0x0000000000486182 in PyEval_EvalCodeEx (co=0x2ac47f4ce738,
   globals=<value optimized out>, locals=<value optimized out>,
args=0x2ac46b0ca6f0,

```



---

Comment by cwitty created at 2008-08-12 13:50:29

Here's a simpler test case:

```
sage: from sage.ext.fast_eval import fast_float_arg, fast_float
sage: fast_float_arg(0)+None
```


This is because of one of these bugs in fast_float:
"When you declare a parameter or C variable as being of an extension
type, Pyrex will allow it to take on the value None as well as values
of its declared type. This is analogous to the way a C pointer can
take on the value NULL, and you need to exercise the same caution
because of it."
(The above is from the Pyrex manual.)


---

Attachment


---

Comment by wdj created at 2008-08-13 12:39:11

This applied cleanly to sage-3.1.alpha1. I tried the code Adrian gave which caused a segfault for me. This nasty segfault does not occur with this patch, instead triggering a traceback with a message about fastfloat. Also, this patch passed sage -testall except for one (unrelated?) failure:


```
sage -t  devel/sage/sage/modular/modsym/tests.py            **********************************************************************
File "/home/wdj/sagefiles/sage-3.1.alpha1/tmp/tests.py", line 223:
    sage: sage.modular.modsym.tests.Test().test('csnew_dimension',seconds=1)
Exception raised:
    Traceback (most recent call last):
      File "/home/wdj/sagefiles/sage-3.1.alpha1/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_11[2]>", line 1, in <module>
        sage.modular.modsym.tests.Test().test('csnew_dimension',seconds=Integer(1))###line 223:
    sage: sage.modular.modsym.tests.Test().test('csnew_dimension',seconds=1)
      File "/home/wdj/sagefiles/sage-3.1.alpha1/local/lib/python2.5/site-packages/sage/modular/modsym/tests.py", line 235, in test
        self._do(name)
      File "/home/wdj/sagefiles/sage-3.1.alpha1/local/lib/python2.5/site-packages/sage/modular/modsym/tests.py", line 196, in _do
        Test.__dict__["test_%s"%name](self)
      File "/home/wdj/sagefiles/sage-3.1.alpha1/local/lib/python2.5/site-packages/sage/modular/modsym/tests.py", line 264, in test_csnew_dimension
        V = M.cuspidal_submodule().new_submodule()
      File "/home/wdj/sagefiles/sage-3.1.alpha1/local/lib/python2.5/site-packages/sage/modular/modsym/ambient.py", line 896, in cuspidal_submodule
        assert d == S.dimension(), "According to dimension formulas the cuspidal subspace of \"%s\" has dimension %s; however, computing it using modular symbols we obtained %s, so there is a bug (please report!)."%(self, d, S.dimension())
    AssertionError: According to dimension formulas the cuspidal subspace of "Modular Symbols space of dimension 6 and level 12, weight 4, character [-1, -1], sign 1, over Rational Field" has dimension 4; however, computing it using modular symbols we obtained 2, so there is a bug (please report!).
```


This is hard to reproduce. Out of 10 tries, I only caught this failure 2 times.

In any case, I think Robert Bradshaw may be working on another patch for this, so maybe this report isn't needed. I just wanted to report that the segfault definitely is fixed with this patch on my machine (amd64, hardy heron).


---

Comment by mabshoff created at 2008-08-15 10:05:13

Positive review from me. If anybody wants to do a cleaner long term solution feel free to open another ticket.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-15 10:11:36

Resolution: fixed


---

Comment by mabshoff created at 2008-08-15 10:11:36

Merged in Sage 3.1.rc0
