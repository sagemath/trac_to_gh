# Issue 3984: Sage 3.1.2.alpha1 - Linux Itanium - segfaults in chmm.pyx and hmm.pyx

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-08-29 01:10:45

Assignee: mabshoff

CC:  bober

On Iras:

```
mabshoff`@`iras:~/build-3.1.2.alpha2/sage-3.1.2.alpha1-iras-gcc-4.3.1> ./sage -t -long devel/sage/sage/stats/hmm/chmm.pyx
sage -t -long devel/sage/sage/stats/hmm/chmm.pyx            

------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------


A mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.
         [4.4 s]
exit code: 768
 
----------------------------------------------------------------------
The following tests failed:


        sage -t -long devel/sage/sage/stats/hmm/chmm.pyx
Total time for all tests: 4.4 seconds
mabshoff`@`iras:~/build-3.1.2.alpha2/sage-3.1.2.alpha1-iras-gcc-4.3.1> ./sage -t -long devel/sage/sage/stats/hmm/hmm.pyx
sage -t -long devel/sage/sage/stats/hmm/hmm.pyx             

------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------


A mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.
         [3.0 s]
exit code: 768
 
----------------------------------------------------------------------
The following tests failed:


        sage -t -long devel/sage/sage/stats/hmm/hmm.pyx
Total time for all tests: 3.0 seconds
mabshoff`@`iras:~/build-3.1.2.alpha2/sage-3.1.2.alpha1-iras-gcc-4.3.1> 
```


All other doctests for 3.1.2.alpha1 pass on that box.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-29 01:14:54

For chmm.pyx with verbose:

```
Trying:
    m = hmm.GaussianHiddenMarkovModel([[RealNumber('0.4'),RealNumber('0.6')],[RealNumber('0.1'),RealNumber('0.9')]], [(RealNumber('0.0'),RealNumber('1.0')),(Integer(1),Integer(1))], [Integer(1),Integer(2)], "Test 1", normalize=False)###line 306:_sage_    >>> m = hmm.GaussianHiddenMarkovModel([[0.4,0.6],[0.1,0.9]], [(0.0,1.0),(1,1)], [1,2], "Test 1", normalize=False)
Expecting nothing


------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------
```

and gdb says:

```
Program received signal SIGSEGV, Segmentation fault.
[Switching to Thread 2305843009213933088 (LWP 29739)]
__pyx_pf_4sage_5stats_3hmm_4chmm_25GaussianHiddenMarkovModel__initialize_state (__pyx_v_self=<value optimized out>, __pyx_v_pi=0x200000000d6e9998) at sage/stats/hmm/chmm.c:2748
2748          ((__pyx_v_state->out_a[0])[__pyx_v_j]) = __pyx_6;
(gdb) bt
#0  __pyx_pf_4sage_5stats_3hmm_4chmm_25GaussianHiddenMarkovModel__initialize_state (__pyx_v_self=<value optimized out>, __pyx_v_pi=0x200000000d6e9998) at sage/stats/hmm/chmm.c:2748
#1  0x4000000000215400 in PyCFunction_Call (func=<value optimized out>, arg=0x200000000b73d390, kw=0x0) at Objects/methodobject.c:82
#2  0x400000000001fe10 in PyObject_Call (func=0x200000000db0b0a8, arg=0x200000000b73d390, kw=0x0) at Objects/abstract.c:1861
#3  0x200000000d9113a0 in __pyx_pf_4sage_5stats_3hmm_4chmm_25GaussianHiddenMarkovModel___init__ (__pyx_v_self=0x200000000db0b0a8, __pyx_args=<value optimized out>, __pyx_kwds=<value optimized out>) at sage/stats/hmm/chmm.c:2369
#4  0x40000000000fb730 in type_call (type=0x200000000d94a4e8, args=0x200000000b73d390, kwds=0x200000000d6f7518) at Objects/typeobject.c:436
#5  0x400000000001fe10 in PyObject_Call (func=0x200000000d94a4e8, arg=0x200000000047fe10, kw=0x60000000016f73d0) at Objects/abstract.c:1861
#6  0x4000000000153610 in PyEval_EvalFrameEx (f=0x60000000017140a0, throwflag=<value optimized out>) at Python/ceval.c:3784
#7  0x4000000000158be0 in PyEval_EvalCodeEx (co=<value optimized out>, globals=0x60000000019f4340, locals=<value optimized out>, args=0x0, argcount=<value optimized out>, kws=0x0, kwcount=0, defs=0x0, defcount=Cannot access memory at address 0x1
) at Python/ceval.c:2836
#8  0x40000000001541f0 in PyEval_EvalFrameEx (f=0x60000000016f69b0, throwflag=<value optimized out>) at Python/ceval.c:494
#9  0x4000000000158be0 in PyEval_EvalCodeEx (co=<value optimized out>, globals=0x20, locals=<value optimized out>, args=0x60000000018ea780, argcount=<value optimized out>, kws=0x60000000018ea7b0, kwcount=0, defs=0x0, defcount=Cannot access memory at address 0x1
) at Python/ceval.c:2836
#10 0x4000000000155620 in PyEval_EvalFrameEx (f=0x60000000018ea5d0, throwflag=<value optimized out>) at Python/ceval.c:3669
#11 0x4000000000158be0 in PyEval_EvalCodeEx (co=<value optimized out>, globals=0x10, locals=<value optimized out>, args=0x60000000000c9310, argcount=<value optimized out>, kws=0x60000000000c9330, kwcount=0, defs=0x20000000018c5c60, defcount=Cannot access memory at address 0x1
)
    at Python/ceval.c:2836
#12 0x4000000000154ba0 in PyEval_EvalFrameEx (f=0x60000000000c9130, throwflag=<value optimized out>) at Python/ceval.c:3669
#13 0x4000000000158be0 in PyEval_EvalCodeEx (co=<value optimized out>, globals=0x20000000005108a0, locals=<value optimized out>, args=0x600000000006f630, argcount=<value optimized out>, kws=0x60000000000bd9d8, kwcount=3, defs=0x200000000188ceb0, defcount=Cannot access memory at address 0x1
)
    at Python/ceval.c:2836
#14 0x4000000000154ba0 in PyEval_EvalFrameEx (f=0x60000000000bd810, throwflag=<value optimized out>) at Python/ceval.c:3669
#15 0x4000000000158be0 in PyEval_EvalCodeEx (co=<value optimized out>, globals=0x600000000006f630, locals=<value optimized out>, args=0x0, argcount=<value optimized out>, kws=0x0, kwcount=0, defs=0x0, defcount=Cannot access memory at address 0x1
) at Python/ceval.c:2836
#16 0x4000000000158eb0 in PyEval_EvalCode (co=0x2000000000518300, globals=0x600000000006f630, locals=0x600000000006f630) at Python/ceval.c:494
#17 0x40000000001a5af0 in PyRun_FileExFlags (fp=<value optimized out>, filename=0x607ffffffeeb276c "/home/mabshoff/build-3.1.2.alpha2/sage-3.1.2.alpha1-iras-gcc-4.3.1/tmp/.doctest_chmm.py", start=<value optimized out>, globals=0x600000000006f630, 
    locals=0x600000000006f630, closeit=1, flags=0x607ffffffeeb1f70) at Python/pythonrun.c:1273
#18 0x40000000001a62e0 in PyRun_SimpleFileExFlags (fp=0x600000000004c010, filename=0x607ffffffeeb276c "/home/mabshoff/build-3.1.2.alpha2/sage-3.1.2.alpha1-iras-gcc-4.3.1/tmp/.doctest_chmm.py", closeit=1, flags=0x607ffffffeeb1f70) at Python/pythonrun.c:879
#19 0x4000000000016060 in Py_Main (argc=2, argv=0x607ffffffeeb22a8) at Modules/main.c:523
#20 0x4000000000014350 in main (argc=2, argv=0x607ffffffeeb22a8) at ./Modules/python.c:23
```




