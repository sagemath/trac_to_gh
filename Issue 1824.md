# Issue 1824: *huge* memory leak in PolyBoRi wrapper

archive/issues_001824.json:
```json
{
    "body": "Assignee: malb\n\nCC:  burcin ralf\n\nValgrinding the `pbori.pyx` leads to:\n\n```\n==14180== LEAK SUMMARY:\n==14180==    definitely lost: 4,152 bytes in 146 blocks.\n==14180==    indirectly lost: 44,286,479 bytes in 330 blocks.\n==14180==      possibly lost: 26,091,338 bytes in 906 blocks.\n==14180==    still reachable: 170,728,275 bytes in 190,628 blocks.\n==14180==         suppressed: 0 bytes in 0 blocks.\n```\n\nIn detail [which is somewhat useless since we do not compile polybori with \"-g\" or strip it]:\n\n```\n==14180== 34,199,168 (1,760 direct, 34,197,408 indirect) bytes in 55 blocks are definitely lost in loss record 2,421 of 7,85\n2\n==14180==    at 0x4A1C344: operator new(unsigned long) (vg_replace_malloc.c:227)\n==14180==    by 0x11C819A1: polybori::OrderedManagerBase<polybori::CCuddInterface>::OrderedManagerBase(unsigned) (in /scratc\nh/mabshoff/release-cycle/sage-2.10.alpha4/local/lib/libpolybori.so)\n==14180==    by 0x11C81CE0: boost::shared_ptr<polybori::OrderedManagerBase<polybori::CCuddInterface> > polybori::get_ordered\n_manager<unsigned>(unsigned&, int) (in /scratch/mabshoff/release-cycle/sage-2.10.alpha4/local/lib/libpolybori.so)\n==14180==    by 0x11C7BB45: polybori::BoolePolyRing::BoolePolyRing(unsigned, int, bool) (in /scratch/mabshoff/release-cycle/\nsage-2.10.alpha4/local/lib/libpolybori.so)\n==14180==    by 0x11A81F1F: __pyx_pf_4sage_5rings_10polynomial_5pbori_21BooleanPolynomialRing___init__(_object*, _object*, _\nobject*) (ccobject.h:50)\n==14180==    by 0x458E40: type_call (typeobject.c:436)\n==14180==    by 0x415542: PyObject_Call (abstract.c:1860)\n==14180==    by 0x482221: PyEval_EvalFrameEx (ceval.c:3775)\n==14180==    by 0x4852CA: PyEval_EvalCodeEx (ceval.c:2831)\n==14180==    by 0x484054: PyEval_EvalFrameEx (ceval.c:494)\n==14180==    by 0x4852CA: PyEval_EvalCodeEx (ceval.c:2831)\n==14180==    by 0x4839EC: PyEval_EvalFrameEx (ceval.c:3660)\n\n==14180== 10,006,804 (80 direct, 10,006,724 indirect) bytes in 5 blocks are definitely lost in loss record 2,566 of 7,852\n==14180==    at 0x4A1C344: operator new(unsigned long) (vg_replace_malloc.c:227)\n==14180==    by 0x11AADF85: std::vector<polybori::BoolePolynomial, std::allocator<polybori::BoolePolynomial> >::operator=(st\nd::vector<polybori::BoolePolynomial, std::allocator<polybori::BoolePolynomial> > const&) (new_allocator.h:88)\n==14180==    by 0x11A9C3E8: __pyx_pf_4sage_5rings_10polynomial_5pbori_31BooleanPolynomialVectorIterator___init__(_object*, _\nobject*, _object*) (pbori.cpp:14851)\n==14180==    by 0x458E40: type_call (typeobject.c:436)\n==14180==    by 0x415542: PyObject_Call (abstract.c:1860)\n==14180==    by 0x47CBE0: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==14180==    by 0x11A775C9: __pyx_pf_4sage_5rings_10polynomial_5pbori_23BooleanPolynomialVector___iter__(_object*) (pbori.cp\np:14614)\n==14180==    by 0x416ABE: PyObject_GetIter (abstract.c:2350)\n==14180==    by 0x435931: listextend (listobject.c:776)\n==14180==    by 0x41797F: PySequence_List (abstract.c:1581)\n==14180==    by 0x478F5F: builtin_sorted (bltinmodule.c:1938)\n==14180==    by 0x415542: PyObject_Call (abstract.c:1860)\n\n==14180== 26,240 (960 direct, 25,280 indirect) bytes in 40 blocks are definitely lost in loss record 3,653 of 7,852\n==14180==    at 0x4A1C344: operator new(unsigned long) (vg_replace_malloc.c:227)\n==14180==    by 0x11C9CA26: boost::shared_ptr<polybori::CTermStackBase<polybori::CCuddNavigator, polybori::CAbstractStackBas\ne<polybori::CCuddNavigator> > >::shared_ptr<polybori::CWrappedStack<polybori::CTermStack<polybori::CCuddNavigator, std::forw\nard_iterator_tag, polybori::CAbstractStackBase<polybori::CCuddNavigator> > > >(polybori::CWrappedStack<polybori::CTermStack<\npolybori::CCuddNavigator, std::forward_iterator_tag, polybori::CAbstractStackBase<polybori::CCuddNavigator> > >*) (in /scrat\nch/mabshoff/release-cycle/sage-2.10.alpha4/local/lib/libpolybori.so)\n==14180==    by 0x11C9ADDE: polybori::LexOrder::leadIteratorBegin(polybori::BoolePolynomial const&) const (in /scratch/mabsh\noff/release-cycle/sage-2.10.alpha4/local/lib/libpolybori.so)\n==14180==    by 0x11C7CF8C: polybori::OrderedManager<polybori::CCuddInterface, polybori::LexOrder>::leadIteratorBegin(polybo\nri::BoolePolynomial const&) const (in /scratch/mabshoff/release-cycle/sage-2.10.alpha4/local/lib/libpolybori.so)\n==14180==    by 0x11C829DE: polybori::BoolePolynomial::orderedBegin() const (in /scratch/mabshoff/release-cycle/sage-2.10.al\npha4/local/lib/libpolybori.so)\n==14180==    by 0x11A7E1E5: __pyx_pf_4sage_5rings_10polynomial_5pbori_17BooleanPolynomial___iter__(_object*) (pbori.cpp:1107\n5)\n==14180==    by 0x416ABE: PyObject_GetIter (abstract.c:2350)\n==14180==    by 0x77BFCD8: izip_new (itertoolsmodule.c:2174)\n==14180==    by 0x458D92: type_call (typeobject.c:422)\n==14180==    by 0x415542: PyObject_Call (abstract.c:1860)\n==14180==    by 0x47CBE0: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==14180==    by 0x11A7C456: __pyx_f_4sage_5rings_10polynomial_5pbori_17BooleanPolynomial__cmp_c_impl(__pyx_obj_4sage_5rings_\n10polynomial_5pbori_BooleanPolynomial*, __pyx_obj_4sage_9structure_7element_Element*) (pbori.cpp:10884)\n\n==14180== 8,640 (288 direct, 8,352 indirect) bytes in 12 blocks are definitely lost in loss record 3,836 of 7,852\n==14180==    at 0x4A1C344: operator new(unsigned long) (vg_replace_malloc.c:227)\n==14180==    by 0x11CA3351: polybori::DegLexOrder::leadIteratorBegin(polybori::BoolePolynomial const&) const (in /scratch/ma\nbshoff/release-cycle/sage-2.10.alpha4/local/lib/libpolybori.so)\n==14180==    by 0x11C7CACC: polybori::OrderedManager<polybori::CCuddInterface, polybori::DegLexOrder>::leadIteratorBegin(pol\nybori::BoolePolynomial const&) const (in /scratch/mabshoff/release-cycle/sage-2.10.alpha4/local/lib/libpolybori.so)\n==14180==    by 0x11C829DE: polybori::BoolePolynomial::orderedBegin() const (in /scratch/mabshoff/release-cycle/sage-2.10.al\npha4/local/lib/libpolybori.so)\n==14180==    by 0x11A7E1E5: __pyx_pf_4sage_5rings_10polynomial_5pbori_17BooleanPolynomial___iter__(_object*) (pbori.cpp:1107\n5)\n==14180==    by 0x416ABE: PyObject_GetIter (abstract.c:2350)\n==14180==    by 0x77BFCD8: izip_new (itertoolsmodule.c:2174)\n==14180==    by 0x458D92: type_call (typeobject.c:422)\n==14180==    by 0x415542: PyObject_Call (abstract.c:1860)\n==14180==    by 0x47CBE0: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==14180==    by 0x11A7C456: __pyx_f_4sage_5rings_10polynomial_5pbori_17BooleanPolynomial__cmp_c_impl(__pyx_obj_4sage_5rings_\n10polynomial_5pbori_BooleanPolynomial*, __pyx_obj_4sage_9structure_7element_Element*) (pbori.cpp:10884)\n==14180==    by 0x97665A7: __pyx_f_4sage_9structure_7element_7Element__richcmp_c_impl (element.c:5395)\n\n==14180== 33,432 (24 direct, 33,408 indirect) bytes in 1 blocks are definitely lost in loss record 4,306 of 7,852\n==14180==    at 0x4A1C344: operator new(unsigned long) (vg_replace_malloc.c:227)\n==14180==    by 0x11C9CA26: boost::shared_ptr<polybori::CTermStackBase<polybori::CCuddNavigator, polybori::CAbstractStackBas\ne<polybori::CCuddNavigator> > >::shared_ptr<polybori::CWrappedStack<polybori::CTermStack<polybori::CCuddNavigator, std::forw\nard_iterator_tag, polybori::CAbstractStackBase<polybori::CCuddNavigator> > > >(polybori::CWrappedStack<polybori::CTermStack<\npolybori::CCuddNavigator, std::forward_iterator_tag, polybori::CAbstractStackBase<polybori::CCuddNavigator> > >*) (in /scrat\nch/mabshoff/release-cycle/sage-2.10.alpha4/local/lib/libpolybori.so)\n==14180==    by 0x11C9ADDE: polybori::LexOrder::leadIteratorBegin(polybori::BoolePolynomial const&) const (in /scratch/mabsh\noff/release-cycle/sage-2.10.alpha4/local/lib/libpolybori.so)\n==14180==    by 0x11C7CF8C: polybori::OrderedManager<polybori::CCuddInterface, polybori::LexOrder>::leadIteratorBegin(polybo\nri::BoolePolynomial const&) const (in /scratch/mabshoff/release-cycle/sage-2.10.alpha4/local/lib/libpolybori.so)\n==14180==    by 0x11C829DE: polybori::BoolePolynomial::orderedBegin() const (in /scratch/mabshoff/release-cycle/sage-2.10.al\npha4/local/lib/libpolybori.so)\n==14180==    by 0x11A7E1E5: __pyx_pf_4sage_5rings_10polynomial_5pbori_17BooleanPolynomial___iter__(_object*) (pbori.cpp:1107\n5)\n==14180==    by 0x416ABE: PyObject_GetIter (abstract.c:2350)\n==14180==    by 0x11AA0697: __pyx_pf_4sage_5rings_10polynomial_5pbori_21BooleanPolynomialRing___call__(_object*, _object*, _\nobject*) (pbori.cpp:5958)\n==14180==    by 0x415542: PyObject_Call (abstract.c:1860)\n==14180==    by 0x482221: PyEval_EvalFrameEx (ceval.c:3775)\n==14180==    by 0x4852CA: PyEval_EvalCodeEx (ceval.c:2831)\n==14180==    by 0x484054: PyEval_EvalFrameEx (ceval.c:494)\n\n==14180== 696 (24 direct, 672 indirect) bytes in 1 blocks are definitely lost in loss record 4,345 of 7,852\n==14180==    at 0x4A1C344: operator new(unsigned long) (vg_replace_malloc.c:227)\n==14180==    by 0x11C9CA26: boost::shared_ptr<polybori::CTermStackBase<polybori::CCuddNavigator, polybori::CAbstractStackBas\ne<polybori::CCuddNavigator> > >::shared_ptr<polybori::CWrappedStack<polybori::CTermStack<polybori::CCuddNavigator, std::forw\nard_iterator_tag, polybori::CAbstractStackBase<polybori::CCuddNavigator> > > >(polybori::CWrappedStack<polybori::CTermStack<\npolybori::CCuddNavigator, std::forward_iterator_tag, polybori::CAbstractStackBase<polybori::CCuddNavigator> > >*) (in /scrat\nch/mabshoff/release-cycle/sage-2.10.alpha4/local/lib/libpolybori.so)\n==14180==    by 0x11C9ADDE: polybori::LexOrder::leadIteratorBegin(polybori::BoolePolynomial const&) const (in /scratch/mabsh\noff/release-cycle/sage-2.10.alpha4/local/lib/libpolybori.so)\n==14180==    by 0x11C7CF8C: polybori::OrderedManager<polybori::CCuddInterface, polybori::LexOrder>::leadIteratorBegin(polybo\nri::BoolePolynomial const&) const (in /scratch/mabshoff/release-cycle/sage-2.10.alpha4/local/lib/libpolybori.so)\n==14180==    by 0x11C829DE: polybori::BoolePolynomial::orderedBegin() const (in /scratch/mabshoff/release-cycle/sage-2.10.al\npha4/local/lib/libpolybori.so)\n==14180==    by 0x11A7E1E5: __pyx_pf_4sage_5rings_10polynomial_5pbori_17BooleanPolynomial___iter__(_object*) (pbori.cpp:1107\n5)\n==14180==    by 0x416ABE: PyObject_GetIter (abstract.c:2350)\n==14180==    by 0x47A9C9: builtin_iter (bltinmodule.c:1152)\n==14180==    by 0x4833C1: PyEval_EvalFrameEx (ceval.c:3564)\n==14180==    by 0x4852CA: PyEval_EvalCodeEx (ceval.c:2831)\n==14180==    by 0x484054: PyEval_EvalFrameEx (ceval.c:494)\n==14180==    by 0x4852CA: PyEval_EvalCodeEx (ceval.c:2831)\n```\n\n\nCheers,\n\nMichael\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1824\n\n",
    "created_at": "2008-01-18T04:54:51Z",
    "labels": [
        "commutative algebra",
        "critical",
        "bug"
    ],
    "title": "*huge* memory leak in PolyBoRi wrapper",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1824",
    "user": "mabshoff"
}
```
Assignee: malb

