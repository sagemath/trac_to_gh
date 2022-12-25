# Issue 894: small ntl memory leaks

archive/issues_000894.json:
```json
{
    "body": "Assignee: mabshoff\n\nKeywords: ntl, givaro\n\nHello,\n\nnot being motivated to do anything productive I ended up valgrinding all ntl doctests. The following is a list of results. No patches yet, I am busy hunting bigger leaks in LinBox for now :)\n\nFrom doctest_ntl_mat_GF2E.py:\n\n```\n==21715== 8 bytes in 1 blocks are definitely lost in loss record 9 of 1,999\n==21715==    at 0x4A1C344: operator new(unsigned long) (vg_replace_malloc.c:227)\n==21715==    by 0xFC803B0: GFqDom<int>::GFqDom(unsigned, unsigned) (givgfq.inl:930)\n==21715==    by 0xFC8091F: GFqDom<int>::GFqDom(unsigned, unsigned, std::vector<unsigned, std::allocator<unsigned> > const&)\n(givgfq.inl:1033)\n==21715==    by 0xFC733DF: __pyx_f_py_19finite_field_givaro_18FiniteField_givaro___init__(_object*, _object*, _object*) (fin\nite_field_givaro.cpp:1847)\n==21715==    by 0x459220: type_call (typeobject.c:436)\n==21715==    by 0x415522: PyObject_Call (abstract.c:1860)\n==21715==    by 0x481ACA: PyEval_EvalFrameEx (ceval.c:3844)\n==21715==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n==21715==    by 0x4CE4C0: function_call (funcobject.c:517)\n==21715==    by 0x415522: PyObject_Call (abstract.c:1860)\n==21715==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==21715==    by 0xD7E6BC0: __pyx_f_py_8ntl_GF2E_ntl_GF2E_sage(_object*, _object*, _object*) (ntl_GF2E.cpp:813)\n\n==21715== 8 bytes in 1 blocks are definitely lost in loss record 9 of 1,999\n==21715==    at 0x4A1C344: operator new(unsigned long) (vg_replace_malloc.c:227)\n==21715==    by 0xFC803B0: GFqDom<int>::GFqDom(unsigned, unsigned) (givgfq.inl:930)\n==21715==    by 0xFC8091F: GFqDom<int>::GFqDom(unsigned, unsigned, std::vector<unsigned, std::allocator<unsigned> > const&)\n(givgfq.inl:1033)\n==21715==    by 0xFC733DF: __pyx_f_py_19finite_field_givaro_18FiniteField_givaro___init__(_object*, _object*, _object*) (fin\nite_field_givaro.cpp:1847)\n==21715==    by 0x459220: type_call (typeobject.c:436)\n==21715==    by 0x415522: PyObject_Call (abstract.c:1860)\n==21715==    by 0x481ACA: PyEval_EvalFrameEx (ceval.c:3844)\n==21715==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n==21715==    by 0x4CE4C0: function_call (funcobject.c:517)\n==21715==    by 0x415522: PyObject_Call (abstract.c:1860)\n==21715==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==21715==    by 0xD7E6BC0: __pyx_f_py_8ntl_GF2E_ntl_GF2E_sage(_object*, _object*, _object*) (ntl_GF2E.cpp:813)\n```\n\nFrom doctest_ntl_ZZ.py:\n\n```\n==21729== 16 bytes in 1 blocks are definitely lost in loss record 40 of 1,847\n==21729==    at 0x4A1BC36: realloc (vg_replace_malloc.c:420)\n==21729==    by 0x5D68E30: __gmpz_realloc (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/local/lib/libgmp.so.3.4.1)\n==21729==    by 0x5C416CA: mpz_set_pylong (mpz_pylong.c:74)\n==21729==    by 0x5C41C19: ZZ_set_pylong(NTL::ZZ&, _object*) (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/devel/sage-main/c_lib/\nlibcsage.so)\n==21729==    by 0xC6BB3DA: __pyx_f_py_6ntl_ZZ_6ntl_ZZ___init__(_object*, _object*, _object*) (ntl_ZZ.cpp:1079)\n==21729==    by 0x459220: type_call (typeobject.c:436)\n==21729==    by 0x415522: PyObject_Call (abstract.c:1860)\n==21729==    by 0x481E91: PyEval_EvalFrameEx (ceval.c:3775)\n==21729==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n==21729==    by 0x483CC4: PyEval_EvalFrameEx (ceval.c:494)\n==21729==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n==21729==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)\n```\n\ndoctest_ntl_ZZ_pE.py\n\n```\n==21736== 16 bytes in 1 blocks are definitely lost in loss record 67 of 1,880\n==21736==    at 0x4A1BC36: realloc (vg_replace_malloc.c:420)\n==21736==    by 0x5D68E30: __gmpz_realloc (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/local/lib/libgmp.so.3.4.1)\n==21736==    by 0x5C416CA: mpz_set_pylong (mpz_pylong.c:74)\n==21736==    by 0x5C41C19: ZZ_set_pylong(NTL::ZZ&, _object*) (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/devel/sage-main/c_lib/\nlibcsage.so)\n==21736==    by 0xCE24430: __pyx_f_py_9ntl_ZZ_pE_9ntl_ZZ_pE___init__(_object*, _object*, _object*) (ntl_ZZ_pE.cpp:1383)\n==21736==    by 0x459220: type_call (typeobject.c:436)\n==21736==    by 0x415522: PyObject_Call (abstract.c:1860)\n==21736==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==21736==    by 0xCD17DFA: __pyx_f_py_16ntl_ZZ_pEContext_22ntl_ZZ_pEContext_class_ZZ_pE(_object*, _object*, _object*) (ntl_Z\nZ_pEContext.cpp:726)\n==21736==    by 0x483031: PyEval_EvalFrameEx (ceval.c:3564)\n==21736==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n==21736==    by 0x483CC4: PyEval_EvalFrameEx (ceval.c:494)\n\n==21736== 32 bytes in 1 blocks are indirectly lost in loss record 109 of 1,880\n==21736==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)\n==21736==    by 0x6179D59: _ntl_gblock_construct_alloc (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/local/lib/libntl.so)\n==21736==    by 0x61D9EB2: NTL::BlockConstruct(NTL::ZZ_p*, long) (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/local/lib/libntl.s\no)\n==21736==    by 0x61DA0CB: NTL::vec_ZZ_p::SetLength(long) (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/local/lib/libntl.so)\n==21736==    by 0x61DA881: NTL::vec_ZZ_p::operator=(NTL::vec_ZZ_p const&) (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/local/lib\n/libntl.so)\n==21736==    by 0x5C46805: NTL::vec_ZZ_p::vec_ZZ_p(NTL::vec_ZZ_p const&) (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/devel/sage\n-main/c_lib/libcsage.so)\n==21736==    by 0x5C46824: NTL::ZZ_pX::ZZ_pX(NTL::ZZ_pX const&) (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/devel/sage-main/c_l\nib/libcsage.so)\n==21736==    by 0x5C42DEA: ZZ_pE_to_ZZ_pX (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/devel/sage-main/c_lib/libcsage.so)\n==21736==    by 0xCE22EA7: __pyx_f_9ntl_ZZ_pE_9ntl_ZZ_pE_get_as_ZZ_pX(__pyx_obj_9ntl_ZZ_pE_ntl_ZZ_pE*) (ntl_ZZ_pE.cpp:2705)\n==21736==    by 0xCE2110E: __pyx_f_py_9ntl_ZZ_pE_9ntl_ZZ_pE___reduce__(_object*, _object*) (ntl_ZZ_pE.cpp:1753)\n==21736==    by 0x415522: PyObject_Call (abstract.c:1860)\n==21736==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)\n\n==21736== 64 bytes in 1 blocks are indirectly lost in loss record 217 of 1,880\n==21736==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)\n==21736==    by 0x61DA129: NTL::vec_ZZ_p::SetLength(long) (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/local/lib/libntl.so)\n==21736==    by 0x61DA881: NTL::vec_ZZ_p::operator=(NTL::vec_ZZ_p const&) (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/local/lib\n/libntl.so)\n==21736==    by 0x5C46805: NTL::vec_ZZ_p::vec_ZZ_p(NTL::vec_ZZ_p const&) (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/devel/sage\n-main/c_lib/libcsage.so)\n==21736==    by 0x5C46824: NTL::ZZ_pX::ZZ_pX(NTL::ZZ_pX const&) (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/devel/sage-main/c_l\nib/libcsage.so)\n==21736==    by 0x5C42DEA: ZZ_pE_to_ZZ_pX (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/devel/sage-main/c_lib/libcsage.so)\n==21736==    by 0xCE22EA7: __pyx_f_9ntl_ZZ_pE_9ntl_ZZ_pE_get_as_ZZ_pX(__pyx_obj_9ntl_ZZ_pE_ntl_ZZ_pE*) (ntl_ZZ_pE.cpp:2705)\n==21736==    by 0xCE2110E: __pyx_f_py_9ntl_ZZ_pE_9ntl_ZZ_pE___reduce__(_object*, _object*) (ntl_ZZ_pE.cpp:1753)\n==21736==    by 0x415522: PyObject_Call (abstract.c:1860)\n==21736==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==21736==    by 0x4589BF: object_reduce_ex (typeobject.c:2786)\n==21736==    by 0x415522: PyObject_Call (abstract.c:1860)\n\n==21736== 64 bytes in 1 blocks are indirectly lost in loss record 220 of 1,880\n==21736==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)\n==21736==    by 0x6179D59: _ntl_gblock_construct_alloc (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/local/lib/libntl.so)\n==21736==    by 0x61D9EB2: NTL::BlockConstruct(NTL::ZZ_p*, long) (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/local/lib/libntl.s\no)\n==21736==    by 0x61DA0CB: NTL::vec_ZZ_p::SetLength(long) (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/local/lib/libntl.so)\n==21736==    by 0x61DA881: NTL::vec_ZZ_p::operator=(NTL::vec_ZZ_p const&) (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/local/lib\n/libntl.so)\n==21736==    by 0x5C46805: NTL::vec_ZZ_p::vec_ZZ_p(NTL::vec_ZZ_p const&) (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/devel/sage\n-main/c_lib/libcsage.so)\n==21736==    by 0x5C46824: NTL::ZZ_pX::ZZ_pX(NTL::ZZ_pX const&) (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/devel/sage-main/c_l\nib/libcsage.so)\n==21736==    by 0x5C42DEA: ZZ_pE_to_ZZ_pX (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/devel/sage-main/c_lib/libcsage.so)\n==21736==    by 0xCE22EA7: __pyx_f_9ntl_ZZ_pE_9ntl_ZZ_pE_get_as_ZZ_pX(__pyx_obj_9ntl_ZZ_pE_ntl_ZZ_pE*) (ntl_ZZ_pE.cpp:2705)\n==21736==    by 0xCE20569: __pyx_f_py_9ntl_ZZ_pE_9ntl_ZZ_pE_get_as_ZZ_pX_doctest(_object*, _object*) (ntl_ZZ_pE.cpp:2753)\n==21736==    by 0x482FE8: PyEval_EvalFrameEx (ceval.c:3548)\n==21736==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n\n==21736== 64 bytes in 1 blocks are indirectly lost in loss record 221 of 1,880\n==21736==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)\n==21736==    by 0x61DA129: NTL::vec_ZZ_p::SetLength(long) (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/local/lib/libntl.so)\n==21736==    by 0x61DA881: NTL::vec_ZZ_p::operator=(NTL::vec_ZZ_p const&) (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/local/lib\n/libntl.so)\n==21736==    by 0x5C46805: NTL::vec_ZZ_p::vec_ZZ_p(NTL::vec_ZZ_p const&) (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/devel/sage\n-main/c_lib/libcsage.so)\n==21736==    by 0x5C46824: NTL::ZZ_pX::ZZ_pX(NTL::ZZ_pX const&) (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/devel/sage-main/c_l\nib/libcsage.so)\n==21736==    by 0x5C42DEA: ZZ_pE_to_ZZ_pX (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/devel/sage-main/c_lib/libcsage.so)\n==21736==    by 0xCE22EA7: __pyx_f_9ntl_ZZ_pE_9ntl_ZZ_pE_get_as_ZZ_pX(__pyx_obj_9ntl_ZZ_pE_ntl_ZZ_pE*) (ntl_ZZ_pE.cpp:2705)\n==21736==    by 0xCE20569: __pyx_f_py_9ntl_ZZ_pE_9ntl_ZZ_pE_get_as_ZZ_pX_doctest(_object*, _object*) (ntl_ZZ_pE.cpp:2753)\n==21736==    by 0x482FE8: PyEval_EvalFrameEx (ceval.c:3548)\n==21736==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n==21736==    by 0x483CC4: PyEval_EvalFrameEx (ceval.c:494)\n==21736==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:283\n\n==21736== 136 (8 direct, 128 indirect) bytes in 1 blocks are definitely lost in loss record 257 of 1,880\n==21736==    at 0x4A1C344: operator new(unsigned long) (vg_replace_malloc.c:227)\n==21736==    by 0x5C42DDA: ZZ_pE_to_ZZ_pX (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/devel/sage-main/c_lib/libcsage.so)\n==21736==    by 0xCE22EA7: __pyx_f_9ntl_ZZ_pE_9ntl_ZZ_pE_get_as_ZZ_pX(__pyx_obj_9ntl_ZZ_pE_ntl_ZZ_pE*) (ntl_ZZ_pE.cpp:2705)\n==21736==    by 0xCE20569: __pyx_f_py_9ntl_ZZ_pE_9ntl_ZZ_pE_get_as_ZZ_pX_doctest(_object*, _object*) (ntl_ZZ_pE.cpp:2753)\n==21736==    by 0x482FE8: PyEval_EvalFrameEx (ceval.c:3548)\n==21736==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n==21736==    by 0x483CC4: PyEval_EvalFrameEx (ceval.c:494)\n==21736==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n==21736==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)\n==21736==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n==21736==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)\n==21736==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n```\n\nFrom doctest_ntl_mat_ZZ.py:\n\n```\n==21903== 10 bytes in 1 blocks are definitely lost in loss record 28 of 1,874\n==21903==    at 0x4A1BFE4: operator new[](unsigned long) (vg_replace_malloc.c:271)\n==21903==    by 0x60454B5: ZZX_repr (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/devel/sage-main/c_lib/libcsage.so)\n==21903==    by 0xCAE53A6: __pyx_f_py_7ntl_ZZX_7ntl_ZZX___repr__(_object*) (ntl_ZZX.cpp:1483)\n==21903==    by 0x442FF9: PyObject_Repr (object.c:361)\n==21903==    by 0x429B3B: PyFile_WriteObject (fileobject.c:2196)\n==21903==    by 0x4AC158: sys_displayhook (sysmodule.c:114)\n==21903==    by 0x415522: PyObject_Call (abstract.c:1860)\n==21903==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==21903==    by 0x4827EE: PyEval_EvalFrameEx (ceval.c:1530)\n==21903==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n==21903==    by 0x483CC4: PyEval_EvalFrameEx (ceval.c:494)\n==21903==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n```\n\nFrom doctest_ntl_ZZ_pEX.py:\n\n```\n==21921== 408 (24 direct, 384 indirect) bytes in 3 blocks are definitely lost in loss record 404 of 1,859\n==21921==    at 0x4A1C344: operator new(unsigned long) (vg_replace_malloc.c:227)\n==21921==    by 0x6042DDA: ZZ_pE_to_ZZ_pX (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/devel/sage-main/c_lib/libcsage.so)\n==21921==    by 0xCE22EA7: __pyx_f_9ntl_ZZ_pE_9ntl_ZZ_pE_get_as_ZZ_pX(__pyx_obj_9ntl_ZZ_pE_ntl_ZZ_pE*) (ntl_ZZ_pE.cpp:2705)\n==21921==    by 0xCE2110E: __pyx_f_py_9ntl_ZZ_pE_9ntl_ZZ_pE___reduce__(_object*, _object*) (ntl_ZZ_pE.cpp:1753)\n==21921==    by 0x415522: PyObject_Call (abstract.c:1860)\n==21921==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==21921==    by 0x4589BF: object_reduce_ex (typeobject.c:2786)\n==21921==    by 0x415522: PyObject_Call (abstract.c:1860)\n==21921==    by 0x76EA743: save (cPickle.c:2495)\n==21921==    by 0x76EBEEC: batch_list (cPickle.c:1558)\n==21921==    by 0x76EAC7B: save (cPickle.c:1626)\n==21921==    by 0x76EA25F: save_tuple (cPickle.c:1381)\n```\n\nFrom doctest_ntl_ZZX.py:\n\n```\n==21981== 8 bytes in 1 blocks are definitely lost in loss record 17 of 1,854\n==21981==    at 0x4A1C344: operator new(unsigned long) (vg_replace_malloc.c:227)\n==21981==    by 0x6045378: ZZX_div (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/devel/sage-main/c_lib/libcsage.so)\n==21981==    by 0xCAE97D9: __pyx_f_py_7ntl_ZZX_7ntl_ZZX___div__(_object*, _object*) (ntl_ZZX.cpp:2388)\n==21981==    by 0x4157EC: binary_op1 (abstract.c:398)\n==21981==    by 0x416DDD: PyNumber_Divide (abstract.c:450)\n==21981==    by 0x47F911: PyEval_EvalFrameEx (ceval.c:1083)\n==21981==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n==21981==    by 0x483CC4: PyEval_EvalFrameEx (ceval.c:494)\n==21981==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n==21981==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)\n==21981==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n==21981==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)\n\n==21981== 10 bytes in 1 blocks are definitely lost in loss record 29 of 1,854\n==21981==    at 0x4A1BFE4: operator new[](unsigned long) (vg_replace_malloc.c:271)\n==21981==    by 0x60454B5: ZZX_repr (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/devel/sage-main/c_lib/libcsage.so)\n==21981==    by 0xCAE53A6: __pyx_f_py_7ntl_ZZX_7ntl_ZZX___repr__(_object*) (ntl_ZZX.cpp:1483)\n==21981==    by 0x482FE8: PyEval_EvalFrameEx (ceval.c:3548)\n==21981==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n==21981==    by 0x483CC4: PyEval_EvalFrameEx (ceval.c:494)\n==21981==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n==21981==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)\n==21981==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n==21981==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)\n==21981==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n==21981==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)\n```\n\nFrom doctest_ntl_GF2E.py:\n\n```\n==22056== 8 bytes in 1 blocks are definitely lost in loss record 32 of 1,987\n==22056==    at 0x4A1C344: operator new(unsigned long) (vg_replace_malloc.c:227)\n==22056==    by 0xFC7F3D6: Poly1FactorDom<GFqDom<int>, Dense, GivRandom>::is_prim_root(givvector<int> const&, givvector<int>\n const&) const (givpoly1proot.inl:236)\n==22056==    by 0xFC80CB6: GFqDom<int>::GFqDom(unsigned, unsigned, std::vector<unsigned, std::allocator<unsigned> > const&)\n(givpoly1proot.inl:300)\n==22056==    by 0xFC733DF: __pyx_f_py_19finite_field_givaro_18FiniteField_givaro___init__(_object*, _object*, _object*) (fin\nite_field_givaro.cpp:1847)\n==22056==    by 0x459220: type_call (typeobject.c:436)\n==22056==    by 0x415522: PyObject_Call (abstract.c:1860)\n==22056==    by 0x481ACA: PyEval_EvalFrameEx (ceval.c:3844)\n==22056==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n==22056==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)\n==22056==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n==22056==    by 0x483CC4: PyEval_EvalFrameEx (ceval.c:494)\n==22056==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n```\n\nFrom doctest_ntl_ZZ_p.py:\n\n```\n==22060== 16 bytes in 1 blocks are definitely lost in loss record 72 of 1,859\n==22060==    at 0x4A1BC36: realloc (vg_replace_malloc.c:420)\n==22060==    by 0x5D68E30: __gmpz_realloc (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/local/lib/libgmp.so.3.4.1)\n==22060==    by 0x5C416CA: mpz_set_pylong (mpz_pylong.c:74)\n==22060==    by 0x5C41C19: ZZ_set_pylong(NTL::ZZ&, _object*) (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/devel/sage-main/c_lib/\nlibcsage.so)\n==22060==    by 0xC9D6520: __pyx_f_py_8ntl_ZZ_p_8ntl_ZZ_p___init__(_object*, _object*, _object*) (ntl_ZZ_p.cpp:1190)\n==22060==    by 0x459220: type_call (typeobject.c:436)\n==22060==    by 0x415522: PyObject_Call (abstract.c:1860)\n==22060==    by 0x481E91: PyEval_EvalFrameEx (ceval.c:3775)\n==22060==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n==22060==    by 0x483CC4: PyEval_EvalFrameEx (ceval.c:494)\n==22060==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n==22060==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)\n```\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/894\n\n",
    "created_at": "2007-10-13T22:32:30Z",
    "labels": [
        "component: memleak",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.12",
    "title": "small ntl memory leaks",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/894",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

Keywords: ntl, givaro

Hello,

not being motivated to do anything productive I ended up valgrinding all ntl doctests. The following is a list of results. No patches yet, I am busy hunting bigger leaks in LinBox for now :)

From doctest_ntl_mat_GF2E.py:

```
==21715== 8 bytes in 1 blocks are definitely lost in loss record 9 of 1,999
==21715==    at 0x4A1C344: operator new(unsigned long) (vg_replace_malloc.c:227)
==21715==    by 0xFC803B0: GFqDom<int>::GFqDom(unsigned, unsigned) (givgfq.inl:930)
==21715==    by 0xFC8091F: GFqDom<int>::GFqDom(unsigned, unsigned, std::vector<unsigned, std::allocator<unsigned> > const&)
(givgfq.inl:1033)
==21715==    by 0xFC733DF: __pyx_f_py_19finite_field_givaro_18FiniteField_givaro___init__(_object*, _object*, _object*) (fin
ite_field_givaro.cpp:1847)
==21715==    by 0x459220: type_call (typeobject.c:436)
==21715==    by 0x415522: PyObject_Call (abstract.c:1860)
==21715==    by 0x481ACA: PyEval_EvalFrameEx (ceval.c:3844)
==21715==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==21715==    by 0x4CE4C0: function_call (funcobject.c:517)
==21715==    by 0x415522: PyObject_Call (abstract.c:1860)
==21715==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)
==21715==    by 0xD7E6BC0: __pyx_f_py_8ntl_GF2E_ntl_GF2E_sage(_object*, _object*, _object*) (ntl_GF2E.cpp:813)