hmm.pyx on the other side:

```
Trying:
    a.viterbi([Integer(1),Integer(0),Integer(0),Integer(1),Integer(0),Integer(0),Integer(1),Integer(1)])###line 678:_sage_    >>> a.viterbi([1,0,0,1,0,0,1,1])
Expecting:
    ([1, 0, 0, 1, 1, 0, 1, 1], -11.062453224772216)


------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------
```

and gdb says:

```
Program received signal SIGSEGV, Segmentation fault.
[Switching to Thread 2305843009213933088 (LWP 29797)]
__pyx_pf_4sage_5stats_3hmm_3hmm_25DiscreteHiddenMarkovModel_viterbi (__pyx_v_self=<value optimized out>, __pyx_v_seq=0x200000000dac9f38) at sage/stats/hmm/hmm.c:5310
5310        __pyx_4 = PyInt_FromLong((__pyx_v_path[__pyx_8])); if (unlikely(!__pyx_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 702; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
(gdb) bt
#0  __pyx_pf_4sage_5stats_3hmm_3hmm_25DiscreteHiddenMarkovModel_viterbi (__pyx_v_self=<value optimized out>, __pyx_v_seq=0x200000000dac9f38) at sage/stats/hmm/hmm.c:5310
#1  0x4000000000154950 in PyEval_EvalFrameEx (f=0x600000000172cec0, throwflag=<value optimized out>) at Python/ceval.c:3561
#2  0x4000000000158be0 in PyEval_EvalCodeEx (co=<value optimized out>, globals=0x60000000018a78a0, locals=<value optimized out>, args=0x0, argcount=<value optimized out>, kws=0x0, kwcount=0, defs=0x0, defcount=143, closure=0xc0f005800c212018)
    at Python/ceval.c:2836
#3  0x40000000001541f0 in PyEval_EvalFrameEx (f=0x600000000171b9f0, throwflag=<value optimized out>) at Python/ceval.c:494
#4  0x4000000000158be0 in PyEval_EvalCodeEx (co=<value optimized out>, globals=0x20, locals=<value optimized out>, args=0x6000000001993ea0, argcount=<value optimized out>, kws=0x6000000001993ed0, kwcount=0, defs=0x0, defcount=143, closure=0xc0f005800c212018)
    at Python/ceval.c:2836
#5  0x4000000000155620 in PyEval_EvalFrameEx (f=0x6000000001993cf0, throwflag=<value optimized out>) at Python/ceval.c:3669
#6  0x4000000000158be0 in PyEval_EvalCodeEx (co=<value optimized out>, globals=0x10, locals=<value optimized out>, args=0x60000000000cd980, argcount=<value optimized out>, kws=0x60000000000cd9a0, kwcount=0, defs=0x20000000018b5c60, defcount=143, 
    closure=0xc0f005800c212018) at Python/ceval.c:2836
#7  0x4000000000154ba0 in PyEval_EvalFrameEx (f=0x60000000000cd7a0, throwflag=<value optimized out>) at Python/ceval.c:3669
#8  0x4000000000158be0 in PyEval_EvalCodeEx (co=<value optimized out>, globals=0x20000000005108a0, locals=<value optimized out>, args=0x600000000006f630, argcount=<value optimized out>, kws=0x60000000000bd9d8, kwcount=3, defs=0x2000000001885bb0, defcount=143, 
    closure=0xc0f005800c212018) at Python/ceval.c:2836
#9  0x4000000000154ba0 in PyEval_EvalFrameEx (f=0x60000000000bd810, throwflag=<value optimized out>) at Python/ceval.c:3669
#10 0x4000000000158be0 in PyEval_EvalCodeEx (co=<value optimized out>, globals=0x600000000006f630, locals=<value optimized out>, args=0x0, argcount=<value optimized out>, kws=0x0, kwcount=0, defs=0x0, defcount=143, closure=0xc0f005800c212018)
    at Python/ceval.c:2836
#11 0x4000000000158eb0 in PyEval_EvalCode (co=0x20000000005160a8, globals=0x600000000006f630, locals=0x600000000006f630) at Python/ceval.c:494
#12 0x40000000001a5af0 in PyRun_FileExFlags (fp=<value optimized out>, filename=0x607ffffffef9e76d "/home/mabshoff/build-3.1.2.alpha2/sage-3.1.2.alpha1-iras-gcc-4.3.1/tmp/.doctest_hmm.py", start=<value optimized out>, globals=0x600000000006f630, 
    locals=0x600000000006f630, closeit=1, flags=0x607ffffffef9df70) at Python/pythonrun.c:1273
#13 0x40000000001a62e0 in PyRun_SimpleFileExFlags (fp=0x600000000004c010, filename=0x607ffffffef9e76d "/home/mabshoff/build-3.1.2.alpha2/sage-3.1.2.alpha1-iras-gcc-4.3.1/tmp/.doctest_hmm.py", closeit=1, flags=0x607ffffffef9df70) at Python/pythonrun.c:879
#14 0x4000000000016060 in Py_Main (argc=2, argv=0x607ffffffef9e2a8) at Modules/main.c:523
#15 0x4000000000014350 in main (argc=2, argv=0x607ffffffef9e2a8) at ./Modules/python.c:23
```


