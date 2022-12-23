# Issue 560: memleak in LinBox::GivPolynomial exposed by ModularSymbols(n,sign=1).decomposition()

archive/issues_000560.json:
```json
{
    "body": "Assignee: mabshoff\n\nHello folks,\n\n```\nfor n in range(10,100): a=ModularSymbols(n,sign=1).decomposition(); print n, get_memory_usage()\n```\n\ncauses (among other things) the following:\n\n```\n==5107== 111,264 (35,472 direct, 75,792 indirect) bytes in 1,478 blocks are definitely lost in loss record 2,758 of 2,944\n==5107==    at 0x4A06019: operator new(unsigned long) (vg_replace_malloc.c:167)\n==5107==    by 0x1F9AF2C0: std::vector<LinBox::GivPolynomial<Integer>*, std::allocator<LinBox::GivPolynomial<Integer>*> >& L\ninBox::GivPolynomialRing<LinBox::UnparametricField<Integer>, Dense>::factor<std::vector<LinBox::GivPolynomial<Integer>*, std\n::allocator<LinBox::GivPolynomial<Integer>*> > >(std::vector<LinBox::GivPolynomial<Integer>*, std::allocator<LinBox::GivPoly\nnomial<Integer>*> >, std::vector<unsigned long, std::allocator<unsigned long> >&, LinBox::GivPolynomial<Integer> const&) (in\n /tmp/Work2/sage-2.8.3.rc3/local/lib/liblinboxwrap.so.0.0.0)\n==5107==    by 0x1FA642A2: LinBox::GivPolynomial<Integer>& LinBox::cia<LinBox::GivPolynomial<Integer>, LinBox::DenseMatrix<L\ninBox::UnparametricField<Integer> > >(LinBox::GivPolynomial<Integer>&, LinBox::DenseMatrix<LinBox::UnparametricField<Integer\n> > const&, LinBox::BlasEliminationTraits const&) (in /tmp/Work2/sage-2.8.3.rc3/local/lib/liblinboxwrap.so.0.0.0)\n==5107==    by 0x1FA64B97: LinBox::GivPolynomial<Integer>& LinBox::charpoly<LinBox::GivPolynomial<Integer>, LinBox::DenseMat\nrix<LinBox::UnparametricField<Integer> > >(LinBox::GivPolynomial<Integer>&, LinBox::DenseMatrix<LinBox::UnparametricField<In\nteger> > const&, LinBox::RingCategories::IntegerTag const&, LinBox::BlasEliminationTraits const&) (in /tmp/Work2/sage-2.8.3.\nrc3/local/lib/liblinboxwrap.so.0.0.0)\n==5107==    by 0x1FA64BD9: LinBox::GivPolynomial<Integer>& LinBox::charpoly<LinBox::GivPolynomial<Integer>, LinBox::Unparame\ntricField<Integer>, LinBox::RingCategories::IntegerTag>(LinBox::GivPolynomial<Integer>&, LinBox::DenseMatrix<LinBox::Unparam\netricField<Integer> > const&, LinBox::RingCategories::IntegerTag const&, LinBox::HybridSpecifier const&) (in /tmp/Work2/sage\n-2.8.3.rc3/local/lib/liblinboxwrap.so.0.0.0)\n==5107==    by 0x1FA64C0D: LinBox::GivPolynomial<Integer>& LinBox::charpoly<LinBox::DenseMatrix<LinBox::UnparametricField<In\nteger> >, LinBox::GivPolynomial<Integer>, LinBox::HybridSpecifier>(LinBox::GivPolynomial<Integer>&, LinBox::DenseMatrix<LinB\nox::UnparametricField<Integer> > const&, LinBox::HybridSpecifier const&) (in /tmp/Work2/sage-2.8.3.rc3/local/lib/liblinboxwr\nap.so.0.0.0)\n==5107==    by 0x1FA64C39: LinBox::GivPolynomial<Integer>& LinBox::charpoly<LinBox::DenseMatrix<LinBox::UnparametricField<In\nteger> >, LinBox::GivPolynomial<Integer> >(LinBox::GivPolynomial<Integer>&, LinBox::DenseMatrix<LinBox::UnparametricField<In\nteger> > const&) (in /tmp/Work2/sage-2.8.3.rc3/local/lib/liblinboxwrap.so.0.0.0)\n==5107==    by 0x1F9AF567: linbox_integer_dense_charpoly (in /tmp/Work2/sage-2.8.3.rc3/local/lib/liblinboxwrap.so.0.0.0)\n==5107==    by 0x1F6CB0F6: __pyx_f_6linbox_20Linbox_integer_dense__poly(_object*, _object*) (linbox.cpp:1124)\n==5107==    by 0x4156A2: PyObject_Call (abstract.c:1860)\n==5107==    by 0x47DB71: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==5107==    by 0x1F6C9E66: __pyx_f_6linbox_20Linbox_integer_dense_charpoly(_object*, _object*) (linbox.cpp:963)\n```\n\nThis looks very ugly. I suspect it can have something to do with the changes made to LinBox in order to compile with gcc 4.2. Those did change some allocation behavior.\n\nCheers,\n\nTagged for 2.8.4\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/560\n\n",
    "created_at": "2007-09-02T00:17:16Z",
    "labels": [
        "memleak",
        "major",
        "bug"
    ],
    "title": "memleak in LinBox::GivPolynomial exposed by ModularSymbols(n,sign=1).decomposition()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/560",
    "user": "mabshoff"
}
```
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

Issue created by migration from https://trac.sagemath.org/ticket/560





---

archive/issue_comments_002898.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-09-02T00:29:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/560",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/560#issuecomment-2898",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_002899.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-07T03:12:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/560",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/560#issuecomment-2899",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_002900.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2007-09-07T03:17:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/560",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/560#issuecomment-2900",
    "user": "mabshoff"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_002901.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-09-07T03:17:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/560",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/560#issuecomment-2901",
    "user": "mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_002902.json:
```json
{
    "body": "Changing status from reopened to new.",
    "created_at": "2007-09-09T06:08:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/560",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/560#issuecomment-2902",
    "user": "mabshoff"
}
```

Changing status from reopened to new.



---

archive/issue_comments_002903.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-09-09T06:09:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/560",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/560#issuecomment-2903",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_002904.json:
```json
{
    "body": "This is likely to be fixed. Please valgrind and report back.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-01T23:53:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/560",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/560#issuecomment-2904",
    "user": "mabshoff"
}
```

This is likely to be fixed. Please valgrind and report back.

Cheers,

Michael



---

archive/issue_comments_002905.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-02T00:48:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/560",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/560#issuecomment-2905",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_002906.json:
```json
{
    "body": "Valgrind says: Fixed in Sage 2.11.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-02T00:48:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/560",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/560#issuecomment-2906",
    "user": "mabshoff"
}
```

Valgrind says: Fixed in Sage 2.11.

Cheers,

Michael
