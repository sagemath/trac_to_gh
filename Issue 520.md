# Issue 520: memory leak: some small issues with Givaro

Issue created by migration from https://trac.sagemath.org/ticket/520

Original creator: mabshoff

Original creation time: 2007-08-29 22:08:32

Assignee: malb

The following issues popped up when running the libsingular doctest under valgring:

```
==11727== 12 bytes in 1 blocks are still reachable in loss record 485 of 2,401
==11727==    at 0x4A05809: malloc (vg_replace_malloc.c:149)
==11727==    by 0x1B255400: GivMMFreeList::_allocate(unsigned long) (in /tmp/Work2/sage-2.8.3.alpha2/local/lib/libgivaro.so.
0.0.0)
==11727==    by 0x1B2530DA: GivMMFreeList::allocate(unsigned long) (in /tmp/Work2/sage-2.8.3.alpha2/local/lib/libgivaro.so.0
.0.0)
==11727==    by 0x1B25312E: GivaroMM<int>::allocate(unsigned long) (in /tmp/Work2/sage-2.8.3.alpha2/local/lib/libgivaro.so.0
.0.0)
==11727==    by 0x1B260725: Array0<char>::allocate(unsigned long) (in /tmp/Work2/sage-2.8.3.alpha2/local/lib/libgivaro.so.0.
0.0)
==11727==    by 0x1B260028: Indeter::Indeter(char const*) (in /tmp/Work2/sage-2.8.3.alpha2/local/lib/libgivaro.so.0.0.0)
==11727==    by 0x1B02A08E: GFqDom<int>::GFqDom(unsigned, unsigned, std::vector<unsigned, std::allocator<unsigned> > const&)
 (givgfq.inl:1035)
==11727==    by 0x1B01DBAB: __pyx_f_19finite_field_givaro_18FiniteField_givaro___init__(_object*, _object*, _object*) (finit
e_field_givaro.cpp:1762)
==11727==    by 0x45A321: type_call (typeobject.c:436)
==11727==    by 0x4156A2: PyObject_Call (abstract.c:1860)
```

and

```
==11727== 24 bytes in 3 blocks are definitely lost in loss record 542 of 2,401
==11727==    at 0x4A06019: operator new(unsigned long) (vg_replace_malloc.c:167)
==11727==    by 0x1B028C00: Poly1FactorDom<GFqDom<int>, Dense, GivRandom>::is_prim_root(givvector<int> const&, givvector<int
> const&) const (givpoly1proot.inl:236)
==11727==    by 0x1B02A3F7: GFqDom<int>::GFqDom(unsigned, unsigned, std::vector<unsigned, std::allocator<unsigned> > const&)
 (givpoly1proot.inl:300)
==11727==    by 0x1B01DBAB: __pyx_f_19finite_field_givaro_18FiniteField_givaro___init__(_object*, _object*, _object*) (finit
e_field_givaro.cpp:1762)
==11727==    by 0x45A321: type_call (typeobject.c:436)
==11727==    by 0x4156A2: PyObject_Call (abstract.c:1860)
==11727==    by 0x47DB71: PyEval_CallObjectWithKeywords (ceval.c:3433)
==11727==    by 0x1AFFDB21: __pyx_f_19finite_field_givaro_unpickle_FiniteField_givaro(_object*, _object*, _object*) (finite_
field_givaro.cpp:6588)
==11727==    by 0x4156A2: PyObject_Call (abstract.c:1860)
==11727==    by 0x47DB71: PyEval_CallObjectWithKeywords (ceval.c:3433)
==11727==    by 0xAE9E21D: Instance_New (cPickle.c:3632)
==11727==    by 0xAEA43F1: load_reduce (cPickle.c:4396)
```


Those two issue show up with varying size, there might be more, I didn't check in greatest detail but I will revisit this issue down the road.

Cheers,

Michael


---

Comment by mabshoff created at 2007-08-30 10:41:42

Changing component from basic arithmetic to memleak.


---

Comment by mabshoff created at 2008-03-15 05:05:05

Changing assignee from malb to mabshoff.


---

Comment by mabshoff created at 2008-03-15 05:05:05

When valgrinding devel/sage-main/sage/rings/finite_field_givaro.pyx with 100% coverage now shows no leak when using the givaro.spkg from #2525. Hence this ticket should be closed once that ticket is merged.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-15 05:05:05

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-03-15 06:45:43

This has been fixed due to the new Givaro.spkg from #2524 (not #2525 as mentioned mistakenly in the previous comment.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-15 06:46:16

Resolution: fixed


---

Comment by mabshoff created at 2008-03-15 06:46:16

Closed in Sage 2.10.4.alpha0 due to merging the Giavro.spkg from #2524.