I will poke around with valgrind on an x86-64 box to see if it picks up anything before actually looking at the code.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-29 07:10:31

Here are some issues picked up by valgrind in chmm.pyx:

```
==26797== Invalid write of size 1
==26797==    at 0x4A1E100: strcpy (mc_replace_strmem.c:268)
==26797==    by 0x1EDDAFE1: __pyx_pf_4sage_5stats_3hmm_4chmm_27ContinuousHiddenMarkovModel___init__ (chmm.c:2127)
==26797==    by 0x459350: type_call (typeobject.c:436)
==26797==    by 0x415832: PyObject_Call (abstract.c:1861)
==26797==    by 0x482DB9: PyEval_EvalFrameEx (ceval.c:3784)
==26797==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==26797==    by 0x484AF1: PyEval_EvalFrameEx (ceval.c:494)
==26797==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==26797==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==26797==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==26797==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==26797==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==26797==  Address 0x77d4b0d is 0 bytes after a block of size 5 alloc'd
==26797==    at 0x4A1BDEB: malloc (vg_replace_malloc.c:207)
==26797==    by 0x1EDDAE1D: __pyx_pf_4sage_5stats_3hmm_4chmm_27ContinuousHiddenMarkovModel___init__ (chmm.c:1943)
==26797==    by 0x459350: type_call (typeobject.c:436)
==26797==    by 0x415832: PyObject_Call (abstract.c:1861)
==26797==    by 0x482DB9: PyEval_EvalFrameEx (ceval.c:3784)
==26797==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==26797==    by 0x484AF1: PyEval_EvalFrameEx (ceval.c:494)
==26797==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==26797==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==26797==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==26797==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==26797==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)

==26797== Invalid write of size 1
==26797==    at 0x4A1E100: strcpy (mc_replace_strmem.c:268)
==26797==    by 0x1EDDAFE1: __pyx_pf_4sage_5stats_3hmm_4chmm_27ContinuousHiddenMarkovModel___init__ (chmm.c:2127)
==26797==    by 0x45402B: wrap_init (typeobject.c:4043)
==26797==    by 0x415832: PyObject_Call (abstract.c:1861)
==26797==    by 0x47D750: PyEval_CallObjectWithKeywords (ceval.c:3442)
==26797==    by 0x4CC304: wrapperdescr_call (descrobject.c:304)
==26797==    by 0x415832: PyObject_Call (abstract.c:1861)
==26797==    by 0x47D750: PyEval_CallObjectWithKeywords (ceval.c:3442)
==26797==    by 0x1EDD736C: __pyx_pf_4sage_5stats_3hmm_4chmm_25GaussianHiddenMarkovModel___init__ (chmm.c:2307)
==26797==    by 0x459350: type_call (typeobject.c:436)
==26797==    by 0x415832: PyObject_Call (abstract.c:1861)
==26797==    by 0x482DB9: PyEval_EvalFrameEx (ceval.c:3784)
==26797==  Address 0x598b686 is 0 bytes after a block of size 6 alloc'd
==26797==    at 0x4A1BDEB: malloc (vg_replace_malloc.c:207)
==26797==    by 0x1EDDAE1D: __pyx_pf_4sage_5stats_3hmm_4chmm_27ContinuousHiddenMarkovModel___init__ (chmm.c:1943)
==26797==    by 0x45402B: wrap_init (typeobject.c:4043)
==26797==    by 0x415832: PyObject_Call (abstract.c:1861)
==26797==    by 0x47D750: PyEval_CallObjectWithKeywords (ceval.c:3442)
==26797==    by 0x4CC304: wrapperdescr_call (descrobject.c:304)
==26797==    by 0x415832: PyObject_Call (abstract.c:1861)
==26797==    by 0x47D750: PyEval_CallObjectWithKeywords (ceval.c:3442)
==26797==    by 0x1EDD736C: __pyx_pf_4sage_5stats_3hmm_4chmm_25GaussianHiddenMarkovModel___init__ (chmm.c:2307)
==26797==    by 0x459350: type_call (typeobject.c:436)
==26797==    by 0x415832: PyObject_Call (abstract.c:1861)
==26797==    by 0x482DB9: PyEval_EvalFrameEx (ceval.c:3784)

==26797== Invalid read of size 1
==26797==    at 0x4A1CDA3: strlen (mc_replace_strmem.c:242)
==26797==    by 0x44DACA: PyString_FromString (stringobject.c:108)
==26797==    by 0x1EDD644A: __pyx_pf_4sage_5stats_3hmm_4chmm_27ContinuousHiddenMarkovModel_name (chmm.c:2191)
==26797==    by 0x415832: PyObject_Call (abstract.c:1861)
==26797==    by 0x1EDD6DFC: __pyx_pf_4sage_5stats_3hmm_4chmm_25GaussianHiddenMarkovModel___reduce__ (chmm.c:2899)
==26797==    by 0x415832: PyObject_Call (abstract.c:1861)
==26797==    by 0x47D750: PyEval_CallObjectWithKeywords (ceval.c:3442)
==26797==    by 0x458C0F: object_reduce_ex (typeobject.c:2867)
==26797==    by 0x415832: PyObject_Call (abstract.c:1861)
==26797==    by 0x7DE9723: save (cPickle.c:2498)
==26797==    by 0x7DEB587: cpm_dumps (cPickle.c:2580)
==26797==    by 0x415832: PyObject_Call (abstract.c:1861)
==26797==  Address 0x123ea484 is 0 bytes after a block of size 4 alloc'd
==26797==    at 0x4A1BDEB: malloc (vg_replace_malloc.c:207)
==26797==    by 0x1EDDAE1D: __pyx_pf_4sage_5stats_3hmm_4chmm_27ContinuousHiddenMarkovModel___init__ (chmm.c:1943)
==26797==    by 0x45402B: wrap_init (typeobject.c:4043)
==26797==    by 0x415832: PyObject_Call (abstract.c:1861)
==26797==    by 0x47D750: PyEval_CallObjectWithKeywords (ceval.c:3442)
==26797==    by 0x4CC304: wrapperdescr_call (descrobject.c:304)
==26797==    by 0x415832: PyObject_Call (abstract.c:1861)
==26797==    by 0x47D750: PyEval_CallObjectWithKeywords (ceval.c:3442)
==26797==    by 0x1EDD736C: __pyx_pf_4sage_5stats_3hmm_4chmm_25GaussianHiddenMarkovModel___init__ (chmm.c:2307)
==26797==    by 0x459350: type_call (typeobject.c:436)
==26797==    by 0x415832: PyObject_Call (abstract.c:1861)
==26797==    by 0x482DB9: PyEval_EvalFrameEx (ceval.c:3784)

==26797== Invalid read of size 1
==26797==    at 0x4A1CDA3: strlen (mc_replace_strmem.c:242)
==26797==    by 0x44DACA: PyString_FromString (stringobject.c:108)
==26797==    by 0x1EDD7992: __pyx_pf_4sage_5stats_3hmm_4chmm_25GaussianHiddenMarkovModel___repr__ (chmm.c:3548)
==26797==    by 0x443669: PyObject_Repr (object.c:361)
==26797==    by 0x429ECB: PyFile_WriteObject (fileobject.c:2195)
==26797==    by 0x4AD248: sys_displayhook (sysmodule.c:114)
==26797==    by 0x415832: PyObject_Call (abstract.c:1861)
==26797==    by 0x47D750: PyEval_CallObjectWithKeywords (ceval.c:3442)
==26797==    by 0x483599: PyEval_EvalFrameEx (ceval.c:1531)
==26797==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==26797==    by 0x484AF1: PyEval_EvalFrameEx (ceval.c:494)
==26797==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==26797==  Address 0x57ddd8c is 0 bytes after a block of size 4 alloc'd
==26797==    at 0x4A1BDEB: malloc (vg_replace_malloc.c:207)
==26797==    by 0x1EDDAE1D: __pyx_pf_4sage_5stats_3hmm_4chmm_27ContinuousHiddenMarkovModel___init__ (chmm.c:1943)
==26797==    by 0x45402B: wrap_init (typeobject.c:4043)
==26797==    by 0x415832: PyObject_Call (abstract.c:1861)
==26797==    by 0x47D750: PyEval_CallObjectWithKeywords (ceval.c:3442)
==26797==    by 0x4CC304: wrapperdescr_call (descrobject.c:304)
==26797==    by 0x415832: PyObject_Call (abstract.c:1861)
==26797==    by 0x47D750: PyEval_CallObjectWithKeywords (ceval.c:3442)
==26797==    by 0x1EDD736C: __pyx_pf_4sage_5stats_3hmm_4chmm_25GaussianHiddenMarkovModel___init__ (chmm.c:2307)
==26797==    by 0x459350: type_call (typeobject.c:436)
==26797==    by 0x415832: PyObject_Call (abstract.c:1861)
==26797==    by 0x1EDD5E62: __pyx_pf_4sage_5stats_3hmm_4chmm_unpickle_gaussian_hmm_v0 (chmm.c:5465)

==26797== Invalid read of size 1
==26797==    at 0x4A1DEF8: memcpy (mc_replace_strmem.c:402)
==26797==    by 0x44DB39: PyString_FromString (stringobject.c:136)
==26797==    by 0x1EDD7992: __pyx_pf_4sage_5stats_3hmm_4chmm_25GaussianHiddenMarkovModel___repr__ (chmm.c:3548)
==26797==    by 0x443669: PyObject_Repr (object.c:361)
==26797==    by 0x429ECB: PyFile_WriteObject (fileobject.c:2195)
==26797==    by 0x4AD248: sys_displayhook (sysmodule.c:114)
==26797==    by 0x415832: PyObject_Call (abstract.c:1861)
==26797==    by 0x47D750: PyEval_CallObjectWithKeywords (ceval.c:3442)
==26797==    by 0x483599: PyEval_EvalFrameEx (ceval.c:1531)
==26797==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==26797==    by 0x484AF1: PyEval_EvalFrameEx (ceval.c:494)
==26797==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==26797==  Address 0x57ddd8c is 0 bytes after a block of size 4 alloc'd
==26797==    at 0x4A1BDEB: malloc (vg_replace_malloc.c:207)
==26797==    by 0x1EDDAE1D: __pyx_pf_4sage_5stats_3hmm_4chmm_27ContinuousHiddenMarkovModel___init__ (chmm.c:1943)
==26797==    by 0x45402B: wrap_init (typeobject.c:4043)
==26797==    by 0x415832: PyObject_Call (abstract.c:1861)
==26797==    by 0x47D750: PyEval_CallObjectWithKeywords (ceval.c:3442)
==26797==    by 0x4CC304: wrapperdescr_call (descrobject.c:304)
==26797==    by 0x415832: PyObject_Call (abstract.c:1861)
==26797==    by 0x47D750: PyEval_CallObjectWithKeywords (ceval.c:3442)
==26797==    by 0x1EDD736C: __pyx_pf_4sage_5stats_3hmm_4chmm_25GaussianHiddenMarkovModel___init__ (chmm.c:2307)
==26797==    by 0x459350: type_call (typeobject.c:436)
==26797==    by 0x415832: PyObject_Call (abstract.c:1861)
==26797==    by 0x1EDD5E62: __pyx_pf_4sage_5stats_3hmm_4chmm_unpickle_gaussian_hmm_v0 (chmm.c:5465)

==26797== Invalid read of size 1
==26797==    at 0x4A1CDA3: strlen (mc_replace_strmem.c:242)
==26797==    by 0x44DACA: PyString_FromString (stringobject.c:108)
==26797==    by 0x1EDD644A: __pyx_pf_4sage_5stats_3hmm_4chmm_27ContinuousHiddenMarkovModel_name (chmm.c:2191)
==26797==    by 0x4841D7: PyEval_EvalFrameEx (ceval.c:3557)
==26797==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==26797==    by 0x484AF1: PyEval_EvalFrameEx (ceval.c:494)
==26797==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==26797==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==26797==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==26797==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==26797==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==26797==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==26797==  Address 0x57a88c2 is 0 bytes after a block of size 10 alloc'd
==26797==    at 0x4A1BDEB: malloc (vg_replace_malloc.c:207)
==26797==    by 0x1EDDAE1D: __pyx_pf_4sage_5stats_3hmm_4chmm_27ContinuousHiddenMarkovModel___init__ (chmm.c:1943)
==26797==    by 0x45402B: wrap_init (typeobject.c:4043)
==26797==    by 0x415832: PyObject_Call (abstract.c:1861)
==26797==    by 0x47D750: PyEval_CallObjectWithKeywords (ceval.c:3442)
==26797==    by 0x4CC304: wrapperdescr_call (descrobject.c:304)
==26797==    by 0x415832: PyObject_Call (abstract.c:1861)
==26797==    by 0x47D750: PyEval_CallObjectWithKeywords (ceval.c:3442)
==26797==    by 0x1EDD736C: __pyx_pf_4sage_5stats_3hmm_4chmm_25GaussianHiddenMarkovModel___init__ (chmm.c:2307)
==26797==    by 0x459350: type_call (typeobject.c:436)
==26797==    by 0x415832: PyObject_Call (abstract.c:1861)
==26797==    by 0x482DB9: PyEval_EvalFrameEx (ceval.c:3784)
```

