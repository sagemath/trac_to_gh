# Issue 4260: use LinBox as native matrix representation for dense matrices over GF(p)

archive/issues_004260.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  simonking @rbeezer drkirkby\n\nKeywords: linbox, linear algebra\n\nCopying to and from LinBox uses up precious RAM and the point of fast linear algebra is to deal with large matrices. We should consider switching to LinBox as the native representation of matrices over GF(p)\n\nIssue created by migration from https://trac.sagemath.org/ticket/4260\n\n",
    "created_at": "2008-10-10T08:54:18Z",
    "labels": [
        "component: linear algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.8",
    "title": "use LinBox as native matrix representation for dense matrices over GF(p)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4260",
    "user": "https://github.com/malb"
}
```
Assignee: @williamstein

CC:  simonking @rbeezer drkirkby

Keywords: linbox, linear algebra

Copying to and from LinBox uses up precious RAM and the point of fast linear algebra is to deal with large matrices. We should consider switching to LinBox as the native representation of matrices over GF(p)

Issue created by migration from https://trac.sagemath.org/ticket/4260





---

archive/issue_comments_030940.json:
```json
{
    "body": "Changing assignee from @williamstein to @ClementPernet.",
    "created_at": "2008-10-10T15:35:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30940",
    "user": "https://github.com/ClementPernet"
}
```

Changing assignee from @williamstein to @ClementPernet.



---

archive/issue_comments_030941.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-10-10T15:35:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30941",
    "user": "https://github.com/ClementPernet"
}
```

Changing status from new to assigned.



---

archive/issue_comments_030942.json:
```json
{
    "body": "I will work on it as a coding sprint at SD10.",
    "created_at": "2008-10-10T15:35:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30942",
    "user": "https://github.com/ClementPernet"
}
```

I will work on it as a coding sprint at SD10.



---

archive/issue_comments_030943.json:
```json
{
    "body": "I finally rebased the patch from SD16. The template class in the patch contains the updates made to the modn_dense class since then, like changes to the `sig_*` functions. Apparently the modn_dense class representation now allows permuting the rows by changing pointers in the `_matrix` array. We can't allow that if we want to pass the `_entries` to linbox, so I skipped those changes.\n\nSage builds with the attached patches, and you can construct matrices. However, there are lots of bugs, some linbox wrappers are still stubs, etc. Expect crashes and wrong results.\n\nWith the patch applied, I get a crash with the following:\n\n\n```\nsage: a = matrix(GF(97),3,4,range(12))\nsage: a.echelonize()\n*** glibc detected *** python: free(): invalid next size (fast): 0x000000000270b370 ***\n======= Backtrace: =========\n<snip>\n```\n\n\nAFAICT, the new cython code is an exact copy of the wrapper function in `linbox-sage.C`. Here is what valgrind says:\n\n\n```\n==3026== Invalid write of size 8\n==3026==    at 0x39E49EF1: T.4552 (ffpack_ludivine.inl:420)\n==3026==    by 0x39E49AA0: T.4552 (ffpack_ludivine.inl:486)\n==3026==    by 0x39E4ABBF: __pyx_pf_4sage_6matrix_24matrix_modn_dense_double_26M\natrix_modn_dense_template_20_echelonize_linbox(_object*, _object*) (ffpack.h:113\n2)\n==3026==    by 0x4E74082: PyObject_Call (abstract.c:2492)\n==3026==    by 0x39E2CA8A: __pyx_pf_4sage_6matrix_24matrix_modn_dense_double_26M\natrix_modn_dense_template_19echelonize(_object*, _object*, _object*) (matrix_mod\nn_dense_double.cpp:8738)\n==3026==    by 0x4F17FF9: PyEval_EvalFrameEx (ceval.c:3706)\n==3026==    by 0x4F19CDC: PyEval_EvalCodeEx (ceval.c:2968)\n==3026==    by 0x4F19DB1: PyEval_EvalCode (ceval.c:522)\n==3026==    by 0x4F19083: PyEval_EvalFrameEx (ceval.c:4401)\n==3026==    by 0x4F19CDC: PyEval_EvalCodeEx (ceval.c:2968)\n<snip lots more Py* lines>\n==3026==  Address 0x6ca16e8 is 0 bytes after a block of size 24 alloc'd\n==3026==    at 0x4C267CE: malloc (vg_replace_malloc.c:236)\n==3026==    by 0x39E4AA5A: __pyx_pf_4sage_6matrix_24matrix_modn_dense_double_26Matrix_modn_dense_template_20_echelonize_linbox(_object*, _object*) (memory.h:32)\n==3026==    by 0x4E74082: PyObject_Call (abstract.c:2492)\n==3026==    by 0x39E2CA8A: __pyx_pf_4sage_6matrix_24matrix_modn_dense_double_26Matrix_modn_dense_template_19echelonize(_object*, _object*, _object*) (matrix_modn_dense_double.cpp:8738)\n==3026==    by 0x4F17FF9: PyEval_EvalFrameEx (ceval.c:3706)\n==3026==    by 0x4F19CDC: PyEval_EvalCodeEx (ceval.c:2968)\n==3026==    by 0x4F19DB1: PyEval_EvalCode (ceval.c:522)\n==3026==    by 0x4F19083: PyEval_EvalFrameEx (ceval.c:4401)\n==3026==    by 0x4F19CDC: PyEval_EvalCodeEx (ceval.c:2968)\n==3026==    by 0x4F18074: PyEval_EvalFrameEx (ceval.c:3802)\n<snip lots of Py* lines>\n```\n\n\nI'd appreciate any pointers about the problem above, though I don't know if I'll have the time to come back to this before the bug days in August (when I presume Martin will take over?).",
    "created_at": "2011-08-02T16:20:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30943",
    "user": "https://github.com/burcin"
}
```

I finally rebased the patch from SD16. The template class in the patch contains the updates made to the modn_dense class since then, like changes to the `sig_*` functions. Apparently the modn_dense class representation now allows permuting the rows by changing pointers in the `_matrix` array. We can't allow that if we want to pass the `_entries` to linbox, so I skipped those changes.

Sage builds with the attached patches, and you can construct matrices. However, there are lots of bugs, some linbox wrappers are still stubs, etc. Expect crashes and wrong results.

With the patch applied, I get a crash with the following:


```
sage: a = matrix(GF(97),3,4,range(12))
sage: a.echelonize()
*** glibc detected *** python: free(): invalid next size (fast): 0x000000000270b370 ***
======= Backtrace: =========
<snip>
```


AFAICT, the new cython code is an exact copy of the wrapper function in `linbox-sage.C`. Here is what valgrind says:


```
==3026== Invalid write of size 8
==3026==    at 0x39E49EF1: T.4552 (ffpack_ludivine.inl:420)
==3026==    by 0x39E49AA0: T.4552 (ffpack_ludivine.inl:486)
==3026==    by 0x39E4ABBF: __pyx_pf_4sage_6matrix_24matrix_modn_dense_double_26M
atrix_modn_dense_template_20_echelonize_linbox(_object*, _object*) (ffpack.h:113
2)
==3026==    by 0x4E74082: PyObject_Call (abstract.c:2492)
==3026==    by 0x39E2CA8A: __pyx_pf_4sage_6matrix_24matrix_modn_dense_double_26M
atrix_modn_dense_template_19echelonize(_object*, _object*, _object*) (matrix_mod
n_dense_double.cpp:8738)
==3026==    by 0x4F17FF9: PyEval_EvalFrameEx (ceval.c:3706)
==3026==    by 0x4F19CDC: PyEval_EvalCodeEx (ceval.c:2968)
==3026==    by 0x4F19DB1: PyEval_EvalCode (ceval.c:522)
==3026==    by 0x4F19083: PyEval_EvalFrameEx (ceval.c:4401)
==3026==    by 0x4F19CDC: PyEval_EvalCodeEx (ceval.c:2968)
<snip lots more Py* lines>
==3026==  Address 0x6ca16e8 is 0 bytes after a block of size 24 alloc'd
==3026==    at 0x4C267CE: malloc (vg_replace_malloc.c:236)
==3026==    by 0x39E4AA5A: __pyx_pf_4sage_6matrix_24matrix_modn_dense_double_26Matrix_modn_dense_template_20_echelonize_linbox(_object*, _object*) (memory.h:32)
==3026==    by 0x4E74082: PyObject_Call (abstract.c:2492)
==3026==    by 0x39E2CA8A: __pyx_pf_4sage_6matrix_24matrix_modn_dense_double_26Matrix_modn_dense_template_19echelonize(_object*, _object*, _object*) (matrix_modn_dense_double.cpp:8738)
==3026==    by 0x4F17FF9: PyEval_EvalFrameEx (ceval.c:3706)
==3026==    by 0x4F19CDC: PyEval_EvalCodeEx (ceval.c:2968)
==3026==    by 0x4F19DB1: PyEval_EvalCode (ceval.c:522)
==3026==    by 0x4F19083: PyEval_EvalFrameEx (ceval.c:4401)
==3026==    by 0x4F19CDC: PyEval_EvalCodeEx (ceval.c:2968)
==3026==    by 0x4F18074: PyEval_EvalFrameEx (ceval.c:3802)
<snip lots of Py* lines>
```


I'd appreciate any pointers about the problem above, though I don't know if I'll have the time to come back to this before the bug days in August (when I presume Martin will take over?).



---

archive/issue_comments_030944.json:
```json
{
    "body": "These are the files in `sage/matrix` with failures:\n\n\n```\n        sage -t  devel/sage-main/sage/matrix/matrix_cyclo_dense.pyx # 22 doctests failed\n        sage -t  devel/sage-main/sage/matrix/strassen.pyx # 2 doctests failed\n        sage -t  devel/sage-main/sage/matrix/matrix0.pyx # 2 doctests failed\n        sage -t  devel/sage-main/sage/matrix/matrix_integer_dense.pyx # 5 doctests failed\n        sage -t  devel/sage-main/sage/matrix/matrix_space.py # 1 doctests failed\n        sage -t  devel/sage-main/sage/matrix/matrix_window_modn_dense.pyx # 1 doctests failed\n        sage -t  devel/sage-main/sage/matrix/matrix_modn_sparse.pyx # 1 doctests failed\n        sage -t  devel/sage-main/sage/matrix/matrix_integer_dense_saturation.py # 0 doctests failed\n        sage -t  devel/sage-main/sage/matrix/matrix_rational_dense.pyx # 44 doctests failed\n        sage -t  devel/sage-main/sage/matrix/matrix2.pyx # Time out\n        sage -t  devel/sage-main/sage/matrix/matrix_modn_dense.pyx # Time out\n        sage -t  devel/sage-main/sage/matrix/matrix_modn_dense_template.pxi # Time out\n```\n",
    "created_at": "2011-08-22T21:07:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30944",
    "user": "https://github.com/rbeezer"
}
```

These are the files in `sage/matrix` with failures:


```
        sage -t  devel/sage-main/sage/matrix/matrix_cyclo_dense.pyx # 22 doctests failed
        sage -t  devel/sage-main/sage/matrix/strassen.pyx # 2 doctests failed
        sage -t  devel/sage-main/sage/matrix/matrix0.pyx # 2 doctests failed
        sage -t  devel/sage-main/sage/matrix/matrix_integer_dense.pyx # 5 doctests failed
        sage -t  devel/sage-main/sage/matrix/matrix_space.py # 1 doctests failed
        sage -t  devel/sage-main/sage/matrix/matrix_window_modn_dense.pyx # 1 doctests failed
        sage -t  devel/sage-main/sage/matrix/matrix_modn_sparse.pyx # 1 doctests failed
        sage -t  devel/sage-main/sage/matrix/matrix_integer_dense_saturation.py # 0 doctests failed
        sage -t  devel/sage-main/sage/matrix/matrix_rational_dense.pyx # 44 doctests failed
        sage -t  devel/sage-main/sage/matrix/matrix2.pyx # Time out
        sage -t  devel/sage-main/sage/matrix/matrix_modn_dense.pyx # Time out
        sage -t  devel/sage-main/sage/matrix/matrix_modn_dense_template.pxi # Time out
