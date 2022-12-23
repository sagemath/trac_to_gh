# Issue 1091: small memleaks exposed by ntl_mat_GF2E.py (from 2.8.12.alpha0)

Issue created by migration from https://trac.sagemath.org/ticket/1091

Original creator: mabshoff

Original creation time: 2007-11-04 00:00:54

Assignee: mabshoff

from ntl_mat_GF2E.py

```
==4434== 8 bytes in 1 blocks are definitely lost in loss record 8 of 2,016
==4434==    at 0x4A1C344: operator new(unsigned long) (vg_replace_malloc.c:227)
==4434==    by 0xE452F76: Poly1FactorDom<GFqDom<int>, Dense, GivRandom>::is_prim_root(givvector<int> const&, givvector<int>
const&) const (givpoly1proot.inl:236)
==4434==    by 0xE4547F6: GFqDom<int>::GFqDom(unsigned, unsigned, std::vector<unsigned, std::allocator<unsigned> > const&) (
givpoly1proot.inl:300)
==4434==    by 0xE446EC2: __pyx_pf_4sage_5rings_19finite_field_givaro_18FiniteField_givaro___init__(_object*, _object*, _obj
ect*) (finite_field_givaro.cpp:1755)
==4434==    by 0x459220: type_call (typeobject.c:436)
==4434==    by 0x415522: PyObject_Call (abstract.c:1860)
==4434==    by 0x481ACA: PyEval_EvalFrameEx (ceval.c:3844)
==4434==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==4434==    by 0x4CE4C0: function_call (funcobject.c:517)
==4434==    by 0x415522: PyObject_Call (abstract.c:1860)
==4434==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)
==4434==    by 0xDC6C9AA: __pyx_pf_4sage_4libs_3ntl_12ntl_mat_GF2E_12ntl_mat_GF2E__sage_(_object*, _object*, _object*) (ntl_
mat_GF2E.cpp:3038)

==4434== 8 bytes in 1 blocks are definitely lost in loss record 9 of 2,016
==4434==    at 0x4A1C344: operator new(unsigned long) (vg_replace_malloc.c:227)
==4434==    by 0xE453F11: GFqDom<int>::GFqDom(unsigned, unsigned) (givgfq.inl:930)
==4434==    by 0xE45445F: GFqDom<int>::GFqDom(unsigned, unsigned, std::vector<unsigned, std::allocator<unsigned> > const&) (
givgfq.inl:1033)
==4434==    by 0xE446EC2: __pyx_pf_4sage_5rings_19finite_field_givaro_18FiniteField_givaro___init__(_object*, _object*, _obj
ect*) (finite_field_givaro.cpp:1755)
==4434==    by 0x459220: type_call (typeobject.c:436)
==4434==    by 0x415522: PyObject_Call (abstract.c:1860)
==4434==    by 0x481ACA: PyEval_EvalFrameEx (ceval.c:3844)
==4434==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==4434==    by 0x4CE4C0: function_call (funcobject.c:517)
==4434==    by 0x415522: PyObject_Call (abstract.c:1860)
==4434==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)
==4434==    by 0xDC6C9AA: __pyx_pf_4sage_4libs_3ntl_12ntl_mat_GF2E_12ntl_mat_GF2E__sage_(_object*, _object*, _object*) (ntl_
mat_GF2E.cpp:3038)

==4434== 8 bytes in 1 blocks are definitely lost in loss record 10 of 2,016
==4434==    at 0x4A1C344: operator new(unsigned long) (vg_replace_malloc.c:227)
==4434==    by 0xE452F76: Poly1FactorDom<GFqDom<int>, Dense, GivRandom>::is_prim_root(givvector<int> const&, givvector<int>
const&) const (givpoly1proot.inl:236)
==4434==    by 0xE4547F6: GFqDom<int>::GFqDom(unsigned, unsigned, std::vector<unsigned, std::allocator<unsigned> > const&) (
givpoly1proot.inl:300)
==4434==    by 0xE446EC2: __pyx_pf_4sage_5rings_19finite_field_givaro_18FiniteField_givaro___init__(_object*, _object*, _obj
ect*) (finite_field_givaro.cpp:1755)
==4434==    by 0x459220: type_call (typeobject.c:436)
==4434==    by 0x415522: PyObject_Call (abstract.c:1860)
==4434==    by 0x481ACA: PyEval_EvalFrameEx (ceval.c:3844)
==4434==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==4434==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)
==4434==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==4434==    by 0x483CC4: PyEval_EvalFrameEx (ceval.c:494)
==4434==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
```



---

Attachment


---

Comment by wjp created at 2008-01-09 23:52:47

Givaro has a number of constructors with a parameter of type `RandIter&` with default argument of the type `(RandIter& g = *(new RandIter()) )`. This is used to initialize a RandIter member variable, copying the new'ed object and immediately leaking the original.

All three of the valgrind traces found by mabshoff above are leaks of this type.

The attached patch to `givaro-3.2.6.p4` should fix this be changing the constructor declarations to `(RandIter g = RandIter() )`.

It does change the signature of the constructors (`RandIter& -> RandIter`), but I don't see any places where this would be a problem after a scan over the givaro sources.


---

Comment by mabshoff created at 2008-01-10 04:42:44

Hi wjp - the patch doesn't fix the leak for me. I did rebuild NTL just to be on the save side, but that didn't fix it either. Any tips what to do? Did you verify that the leak is gone via valgrind?

Cheers,

Michael


---

Comment by wjp created at 2008-01-10 10:06:21

You may have to manually trigger a rebuild of `finite_field_givaro.pyx`. I think `sage -b` didn't pick up the changes to the givaro headers automatically.


---

Comment by mabshoff created at 2008-01-10 18:13:47

Thanks wjp. I can confirm that rebuilding `finite_field_givaro.pyx` does fix the issue. An givaro.spkg which incorporates the fix is at:

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10/alpha2/givaro-3.2.6.p5.spkg

Cheers,

Michale


---

Comment by mabshoff created at 2008-01-10 18:14:12

Resolution: fixed


---

Comment by mabshoff created at 2008-01-10 18:14:12

Merged in Sage 2.10.alpha2.