There are also some leaks:

```
==26797== LEAK SUMMARY:
==26797==    definitely lost: 1,156 bytes in 25 blocks.
==26797==    indirectly lost: 233 bytes in 14 blocks.
==26797==      possibly lost: 308,845 bytes in 858 blocks.
==26797==    still reachable: 31,948,070 bytes in 191,804 blocks.
==26797==         suppressed: 305,691 bytes in 4,843 blocks.
```



---

Comment by mabshoff created at 2008-08-29 07:13:27

And here are some issues from hmm.pyx:

```
==27543== Invalid write of size 1
==27543==    at 0x4A1E100: strcpy (mc_replace_strmem.c:268)
==27543==    by 0x1E9BBE38: __pyx_pf_4sage_5stats_3hmm_3hmm_25DiscreteHiddenMarkovModel___init__ (hmm.c:2786)
==27543==    by 0x459350: type_call (typeobject.c:436)
==27543==    by 0x415832: PyObject_Call (abstract.c:1861)
==27543==    by 0x482DB9: PyEval_EvalFrameEx (ceval.c:3784)
==27543==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==27543==    by 0x484AF1: PyEval_EvalFrameEx (ceval.c:494)
==27543==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==27543==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==27543==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==27543==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==27543==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==27543==  Address 0x894890a is 0 bytes after a block of size 10 alloc'd
==27543==    at 0x4A1BDEB: malloc (vg_replace_malloc.c:207)
==27543==    by 0x1E9BBCF6: __pyx_pf_4sage_5stats_3hmm_3hmm_25DiscreteHiddenMarkovModel___init__ (hmm.c:1886)
==27543==    by 0x459350: type_call (typeobject.c:436)
==27543==    by 0x415832: PyObject_Call (abstract.c:1861)
==27543==    by 0x482DB9: PyEval_EvalFrameEx (ceval.c:3784)
==27543==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==27543==    by 0x484AF1: PyEval_EvalFrameEx (ceval.c:494)
==27543==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==27543==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==27543==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==27543==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==27543==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)

==27543== Invalid read of size 1
==27543==    at 0x4A1CDA3: strlen (mc_replace_strmem.c:242)
==27543==    by 0x44DACA: PyString_FromString (stringobject.c:108)
==27543==    by 0x1E9B3C4A: __pyx_pf_4sage_5stats_3hmm_3hmm_25DiscreteHiddenMarkovModel_name (hmm.c:4097)
==27543==    by 0x4841D7: PyEval_EvalFrameEx (ceval.c:3557)
==27543==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==27543==    by 0x484AF1: PyEval_EvalFrameEx (ceval.c:494)
==27543==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==27543==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==27543==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==27543==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==27543==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==27543==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==27543==  Address 0x894890a is 0 bytes after a block of size 10 alloc'd
==27543==    at 0x4A1BDEB: malloc (vg_replace_malloc.c:207)
==27543==    by 0x1E9BBCF6: __pyx_pf_4sage_5stats_3hmm_3hmm_25DiscreteHiddenMarkovModel___init__ (hmm.c:1886)
==27543==    by 0x459350: type_call (typeobject.c:436)
==27543==    by 0x415832: PyObject_Call (abstract.c:1861)
==27543==    by 0x482DB9: PyEval_EvalFrameEx (ceval.c:3784)
==27543==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==27543==    by 0x484AF1: PyEval_EvalFrameEx (ceval.c:494)
==27543==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==27543==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==27543==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==27543==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==27543==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)

==27543== Conditional jump or move depends on uninitialised value(s)
==27543==    at 0x1EAE4670: ghmm_dmodel_generate_sequences (in /scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/local/lib/libghmm.so.1.0.0)
==27543==    by 0x1E9BFB12: __pyx_pf_4sage_5stats_3hmm_3hmm_25DiscreteHiddenMarkovModel_sample (hmm.c:4522)
==27543==    by 0x483E46: PyEval_EvalFrameEx (ceval.c:3573)
==27543==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==27543==    by 0x484AF1: PyEval_EvalFrameEx (ceval.c:494)
==27543==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==27543==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==27543==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==27543==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==27543==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==27543==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==27543==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)

==27543== Invalid read of size 1
==27543==    at 0x4A1CDA3: strlen (mc_replace_strmem.c:242)
==27543==    by 0x44DACA: PyString_FromString (stringobject.c:108)
==27543==    by 0x1E9B3C4A: __pyx_pf_4sage_5stats_3hmm_3hmm_25DiscreteHiddenMarkovModel_name (hmm.c:4097)
==27543==    by 0x415832: PyObject_Call (abstract.c:1861)
==27543==    by 0x1E9B6AFC: __pyx_pf_4sage_5stats_3hmm_3hmm_25DiscreteHiddenMarkovModel___reduce__ (hmm.c:3704)
==27543==    by 0x415832: PyObject_Call (abstract.c:1861)
==27543==    by 0x47D750: PyEval_CallObjectWithKeywords (ceval.c:3442)
==27543==    by 0x458C0F: object_reduce_ex (typeobject.c:2867)
==27543==    by 0x415832: PyObject_Call (abstract.c:1861)
==27543==    by 0x7DE9723: save (cPickle.c:2498)
==27543==    by 0x7DEB587: cpm_dumps (cPickle.c:2580)
==27543==    by 0x415832: PyObject_Call (abstract.c:1861)
==27543==  Address 0x5a82f9a is 0 bytes after a block of size 10 alloc'd
==27543==    at 0x4A1BDEB: malloc (vg_replace_malloc.c:207)
==27543==    by 0x1E9BBCF6: __pyx_pf_4sage_5stats_3hmm_3hmm_25DiscreteHiddenMarkovModel___init__ (hmm.c:1886)
==27543==    by 0x459350: type_call (typeobject.c:436)
==27543==    by 0x415832: PyObject_Call (abstract.c:1861)
==27543==    by 0x482DB9: PyEval_EvalFrameEx (ceval.c:3784)
==27543==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==27543==    by 0x484AF1: PyEval_EvalFrameEx (ceval.c:494)
==27543==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==27543==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==27543==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==27543==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==27543==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)

==27543== Invalid read of size 1
==27543==    at 0x4A1DFC3: memcpy (mc_replace_strmem.c:402)
==27543==    by 0x44DB39: PyString_FromString (stringobject.c:136)
==27543==    by 0x1E9B3C4A: __pyx_pf_4sage_5stats_3hmm_3hmm_25DiscreteHiddenMarkovModel_name (hmm.c:4097)
==27543==    by 0x4841D7: PyEval_EvalFrameEx (ceval.c:3557)
==27543==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==27543==    by 0x484AF1: PyEval_EvalFrameEx (ceval.c:494)
==27543==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==27543==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==27543==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==27543==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==27543==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==27543==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==27543==  Address 0x57beb62 is 0 bytes after a block of size 10 alloc'd
==27543==    at 0x4A1BDEB: malloc (vg_replace_malloc.c:207)
==27543==    by 0x1E9BBCF6: __pyx_pf_4sage_5stats_3hmm_3hmm_25DiscreteHiddenMarkovModel___init__ (hmm.c:1886)
==27543==    by 0x459350: type_call (typeobject.c:436)
==27543==    by 0x415832: PyObject_Call (abstract.c:1861)
==27543==    by 0x1E9B3A05: __pyx_pf_4sage_5stats_3hmm_3hmm_unpickle_discrete_hmm_v0 (hmm.c:5875)
==27543==    by 0x415832: PyObject_Call (abstract.c:1861)
==27543==    by 0x47D750: PyEval_CallObjectWithKeywords (ceval.c:3442)
==27543==    by 0x7DE575D: Instance_New (cPickle.c:3651)
==27543==    by 0x7DEB7EE: load_reduce (cPickle.c:4417)
==27543==    by 0x7DEF35C: load (cPickle.c:4712)
==27543==    by 0x7DEFBFE: cpm_loads (cPickle.c:5488)
==27543==    by 0x415832: PyObject_Call (abstract.c:1861)

==27543== Invalid read of size 1
==27543==    at 0x4A1CDA3: strlen (mc_replace_strmem.c:242)
==27543==    by 0x44DACA: PyString_FromString (stringobject.c:108)
==27543==    by 0x1E9B506C: __pyx_pf_4sage_5stats_3hmm_3hmm_25DiscreteHiddenMarkovModel___repr__ (hmm.c:3899)
==27543==    by 0x443669: PyObject_Repr (object.c:361)
==27543==    by 0x429ECB: PyFile_WriteObject (fileobject.c:2195)
==27543==    by 0x4AD248: sys_displayhook (sysmodule.c:114)
==27543==    by 0x415832: PyObject_Call (abstract.c:1861)
==27543==    by 0x47D750: PyEval_CallObjectWithKeywords (ceval.c:3442)
==27543==    by 0x483599: PyEval_EvalFrameEx (ceval.c:1531)
==27543==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==27543==    by 0x484AF1: PyEval_EvalFrameEx (ceval.c:494)
==27543==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==27543==  Address 0x530b132 is 0 bytes after a block of size 10 alloc'd
==27543==    at 0x4A1BDEB: malloc (vg_replace_malloc.c:207)
==27543==    by 0x1E9BBCF6: __pyx_pf_4sage_5stats_3hmm_3hmm_25DiscreteHiddenMarkovModel___init__ (hmm.c:1886)
==27543==    by 0x459350: type_call (typeobject.c:436)
==27543==    by 0x415832: PyObject_Call (abstract.c:1861)
==27543==    by 0x1E9B3A05: __pyx_pf_4sage_5stats_3hmm_3hmm_unpickle_discrete_hmm_v0 (hmm.c:5875)
==27543==    by 0x483E46: PyEval_EvalFrameEx (ceval.c:3573)
==27543==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==27543==    by 0x484AF1: PyEval_EvalFrameEx (ceval.c:494)
==27543==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==27543==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==27543==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==27543==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
```

