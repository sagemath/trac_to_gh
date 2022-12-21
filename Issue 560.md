# Issue 560: memleak in LinBox::GivPolynomial exposed by ModularSymbols(n,sign=1).decomposition()

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-09-02 00:17:16

Assignee: mabshoff

Hello folks,

```
for n in range(10,100): a=ModularSymbols(n,sign=1).decomposition(); print n, get_memory_usage()
```

causes (among other things) the following:

```
==5107== 111,264 (35,472 direct, 75,792 indirect) bytes in 1,478 blocks are definitely lost in loss record 2,758 of 2,944
==5107==    at 0x4A06019: operator new(unsigned long) (vg_replace_malloc.c:167)
==5107==    by 0x1F9AF2C0: std::vector<LinBox::GivPolynomial<Integer>*, std::allocator<LinBox::GivPolynomial<Integer>*> >& L
inBox::GivPolynomialRing<LinBox::UnparametricField<Integer>, Dense>::factor<std::vector<LinBox::GivPolynomial<Integer>*, std
::allocator<LinBox::GivPolynomial<Integer>*> > >(std::vector<LinBox::GivPolynomial<Integer>*, std::allocator<LinBox::GivPoly
nomial<Integer>*> >, std::vector<unsigned long, std::allocator<unsigned long> >&, LinBox::GivPolynomial<Integer> const&) (in
 /tmp/Work2/sage-2.8.3.rc3/local/lib/liblinboxwrap.so.0.0.0)
==5107==    by 0x1FA642A2: LinBox::GivPolynomial<Integer>& LinBox::cia<LinBox::GivPolynomial<Integer>, LinBox::DenseMatrix<L
inBox::UnparametricField<Integer> > >(LinBox::GivPolynomial<Integer>&, LinBox::DenseMatrix<LinBox::UnparametricField<Integer
> > const&, LinBox::BlasEliminationTraits const&) (in /tmp/Work2/sage-2.8.3.rc3/local/lib/liblinboxwrap.so.0.0.0)
==5107==    by 0x1FA64B97: LinBox::GivPolynomial<Integer>& LinBox::charpoly<LinBox::GivPolynomial<Integer>, LinBox::DenseMat
rix<LinBox::UnparametricField<Integer> > >(LinBox::GivPolynomial<Integer>&, LinBox::DenseMatrix<LinBox::UnparametricField<In
teger> > const&, LinBox::RingCategories::IntegerTag const&, LinBox::BlasEliminationTraits const&) (in /tmp/Work2/sage-2.8.3.
rc3/local/lib/liblinboxwrap.so.0.0.0)
==5107==    by 0x1FA64BD9: LinBox::GivPolynomial<Integer>& LinBox::charpoly<LinBox::GivPolynomial<Integer>, LinBox::Unparame
tricField<Integer>, LinBox::RingCategories::IntegerTag>(LinBox::GivPolynomial<Integer>&, LinBox::DenseMatrix<LinBox::Unparam
etricField<Integer> > const&, LinBox::RingCategories::IntegerTag const&, LinBox::HybridSpecifier const&) (in /tmp/Work2/sage
-2.8.3.rc3/local/lib/liblinboxwrap.so.0.0.0)
==5107==    by 0x1FA64C0D: LinBox::GivPolynomial<Integer>& LinBox::charpoly<LinBox::DenseMatrix<LinBox::UnparametricField<In
teger> >, LinBox::GivPolynomial<Integer>, LinBox::HybridSpecifier>(LinBox::GivPolynomial<Integer>&, LinBox::DenseMatrix<LinB
ox::UnparametricField<Integer> > const&, LinBox::HybridSpecifier const&) (in /tmp/Work2/sage-2.8.3.rc3/local/lib/liblinboxwr
ap.so.0.0.0)
==5107==    by 0x1FA64C39: LinBox::GivPolynomial<Integer>& LinBox::charpoly<LinBox::DenseMatrix<LinBox::UnparametricField<In
teger> >, LinBox::GivPolynomial<Integer> >(LinBox::GivPolynomial<Integer>&, LinBox::DenseMatrix<LinBox::UnparametricField<In
teger> > const&) (in /tmp/Work2/sage-2.8.3.rc3/local/lib/liblinboxwrap.so.0.0.0)
==5107==    by 0x1F9AF567: linbox_integer_dense_charpoly (in /tmp/Work2/sage-2.8.3.rc3/local/lib/liblinboxwrap.so.0.0.0)
==5107==    by 0x1F6CB0F6: __pyx_f_6linbox_20Linbox_integer_dense__poly(_object*, _object*) (linbox.cpp:1124)
==5107==    by 0x4156A2: PyObject_Call (abstract.c:1860)
==5107==    by 0x47DB71: PyEval_CallObjectWithKeywords (ceval.c:3433)
==5107==    by 0x1F6C9E66: __pyx_f_6linbox_20Linbox_integer_dense_charpoly(_object*, _object*) (linbox.cpp:963)
```

This looks very ugly. I suspect it can have something to do with the changes made to LinBox in order to compile with gcc 4.2. Those did change some allocation behavior.

Cheers,

Tagged for 2.8.4

Michael


---

Comment by mabshoff created at 2007-09-02 00:29:50

Changing status from new to assigned.


---

Comment by was created at 2007-09-07 03:12:47

Resolution: fixed


---

Comment by mabshoff created at 2007-09-07 03:17:50

Resolution changed from fixed to 


---

Comment by mabshoff created at 2007-09-07 03:17:50

Changing status from closed to reopened.


---

Comment by mabshoff created at 2007-09-09 06:08:55

Changing status from reopened to new.


---

Comment by mabshoff created at 2007-09-09 06:09:01

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-04-01 23:53:15

This is likely to be fixed. Please valgrind and report back.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-02 00:48:04

Resolution: fixed


---

Comment by mabshoff created at 2008-04-02 00:48:04

Valgrind says: Fixed in Sage 2.11.

Cheers,

Michael
