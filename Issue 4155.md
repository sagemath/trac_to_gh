# Issue 4155: [with patch, needs review] Speed up totally real field enumeration code

Issue created by migration from https://trac.sagemath.org/ticket/4155

Original creator: craigcitro

Original creation time: 2008-09-20 08:18:45

Assignee: craigcitro

CC:  alexghitza

The attached patch provides a significant speedup of John Voight's totally real field enumeration code. The patch moves `enumerate_totallyreal_fields_prim` into Cython (and thus `totallyreal.py` becomes `totallyreal.pyx`). Most of the speedup comes from explicitly declaring and being careful about types. A few small improvements to the Pari interface are thrown in, since they were written in the process of speeding up this code.

While I haven't performed any sort of systematic test, it seems that this code offers a factor of at least 2X speedup for enumerating fields of degree 5 or 6. 


---

Attachment


---

Comment by jvoight created at 2008-09-20 17:07:38

Thanks!  I tried your patch against my (presumably clean upgraded)
3.1.2 and it tells me:

sage: hg_sage.import_patch('trac-4155.patch')
Not trusting file /usr/local/sage/devel/sage-main/.hg/hgrc from
untrusted user lkost, group lkost
Not trusting file /usr/local/sage/devel/sage-main/.hg/hgrc from
untrusted user lkost, group lkost
applying /home/jvoight/trac-4155.patch
abort: no diffs found
cd "/usr/local/sage/devel/sage" && hg status
cd "/usr/local/sage/devel/sage" && hg status
cd "/usr/local/sage/devel/sage" && hg import   "/home/jvoight/trac-4155.patch"
sage: len(enumerate_totallyreal_fields_prim(5,5**7))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/jvoight/<ipython console> in <module>()

/home/jvoight/totallyreal.pyx in
sage.rings.number_field.totallyreal.enumerate_totallyreal_fields_prim
(sage/rings/number_field/totallyreal.c:4360)()

TypeError: Cannot convert int to sage.libs.pari.gen.gen

Maybe there's something going on with nfbasis_d?  That was the only
thing that came up as a possible conflict when I upgraded to 3.1.2.

   def nfbasis_d(self, long flag=0, p=0):
       """
       nfbasis_d(x): Return a basis of the number field defined over
       QQ by x and its discriminant.

       EXAMPLES:
           sage: F = NumberField(x^3-2,'alpha')
           sage: F._pari_()[0].nfbasis_d()
           ([1, x, x^2], -108)

           sage: G = NumberField(x^5-11,'beta')
           sage: G._pari_()[0].nfbasis_d()
           ([1, x, x^2, x^3, x^4], 45753125)

           sage: pari([-2,0,0,1]).Polrev().nfbasis_d()
           ([1, x, x^2], -108)
       """
       cdef gen d
       cdef GEN g

       if p:
           g = (<gen>self.pari(p)).g
       else:
           g = <GEN>NULL
       d = self.pari(0)
       _sig_on
       nfb = self.new_gen(nfbasis(self.g, &d.g, flag, g))
       return nfb, d.__int__()

JV


---

Comment by craigcitro created at 2008-09-20 22:59:14

Changing status from new to assigned.


---

Comment by craigcitro created at 2008-09-20 22:59:14

John -- so I can't reproduce this on my machine, and I just had someone else try on a clean 3.1.2 branch, and they didn't have any trouble either. Could I get you to make sure you did a `sage -br` after applying the patch and try again, or failing that, make a new 3.1.2 branch and try again? If that doesn't work, I'll have to think of something else to figure out why it wasn't working for you ...


---

Comment by mabshoff created at 2008-09-20 23:03:27

