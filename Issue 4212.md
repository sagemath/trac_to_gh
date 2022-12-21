# Issue 4212: [with patch, needs review] Invalid read of size 8 in totallyreal.pyx

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-09-28 07:48:32

Assignee: craigcitro, jvoight

CC:  mhansen craigcitro jvoight


```
==29696== Invalid read of size 8
==29696==    at 0x1320D5D9: __pyx_f_4sage_5rings_12number_field_16totallyreal_data_lagrange_degree_3 (totallyreal_data.c:2777)
==29696==    by 0x1321C5B5: __pyx_f_4sage_5rings_12number_field_16totallyreal_data_7tr_data_incr (totallyreal_data.c:5957)
==29696==    by 0x130E6BBA: __pyx_pf_4sage_5rings_12number_field_11totallyreal_enumerate_totallyreal_fields_prim (totallyreal.c:4212)
==29696==    by 0x483E46: PyEval_EvalFrameEx (ceval.c:3573)
==29696==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==29696==    by 0x484AF1: PyEval_EvalFrameEx (ceval.c:494)
==29696==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==29696==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==29696==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==29696==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==29696==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==29696==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==29696==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==29696==    by 0x486051: PyEval_EvalCode (ceval.c:494)
==29696==    by 0x4A751D: PyRun_FileExFlags (pythonrun.c:1273)
==29696==    by 0x4A77AF: PyRun_SimpleFileExFlags (pythonrun.c:879)
==29696==    by 0x41215F: Py_Main (main.c:523)
==29696==    by 0x4FD94C9: (below main) (in /lib/libc-2.3.6.so)
==29696==  Address 0x8e598b0 is 8 bytes after a block of size 48 alloc'd
==29696==    at 0x4A1BE1B: malloc (vg_replace_malloc.c:207)
==29696==    by 0x133508CA: PyArray_NewFromDescr (arrayobject.c:5633)
==29696==    by 0x13377F52: PyArray_Concatenate (multiarraymodule.c:1846)
==29696==    by 0x13377A5C: PyArray_Concatenate (multiarraymodule.c:1745)
==29696==    by 0x133780EF: array_concatenate (multiarraymodule.c:6745)
==29696==    by 0x483E46: PyEval_EvalFrameEx (ceval.c:3573)
==29696==    by 0x48491B: PyEval_EvalFrameEx (ceval.c:3659)
==29696==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==29696==    by 0x4CF3F7: function_call (funcobject.c:517)
==29696==    by 0x415832: PyObject_Call (abstract.c:1861)
==29696==    by 0x1320D1D0: __pyx_f_4sage_5rings_12number_field_16totallyreal_data_lagrange_degree_3 (totallyreal_data.c:2670)
==29696==    by 0x1321C5B5: __pyx_f_4sage_5rings_12number_field_16totallyreal_data_7tr_data_incr (totallyreal_data.c:5957)
==29696==    by 0x130E6BBA: __pyx_pf_4sage_5rings_12number_field_11totallyreal_enumerate_totallyreal_fields_prim (totallyreal.c:4212)
==29696==    by 0x483E46: PyEval_EvalFrameEx (ceval.c:3573)
==29696==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==29696==    by 0x484AF1: PyEval_EvalFrameEx (ceval.c:494)
==29696==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==29696==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==29696==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==29696==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==29696==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==29696==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==29696==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==29696==    by 0x486051: PyEval_EvalCode (ceval.c:494)
==29696==    by 0x4A751D: PyRun_FileExFlags (pythonrun.c:1273)
==29696== 
==29696== Invalid read of size 8
==29696==    at 0x1320DBF9: __pyx_f_4sage_5rings_12number_field_16totallyreal_data_lagrange_degree_3 (totallyreal_data.c:2792)
==29696==    by 0x1321C5B5: __pyx_f_4sage_5rings_12number_field_16totallyreal_data_7tr_data_incr (totallyreal_data.c:5957)
==29696==    by 0x130E6BBA: __pyx_pf_4sage_5rings_12number_field_11totallyreal_enumerate_totallyreal_fields_prim (totallyreal.c:4212)
==29696==    by 0x483E46: PyEval_EvalFrameEx (ceval.c:3573)
==29696==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==29696==    by 0x484AF1: PyEval_EvalFrameEx (ceval.c:494)
==29696==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==29696==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==29696==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==29696==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==29696==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==29696==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==29696==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==29696==    by 0x486051: PyEval_EvalCode (ceval.c:494)
==29696==    by 0x4A751D: PyRun_FileExFlags (pythonrun.c:1273)
==29696==    by 0x4A77AF: PyRun_SimpleFileExFlags (pythonrun.c:879)
==29696==    by 0x41215F: Py_Main (main.c:523)
==29696==    by 0x4FD94C9: (below main) (in /lib/libc-2.3.6.so)
==29696==  Address 0x8e598a8 is 0 bytes after a block of size 48 alloc'd
==29696==    at 0x4A1BE1B: malloc (vg_replace_malloc.c:207)
==29696==    by 0x133508CA: PyArray_NewFromDescr (arrayobject.c:5633)
==29696==    by 0x13377F52: PyArray_Concatenate (multiarraymodule.c:1846)
==29696==    by 0x13377A5C: PyArray_Concatenate (multiarraymodule.c:1745)
==29696==    by 0x133780EF: array_concatenate (multiarraymodule.c:6745)
==29696==    by 0x483E46: PyEval_EvalFrameEx (ceval.c:3573)
==29696==    by 0x48491B: PyEval_EvalFrameEx (ceval.c:3659)
==29696==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==29696==    by 0x4CF3F7: function_call (funcobject.c:517)
==29696==    by 0x415832: PyObject_Call (abstract.c:1861)
==29696==    by 0x1320D1D0: __pyx_f_4sage_5rings_12number_field_16totallyreal_data_lagrange_degree_3 (totallyreal_data.c:2670)
==29696==    by 0x1321C5B5: __pyx_f_4sage_5rings_12number_field_16totallyreal_data_7tr_data_incr (totallyreal_data.c:5957)
==29696==    by 0x130E6BBA: __pyx_pf_4sage_5rings_12number_field_11totallyreal_enumerate_totallyreal_fields_prim (totallyreal.c:4212)
==29696==    by 0x483E46: PyEval_EvalFrameEx (ceval.c:3573)
==29696==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==29696==    by 0x484AF1: PyEval_EvalFrameEx (ceval.c:494)
==29696==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==29696==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==29696==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==29696==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==29696==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==29696==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==29696==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==29696==    by 0x486051: PyEval_EvalCode (ceval.c:494)
==29696==    by 0x4A751D: PyRun_FileExFlags (pythonrun.c:1273)
```