==21715== 8 bytes in 1 blocks are definitely lost in loss record 9 of 1,999
==21715==    at 0x4A1C344: operator new(unsigned long) (vg_replace_malloc.c:227)
==21715==    by 0xFC803B0: GFqDom<int>::GFqDom(unsigned, unsigned) (givgfq.inl:930)
==21715==    by 0xFC8091F: GFqDom<int>::GFqDom(unsigned, unsigned, std::vector<unsigned, std::allocator<unsigned> > const&)
(givgfq.inl:1033)
==21715==    by 0xFC733DF: __pyx_f_py_19finite_field_givaro_18FiniteField_givaro___init__(_object*, _object*, _object*) (fin
ite_field_givaro.cpp:1847)
==21715==    by 0x459220: type_call (typeobject.c:436)
==21715==    by 0x415522: PyObject_Call (abstract.c:1860)
==21715==    by 0x481ACA: PyEval_EvalFrameEx (ceval.c:3844)
==21715==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==21715==    by 0x4CE4C0: function_call (funcobject.c:517)
==21715==    by 0x415522: PyObject_Call (abstract.c:1860)
==21715==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)
==21715==    by 0xD7E6BC0: __pyx_f_py_8ntl_GF2E_ntl_GF2E_sage(_object*, _object*, _object*) (ntl_GF2E.cpp:813)
```

From doctest_ntl_ZZ.py:

```
==21729== 16 bytes in 1 blocks are definitely lost in loss record 40 of 1,847
==21729==    at 0x4A1BC36: realloc (vg_replace_malloc.c:420)
==21729==    by 0x5D68E30: __gmpz_realloc (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/local/lib/libgmp.so.3.4.1)
==21729==    by 0x5C416CA: mpz_set_pylong (mpz_pylong.c:74)
==21729==    by 0x5C41C19: ZZ_set_pylong(NTL::ZZ&, _object*) (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/devel/sage-main/c_lib/
libcsage.so)
==21729==    by 0xC6BB3DA: __pyx_f_py_6ntl_ZZ_6ntl_ZZ___init__(_object*, _object*, _object*) (ntl_ZZ.cpp:1079)
==21729==    by 0x459220: type_call (typeobject.c:436)
==21729==    by 0x415522: PyObject_Call (abstract.c:1860)
==21729==    by 0x481E91: PyEval_EvalFrameEx (ceval.c:3775)
==21729==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==21729==    by 0x483CC4: PyEval_EvalFrameEx (ceval.c:494)
==21729==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==21729==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)
```

doctest_ntl_ZZ_pE.py

```
==21736== 16 bytes in 1 blocks are definitely lost in loss record 67 of 1,880
==21736==    at 0x4A1BC36: realloc (vg_replace_malloc.c:420)
==21736==    by 0x5D68E30: __gmpz_realloc (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/local/lib/libgmp.so.3.4.1)
==21736==    by 0x5C416CA: mpz_set_pylong (mpz_pylong.c:74)
==21736==    by 0x5C41C19: ZZ_set_pylong(NTL::ZZ&, _object*) (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/devel/sage-main/c_lib/
libcsage.so)
==21736==    by 0xCE24430: __pyx_f_py_9ntl_ZZ_pE_9ntl_ZZ_pE___init__(_object*, _object*, _object*) (ntl_ZZ_pE.cpp:1383)
==21736==    by 0x459220: type_call (typeobject.c:436)
==21736==    by 0x415522: PyObject_Call (abstract.c:1860)
==21736==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)
==21736==    by 0xCD17DFA: __pyx_f_py_16ntl_ZZ_pEContext_22ntl_ZZ_pEContext_class_ZZ_pE(_object*, _object*, _object*) (ntl_Z
Z_pEContext.cpp:726)
==21736==    by 0x483031: PyEval_EvalFrameEx (ceval.c:3564)
==21736==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==21736==    by 0x483CC4: PyEval_EvalFrameEx (ceval.c:494)