```




---

archive/issue_comments_030945.json:
```json
{
    "body": "Attachment [trac_4260-linbox_default.patch](tarball://root/attachments/some-uuid/ticket4260/trac_4260-linbox_default.patch) by @malb created at 2011-08-23 19:15:15\n\nmake matrix space constructor use the new classes",
    "created_at": "2011-08-23T19:15:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30945",
    "user": "https://github.com/malb"
}
```

Attachment [trac_4260-linbox_default.patch](tarball://root/attachments/some-uuid/ticket4260/trac_4260-linbox_default.patch) by @malb created at 2011-08-23 19:15:15

make matrix space constructor use the new classes



---

archive/issue_comments_030946.json:
```json
{
    "body": "I fixed a few issues and segfaults but the thing is far from done. However, one can probably do higher level stuff now, i.e. it shouldn't crash that much any more.\n\nWe need a new LinBox SPKG because `Modular<float>` didn't have a `NonZeroRandIter` which is needed by the charpoly code. LinBox 1.1.7 fixes this issue but I tried unsuccessfully to upgrade to 1.1.7 for like 10 hours (cf. #11718).",
    "created_at": "2011-08-23T19:23:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30946",
    "user": "https://github.com/malb"
}
```

I fixed a few issues and segfaults but the thing is far from done. However, one can probably do higher level stuff now, i.e. it shouldn't crash that much any more.

We need a new LinBox SPKG because `Modular<float>` didn't have a `NonZeroRandIter` which is needed by the charpoly code. LinBox 1.1.7 fixes this issue but I tried unsuccessfully to upgrade to 1.1.7 for like 10 hours (cf. #11718).



---

archive/issue_comments_030947.json:
```json
{
    "body": "Doctest failures with most recent patch on sage.math:\n\n```\n        sage -t  -long -force_lib devel/sage/doc/de/tutorial/tour_advanced.rst # 2 doctests failed\n        sage -t  -long -force_lib devel/sage/doc/en/tutorial/tour_advanced.rst # 2 doctests failed\n        sage -t  -long -force_lib devel/sage/doc/en/bordeaux_2008/modular_forms_and_hecke_operators.rst # 1 doctests failed\n        sage -t  -long -force_lib devel/sage/doc/en/bordeaux_2008/elliptic_curves.rst # 4 doctests failed\n        sage -t  -long -force_lib devel/sage/doc/fr/tutorial/tour_advanced.rst # 2 doctests failed\n        sage -t  -long -force_lib devel/sage/doc/ru/tutorial/tour_advanced.rst # 2 doctests failed\n        sage -t  -long -force_lib devel/sage/sage/modular/modsym/heilbronn.pyx # 2 doctests failed\n        sage -t  -long -force_lib devel/sage/sage/modular/modsym/tests.py # 1 doctests failed\n        sage -t  -long -force_lib devel/sage/sage/modular/modsym/subspace.py # 9 doctests failed\n        sage -t  -long -force_lib devel/sage/sage/modular/modsym/space.py # 18 doctests failed\n        sage -t  -long -force_lib devel/sage/sage/modular/modform/eisenstein_submodule.py # 3 doctests failed\n        sage -t  -long -force_lib devel/sage/sage/modular/modform/tests.py # 1 doctests failed\n        sage -t  -long -force_lib devel/sage/sage/modular/modform/constructor.py # 3 doctests failed\n        sage -t  -long -force_lib devel/sage/sage/modular/modform/space.py # 8 doctests failed\n        sage -t  -long -force_lib devel/sage/sage/modular/modform/ambient.py # 4 doctests failed\n        sage -t  -long -force_lib devel/sage/sage/modular/modform/cuspidal_submodule.py # 6 doctests failed\n        sage -t  -long -force_lib devel/sage/sage/modular/modsym/ambient.py # 4 doctests failed\n        sage -t  -long -force_lib devel/sage/sage/modular/modform/element.py # 11 doctests failed\n        sage -t  -long -force_lib devel/sage/sage/modular/hecke/element.py # 1 doctests failed\n        sage -t  -long -force_lib devel/sage/sage/modular/hecke/hecke_operator.py # 1 doctests failed\n        sage -t  -long -force_lib devel/sage/sage/modular/hecke/module.py # 3 doctests failed\n        sage -t  -long -force_lib devel/sage/sage/modular/abvar/homology.py # 3 doctests failed\n        sage -t  -long -force_lib devel/sage/sage/modular/hecke/submodule.py # 3 doctests failed\n        sage -t  -long -force_lib devel/sage/sage/modular/abvar/torsion_subgroup.py # 4 doctests failed\n        sage -t  -long -force_lib devel/sage/sage/modular/abvar/abvar.py # 4 doctests failed\n        sage -t  -long -force_lib devel/sage/sage/matrix/matrix_cyclo_dense.pyx # 8 doctests failed\n        sage -t  -long -force_lib devel/sage/sage/matrix/matrix2.pyx # 1 doctests failed\n        sage -t  -long -force_lib devel/sage/sage/tests/cmdline.py # 1 doctests failed\n        sage -t  -long -force_lib devel/sage/sage/combinat/symmetric_group_representations.py # 1 doctests failed\n        sage -t  -long -force_lib devel/sage/sage/schemes/elliptic_curves/padics.py # 29 doctests failed\n        sage -t  -long -force_lib devel/sage/sage/schemes/elliptic_curves/padic_lseries.py # 6 doctests failed\n        sage -t  -long -force_lib devel/sage/sage/schemes/elliptic_curves/ell_modular_symbols.py # 2 doctests failed\n        sage -t  -long -force_lib devel/sage/sage/schemes/generic/toric_chow_group.py # 16 doctests failed\n        sage -t  -long -force_lib devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py # 1 doctests failed\n        sage -t  -long -force_lib devel/sage/sage/schemes/elliptic_curves/sha_tate.py # 10 doctests failed\n```\n",
    "created_at": "2011-08-24T01:40:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30947",
    "user": "https://github.com/malb"
}
```

Doctest failures with most recent patch on sage.math:

```
        sage -t  -long -force_lib devel/sage/doc/de/tutorial/tour_advanced.rst # 2 doctests failed
        sage -t  -long -force_lib devel/sage/doc/en/tutorial/tour_advanced.rst # 2 doctests failed
        sage -t  -long -force_lib devel/sage/doc/en/bordeaux_2008/modular_forms_and_hecke_operators.rst # 1 doctests failed
        sage -t  -long -force_lib devel/sage/doc/en/bordeaux_2008/elliptic_curves.rst # 4 doctests failed
        sage -t  -long -force_lib devel/sage/doc/fr/tutorial/tour_advanced.rst # 2 doctests failed
        sage -t  -long -force_lib devel/sage/doc/ru/tutorial/tour_advanced.rst # 2 doctests failed
        sage -t  -long -force_lib devel/sage/sage/modular/modsym/heilbronn.pyx # 2 doctests failed
        sage -t  -long -force_lib devel/sage/sage/modular/modsym/tests.py # 1 doctests failed
        sage -t  -long -force_lib devel/sage/sage/modular/modsym/subspace.py # 9 doctests failed
        sage -t  -long -force_lib devel/sage/sage/modular/modsym/space.py # 18 doctests failed
        sage -t  -long -force_lib devel/sage/sage/modular/modform/eisenstein_submodule.py # 3 doctests failed
        sage -t  -long -force_lib devel/sage/sage/modular/modform/tests.py # 1 doctests failed
        sage -t  -long -force_lib devel/sage/sage/modular/modform/constructor.py # 3 doctests failed
        sage -t  -long -force_lib devel/sage/sage/modular/modform/space.py # 8 doctests failed
        sage -t  -long -force_lib devel/sage/sage/modular/modform/ambient.py # 4 doctests failed
        sage -t  -long -force_lib devel/sage/sage/modular/modform/cuspidal_submodule.py # 6 doctests failed
        sage -t  -long -force_lib devel/sage/sage/modular/modsym/ambient.py # 4 doctests failed
        sage -t  -long -force_lib devel/sage/sage/modular/modform/element.py # 11 doctests failed
        sage -t  -long -force_lib devel/sage/sage/modular/hecke/element.py # 1 doctests failed
        sage -t  -long -force_lib devel/sage/sage/modular/hecke/hecke_operator.py # 1 doctests failed
        sage -t  -long -force_lib devel/sage/sage/modular/hecke/module.py # 3 doctests failed
        sage -t  -long -force_lib devel/sage/sage/modular/abvar/homology.py # 3 doctests failed
        sage -t  -long -force_lib devel/sage/sage/modular/hecke/submodule.py # 3 doctests failed
        sage -t  -long -force_lib devel/sage/sage/modular/abvar/torsion_subgroup.py # 4 doctests failed
        sage -t  -long -force_lib devel/sage/sage/modular/abvar/abvar.py # 4 doctests failed
        sage -t  -long -force_lib devel/sage/sage/matrix/matrix_cyclo_dense.pyx # 8 doctests failed
        sage -t  -long -force_lib devel/sage/sage/matrix/matrix2.pyx # 1 doctests failed
        sage -t  -long -force_lib devel/sage/sage/tests/cmdline.py # 1 doctests failed
        sage -t  -long -force_lib devel/sage/sage/combinat/symmetric_group_representations.py # 1 doctests failed
        sage -t  -long -force_lib devel/sage/sage/schemes/elliptic_curves/padics.py # 29 doctests failed
        sage -t  -long -force_lib devel/sage/sage/schemes/elliptic_curves/padic_lseries.py # 6 doctests failed
        sage -t  -long -force_lib devel/sage/sage/schemes/elliptic_curves/ell_modular_symbols.py # 2 doctests failed
        sage -t  -long -force_lib devel/sage/sage/schemes/generic/toric_chow_group.py # 16 doctests failed
        sage -t  -long -force_lib devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py # 1 doctests failed
        sage -t  -long -force_lib devel/sage/sage/schemes/elliptic_curves/sha_tate.py # 10 doctests failed