There are also some memory leaks:

```
==27543== LEAK SUMMARY:
==27543==    definitely lost: 1,548 bytes in 52 blocks.
==27543==    indirectly lost: 8,984 bytes in 58 blocks.
==27543==      possibly lost: 333,965 bytes in 908 blocks.
==27543==    still reachable: 31,962,542 bytes in 191,843 blocks.
==27543==         suppressed: 305,691 bytes in 4,843 blocks.
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-09-05 10:17:59

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-09-12 23:12:28

This ticket fixes most of the issues. Since we will disable doctests in the two files due to a bug in ghmm itself that only hit us on Itanium the other ones will be fixed down the road.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-12 23:14:06

Oops, wrong ticket. But nearly all of the valgrind issue are fixed.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-13 02:04:41

We will deal with this post 3.1.2.

Cheers,

Michael


---

Comment by was created at 2009-04-23 07:37:00

On Solaris 3.4.1 x86 right now only two tiny doctests fail:


```
-bash-3.00$ sage -t *
sage -t  "devel/sage-main/sage/stats/hmm/all.py"            
         [0.3 s]
sage -t  "devel/sage-main/sage/stats/hmm/chmm.pyx"          
**********************************************************************
File "/home/mabshoff/build-3.4.1.rc4/sage-3.4.1.rc4-fulvia-gcc-4.3.3/devel/sage-main/sage/stats/hmm/chmm.pyx", line 592:
    sage: m.log_likelihood(finance.TimeSeries(100).randomize('normal',10,1))