==21736== 32 bytes in 1 blocks are indirectly lost in loss record 109 of 1,880
==21736==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)
==21736==    by 0x6179D59: _ntl_gblock_construct_alloc (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/local/lib/libntl.so)
==21736==    by 0x61D9EB2: NTL::BlockConstruct(NTL::ZZ_p*, long) (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/local/lib/libntl.s
o)
==21736==    by 0x61DA0CB: NTL::vec_ZZ_p::SetLength(long) (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/local/lib/libntl.so)
==21736==    by 0x61DA881: NTL::vec_ZZ_p::operator=(NTL::vec_ZZ_p const&) (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/local/lib
/libntl.so)
==21736==    by 0x5C46805: NTL::vec_ZZ_p::vec_ZZ_p(NTL::vec_ZZ_p const&) (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/devel/sage
-main/c_lib/libcsage.so)
==21736==    by 0x5C46824: NTL::ZZ_pX::ZZ_pX(NTL::ZZ_pX const&) (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/devel/sage-main/c_l
ib/libcsage.so)
==21736==    by 0x5C42DEA: ZZ_pE_to_ZZ_pX (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/devel/sage-main/c_lib/libcsage.so)
==21736==    by 0xCE22EA7: __pyx_f_9ntl_ZZ_pE_9ntl_ZZ_pE_get_as_ZZ_pX(__pyx_obj_9ntl_ZZ_pE_ntl_ZZ_pE*) (ntl_ZZ_pE.cpp:2705)
==21736==    by 0xCE2110E: __pyx_f_py_9ntl_ZZ_pE_9ntl_ZZ_pE___reduce__(_object*, _object*) (ntl_ZZ_pE.cpp:1753)
==21736==    by 0x415522: PyObject_Call (abstract.c:1860)
==21736==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)

