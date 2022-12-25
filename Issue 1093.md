# Issue 1093: small memleaks exposed by ntl_ZZ_pX.py (from 2.8.12.alpha0)

archive/issues_001093.json:
```json
{
    "body": "Assignee: mabshoff\n\nntl_ZZ_pX.py\n\n```\n==4504== 504 (72 direct, 432 indirect) bytes in 9 blocks are definitely lost in loss record 305 of 1,918\n==4504==    at 0x4A1C344: operator new(unsigned long) (vg_replace_malloc.c:227)\n==4504==    by 0x6041C2A: ZZ_pX_linear_roots (in /tmp/Work-mabshoff/sage-2.8.11/devel/sage-main/c_lib/libcsage.so)\n==4504==    by 0xCC4DB97: __pyx_pf_4sage_4libs_3ntl_9ntl_ZZ_pX_9ntl_ZZ_pX_linear_roots(_object*, _object*) (ntl_ZZ_pX.cpp:35\n95)\n==4504==    by 0x482FE8: PyEval_EvalFrameEx (ceval.c:3548)\n==4504==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n==4504==    by 0x483CC4: PyEval_EvalFrameEx (ceval.c:494)\n==4504==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n==4504==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)\n==4504==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n==4504==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)\n==4504==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n==4504==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)\n\n==4504== 880 (48 direct, 832 indirect) bytes in 6 blocks are definitely lost in loss record 470 of 1,918\n==4504==    at 0x4A1C344: operator new(unsigned long) (vg_replace_malloc.c:227)\n==4504==    by 0x6041D65: ZZ_pX_factor (in /tmp/Work-mabshoff/sage-2.8.11/devel/sage-main/c_lib/libcsage.so)\n==4504==    by 0xCC4C380: __pyx_pf_4sage_4libs_3ntl_9ntl_ZZ_pX_9ntl_ZZ_pX_factor(_object*, _object*, _object*) (ntl_ZZ_pX.cp\np:3407)\n==4504==    by 0x483031: PyEval_EvalFrameEx (ceval.c:3564)\n==4504==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n==4504==    by 0x483CC4: PyEval_EvalFrameEx (ceval.c:494)\n==4504==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n==4504==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)\n==4504==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n==4504==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)\n==4504==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n==4504==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)\n```\n\nI believe those leaks are actually in NTL itself. Shoup has stated that there are some issues, but that he is not going to fix them, but I might be totally wrong here :)\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1093\n\n",
    "created_at": "2007-11-04T00:05:03Z",
    "labels": [
        "component: memleak",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10",
    "title": "small memleaks exposed by ntl_ZZ_pX.py (from 2.8.12.alpha0)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1093",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

ntl_ZZ_pX.py

```
==4504== 504 (72 direct, 432 indirect) bytes in 9 blocks are definitely lost in loss record 305 of 1,918
==4504==    at 0x4A1C344: operator new(unsigned long) (vg_replace_malloc.c:227)
==4504==    by 0x6041C2A: ZZ_pX_linear_roots (in /tmp/Work-mabshoff/sage-2.8.11/devel/sage-main/c_lib/libcsage.so)
==4504==    by 0xCC4DB97: __pyx_pf_4sage_4libs_3ntl_9ntl_ZZ_pX_9ntl_ZZ_pX_linear_roots(_object*, _object*) (ntl_ZZ_pX.cpp:35
95)
==4504==    by 0x482FE8: PyEval_EvalFrameEx (ceval.c:3548)
==4504==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==4504==    by 0x483CC4: PyEval_EvalFrameEx (ceval.c:494)
==4504==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==4504==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)
==4504==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==4504==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)
==4504==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==4504==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)

