# Issue 511: memory leak: ntl wrapper leaks in __repr__

Issue created by migration from https://trac.sagemath.org/ticket/511

Original creator: mabshoff

Original creation time: 2007-08-29 12:06:18

Assignee: somebody

Keywords: ntl wrapper memory leak

See ticket #501 for more details:

The problem:

```
==22784== 791,674 bytes in 65,421 blocks are definitely lost in loss record 2,472 of 2,481
==22784==    at 0x4A05CB9: operator new[](unsigned long) (vg_replace_malloc.c:199)
==22784==    by 0x9280247: ZZ_pX_repr (in /tmp/Work2/sage-2.8.3.alpha2/local/lib/libcsage.so.0.0.0)
==22784==    by 0x176D6D57: __pyx_f_3ntl_9ntl_ZZ_pX___repr__ (ntl.c:6216)
==22784==    by 0x443C61: _PyObject_Str (object.c:406)
==22784==    by 0x443D0A: PyObject_Str (object.c:426)
==22784==    by 0x44EA8F: string_new (stringobject.c:3892)
==22784==    by 0x45A272: type_call (typeobject.c:422)
==22784==    by 0x4156A2: PyObject_Call (abstract.c:1860)
==22784==    by 0x480783: PyEval_EvalFrameEx (ceval.c:3775)
==22784==    by 0x485025: PyEval_EvalFrameEx (ceval.c:3650)
==22784==    by 0x4865EF: PyEval_EvalCodeEx (ceval.c:2831)
==22784==    by 0x4CFF37: function_call (funcobject.c:517)
```


The fix was suggested by was but never implemented:

```
17:53 < wstein> I changed that __repr__ code to this:
17:53 < wstein> ntl.set_modulus(ntl.ZZ(20))
17:53 < wstein> f = ntl.ZZ_pX(range(10000))
17:54 < wstein>     def __repr__(self):
17:54 < wstein>         cdef char* s = ZZ_pX_repr(self.x)
17:54 < wstein>         t = str(s)
17:54 < wstein>         free(s)
17:54 < wstein>         return t
17:54 < wstein> And the memory leak completely vanishes.
17:54 < mabshoff> :)
17:54 < wstein> Of course, this is wrong since I'm mixing malloc's free with C++'s new.
17:54 < wstein> It's just a demo.
17:54 < mabshoff> mmmh
```

So the credit should go to him, but I also fixed a second analog problem further down the code.

Without the patch:

```
==22784== LEAK SUMMARY:
==22784==    definitely lost: 794,838 bytes in 65,475 blocks.
==22784==      possibly lost: 350,158 bytes in 953 blocks.
==22784==    still reachable: 137,588,639 bytes in 19,728 blocks.
==22784==         suppressed: 0 bytes in 0 blocks.
```


With the patch:

```
==22993== LEAK SUMMARY:
==22993==    definitely lost: 3,103 bytes in 49 blocks.
==22993==      possibly lost: 349,334 bytes in 931 blocks.
==22993==    still reachable: 137,589,847 bytes in 19,621 blocks.
==22993==         suppressed: 0 bytes in 0 blocks.
```


The test computation finished, but I have no clue if it is correct.

Cheers,

Michael


---

Comment by mabshoff created at 2007-08-29 12:08:16

Changing assignee from somebody to was.


---

Comment by mabshoff created at 2007-08-29 12:08:16

Hmm, trac refused to accept by patch. So here is a link:

http://fsmath.mathematik.uni-dortmund.de/~mabshoff/patches/sage-2.8.3alpha2-fix-ntl-memleak-in-__repr__.patch


Cheers,

Michael


---

Comment by malb created at 2007-08-29 13:30:04

Trac still refuses attachments, so here is the patch for the c_lib which 'calloc's (instead of 'new') the memory mabshoff's patch 'free's
http://sage.math.washington.edu/home/malb/ntl_wrap_calloc.patch


---

Comment by mabshoff created at 2007-08-29 20:35:08

If #411 goes in this might or might not be needed any more.

Cheers,

Michael


---

Comment by was created at 2007-08-30 02:11:41

Fixed in sage-2.8.3.


---

Comment by was created at 2007-08-30 02:11:41

Resolution: fixed