==21736== 64 bytes in 1 blocks are indirectly lost in loss record 217 of 1,880
==21736==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)
==21736==    by 0x61DA129: NTL::vec_ZZ_p::SetLength(long) (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/local/lib/libntl.so)
==21736==    by 0x61DA881: NTL::vec_ZZ_p::operator=(NTL::vec_ZZ_p const&) (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/local/lib
/libntl.so)
==21736==    by 0x5C46805: NTL::vec_ZZ_p::vec_ZZ_p(NTL::vec_ZZ_p const&) (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/devel/sage
-main/c_lib/libcsage.so)
==21736==    by 0x5C46824: NTL::ZZ_pX::ZZ_pX(NTL::ZZ_pX const&) (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/devel/sage-main/c_l
ib/libcsage.so)
==21736==    by 0x5C42DEA: ZZ_pE_to_ZZ_pX (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/devel/sage-main/c_lib/libcsage.so)
==21736==    by 0xCE22EA7: __pyx_f_9ntl_ZZ_pE_9ntl_ZZ_pE_get_as_ZZ_pX(__pyx_obj_9ntl_ZZ_pE_ntl_ZZ_pE*) (ntl_ZZ_pE.cpp:2705)
==21736==    by 0xCE2110E: __pyx_f_py_9ntl_ZZ_pE_9ntl_ZZ_pE___reduce__(_object*, _object*) (ntl_ZZ_pE.cpp:1753)
==21736==    by 0x415522: PyObject_Call (abstract.c:1860)
==21736==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)
==21736==    by 0x4589BF: object_reduce_ex (typeobject.c:2786)
==21736==    by 0x415522: PyObject_Call (abstract.c:1860)

