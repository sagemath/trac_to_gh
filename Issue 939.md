# Issue 939: segfault in graph_isom.pyx

archive/issues_000939.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\n        sage: import sage.graphs.graph_isom\n        sage: from sage.graphs.graph_isom import search_tree, all_labeled_digraphs_with_loops\n        sage: from sage.graphs.graph import enum\n        sage: Glist = {}\n        sage: Giso  = {}\n        sage: for n in range(1,4):\n        ...    Glist[n] = all_labeled_digraphs_with_loops(n)\n        ...    Giso[n] = []\n        ...    for g in Glist[n]:\n        ...        a, b = search_tree(g, [range(n)], dig=True)\n        ...        inn = False\n        ...        for gi in Giso[n]:\n        ...            if enum(b) == enum(gi):\n        ...                inn = True\n        ...        if not inn:\n        ...            Giso[n].append(b)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/939\n\n",
    "created_at": "2007-10-20T06:55:13Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.8",
    "title": "segfault in graph_isom.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/939",
    "user": "@williamstein"
}
```
Assignee: @williamstein


```
        sage: import sage.graphs.graph_isom
        sage: from sage.graphs.graph_isom import search_tree, all_labeled_digraphs_with_loops
        sage: from sage.graphs.graph import enum
        sage: Glist = {}
        sage: Giso  = {}
        sage: for n in range(1,4):
        ...    Glist[n] = all_labeled_digraphs_with_loops(n)
        ...    Giso[n] = []
        ...    for g in Glist[n]:
        ...        a, b = search_tree(g, [range(n)], dig=True)
        ...        inn = False
        ...        for gi in Giso[n]:
        ...            if enum(b) == enum(gi):
        ...                inn = True
        ...        if not inn:
        ...            Giso[n].append(b)
```


Issue created by migration from https://trac.sagemath.org/ticket/939





---

archive/issue_comments_005741.json:
```json
{
    "body": "In sage-2.8.8 the above doctest will have \n   # not tested since it seg faults\nin every line.  This will stay until things are fixed.",
    "created_at": "2007-10-20T07:20:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/939#issuecomment-5741",
    "user": "@williamstein"
}
```

In sage-2.8.8 the above doctest will have 
   # not tested since it seg faults
in every line.  This will stay until things are fixed.



---

archive/issue_comments_005742.json:
```json
{
    "body": "I am running the code with verbosity level 3, i.e.\n\n```\nimport sage.graphs.graph_isom\nfrom sage.graphs.graph_isom import search_tree, all_labeled_digraphs_with_loops\nfrom sage.graphs.graph import enum\nGlist = {}\nGiso  = {}\nfor n in range(1,4):\n    Glist[n] = all_labeled_digraphs_with_loops(n)\n    Giso[n] = []\n    for g in Glist[n]:\n        a, b = search_tree(g, [range(n)], dig=True, verbosity=3)\n        inn = False\n        for gi in Giso[n]:\n            if enum(b) == enum(gi):\n                inn = True\n        if not inn:\n            Giso[n].append(b)\n```\n\nAfter some playing around it appears that k grows too large and we end up over running the end zb_mpz in step 5:\n\n```\nmpz_set(zf_mpz[k], Lambda_mpz[k])\nmpz_set(zb_mpz[k], Lambda_mpz[k])\n```\n\nk equals 5 in the example from above, while n=4 .\n\nCheers,\n\nMichael",
    "created_at": "2007-10-20T09:20:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/939#issuecomment-5742",
    "user": "mabshoff"
}
```

I am running the code with verbosity level 3, i.e.

```
import sage.graphs.graph_isom
from sage.graphs.graph_isom import search_tree, all_labeled_digraphs_with_loops
from sage.graphs.graph import enum
Glist = {}
Giso  = {}
for n in range(1,4):
    Glist[n] = all_labeled_digraphs_with_loops(n)
    Giso[n] = []
    for g in Glist[n]:
        a, b = search_tree(g, [range(n)], dig=True, verbosity=3)
        inn = False
        for gi in Giso[n]:
            if enum(b) == enum(gi):
                inn = True
        if not inn:
            Giso[n].append(b)
