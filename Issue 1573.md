# Issue 1573: Mismatched free() / delete / delete [] in wrap.cc

archive/issues_001573.json:
```json
{
    "body": "Assignee: mabshoff\n\nThe following causes double frees upon exit of Sage when using functions in mwrank.pyx:\n\n```\n==1359== Mismatched free() / delete / delete []\n==1359==    at 0x4A1B74A: free (vg_replace_malloc.c:320)\n==1359==    by 0xE1A4B60: __pyx_f_4sage_4libs_6mwrank_6mwrank_string_sigoff (mwrank.c:314)\n==1359==    by 0xE1A62C9: __pyx_pf_4sage_4libs_6mwrank_6mwrank_10_Curvedata_discriminant (mwrank.c:1339)\n==1359==    by 0x415542: PyObject_Call (abstract.c:1860)\n==1359==    by 0x47C480: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==1359==    by 0xE1A9DEC: __pyx_pf_4sage_4libs_6mwrank_6mwrank_10_Curvedata___init__ (mwrank.c:1003)\n==1359==    by 0x458E40: type_call (typeobject.c:436)\n==1359==    by 0x415542: PyObject_Call (abstract.c:1860)\n==1359==    by 0x481AC1: PyEval_EvalFrameEx (ceval.c:3775)\n==1359==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==1359==    by 0x4838F4: PyEval_EvalFrameEx (ceval.c:494)\n==1359==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==1359==  Address 0x77ae6a8 is 0 bytes inside a block of size 7 alloc'd\n==1359==    at 0x4A1BFE4: operator new[](unsigned long) (vg_replace_malloc.c:271)\n==1359==    by 0xE1AB0E6: stringstream_to_char(std::basic_ostringstream<char, std::char_traits<char>, std::allocator<char> >\n&) (wrap.cc:26)\n==1359==    by 0xE1AC000: Curvedata_getdiscr (wrap.cc:98)\n==1359==    by 0xE1A62C1: __pyx_pf_4sage_4libs_6mwrank_6mwrank_10_Curvedata_discriminant (mwrank.c:1339)\n==1359==    by 0x415542: PyObject_Call (abstract.c:1860)\n==1359==    by 0x47C480: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==1359==    by 0xE1A9DEC: __pyx_pf_4sage_4libs_6mwrank_6mwrank_10_Curvedata___init__ (mwrank.c:1003)\n==1359==    by 0x458E40: type_call (typeobject.c:436)\n==1359==    by 0x415542: PyObject_Call (abstract.c:1860)\n==1359==    by 0x481AC1: PyEval_EvalFrameEx (ceval.c:3775)\n==1359==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==1359==    by 0x4838F4: PyEval_EvalFrameEx (ceval.c:494)\n```\n\n\nThe attached patch fixes the issue.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1573\n\n",
    "created_at": "2007-12-20T11:42:48Z",
    "labels": [
        "memleak",
        "critical",
        "bug"
    ],
    "title": "Mismatched free() / delete / delete [] in wrap.cc",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1573",
    "user": "mabshoff"
}
```
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

Issue created by migration from https://trac.sagemath.org/ticket/1573





---

archive/issue_comments_010008.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-12-20T12:18:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1573#issuecomment-10008",
    "user": "mabshoff"
}
```

Attachment



---

archive/issue_comments_010009.json:
```json
{
    "body": "The patch fixes the doctest failures caused by the updated cremona.spkg at #1233.\n\nWith the patch testall passes.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-20T12:47:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1573#issuecomment-10009",
    "user": "mabshoff"
}
```

The patch fixes the doctest failures caused by the updated cremona.spkg at #1233.

With the patch testall passes.

Cheers,

Michael



---

archive/issue_comments_010010.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-20T18:07:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1573#issuecomment-10010",
    "user": "rlm"
}
```

Resolution: fixed



---

archive/issue_comments_010011.json:
```json
{
    "body": "Merged in 2.9.1 alpha2",
    "created_at": "2007-12-20T18:07:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1573#issuecomment-10011",
    "user": "rlm"
}
```

Merged in 2.9.1 alpha2