```




---

archive/issue_comments_030948.json:
```json
{
    "body": "I've fixed all the easy stuff which brings the doctest failures down to:\n\n\n```\nsage -t  -long devel/sage/doc/en/bordeaux_2008/elliptic_curves.rst # 4 doctests failed\nsage -t  -long devel/sage/sage/modular/modsym/subspace.py # 9 doctests failed\nsage -t  -long devel/sage/sage/modular/modsym/space.py # 18 doctests failed\nsage -t  -long devel/sage/sage/modular/modform/eisenstein_submodule.py # 3 doctests failed\nsage -t  -long devel/sage/sage/modular/modform/constructor.py # 3 doctests failed\nsage -t  -long devel/sage/sage/modular/modform/space.py # 8 doctests failed\nsage -t  -long devel/sage/sage/modular/modform/ambient.py # 4 doctests failed\nsage -t  -long devel/sage/sage/modular/hecke/element.py # 1 doctests failed\nsage -t  -long devel/sage/sage/modular/hecke/hecke_operator.py # 1 doctests failed\nsage -t  -long devel/sage/sage/modular/hecke/module.py # 3 doctests failed\nsage -t  -long devel/sage/sage/modular/abvar/homology.py # 3 doctests failed\nsage -t  -long devel/sage/sage/modular/hecke/submodule.py # 3 doctests failed\nsage -t  -long devel/sage/sage/modular/abvar/torsion_subgroup.py # 4 doctests failed\nsage -t  -long devel/sage/sage/modular/abvar/abvar.py # 4 doctests failed\nsage -t  -long devel/sage/sage/combinat/symmetric_group_representations.py # 1 doctests failed\nsage -t  -long devel/sage/sage/schemes/elliptic_curves/padics.py # 29 doctests failed\nsage -t  -long devel/sage/sage/schemes/elliptic_curves/padic_lseries.py # 6 doctests failed\nsage -t  -long devel/sage/sage/schemes/elliptic_curves/ell_modular_symbols.py # 2 doctests failed\nsage -t  -long devel/sage/sage/schemes/generic/toric_chow_group.py # 16 doctests failed\nsage -t  -long devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py # 1 doctests failed\nsage -t  -long devel/sage/sage/schemes/elliptic_curves/sha_tate.py # 10 doctests failed\n```\n\n\nmany of which seem to be caused by a small set of bugs.",
    "created_at": "2011-08-24T02:31:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30948",
    "user": "https://github.com/malb"
}
```

I've fixed all the easy stuff which brings the doctest failures down to:


```
sage -t  -long devel/sage/doc/en/bordeaux_2008/elliptic_curves.rst # 4 doctests failed
sage -t  -long devel/sage/sage/modular/modsym/subspace.py # 9 doctests failed
sage -t  -long devel/sage/sage/modular/modsym/space.py # 18 doctests failed
sage -t  -long devel/sage/sage/modular/modform/eisenstein_submodule.py # 3 doctests failed
sage -t  -long devel/sage/sage/modular/modform/constructor.py # 3 doctests failed
sage -t  -long devel/sage/sage/modular/modform/space.py # 8 doctests failed
sage -t  -long devel/sage/sage/modular/modform/ambient.py # 4 doctests failed
sage -t  -long devel/sage/sage/modular/hecke/element.py # 1 doctests failed
sage -t  -long devel/sage/sage/modular/hecke/hecke_operator.py # 1 doctests failed
sage -t  -long devel/sage/sage/modular/hecke/module.py # 3 doctests failed
sage -t  -long devel/sage/sage/modular/abvar/homology.py # 3 doctests failed
sage -t  -long devel/sage/sage/modular/hecke/submodule.py # 3 doctests failed
sage -t  -long devel/sage/sage/modular/abvar/torsion_subgroup.py # 4 doctests failed
sage -t  -long devel/sage/sage/modular/abvar/abvar.py # 4 doctests failed
sage -t  -long devel/sage/sage/combinat/symmetric_group_representations.py # 1 doctests failed
sage -t  -long devel/sage/sage/schemes/elliptic_curves/padics.py # 29 doctests failed
sage -t  -long devel/sage/sage/schemes/elliptic_curves/padic_lseries.py # 6 doctests failed
sage -t  -long devel/sage/sage/schemes/elliptic_curves/ell_modular_symbols.py # 2 doctests failed
sage -t  -long devel/sage/sage/schemes/generic/toric_chow_group.py # 16 doctests failed
sage -t  -long devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py # 1 doctests failed
sage -t  -long devel/sage/sage/schemes/elliptic_curves/sha_tate.py # 10 doctests failed
```


many of which seem to be caused by a small set of bugs.



---

archive/issue_comments_030949.json:
```json
{
    "body": "Here's where we are at on sage.math:\n\n\n```\nsage -t  devel/sage/doc/en/bordeaux_2008/elliptic_curves.rst # 4 doctests failed\nsage -t  devel/sage/sage/modular/modsym/subspace.py # 9 doctests failed\nsage -t  devel/sage/sage/modular/modsym/space.py # 12 doctests failed\nsage -t  devel/sage/sage/modular/modform/eisenstein_submodule.py # 1 doctests failed\nsage -t  devel/sage/sage/modular/modform/space.py # 7 doctests failed\nsage -t  devel/sage/sage/modular/modform/constructor.py # 1 doctests failed\nsage -t  devel/sage/sage/modular/modform/ambient.py # 4 doctests failed\nsage -t  devel/sage/sage/modular/hecke/element.py # 1 doctests failed\nsage -t  devel/sage/sage/modular/hecke/hecke_operator.py # 1 doctests failed\nsage -t  devel/sage/sage/modular/hecke/module.py # 3 doctests failed\nsage -t  devel/sage/sage/modular/abvar/homology.py # 3 doctests failed\nsage -t  devel/sage/sage/modular/abvar/torsion_subgroup.py # 4 doctests failed\nsage -t  devel/sage/sage/modular/hecke/submodule.py # 3 doctests failed\nsage -t  devel/sage/sage/modular/abvar/abvar.py # 4 doctests failed\nsage -t  devel/sage/sage/structure/sage_object.pyx # 1 doctests failed\nsage -t  devel/sage/sage/combinat/symmetric_group_representations.py # 1 doctests failed\nsage -t  devel/sage/sage/schemes/elliptic_curves/padics.py # 29 doctests failed\nsage -t  devel/sage/sage/schemes/elliptic_curves/padic_lseries.py # 6 doctests failed\nsage -t  devel/sage/sage/schemes/elliptic_curves/ell_modular_symbols.py # 2 doctests failed\nsage -t  devel/sage/sage/schemes/generic/toric_chow_group.py # 16 doctests failed\nsage -t  devel/sage/sage/schemes/elliptic_curves/sha_tate.py # 10 doctests failed\nsage -t  devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py # 1 doctests failed\n```\n",
    "created_at": "2011-08-24T08:08:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30949",
    "user": "https://github.com/malb"
}
```

Here's where we are at on sage.math:


```
sage -t  devel/sage/doc/en/bordeaux_2008/elliptic_curves.rst # 4 doctests failed
sage -t  devel/sage/sage/modular/modsym/subspace.py # 9 doctests failed
sage -t  devel/sage/sage/modular/modsym/space.py # 12 doctests failed
sage -t  devel/sage/sage/modular/modform/eisenstein_submodule.py # 1 doctests failed
sage -t  devel/sage/sage/modular/modform/space.py # 7 doctests failed
sage -t  devel/sage/sage/modular/modform/constructor.py # 1 doctests failed
sage -t  devel/sage/sage/modular/modform/ambient.py # 4 doctests failed
sage -t  devel/sage/sage/modular/hecke/element.py # 1 doctests failed
sage -t  devel/sage/sage/modular/hecke/hecke_operator.py # 1 doctests failed
sage -t  devel/sage/sage/modular/hecke/module.py # 3 doctests failed
sage -t  devel/sage/sage/modular/abvar/homology.py # 3 doctests failed
sage -t  devel/sage/sage/modular/abvar/torsion_subgroup.py # 4 doctests failed
sage -t  devel/sage/sage/modular/hecke/submodule.py # 3 doctests failed
sage -t  devel/sage/sage/modular/abvar/abvar.py # 4 doctests failed
sage -t  devel/sage/sage/structure/sage_object.pyx # 1 doctests failed
sage -t  devel/sage/sage/combinat/symmetric_group_representations.py # 1 doctests failed
sage -t  devel/sage/sage/schemes/elliptic_curves/padics.py # 29 doctests failed
sage -t  devel/sage/sage/schemes/elliptic_curves/padic_lseries.py # 6 doctests failed
sage -t  devel/sage/sage/schemes/elliptic_curves/ell_modular_symbols.py # 2 doctests failed
sage -t  devel/sage/sage/schemes/generic/toric_chow_group.py # 16 doctests failed
sage -t  devel/sage/sage/schemes/elliptic_curves/sha_tate.py # 10 doctests failed
sage -t  devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py # 1 doctests failed
```




---

archive/issue_comments_030950.json:
```json
{
    "body": "With the updated patch we are down to:\n\n\n```\nsage -t  -long devel/sage/sage/modular/modsym/heilbronn.pyx # 2 doctests failed\nsage -t  -long devel/sage/sage/modular/abvar/homology.py # 3 doctests failed\n```\n\n\nHowever, there also seems to be a doctest failure in `matrix2.pyx` which is not that easily reproduced.",
    "created_at": "2011-08-25T01:40:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30950",
    "user": "https://github.com/malb"
}
```

With the updated patch we are down to:


```
sage -t  -long devel/sage/sage/modular/modsym/heilbronn.pyx # 2 doctests failed
sage -t  -long devel/sage/sage/modular/abvar/homology.py # 3 doctests failed
```


However, there also seems to be a doctest failure in `matrix2.pyx` which is not that easily reproduced.



---

archive/issue_comments_030951.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-08-25T02:42:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30951",
    "user": "https://github.com/malb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_030952.json:
```json
{
    "body": "Now all doctests should pass!",
    "created_at": "2011-08-25T02:42:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30952",
    "user": "https://github.com/malb"
}
```

Now all doctests should pass!



---

archive/issue_comments_030953.json:
```json
{
    "body": "Changing keywords from \"linbox, linear algebra\" to \"linbox, linear algebra, sd32\".",
    "created_at": "2011-08-25T05:21:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30953",
    "user": "https://github.com/williamstein"
}
```

Changing keywords from "linbox, linear algebra" to "linbox, linear algebra, sd32".



---

archive/issue_comments_030954.json:
```json
{
    "body": "Attachment [trac_4260-dense_ctypes_template.patch](tarball://root/attachments/some-uuid/ticket4260/trac_4260-dense_ctypes_template.patch) by @malb created at 2011-08-25 07:13:53\n\nadd templated classes for float and double representation",
    "created_at": "2011-08-25T07:13:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30954",
    "user": "https://github.com/malb"
}
```

Attachment [trac_4260-dense_ctypes_template.patch](tarball://root/attachments/some-uuid/ticket4260/trac_4260-dense_ctypes_template.patch) by @malb created at 2011-08-25 07:13:53

add templated classes for float and double representation



---

archive/issue_comments_030955.json:
```json
{
    "body": "I adapted the crossover from `float` to `double`. Around 2<sup>11</sup> `Modular<float>`} is **really** slow because there are not enough bits left to let ATLAS do it's magic, i.e., too many modular reductions. On my computer using `Modular<float>` up to 2<sup>8</sup> seems like a good choice. On sage.math this choice isn't too bad (but not optimal). Multiplying two 1,000 x 1,000 matrices over GF(p) (2nd column) which is smaller than 2<sup>i</sup> (1st column) and the time it takes:\n\n\n```\n 2          3 0.22000\n 3          7 0.24000\n 4         13 0.24000\n 5         31 0.25000\n 6         61 0.26000\n 7        127 0.26000\n 8        251 0.62000\n 9        509 0.38000 <=== using Modular<double> now\n10       1021 0.38000\n11       2039 0.39000\n12       4093 0.39000\n13       8191 0.40000\n14      16381 0.41000\n15      32749 0.41000\n16      65521 0.42000\n17     131071 0.43000\n18     262139 0.43000\n19     524287 0.44000\n20    1048573 0.44000\n21    2097143 0.45000\n22    4194301 0.66000\n23    8388593 1.91000 <=== Generic matrices\n```\n",
    "created_at": "2011-08-25T08:00:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30955",
    "user": "https://github.com/malb"
}
```

I adapted the crossover from `float` to `double`. Around 2<sup>11</sup> `Modular<float>`} is **really** slow because there are not enough bits left to let ATLAS do it's magic, i.e., too many modular reductions. On my computer using `Modular<float>` up to 2<sup>8</sup> seems like a good choice. On sage.math this choice isn't too bad (but not optimal). Multiplying two 1,000 x 1,000 matrices over GF(p) (2nd column) which is smaller than 2<sup>i</sup> (1st column) and the time it takes:


```
 2          3 0.22000
 3          7 0.24000
 4         13 0.24000
 5         31 0.25000
 6         61 0.26000
 7        127 0.26000
 8        251 0.62000
 9        509 0.38000 <=== using Modular<double> now