This is perplexing considering that we are having a degree six polynomial. *But* when the roots are real numpy returns an array of doubles and not complex numbers. With the following patch applied

```
--- a/sage/rings/number_field/totallyreal_data.pyx	Sun Sep 21 20:50:32 2008 -0700
+++ b/sage/rings/number_field/totallyreal_data.pyx	Sun Sep 28 00:41:17 2008 -0700
`@``@` -326,6 +326,10 `@``@`
         
         fcoeff = [ int(coeffs[i]) for i in range(7) ]
         rts = numpy.roots(fcoeff)
+
+        import sys
+        sys.stderr.write(str(fcoeff)+"\n")
+        sys.stderr.write(str(rts)+"\n")
 
         roots_data = <double *>((<ndarray>rts).data)
         for i from 0 <= i < 6:
```

we get:

```
<SNIP>
[200, -480, -2712, 4052, 18072, -10800, -54000]
[ 3.25148114+0.j          2.61459959+0.75768433j  2.61459959-0.75768433j
 -1.91214896+1.14457619j -1.91214896-1.14457619j -2.25638240+0.j        ]
[200, -480, -2712, 4592, 17424, -13824, -53568]
[ 3.18809326+0.j          2.64899261+0.91101386j  2.64899261-0.91101386j
 -1.88057770+1.03363004j -1.88057770-1.03363004j -2.32492308+0.j        ]
[225, -540, -2196, 3744, 6192, -4032, 576]
[ 2.92664989  2.92664995 -2.00000003 -1.99999997  0.27335008  0.27335009]
```

Notice that the last output for rst is six doubles, i.e. an array of 48 bytes. The fix is to ask for rts as complex128, i.e.

```
rts = numpy.roots(fcoeff).astype("complex128")
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-09-28 07:54:45

With the patch applied the problem goes away, i.e.:

```
Trying:
    ls = enumerate_totallyreal_fields_prim(Integer(5),Integer(10)**Integer(5)) ; ls###line 171:_sage_    >>> ls = enumerate_totallyreal_fields_prim(5,10^5) ; ls
Expecting:
    [[14641, x^5 - x^4 - 4*x^3 + 3*x^2 + 3*x - 1],
     [24217, x^5 - 5*x^3 - x^2 + 3*x + 1],
     [36497, x^5 - 2*x^4 - 3*x^3 + 5*x^2 + x - 1],
     [38569, x^5 - 5*x^3 + 4*x - 1],
     [65657, x^5 - x^4 - 5*x^3 + 2*x^2 + 5*x + 1],
     [70601, x^5 - x^4 - 5*x^3 + 2*x^2 + 3*x - 1],
     [81509, x^5 - x^4 - 5*x^3 + 3*x^2 + 5*x - 2],
     [81589, x^5 - 6*x^3 + 8*x - 1],
     [89417, x^5 - 6*x^3 - x^2 + 8*x + 3]]
ok
```


John, Craig, 

please audit the totallyreal* code for similar problems arising from numpy. I consider it quite a coincidence that we hit this issue.

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2008-09-28 07:59:00

For the record: This fix has been a joined mhansen & mabshoff production and review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-28 07:59:00

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-09-28 07:59:00

Changing assignee from craigcitro, jvoight to mabshoff.


---

Comment by mhansen created at 2008-09-28 08:00:53

Looks good to me.


---

Comment by mabshoff created at 2008-09-28 08:05:39

Resolution: fixed


---

Comment by mabshoff created at 2008-09-28 08:05:39

Merged in Sage 3.1.3.alpha2