==4504== 880 (48 direct, 832 indirect) bytes in 6 blocks are definitely lost in loss record 470 of 1,918
==4504==    at 0x4A1C344: operator new(unsigned long) (vg_replace_malloc.c:227)
==4504==    by 0x6041D65: ZZ_pX_factor (in /tmp/Work-mabshoff/sage-2.8.11/devel/sage-main/c_lib/libcsage.so)
==4504==    by 0xCC4C380: __pyx_pf_4sage_4libs_3ntl_9ntl_ZZ_pX_9ntl_ZZ_pX_factor(_object*, _object*, _object*) (ntl_ZZ_pX.cp
p:3407)
==4504==    by 0x483031: PyEval_EvalFrameEx (ceval.c:3564)
==4504==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==4504==    by 0x483CC4: PyEval_EvalFrameEx (ceval.c:494)
==4504==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==4504==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)
==4504==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==4504==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)
==4504==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==4504==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)
```

I believe those leaks are actually in NTL itself. Shoup has stated that there are some issues, but that he is not going to fix them, but I might be totally wrong here :)

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1093





---

archive/issue_comments_006597.json:
```json
{
    "body": "With Sage 2.10.alpha0 I get:\n\n```\n==26526== 880 (48 direct, 832 indirect) bytes in 6 blocks are definitely lost in loss record 1,361 of 7,607\n==26526==    at 0x4A1C344: operator new(unsigned long) (vg_replace_malloc.c:227)\n==26526==    by 0x6041D25: ZZ_pX_factor (in /tmp/Work-mabshoff/release-cycle/sage-2.9.3.rc1ish/devel/sage-main/c_lib/libcsag\ne.so)\n==26526==    by 0xC9F8440: __pyx_pf_4sage_4libs_3ntl_9ntl_ZZ_pX_9ntl_ZZ_pX_factor(_object*, _object*, _object*) (ntl_ZZ_pX.c\npp:4208)\n==26526==    by 0x482C61: PyEval_EvalFrameEx (ceval.c:3564)\n==26526==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==26526==    by 0x4838F4: PyEval_EvalFrameEx (ceval.c:494)\n==26526==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==26526==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)\n==26526==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==26526==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)\n==26526==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==26526==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)\n\n==26526== 504 (72 direct, 432 indirect) bytes in 9 blocks are definitely lost in loss record 3,419 of 7,607\n==26526==    at 0x4A1C344: operator new(unsigned long) (vg_replace_malloc.c:227)\n==26526==    by 0x6041BEA: ZZ_pX_linear_roots (in /tmp/Work-mabshoff/release-cycle/sage-2.9.3.rc1ish/devel/sage-main/c_lib/l\nibcsage.so)\n==26526==    by 0xC9F9C57: __pyx_pf_4sage_4libs_3ntl_9ntl_ZZ_pX_9ntl_ZZ_pX_linear_roots(_object*, _object*) (ntl_ZZ_pX.cpp:4\n420)\n==26526==    by 0x482C18: PyEval_EvalFrameEx (ceval.c:3548)\n==26526==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==26526==    by 0x4838F4: PyEval_EvalFrameEx (ceval.c:494)\n==26526==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==26526==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)\n==26526==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==26526==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)\n==26526==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==26526==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)\n```\n\nLeak summary:\n\n```\n==26526== LEAK SUMMARY:\n==26526==    definitely lost: 120 bytes in 15 blocks.\n==26526==    indirectly lost: 1,264 bytes in 21 blocks.\n==26526==      possibly lost: 275,647 bytes in 811 blocks.\n==26526==    still reachable: 29,982,860 bytes in 185,500 blocks.\n==26526==         suppressed: 0 bytes in 0 blocks.\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-01-07T18:03:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1093",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1093#issuecomment-6597",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

With Sage 2.10.alpha0 I get:

```
==26526== 880 (48 direct, 832 indirect) bytes in 6 blocks are definitely lost in loss record 1,361 of 7,607
==26526==    at 0x4A1C344: operator new(unsigned long) (vg_replace_malloc.c:227)
==26526==    by 0x6041D25: ZZ_pX_factor (in /tmp/Work-mabshoff/release-cycle/sage-2.9.3.rc1ish/devel/sage-main/c_lib/libcsag
e.so)
==26526==    by 0xC9F8440: __pyx_pf_4sage_4libs_3ntl_9ntl_ZZ_pX_9ntl_ZZ_pX_factor(_object*, _object*, _object*) (ntl_ZZ_pX.c
pp:4208)
==26526==    by 0x482C61: PyEval_EvalFrameEx (ceval.c:3564)
==26526==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==26526==    by 0x4838F4: PyEval_EvalFrameEx (ceval.c:494)
==26526==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==26526==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)
==26526==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==26526==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)
==26526==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==26526==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)

==26526== 504 (72 direct, 432 indirect) bytes in 9 blocks are definitely lost in loss record 3,419 of 7,607
==26526==    at 0x4A1C344: operator new(unsigned long) (vg_replace_malloc.c:227)
==26526==    by 0x6041BEA: ZZ_pX_linear_roots (in /tmp/Work-mabshoff/release-cycle/sage-2.9.3.rc1ish/devel/sage-main/c_lib/l
ibcsage.so)
==26526==    by 0xC9F9C57: __pyx_pf_4sage_4libs_3ntl_9ntl_ZZ_pX_9ntl_ZZ_pX_linear_roots(_object*, _object*) (ntl_ZZ_pX.cpp:4
420)
==26526==    by 0x482C18: PyEval_EvalFrameEx (ceval.c:3548)
==26526==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==26526==    by 0x4838F4: PyEval_EvalFrameEx (ceval.c:494)
==26526==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==26526==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)
==26526==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==26526==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)
==26526==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==26526==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)
```

Leak summary:

```
==26526== LEAK SUMMARY:
==26526==    definitely lost: 120 bytes in 15 blocks.
==26526==    indirectly lost: 1,264 bytes in 21 blocks.
==26526==      possibly lost: 275,647 bytes in 811 blocks.
==26526==    still reachable: 29,982,860 bytes in 185,500 blocks.
==26526==         suppressed: 0 bytes in 0 blocks.
```


Cheers,

Michael



---

archive/issue_comments_006598.json:
```json
{
    "body": "Ok, the attached patch fixes the issue for me:\n\n```\n==21015== LEAK SUMMARY:\n==21015==    definitely lost: 0 bytes in 0 blocks.\n==21015==      possibly lost: 275,647 bytes in 811 blocks.\n==21015==    still reachable: 29,982,990 bytes in 185,501 blocks.\n==21015==         suppressed: 0 bytes in 0 blocks\n```\n\nAs `ntl_wrap.h` states:\n\n```\n// Factoring elements of ZZ_pX:\n// OUTPUT: v -- pointer to list of n ZZ_pX elements (the irred factors)\n//         e -- point to list of e longs (the exponents)\n//         n -- length of above two lists\n//  The lists v and e are mallocd, and must be freed by the calling code.\nEXTERN void ZZ_pX_factor(struct ZZ_pX*** v, long** e, long* n, struct ZZ_pX* x, long verbose);\nEXTERN void ZZ_pX_linear_roots(struct ZZ_p*** v, long* n, struct ZZ_pX* f);\n```\n\nThe other part of the patch fixes the following problem which was only triggered after correctly freeing `v`:\n\n```\n==19279== Mismatched free() / delete / delete []\n==19279==    at 0x4A1B74A: free (vg_replace_malloc.c:320)\n==19279==    by 0xC9F501F: __pyx_pf_4sage_4libs_3ntl_9ntl_ZZ_pX_9ntl_ZZ_pX_trace_list(_object*, _object*) (ntl_ZZ_pX.cpp:419\n)\n==19279==    by 0x482C18: PyEval_EvalFrameEx (ceval.c:3548)\n==19279==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==19279==    by 0x4838F4: PyEval_EvalFrameEx (ceval.c:494)\n==19279==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==19279==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)\n==19279==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==19279==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)\n==19279==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==19279==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)\n==19279==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==19279==  Address 0x177a3a40 is 0 bytes inside a block of size 14 alloc'd\n==19279==    at 0x4A1BFE4: operator new[](unsigned long) (vg_replace_malloc.c:271)\n==19279==    by 0x6042125: ZZ_pX_trace_list (in /tmp/Work-mabshoff/release-cycle/sage-2.10.alpha0/devel/sage-main/c_lib/libc\nsage.so)\n==19279==    by 0xC9F4F89: __pyx_pf_4sage_4libs_3ntl_9ntl_ZZ_pX_9ntl_ZZ_pX_trace_list(_object*, _object*) (ntl_ZZ_pX.cpp:538\n3)\n==19279==    by 0x482C18: PyEval_EvalFrameEx (ceval.c:3548)\n==19279==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==19279==    by 0x4838F4: PyEval_EvalFrameEx (ceval.c:494)\n==19279==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==19279==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)\n==19279==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==19279==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)\n==19279==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==19279==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-01-07T22:50:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1093",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1093#issuecomment-6598",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ok, the attached patch fixes the issue for me:

```
==21015== LEAK SUMMARY:
==21015==    definitely lost: 0 bytes in 0 blocks.
==21015==      possibly lost: 275,647 bytes in 811 blocks.
==21015==    still reachable: 29,982,990 bytes in 185,501 blocks.
==21015==         suppressed: 0 bytes in 0 blocks
```

As `ntl_wrap.h` states:

```
// Factoring elements of ZZ_pX:
// OUTPUT: v -- pointer to list of n ZZ_pX elements (the irred factors)
//         e -- point to list of e longs (the exponents)
//         n -- length of above two lists
//  The lists v and e are mallocd, and must be freed by the calling code.
EXTERN void ZZ_pX_factor(struct ZZ_pX*** v, long** e, long* n, struct ZZ_pX* x, long verbose);
EXTERN void ZZ_pX_linear_roots(struct ZZ_p*** v, long* n, struct ZZ_pX* f);
```

The other part of the patch fixes the following problem which was only triggered after correctly freeing `v`:

```
==19279== Mismatched free() / delete / delete []
==19279==    at 0x4A1B74A: free (vg_replace_malloc.c:320)
==19279==    by 0xC9F501F: __pyx_pf_4sage_4libs_3ntl_9ntl_ZZ_pX_9ntl_ZZ_pX_trace_list(_object*, _object*) (ntl_ZZ_pX.cpp:419
)
==19279==    by 0x482C18: PyEval_EvalFrameEx (ceval.c:3548)
==19279==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==19279==    by 0x4838F4: PyEval_EvalFrameEx (ceval.c:494)
==19279==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==19279==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)
==19279==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==19279==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)
==19279==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==19279==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)
==19279==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==19279==  Address 0x177a3a40 is 0 bytes inside a block of size 14 alloc'd
==19279==    at 0x4A1BFE4: operator new[](unsigned long) (vg_replace_malloc.c:271)
==19279==    by 0x6042125: ZZ_pX_trace_list (in /tmp/Work-mabshoff/release-cycle/sage-2.10.alpha0/devel/sage-main/c_lib/libc
sage.so)
==19279==    by 0xC9F4F89: __pyx_pf_4sage_4libs_3ntl_9ntl_ZZ_pX_9ntl_ZZ_pX_trace_list(_object*, _object*) (ntl_ZZ_pX.cpp:538
3)
==19279==    by 0x482C18: PyEval_EvalFrameEx (ceval.c:3548)
==19279==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==19279==    by 0x4838F4: PyEval_EvalFrameEx (ceval.c:494)
==19279==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==19279==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)
==19279==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==19279==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)
==19279==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==19279==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)
```


Cheers,

Michael



---

archive/issue_comments_006599.json:
```json
{
    "body": "Attachment [Sage-2.10.alpha3-fix-ntl_ZZ_pX.pyx-memleaks.patch](tarball://root/attachments/some-uuid/ticket1093/Sage-2.10.alpha3-fix-ntl_ZZ_pX.pyx-memleaks.patch) by mabshoff created at 2008-01-07 22:50:45",
    "created_at": "2008-01-07T22:50:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1093",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1093#issuecomment-6599",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [Sage-2.10.alpha3-fix-ntl_ZZ_pX.pyx-memleaks.patch](tarball://root/attachments/some-uuid/ticket1093/Sage-2.10.alpha3-fix-ntl_ZZ_pX.pyx-memleaks.patch) by mabshoff created at 2008-01-07 22:50:45



---

archive/issue_comments_006600.json:
```json
{
    "body": "The patch to ntl_ZZ_pX.pyx looks correct to me.\n\nI'd fix the mismatched free/delete[] by changing the string(t) call to a string_delete(t) call, instead of modifying string(), though.\nPatch attached to do this, also in ntl_ZZX.pyx.",
    "created_at": "2008-01-07T23:40:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1093",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1093#issuecomment-6600",
    "user": "https://github.com/wjp"
}
```

The patch to ntl_ZZ_pX.pyx looks correct to me.

I'd fix the mismatched free/delete[] by changing the string(t) call to a string_delete(t) call, instead of modifying string(), though.
Patch attached to do this, also in ntl_ZZX.pyx.



---

archive/issue_comments_006601.json:
```json
{
    "body": "Attachment [ntl_free_mismatch.patch](tarball://root/attachments/some-uuid/ticket1093/ntl_free_mismatch.patch) by mabshoff created at 2008-01-08 00:37:02",
    "created_at": "2008-01-08T00:37:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1093",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1093#issuecomment-6601",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [ntl_free_mismatch.patch](tarball://root/attachments/some-uuid/ticket1093/ntl_free_mismatch.patch) by mabshoff created at 2008-01-08 00:37:02



---

archive/issue_comments_006602.json:
```json
{
    "body": "Attachment [Sage-2.10.alpha3-revert-charstar-fix.patch](tarball://root/attachments/some-uuid/ticket1093/Sage-2.10.alpha3-revert-charstar-fix.patch) by mabshoff created at 2008-01-08 00:37:37\n\nApply patches in order of attaching them.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-08T00:37:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1093",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1093#issuecomment-6602",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [Sage-2.10.alpha3-revert-charstar-fix.patch](tarball://root/attachments/some-uuid/ticket1093/Sage-2.10.alpha3-revert-charstar-fix.patch) by mabshoff created at 2008-01-08 00:37:37

Apply patches in order of attaching them.

Cheers,

Michael



---

archive/issue_comments_006603.json:
```json
{
    "body": "These three patches together look good to me.",
    "created_at": "2008-01-08T00:39:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1093",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1093#issuecomment-6603",
    "user": "https://github.com/wjp"
}
```

These three patches together look good to me.



---

archive/issue_events_001219.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-08T02:07:12Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1093",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1093#event-1219"
}
```



---

archive/issue_comments_006604.json:
```json
{
    "body": "Merge in 2.10.alpha0",
    "created_at": "2008-01-08T02:07:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1093",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1093#issuecomment-6604",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merge in 2.10.alpha0



---

archive/issue_comments_006605.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-08T02:07:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1093",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1093#issuecomment-6605",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