10       1021 0.38000
11       2039 0.39000
12       4093 0.39000
13       8191 0.40000
14      16381 0.41000
15      32749 0.41000
16      65521 0.42000
17     131071 0.43000
18     262139 0.43000
19     524287 0.44000
20    1048573 0.44000
21    2097143 0.45000
22    4194301 0.66000
23    8388593 1.91000 <=== Generic matrices
```




---

archive/issue_comments_030956.json:
```json
{
    "body": "I found that the time for computing echelon form became worse:\n\nsage-4.6.2\n\n```\nsage: MS = MatrixSpace(GF(101),2000,2000)\nsage: %time A = MS.random_element()\nCPU times: user 0.17 s, sys: 0.03 s, total: 0.20 s\nWall time: 0.20 s\nsage: B = MS.random_element()\nsage: %time C = A*B\nCPU times: user 8.35 s, sys: 0.07 s, total: 8.42 s\nWall time: 8.45 s\nsage: %time A.echelonize()\nCPU times: user 1.22 s, sys: 0.06 s, total: 1.28 s\nWall time: 1.38 s\n```\n\n\nsage-4.7.2.alpha2 with the patches and spkg from here:\n\n```\nsage: MS = MatrixSpace(GF(101),2000,2000)\nsage: %time A = MS.random_element()\nCPU times: user 0.19 s, sys: 0.03 s, total: 0.22 s\nWall time: 0.22 s\nsage: B = MS.random_element()\nsage:  %time C = A*B\nCPU times: user 1.16 s, sys: 0.02 s, total: 1.17 s\nWall time: 1.22 s\nsage: %time A.echelonize()\nCPU times: user 1.87 s, sys: 0.00 s, total: 1.87 s\nWall time: 1.92 s\n```\n",
    "created_at": "2011-08-26T12:09:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30956",
    "user": "https://github.com/simon-king-jena"
}
```

I found that the time for computing echelon form became worse:

sage-4.6.2

```
sage: MS = MatrixSpace(GF(101),2000,2000)
sage: %time A = MS.random_element()
CPU times: user 0.17 s, sys: 0.03 s, total: 0.20 s
Wall time: 0.20 s
sage: B = MS.random_element()
sage: %time C = A*B
CPU times: user 8.35 s, sys: 0.07 s, total: 8.42 s
Wall time: 8.45 s
sage: %time A.echelonize()
CPU times: user 1.22 s, sys: 0.06 s, total: 1.28 s
Wall time: 1.38 s
```


sage-4.7.2.alpha2 with the patches and spkg from here:

```
sage: MS = MatrixSpace(GF(101),2000,2000)
sage: %time A = MS.random_element()
CPU times: user 0.19 s, sys: 0.03 s, total: 0.22 s
Wall time: 0.22 s
sage: B = MS.random_element()
sage:  %time C = A*B
CPU times: user 1.16 s, sys: 0.02 s, total: 1.17 s
Wall time: 1.22 s
sage: %time A.echelonize()
CPU times: user 1.87 s, sys: 0.00 s, total: 1.87 s
Wall time: 1.92 s
```




---

archive/issue_comments_030957.json:
```json
{
    "body": "Attachment [trac_4260_more_doctests.patch](tarball://root/attachments/some-uuid/ticket4260/trac_4260_more_doctests.patch) by @malb created at 2011-08-26 12:42:27",
    "created_at": "2011-08-26T12:42:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30957",
    "user": "https://github.com/malb"
}
```

Attachment [trac_4260_more_doctests.patch](tarball://root/attachments/some-uuid/ticket4260/trac_4260_more_doctests.patch) by @malb created at 2011-08-26 12:42:27



---

archive/issue_comments_030958.json:
```json
{
    "body": "* renamed Rob's patch to fix ticket number\n  * (hopefully) added doctests for every single function\n  * Simon, can you try again after setting `MAX_MODULUS` in sage.matrix.matrix_modn_dense_float to 2<sup>6</sup>? This forces the use of doubles for GF(101) which might be more efficient. Also, how fast is `A.echelonize('gauss')` for you on that benchmark?",
    "created_at": "2011-08-26T12:45:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30958",
    "user": "https://github.com/malb"
}
```

* renamed Rob's patch to fix ticket number
  * (hopefully) added doctests for every single function
  * Simon, can you try again after setting `MAX_MODULUS` in sage.matrix.matrix_modn_dense_float to 2<sup>6</sup>? This forces the use of doubles for GF(101) which might be more efficient. Also, how fast is `A.echelonize('gauss')` for you on that benchmark?



---

archive/issue_comments_030959.json:
```json
{
    "body": "Replying to [comment:17 malb]:\n>  * Simon, can you try again after setting `MAX_MODULUS` in sage.matrix.matrix_modn_dense_float to 2<sup>6</sup>? This forces the use of doubles for GF(101) which might be more efficient.\n\nIt isn't:\n\n```\nsage: sage.matrix.matrix_modn_dense_float.MAX_MODULUS = 2^6\nsage: MS = MatrixSpace(GF(101),2000,2000)\nsage: %time A = MS.random_element()\nCPU times: user 0.21 s, sys: 0.01 s, total: 0.22 s\nWall time: 0.22 s\nsage: B = MS.random_element()\nsage: %time C = A*B\nCPU times: user 1.88 s, sys: 0.04 s, total: 1.92 s\nWall time: 1.93 s\nsage: %time A.echelonize()\nCPU times: user 2.65 s, sys: 0.00 s, total: 2.65 s\nWall time: 2.69 s\nsage: type(A)\n<type 'sage.matrix.matrix_modn_dense_double.Matrix_modn_dense_double'>\n```\n\n\n> Also, how fast is `A.echelonize('gauss')` for you on that benchmark?\n\nYou mean \"how slow\", I suppose:\n\n```\nsage: A = MS.random_element()\nsage: %time A.echelonize('gauss')\nCPU times: user 41.53 s, sys: 0.10 s, total: 41.63 s\nWall time: 41.75 s\n```\n",
    "created_at": "2011-08-26T12:58:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30959",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:17 malb]:
>  * Simon, can you try again after setting `MAX_MODULUS` in sage.matrix.matrix_modn_dense_float to 2<sup>6</sup>? This forces the use of doubles for GF(101) which might be more efficient.

It isn't:

```
sage: sage.matrix.matrix_modn_dense_float.MAX_MODULUS = 2^6
sage: MS = MatrixSpace(GF(101),2000,2000)
sage: %time A = MS.random_element()
CPU times: user 0.21 s, sys: 0.01 s, total: 0.22 s
Wall time: 0.22 s
sage: B = MS.random_element()
sage: %time C = A*B
CPU times: user 1.88 s, sys: 0.04 s, total: 1.92 s
Wall time: 1.93 s
sage: %time A.echelonize()
CPU times: user 2.65 s, sys: 0.00 s, total: 2.65 s
Wall time: 2.69 s
sage: type(A)
<type 'sage.matrix.matrix_modn_dense_double.Matrix_modn_dense_double'>
```


> Also, how fast is `A.echelonize('gauss')` for you on that benchmark?

You mean "how slow", I suppose:

```
sage: A = MS.random_element()
sage: %time A.echelonize('gauss')
CPU times: user 41.53 s, sys: 0.10 s, total: 41.63 s
Wall time: 41.75 s
```




---

archive/issue_comments_030960.json:
```json
{
    "body": "Okay, so both the old code and this patch call LinBox but with the patch it's slower (I can reproduce your timing difference). Hence, we'll have to check what LinBox in the old version ends up doing vs. what it is doing now.",
    "created_at": "2011-08-26T13:10:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30960",
    "user": "https://github.com/malb"
}
```

Okay, so both the old code and this patch call LinBox but with the patch it's slower (I can reproduce your timing difference). Hence, we'll have to check what LinBox in the old version ends up doing vs. what it is doing now.



---

archive/issue_comments_030961.json:
```json
{
    "body": "A word about the regression (I'm copying my reply to malb on linbox-devel)\n\nThe new code (that I wrote )\n\n```\nsize_t r = FFPACK::ReducedRowEchelonForm(F, nrows, ncols, matrix, ncols, P,Q);\n```\n\n\ncalls the actual RowEchelon elimination in FFPACK, which transforms A into its redrowechelon form E and the transformation matrix U (both matrices being magically stored inplace in A)\n\nIt is slower than the older code sage-4.6 using linbox-1.1.6:\n\n\n```\nint rank = EF.rowReducedEchelon(E, A);\n```\n\n\nThe latter computes the redrowechlon (actually the trans of the redcolechelon), but no transformation matrix.\nThis saves roughly 50% of the total number of arithmetic ops (1n^3 rather than 2n^3), and explains the regression.\n\nSwitching back to the old way should fix the regression (for a quick fix).\nAnd I still need to add the feature of not computing the transform at the level of FFPACK, since I expect some timing improvements over the old version in linbox  1.1.6.",
    "created_at": "2011-08-31T13:54:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30961",
    "user": "https://github.com/ClementPernet"
}
```

A word about the regression (I'm copying my reply to malb on linbox-devel)

The new code (that I wrote )

```
size_t r = FFPACK::ReducedRowEchelonForm(F, nrows, ncols, matrix, ncols, P,Q);
```


calls the actual RowEchelon elimination in FFPACK, which transforms A into its redrowechelon form E and the transformation matrix U (both matrices being magically stored inplace in A)

It is slower than the older code sage-4.6 using linbox-1.1.6:


```
int rank = EF.rowReducedEchelon(E, A);
```


The latter computes the redrowechlon (actually the trans of the redcolechelon), but no transformation matrix.
This saves roughly 50% of the total number of arithmetic ops (1n^3 rather than 2n^3), and explains the regression.

Switching back to the old way should fix the regression (for a quick fix).
And I still need to add the feature of not computing the transform at the level of FFPACK, since I expect some timing improvements over the old version in linbox  1.1.6.



---

archive/issue_comments_030962.json:
```json
{
    "body": "Hi Clement, \n\nthanks for explaining. I always forget about the transformation matrix (e.g., that in fact M4RI is even faster than Magma than previously thought, because we always compute the transformation matrix and yet we are faster :)). I'll try to \"switch back\". Btw. is there a way to construct the right matrices without copying?\n\nPS: I didn't get your reply on [linbox-devel] btw.",
    "created_at": "2011-09-01T09:52:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30962",
    "user": "https://github.com/malb"
}
```

Hi Clement, 

thanks for explaining. I always forget about the transformation matrix (e.g., that in fact M4RI is even faster than Magma than previously thought, because we always compute the transformation matrix and yet we are faster :)). I'll try to "switch back". Btw. is there a way to construct the right matrices without copying?

PS: I didn't get your reply on [linbox-devel] btw.



---

archive/issue_comments_030963.json:
```json
{
    "body": "The additional patch makes us use the old EchelonFormDomain interface which is twice as fast (as Cl\u00e9ment explained). Simon, can you review this ticket?",
    "created_at": "2011-09-27T13:32:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30963",
    "user": "https://github.com/malb"
}
```