==21736== 64 bytes in 1 blocks are indirectly lost in loss record 220 of 1,880
==21736==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)
==21736==    by 0x6179D59: _ntl_gblock_construct_alloc (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/local/lib/libntl.so)
==21736==    by 0x61D9EB2: NTL::BlockConstruct(NTL::ZZ_p*, long) (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/local/lib/libntl.s
o)
==21736==    by 0x61DA0CB: NTL::vec_ZZ_p::SetLength(long) (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/local/lib/libntl.so)
==21736==    by 0x61DA881: NTL::vec_ZZ_p::operator=(NTL::vec_ZZ_p const&) (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/local/lib
/libntl.so)
==21736==    by 0x5C46805: NTL::vec_ZZ_p::vec_ZZ_p(NTL::vec_ZZ_p const&) (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/devel/sage
-main/c_lib/libcsage.so)
==21736==    by 0x5C46824: NTL::ZZ_pX::ZZ_pX(NTL::ZZ_pX const&) (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/devel/sage-main/c_l
ib/libcsage.so)
==21736==    by 0x5C42DEA: ZZ_pE_to_ZZ_pX (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/devel/sage-main/c_lib/libcsage.so)
==21736==    by 0xCE22EA7: __pyx_f_9ntl_ZZ_pE_9ntl_ZZ_pE_get_as_ZZ_pX(__pyx_obj_9ntl_ZZ_pE_ntl_ZZ_pE*) (ntl_ZZ_pE.cpp:2705)
==21736==    by 0xCE20569: __pyx_f_py_9ntl_ZZ_pE_9ntl_ZZ_pE_get_as_ZZ_pX_doctest(_object*, _object*) (ntl_ZZ_pE.cpp:2753)
==21736==    by 0x482FE8: PyEval_EvalFrameEx (ceval.c:3548)
==21736==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)

