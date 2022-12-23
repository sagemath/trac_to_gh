# Issue 519: memory leak: many states passed to gmp_randinit_mt are leaked (2.5kb each)

archive/issues_000519.json:
```json
{
    "body": "Assignee: was\n\nHello,\n\nwhen we initialize the Mersenne Twister random number generator in the gmp we pass a state. That state needs to be deallocated via gmp_randclear() - see http://gmplib.org/manual/Random-State-Initialization.html - otherwise we leak about 2.5kb.\n\nWe should audit the following places:\n\n```\nsage/build/sage/matrix/matrix_integer_dense.pyx:gmp_randinit_mt(state)\nsage/sage/matrix/matrix_rational_dense.c:  gmp_randinit_mt(__pyx_v_21matrix_rational_dense_state);\nsage/sage/matrix/matrix_modn_dense.c:  gmp_randinit_mt(__pyx_v_17matrix_modn_dense_state);\nsage/sage/matrix/matrix_integer_dense.pyx:gmp_randinit_mt(state)\nsage/sage/matrix/matrix_integer_dense.c:  gmp_randinit_mt(__pyx_v_20matrix_integer_dense_state);\nsage/sage/matrix/matrix_integer_dense.c:  gmp_randinit_mt(__pyx_v_20matrix_integer_dense_state);\nsage/sage/matrix/matrix_mod2_dense.c:  gmp_randinit_mt(__pyx_v_17matrix_mod2_dense_state);\nsage/sage/rings/integer_ring.c:  gmp_randinit_mt(__pyx_v_12integer_ring_state);\nsage/sage/rings/real_mpfr.c:  gmp_randinit_mt(__pyx_v_9real_mpfr_state);\nsage/sage/rings/real_double.c:  gmp_randinit_mt(__pyx_v_11real_double_state);\nsage-main/build/sage/matrix/matrix_integer_dense.pyx:gmp_randinit_mt(state)\nsage-main/sage/matrix/matrix_rational_dense.c:  gmp_randinit_mt(__pyx_v_21matrix_rational_dense_state);\nsage-main/sage/matrix/matrix_modn_dense.c:  gmp_randinit_mt(__pyx_v_17matrix_modn_dense_state);\nsage-main/sage/matrix/matrix_integer_dense.pyx:gmp_randinit_mt(state)\nsage-main/sage/matrix/matrix_integer_dense.c:  gmp_randinit_mt(__pyx_v_20matrix_integer_dense_state);\nsage-main/sage/matrix/matrix_integer_dense.c:  gmp_randinit_mt(__pyx_v_20matrix_integer_dense_state);\nsage-main/sage/matrix/matrix_mod2_dense.c:  gmp_randinit_mt(__pyx_v_17matrix_mod2_dense_state);\nsage-main/sage/rings/integer_ring.c:  gmp_randinit_mt(__pyx_v_12integer_ring_state);\nsage-main/sage/rings/real_mpfr.c:  gmp_randinit_mt(__pyx_v_9real_mpfr_state);\nsage-main/sage/rings/real_double.c:  gmp_randinit_mt(__pyx_v_11real_double_state);\n```\n\nTwo examples:\n\n```\n==11727== 2,500 bytes in 1 blocks are still reachable in loss record 2,024 of 2,401\n==11727==    at 0x4A05809: malloc (vg_replace_malloc.c:149)\n==11727==    by 0x9452A9C: __gmp_randinit_mt_noseed (in /tmp/Work2/sage-2.8.3.alpha2/local/lib/libgmp.so.3.4.1)\n==11727==    by 0x9452AE8: __gmp_randinit_mt (in /tmp/Work2/sage-2.8.3.alpha2/local/lib/libgmp.so.3.4.1)\n==11727==    by 0x2011A06C: initmatrix_integer_dense (matrix_integer_dense.c:18918)\n==11727==    by 0x49F762: _PyImport_LoadDynamicModule (importdl.c:53)\n==11727==    by 0x49D63E: import_submodule (import.c:2394)\n==11727==    by 0x49DB11: load_next (import.c:2214)\n==11727==    by 0x49DD33: import_module_level (import.c:1995)\n==11727==    by 0x49E1A4: PyImport_ImportModuleLevel (import.c:2066)\n==11727==    by 0x47D5D8: builtin___import__ (bltinmodule.c:47)\n==11727==    by 0x4156A2: PyObject_Call (abstract.c:1860)\n==11727==    by 0x47DB71: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==11727==\n==11727==\n==11727== 2,500 bytes in 1 blocks are still reachable in loss record 2,025 of 2,401\n==11727==    at 0x4A05809: malloc (vg_replace_malloc.c:149)\n==11727==    by 0x9452A9C: __gmp_randinit_mt_noseed (in /tmp/Work2/sage-2.8.3.alpha2/local/lib/libgmp.so.3.4.1)\n==11727==    by 0x9452AE8: __gmp_randinit_mt (in /tmp/Work2/sage-2.8.3.alpha2/local/lib/libgmp.so.3.4.1)\n==11727==    by 0x20118F53: initmatrix_integer_dense (matrix_integer_dense.c:18410)\n==11727==    by 0x49F762: _PyImport_LoadDynamicModule (importdl.c:53)\n==11727==    by 0x49D63E: import_submodule (import.c:2394)\n==11727==    by 0x49DB11: load_next (import.c:2214)\n==11727==    by 0x49DD33: import_module_level (import.c:1995)\n==11727==    by 0x49E1A4: PyImport_ImportModuleLevel (import.c:2066)\n==11727==    by 0x47D5D8: builtin___import__ (bltinmodule.c:47)\n==11727==    by 0x4156A2: PyObject_Call (abstract.c:1860)\n==11727==    by 0x47DB71: PyEval_CallObjectWithKeywords (ceval.c:3433)\n```\n\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/519\n\n",
    "created_at": "2007-08-29T22:01:34Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "title": "memory leak: many states passed to gmp_randinit_mt are leaked (2.5kb each)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/519",
    "user": "mabshoff"
}
```
Assignee: was

