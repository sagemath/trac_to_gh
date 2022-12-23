# Issue 1026: memleak in linbox's gmp++_int_io.C

Issue created by migration from https://trac.sagemath.org/ticket/1026

Original creator: mabshoff

Original creation time: 2007-10-29 04:17:24

Assignee: mabshoff

Keywords: LinBox

Omega says:

```
==4541== Loss Record 193: Leaked 171 (0xAB) bytes in 32 blocks
==4541==    at 0x1235298A: Integer::operator std::string() const (gmp++_int_io.C:53)
==4541==    by 0x12237B33: std::vector<LinBox::GivPolynomial<Integer>*, std::allocator<LinBox::GivPolynomial<Integer>*> >& L
inBox::GivPolynomialRing<LinBox::UnparametricField<Integer>, Dense>::factor<std::vector<LinBox::GivPolynomial<Integer>*, std
::allocator<LinBox::GivPolynomial<Integer>*> > >(std::vector<LinBox::GivPolynomial<Integer>*, std::allocator<LinBox::GivPoly
nomial<Integer>*> >, std::vector<unsigned long, std::allocator<unsigned long> >&, LinBox::GivPolynomial<Integer> const&) (gi
varo-polynomial.h:68)
==4541==    by 0x12350688: LinBox::GivPolynomial<Integer>& LinBox::cia<LinBox::GivPolynomial<Integer>, LinBox::DenseMatrix<L
inBox::UnparametricField<Integer> > >(LinBox::GivPolynomial<Integer>&, LinBox::DenseMatrix<LinBox::UnparametricField<Integer
> > const&, LinBox::BlasEliminationTraits const&) (cia.h:54)
==4541==    by 0x12350F77: LinBox::GivPolynomial<Integer>& LinBox::charpoly<LinBox::GivPolynomial<Integer>, LinBox::DenseMat
rix<LinBox::UnparametricField<Integer> > >(LinBox::GivPolynomial<Integer>&, LinBox::DenseMatrix<LinBox::UnparametricField<In
teger> > const&, LinBox::RingCategories::IntegerTag const&, LinBox::BlasEliminationTraits const&) (charpoly.h:188)
==4541==    by 0x12350FB9: LinBox::GivPolynomial<Integer>& LinBox::charpoly<LinBox::GivPolynomial<Integer>, LinBox::Unparame
tricField<Integer>, LinBox::RingCategories::IntegerTag>(LinBox::GivPolynomial<Integer>&, LinBox::DenseMatrix<LinBox::Unparam
etricField<Integer> > const&, LinBox::RingCategories::IntegerTag const&, LinBox::HybridSpecifier const&) (charpoly.h:127)
==4541==    by 0x12350FED: LinBox::GivPolynomial<Integer>& LinBox::charpoly<LinBox::DenseMatrix<LinBox::UnparametricField<In
teger> >, LinBox::GivPolynomial<Integer>, LinBox::HybridSpecifier>(LinBox::GivPolynomial<Integer>&, LinBox::DenseMatrix<LinB
ox::UnparametricField<Integer> > const&, LinBox::HybridSpecifier const&) (charpoly.h:81)
==4541==    by 0x12351019: LinBox::GivPolynomial<Integer>& LinBox::charpoly<LinBox::DenseMatrix<LinBox::UnparametricField<In
teger> >, LinBox::GivPolynomial<Integer> >(LinBox::GivPolynomial<Integer>&, LinBox::DenseMatrix<LinBox::UnparametricField<In
teger> > const&) (charpoly.h:94)
==4541==    by 0x12237F4D: linbox_integer_dense_charpoly (linbox_wrap.cpp:309)
==4541==    by 0x11FC85B9: __pyx_f_4sage_4libs_6linbox_6linbox_20Linbox_integer_dense__poly(_object*, _object*) (linbox.cpp:
2972)
==4541==    by 0x415522: PyObject_Call (abstract.c:1860)
==4541==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)
==4541==    by 0x11FC73C2: __pyx_f_4sage_4libs_6linbox_6linbox_20Linbox_integer_dense_charpoly(_object*, _object*) (linbox.c
pp:2840)
==4541==  Blocks allocated
==4541==    at 0x4A1B674: operator new[](unsigned long) (vg_replace_malloc.c:271)
==4541==    by 0x123528EA: Integer::operator std::string() const (gmp++_int_io.C:48)
==4541==    by 0x12237B33: std::vector<LinBox::GivPolynomial<Integer>*, std::allocator<LinBox::GivPolynomial<Integer>*> >& L
inBox::GivPolynomialRing<LinBox::UnparametricField<Integer>, Dense>::factor<std::vector<LinBox::GivPolynomial<Integer>*, std
::allocator<LinBox::GivPolynomial<Integer>*> > >(std::vector<LinBox::GivPolynomial<Integer>*, std::allocator<LinBox::GivPoly
nomial<Integer>*> >, std::vector<unsigned long, std::allocator<unsigned long> >&, LinBox::GivPolynomial<Integer> const&) (gi
varo-polynomial.h:68)
==4541==    by 0x12350688: LinBox::GivPolynomial<Integer>& LinBox::cia<LinBox::GivPolynomial<Integer>, LinBox::DenseMatrix<L
inBox::UnparametricField<Integer> > >(LinBox::GivPolynomial<Integer>&, LinBox::DenseMatrix<LinBox::UnparametricField<Integer
> > const&, LinBox::BlasEliminationTraits const&) (cia.h:54)
==4541==    by 0x12350F77: LinBox::GivPolynomial<Integer>& LinBox::charpoly<LinBox::GivPolynomial<Integer>, LinBox::DenseMat
rix<LinBox::UnparametricField<Integer> > >(LinBox::GivPolynomial<Integer>&, LinBox::DenseMatrix<LinBox::UnparametricField<In
teger> > const&, LinBox::RingCategories::IntegerTag const&, LinBox::BlasEliminationTraits const&) (charpoly.h:188)
==4541==    by 0x12350FB9: LinBox::GivPolynomial<Integer>& LinBox::charpoly<LinBox::GivPolynomial<Integer>, LinBox::Unparame
tricField<Integer>, LinBox::RingCategories::IntegerTag>(LinBox::GivPolynomial<Integer>&, LinBox::DenseMatrix<LinBox::Unparam
etricField<Integer> > const&, LinBox::RingCategories::IntegerTag const&, LinBox::HybridSpecifier const&) (charpoly.h:127)
==4541==    by 0x12350FED: LinBox::GivPolynomial<Integer>& LinBox::charpoly<LinBox::DenseMatrix<LinBox::UnparametricField<In
teger> >, LinBox::GivPolynomial<Integer>, LinBox::HybridSpecifier>(LinBox::GivPolynomial<Integer>&, LinBox::DenseMatrix<LinB
ox::UnparametricField<Integer> > const&, LinBox::HybridSpecifier const&) (charpoly.h:81)
==4541==    by 0x12351019: LinBox::GivPolynomial<Integer>& LinBox::charpoly<LinBox::DenseMatrix<LinBox::UnparametricField<In
teger> >, LinBox::GivPolynomial<Integer> >(LinBox::GivPolynomial<Integer>&, LinBox::DenseMatrix<LinBox::UnparametricField<In
teger> > const&) (charpoly.h:94)
==4541==    by 0x12237F4D: linbox_integer_dense_charpoly (linbox_wrap.cpp:309)
==4541==    by 0x11FC85B9: __pyx_f_4sage_4libs_6linbox_6linbox_20Linbox_integer_dense__poly(_object*, _object*) (linbox.cpp:
2972)
```