==21736== 64 bytes in 1 blocks are indirectly lost in loss record 221 of 1,880
==21736==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)
==21736==    by 0x61DA129: NTL::vec_ZZ_p::SetLength(long) (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/local/lib/libntl.so)
==21736==    by 0x61DA881: NTL::vec_ZZ_p::operator=(NTL::vec_ZZ_p const&) (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/local/lib
/libntl.so)
==21736==    by 0x5C46805: NTL::vec_ZZ_p::vec_ZZ_p(NTL::vec_ZZ_p const&) (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/devel/sage
-main/c_lib/libcsage.so)
==21736==    by 0x5C46824: NTL::ZZ_pX::ZZ_pX(NTL::ZZ_pX const&) (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/devel/sage-main/c_l
ib/libcsage.so)
==21736==    by 0x5C42DEA: ZZ_pE_to_ZZ_pX (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/devel/sage-main/c_lib/libcsage.so)
==21736==    by 0xCE22EA7: __pyx_f_9ntl_ZZ_pE_9ntl_ZZ_pE_get_as_ZZ_pX(__pyx_obj_9ntl_ZZ_pE_ntl_ZZ_pE*) (ntl_ZZ_pE.cpp:2705)
==21736==    by 0xCE20569: __pyx_f_py_9ntl_ZZ_pE_9ntl_ZZ_pE_get_as_ZZ_pX_doctest(_object*, _object*) (ntl_ZZ_pE.cpp:2753)
==21736==    by 0x482FE8: PyEval_EvalFrameEx (ceval.c:3548)
==21736==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==21736==    by 0x483CC4: PyEval_EvalFrameEx (ceval.c:494)
==21736==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:283