Expected:
    -5010.151947016132
Got:
    -5010.1519470161311
**********************************************************************
1 items had failures:
   1 of  13 in __main__.example_18
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/mabshoff/build-3.4.1.rc4/sage-3.4.1.rc4-fulvia-gcc-4.3.3/tmp/.doctest_chmm.py
         [5.8 s]
exit code: 1024
sage -t  "devel/sage-main/sage/stats/hmm/hmm.pyx"           
**********************************************************************
File "/home/mabshoff/build-3.4.1.rc4/sage-3.4.1.rc4-fulvia-gcc-4.3.3/devel/sage-main/sage/stats/hmm/hmm.pyx", line 629:
    sage: a.log_likelihood([0,0])
Expected:
    -inf
Got:
    -Infinity
**********************************************************************
1 items had failures:
   1 of  12 in __main__.example_18
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/mabshoff/build-3.4.1.rc4/sage-3.4.1.rc4-fulvia-gcc-4.3.3/tmp/.doctest_hmm.py
         [7.3 s]
exit code: 1024
sage -t  "devel/sage-main/sage/stats/hmm/misc.pxi"          
         [4.9 s]
 
----------------------------------------------------------------------
The following tests failed:
```



---

Comment by was created at 2009-06-15 23:22:35

Changing priority from blocker to critical.


---

Comment by was created at 2009-06-15 23:22:35

If we've released for months and months without fixing this, it doesn't make sense to keep it as a blocker.


---

Comment by was created at 2010-01-17 12:21:16

1. I tried enabling the doctests on x86_64, and they still work fine. 

2. Here's the backtrace on Itanium, where there are still segfaults:


```
Program received signal SIGSEGV, Segmentation fault.
[Switching to Thread 2305843009213932800 (LWP 558)] 
0x2000000011100c51 in __pyx_pf_4sage_5stats_3hmm_3hmm_25DiscreteHiddenMarkovModel_viterbi (
    __pyx_v_self=0x2000000011639f58, __pyx_v_seq=0x2000000011660098)                       
    at sage/stats/hmm/hmm.c:6368                                                           
