# Issue 2107: serious malloc problem triggered by Hecke operator computation

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-02-08 09:50:23

Assignee: was


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



---

Comment by mabshoff created at 2008-02-08 22:47:55

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

Attachment

Change the wrapper for linbox rank, to directly use FFPACK rank.


---

Comment by mabshoff created at 2008-02-13 13:14:11

Patch looks good and fixes the problem.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-14 17:51:25

But it cannot be applied until the issues with #2127 (which touches the same file) are resolved. In that patch we introduce another copy operation, but in that case the above example still segfaults. So I am reverting my positive review to a negative one until those issues are resolved.

Cheers,

Michael


---

Comment by cpernet created at 2008-02-16 23:32:45

Fix the conflict of the previous patch with ticket 2127


---

Attachment

adds the originial problem report as a doctest


---

Attachment

The spkg at 

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.2/alpha1/linbox-20070915.p5.spkg

fixes the issue. It is linbox-20070915.p4 + the fixes from linbox-20070915.p5 at #2127 merged into one.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-17 00:28:53

Merged Sage-2.10.2.alpha1-trac_2107_doctest.patch and linbox-20070915.p5.spkg in Sage 2.10.2.alpha1


---

Comment by mabshoff created at 2008-02-17 00:28:53

Resolution: fixed