Hello,

when we initialize the Mersenne Twister random number generator in the gmp we pass a state. That state needs to be deallocated via gmp_randclear() - see http://gmplib.org/manual/Random-State-Initialization.html - otherwise we leak about 2.5kb.

We should audit the following places:

```
sage/build/sage/matrix/matrix_integer_dense.pyx:gmp_randinit_mt(state)
sage/sage/matrix/matrix_rational_dense.c:  gmp_randinit_mt(__pyx_v_21matrix_rational_dense_state);
sage/sage/matrix/matrix_modn_dense.c:  gmp_randinit_mt(__pyx_v_17matrix_modn_dense_state);
sage/sage/matrix/matrix_integer_dense.pyx:gmp_randinit_mt(state)
sage/sage/matrix/matrix_integer_dense.c:  gmp_randinit_mt(__pyx_v_20matrix_integer_dense_state);
sage/sage/matrix/matrix_integer_dense.c:  gmp_randinit_mt(__pyx_v_20matrix_integer_dense_state);
sage/sage/matrix/matrix_mod2_dense.c:  gmp_randinit_mt(__pyx_v_17matrix_mod2_dense_state);
sage/sage/rings/integer_ring.c:  gmp_randinit_mt(__pyx_v_12integer_ring_state);
sage/sage/rings/real_mpfr.c:  gmp_randinit_mt(__pyx_v_9real_mpfr_state);
sage/sage/rings/real_double.c:  gmp_randinit_mt(__pyx_v_11real_double_state);
sage-main/build/sage/matrix/matrix_integer_dense.pyx:gmp_randinit_mt(state)
sage-main/sage/matrix/matrix_rational_dense.c:  gmp_randinit_mt(__pyx_v_21matrix_rational_dense_state);
sage-main/sage/matrix/matrix_modn_dense.c:  gmp_randinit_mt(__pyx_v_17matrix_modn_dense_state);
sage-main/sage/matrix/matrix_integer_dense.pyx:gmp_randinit_mt(state)
sage-main/sage/matrix/matrix_integer_dense.c:  gmp_randinit_mt(__pyx_v_20matrix_integer_dense_state);
sage-main/sage/matrix/matrix_integer_dense.c:  gmp_randinit_mt(__pyx_v_20matrix_integer_dense_state);
sage-main/sage/matrix/matrix_mod2_dense.c:  gmp_randinit_mt(__pyx_v_17matrix_mod2_dense_state);
sage-main/sage/rings/integer_ring.c:  gmp_randinit_mt(__pyx_v_12integer_ring_state);
sage-main/sage/rings/real_mpfr.c:  gmp_randinit_mt(__pyx_v_9real_mpfr_state);
sage-main/sage/rings/real_double.c:  gmp_randinit_mt(__pyx_v_11real_double_state);
```

Two examples:

```
==11727== 2,500 bytes in 1 blocks are still reachable in loss record 2,024 of 2,401
==11727==    at 0x4A05809: malloc (vg_replace_malloc.c:149)
==11727==    by 0x9452A9C: __gmp_randinit_mt_noseed (in /tmp/Work2/sage-2.8.3.alpha2/local/lib/libgmp.so.3.4.1)
==11727==    by 0x9452AE8: __gmp_randinit_mt (in /tmp/Work2/sage-2.8.3.alpha2/local/lib/libgmp.so.3.4.1)
==11727==    by 0x2011A06C: initmatrix_integer_dense (matrix_integer_dense.c:18918)
==11727==    by 0x49F762: _PyImport_LoadDynamicModule (importdl.c:53)
==11727==    by 0x49D63E: import_submodule (import.c:2394)
==11727==    by 0x49DB11: load_next (import.c:2214)
==11727==    by 0x49DD33: import_module_level (import.c:1995)
==11727==    by 0x49E1A4: PyImport_ImportModuleLevel (import.c:2066)
==11727==    by 0x47D5D8: builtin___import__ (bltinmodule.c:47)
==11727==    by 0x4156A2: PyObject_Call (abstract.c:1860)
==11727==    by 0x47DB71: PyEval_CallObjectWithKeywords (ceval.c:3433)
==11727==
==11727==
==11727== 2,500 bytes in 1 blocks are still reachable in loss record 2,025 of 2,401
==11727==    at 0x4A05809: malloc (vg_replace_malloc.c:149)
==11727==    by 0x9452A9C: __gmp_randinit_mt_noseed (in /tmp/Work2/sage-2.8.3.alpha2/local/lib/libgmp.so.3.4.1)
==11727==    by 0x9452AE8: __gmp_randinit_mt (in /tmp/Work2/sage-2.8.3.alpha2/local/lib/libgmp.so.3.4.1)
==11727==    by 0x20118F53: initmatrix_integer_dense (matrix_integer_dense.c:18410)
==11727==    by 0x49F762: _PyImport_LoadDynamicModule (importdl.c:53)
==11727==    by 0x49D63E: import_submodule (import.c:2394)
==11727==    by 0x49DB11: load_next (import.c:2214)
==11727==    by 0x49DD33: import_module_level (import.c:1995)
==11727==    by 0x49E1A4: PyImport_ImportModuleLevel (import.c:2066)
==11727==    by 0x47D5D8: builtin___import__ (bltinmodule.c:47)
==11727==    by 0x4156A2: PyObject_Call (abstract.c:1860)
==11727==    by 0x47DB71: PyEval_CallObjectWithKeywords (ceval.c:3433)
```


Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/519





---

archive/issue_comments_002626.json:
```json
{
    "body": "Changing assignee from was to mabshoff.",
    "created_at": "2007-08-30T10:41:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/519#issuecomment-2626",
    "user": "mabshoff"
}
```

Changing assignee from was to mabshoff.



---

archive/issue_comments_002627.json:
```json
{
    "body": "Changing component from algebraic geometry to memleak.",
    "created_at": "2007-08-30T10:41:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/519#issuecomment-2627",
    "user": "mabshoff"
}
```

Changing component from algebraic geometry to memleak.



---

archive/issue_comments_002628.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-09-02T00:54:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/519#issuecomment-2628",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_002629.json:
```json
{
    "body": "\n```\n[01:37] <mabshoff> So do you think that the rand_init_mt() should also be moved to sagelib.c?\n[01:37] <mabshoff> And have its own cleanup routine to be called from\n[01:52] <sage> yep.\n[01:52] <sage> also moving rand_init_mt to libcsage makes sense, I think.\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2007-09-03T00:09:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/519#issuecomment-2629",
    "user": "mabshoff"
}
```


```
[01:37] <mabshoff> So do you think that the rand_init_mt() should also be moved to sagelib.c?
[01:37] <mabshoff> And have its own cleanup routine to be called from
[01:52] <sage> yep.
[01:52] <sage> also moving rand_init_mt to libcsage makes sense, I think.
```


Cheers,

Michael



---

archive/issue_comments_002630.json:
```json
{
    "body": "I believe this can be closed. The only problem left is \"sage/matrix/matrix_integer_dense.pyx has own private gmp_randinit_mt()\" - see\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/5fe050ae9a2dc373/\n\nCheers,\n\nMichael",
    "created_at": "2007-09-13T10:33:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/519#issuecomment-2630",
    "user": "mabshoff"
}
```

I believe this can be closed. The only problem left is "sage/matrix/matrix_integer_dense.pyx has own private gmp_randinit_mt()" - see

http://groups.google.com/group/sage-devel/browse_thread/thread/5fe050ae9a2dc373/

Cheers,

Michael



---

archive/issue_comments_002631.json:
```json
{
    "body": "I will close this ticket since malb's patch fixed this, but I will open another ticket for that leak.\n\nCheers,\n\nMichael",
    "created_at": "2007-09-13T15:57:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/519#issuecomment-2631",
    "user": "mabshoff"
}
```

I will close this ticket since malb's patch fixed this, but I will open another ticket for that leak.

Cheers,

Michael



---

archive/issue_comments_002632.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-13T15:57:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/519#issuecomment-2632",
    "user": "mabshoff"
}
```

Resolution: fixed