CC:  burcin ralf

Valgrinding the `pbori.pyx` leads to:

```
==14180== LEAK SUMMARY:
==14180==    definitely lost: 4,152 bytes in 146 blocks.
==14180==    indirectly lost: 44,286,479 bytes in 330 blocks.
==14180==      possibly lost: 26,091,338 bytes in 906 blocks.
==14180==    still reachable: 170,728,275 bytes in 190,628 blocks.
==14180==         suppressed: 0 bytes in 0 blocks.
```

In detail [which is somewhat useless since we do not compile polybori with "-g" or strip it]:

```
==14180== 34,199,168 (1,760 direct, 34,197,408 indirect) bytes in 55 blocks are definitely lost in loss record 2,421 of 7,85
2
==14180==    at 0x4A1C344: operator new(unsigned long) (vg_replace_malloc.c:227)
==14180==    by 0x11C819A1: polybori::OrderedManagerBase<polybori::CCuddInterface>::OrderedManagerBase(unsigned) (in /scratc
h/mabshoff/release-cycle/sage-2.10.alpha4/local/lib/libpolybori.so)
==14180==    by 0x11C81CE0: boost::shared_ptr<polybori::OrderedManagerBase<polybori::CCuddInterface> > polybori::get_ordered
_manager<unsigned>(unsigned&, int) (in /scratch/mabshoff/release-cycle/sage-2.10.alpha4/local/lib/libpolybori.so)
==14180==    by 0x11C7BB45: polybori::BoolePolyRing::BoolePolyRing(unsigned, int, bool) (in /scratch/mabshoff/release-cycle/
sage-2.10.alpha4/local/lib/libpolybori.so)
==14180==    by 0x11A81F1F: __pyx_pf_4sage_5rings_10polynomial_5pbori_21BooleanPolynomialRing___init__(_object*, _object*, _
object*) (ccobject.h:50)
==14180==    by 0x458E40: type_call (typeobject.c:436)
==14180==    by 0x415542: PyObject_Call (abstract.c:1860)
==14180==    by 0x482221: PyEval_EvalFrameEx (ceval.c:3775)
==14180==    by 0x4852CA: PyEval_EvalCodeEx (ceval.c:2831)
==14180==    by 0x484054: PyEval_EvalFrameEx (ceval.c:494)
==14180==    by 0x4852CA: PyEval_EvalCodeEx (ceval.c:2831)
==14180==    by 0x4839EC: PyEval_EvalFrameEx (ceval.c:3660)

==14180== 10,006,804 (80 direct, 10,006,724 indirect) bytes in 5 blocks are definitely lost in loss record 2,566 of 7,852
==14180==    at 0x4A1C344: operator new(unsigned long) (vg_replace_malloc.c:227)
==14180==    by 0x11AADF85: std::vector<polybori::BoolePolynomial, std::allocator<polybori::BoolePolynomial> >::operator=(st
d::vector<polybori::BoolePolynomial, std::allocator<polybori::BoolePolynomial> > const&) (new_allocator.h:88)
==14180==    by 0x11A9C3E8: __pyx_pf_4sage_5rings_10polynomial_5pbori_31BooleanPolynomialVectorIterator___init__(_object*, _
object*, _object*) (pbori.cpp:14851)
==14180==    by 0x458E40: type_call (typeobject.c:436)
==14180==    by 0x415542: PyObject_Call (abstract.c:1860)
==14180==    by 0x47CBE0: PyEval_CallObjectWithKeywords (ceval.c:3433)
==14180==    by 0x11A775C9: __pyx_pf_4sage_5rings_10polynomial_5pbori_23BooleanPolynomialVector___iter__(_object*) (pbori.cp
p:14614)
==14180==    by 0x416ABE: PyObject_GetIter (abstract.c:2350)
==14180==    by 0x435931: listextend (listobject.c:776)
==14180==    by 0x41797F: PySequence_List (abstract.c:1581)
==14180==    by 0x478F5F: builtin_sorted (bltinmodule.c:1938)
==14180==    by 0x415542: PyObject_Call (abstract.c:1860)

==14180== 26,240 (960 direct, 25,280 indirect) bytes in 40 blocks are definitely lost in loss record 3,653 of 7,852
==14180==    at 0x4A1C344: operator new(unsigned long) (vg_replace_malloc.c:227)
==14180==    by 0x11C9CA26: boost::shared_ptr<polybori::CTermStackBase<polybori::CCuddNavigator, polybori::CAbstractStackBas
e<polybori::CCuddNavigator> > >::shared_ptr<polybori::CWrappedStack<polybori::CTermStack<polybori::CCuddNavigator, std::forw
ard_iterator_tag, polybori::CAbstractStackBase<polybori::CCuddNavigator> > > >(polybori::CWrappedStack<polybori::CTermStack<
polybori::CCuddNavigator, std::forward_iterator_tag, polybori::CAbstractStackBase<polybori::CCuddNavigator> > >*) (in /scrat
ch/mabshoff/release-cycle/sage-2.10.alpha4/local/lib/libpolybori.so)
==14180==    by 0x11C9ADDE: polybori::LexOrder::leadIteratorBegin(polybori::BoolePolynomial const&) const (in /scratch/mabsh
off/release-cycle/sage-2.10.alpha4/local/lib/libpolybori.so)
==14180==    by 0x11C7CF8C: polybori::OrderedManager<polybori::CCuddInterface, polybori::LexOrder>::leadIteratorBegin(polybo
ri::BoolePolynomial const&) const (in /scratch/mabshoff/release-cycle/sage-2.10.alpha4/local/lib/libpolybori.so)
==14180==    by 0x11C829DE: polybori::BoolePolynomial::orderedBegin() const (in /scratch/mabshoff/release-cycle/sage-2.10.al
pha4/local/lib/libpolybori.so)
==14180==    by 0x11A7E1E5: __pyx_pf_4sage_5rings_10polynomial_5pbori_17BooleanPolynomial___iter__(_object*) (pbori.cpp:1107
5)
==14180==    by 0x416ABE: PyObject_GetIter (abstract.c:2350)
==14180==    by 0x77BFCD8: izip_new (itertoolsmodule.c:2174)
==14180==    by 0x458D92: type_call (typeobject.c:422)
==14180==    by 0x415542: PyObject_Call (abstract.c:1860)
==14180==    by 0x47CBE0: PyEval_CallObjectWithKeywords (ceval.c:3433)
==14180==    by 0x11A7C456: __pyx_f_4sage_5rings_10polynomial_5pbori_17BooleanPolynomial__cmp_c_impl(__pyx_obj_4sage_5rings_
10polynomial_5pbori_BooleanPolynomial*, __pyx_obj_4sage_9structure_7element_Element*) (pbori.cpp:10884)

==14180== 8,640 (288 direct, 8,352 indirect) bytes in 12 blocks are definitely lost in loss record 3,836 of 7,852
==14180==    at 0x4A1C344: operator new(unsigned long) (vg_replace_malloc.c:227)
==14180==    by 0x11CA3351: polybori::DegLexOrder::leadIteratorBegin(polybori::BoolePolynomial const&) const (in /scratch/ma
bshoff/release-cycle/sage-2.10.alpha4/local/lib/libpolybori.so)
==14180==    by 0x11C7CACC: polybori::OrderedManager<polybori::CCuddInterface, polybori::DegLexOrder>::leadIteratorBegin(pol
ybori::BoolePolynomial const&) const (in /scratch/mabshoff/release-cycle/sage-2.10.alpha4/local/lib/libpolybori.so)
==14180==    by 0x11C829DE: polybori::BoolePolynomial::orderedBegin() const (in /scratch/mabshoff/release-cycle/sage-2.10.al
pha4/local/lib/libpolybori.so)
==14180==    by 0x11A7E1E5: __pyx_pf_4sage_5rings_10polynomial_5pbori_17BooleanPolynomial___iter__(_object*) (pbori.cpp:1107
5)
==14180==    by 0x416ABE: PyObject_GetIter (abstract.c:2350)
==14180==    by 0x77BFCD8: izip_new (itertoolsmodule.c:2174)
==14180==    by 0x458D92: type_call (typeobject.c:422)
==14180==    by 0x415542: PyObject_Call (abstract.c:1860)
==14180==    by 0x47CBE0: PyEval_CallObjectWithKeywords (ceval.c:3433)
==14180==    by 0x11A7C456: __pyx_f_4sage_5rings_10polynomial_5pbori_17BooleanPolynomial__cmp_c_impl(__pyx_obj_4sage_5rings_
10polynomial_5pbori_BooleanPolynomial*, __pyx_obj_4sage_9structure_7element_Element*) (pbori.cpp:10884)
==14180==    by 0x97665A7: __pyx_f_4sage_9structure_7element_7Element__richcmp_c_impl (element.c:5395)

==14180== 33,432 (24 direct, 33,408 indirect) bytes in 1 blocks are definitely lost in loss record 4,306 of 7,852
==14180==    at 0x4A1C344: operator new(unsigned long) (vg_replace_malloc.c:227)
==14180==    by 0x11C9CA26: boost::shared_ptr<polybori::CTermStackBase<polybori::CCuddNavigator, polybori::CAbstractStackBas
e<polybori::CCuddNavigator> > >::shared_ptr<polybori::CWrappedStack<polybori::CTermStack<polybori::CCuddNavigator, std::forw
ard_iterator_tag, polybori::CAbstractStackBase<polybori::CCuddNavigator> > > >(polybori::CWrappedStack<polybori::CTermStack<
polybori::CCuddNavigator, std::forward_iterator_tag, polybori::CAbstractStackBase<polybori::CCuddNavigator> > >*) (in /scrat
ch/mabshoff/release-cycle/sage-2.10.alpha4/local/lib/libpolybori.so)
==14180==    by 0x11C9ADDE: polybori::LexOrder::leadIteratorBegin(polybori::BoolePolynomial const&) const (in /scratch/mabsh
off/release-cycle/sage-2.10.alpha4/local/lib/libpolybori.so)
==14180==    by 0x11C7CF8C: polybori::OrderedManager<polybori::CCuddInterface, polybori::LexOrder>::leadIteratorBegin(polybo
ri::BoolePolynomial const&) const (in /scratch/mabshoff/release-cycle/sage-2.10.alpha4/local/lib/libpolybori.so)
==14180==    by 0x11C829DE: polybori::BoolePolynomial::orderedBegin() const (in /scratch/mabshoff/release-cycle/sage-2.10.al
pha4/local/lib/libpolybori.so)
==14180==    by 0x11A7E1E5: __pyx_pf_4sage_5rings_10polynomial_5pbori_17BooleanPolynomial___iter__(_object*) (pbori.cpp:1107
5)
==14180==    by 0x416ABE: PyObject_GetIter (abstract.c:2350)
==14180==    by 0x11AA0697: __pyx_pf_4sage_5rings_10polynomial_5pbori_21BooleanPolynomialRing___call__(_object*, _object*, _
object*) (pbori.cpp:5958)
==14180==    by 0x415542: PyObject_Call (abstract.c:1860)
==14180==    by 0x482221: PyEval_EvalFrameEx (ceval.c:3775)
==14180==    by 0x4852CA: PyEval_EvalCodeEx (ceval.c:2831)
==14180==    by 0x484054: PyEval_EvalFrameEx (ceval.c:494)

==14180== 696 (24 direct, 672 indirect) bytes in 1 blocks are definitely lost in loss record 4,345 of 7,852
==14180==    at 0x4A1C344: operator new(unsigned long) (vg_replace_malloc.c:227)
==14180==    by 0x11C9CA26: boost::shared_ptr<polybori::CTermStackBase<polybori::CCuddNavigator, polybori::CAbstractStackBas
e<polybori::CCuddNavigator> > >::shared_ptr<polybori::CWrappedStack<polybori::CTermStack<polybori::CCuddNavigator, std::forw
ard_iterator_tag, polybori::CAbstractStackBase<polybori::CCuddNavigator> > > >(polybori::CWrappedStack<polybori::CTermStack<
polybori::CCuddNavigator, std::forward_iterator_tag, polybori::CAbstractStackBase<polybori::CCuddNavigator> > >*) (in /scrat
ch/mabshoff/release-cycle/sage-2.10.alpha4/local/lib/libpolybori.so)
==14180==    by 0x11C9ADDE: polybori::LexOrder::leadIteratorBegin(polybori::BoolePolynomial const&) const (in /scratch/mabsh
off/release-cycle/sage-2.10.alpha4/local/lib/libpolybori.so)
==14180==    by 0x11C7CF8C: polybori::OrderedManager<polybori::CCuddInterface, polybori::LexOrder>::leadIteratorBegin(polybo
ri::BoolePolynomial const&) const (in /scratch/mabshoff/release-cycle/sage-2.10.alpha4/local/lib/libpolybori.so)
==14180==    by 0x11C829DE: polybori::BoolePolynomial::orderedBegin() const (in /scratch/mabshoff/release-cycle/sage-2.10.al
pha4/local/lib/libpolybori.so)
==14180==    by 0x11A7E1E5: __pyx_pf_4sage_5rings_10polynomial_5pbori_17BooleanPolynomial___iter__(_object*) (pbori.cpp:1107
5)
==14180==    by 0x416ABE: PyObject_GetIter (abstract.c:2350)
==14180==    by 0x47A9C9: builtin_iter (bltinmodule.c:1152)
==14180==    by 0x4833C1: PyEval_EvalFrameEx (ceval.c:3564)
==14180==    by 0x4852CA: PyEval_EvalCodeEx (ceval.c:2831)
==14180==    by 0x484054: PyEval_EvalFrameEx (ceval.c:494)
==14180==    by 0x4852CA: PyEval_EvalCodeEx (ceval.c:2831)
```