The patch that Craig posted applies cleanly against 3.1.2 as well as my current 3.1.3.alpha1 merge tree:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.3.alpha1/devel/sage$ patch -p1 --dry-run < trac-4155.patch 
patching file sage/libs/pari/gen.pxd
patching file sage/libs/pari/gen.pyx
Hunk #1 succeeded at 4933 (offset 23 lines).
Hunk #2 succeeded at 6448 (offset 70 lines).
patching file sage/rings/number_field/totallyreal.py
patching file sage/rings/number_field/totallyreal.pyx
patching file sage/rings/number_field/totallyreal_data.pxd
patching file sage/rings/number_field/totallyreal_data.pyx
patching file sage/rings/number_field/totallyreal_rel.py
patching file setup.py
Hunk #1 succeeded at 955 (offset 12 lines).
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.2/devel/sage$ patch -p1 --dry-run < trac-4155.patch 
patching file sage/libs/pari/gen.pxd
patching file sage/libs/pari/gen.pyx
Hunk #1 succeeded at 4933 (offset 23 lines).
Hunk #2 succeeded at 6448 (offset 70 lines).
patching file sage/rings/number_field/totallyreal.py
patching file sage/rings/number_field/totallyreal.pyx
patching file sage/rings/number_field/totallyreal_data.pxd
patching file sage/rings/number_field/totallyreal_data.pyx
patching file sage/rings/number_field/totallyreal_rel.py
patching file setup.py
Hunk #1 succeeded at 954 (offset 11 lines).
```


Doctests for 3.1.2+Craig's patch pass. I assume they also do against the current 3.1.3.alpha1 merge tree.

Cheers,

Michael


---

Comment by jvoight created at 2008-09-21 14:59:11

Not sure what was going on with my version of sage--something must have happened during an upgrade.  A fresh install shows (as with Michael) that the patch applies cleanly.  

I did several tests of my own, including a long one (9h 50m to compute the 70463 totally real quintic fields with discriminant <= 50000000), and it passed all of these tests.  So it gets the green flag from me.

Awesome work, Craig!

JV


---

Comment by mabshoff created at 2008-09-21 22:05:05

Oops: While valgrinding totallyreal.py I saw this:

```
==16950== More than 10000000 total errors detected.  I'm not reporting any more.
==16950== Final error counts will be inaccurate.  Go fix your program!
==16950== Rerun with --error-limit=no to disable this cutoff.  Note
==16950== that errors may occur in your program without prior warning from
==16950== Valgrind, because errors are no longer being displayed.
```

Those are the issues:

```
==16950== Conditional jump or move depends on uninitialised value(s)
==16950==    at 0x12A60CC6: __pyx_f_4sage_5rings_12number_field_16totallyreal_data_7tr_data_incr (totallyreal_data.c:5532)
==16950==    by 0x12932601: __pyx_pf_4sage_5rings_12number_field_11totallyreal_enumerate_totallyreal_fields_prim (totallyreal.c:3205)
==16950==    by 0x483E46: PyEval_EvalFrameEx (ceval.c:3573)
==16950==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==16950==    by 0x484AF1: PyEval_EvalFrameEx (ceval.c:494)
==16950==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==16950==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==16950==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==16950==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==16950==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==16950==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==16950==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==16950==    by 0x486051: PyEval_EvalCode (ceval.c:494)
==16950==    by 0x4A751D: PyRun_FileExFlags (pythonrun.c:1273)
==16950==    by 0x4A77AF: PyRun_SimpleFileExFlags (pythonrun.c:879)
==16950==    by 0x41215F: Py_Main (main.c:523)
==16950==    by 0x4FD94C9: (below main) (in /lib/libc-2.3.6.so)
```


```
==16950== Invalid read of size 8
==16950==    at 0x12A55392: __pyx_f_4sage_5rings_12number_field_16totallyreal_data_lagrange_degree_3 (totallyreal_data.c:2713)
==16950==    by 0x12A63665: __pyx_f_4sage_5rings_12number_field_16totallyreal_data_7tr_data_incr (totallyreal_data.c:5727)
==16950==    by 0x12932601: __pyx_pf_4sage_5rings_12number_field_11totallyreal_enumerate_totallyreal_fields_prim (totallyreal.c:3205)
==16950==    by 0x483E46: PyEval_EvalFrameEx (ceval.c:3573)
==16950==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==16950==    by 0x484AF1: PyEval_EvalFrameEx (ceval.c:494)
==16950==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==16950==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==16950==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==16950==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==16950==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==16950==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==16950==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==16950==    by 0x486051: PyEval_EvalCode (ceval.c:494)
==16950==    by 0x4A751D: PyRun_FileExFlags (pythonrun.c:1273)
==16950==    by 0x4A77AF: PyRun_SimpleFileExFlags (pythonrun.c:879)
==16950==    by 0x41215F: Py_Main (main.c:523)
==16950==    by 0x4FD94C9: (below main) (in /lib/libc-2.3.6.so)
==16950==  Address 0x19ae0cd8 is 8 bytes after a block of size 96 alloc'd
==16950==    at 0x4A1BE1B: malloc (vg_replace_malloc.c:207)
==16950==    by 0x12B9694A: PyArray_NewFromDescr (arrayobject.c:5626)
==16950==    by 0x12BC1842: PyArray_Concatenate (multiarraymodule.c:1834)
==16950==    by 0x12BC134C: PyArray_Concatenate (multiarraymodule.c:1733)
==16950==    by 0x12BC19DF: array_concatenate (multiarraymodule.c:6701)
==16950==    by 0x483E46: PyEval_EvalFrameEx (ceval.c:3573)
==16950==    by 0x48491B: PyEval_EvalFrameEx (ceval.c:3659)
==16950==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==16950==    by 0x4CF3F7: function_call (funcobject.c:517)
==16950==    by 0x415832: PyObject_Call (abstract.c:1861)
==16950==    by 0x12A55233: __pyx_f_4sage_5rings_12number_field_16totallyreal_data_lagrange_degree_3 (totallyreal_data.c:2668)
==16950==    by 0x12A63665: __pyx_f_4sage_5rings_12number_field_16totallyreal_data_7tr_data_incr (totallyreal_data.c:5727)
==16950==    by 0x12932601: __pyx_pf_4sage_5rings_12number_field_11totallyreal_enumerate_totallyreal_fields_prim (totallyreal.c:3205)
==16950==    by 0x483E46: PyEval_EvalFrameEx (ceval.c:3573)
==16950==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==16950==    by 0x484AF1: PyEval_EvalFrameEx (ceval.c:494)
==16950==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==16950==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==16950==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==16950==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==16950==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==16950==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==16950==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==16950==    by 0x486051: PyEval_EvalCode (ceval.c:494)
==16950==    by 0x4A751D: PyRun_FileExFlags (pythonrun.c:1273)
```


```
==16950== Conditional jump or move depends on uninitialised value(s)
==16950==    at 0x4E524E3: ceil (in /lib/libm-2.3.6.so)
==16950==    by 0x12A61046: __pyx_f_4sage_5rings_12number_field_16totallyreal_data_7tr_data_incr (totallyreal_data.c:6141)
==16950==    by 0x12932601: __pyx_pf_4sage_5rings_12number_field_11totallyreal_enumerate_totallyreal_fields_prim (totallyreal.c:3205)
==16950==    by 0x483E46: PyEval_EvalFrameEx (ceval.c:3573)
==16950==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==16950==    by 0x484AF1: PyEval_EvalFrameEx (ceval.c:494)
==16950==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==16950==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==16950==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==16950==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==16950==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==16950==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==16950==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==16950==    by 0x486051: PyEval_EvalCode (ceval.c:494)
==16950==    by 0x4A751D: PyRun_FileExFlags (pythonrun.c:1273)
==16950==    by 0x4A77AF: PyRun_SimpleFileExFlags (pythonrun.c:879)
==16950==    by 0x41215F: Py_Main (main.c:523)
==16950==    by 0x4FD94C9: (below main) (in /lib/libc-2.3.6.so)
```

There are more, but you get the idea. I will poke around.

It seems that there are no memory leaks in the code as far as I know, but one valgrind tests is still running.

Cheers,

Michael


---

Comment by craigcitro created at 2008-09-22 05:11:57

Ok, having talked with Michael, we've cleaned up lots of valgrind-inspired stuff (explicitly initializing memory, etc), and caught one buglet (7 and 6 are apparently not equal).


---

Comment by mabshoff created at 2008-09-22 05:17:47

Positive review on trac-4155-2.patch from my end - I was deeply involved with the fixes, but aside from one issue left over this is a giant improvement from millions of errors to two, which will be addressed via a follow up ticket.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-23 00:09:03

Merged both patches in Sage 3.1.3.alpha1


---

Comment by mabshoff created at 2008-09-23 00:09:03

Resolution: fixed