6368        __pyx_t_4 = PyInt_FromLong((__pyx_v_path[__pyx_t_8])); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[1]; __pyx_lineno = 702; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
(gdb) bt                                                                                       
#0  0x2000000011100c51 in __pyx_pf_4sage_5stats_3hmm_3hmm_25DiscreteHiddenMarkovModel_viterbi  
    (__pyx_v_self=0x2000000011639f58, __pyx_v_seq=0x2000000011660098)                          
    at sage/stats/hmm/hmm.c:6368                                                               
#1  0x400000000019efc0 in PyEval_EvalFrameEx (f=0x600000000209e630,                            
    throwflag=<value optimized out>) at Python/ceval.c:3694                                    
#2  0x40000000001a26c0 in PyEval_EvalCodeEx (co=<value optimized out>,                         
    globals=0x6000000002118960, locals=0x6000000002118960, args=0x0, argcount=0, kws=0x0,
    kwcount=0, defs=0x0, defcount=Cannot access memory at address 0x219a
) at Python/ceval.c:2968
#3  0x40000000001a28e0 in PyEval_EvalCode (co=0x200000001163c8a0, globals=0x6000000002118960,
...
```


Using --verbose we get an example:


```
sage:  a = hmm.DiscreteHiddenMarkovModel([[0.1,0.9],[0.1,0.9]], [[0.9,0.1],[0.1,0.9]], [0.5,0.5])
sage: a.viterbi([1,0,0,1,0,0,1,1])
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

Comment by was created at 2010-01-17 12:29:01

At this point a natural strategy is the following:

 (1) try the above with standalone GHMM (but basically the one that comes with Sage).  This will very likely fail due to this likely being a GHMM bug. 

 (2) try the above calculation on itanium with the latest svn standalone version of GHMM.  

 (3) If 2 works, it's a no brainer -- we have to upgrade GHMM.  If 2 fails, then report upstream.


---

Comment by bober created at 2012-03-21 00:31:13

Changing status from new to needs_review.


---

Comment by bober created at 2012-03-21 00:31:13

This is really old and it must have been fixed at some point if tests actually pass sometimes on iras.


---

Comment by was created at 2012-03-21 21:10:26

Resolution: fixed