I will post an updated LinBox.spkg with two small additional tweaks shortly.

before the patch:

```
==15811== LEAK SUMMARY:
==15811==    definitely lost: 406,088 bytes in 5,792 blocks.
==15811==    indirectly lost: 415,504 bytes in 7,199 blocks.
==15811==      possibly lost: 382,110 bytes in 1,198 blocks.
==15811==    still reachable: 93,391,247 bytes in 1,343,745 blocks.
==15811==         suppressed: 0 bytes in 0 blocks.
```

with the patch:

```
==19741== LEAK SUMMARY:
==19741==    definitely lost: 11,608 bytes in 352 blocks.
==19741==    indirectly lost: 286,560 bytes in 390 blocks.
==19741==      possibly lost: 463,342 bytes in 879 blocks.
==19741==    still reachable: 71,109,048 bytes in 1,285,713 blocks.
==19741==         suppressed: 0 bytes in 0 blocks.
```


Cheers,

Michael


---

Comment by mabshoff created at 2007-10-29 04:17:45

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-10-29 04:37:40

For the new spkg check out

http://sage.math.washington.edu/home/mabshoff/linbox-20070915.p1.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2007-11-01 10:21:40

Resolution: fixed


---

Comment by mabshoff created at 2007-11-01 10:21:40

applied to 2.8.11.alpha0