```

After some playing around it appears that k grows too large and we end up over running the end zb_mpz in step 5:

```
mpz_set(zf_mpz[k], Lambda_mpz[k])
mpz_set(zb_mpz[k], Lambda_mpz[k])
```

k equals 5 in the example from above, while n=4 .

Cheers,

Michael



---

archive/issue_comments_005743.json:
```json
{
    "body": "I am under the impression now, that potentially only specific graphs might actually crash search_tree, so it might be interesting to isolate that case and have a closer look.\n\nCheers,\n\nMichael",
    "created_at": "2007-10-20T10:46:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/939#issuecomment-5743",
    "user": "mabshoff"
}
```

I am under the impression now, that potentially only specific graphs might actually crash search_tree, so it might be interesting to isolate that case and have a closer look.

Cheers,

Michael



---

archive/issue_comments_005744.json:
```json
{
    "body": "Valgrind says:\n\n```\n==31660== Conditional jump or move depends on uninitialised value(s)\n==31660==    at 0x4451ED: PyObject_Free (obmalloc.c:920)\n==31660==    by 0x4C7158: code_dealloc (codeobject.c:270)\n==31660==    by 0x4CD46D: frame_dealloc (frameobject.c:444)\n==31660==    by 0x4AC94A: tb_dealloc (traceback.c:34)\n==31660==    by 0x4AC956: tb_dealloc (traceback.c:33)\n==31660==    by 0x4AC956: tb_dealloc (traceback.c:33)\n==31660==    by 0x4AC956: tb_dealloc (traceback.c:33)\n==31660==    by 0x4AC956: tb_dealloc (traceback.c:33)\n==31660==    by 0x4AC956: tb_dealloc (traceback.c:33)\n==31660==    by 0x4AC956: tb_dealloc (traceback.c:33)\n==31660==    by 0x96389BC: __Pyx_GetExcValue (parent.c:6870)\n==31660==    by 0x9648136: __pyx_f_6parent_6Parent_get_action_c_impl (parent.c:2844)\n\n==31660== Use of uninitialised value of size 8\n==31660==    at 0x445206: PyObject_Free (obmalloc.c:920)\n==31660==    by 0x4C7158: code_dealloc (codeobject.c:270)\n==31660==    by 0x4CD46D: frame_dealloc (frameobject.c:444)\n==31660==    by 0x4AC94A: tb_dealloc (traceback.c:34)\n==31660==    by 0x96389BC: __Pyx_GetExcValue (parent.c:6870)\n==31660==    by 0x9646E52: __pyx_f_6parent_6Parent_get_action_c_impl (parent.c:2556)\n==31660==    by 0x963D127: __pyx_f_6parent_6Parent_get_action_c (parent.c:1658)\n==31660==    by 0x99C9FD4: __pyx_f_6coerce_24CoercionModel_cache_maps_discover_action_c (coerce.c:6409)\n==31660==    by 0x99CA974: __pyx_f_6coerce_24CoercionModel_cache_maps_discover_action_c (coerce.c:6824)\n==31660==    by 0x99C1D77: __pyx_f_6coerce_24CoercionModel_cache_maps_get_action_c (coerce.c:6261)\n==31660==    by 0x99DBB96: __pyx_f_6coerce_24CoercionModel_cache_maps_bin_op_c (coerce.c:4515)\n==31660==    by 0x977FCA1: __pyx_f_py_7element_11RingElement___mul__ (element.c:7603)\n```\n\nBut that might be just due to k being \"out of bounds\" again.\n\nCheers,\n\nMichael",
    "created_at": "2007-10-20T17:39:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/939#issuecomment-5744",
    "user": "mabshoff"
}
```

Valgrind says:

```
==31660== Conditional jump or move depends on uninitialised value(s)
==31660==    at 0x4451ED: PyObject_Free (obmalloc.c:920)
==31660==    by 0x4C7158: code_dealloc (codeobject.c:270)
==31660==    by 0x4CD46D: frame_dealloc (frameobject.c:444)
==31660==    by 0x4AC94A: tb_dealloc (traceback.c:34)
==31660==    by 0x4AC956: tb_dealloc (traceback.c:33)
==31660==    by 0x4AC956: tb_dealloc (traceback.c:33)
==31660==    by 0x4AC956: tb_dealloc (traceback.c:33)
==31660==    by 0x4AC956: tb_dealloc (traceback.c:33)
==31660==    by 0x4AC956: tb_dealloc (traceback.c:33)
==31660==    by 0x4AC956: tb_dealloc (traceback.c:33)
==31660==    by 0x96389BC: __Pyx_GetExcValue (parent.c:6870)
==31660==    by 0x9648136: __pyx_f_6parent_6Parent_get_action_c_impl (parent.c:2844)