==21736== 136 (8 direct, 128 indirect) bytes in 1 blocks are definitely lost in loss record 257 of 1,880
==21736==    at 0x4A1C344: operator new(unsigned long) (vg_replace_malloc.c:227)
==21736==    by 0x5C42DDA: ZZ_pE_to_ZZ_pX (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/devel/sage-main/c_lib/libcsage.so)
==21736==    by 0xCE22EA7: __pyx_f_9ntl_ZZ_pE_9ntl_ZZ_pE_get_as_ZZ_pX(__pyx_obj_9ntl_ZZ_pE_ntl_ZZ_pE*) (ntl_ZZ_pE.cpp:2705)
==21736==    by 0xCE20569: __pyx_f_py_9ntl_ZZ_pE_9ntl_ZZ_pE_get_as_ZZ_pX_doctest(_object*, _object*) (ntl_ZZ_pE.cpp:2753)
==21736==    by 0x482FE8: PyEval_EvalFrameEx (ceval.c:3548)
==21736==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==21736==    by 0x483CC4: PyEval_EvalFrameEx (ceval.c:494)
==21736==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==21736==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)
==21736==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==21736==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)
==21736==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
```

From doctest_ntl_mat_ZZ.py:

```
==21903== 10 bytes in 1 blocks are definitely lost in loss record 28 of 1,874
==21903==    at 0x4A1BFE4: operator new[](unsigned long) (vg_replace_malloc.c:271)
==21903==    by 0x60454B5: ZZX_repr (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/devel/sage-main/c_lib/libcsage.so)
==21903==    by 0xCAE53A6: __pyx_f_py_7ntl_ZZX_7ntl_ZZX___repr__(_object*) (ntl_ZZX.cpp:1483)
==21903==    by 0x442FF9: PyObject_Repr (object.c:361)
==21903==    by 0x429B3B: PyFile_WriteObject (fileobject.c:2196)
==21903==    by 0x4AC158: sys_displayhook (sysmodule.c:114)
==21903==    by 0x415522: PyObject_Call (abstract.c:1860)
==21903==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)
==21903==    by 0x4827EE: PyEval_EvalFrameEx (ceval.c:1530)
==21903==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==21903==    by 0x483CC4: PyEval_EvalFrameEx (ceval.c:494)
==21903==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
```

From doctest_ntl_ZZ_pEX.py:

```
==21921== 408 (24 direct, 384 indirect) bytes in 3 blocks are definitely lost in loss record 404 of 1,859
==21921==    at 0x4A1C344: operator new(unsigned long) (vg_replace_malloc.c:227)
==21921==    by 0x6042DDA: ZZ_pE_to_ZZ_pX (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/devel/sage-main/c_lib/libcsage.so)
==21921==    by 0xCE22EA7: __pyx_f_9ntl_ZZ_pE_9ntl_ZZ_pE_get_as_ZZ_pX(__pyx_obj_9ntl_ZZ_pE_ntl_ZZ_pE*) (ntl_ZZ_pE.cpp:2705)
==21921==    by 0xCE2110E: __pyx_f_py_9ntl_ZZ_pE_9ntl_ZZ_pE___reduce__(_object*, _object*) (ntl_ZZ_pE.cpp:1753)
==21921==    by 0x415522: PyObject_Call (abstract.c:1860)
==21921==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)
==21921==    by 0x4589BF: object_reduce_ex (typeobject.c:2786)
==21921==    by 0x415522: PyObject_Call (abstract.c:1860)
==21921==    by 0x76EA743: save (cPickle.c:2495)
==21921==    by 0x76EBEEC: batch_list (cPickle.c:1558)
==21921==    by 0x76EAC7B: save (cPickle.c:1626)
==21921==    by 0x76EA25F: save_tuple (cPickle.c:1381)
```

From doctest_ntl_ZZX.py:

```
==21981== 8 bytes in 1 blocks are definitely lost in loss record 17 of 1,854
==21981==    at 0x4A1C344: operator new(unsigned long) (vg_replace_malloc.c:227)
==21981==    by 0x6045378: ZZX_div (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/devel/sage-main/c_lib/libcsage.so)
==21981==    by 0xCAE97D9: __pyx_f_py_7ntl_ZZX_7ntl_ZZX___div__(_object*, _object*) (ntl_ZZX.cpp:2388)
==21981==    by 0x4157EC: binary_op1 (abstract.c:398)
==21981==    by 0x416DDD: PyNumber_Divide (abstract.c:450)
==21981==    by 0x47F911: PyEval_EvalFrameEx (ceval.c:1083)
==21981==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==21981==    by 0x483CC4: PyEval_EvalFrameEx (ceval.c:494)
==21981==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==21981==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)
==21981==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==21981==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)

==21981== 10 bytes in 1 blocks are definitely lost in loss record 29 of 1,854
==21981==    at 0x4A1BFE4: operator new[](unsigned long) (vg_replace_malloc.c:271)
==21981==    by 0x60454B5: ZZX_repr (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/devel/sage-main/c_lib/libcsage.so)
==21981==    by 0xCAE53A6: __pyx_f_py_7ntl_ZZX_7ntl_ZZX___repr__(_object*) (ntl_ZZX.cpp:1483)
==21981==    by 0x482FE8: PyEval_EvalFrameEx (ceval.c:3548)
==21981==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==21981==    by 0x483CC4: PyEval_EvalFrameEx (ceval.c:494)
==21981==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==21981==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)
==21981==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==21981==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)
==21981==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==21981==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)
```

From doctest_ntl_GF2E.py:

```
==22056== 8 bytes in 1 blocks are definitely lost in loss record 32 of 1,987
==22056==    at 0x4A1C344: operator new(unsigned long) (vg_replace_malloc.c:227)
==22056==    by 0xFC7F3D6: Poly1FactorDom<GFqDom<int>, Dense, GivRandom>::is_prim_root(givvector<int> const&, givvector<int>
 const&) const (givpoly1proot.inl:236)