The additional patch makes us use the old EchelonFormDomain interface which is twice as fast (as Clément explained). Simon, can you review this ticket?



---

archive/issue_comments_030964.json:
```json
{
    "body": "Attachment [trac_4260-minor_fixes.patch](tarball://root/attachments/some-uuid/ticket4260/trac_4260-minor_fixes.patch) by @burcin created at 2011-09-29 16:08:30\n\nminor fixes",
    "created_at": "2011-09-29T16:08:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30964",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_4260-minor_fixes.patch](tarball://root/attachments/some-uuid/ticket4260/trac_4260-minor_fixes.patch) by @burcin created at 2011-09-29 16:08:30

minor fixes



---

archive/issue_comments_030965.json:
```json
{
    "body": "attachment:trac_4260-minor_fixes.patch\n* makes some cosmetic changes and\n* fixes a possible memory leak if allocation of these matrices fail.\n\nI read through the patches and the resulting code. All looks good to me. Please switch this to positive review if my patch is ok.\n\nThanks everyone for finally finishing this off.",
    "created_at": "2011-09-29T16:10:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30965",
    "user": "https://github.com/burcin"
}
```

attachment:trac_4260-minor_fixes.patch
* makes some cosmetic changes and
* fixes a possible memory leak if allocation of these matrices fail.

I read through the patches and the resulting code. All looks good to me. Please switch this to positive review if my patch is ok.

Thanks everyone for finally finishing this off.



---

archive/issue_comments_030966.json:
```json
{
    "body": "Changing keywords from \"linbox, linear algebra, sd32\" to \"linbox, linear algebra, sd32, sd34\".",
    "created_at": "2011-09-29T16:10:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30966",
    "user": "https://github.com/burcin"
}
```

Changing keywords from "linbox, linear algebra, sd32" to "linbox, linear algebra, sd32, sd34".



---

archive/issue_comments_030967.json:
```json
{
    "body": "Burcin's patch looks good. Thus, giving it a **positive review**. I'm also running doctests again against 4.7.2.alpha3.",
    "created_at": "2011-09-29T16:26:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30967",
    "user": "https://github.com/malb"
}
```

Burcin's patch looks good. Thus, giving it a **positive review**. I'm also running doctests again against 4.7.2.alpha3.



---

archive/issue_comments_030968.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-09-29T16:26:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30968",
    "user": "https://github.com/malb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_030969.json:
```json
{
    "body": "Doctests indeed pass on sage.math.",
    "created_at": "2011-09-29T20:48:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30969",
    "user": "https://github.com/malb"
}
```

Doctests indeed pass on sage.math.



---

archive/issue_comments_030970.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-10-10T10:07:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30970",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_030971.json:
```json
{
    "body": "The spkg could do with some cleanup:\n1. What is the purpose of `spkg-rebuild`?  If it is not used, remove it.  If it is used, document it.\n2. `spkg-debian` and the `dist` directory should be removed.  They are leftovers for Debian, but these are now being removed from every spkg.\n3. Why is \"linbox\" in `.hgignore`?\n4. The file `patches/commentator.C` lacks a corresponding `.patch` file.\n\nOptional:\n5. Make `spkg-install` use `patch` for patching.",
    "created_at": "2011-10-10T10:07:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30971",
    "user": "https://github.com/jdemeyer"
}
```

The spkg could do with some cleanup:
1. What is the purpose of `spkg-rebuild`?  If it is not used, remove it.  If it is used, document it.
2. `spkg-debian` and the `dist` directory should be removed.  They are leftovers for Debian, but these are now being removed from every spkg.
3. Why is "linbox" in `.hgignore`?
4. The file `patches/commentator.C` lacks a corresponding `.patch` file.

Optional:
5. Make `spkg-install` use `patch` for patching.



---

archive/issue_comments_030972.json:
```json
{
    "body": "> What is the purpose of spkg-rebuild? If it is not used, remove it. If it is used, document it.\n\nremoved\n\n> spkg-debian and the dist directory should be removed. They are leftovers for Debian, but these are now being removed from every spkg.\n\nremoved\n\n> Why is \"linbox\" in .hgignore?\n\nremoved\n\n> The file patches/commentator.C lacks a corresponding .patch file.\n\nadded\n\n> Make spkg-install use patch for patching.\n\nleft for another time",
    "created_at": "2011-10-10T16:17:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30972",
    "user": "https://github.com/malb"
}
```

> What is the purpose of spkg-rebuild? If it is not used, remove it. If it is used, document it.

removed

> spkg-debian and the dist directory should be removed. They are leftovers for Debian, but these are now being removed from every spkg.

removed

> Why is "linbox" in .hgignore?

removed

> The file patches/commentator.C lacks a corresponding .patch file.

added

> Make spkg-install use patch for patching.

left for another time



---

archive/issue_comments_030973.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-10-10T16:17:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30973",
    "user": "https://github.com/malb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_030974.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-10-12T07:34:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30974",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_004499.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-10-12T07:34:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4260#event-4499"
}
```



---

archive/issue_comments_030975.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2011-11-03T09:01:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30975",
    "user": "https://github.com/jdemeyer"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_030976.json:
```json
{
    "body": "Unfortunately, there are failures on OS X 10.4 PPC, all in the file `sage/matrix/matrix_modn_dense_double.pyx`:\n\n```\nsage -t  -long -force_lib devel/sage/sage/matrix/matrix_modn_dense_double.pyx\n**********************************************************************\nFile \"/Users/jdemeyer/sage-4.7.3.alpha0/devel/sage-main/sage/matrix/matrix_modn_dense_double.pyx\", line 71:\n    sage: A[0,0] = 220082r; A\nExpected:\n    [ 220082 2824836  765701 2282256]\n    [1795330  767112 2967421 1373921]\n    [2757699 1142917 2720973 2877160]\n    [1674049 1341486 2641133 2173280]\nGot:\n    [      0 2824836  765701 2282256]\n    [1795330  767112 2967421 1373921]\n    [2757699 1142917 2720973 2877160]\n    [1674049 1341486 2641133 2173280]\n**********************************************************************\nFile \"/Users/jdemeyer/sage-4.7.3.alpha0/devel/sage-main/sage/matrix/matrix_modn_dense_double.pyx\", line 76:\n    sage: a = A[0,0]; a\nExpected:\n    220082\nGot:\n    0\n**********************************************************************\nFile \"/Users/jdemeyer/sage-4.7.3.alpha0/devel/sage-main/sage/matrix/matrix_modn_dense_double.pyx\", line 78:\n    sage: ~a\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/jdemeyer/sage-4.7.3.alpha0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/Users/jdemeyer/sage-4.7.3.alpha0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/Users/jdemeyer/sage-4.7.3.alpha0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_2[5]>\", line 1, in <module>\n        ~a###line 78:\n    sage: ~a\n      File \"integer_mod.pyx\", line 3240, in sage.rings.finite_rings.integer_mod.IntegerMod_int64.__invert__ (sage/rings/finite_rings/integer_mod.c:25534)\n      File \"integer_mod.pyx\", line 3371, in sage.rings.finite_rings.integer_mod.mod_inverse_int64 (sage/rings/finite_rings/integer_mod.c:26331)\n    ZeroDivisionError: Inverse does not exist.\n**********************************************************************\nFile \"/Users/jdemeyer/sage-4.7.3.alpha0/devel/sage-main/sage/matrix/matrix_modn_dense_double.pyx\", line 86:\n    sage: A[0,0] = 220082r; A\nExpected:\n    [ 220082 1237101 2033003 3788106]\n    [4649912 1157595 4928315 4382585]\n    [4252686  978867 2601478 1759921]\n    [1303120 1860486 3405811 2203284]\nGot:\n    [      0 1237101 2033003 3788106]\n    [4649912 1157595 4928315 4382585]\n    [4252686  978867 2601478 1759921]\n    [1303120 1860486 3405811 2203284]\n**********************************************************************\nFile \"/Users/jdemeyer/sage-4.7.3.alpha0/devel/sage-main/sage/matrix/matrix_modn_dense_double.pyx\", line 91:\n    sage: a = A[0,0]; a\nExpected:\n    220082\nGot:\n    0\n**********************************************************************\nFile \"/Users/jdemeyer/sage-4.7.3.alpha0/devel/sage-main/sage/matrix/matrix_modn_dense_double.pyx\", line 93:\n    sage: a*a\nExpected:\n    4777936\nGot:\n    0\n**********************************************************************\nFile \"/Users/jdemeyer/sage-4.7.3.alpha0/devel/sage-main/sage/matrix/matrix_modn_dense_double.pyx\", line 112:\n    sage: A[0,0] = K(220082); A\nExpected:\n    [ 220082 2824836  765701 2282256]\n    [1795330  767112 2967421 1373921]\n    [2757699 1142917 2720973 2877160]\n    [1674049 1341486 2641133 2173280]\nGot:\n    [      0 2824836  765701 2282256]\n    [1795330  767112 2967421 1373921]\n    [2757699 1142917 2720973 2877160]\n    [1674049 1341486 2641133 2173280]\n**********************************************************************\nFile \"/Users/jdemeyer/sage-4.7.3.alpha0/devel/sage-main/sage/matrix/matrix_modn_dense_double.pyx\", line 117:\n    sage: a = A[0,0]; a\nExpected:\n    220082\nGot:\n    0\n**********************************************************************\nFile \"/Users/jdemeyer/sage-4.7.3.alpha0/devel/sage-main/sage/matrix/matrix_modn_dense_double.pyx\", line 119:\n    sage: ~a\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/jdemeyer/sage-4.7.3.alpha0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/Users/jdemeyer/sage-4.7.3.alpha0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/Users/jdemeyer/sage-4.7.3.alpha0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_3[6]>\", line 1, in <module>\n        ~a###line 119:\n    sage: ~a\n      File \"integer_mod.pyx\", line 3240, in sage.rings.finite_rings.integer_mod.IntegerMod_int64.__invert__ (sage/rings/finite_rings/integer_mod.c:25534)\n      File \"integer_mod.pyx\", line 3371, in sage.rings.finite_rings.integer_mod.mod_inverse_int64 (sage/rings/finite_rings/integer_mod.c:26331)\n    ZeroDivisionError: Inverse does not exist.\n**********************************************************************\nFile \"/Users/jdemeyer/sage-4.7.3.alpha0/devel/sage-main/sage/matrix/matrix_modn_dense_double.pyx\", line 129:\n    sage: a = A[0,0]; a\nExpected:\n    220081\nGot:\n    0\n**********************************************************************\nFile \"/Users/jdemeyer/sage-4.7.3.alpha0/devel/sage-main/sage/matrix/matrix_modn_dense_double.pyx\", line 131:\n    sage: a*a\nExpected:\n    4337773\nGot:\n    0\n**********************************************************************\n```\n",
    "created_at": "2011-11-03T09:01:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30976",
    "user": "https://github.com/jdemeyer"
}
```

Unfortunately, there are failures on OS X 10.4 PPC, all in the file `sage/matrix/matrix_modn_dense_double.pyx`:

```
sage -t  -long -force_lib devel/sage/sage/matrix/matrix_modn_dense_double.pyx
**********************************************************************
File "/Users/jdemeyer/sage-4.7.3.alpha0/devel/sage-main/sage/matrix/matrix_modn_dense_double.pyx", line 71:
    sage: A[0,0] = 220082r; A
Expected:
    [ 220082 2824836  765701 2282256]
    [1795330  767112 2967421 1373921]
    [2757699 1142917 2720973 2877160]
    [1674049 1341486 2641133 2173280]
