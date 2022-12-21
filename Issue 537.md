# Issue 537: leak in _ntl_gsetlength (from modular/dirichlet.py)

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-08-30 18:55:16

Assignee: mabshoff

From Sage 2.8.3rc3:

```
==25034== 48 bytes in 1 blocks are definitely lost in loss record 746 of 2,712
==25034==    at 0x4A05809: malloc (vg_replace_malloc.c:149)
==25034==    by 0x9774DD5: _ntl_gsetlength (in /tmp/Work2/sage-2.8.3.rc3/local/lib/libntl.so)
==25034==    by 0x9775D6F: _ntl_gmul (in /tmp/Work2/sage-2.8.3.rc3/local/lib/libntl.so)
==25034==    by 0x1B7908F4: __pyx_f_20number_field_element_18NumberFieldElement__mul_c_impl(__pyx_obj_20number_field_element
_NumberFieldElement*, __pyx_obj_4sage_9structure_7element_RingElement*) (ZZ.h:384)
==25034==    by 0xE3C999D: __pyx_f_7element_11RingElement__mul_c (element.c:8340)
==25034==    by 0xE3BD3E4: __pyx_f_7element_11RingElement___mul__ (element.c:7922)
==25034==    by 0x41596C: binary_op1 (abstract.c:398)
==25034==    by 0x418EC3: PyNumber_InPlaceMultiply (abstract.c:744)
==25034==    by 0x481053: PyEval_EvalFrameEx (ceval.c:1274)
==25034==    by 0x485025: PyEval_EvalFrameEx (ceval.c:3650)
==25034==    by 0x4865EF: PyEval_EvalCodeEx (ceval.c:2831)
==25034==    by 0x4845B3: PyEval_EvalFrameEx (ceval.c:3660)
```

Cheers,

Michael


---

Comment by mabshoff created at 2007-08-30 18:55:22

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-09-09 18:50:48

The NTL itself does actually leak some memory. This might be one of those. I has been considered not worth fixing by Victor Shoup, but I cannot find the reference at the moment. 

So  we might need to close this or add some deallocation hooks to NTL itself. Because this leak is rather small I don't consider this a high priority for now.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-20 06:54:15

This is still an issue with 3.0.alpha6, but the "definitely lost" turned into "still reachable".

Cheers,

Michael


---

Comment by craigcitro created at 2010-01-20 06:36:07

Resolution: wontfix


---

Comment by craigcitro created at 2010-01-20 06:36:07

I'm closing this one, for pretty much the same reasons as #536. It's too bad we don't have the doctests that caused these ...