==31660== Use of uninitialised value of size 8
==31660==    at 0x445206: PyObject_Free (obmalloc.c:920)
==31660==    by 0x4C7158: code_dealloc (codeobject.c:270)
==31660==    by 0x4CD46D: frame_dealloc (frameobject.c:444)
==31660==    by 0x4AC94A: tb_dealloc (traceback.c:34)
==31660==    by 0x96389BC: __Pyx_GetExcValue (parent.c:6870)
==31660==    by 0x9646E52: __pyx_f_6parent_6Parent_get_action_c_impl (parent.c:2556)
==31660==    by 0x963D127: __pyx_f_6parent_6Parent_get_action_c (parent.c:1658)
==31660==    by 0x99C9FD4: __pyx_f_6coerce_24CoercionModel_cache_maps_discover_action_c (coerce.c:6409)
==31660==    by 0x99CA974: __pyx_f_6coerce_24CoercionModel_cache_maps_discover_action_c (coerce.c:6824)
==31660==    by 0x99C1D77: __pyx_f_6coerce_24CoercionModel_cache_maps_get_action_c (coerce.c:6261)
==31660==    by 0x99DBB96: __pyx_f_6coerce_24CoercionModel_cache_maps_bin_op_c (coerce.c:4515)
==31660==    by 0x977FCA1: __pyx_f_py_7element_11RingElement___mul__ (element.c:7603)
```

But that might be just due to k being "out of bounds" again.

Cheers,

Michael



---

archive/issue_comments_005745.json:
```json
{
    "body": "Well, right before the crash the following happens:\n\n```\n==31660== Use of uninitialised value of size 8\n==31660==    at 0x17DBDB63: __pyx_f_10graph_isom_14PartitionStack__degree_inv_square_matrix (graph_isom.c:5129)\n==31660==    by 0x17DBDD7C: __pyx_f_10graph_isom_14PartitionStack__refine_by_square_matrix (graph_isom.c:4378)\n==31660==    by 0x17DDCC69: __pyx_f_py_10graph_isom_search_tree (graph_isom.c:8017)\n==31660==    by 0x415522: PyObject_Call (abstract.c:1860)\n==31660==    by 0x481E91: PyEval_EvalFrameEx (ceval.c:3775)\n==31660==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n==31660==    by 0x483CC4: PyEval_EvalFrameEx (ceval.c:494)\n==31660==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n==31660==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)\n==31660==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n==31660==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)\n==31660==    by 0x48403A: PyEval_EvalFrameEx (ceval.c:3650)\n==31660==\n==31660== Invalid read of size 4\n==31660==    at 0x17DBDB63: __pyx_f_10graph_isom_14PartitionStack__degree_inv_square_matrix (graph_isom.c:5129)\n==31660==    by 0x17DBDD7C: __pyx_f_10graph_isom_14PartitionStack__refine_by_square_matrix (graph_isom.c:4378)\n==31660==    by 0x17DDCC69: __pyx_f_py_10graph_isom_search_tree (graph_isom.c:8017)\n==31660==    by 0x415522: PyObject_Call (abstract.c:1860)\n==31660==    by 0x481E91: PyEval_EvalFrameEx (ceval.c:3775)\n==31660==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n==31660==    by 0x483CC4: PyEval_EvalFrameEx (ceval.c:494)\n==31660==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n==31660==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)\n==31660==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n==31660==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)\n==31660==    by 0x48403A: PyEval_EvalFrameEx (ceval.c:3650)\n==31660==  Address 0x40a4ee08 is not stack'd, malloc'd or (recently) free'd\n```\n\nSo besides the k>n+1 issue there might also be a problem in degree_inv_square_matrix.\n\nCheers,\n\nMichael",
    "created_at": "2007-10-20T17:50:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/939#issuecomment-5745",
    "user": "mabshoff"
}
```

Well, right before the crash the following happens:

```
==31660== Use of uninitialised value of size 8
==31660==    at 0x17DBDB63: __pyx_f_10graph_isom_14PartitionStack__degree_inv_square_matrix (graph_isom.c:5129)
==31660==    by 0x17DBDD7C: __pyx_f_10graph_isom_14PartitionStack__refine_by_square_matrix (graph_isom.c:4378)
==31660==    by 0x17DDCC69: __pyx_f_py_10graph_isom_search_tree (graph_isom.c:8017)
==31660==    by 0x415522: PyObject_Call (abstract.c:1860)
==31660==    by 0x481E91: PyEval_EvalFrameEx (ceval.c:3775)
==31660==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==31660==    by 0x483CC4: PyEval_EvalFrameEx (ceval.c:494)
==31660==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==31660==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)
==31660==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==31660==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)
==31660==    by 0x48403A: PyEval_EvalFrameEx (ceval.c:3650)
==31660==
==31660== Invalid read of size 4
==31660==    at 0x17DBDB63: __pyx_f_10graph_isom_14PartitionStack__degree_inv_square_matrix (graph_isom.c:5129)
==31660==    by 0x17DBDD7C: __pyx_f_10graph_isom_14PartitionStack__refine_by_square_matrix (graph_isom.c:4378)
==31660==    by 0x17DDCC69: __pyx_f_py_10graph_isom_search_tree (graph_isom.c:8017)
==31660==    by 0x415522: PyObject_Call (abstract.c:1860)
==31660==    by 0x481E91: PyEval_EvalFrameEx (ceval.c:3775)
==31660==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==31660==    by 0x483CC4: PyEval_EvalFrameEx (ceval.c:494)
==31660==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==31660==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)
==31660==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==31660==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)
==31660==    by 0x48403A: PyEval_EvalFrameEx (ceval.c:3650)
==31660==  Address 0x40a4ee08 is not stack'd, malloc'd or (recently) free'd
```

So besides the k>n+1 issue there might also be a problem in degree_inv_square_matrix.

Cheers,

Michael



---

archive/issue_comments_005746.json:
```json
{
    "body": "Attachment [7031.patch](tarball://root/attachments/some-uuid/ticket939/7031.patch) by @rlmill created at 2007-10-21 02:38:49\n\nFix.",
    "created_at": "2007-10-21T02:38:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/939#issuecomment-5746",
    "user": "@rlmill"
}
```

Attachment [7031.patch](tarball://root/attachments/some-uuid/ticket939/7031.patch) by @rlmill created at 2007-10-21 02:38:49

Fix.



---

archive/issue_comments_005747.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-21T02:39:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/939#issuecomment-5747",
    "user": "@rlmill"
}
```

Resolution: fixed



---

archive/issue_comments_005748.json:
```json
{
    "body": "Attachment [doctest.patch](tarball://root/attachments/some-uuid/ticket939/doctest.patch) by @williamstein created at 2007-10-21 02:46:12",
    "created_at": "2007-10-21T02:46:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/939#issuecomment-5748",
    "user": "@williamstein"
}
```

Attachment [doctest.patch](tarball://root/attachments/some-uuid/ticket939/doctest.patch) by @williamstein created at 2007-10-21 02:46:12
