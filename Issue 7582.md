# Issue 7582: Segfault in variety() over cyclotomicfield

archive/issues_007582.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCC:  malb wjp\n\nKeywords: variety\n\nI ran into a segfault on OS X 10.6, but I tried it on sagenb.org as well (see http://sagenb.org:8888/home/pub/1195/ ) and it seems to be a problem there too though it doesn't print an error like it does locally.\n\nI have included a backtrace from my machine in case it's different due to OS X 10.6.\n\nsage: R.<x,y,z> = PolynomialRing(CyclotomicField(2),3)\nsage: I=R*(x+y+z)\nsage: I.variety()\nverbose 0 (952: multi_polynomial_ideal.py, dimension) Warning: falling back to very slow toy implementation.\n\nProgram received signal EXC_BAD_ACCESS, Could not access memory.\nReason: KERN_INVALID_ADDRESS at address: 0x0000000000000005\n0x000000010624ccd0 in naIsZero () at omInline.h:30\n30      omInline.h: No such file or directory.\n        in omInline.h\n(gdb) bt\n#0  0x000000010624ccd0 in naIsZero () at omInline.h:30\n#1  0x000000010628134f in p_NSet () at omInline.h:30\n#2  0x00000001060d6557 in __pyx_f_4sage_5rings_10polynomial_28multi_polynomial_libsingular_27MPolynomialRing_libsingular__coerce_c_impl (__pyx_v_self=0x10c30d190, __pyx_v_element=0x10582b390) at sage/rings/polynomial/multi_polynomial_libsingular.cpp:4869\n#3  0x0000000101dc8a5c in __pyx_f_4sage_9structure_10parent_old_6Parent__coerce_c (__pyx_v_self=<value temporarily unavailable, due to optimizations>, __pyx_v_x=0x10582b390, __pyx_skip_dispatch=<value temporarily unavailable, due to optimizations>) at sage/structure/parent_old.c:3456\n#4  0x0000000101dc5c53 in __pyx_f_4sage_9structure_10parent_old_6Parent_has_coerce_map_from_c_impl (__pyx_v_self=0x10c30d190, __pyx_v_S=0x101ce0970) at sage/structure/parent_old.c:4583\n#5  0x0000000101dc69bc in __pyx_f_4sage_9structure_10parent_old_6Parent_has_coerce_map_from_c (__pyx_v_self=0x10c30d190, __pyx_v_S=0x101ce0970, __pyx_skip_dispatch=<value temporarily unavailable, due to optimizations>) at sage/structure/parent_old.c:4368\n#6  0x0000000101dc2b5a in __pyx_f_4sage_9structure_10parent_old_6Parent_coerce_map_from_c_impl (__pyx_v_self=0x10c30d190, __pyx_v_S=0x101ce0970) at sage/structure/parent_old.c:2436\n#7  0x0000000101dc0274 in __pyx_f_4sage_9structure_10parent_old_6Parent_coerce_map_from_c (__pyx_v_self=<value temporarily unavailable, due to optimizations>, __pyx_v_S=0x101ce0970, __pyx_skip_dispatch=<value temporarily unavailable, due to optimizations>) at sage/structure/parent_old.c:1725\n#8  0x0000000101dc0086 in __pyx_f_4sage_9structure_10parent_old_6Parent_coerce_map_from_c (__pyx_v_self=0x10c30d190, __pyx_v_S=0x100157900, __pyx_skip_dispatch=<value temporarily unavailable, due to optimizations>) at sage/structure/parent_old.c:1914\n#9  0x0000000101dba792 in __pyx_f_4sage_9structure_10parent_old_6Parent__coerce_map_from_ (__pyx_v_self=0x10c30d190, __pyx_v_S=0x100157900, __pyx_skip_dispatch=<value temporarily unavailable, due to optimizations>) at sage/structure/parent_old.c:5841\n#10 0x0000000101de77ae in __pyx_f_4sage_9structure_6parent_6Parent_discover_coerce_map_from (__pyx_v_self=0x10c30d190, __pyx_v_S=0x100157900) at sage/structure/parent.c:9948\n#11 0x0000000101dfa47e in __pyx_f_4sage_9structure_6parent_6Parent_coerce_map_from (__pyx_v_self=0x10c30d190, __pyx_v_S=0x100157900, __pyx_skip_dispatch=<value temporarily unavailable, due to optimizations>) at sage/structure/parent.c:9550\n#12 0x0000000101f0997e in __pyx_f_4sage_9structure_6coerce_24CoercionModel_cache_maps_discover_coercion (__pyx_v_self=0x101d95530, __pyx_v_R=0x10c30d190, __pyx_v_S=0x100157900, __pyx_skip_dispatch=<value temporarily unavailable, due to optimizations>) at sage/structure/coerce.c:10385\n#13 0x0000000101f0b45f in __pyx_f_4sage_9structure_6coerce_24CoercionModel_cache_maps_coercion_maps (__pyx_v_self=0x101d95530, __pyx_v_R=0x10c30d190, __pyx_v_S=0x100157900, __pyx_skip_dispatch=<value temporarily unavailable, due to optimizations>) at sage/structure/coerce.c:8893\n#14 0x0000000101f1273c in __pyx_f_4sage_9structure_6coerce_24CoercionModel_cache_maps_canonical_coercion (__pyx_v_self=0x101d95530, __pyx_v_x=0x10c1f11b8, __pyx_v_y=0x100302840, __pyx_skip_dispatch=<value temporarily unavailable, due to optimizations>) at sage/structure/coerce.c:7278\n#15 0x0000000101e9a883 in __pyx_f_4sage_9structure_7element_7Element__richcmp (__pyx_v_left=0x10c1f11b8, __pyx_v_right=0x100302840, __pyx_v_op=3) at sage/structure/element.c:5848\n#16 0x0000000106097a2b in __pyx_pf_4sage_5rings_10polynomial_28multi_polynomial_libsingular_23MPolynomial_libsingular___richcmp__ (__pyx_v_left=<value temporarily unavailable, due to optimizations>, __pyx_v_right=<value temporarily unavailable, due to optimizations>, __pyx_v_op=<value temporarily unavailable, due to optimizations>) at sage/rings/polynomial/multi_polynomial_libsingular.cpp:13679\n#17 0x000000010004dacc in try_rich_compare ()\n#18 0x000000010004f46f in PyObject_RichCompare ()\n#19 0x00000001000b20d0 in PyEval_EvalFrameEx ()\n#20 0x00000001000b601d in PyEval_EvalFrameEx ()\n#21 0x00000001000b601d in PyEval_EvalFrameEx ()\n#22 0x00000001000b6bd2 in PyEval_EvalCodeEx ()\n#23 0x00000001000361cd in function_call ()\n#24 0x00000001000073d2 in PyObject_Call ()\n#25 0x00000001000b123e in PyEval_EvalFrameEx ()\n#26 0x00000001000b6bd2 in PyEval_EvalCodeEx ()\n#27 0x00000001000360c5 in function_call ()\n#28 0x00000001000073d2 in PyObject_Call ()\n#29 0x000000010001816b in instancemethod_call ()\n#30 0x00000001000073d2 in PyObject_Call ()\n#31 0x000000010006f24a in slot_tp_call ()\n#32 0x00000001000073d2 in PyObject_Call ()\n#33 0x00000001000b23a8 in PyEval_EvalFrameEx ()\n#34 0x00000001000b6bd2 in PyEval_EvalCodeEx ()\n#35 0x00000001000361cd in function_call ()\n#36 0x00000001000073d2 in PyObject_Call ()\n#37 0x00000001000b123e in PyEval_EvalFrameEx ()\n#38 0x00000001000b6bd2 in PyEval_EvalCodeEx ()\n#39 0x00000001000360c5 in function_call ()\n#40 0x00000001000073d2 in PyObject_Call ()\n#41 0x000000010001816b in instancemethod_call ()\n#42 0x00000001000073d2 in PyObject_Call ()\n#43 0x000000010006f24a in slot_tp_call ()\n#44 0x00000001000073d2 in PyObject_Call ()\n#45 0x00000001000b23a8 in PyEval_EvalFrameEx ()\n#46 0x00000001000b6bd2 in PyEval_EvalCodeEx ()\n#47 0x00000001000b4fa0 in PyEval_EvalFrameEx ()\n#48 0x00000001000b6bd2 in PyEval_EvalCodeEx ()\n#49 0x00000001000b476e in PyEval_EvalFrameEx ()\n#50 0x00000001000b6bd2 in PyEval_EvalCodeEx ()\n#51 0x00000001000b476e in PyEval_EvalFrameEx ()\n#52 0x00000001000b601d in PyEval_EvalFrameEx ()\n#53 0x00000001000b6bd2 in PyEval_EvalCodeEx ()\n#54 0x00000001000b476e in PyEval_EvalFrameEx ()\n#55 0x00000001000b6bd2 in PyEval_EvalCodeEx ()\n#56 0x00000001000b476e in PyEval_EvalFrameEx ()\n#57 0x00000001000b6bd2 in PyEval_EvalCodeEx ()\n#58 0x00000001000b476e in PyEval_EvalFrameEx ()\n#59 0x00000001000b6bd2 in PyEval_EvalCodeEx ()\n#60 0x00000001000b6cb6 in PyEval_EvalCode ()\n#61 0x00000001000dbe5e in PyRun_FileExFlags ()\n#62 0x00000001000dc119 in PyRun_SimpleFileExFlags ()\n#63 0x00000001000e951b in Py_Main ()\n#64 0x0000000100001622 in _start ()\n#65 0x0000000100001541 in start ()\n(gdb)\n\nIssue created by migration from https://trac.sagemath.org/ticket/7582\n\n",
    "created_at": "2009-12-02T12:23:01Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "Segfault in variety() over cyclotomicfield",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7582",
    "user": "iandrus"
}
```
Assignee: AlexGhitza

CC:  malb wjp

Keywords: variety

I ran into a segfault on OS X 10.6, but I tried it on sagenb.org as well (see http://sagenb.org:8888/home/pub/1195/ ) and it seems to be a problem there too though it doesn't print an error like it does locally.

I have included a backtrace from my machine in case it's different due to OS X 10.6.

sage: R.<x,y,z> = PolynomialRing(CyclotomicField(2),3)
sage: I=R*(x+y+z)
sage: I.variety()
verbose 0 (952: multi_polynomial_ideal.py, dimension) Warning: falling back to very slow toy implementation.

Program received signal EXC_BAD_ACCESS, Could not access memory.
Reason: KERN_INVALID_ADDRESS at address: 0x0000000000000005
0x000000010624ccd0 in naIsZero () at omInline.h:30
30      omInline.h: No such file or directory.
        in omInline.h
(gdb) bt
#0  0x000000010624ccd0 in naIsZero () at omInline.h:30
#1  0x000000010628134f in p_NSet () at omInline.h:30
#2  0x00000001060d6557 in __pyx_f_4sage_5rings_10polynomial_28multi_polynomial_libsingular_27MPolynomialRing_libsingular__coerce_c_impl (__pyx_v_self=0x10c30d190, __pyx_v_element=0x10582b390) at sage/rings/polynomial/multi_polynomial_libsingular.cpp:4869
#3  0x0000000101dc8a5c in __pyx_f_4sage_9structure_10parent_old_6Parent__coerce_c (__pyx_v_self=<value temporarily unavailable, due to optimizations>, __pyx_v_x=0x10582b390, __pyx_skip_dispatch=<value temporarily unavailable, due to optimizations>) at sage/structure/parent_old.c:3456
#4  0x0000000101dc5c53 in __pyx_f_4sage_9structure_10parent_old_6Parent_has_coerce_map_from_c_impl (__pyx_v_self=0x10c30d190, __pyx_v_S=0x101ce0970) at sage/structure/parent_old.c:4583
#5  0x0000000101dc69bc in __pyx_f_4sage_9structure_10parent_old_6Parent_has_coerce_map_from_c (__pyx_v_self=0x10c30d190, __pyx_v_S=0x101ce0970, __pyx_skip_dispatch=<value temporarily unavailable, due to optimizations>) at sage/structure/parent_old.c:4368
#6  0x0000000101dc2b5a in __pyx_f_4sage_9structure_10parent_old_6Parent_coerce_map_from_c_impl (__pyx_v_self=0x10c30d190, __pyx_v_S=0x101ce0970) at sage/structure/parent_old.c:2436
#7  0x0000000101dc0274 in __pyx_f_4sage_9structure_10parent_old_6Parent_coerce_map_from_c (__pyx_v_self=<value temporarily unavailable, due to optimizations>, __pyx_v_S=0x101ce0970, __pyx_skip_dispatch=<value temporarily unavailable, due to optimizations>) at sage/structure/parent_old.c:1725
#8  0x0000000101dc0086 in __pyx_f_4sage_9structure_10parent_old_6Parent_coerce_map_from_c (__pyx_v_self=0x10c30d190, __pyx_v_S=0x100157900, __pyx_skip_dispatch=<value temporarily unavailable, due to optimizations>) at sage/structure/parent_old.c:1914
#9  0x0000000101dba792 in __pyx_f_4sage_9structure_10parent_old_6Parent__coerce_map_from_ (__pyx_v_self=0x10c30d190, __pyx_v_S=0x100157900, __pyx_skip_dispatch=<value temporarily unavailable, due to optimizations>) at sage/structure/parent_old.c:5841
#10 0x0000000101de77ae in __pyx_f_4sage_9structure_6parent_6Parent_discover_coerce_map_from (__pyx_v_self=0x10c30d190, __pyx_v_S=0x100157900) at sage/structure/parent.c:9948
#11 0x0000000101dfa47e in __pyx_f_4sage_9structure_6parent_6Parent_coerce_map_from (__pyx_v_self=0x10c30d190, __pyx_v_S=0x100157900, __pyx_skip_dispatch=<value temporarily unavailable, due to optimizations>) at sage/structure/parent.c:9550
#12 0x0000000101f0997e in __pyx_f_4sage_9structure_6coerce_24CoercionModel_cache_maps_discover_coercion (__pyx_v_self=0x101d95530, __pyx_v_R=0x10c30d190, __pyx_v_S=0x100157900, __pyx_skip_dispatch=<value temporarily unavailable, due to optimizations>) at sage/structure/coerce.c:10385
#13 0x0000000101f0b45f in __pyx_f_4sage_9structure_6coerce_24CoercionModel_cache_maps_coercion_maps (__pyx_v_self=0x101d95530, __pyx_v_R=0x10c30d190, __pyx_v_S=0x100157900, __pyx_skip_dispatch=<value temporarily unavailable, due to optimizations>) at sage/structure/coerce.c:8893
#14 0x0000000101f1273c in __pyx_f_4sage_9structure_6coerce_24CoercionModel_cache_maps_canonical_coercion (__pyx_v_self=0x101d95530, __pyx_v_x=0x10c1f11b8, __pyx_v_y=0x100302840, __pyx_skip_dispatch=<value temporarily unavailable, due to optimizations>) at sage/structure/coerce.c:7278
#15 0x0000000101e9a883 in __pyx_f_4sage_9structure_7element_7Element__richcmp (__pyx_v_left=0x10c1f11b8, __pyx_v_right=0x100302840, __pyx_v_op=3) at sage/structure/element.c:5848
#16 0x0000000106097a2b in __pyx_pf_4sage_5rings_10polynomial_28multi_polynomial_libsingular_23MPolynomial_libsingular___richcmp__ (__pyx_v_left=<value temporarily unavailable, due to optimizations>, __pyx_v_right=<value temporarily unavailable, due to optimizations>, __pyx_v_op=<value temporarily unavailable, due to optimizations>) at sage/rings/polynomial/multi_polynomial_libsingular.cpp:13679
#17 0x000000010004dacc in try_rich_compare ()
#18 0x000000010004f46f in PyObject_RichCompare ()
#19 0x00000001000b20d0 in PyEval_EvalFrameEx ()
#20 0x00000001000b601d in PyEval_EvalFrameEx ()
#21 0x00000001000b601d in PyEval_EvalFrameEx ()
#22 0x00000001000b6bd2 in PyEval_EvalCodeEx ()
#23 0x00000001000361cd in function_call ()
#24 0x00000001000073d2 in PyObject_Call ()
#25 0x00000001000b123e in PyEval_EvalFrameEx ()
#26 0x00000001000b6bd2 in PyEval_EvalCodeEx ()
#27 0x00000001000360c5 in function_call ()
#28 0x00000001000073d2 in PyObject_Call ()
#29 0x000000010001816b in instancemethod_call ()
#30 0x00000001000073d2 in PyObject_Call ()
#31 0x000000010006f24a in slot_tp_call ()
#32 0x00000001000073d2 in PyObject_Call ()
#33 0x00000001000b23a8 in PyEval_EvalFrameEx ()
#34 0x00000001000b6bd2 in PyEval_EvalCodeEx ()
#35 0x00000001000361cd in function_call ()
#36 0x00000001000073d2 in PyObject_Call ()
#37 0x00000001000b123e in PyEval_EvalFrameEx ()
#38 0x00000001000b6bd2 in PyEval_EvalCodeEx ()
#39 0x00000001000360c5 in function_call ()
#40 0x00000001000073d2 in PyObject_Call ()
#41 0x000000010001816b in instancemethod_call ()
#42 0x00000001000073d2 in PyObject_Call ()
#43 0x000000010006f24a in slot_tp_call ()
#44 0x00000001000073d2 in PyObject_Call ()
#45 0x00000001000b23a8 in PyEval_EvalFrameEx ()
#46 0x00000001000b6bd2 in PyEval_EvalCodeEx ()
#47 0x00000001000b4fa0 in PyEval_EvalFrameEx ()
#48 0x00000001000b6bd2 in PyEval_EvalCodeEx ()
#49 0x00000001000b476e in PyEval_EvalFrameEx ()
#50 0x00000001000b6bd2 in PyEval_EvalCodeEx ()
#51 0x00000001000b476e in PyEval_EvalFrameEx ()
#52 0x00000001000b601d in PyEval_EvalFrameEx ()
#53 0x00000001000b6bd2 in PyEval_EvalCodeEx ()
#54 0x00000001000b476e in PyEval_EvalFrameEx ()
#55 0x00000001000b6bd2 in PyEval_EvalCodeEx ()
#56 0x00000001000b476e in PyEval_EvalFrameEx ()
#57 0x00000001000b6bd2 in PyEval_EvalCodeEx ()
#58 0x00000001000b476e in PyEval_EvalFrameEx ()
#59 0x00000001000b6bd2 in PyEval_EvalCodeEx ()
#60 0x00000001000b6cb6 in PyEval_EvalCode ()
#61 0x00000001000dbe5e in PyRun_FileExFlags ()
#62 0x00000001000dc119 in PyRun_SimpleFileExFlags ()
#63 0x00000001000e951b in Py_Main ()
#64 0x0000000100001622 in _start ()
#65 0x0000000100001541 in start ()
(gdb)

Issue created by migration from https://trac.sagemath.org/ticket/7582





---

archive/issue_comments_064635.json:
```json
{
    "body": "Changing assignee from AlexGhitza to malb.",
    "created_at": "2009-12-02T19:06:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7582#issuecomment-64635",
    "user": "mhansen"
}
```

Changing assignee from AlexGhitza to malb.



---

archive/issue_comments_064636.json:
```json
{
    "body": "Changing keywords from \"variety\" to \"singular\".",
    "created_at": "2010-01-17T02:10:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7582#issuecomment-64636",
    "user": "burcin"
}
```

Changing keywords from "variety" to "singular".



---

archive/issue_comments_064637.json:
```json
{
    "body": "Changing component from algebraic geometry to commutative algebra.",
    "created_at": "2010-01-17T02:10:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7582#issuecomment-64637",
    "user": "burcin"
}
```

Changing component from algebraic geometry to commutative algebra.



---

archive/issue_comments_064638.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-17T02:10:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7582#issuecomment-64638",
    "user": "burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_064639.json:
```json
{
    "body": "attachment:trac_7582-libsingular_segfault.patch fixes this. The `sa2si_NF` method worked before only because the `list()` method on number field elements always returned a list padded with zeroes.\n\nThe variety computation in the given example still doesn't work, since we can only compute varieties for zero dimensional ideals and this one has dimension 2.",
    "created_at": "2010-01-17T02:10:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7582#issuecomment-64639",
    "user": "burcin"
}
```

attachment:trac_7582-libsingular_segfault.patch fixes this. The `sa2si_NF` method worked before only because the `list()` method on number field elements always returned a list padded with zeroes.

The variety computation in the given example still doesn't work, since we can only compute varieties for zero dimensional ideals and this one has dimension 2.



---

archive/issue_comments_064640.json:
```json
{
    "body": "fix segfault in coercion of integer to libsingular polynomial over number field",
    "created_at": "2010-01-17T02:19:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7582#issuecomment-64640",
    "user": "burcin"
}
```

fix segfault in coercion of integer to libsingular polynomial over number field



---

archive/issue_comments_064641.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-17T17:30:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7582#issuecomment-64641",
    "user": "wjp"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_064642.json:
```json
{
    "body": "Attachment [trac_7582-libsingular_segfault.patch](tarball://root/attachments/some-uuid/ticket7582/trac_7582-libsingular_segfault.patch) by wjp created at 2010-01-17 17:30:48\n\nLooks good.",
    "created_at": "2010-01-17T17:30:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7582#issuecomment-64642",
    "user": "wjp"
}
```

Attachment [trac_7582-libsingular_segfault.patch](tarball://root/attachments/some-uuid/ticket7582/trac_7582-libsingular_segfault.patch) by wjp created at 2010-01-17 17:30:48

Looks good.



---

archive/issue_comments_064643.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-18T23:51:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7582#issuecomment-64643",
    "user": "rlm"
}
```

Resolution: fixed
