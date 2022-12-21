# Issue 1093: small memleaks exposed by ntl_ZZ_pX.py (from 2.8.12.alpha0)

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-11-04 00:05:03

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


---

Comment by mabshoff created at 2008-01-07 18:03:45

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

Comment by mabshoff created at 2008-01-07 22:50:05

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

Attachment


---

Comment by wjp created at 2008-01-07 23:40:41

The patch to ntl_ZZ_pX.pyx looks correct to me.

I'd fix the mismatched free/delete[] by changing the string(t) call to a string_delete(t) call, instead of modifying string(), though.
Patch attached to do this, also in ntl_ZZX.pyx.


---

Attachment


---

Attachment

Apply patches in order of attaching them.

Cheers,

Michael


---

Comment by wjp created at 2008-01-08 00:39:42

These three patches together look good to me.


---

Comment by mabshoff created at 2008-01-08 02:07:12

Merge in 2.10.alpha0


---

Comment by mabshoff created at 2008-01-08 02:07:12

Resolution: fixed