==22056==    by 0xFC80CB6: GFqDom<int>::GFqDom(unsigned, unsigned, std::vector<unsigned, std::allocator<unsigned> > const&)
(givpoly1proot.inl:300)
==22056==    by 0xFC733DF: __pyx_f_py_19finite_field_givaro_18FiniteField_givaro___init__(_object*, _object*, _object*) (fin
ite_field_givaro.cpp:1847)
==22056==    by 0x459220: type_call (typeobject.c:436)
==22056==    by 0x415522: PyObject_Call (abstract.c:1860)
==22056==    by 0x481ACA: PyEval_EvalFrameEx (ceval.c:3844)
==22056==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==22056==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)
==22056==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==22056==    by 0x483CC4: PyEval_EvalFrameEx (ceval.c:494)
==22056==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
```

From doctest_ntl_ZZ_p.py:

```
==22060== 16 bytes in 1 blocks are definitely lost in loss record 72 of 1,859
==22060==    at 0x4A1BC36: realloc (vg_replace_malloc.c:420)
==22060==    by 0x5D68E30: __gmpz_realloc (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/local/lib/libgmp.so.3.4.1)
==22060==    by 0x5C416CA: mpz_set_pylong (mpz_pylong.c:74)
==22060==    by 0x5C41C19: ZZ_set_pylong(NTL::ZZ&, _object*) (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/devel/sage-main/c_lib/
libcsage.so)
==22060==    by 0xC9D6520: __pyx_f_py_8ntl_ZZ_p_8ntl_ZZ_p___init__(_object*, _object*, _object*) (ntl_ZZ_p.cpp:1190)
==22060==    by 0x459220: type_call (typeobject.c:436)
==22060==    by 0x415522: PyObject_Call (abstract.c:1860)
==22060==    by 0x481E91: PyEval_EvalFrameEx (ceval.c:3775)
==22060==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==22060==    by 0x483CC4: PyEval_EvalFrameEx (ceval.c:494)
==22060==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==22060==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)
```

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/894





---

archive/issue_comments_005484.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-18T11:04:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/894",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/894#issuecomment-5484",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_events_002475.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-21T03:34:21Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/894",
    "milestone": "sage-2.8.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/894#event-2475"
}
```



---

archive/issue_events_002476.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-10-25T01:09:29Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/894",
    "milestone": "sage-2.8.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/894#event-2476"
}
```



---

archive/issue_events_002477.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-10-25T01:09:29Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/894",
    "milestone": "sage-2.8.10",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/894#event-2477"
}
```



---

archive/issue_comments_005485.json:
```json
{
    "body": "I'm attaching a patch that fixes about half or more of the memory leaks above (many of them are now irrelevant due to a rewrite of the GF(2)-stuff by malb). I think we should close this ticket and wait until mabshoff valgrinds the directory again to open more to fix. Also, these aren't super-high priority: any \"production\" code that uses parts of NTL in a serious way should often be using NTL directly, not going through the wrapper (for speed).",
    "created_at": "2007-11-03T18:14:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/894",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/894#issuecomment-5485",
    "user": "https://github.com/craigcitro"
}
```

I'm attaching a patch that fixes about half or more of the memory leaks above (many of them are now irrelevant due to a rewrite of the GF(2)-stuff by malb). I think we should close this ticket and wait until mabshoff valgrinds the directory again to open more to fix. Also, these aren't super-high priority: any "production" code that uses parts of NTL in a serious way should often be using NTL directly, not going through the wrapper (for speed).



---

archive/issue_events_002478.json:
```json
{
    "actor": "https://github.com/craigcitro",
    "created_at": "2007-11-03T18:14:14Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/894",
    "milestone": "sage-2.8.10",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/894#event-2478"
}
```



---

archive/issue_events_002479.json:
```json
{
    "actor": "https://github.com/craigcitro",
    "created_at": "2007-11-03T18:14:14Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/894",
    "milestone": "sage-2.8.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/894#event-2479"
}
```



---

archive/issue_comments_005486.json:
```json
{
    "body": "Changing assignee from mabshoff to @craigcitro.",
    "created_at": "2007-11-03T18:44:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/894",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/894#issuecomment-5486",
    "user": "https://github.com/craigcitro"
}
```

Changing assignee from mabshoff to @craigcitro.



---

archive/issue_comments_005487.json:
```json
{
    "body": "Changing status from assigned to new.",
    "created_at": "2007-11-03T18:44:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/894",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/894#issuecomment-5487",
    "user": "https://github.com/craigcitro"
}
```

Changing status from assigned to new.



---

archive/issue_comments_005488.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-11-03T18:44:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/894",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/894#issuecomment-5488",
    "user": "https://github.com/craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_005489.json:
```json
{
    "body": "Attachment [trac_894.hg](tarball://root/attachments/some-uuid/ticket894/trac_894.hg) by @craigcitro created at 2007-11-03 20:13:59",
    "created_at": "2007-11-03T20:13:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/894",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/894#issuecomment-5489",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac_894.hg](tarball://root/attachments/some-uuid/ticket894/trac_894.hg) by @craigcitro created at 2007-11-03 20:13:59



---

archive/issue_comments_005490.json:
```json
{
    "body": "Previous version of this patch didn't actually work. This should work fine. I didn't sage -testall, but sage -t * in sage/libs/ntl works fine; this is fairly reassuring, since that directory has 100% doctest coverage.",
    "created_at": "2007-11-03T20:15:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/894",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/894#issuecomment-5490",
    "user": "https://github.com/craigcitro"
}
```

Previous version of this patch didn't actually work. This should work fine. I didn't sage -testall, but sage -t * in sage/libs/ntl works fine; this is fairly reassuring, since that directory has 100% doctest coverage.



---

archive/issue_events_002480.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-11-03T21:07:46Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/894",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/894#event-2480"
}
```



---

archive/issue_comments_005491.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-03T21:07:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/894",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/894#issuecomment-5491",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