Cheers,

Michael


Issue created by migration from https://trac.sagemath.org/ticket/1824





---

archive/issue_comments_011548.json:
```json
{
    "body": "Changing assignee from malb to mabshoff.",
    "created_at": "2008-01-18T05:06:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1824#issuecomment-11548",
    "user": "mabshoff"
}
```

Changing assignee from malb to mabshoff.



---

archive/issue_comments_011549.json:
```json
{
    "body": "Changing component from commutative algebra to memleak.",
    "created_at": "2008-01-18T05:06:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1824#issuecomment-11549",
    "user": "mabshoff"
}
```

Changing component from commutative algebra to memleak.



---

archive/issue_comments_011550.json:
```json
{
    "body": "D'oh ... assigned to the correct component now ;)",
    "created_at": "2008-01-18T05:06:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1824#issuecomment-11550",
    "user": "mabshoff"
}
```

D'oh ... assigned to the correct component now ;)



---

archive/issue_comments_011551.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-20T10:07:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1824#issuecomment-11551",
    "user": "burcin"
}
```

Changing status from new to assigned.



---

archive/issue_comments_011552.json:
```json
{
    "body": "Changing assignee from mabshoff to burcin.",
    "created_at": "2008-01-20T10:07:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1824#issuecomment-11552",
    "user": "burcin"
}
```

Changing assignee from mabshoff to burcin.



---

archive/issue_comments_011553.json:
```json
{
    "body": "If you install the polybori package with the environment variable `SAGE_DEBUG` set, then it builds the debug symbols.\n\nI will look into these.",
    "created_at": "2008-01-20T10:07:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1824#issuecomment-11553",
    "user": "burcin"
}
```

If you install the polybori package with the environment variable `SAGE_DEBUG` set, then it builds the debug symbols.

I will look into these.



---

archive/issue_comments_011554.json:
```json
{
    "body": "Hi brucin,\n\nrpw might have a fix for this issue. You should ping him about this. \n\nCheers,\n\nMichael",
    "created_at": "2008-01-21T07:15:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1824#issuecomment-11554",
    "user": "mabshoff"
}
```

Hi brucin,

rpw might have a fix for this issue. You should ping him about this. 

Cheers,

Michael



---

archive/issue_comments_011555.json:
```json
{
    "body": "Attachment [pbori_memleak_1.patch](tarball://root/attachments/some-uuid/ticket1824/pbori_memleak_1.patch) by malb created at 2008-02-05 23:48:26\n\nfixes at least parts of the memleaks",
    "created_at": "2008-02-05T23:48:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1824#issuecomment-11555",
    "user": "malb"
}
```

Attachment [pbori_memleak_1.patch](tarball://root/attachments/some-uuid/ticket1824/pbori_memleak_1.patch) by malb created at 2008-02-05 23:48:26

fixes at least parts of the memleaks



---

archive/issue_comments_011556.json:
```json
{
    "body": "The attached patch adds destructors for all iterators which significantly reduces the leakage for me. However, I still have a lot of leakage when doctesting `pbori.pyx`:\n\n\n```\n==31473== 524,288 bytes in 1 blocks are still reachable in loss record 2,590 of 2,625\n==31473==    at 0x4C21FAB: malloc (vg_replace_malloc.c:207)\n==31473==    by 0x1A297E76: MMalloc (in /usr/local/sage-2.10.1/local/lib/libpolybori.so)\n==31473==    by 0x1A2B62EC: cuddInitTable (in /usr/local/sage-2.10.1/local/lib/libpolybori.so)\n==31473==    by 0x1A29B9B2: Cudd_Init (in /usr/local/sage-2.10.1/local/lib/libpolybori.so)\n==31473==    by 0x1A303FA3: polybori::OrderedManagerBase<polybori::CCuddInterface>::OrderedManagerBase(unsigned) (in /usr/local/sage-2.10.1/local/lib/libpolybori.so)\n==31473==    by 0x1A304318: boost::shared_ptr<polybori::OrderedManagerBase<polybori::CCuddInterface> > polybori::get_ordered_manager<unsigned>(unsigned&, int) (in /usr/local/sage-2.10.1/local/lib/libpolybori.so)\n==31473==    by 0x1A2FE7B5: polybori::BoolePolyRing::BoolePolyRing(unsigned, int, bool) (in /usr/local/sage-2.10.1/local/lib/libpolybori.so)\n==31473==    by 0x1A023A92: polybori::BoolePolyRing* Construct_pp<polybori::BoolePolyRing, unsigned, int>(void*, unsigned const&, int const&) (ccobject.h:50)\n==31473==    by 0x1A009ED2: __pyx_pf_4sage_5rings_10polynomial_5pbori_21BooleanPolynomialRing___init__(_object*, _object*, _object*) (pbori.cpp:2726)\n==31473==    by 0x45CC20: type_call (typeobject.c:436)\n==31473==    by 0x417BB2: PyObject_Call (abstract.c:1860)\n==31473==    by 0x4808A1: PyEval_CallObjectWithKeywords (ceval.c:3433)\n```\n",
    "created_at": "2008-02-05T23:50:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1824#issuecomment-11556",
    "user": "malb"
}
```

The attached patch adds destructors for all iterators which significantly reduces the leakage for me. However, I still have a lot of leakage when doctesting `pbori.pyx`:


```
==31473== 524,288 bytes in 1 blocks are still reachable in loss record 2,590 of 2,625
==31473==    at 0x4C21FAB: malloc (vg_replace_malloc.c:207)
==31473==    by 0x1A297E76: MMalloc (in /usr/local/sage-2.10.1/local/lib/libpolybori.so)
==31473==    by 0x1A2B62EC: cuddInitTable (in /usr/local/sage-2.10.1/local/lib/libpolybori.so)
==31473==    by 0x1A29B9B2: Cudd_Init (in /usr/local/sage-2.10.1/local/lib/libpolybori.so)
==31473==    by 0x1A303FA3: polybori::OrderedManagerBase<polybori::CCuddInterface>::OrderedManagerBase(unsigned) (in /usr/local/sage-2.10.1/local/lib/libpolybori.so)
==31473==    by 0x1A304318: boost::shared_ptr<polybori::OrderedManagerBase<polybori::CCuddInterface> > polybori::get_ordered_manager<unsigned>(unsigned&, int) (in /usr/local/sage-2.10.1/local/lib/libpolybori.so)
==31473==    by 0x1A2FE7B5: polybori::BoolePolyRing::BoolePolyRing(unsigned, int, bool) (in /usr/local/sage-2.10.1/local/lib/libpolybori.so)
==31473==    by 0x1A023A92: polybori::BoolePolyRing* Construct_pp<polybori::BoolePolyRing, unsigned, int>(void*, unsigned const&, int const&) (ccobject.h:50)
==31473==    by 0x1A009ED2: __pyx_pf_4sage_5rings_10polynomial_5pbori_21BooleanPolynomialRing___init__(_object*, _object*, _object*) (pbori.cpp:2726)
==31473==    by 0x45CC20: type_call (typeobject.c:436)
==31473==    by 0x417BB2: PyObject_Call (abstract.c:1860)
==31473==    by 0x4808A1: PyEval_CallObjectWithKeywords (ceval.c:3433)
```




---

archive/issue_comments_011557.json:
```json
{
    "body": "Patch looks good to me. I will look into the remaining memleak. It looks like CuddInit is called - we might need to call some deallocation routine for Cudd before exiting Sage. I will open another ticket once I figure out whose fault the memleak is.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-07T05:31:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1824#issuecomment-11557",
    "user": "mabshoff"
}
```

Patch looks good to me. I will look into the remaining memleak. It looks like CuddInit is called - we might need to call some deallocation routine for Cudd before exiting Sage. I will open another ticket once I figure out whose fault the memleak is.

Cheers,

Michael



---

archive/issue_comments_011558.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha0",
    "created_at": "2008-02-07T05:32:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1824#issuecomment-11558",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.2.alpha0



---

archive/issue_comments_011559.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-07T05:32:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1824#issuecomment-11559",
    "user": "mabshoff"
}
```

Resolution: fixed