Got:
    [      0 2824836  765701 2282256]
    [1795330  767112 2967421 1373921]
    [2757699 1142917 2720973 2877160]
    [1674049 1341486 2641133 2173280]
**********************************************************************
File "/Users/jdemeyer/sage-4.7.3.alpha0/devel/sage-main/sage/matrix/matrix_modn_dense_double.pyx", line 76:
    sage: a = A[0,0]; a
Expected:
    220082
Got:
    0
**********************************************************************
File "/Users/jdemeyer/sage-4.7.3.alpha0/devel/sage-main/sage/matrix/matrix_modn_dense_double.pyx", line 78:
    sage: ~a
Exception raised:
    Traceback (most recent call last):
      File "/Users/jdemeyer/sage-4.7.3.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/jdemeyer/sage-4.7.3.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/jdemeyer/sage-4.7.3.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[5]>", line 1, in <module>
        ~a###line 78:
    sage: ~a
      File "integer_mod.pyx", line 3240, in sage.rings.finite_rings.integer_mod.IntegerMod_int64.__invert__ (sage/rings/finite_rings/integer_mod.c:25534)
      File "integer_mod.pyx", line 3371, in sage.rings.finite_rings.integer_mod.mod_inverse_int64 (sage/rings/finite_rings/integer_mod.c:26331)
    ZeroDivisionError: Inverse does not exist.
**********************************************************************
File "/Users/jdemeyer/sage-4.7.3.alpha0/devel/sage-main/sage/matrix/matrix_modn_dense_double.pyx", line 86:
    sage: A[0,0] = 220082r; A
Expected:
    [ 220082 1237101 2033003 3788106]
    [4649912 1157595 4928315 4382585]
    [4252686  978867 2601478 1759921]
    [1303120 1860486 3405811 2203284]
Got:
    [      0 1237101 2033003 3788106]
    [4649912 1157595 4928315 4382585]
    [4252686  978867 2601478 1759921]
    [1303120 1860486 3405811 2203284]
**********************************************************************
File "/Users/jdemeyer/sage-4.7.3.alpha0/devel/sage-main/sage/matrix/matrix_modn_dense_double.pyx", line 91:
    sage: a = A[0,0]; a
Expected:
    220082
Got:
    0
**********************************************************************
File "/Users/jdemeyer/sage-4.7.3.alpha0/devel/sage-main/sage/matrix/matrix_modn_dense_double.pyx", line 93:
    sage: a*a
Expected:
    4777936
Got:
    0
**********************************************************************
File "/Users/jdemeyer/sage-4.7.3.alpha0/devel/sage-main/sage/matrix/matrix_modn_dense_double.pyx", line 112:
    sage: A[0,0] = K(220082); A
Expected:
    [ 220082 2824836  765701 2282256]
    [1795330  767112 2967421 1373921]
    [2757699 1142917 2720973 2877160]
    [1674049 1341486 2641133 2173280]
Got:
    [      0 2824836  765701 2282256]
    [1795330  767112 2967421 1373921]
    [2757699 1142917 2720973 2877160]
    [1674049 1341486 2641133 2173280]
**********************************************************************
File "/Users/jdemeyer/sage-4.7.3.alpha0/devel/sage-main/sage/matrix/matrix_modn_dense_double.pyx", line 117:
    sage: a = A[0,0]; a
Expected:
    220082
Got:
    0
**********************************************************************
File "/Users/jdemeyer/sage-4.7.3.alpha0/devel/sage-main/sage/matrix/matrix_modn_dense_double.pyx", line 119:
    sage: ~a
Exception raised:
    Traceback (most recent call last):
      File "/Users/jdemeyer/sage-4.7.3.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/jdemeyer/sage-4.7.3.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/jdemeyer/sage-4.7.3.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[6]>", line 1, in <module>
        ~a###line 119:
    sage: ~a
      File "integer_mod.pyx", line 3240, in sage.rings.finite_rings.integer_mod.IntegerMod_int64.__invert__ (sage/rings/finite_rings/integer_mod.c:25534)
      File "integer_mod.pyx", line 3371, in sage.rings.finite_rings.integer_mod.mod_inverse_int64 (sage/rings/finite_rings/integer_mod.c:26331)
    ZeroDivisionError: Inverse does not exist.
**********************************************************************
File "/Users/jdemeyer/sage-4.7.3.alpha0/devel/sage-main/sage/matrix/matrix_modn_dense_double.pyx", line 129:
    sage: a = A[0,0]; a
Expected:
    220081
Got:
    0
**********************************************************************
File "/Users/jdemeyer/sage-4.7.3.alpha0/devel/sage-main/sage/matrix/matrix_modn_dense_double.pyx", line 131:
    sage: a*a
Expected:
    4337773
Got:
    0
**********************************************************************
```




---

archive/issue_comments_030977.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2011-11-03T09:01:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30977",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from closed to new.



---

archive/issue_events_004500.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-11-03T09:01:11Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4260#event-4500"
}
```



---

archive/issue_comments_030978.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-11-03T09:01:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30978",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_030979.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-11-03T09:01:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30979",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_030980.json:
```json
{
    "body": "If I understand the errors correctly it's only setting elements which goes wrong, so I assume some cast doesn't work on PPC OSX 10.4. Can I get access to such a machine somehow?",
    "created_at": "2011-11-03T10:10:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30980",
    "user": "https://github.com/malb"
}
```

If I understand the errors correctly it's only setting elements which goes wrong, so I assume some cast doesn't work on PPC OSX 10.4. Can I get access to such a machine somehow?



---

archive/issue_comments_030981.json:
```json
{
    "body": "Replying to [comment:35 malb]:\n> If I understand the errors correctly it's only setting elements which goes wrong, so I assume some cast doesn't work on PPC OSX 10.4. Can I get access to such a machine somehow?\n\nThe machine that I'm using for this testing is not mine, but I can ask the owner.  I guess it will be okay for him to make an account for you.  He is on holidays now (I think up to sunday), so it will take a few days.",
    "created_at": "2011-11-03T10:39:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30981",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:35 malb]:
> If I understand the errors correctly it's only setting elements which goes wrong, so I assume some cast doesn't work on PPC OSX 10.4. Can I get access to such a machine somehow?

The machine that I'm using for this testing is not mine, but I can ask the owner.  I guess it will be okay for him to make an account for you.  He is on holidays now (I think up to sunday), so it will take a few days.



---

archive/issue_comments_030982.json:
```json
{
    "body": "Thanks.",
    "created_at": "2011-11-03T12:56:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30982",
    "user": "https://github.com/malb"
}
```

Thanks.



---

archive/issue_comments_030983.json:
```json
{
    "body": "Milestone sage-4.7.3 deleted",
    "created_at": "2011-11-03T16:14:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30983",
    "user": "https://github.com/jdemeyer"
}
```

Milestone sage-4.7.3 deleted



---

archive/issue_comments_030984.json:
```json
{
    "body": "Replying to [comment:35 malb]:\n> If I understand the errors correctly it's only setting elements which goes wrong, so I assume some cast doesn't work on PPC OSX 10.4. Can I get access to such a machine somehow?\n\nYes, see private email.",
    "created_at": "2011-11-08T17:18:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30984",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:35 malb]:
> If I understand the errors correctly it's only setting elements which goes wrong, so I assume some cast doesn't work on PPC OSX 10.4. Can I get access to such a machine somehow?

Yes, see private email.



---

archive/issue_comments_030985.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-11-09T12:40:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30985",
    "user": "https://github.com/malb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_030986.json:
```json
{
    "body": "Attachment [trac_4260_bugfix.patch](tarball://root/attachments/some-uuid/ticket4260/trac_4260_bugfix.patch) by @malb created at 2011-11-09 12:40:36\n\nThe attached patch fixes the issue on the machine in question. We forgot to deal with 32-bit systems in setting elements while we did it for getting elements.",
    "created_at": "2011-11-09T12:40:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30986",
    "user": "https://github.com/malb"
}
```

Attachment [trac_4260_bugfix.patch](tarball://root/attachments/some-uuid/ticket4260/trac_4260_bugfix.patch) by @malb created at 2011-11-09 12:40:36

The attached patch fixes the issue on the machine in question. We forgot to deal with 32-bit systems in setting elements while we did it for getting elements.



---

archive/issue_comments_030987.json:
```json
{
    "body": "Why do you write\n\n```\nceil(sqrt(2^31-1)) < 2^23\n```\n\nIt is a true statement, but where does the \"23\" come from?  You could write\n\n```\nceil(sqrt(2^31-1)) = 46341\n```\n",
    "created_at": "2011-11-09T13:20:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30987",
    "user": "https://github.com/jdemeyer"
}
```

Why do you write

```
ceil(sqrt(2^31-1)) < 2^23
```

It is a true statement, but where does the "23" come from?  You could write

```
ceil(sqrt(2^31-1)) = 46341
```




---

archive/issue_comments_030988.json:
```json
{
    "body": "2^23 is the maximum modulus of LinBox's double based matrix representation and writing 2^23 is easier to read than 46241.",
    "created_at": "2011-11-09T13:24:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30988",
    "user": "https://github.com/malb"
}
```

2^23 is the maximum modulus of LinBox's double based matrix representation and writing 2^23 is easier to read than 46241.



---

archive/issue_comments_030989.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-11-15T08:54:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30989",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_004501.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-11-15T08:54:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4260#event-4501"
}
```



---

archive/issue_comments_030990.json:
```json
{
    "body": "Works on OS X 10.4 PPC, so positive review.",
    "created_at": "2011-11-15T08:54:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30990",
    "user": "https://github.com/jdemeyer"
}
```

Works on OS X 10.4 PPC, so positive review.



---

archive/issue_comments_030991.json:
```json
{
    "body": "This crashes all over the place on OpenSolaris 06.2009-32 (hawk).  For example:\n\n```\nsage -t -long  -force_lib devel/sage/sage/rings/qqbar.py\n**********************************************************************\nFile \"/export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.8.alpha2/devel/sage-main/sage/rings/qqbar.py\", line 241:\n    sage: r.imag().minpoly() # this takes a long time (143s on my laptop)\nException raised:\n    Traceback (most recent call last):\n      File \"/export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.8.alpha2/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.8.alpha2/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.8.alpha2/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[74]>\", line 1, in <module>\n        r.imag().minpoly() # this takes a long time (143s on my laptop)###line 241:\n    sage: r.imag().minpoly() # this takes a long time (143s on my laptop)\n      File \"/export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.8.alpha2/local/lib/python/site-packages/sage/rings/qqbar.py\", line 2873, in minpoly\n        self._minimal_polynomial = self._descr.minpoly()\n      File \"/export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.8.alpha2/local/lib/python/site-packages/sage/rings/qqbar.py\", line 5406, in minpoly\n        self._minpoly = self._value.minpoly()\n      File \"number_field_element.pyx\", line 3495, in sage.rings.number_field.number_field_element.NumberFieldElement_absolute.minpoly (sage/rings/number_field/number_field_element.cpp:21939)\n      File \"number_field_element.pyx\", line 3462, in sage.rings.number_field.number_field_element.NumberFieldElement_absolute.charpoly (sage/rings/number_field/number_field_element.cpp:21816)\n      File \"matrix_rational_dense.pyx\", line 936, in sage.matrix.matrix_rational_dense.Matrix_rational_dense.charpoly (sage/matrix/matrix_rational_dense.c:10895)\n      File \"matrix_integer_dense.pyx\", line 1017, in sage.matrix.matrix_integer_dense.Matrix_integer_dense.charpoly (sage/matrix/matrix_integer_dense.c:10961)\n      File \"matrix_integer_dense.pyx\", line 1074, in sage.matrix.matrix_integer_dense.Matrix_integer_dense._charpoly_linbox (sage/matrix/matrix_integer_dense.c:11601)\n      File \"matrix_integer_dense.pyx\", line 1096, in sage.matrix.matrix_integer_dense.Matrix_integer_dense._poly_linbox (sage/matrix/matrix_integer_dense.c:11869)\n    RuntimeError: Segmentation fault\n**********************************************************************\n```\n\n\nThere are many more like this.",
    "created_at": "2011-11-17T13:01:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30991",
    "user": "https://github.com/jdemeyer"
}
```

This crashes all over the place on OpenSolaris 06.2009-32 (hawk).  For example:

```
sage -t -long  -force_lib devel/sage/sage/rings/qqbar.py
**********************************************************************
File "/export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.8.alpha2/devel/sage-main/sage/rings/qqbar.py", line 241:
    sage: r.imag().minpoly() # this takes a long time (143s on my laptop)
