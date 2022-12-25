# Issue 2107: [with patch, with positive review] serious malloc problem triggered by Hecke operator computation

archive/issues_002107.json:
```json
{
    "body": "Assignee: @williamstein\n\n```\nsage: B = victor_miller_basis(100,30)\nsage: t2 = hecke_operator_on_basis(B, 100, 2)\nsage.bin(40290) malloc: *** error for object 0x37e2f10: incorrect checksum for freed object - object was probably modified after being freed.\n*** set a breakpoint in malloc_error_break to debug\nsage.bin(40290) malloc: *** error for object 0x37e2f80: Non-aligned pointer being freed (2)\n*** set a breakpoint in malloc_error_break to debug\nsage.bin(40290) malloc: *** error for object 0x37e2f20: Non-aligned pointer being freed (2)\n*** set a breakpoint in malloc_error_break to debug\nsage.bin(40290) malloc: *** error for object 0x37e2f40: Non-aligned pointer being freed (2)\n*** set a breakpoint in malloc_error_break to debug\nsage.bin(40290) malloc: *** error for object 0x37d6120: Non-aligned pointer being freed (2)\n*** set a breakpoint in malloc_error_break to debug\nsage.bin(40290) malloc: *** error for object 0x37d6170: Non-aligned pointer being freed (2)\n*** set a breakpoint in malloc_error_break to debug\nsage.bin(40290) malloc: *** error for object 0x3780500: Non-aligned pointer being freed (2)\n*** set a breakpoint in malloc_error_break to debug\nsage.bin(40290) malloc: *** error for object 0x3781090: Non-aligned pointer being freed (2)\n*** set a breakpoint in malloc_error_break to debug\nsage.bin(40290) malloc: *** error for object 0x37dce90: Non-aligned pointer being freed (2)\n*** set a breakpoint in malloc_error_break to debug\n\n\n------------------------------------------------------------\nUnhandled SIGSEGV: A segmentation fault occured in SAGE.\nThis probably occured because a *compiled* component\nof SAGE has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run SAGE under gdb with 'sage -gdb' to debug this.\nSAGE will now terminate (sorry).\n------------------------------------------------------------\n\nsage.bin(40290) malloc: *** error for object 0x3796f40: Non-aligned pointer being freed (2)\n*** set a breakpoint in malloc_error_break to debug\nsage.bin(40290) malloc: *** error for object 0x37975b0: Non-aligned pointer being freed (2)\n*** set a breakpoint in malloc_error_break to debug\nsage.bin(40290) malloc: *** error for object 0x3797890: Non-aligned pointer being freed (2)\n*** set a breakpoint in malloc_error_break to debug\nsage.bin(40290) malloc: *** error for object 0x3797880: Non-aligned pointer being freed (2)\n*** set a breakpoint in malloc_error_break to debug\nsage.bin(40290) malloc: *** error for object 0x3746ef0: Non-aligned pointer being freed (2)\n*** set a breakpoint in malloc_error_break to debug\nsage.bin(40290) malloc: *** error for object 0x3773150: Non-aligned pointer being freed (2)\n*** set a breakpoint in malloc_error_break to debug\nsage.bin(40290) malloc: *** error for object 0x373c6c0: Non-aligned pointer being freed (2)\n*** set a breakpoint in malloc_error_break to debug\nsage.bin(40290) malloc: *** error for object 0x3767990: Non-aligned pointer being freed (2)\n*** set a breakpoint in malloc_error_break to debug\nsage.bin(40290) malloc: *** error for object 0x3762180: Non-aligned pointer being freed (2)\n*** set a breakpoint in malloc_error_break to debug\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/2107\n\n",
    "closed_at": "2008-02-17T00:28:53Z",
    "created_at": "2008-02-08T09:50:23Z",
    "labels": [
        "component: modular forms",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "[with patch, with positive review] serious malloc problem triggered by Hecke operator computation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2107",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

```
sage: B = victor_miller_basis(100,30)
sage: t2 = hecke_operator_on_basis(B, 100, 2)
sage.bin(40290) malloc: *** error for object 0x37e2f10: incorrect checksum for freed object - object was probably modified after being freed.
*** set a breakpoint in malloc_error_break to debug
sage.bin(40290) malloc: *** error for object 0x37e2f80: Non-aligned pointer being freed (2)
*** set a breakpoint in malloc_error_break to debug
sage.bin(40290) malloc: *** error for object 0x37e2f20: Non-aligned pointer being freed (2)
*** set a breakpoint in malloc_error_break to debug
sage.bin(40290) malloc: *** error for object 0x37e2f40: Non-aligned pointer being freed (2)
*** set a breakpoint in malloc_error_break to debug
sage.bin(40290) malloc: *** error for object 0x37d6120: Non-aligned pointer being freed (2)
*** set a breakpoint in malloc_error_break to debug
sage.bin(40290) malloc: *** error for object 0x37d6170: Non-aligned pointer being freed (2)
*** set a breakpoint in malloc_error_break to debug
sage.bin(40290) malloc: *** error for object 0x3780500: Non-aligned pointer being freed (2)
*** set a breakpoint in malloc_error_break to debug
sage.bin(40290) malloc: *** error for object 0x3781090: Non-aligned pointer being freed (2)
*** set a breakpoint in malloc_error_break to debug
sage.bin(40290) malloc: *** error for object 0x37dce90: Non-aligned pointer being freed (2)
*** set a breakpoint in malloc_error_break to debug


------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------

sage.bin(40290) malloc: *** error for object 0x3796f40: Non-aligned pointer being freed (2)
*** set a breakpoint in malloc_error_break to debug
sage.bin(40290) malloc: *** error for object 0x37975b0: Non-aligned pointer being freed (2)
*** set a breakpoint in malloc_error_break to debug
sage.bin(40290) malloc: *** error for object 0x3797890: Non-aligned pointer being freed (2)
*** set a breakpoint in malloc_error_break to debug
sage.bin(40290) malloc: *** error for object 0x3797880: Non-aligned pointer being freed (2)
*** set a breakpoint in malloc_error_break to debug
sage.bin(40290) malloc: *** error for object 0x3746ef0: Non-aligned pointer being freed (2)
*** set a breakpoint in malloc_error_break to debug
sage.bin(40290) malloc: *** error for object 0x3773150: Non-aligned pointer being freed (2)
*** set a breakpoint in malloc_error_break to debug
sage.bin(40290) malloc: *** error for object 0x373c6c0: Non-aligned pointer being freed (2)
*** set a breakpoint in malloc_error_break to debug
sage.bin(40290) malloc: *** error for object 0x3767990: Non-aligned pointer being freed (2)
*** set a breakpoint in malloc_error_break to debug
sage.bin(40290) malloc: *** error for object 0x3762180: Non-aligned pointer being freed (2)
*** set a breakpoint in malloc_error_break to debug
```

Issue created by migration from https://trac.sagemath.org/ticket/2107





---

archive/issue_comments_013705.json:
```json
{
    "body": "LinBox seems to be at fault here or at least involved:\n\n```\n==7910== Invalid read of size 8\n==7910==    at 0x149D79B0: LinBox::DenseMatrixBase<double>::setEntry(unsigned long, unsigned long, double const&) (dense.h:173)\n==7910==    by 0x149DB884: void LinBox::BlasMatrix<double>::createBlasMatrix<LinBox::DenseMatrix<LinBox::Modular<double> > >(LinBox::De\nnseMatrix<LinBox::Modular<double> > const&, LinBox::MatrixContainerCategory::Container) (blas-matrix.h:119)\n==7910==    by 0x14A0DEAB: LinBox::BlasMatrix<double>::BlasMatrix<LinBox::DenseMatrix<LinBox::Modular<double> > >(LinBox::DenseMatrix<L\ninBox::Modular<double> > const&) (blas-matrix.h:87)\n==7910==    by 0x14A87781: unsigned long& LinBox::rank<LinBox::DenseMatrix<LinBox::Modular<double> > >(unsigned long&, LinBox::DenseMat\nrix<LinBox::Modular<double> > const&, LinBox::RingCategories::ModularTag const&, LinBox::BlasEliminationTraits const&) (rank.h:529)\n==7910==    by 0x14ACAB18: unsigned long& LinBox::rank<LinBox::DenseMatrix<LinBox::Modular<double> > >(unsigned long&, LinBox::DenseMat\nrix<LinBox::Modular<double> > const&, LinBox::RingCategories::ModularTag const&, LinBox::EliminationSpecifier const&) (rank.h:115)\n==7910==    by 0x14ADBC3B: unsigned long& LinBox::rank<LinBox::DenseMatrix<LinBox::Modular<double> > >(unsigned long&, LinBox::DenseMat\nrix<LinBox::Modular<double> > const&, LinBox::RingCategories::ModularTag const&, LinBox::HybridSpecifier const&) (rank.h:102)\n==7910==    by 0x14ADBEE0: unsigned long& LinBox::rank<LinBox::DenseMatrix<LinBox::Modular<double> > >(unsigned long&, LinBox::DenseMat\nrix<LinBox::Modular<double> > const&) (rank.h:84)\n==7910==    by 0x149CDB0D: linbox_modn_dense_rank (linbox_wrap.cpp:102)\n==7910==    by 0x147624F0: __pyx_f_4sage_4libs_6linbox_6linbox_17Linbox_modn_dense_rank(__pyx_obj_4sage_4libs_6linbox_6linbox_Linbox_mo\ndn_dense*) (linbox.cpp:1511)\n==7910==    by 0x1442F979: __pyx_pf_4sage_6matrix_17matrix_modn_dense_17Matrix_modn_dense_rank (matrix_modn_dense.c:7178)\n==7910==    by 0x415542: PyObject_Call (abstract.c:1860)\n==7910==    by 0x150AB893: __pyx_pf_4sage_6matrix_20matrix_integer_dense_20Matrix_integer_dense__rank_modp (matrix_integer_dense.c:1596\n5)\n==7910==  Address 0x7172cf0 is 0 bytes after a block of size 0 alloc'd\n==7910==    at 0x4A1C649: operator new(unsigned long) (vg_replace_malloc.c:230)\n==7910==    by 0x14A0DAE2: __gnu_cxx::new_allocator<double>::allocate(unsigned long, void const*) (new_allocator.h:88)\n==7910==    by 0x14A0DB0A: std::_Vector_base<double, std::allocator<double> >::_M_allocate(unsigned long) (stl_vector.h:127)\n==7910==    by 0x14A0DB3C: std::_Vector_base<double, std::allocator<double> >::_Vector_base(unsigned long, std::allocator<double> const\n&) (stl_vector.h:113)\n==7910==    by 0x14A0DBC1: std::vector<double, std::allocator<double> >::vector(unsigned long, double const&, std::allocator<double> co\nnst&) (stl_vector.h:216)\n==7910==    by 0x14A0DC93: LinBox::DenseMatrixBase<double>::DenseMatrixBase(unsigned long, unsigned long) (dense.h:101)\n==7910==    by 0x14AB7354: LinBox::DenseMatrix<LinBox::Modular<double> >::DenseMatrix(LinBox::Modular<double> const&, unsigned long, un\nsigned long) (dense.h:98)\n==7910==    by 0x149CDA1F: linbox_modn_dense_rank (linbox_wrap.cpp:92)\n==7910==    by 0x147624F0: __pyx_f_4sage_4libs_6linbox_6linbox_17Linbox_modn_dense_rank(__pyx_obj_4sage_4libs_6linbox_6linbox_Linbox_mo\ndn_dense*) (linbox.cpp:1511)\n==7910==    by 0x1442F979: __pyx_pf_4sage_6matrix_17matrix_modn_dense_17Matrix_modn_dense_rank (matrix_modn_dense.c:7178)\n==7910==    by 0x415542: PyObject_Call (abstract.c:1860)\n==7910==    by 0x150AB893: __pyx_pf_4sage_6matrix_20matrix_integer_dense_20Matrix_integer_dense__rank_modp (matrix_integer_dense.c:1596\n5)\n==7910==\n==7910== Invalid write of size 8\n==7910==    at 0x149D79B3: LinBox::DenseMatrixBase<double>::setEntry(unsigned long, unsigned long, double const&) (dense.h:173)\n==7910==    by 0x149DB884: void LinBox::BlasMatrix<double>::createBlasMatrix<LinBox::DenseMatrix<LinBox::Modular<double> > >(LinBox::De\nnseMatrix<LinBox::Modular<double> > const&, LinBox::MatrixContainerCategory::Container) (blas-matrix.h:119)\n==7910==    by 0x14A0DEAB: LinBox::BlasMatrix<double>::BlasMatrix<LinBox::DenseMatrix<LinBox::Modular<double> > >(LinBox::DenseMatrix<L\ninBox::Modular<double> > const&) (blas-matrix.h:87)\n==7910==    by 0x14A87781: unsigned long& LinBox::rank<LinBox::DenseMatrix<LinBox::Modular<double> > >(unsigned long&, LinBox::DenseMat\nrix<LinBox::Modular<double> > const&, LinBox::RingCategories::ModularTag const&, LinBox::BlasEliminationTraits const&) (rank.h:529)\n==7910==    by 0x14ACAB18: unsigned long& LinBox::rank<LinBox::DenseMatrix<LinBox::Modular<double> > >(unsigned long&, LinBox::DenseMat\nrix<LinBox::Modular<double> > const&, LinBox::RingCategories::ModularTag const&, LinBox::EliminationSpecifier const&) (rank.h:115)\n==7910==    by 0x14ADBC3B: unsigned long& LinBox::rank<LinBox::DenseMatrix<LinBox::Modular<double> > >(unsigned long&, LinBox::DenseMat\nrix<LinBox::Modular<double> > const&, LinBox::RingCategories::ModularTag const&, LinBox::HybridSpecifier const&) (rank.h:102)\n==7910==    by 0x14ADBEE0: unsigned long& LinBox::rank<LinBox::DenseMatrix<LinBox::Modular<double> > >(unsigned long&, LinBox::DenseMat\nrix<LinBox::Modular<double> > const&) (rank.h:84)\n==7910==    by 0x149CDB0D: linbox_modn_dense_rank (linbox_wrap.cpp:102)\n==7910==    by 0x147624F0: __pyx_f_4sage_4libs_6linbox_6linbox_17Linbox_modn_dense_rank(__pyx_obj_4sage_4libs_6linbox_6linbox_Linbox_mo\ndn_dense*) (linbox.cpp:1511)\n==7910==    by 0x1442F979: __pyx_pf_4sage_6matrix_17matrix_modn_dense_17Matrix_modn_dense_rank (matrix_modn_dense.c:7178)\n==7910==    by 0x415542: PyObject_Call (abstract.c:1860)\n==7910==    by 0x150AB893: __pyx_pf_4sage_6matrix_20matrix_integer_dense_20Matrix_integer_dense__rank_modp (matrix_integer_dense.c:1596\n5)\n==7910==  Address 0x79543e8 is 0 bytes after a block of size 0 alloc'd\n==7910==    at 0x4A1C649: operator new(unsigned long) (vg_replace_malloc.c:230)\n==7910==    by 0x14A0DAE2: __gnu_cxx::new_allocator<double>::allocate(unsigned long, void const*) (new_allocator.h:88)\n==7910==    by 0x14A0DB0A: std::_Vector_base<double, std::allocator<double> >::_M_allocate(unsigned long) (stl_vector.h:127)\n==7910==    by 0x14A0DB3C: std::_Vector_base<double, std::allocator<double> >::_Vector_base(unsigned long, std::allocator<double> const\n&) (stl_vector.h:113)\n==7910==    by 0x14A0DBC1: std::vector<double, std::allocator<double> >::vector(unsigned long, double const&, std::allocator<double> co\nnst&) (stl_vector.h:216)\n==7910==    by 0x14A0DD5D: LinBox::DenseMatrixBase<double>::DenseMatrixBase(unsigned long, unsigned long) (dense.h:101)\n==7910==    by 0x14A0DE45: LinBox::BlasMatrix<double>::BlasMatrix<LinBox::DenseMatrix<LinBox::Modular<double> > >(LinBox::DenseMatrix<L\ninBox::Modular<double> > const&) (blas-matrix.h:84)\n==7910==    by 0x14A87781: unsigned long& LinBox::rank<LinBox::DenseMatrix<LinBox::Modular<double> > >(unsigned long&, LinBox::DenseMat\nrix<LinBox::Modular<double> > const&, LinBox::RingCategories::ModularTag const&, LinBox::BlasEliminationTraits const&) (rank.h:529)\n==7910==    by 0x14ACAB18: unsigned long& LinBox::rank<LinBox::DenseMatrix<LinBox::Modular<double> > >(unsigned long&, LinBox::DenseMat\nrix<LinBox::Modular<double> > const&, LinBox::RingCategories::ModularTag const&, LinBox::EliminationSpecifier const&) (rank.h:115)\n==7910==    by 0x14ADBC3B: unsigned long& LinBox::rank<LinBox::DenseMatrix<LinBox::Modular<double> > >(unsigned long&, LinBox::DenseMat\nrix<LinBox::Modular<double> > const&, LinBox::RingCategories::ModularTag const&, LinBox::HybridSpecifier const&) (rank.h:102)\n==7910==    by 0x14ADBEE0: unsigned long& LinBox::rank<LinBox::DenseMatrix<LinBox::Modular<double> > >(unsigned long&, LinBox::DenseMat\nrix<LinBox::Modular<double> > const&) (rank.h:84)\n==7910==    by 0x149CDB0D: linbox_modn_dense_rank (linbox_wrap.cpp:102)\n--7910-- VALGRIND INTERNAL ERROR: Valgrind received a signal 11 (SIGSEGV) - exiting\n--7910-- si_code=1;  Faulting address: 0x78;  sp: 0x403469CF0\n\nvalgrind: the 'impossible' happened:\n   Killed by fatal signal\n==7910==    at 0x38021BBE: mkFreeBlock (m_mallocfree.c:205)\n==7910==    by 0x38022455: vgPlain_arena_malloc (m_mallocfree.c:1204)\n==7910==    by 0x380028B8: vgMemCheck_new_block (mc_malloc_wrappers.c:195)\n==7910==    by 0x38002CF3: vgMemCheck_malloc (mc_malloc_wrappers.c:226)\n==7910==    by 0x38032F1D: do_client_request (scheduler.c:1269)\n==7910==    by 0x380342E0: vgPlain_scheduler (scheduler.c:979)\n==7910==    by 0x380445AE: run_a_thread_NORETURN (syswrap-linux.c:89)\n```\n\nCheers,\n\nMichael",
    "created_at": "2008-02-08T22:47:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2107#issuecomment-13705",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

LinBox seems to be at fault here or at least involved:

```
==7910== Invalid read of size 8
==7910==    at 0x149D79B0: LinBox::DenseMatrixBase<double>::setEntry(unsigned long, unsigned long, double const&) (dense.h:173)
==7910==    by 0x149DB884: void LinBox::BlasMatrix<double>::createBlasMatrix<LinBox::DenseMatrix<LinBox::Modular<double> > >(LinBox::De
nseMatrix<LinBox::Modular<double> > const&, LinBox::MatrixContainerCategory::Container) (blas-matrix.h:119)
==7910==    by 0x14A0DEAB: LinBox::BlasMatrix<double>::BlasMatrix<LinBox::DenseMatrix<LinBox::Modular<double> > >(LinBox::DenseMatrix<L
inBox::Modular<double> > const&) (blas-matrix.h:87)
==7910==    by 0x14A87781: unsigned long& LinBox::rank<LinBox::DenseMatrix<LinBox::Modular<double> > >(unsigned long&, LinBox::DenseMat
rix<LinBox::Modular<double> > const&, LinBox::RingCategories::ModularTag const&, LinBox::BlasEliminationTraits const&) (rank.h:529)
==7910==    by 0x14ACAB18: unsigned long& LinBox::rank<LinBox::DenseMatrix<LinBox::Modular<double> > >(unsigned long&, LinBox::DenseMat
rix<LinBox::Modular<double> > const&, LinBox::RingCategories::ModularTag const&, LinBox::EliminationSpecifier const&) (rank.h:115)
==7910==    by 0x14ADBC3B: unsigned long& LinBox::rank<LinBox::DenseMatrix<LinBox::Modular<double> > >(unsigned long&, LinBox::DenseMat
rix<LinBox::Modular<double> > const&, LinBox::RingCategories::ModularTag const&, LinBox::HybridSpecifier const&) (rank.h:102)
==7910==    by 0x14ADBEE0: unsigned long& LinBox::rank<LinBox::DenseMatrix<LinBox::Modular<double> > >(unsigned long&, LinBox::DenseMat
rix<LinBox::Modular<double> > const&) (rank.h:84)
==7910==    by 0x149CDB0D: linbox_modn_dense_rank (linbox_wrap.cpp:102)
==7910==    by 0x147624F0: __pyx_f_4sage_4libs_6linbox_6linbox_17Linbox_modn_dense_rank(__pyx_obj_4sage_4libs_6linbox_6linbox_Linbox_mo
dn_dense*) (linbox.cpp:1511)
==7910==    by 0x1442F979: __pyx_pf_4sage_6matrix_17matrix_modn_dense_17Matrix_modn_dense_rank (matrix_modn_dense.c:7178)
==7910==    by 0x415542: PyObject_Call (abstract.c:1860)
==7910==    by 0x150AB893: __pyx_pf_4sage_6matrix_20matrix_integer_dense_20Matrix_integer_dense__rank_modp (matrix_integer_dense.c:1596
5)
==7910==  Address 0x7172cf0 is 0 bytes after a block of size 0 alloc'd
==7910==    at 0x4A1C649: operator new(unsigned long) (vg_replace_malloc.c:230)
==7910==    by 0x14A0DAE2: __gnu_cxx::new_allocator<double>::allocate(unsigned long, void const*) (new_allocator.h:88)
==7910==    by 0x14A0DB0A: std::_Vector_base<double, std::allocator<double> >::_M_allocate(unsigned long) (stl_vector.h:127)
==7910==    by 0x14A0DB3C: std::_Vector_base<double, std::allocator<double> >::_Vector_base(unsigned long, std::allocator<double> const
&) (stl_vector.h:113)
==7910==    by 0x14A0DBC1: std::vector<double, std::allocator<double> >::vector(unsigned long, double const&, std::allocator<double> co
nst&) (stl_vector.h:216)
==7910==    by 0x14A0DC93: LinBox::DenseMatrixBase<double>::DenseMatrixBase(unsigned long, unsigned long) (dense.h:101)
==7910==    by 0x14AB7354: LinBox::DenseMatrix<LinBox::Modular<double> >::DenseMatrix(LinBox::Modular<double> const&, unsigned long, un
signed long) (dense.h:98)
==7910==    by 0x149CDA1F: linbox_modn_dense_rank (linbox_wrap.cpp:92)
==7910==    by 0x147624F0: __pyx_f_4sage_4libs_6linbox_6linbox_17Linbox_modn_dense_rank(__pyx_obj_4sage_4libs_6linbox_6linbox_Linbox_mo
dn_dense*) (linbox.cpp:1511)
==7910==    by 0x1442F979: __pyx_pf_4sage_6matrix_17matrix_modn_dense_17Matrix_modn_dense_rank (matrix_modn_dense.c:7178)
==7910==    by 0x415542: PyObject_Call (abstract.c:1860)
==7910==    by 0x150AB893: __pyx_pf_4sage_6matrix_20matrix_integer_dense_20Matrix_integer_dense__rank_modp (matrix_integer_dense.c:1596
5)
==7910==
==7910== Invalid write of size 8
==7910==    at 0x149D79B3: LinBox::DenseMatrixBase<double>::setEntry(unsigned long, unsigned long, double const&) (dense.h:173)
==7910==    by 0x149DB884: void LinBox::BlasMatrix<double>::createBlasMatrix<LinBox::DenseMatrix<LinBox::Modular<double> > >(LinBox::De
nseMatrix<LinBox::Modular<double> > const&, LinBox::MatrixContainerCategory::Container) (blas-matrix.h:119)
==7910==    by 0x14A0DEAB: LinBox::BlasMatrix<double>::BlasMatrix<LinBox::DenseMatrix<LinBox::Modular<double> > >(LinBox::DenseMatrix<L
inBox::Modular<double> > const&) (blas-matrix.h:87)
==7910==    by 0x14A87781: unsigned long& LinBox::rank<LinBox::DenseMatrix<LinBox::Modular<double> > >(unsigned long&, LinBox::DenseMat
rix<LinBox::Modular<double> > const&, LinBox::RingCategories::ModularTag const&, LinBox::BlasEliminationTraits const&) (rank.h:529)
==7910==    by 0x14ACAB18: unsigned long& LinBox::rank<LinBox::DenseMatrix<LinBox::Modular<double> > >(unsigned long&, LinBox::DenseMat
rix<LinBox::Modular<double> > const&, LinBox::RingCategories::ModularTag const&, LinBox::EliminationSpecifier const&) (rank.h:115)
==7910==    by 0x14ADBC3B: unsigned long& LinBox::rank<LinBox::DenseMatrix<LinBox::Modular<double> > >(unsigned long&, LinBox::DenseMat
rix<LinBox::Modular<double> > const&, LinBox::RingCategories::ModularTag const&, LinBox::HybridSpecifier const&) (rank.h:102)
==7910==    by 0x14ADBEE0: unsigned long& LinBox::rank<LinBox::DenseMatrix<LinBox::Modular<double> > >(unsigned long&, LinBox::DenseMat
rix<LinBox::Modular<double> > const&) (rank.h:84)
==7910==    by 0x149CDB0D: linbox_modn_dense_rank (linbox_wrap.cpp:102)
==7910==    by 0x147624F0: __pyx_f_4sage_4libs_6linbox_6linbox_17Linbox_modn_dense_rank(__pyx_obj_4sage_4libs_6linbox_6linbox_Linbox_mo
dn_dense*) (linbox.cpp:1511)
==7910==    by 0x1442F979: __pyx_pf_4sage_6matrix_17matrix_modn_dense_17Matrix_modn_dense_rank (matrix_modn_dense.c:7178)
==7910==    by 0x415542: PyObject_Call (abstract.c:1860)
==7910==    by 0x150AB893: __pyx_pf_4sage_6matrix_20matrix_integer_dense_20Matrix_integer_dense__rank_modp (matrix_integer_dense.c:1596
5)
==7910==  Address 0x79543e8 is 0 bytes after a block of size 0 alloc'd
==7910==    at 0x4A1C649: operator new(unsigned long) (vg_replace_malloc.c:230)
==7910==    by 0x14A0DAE2: __gnu_cxx::new_allocator<double>::allocate(unsigned long, void const*) (new_allocator.h:88)
==7910==    by 0x14A0DB0A: std::_Vector_base<double, std::allocator<double> >::_M_allocate(unsigned long) (stl_vector.h:127)
==7910==    by 0x14A0DB3C: std::_Vector_base<double, std::allocator<double> >::_Vector_base(unsigned long, std::allocator<double> const
&) (stl_vector.h:113)
==7910==    by 0x14A0DBC1: std::vector<double, std::allocator<double> >::vector(unsigned long, double const&, std::allocator<double> co
nst&) (stl_vector.h:216)
==7910==    by 0x14A0DD5D: LinBox::DenseMatrixBase<double>::DenseMatrixBase(unsigned long, unsigned long) (dense.h:101)
==7910==    by 0x14A0DE45: LinBox::BlasMatrix<double>::BlasMatrix<LinBox::DenseMatrix<LinBox::Modular<double> > >(LinBox::DenseMatrix<L
inBox::Modular<double> > const&) (blas-matrix.h:84)
==7910==    by 0x14A87781: unsigned long& LinBox::rank<LinBox::DenseMatrix<LinBox::Modular<double> > >(unsigned long&, LinBox::DenseMat
rix<LinBox::Modular<double> > const&, LinBox::RingCategories::ModularTag const&, LinBox::BlasEliminationTraits const&) (rank.h:529)
==7910==    by 0x14ACAB18: unsigned long& LinBox::rank<LinBox::DenseMatrix<LinBox::Modular<double> > >(unsigned long&, LinBox::DenseMat
rix<LinBox::Modular<double> > const&, LinBox::RingCategories::ModularTag const&, LinBox::EliminationSpecifier const&) (rank.h:115)
==7910==    by 0x14ADBC3B: unsigned long& LinBox::rank<LinBox::DenseMatrix<LinBox::Modular<double> > >(unsigned long&, LinBox::DenseMat
rix<LinBox::Modular<double> > const&, LinBox::RingCategories::ModularTag const&, LinBox::HybridSpecifier const&) (rank.h:102)
==7910==    by 0x14ADBEE0: unsigned long& LinBox::rank<LinBox::DenseMatrix<LinBox::Modular<double> > >(unsigned long&, LinBox::DenseMat
rix<LinBox::Modular<double> > const&) (rank.h:84)
==7910==    by 0x149CDB0D: linbox_modn_dense_rank (linbox_wrap.cpp:102)
--7910-- VALGRIND INTERNAL ERROR: Valgrind received a signal 11 (SIGSEGV) - exiting
--7910-- si_code=1;  Faulting address: 0x78;  sp: 0x403469CF0

valgrind: the 'impossible' happened:
   Killed by fatal signal
==7910==    at 0x38021BBE: mkFreeBlock (m_mallocfree.c:205)
==7910==    by 0x38022455: vgPlain_arena_malloc (m_mallocfree.c:1204)
==7910==    by 0x380028B8: vgMemCheck_new_block (mc_malloc_wrappers.c:195)
==7910==    by 0x38002CF3: vgMemCheck_malloc (mc_malloc_wrappers.c:226)
==7910==    by 0x38032F1D: do_client_request (scheduler.c:1269)
==7910==    by 0x380342E0: vgPlain_scheduler (scheduler.c:979)
==7910==    by 0x380445AE: run_a_thread_NORETURN (syswrap-linux.c:89)
```

Cheers,

Michael



---

archive/issue_comments_013706.json:
```json
{
    "body": "Attachment [trac-2107.patch](tarball://root/attachments/some-uuid/ticket2107/trac-2107.patch) by @ClementPernet created at 2008-02-09 00:31:39\n\nChange the wrapper for linbox rank, to directly use FFPACK rank.",
    "created_at": "2008-02-09T00:31:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2107#issuecomment-13706",
    "user": "https://github.com/ClementPernet"
}
```

Attachment [trac-2107.patch](tarball://root/attachments/some-uuid/ticket2107/trac-2107.patch) by @ClementPernet created at 2008-02-09 00:31:39

Change the wrapper for linbox rank, to directly use FFPACK rank.



---

archive/issue_comments_013707.json:
```json
{
    "body": "Patch looks good and fixes the problem.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-13T13:14:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2107#issuecomment-13707",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Patch looks good and fixes the problem.

Cheers,

Michael



---

archive/issue_comments_013708.json:
```json
{
    "body": "But it cannot be applied until the issues with #2127 (which touches the same file) are resolved. In that patch we introduce another copy operation, but in that case the above example still segfaults. So I am reverting my positive review to a negative one until those issues are resolved.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-14T17:51:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2107#issuecomment-13708",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

But it cannot be applied until the issues with #2127 (which touches the same file) are resolved. In that patch we introduce another copy operation, but in that case the above example still segfaults. So I am reverting my positive review to a negative one until those issues are resolved.

Cheers,

Michael



---

archive/issue_comments_013709.json:
```json
{
    "body": "Fix the conflict of the previous patch with ticket 2127",
    "created_at": "2008-02-16T23:32:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2107#issuecomment-13709",
    "user": "https://github.com/ClementPernet"
}
```

Fix the conflict of the previous patch with ticket 2127



---

archive/issue_comments_013710.json:
```json
{
    "body": "Attachment [linboxdet.3.patch](tarball://root/attachments/some-uuid/ticket2107/linboxdet.3.patch) by mabshoff created at 2008-02-17 00:26:34\n\nadds the originial problem report as a doctest",
    "created_at": "2008-02-17T00:26:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2107#issuecomment-13710",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [linboxdet.3.patch](tarball://root/attachments/some-uuid/ticket2107/linboxdet.3.patch) by mabshoff created at 2008-02-17 00:26:34

adds the originial problem report as a doctest



---

archive/issue_comments_013711.json:
```json
{
    "body": "Attachment [Sage-2.10.2.alpha1-trac_2107_doctest.patch](tarball://root/attachments/some-uuid/ticket2107/Sage-2.10.2.alpha1-trac_2107_doctest.patch) by mabshoff created at 2008-02-17 00:28:02\n\nThe spkg at \n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.2/alpha1/linbox-20070915.p5.spkg\n\nfixes the issue. It is linbox-20070915.p4 + the fixes from linbox-20070915.p5 at #2127 merged into one.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-17T00:28:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2107#issuecomment-13711",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [Sage-2.10.2.alpha1-trac_2107_doctest.patch](tarball://root/attachments/some-uuid/ticket2107/Sage-2.10.2.alpha1-trac_2107_doctest.patch) by mabshoff created at 2008-02-17 00:28:02

The spkg at 

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.2/alpha1/linbox-20070915.p5.spkg

fixes the issue. It is linbox-20070915.p4 + the fixes from linbox-20070915.p5 at #2127 merged into one.

Cheers,

Michael



---

archive/issue_events_005054.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-17T00:28:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2107",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2107#event-5054"
}
```



---

archive/issue_comments_013712.json:
```json
{
    "body": "Merged Sage-2.10.2.alpha1-trac_2107_doctest.patch and linbox-20070915.p5.spkg in Sage 2.10.2.alpha1",
    "created_at": "2008-02-17T00:28:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2107#issuecomment-13712",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged Sage-2.10.2.alpha1-trac_2107_doctest.patch and linbox-20070915.p5.spkg in Sage 2.10.2.alpha1



---

archive/issue_comments_013713.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-17T00:28:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2107#issuecomment-13713",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
