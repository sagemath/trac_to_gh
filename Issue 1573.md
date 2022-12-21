# Issue 1573: Mismatched free() / delete / delete [] in wrap.cc

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-12-20 11:42:48

Assignee: mabshoff

The following causes double frees upon exit of Sage when using functions in mwrank.pyx:

```
==1359== Mismatched free() / delete / delete []
==1359==    at 0x4A1B74A: free (vg_replace_malloc.c:320)
==1359==    by 0xE1A4B60: __pyx_f_4sage_4libs_6mwrank_6mwrank_string_sigoff (mwrank.c:314)
==1359==    by 0xE1A62C9: __pyx_pf_4sage_4libs_6mwrank_6mwrank_10_Curvedata_discriminant (mwrank.c:1339)
==1359==    by 0x415542: PyObject_Call (abstract.c:1860)
==1359==    by 0x47C480: PyEval_CallObjectWithKeywords (ceval.c:3433)
==1359==    by 0xE1A9DEC: __pyx_pf_4sage_4libs_6mwrank_6mwrank_10_Curvedata___init__ (mwrank.c:1003)
==1359==    by 0x458E40: type_call (typeobject.c:436)
==1359==    by 0x415542: PyObject_Call (abstract.c:1860)
==1359==    by 0x481AC1: PyEval_EvalFrameEx (ceval.c:3775)
==1359==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==1359==    by 0x4838F4: PyEval_EvalFrameEx (ceval.c:494)
==1359==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==1359==  Address 0x77ae6a8 is 0 bytes inside a block of size 7 alloc'd
==1359==    at 0x4A1BFE4: operator new[](unsigned long) (vg_replace_malloc.c:271)
==1359==    by 0xE1AB0E6: stringstream_to_char(std::basic_ostringstream<char, std::char_traits<char>, std::allocator<char> >
&) (wrap.cc:26)
==1359==    by 0xE1AC000: Curvedata_getdiscr (wrap.cc:98)
==1359==    by 0xE1A62C1: __pyx_pf_4sage_4libs_6mwrank_6mwrank_10_Curvedata_discriminant (mwrank.c:1339)
==1359==    by 0x415542: PyObject_Call (abstract.c:1860)
==1359==    by 0x47C480: PyEval_CallObjectWithKeywords (ceval.c:3433)
==1359==    by 0xE1A9DEC: __pyx_pf_4sage_4libs_6mwrank_6mwrank_10_Curvedata___init__ (mwrank.c:1003)
==1359==    by 0x458E40: type_call (typeobject.c:436)
==1359==    by 0x415542: PyObject_Call (abstract.c:1860)
==1359==    by 0x481AC1: PyEval_EvalFrameEx (ceval.c:3775)
==1359==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==1359==    by 0x4838F4: PyEval_EvalFrameEx (ceval.c:494)
```


The attached patch fixes the issue.

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2007-12-20 12:47:51

The patch fixes the doctest failures caused by the updated cremona.spkg at #1233.

With the patch testall passes.

Cheers,

Michael


---

Comment by rlm created at 2007-12-20 18:07:04

Resolution: fixed


---

Comment by rlm created at 2007-12-20 18:07:04

Merged in 2.9.1 alpha2