Exception raised:
    Traceback (most recent call last):
      File "/export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.8.alpha2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.8.alpha2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.8.alpha2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[74]>", line 1, in <module>
        r.imag().minpoly() # this takes a long time (143s on my laptop)###line 241:
    sage: r.imag().minpoly() # this takes a long time (143s on my laptop)
      File "/export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.8.alpha2/local/lib/python/site-packages/sage/rings/qqbar.py", line 2873, in minpoly
        self._minimal_polynomial = self._descr.minpoly()
      File "/export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.8.alpha2/local/lib/python/site-packages/sage/rings/qqbar.py", line 5406, in minpoly
        self._minpoly = self._value.minpoly()
      File "number_field_element.pyx", line 3495, in sage.rings.number_field.number_field_element.NumberFieldElement_absolute.minpoly (sage/rings/number_field/number_field_element.cpp:21939)
      File "number_field_element.pyx", line 3462, in sage.rings.number_field.number_field_element.NumberFieldElement_absolute.charpoly (sage/rings/number_field/number_field_element.cpp:21816)
      File "matrix_rational_dense.pyx", line 936, in sage.matrix.matrix_rational_dense.Matrix_rational_dense.charpoly (sage/matrix/matrix_rational_dense.c:10895)
      File "matrix_integer_dense.pyx", line 1017, in sage.matrix.matrix_integer_dense.Matrix_integer_dense.charpoly (sage/matrix/matrix_integer_dense.c:10961)
      File "matrix_integer_dense.pyx", line 1074, in sage.matrix.matrix_integer_dense.Matrix_integer_dense._charpoly_linbox (sage/matrix/matrix_integer_dense.c:11601)
      File "matrix_integer_dense.pyx", line 1096, in sage.matrix.matrix_integer_dense.Matrix_integer_dense._poly_linbox (sage/matrix/matrix_integer_dense.c:11869)
    RuntimeError: Segmentation fault
**********************************************************************
```


There are many more like this.



---

archive/issue_comments_030992.json:
```json
{
    "body": "Mhh, the trouble is in Matrix_integer_dense, which isn't what this ticket is about, so that's curious. How do I log into hawk?",
    "created_at": "2011-11-17T15:44:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30992",
    "user": "https://github.com/malb"
}
```

Mhh, the trouble is in Matrix_integer_dense, which isn't what this ticket is about, so that's curious. How do I log into hawk?



---

archive/issue_comments_030993.json:
```json
{
    "body": "I still want to investigate some more, for example I have not checked that it is really this ticket which causes the problems (but you do see \"linbox\" appearing in the backtrace).\n\nStrangely, even building the documentation crashes:\n\n```\nsphinx-build -b html -d /export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.8.alpha2/devel/sage/doc/output/doctrees/en/reference   -A hide_pdf_links=1 /export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.8.alpha2/devel/sage/doc/en/reference /export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.8.alpha2/devel/sage/doc/output/html/en/reference\nRunning Sphinx v1.1.2\nloading pickled environment... not yet created\nbuilding [html]: targets for 935 source files that are out of date\nupdating environment: 935 added, 0 changed, 0 removed\nreading sources... [  0%] algebras\nreading sources... [  0%] arithgroup\nreading sources... [  0%] calculus\nreading sources... [  0%] categories\nreading sources... [  0%] cmd\nreading sources... [  0%] coding\nreading sources... [  0%] coercion\nreading sources... [  0%] combinat/algebra\nreading sources... [  0%] combinat/crystals\n[...]\nwriting additional files... genindex py-modindex search\ncopying images... [ 16%] sage/graphs/../../media/heawood-graph-latex.png\ncopying images... [ 33%] sage/homology/../../media/homology/simplices.png\ncopying images... [ 50%] sage/homology/../../media/homology/torus.png\ncopying images... [ 66%] sage/homology/../../media/homology/klein.png\ncopying images... [ 83%] sage/homology/../../media/homology/rp2.png\ncopying images... [100%] sage/homology/../../media/homology/torus_labelled.png\n\ncopying static files... done\ndumping search index... done\ndumping object inventory... done\nbuild succeeded.\n\n------------------------------------------------------------------------\nUnhandled SIGSEGV: A segmentation fault occurred in Sage.\nThis probably occurred because a *compiled* component of Sage has a bug\nin it and is not properly wrapped with sig_on(), sig_off(). You might\nwant to run Sage under gdb with 'sage -gdb' to debug this.\nSage will now terminate.\n------------------------------------------------------------------------\nBuild finished.  The built documents can be found in /export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.8.alpha2/devel/sage/doc/output/html/en/reference\n```\n",
    "created_at": "2011-11-18T08:21:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30993",
    "user": "https://github.com/jdemeyer"
}
```

I still want to investigate some more, for example I have not checked that it is really this ticket which causes the problems (but you do see "linbox" appearing in the backtrace).

Strangely, even building the documentation crashes:

```
sphinx-build -b html -d /export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.8.alpha2/devel/sage/doc/output/doctrees/en/reference   -A hide_pdf_links=1 /export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.8.alpha2/devel/sage/doc/en/reference /export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.8.alpha2/devel/sage/doc/output/html/en/reference
Running Sphinx v1.1.2
loading pickled environment... not yet created
building [html]: targets for 935 source files that are out of date
updating environment: 935 added, 0 changed, 0 removed
reading sources... [  0%] algebras
reading sources... [  0%] arithgroup
reading sources... [  0%] calculus
reading sources... [  0%] categories
reading sources... [  0%] cmd
reading sources... [  0%] coding
reading sources... [  0%] coercion
reading sources... [  0%] combinat/algebra
reading sources... [  0%] combinat/crystals
[...]
writing additional files... genindex py-modindex search
copying images... [ 16%] sage/graphs/../../media/heawood-graph-latex.png
copying images... [ 33%] sage/homology/../../media/homology/simplices.png
copying images... [ 50%] sage/homology/../../media/homology/torus.png
copying images... [ 66%] sage/homology/../../media/homology/klein.png
copying images... [ 83%] sage/homology/../../media/homology/rp2.png
copying images... [100%] sage/homology/../../media/homology/torus_labelled.png

copying static files... done
dumping search index... done
dumping object inventory... done
build succeeded.

------------------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occurred in Sage.
This probably occurred because a *compiled* component of Sage has a bug
in it and is not properly wrapped with sig_on(), sig_off(). You might
want to run Sage under gdb with 'sage -gdb' to debug this.
Sage will now terminate.
------------------------------------------------------------------------
Build finished.  The built documents can be found in /export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.8.alpha2/devel/sage/doc/output/html/en/reference
```




---

archive/issue_comments_030994.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2011-11-20T10:24:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30994",
    "user": "https://github.com/jdemeyer"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_030995.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2011-11-20T10:24:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30995",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from closed to new.



---

archive/issue_events_004502.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-11-20T10:24:11Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4260#event-4502"
}
```



---

archive/issue_comments_030996.json:
```json
{
    "body": "Replying to [comment:45 malb]:\n> Mhh, the trouble is in Matrix_integer_dense, which isn't what this ticket is about, so that's curious. How do I log into hawk?\n\nHawk is a machine from David Kirkby, so you should ask him.",
    "created_at": "2011-11-20T10:28:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30996",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:45 malb]:
> Mhh, the trouble is in Matrix_integer_dense, which isn't what this ticket is about, so that's curious. How do I log into hawk?

Hawk is a machine from David Kirkby, so you should ask him.



---

archive/issue_comments_030997.json:
```json
{
    "body": "Okay, I managed to build 4.8-alpha2 + this ticket on hawk. Just starting and stopping Sage gives:\n\n```\n#0  0xfec9c7fb in _free_unlocked () from /lib/libc.so.1\n#1  0xfec9c7af in free () from /lib/libc.so.1\n#2  0xfdb81d01 in operator delete (ptr=0x8) at ../../../../gcc-4.5.0/libstdc++-v3/libsupc++/del_op.cc:44\n#3  0xfdb81d5d in operator delete[] (ptr=0x8) at ../../../../gcc-4.5.0/libstdc++-v3/libsupc++/del_opv.cc:32\n#4  0xfdb72543 in ~ios_base (this=0xf9a3e704) at ../../../../gcc-4.5.0/libstdc++-v3/src/ios.cc:93\n#5  0xf9892891 in __static_initialization_and_destruction_0 (__initialize_p=<value optimized out>)\n    at /usr/local/gcc-4.5.0/lib/gcc/i386-pc-solaris2.10/4.5.0/../../../../include/c++/4.5.0/bits/basic_ios.h:272\n#6  0xf988e3b0 in __do_global_dtors_aux () from /export/home/martina/sage-4.8.alpha2/local/lib//liblinboxsage.so.0\n#7  0xf99f7835 in _fini () from /export/home/martina/sage-4.8.alpha2/local/lib//liblinboxsage.so.0\n#8  0xfefd15fe in call_fini () from /usr/lib/ld.so.1\n#9  0xfefd17b3 in atexit_fini () from /usr/lib/ld.so.1\n#10 0xfec8370c in _exithandle () from /lib/libc.so.1\n#11 0xfec73f52 in exit () from /lib/libc.so.1\n#12 0xfeef3232 in Py_Exit (sts=0) at Python/pythonrun.c:1716\n#13 0xfeef3357 in handle_system_exit () at Python/pythonrun.c:1116\n#14 0x00000000 in ?? ()\n```\n\n\nSo it tries to clean up LinBox at the end and that's when things go wrong:\n\n```\n_fini () from /export/home/martina/sage-4.8.alpha2/local/lib//liblinboxsage.so.0\n```\n\nany ideas about why?",
    "created_at": "2011-11-22T17:25:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30997",
    "user": "https://github.com/malb"
}
```

Okay, I managed to build 4.8-alpha2 + this ticket on hawk. Just starting and stopping Sage gives:

```
#0  0xfec9c7fb in _free_unlocked () from /lib/libc.so.1
#1  0xfec9c7af in free () from /lib/libc.so.1
#2  0xfdb81d01 in operator delete (ptr=0x8) at ../../../../gcc-4.5.0/libstdc++-v3/libsupc++/del_op.cc:44
#3  0xfdb81d5d in operator delete[] (ptr=0x8) at ../../../../gcc-4.5.0/libstdc++-v3/libsupc++/del_opv.cc:32
#4  0xfdb72543 in ~ios_base (this=0xf9a3e704) at ../../../../gcc-4.5.0/libstdc++-v3/src/ios.cc:93
#5  0xf9892891 in __static_initialization_and_destruction_0 (__initialize_p=<value optimized out>)
    at /usr/local/gcc-4.5.0/lib/gcc/i386-pc-solaris2.10/4.5.0/../../../../include/c++/4.5.0/bits/basic_ios.h:272
#6  0xf988e3b0 in __do_global_dtors_aux () from /export/home/martina/sage-4.8.alpha2/local/lib//liblinboxsage.so.0
#7  0xf99f7835 in _fini () from /export/home/martina/sage-4.8.alpha2/local/lib//liblinboxsage.so.0
#8  0xfefd15fe in call_fini () from /usr/lib/ld.so.1
#9  0xfefd17b3 in atexit_fini () from /usr/lib/ld.so.1
#10 0xfec8370c in _exithandle () from /lib/libc.so.1
#11 0xfec73f52 in exit () from /lib/libc.so.1
#12 0xfeef3232 in Py_Exit (sts=0) at Python/pythonrun.c:1716
#13 0xfeef3357 in handle_system_exit () at Python/pythonrun.c:1116
#14 0x00000000 in ?? ()
```


So it tries to clean up LinBox at the end and that's when things go wrong:

```
_fini () from /export/home/martina/sage-4.8.alpha2/local/lib//liblinboxsage.so.0
```

any ideas about why?



---

archive/issue_comments_030998.json:
```json
{
    "body": "Weird, I rebuilt everything from scratch using these environment variables \n\n```\nSAGE_PARALLEL_SPKG_BUILD=yes\nLD_LIBRARY_PATH=/usr/local/lib\nPATH=/usr/local/bins-for-sage:/usr/local/bin:/usr/bin:/bin\nMAKE=make -j4\n```\n\n\nand now\n\n\n```\nAll tests passed!\nTotal time for all tests: 1742.8 seconds\n```\n\n\ni.e., the segfault is gone. How does the buildbot build Sage?",
    "created_at": "2011-11-23T18:18:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30998",
    "user": "https://github.com/malb"
}
```

Weird, I rebuilt everything from scratch using these environment variables 

```
SAGE_PARALLEL_SPKG_BUILD=yes
LD_LIBRARY_PATH=/usr/local/lib
PATH=/usr/local/bins-for-sage:/usr/local/bin:/usr/bin:/bin
MAKE=make -j4
```


and now


```
All tests passed!
Total time for all tests: 1742.8 seconds
```


i.e., the segfault is gone. How does the buildbot build Sage?



---

archive/issue_comments_030999.json:
```json
{
    "body": "Replying to [comment:50 malb]:\n> i.e., the segfault is gone. How does the buildbot build Sage?\n\n```\nEDITOR=emacs\nHISTCONTROL=ignoreboth\nHISTSIZE=2000\nHOME=/export/home/buildbot\nIGNOREEOF=100\nLANG=C\nLD_LIBRARY_PATH=/usr/local/gcc-4.5.0/lib:/usr/local/gcc-4.5.0/lib/amd64\nLESS=iMqR\nLESSHISTFILE=-\nLOGNAME=buildbot\nMAIL=/var/mail/buildbot\nMAKE=make -j12\nMAKEOPTS=-j12\nPAGER=/usr/bin/less\nPATH=/export/home/buildbot/bin:/export/home/buildbot/local/hawk/bin:/usr/local/bins-for-sage:/usr/local/gcc-4.5.0/bin:/usr/local/bin:/usr/local/texlive/2010/bin/i386-solaris/:/usr/bin:/usr/sbin\nPWD=/export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.8.alpha2\nSAGE_ATLAS_LIB=/ATLAS32\nSAGE_FORTRAN=/usr/local/gcc-4.5.0/bin/gfortran\nSAGE_FORTRAN_LIB=/usr/local/gcc-4.5.0/lib/libgfortran.so\nSAGE_PARALLEL_SPKG_BUILD=yes\nSAGE_PORT=true\nSHELL=/bin/bash\nSHLVL=1\nSSH_CLIENT=128.208.160.197 44994 22\nSSH_CONNECTION=128.208.160.197 44994 192.168.1.191 22\nSSH_TTY=/dev/pts/2\nTERM=screen\nTZ=Europe/London\nUSER=buildbot\nVIRTUAL_ENV=/export/home/buildbot/local/hawk\nVIRTUAL_ENV_DISABLE_PROMPT=yes\nVISUAL=emacs\n```\n",
    "created_at": "2011-11-26T13:16:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-30999",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:50 malb]:
> i.e., the segfault is gone. How does the buildbot build Sage?

```
EDITOR=emacs
HISTCONTROL=ignoreboth
HISTSIZE=2000
HOME=/export/home/buildbot
IGNOREEOF=100
LANG=C
LD_LIBRARY_PATH=/usr/local/gcc-4.5.0/lib:/usr/local/gcc-4.5.0/lib/amd64
LESS=iMqR
LESSHISTFILE=-
LOGNAME=buildbot
MAIL=/var/mail/buildbot
MAKE=make -j12
MAKEOPTS=-j12
PAGER=/usr/bin/less
PATH=/export/home/buildbot/bin:/export/home/buildbot/local/hawk/bin:/usr/local/bins-for-sage:/usr/local/gcc-4.5.0/bin:/usr/local/bin:/usr/local/texlive/2010/bin/i386-solaris/:/usr/bin:/usr/sbin
PWD=/export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.8.alpha2
SAGE_ATLAS_LIB=/ATLAS32
SAGE_FORTRAN=/usr/local/gcc-4.5.0/bin/gfortran
SAGE_FORTRAN_LIB=/usr/local/gcc-4.5.0/lib/libgfortran.so
SAGE_PARALLEL_SPKG_BUILD=yes
SAGE_PORT=true
SHELL=/bin/bash
SHLVL=1
SSH_CLIENT=128.208.160.197 44994 22
SSH_CONNECTION=128.208.160.197 44994 192.168.1.191 22
SSH_TTY=/dev/pts/2
TERM=screen
TZ=Europe/London
USER=buildbot
VIRTUAL_ENV=/export/home/buildbot/local/hawk
VIRTUAL_ENV_DISABLE_PROMPT=yes
VISUAL=emacs
```




---

archive/issue_comments_031000.json:
```json
{
    "body": "Perhaps, it's a GCC 4.5.0 issue?",
    "created_at": "2011-11-27T00:47:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-31000",
    "user": "https://github.com/malb"
}
```

Perhaps, it's a GCC 4.5.0 issue?



---

archive/issue_comments_031001.json:
```json
{
    "body": "Replying to [comment:52 malb]:\n> Perhaps, it's a GCC 4.5.0 issue?\nCould very well be.\n\nWhat does your gcc --version say? (the gcc you used to compile Linbox successfully)",
    "created_at": "2011-11-27T09:07:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-31001",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:52 malb]:
> Perhaps, it's a GCC 4.5.0 issue?
Could very well be.

What does your gcc --version say? (the gcc you used to compile Linbox successfully)



---

archive/issue_comments_031002.json:
```json
{
    "body": "\n```\n$ gcc --version\ngcc (GCC) 4.4.3 20100112 (prerelease)\nCopyright (C) 2010 Free Software Foundation, Inc.\nThis is free software; see the source for copying conditions.  There is NO\nwarranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.\n```\n",
    "created_at": "2011-11-27T21:56:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-31002",
    "user": "https://github.com/malb"
}
```


```
$ gcc --version
gcc (GCC) 4.4.3 20100112 (prerelease)
Copyright (C) 2010 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```




---

archive/issue_comments_031003.json:
```json
{
    "body": "I can confirm that this bug is at least triggered by GCC 4.5.\n\nHere's the relevant bits of the env that I used to build Sage + this ticket just now:\n\n```\nSAGE_PARALLEL_SPKG_BUILD=yes\nLD_LIBRARY_PATH=/usr/local/gcc-4.5.0/lib:/usr/local/gcc-4.5.0/lib/amd64\nPATH=/usr/local/gcc-4.5.0/bin:/usr/local/bins-for-sage/:/usr/local/bin:/usr/bin:/usr/sbin\nMAKE=make -j8\n```\n\nand this one crashes with a SIGSEGV. Whereas the env posted above by doesn't.\n\nI am not sure what to do about this? Ask Dave to install a newer GCC to test whether it fails with it as well?",
    "created_at": "2011-11-29T11:15:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-31003",
    "user": "https://github.com/malb"
}
```

I can confirm that this bug is at least triggered by GCC 4.5.

Here's the relevant bits of the env that I used to build Sage + this ticket just now:

```
SAGE_PARALLEL_SPKG_BUILD=yes
LD_LIBRARY_PATH=/usr/local/gcc-4.5.0/lib:/usr/local/gcc-4.5.0/lib/amd64
PATH=/usr/local/gcc-4.5.0/bin:/usr/local/bins-for-sage/:/usr/local/bin:/usr/bin:/usr/sbin
MAKE=make -j8
```

and this one crashes with a SIGSEGV. Whereas the env posted above by doesn't.

I am not sure what to do about this? Ask Dave to install a newer GCC to test whether it fails with it as well?



---

archive/issue_comments_031004.json:
```json
{
    "body": "Replying to [comment:55 malb]:\n\n> I am not sure what to do about this? Ask Dave to install a newer GCC to test whether it fails with it as well?\n\nThat's not a bad suggestion, asking to install gcc 4.5.3 for example (the latest in the 4.5 series)",
    "created_at": "2011-11-29T13:27:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-31004",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:55 malb]:

> I am not sure what to do about this? Ask Dave to install a newer GCC to test whether it fails with it as well?

That's not a bad suggestion, asking to install gcc 4.5.3 for example (the latest in the 4.5 series)



---

archive/issue_comments_031005.json:
```json
{
    "body": "I conclude it's a compiler bug: I just built with:\n\n\n```\nSAGE_PARALLEL_SPKG_BUILD=yes\nLD_LIBRARY_PATH=/usr/local/gcc-4.6.0/lib:/usr/local/gcc-4.6.0/lib/amd64\nPATH=/usr/local/gcc-4.6.0/bin:/usr/local/bins-for-sage/:/usr/local/bin:/usr/bin:/usr/sbin\nMAKE=make -j8\n```\n\n\nand \n\n\n```\nAll tests passed!\nTotal time for all tests: 1786.1 seconds\n```\n\n\nI suggest to avoid 4.5.0 (at least on OpenSolaris) and to change the status of this ticket back to **positive review**.",
    "created_at": "2011-11-30T15:02:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-31005",
    "user": "https://github.com/malb"
}
```

I conclude it's a compiler bug: I just built with:


```
SAGE_PARALLEL_SPKG_BUILD=yes
LD_LIBRARY_PATH=/usr/local/gcc-4.6.0/lib:/usr/local/gcc-4.6.0/lib/amd64
PATH=/usr/local/gcc-4.6.0/bin:/usr/local/bins-for-sage/:/usr/local/bin:/usr/bin:/usr/sbin
MAKE=make -j8
```


and 


```
All tests passed!
Total time for all tests: 1786.1 seconds
```


I suggest to avoid 4.5.0 (at least on OpenSolaris) and to change the status of this ticket back to **positive review**.



---

archive/issue_comments_031006.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-11-30T15:05:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-31006",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_031007.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-11-30T15:05:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-31007",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_004503.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-12-01T08:12:15Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4260#event-4503"
}
```



---

archive/issue_comments_031008.json:
```json
{
    "body": "Testing again on hawk...",
    "created_at": "2011-12-01T08:12:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-31008",
    "user": "https://github.com/jdemeyer"
}
```

Testing again on hawk...



---

archive/issue_comments_031009.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-12-01T08:12:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4260#issuecomment-31009",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
