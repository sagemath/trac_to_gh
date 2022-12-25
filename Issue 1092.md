# Issue 1092: [with patch, with positive review] small memleaks exposed by ntl_ZZ_pE (from 2.8.12.alpha0)

archive/issues_001092.json:
```json
{
    "body": "Assignee: mabshoff\n\nntl_ZZ_pE.py\n\n```\n==4443== 104 (8 direct, 96 indirect) bytes in 1 blocks are definitely lost in loss record 33 of 1,883\n==4443==    at 0x4A1C344: operator new(unsigned long) (vg_replace_malloc.c:227)\n==4443==    by 0x5C41AB6: ZZ_pE_to_ZZ_pX (in /tmp/Work-mabshoff/sage-2.8.11/devel/sage-main/c_lib/libcsage.so)\n==4443==    by 0xCE6A067: __pyx_f_4sage_4libs_3ntl_9ntl_ZZ_pE_9ntl_ZZ_pE_get_as_ZZ_pX (ntl_ZZ_pE.cpp:2514)\n==4443==    by 0xCE6889E: __pyx_pf_4sage_4libs_3ntl_9ntl_ZZ_pE_9ntl_ZZ_pE___reduce__(_object*, _object*) (ntl_ZZ_pE.cpp:1661\n)\n==4443==    by 0x415522: PyObject_Call (abstract.c:1860)\n==4443==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==4443==    by 0x4589BF: object_reduce_ex (typeobject.c:2786)\n==4443==    by 0x415522: PyObject_Call (abstract.c:1860)\n==4443==    by 0x76F0743: save (cPickle.c:2495)\n==4443==    by 0x76F2597: cpm_dumps (cPickle.c:2577)\n==4443==    by 0x415522: PyObject_Call (abstract.c:1860)\n==4443==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)\n\n==4443== 136 (8 direct, 128 indirect) bytes in 1 blocks are definitely lost in loss record 84 of 1,883\n==4443==    at 0x4A1C344: operator new(unsigned long) (vg_replace_malloc.c:227)\n==4443==    by 0x5C41AB6: ZZ_pE_to_ZZ_pX (in /tmp/Work-mabshoff/sage-2.8.11/devel/sage-main/c_lib/libcsage.so)\n==4443==    by 0xCE6A067: __pyx_f_4sage_4libs_3ntl_9ntl_ZZ_pE_9ntl_ZZ_pE_get_as_ZZ_pX (ntl_ZZ_pE.cpp:2514)\n==4443==    by 0xCE67C49: __pyx_pf_4sage_4libs_3ntl_9ntl_ZZ_pE_9ntl_ZZ_pE_get_as_ZZ_pX_doctest(_object*, _object*) (ntl_ZZ_p\nE.cpp:2554)\n==4443==    by 0x482FE8: PyEval_EvalFrameEx (ceval.c:3548)\n==4443==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n==4443==    by 0x483CC4: PyEval_EvalFrameEx (ceval.c:494)\n==4443==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n==4443==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)\n==4443==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n==4443==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)\n==4443==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/1092\n\n",
    "closed_at": "2008-01-08T02:03:16Z",
    "created_at": "2007-11-04T00:02:14Z",
    "labels": [
        "component: memleak",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10",
    "title": "[with patch, with positive review] small memleaks exposed by ntl_ZZ_pE (from 2.8.12.alpha0)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1092",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

ntl_ZZ_pE.py

```
==4443== 104 (8 direct, 96 indirect) bytes in 1 blocks are definitely lost in loss record 33 of 1,883
==4443==    at 0x4A1C344: operator new(unsigned long) (vg_replace_malloc.c:227)
==4443==    by 0x5C41AB6: ZZ_pE_to_ZZ_pX (in /tmp/Work-mabshoff/sage-2.8.11/devel/sage-main/c_lib/libcsage.so)
==4443==    by 0xCE6A067: __pyx_f_4sage_4libs_3ntl_9ntl_ZZ_pE_9ntl_ZZ_pE_get_as_ZZ_pX (ntl_ZZ_pE.cpp:2514)
==4443==    by 0xCE6889E: __pyx_pf_4sage_4libs_3ntl_9ntl_ZZ_pE_9ntl_ZZ_pE___reduce__(_object*, _object*) (ntl_ZZ_pE.cpp:1661
)
==4443==    by 0x415522: PyObject_Call (abstract.c:1860)
==4443==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)
==4443==    by 0x4589BF: object_reduce_ex (typeobject.c:2786)
==4443==    by 0x415522: PyObject_Call (abstract.c:1860)
==4443==    by 0x76F0743: save (cPickle.c:2495)
==4443==    by 0x76F2597: cpm_dumps (cPickle.c:2577)
==4443==    by 0x415522: PyObject_Call (abstract.c:1860)
==4443==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)

==4443== 136 (8 direct, 128 indirect) bytes in 1 blocks are definitely lost in loss record 84 of 1,883
==4443==    at 0x4A1C344: operator new(unsigned long) (vg_replace_malloc.c:227)
==4443==    by 0x5C41AB6: ZZ_pE_to_ZZ_pX (in /tmp/Work-mabshoff/sage-2.8.11/devel/sage-main/c_lib/libcsage.so)
==4443==    by 0xCE6A067: __pyx_f_4sage_4libs_3ntl_9ntl_ZZ_pE_9ntl_ZZ_pE_get_as_ZZ_pX (ntl_ZZ_pE.cpp:2514)
==4443==    by 0xCE67C49: __pyx_pf_4sage_4libs_3ntl_9ntl_ZZ_pE_9ntl_ZZ_pE_get_as_ZZ_pX_doctest(_object*, _object*) (ntl_ZZ_p
E.cpp:2554)
==4443==    by 0x482FE8: PyEval_EvalFrameEx (ceval.c:3548)
==4443==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==4443==    by 0x483CC4: PyEval_EvalFrameEx (ceval.c:494)
==4443==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==4443==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)
==4443==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==4443==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)
==4443==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
```

Issue created by migration from https://trac.sagemath.org/ticket/1092





---

archive/issue_comments_006592.json:
```json
{
    "body": "With Sage 2.10.alpha0 I get:\n\n```\n==26597== 104 (8 direct, 96 indirect) bytes in 1 blocks are definitely lost in loss record 1,466 of 7,536\n==26597==    at 0x4A1C344: operator new(unsigned long) (vg_replace_malloc.c:227)\n==26597==    by 0x5C41A76: ZZ_pE_to_ZZ_pX (in /tmp/Work-mabshoff/release-cycle/sage-2.9.3.rc1ish/devel/sage-main/c_lib/libcs\nage.so)\n==26597==    by 0xCC170F7: __pyx_f_4sage_4libs_3ntl_9ntl_ZZ_pE_9ntl_ZZ_pE_get_as_ZZ_pX (ntl_ZZ_pE.cpp:4203)\n==26597==    by 0xCC1592E: __pyx_pf_4sage_4libs_3ntl_9ntl_ZZ_pE_9ntl_ZZ_pE___reduce__(_object*, _object*) (ntl_ZZ_pE.cpp:312\n6)\n==26597==    by 0x415542: PyObject_Call (abstract.c:1860)\n==26597==    by 0x47C480: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==26597==    by 0x4585DF: object_reduce_ex (typeobject.c:2786)\n==26597==    by 0x415542: PyObject_Call (abstract.c:1860)\n==26597==    by 0x7AEF743: save (cPickle.c:2495)\n==26597==    by 0x7AF1597: cpm_dumps (cPickle.c:2577)\n==26597==    by 0x415542: PyObject_Call (abstract.c:1860)\n==26597==    by 0x47C480: PyEval_CallObjectWithKeywords (ceval.c:3433)\n\n==26597== 136 (8 direct, 128 indirect) bytes in 1 blocks are definitely lost in loss record 3,065 of 7,536\n==26597==    at 0x4A1C344: operator new(unsigned long) (vg_replace_malloc.c:227)\n==26597==    by 0x5C41A76: ZZ_pE_to_ZZ_pX (in /tmp/Work-mabshoff/release-cycle/sage-2.9.3.rc1ish/devel/sage-main/c_lib/libcs\nage.so)\n==26597==    by 0xCC170F7: __pyx_f_4sage_4libs_3ntl_9ntl_ZZ_pE_9ntl_ZZ_pE_get_as_ZZ_pX (ntl_ZZ_pE.cpp:4203)\n==26597==    by 0xCC14CD9: __pyx_pf_4sage_4libs_3ntl_9ntl_ZZ_pE_9ntl_ZZ_pE_get_as_ZZ_pX_doctest(_object*, _object*) (ntl_ZZ_\npE.cpp:4259)\n==26597==    by 0x482C18: PyEval_EvalFrameEx (ceval.c:3548)\n==26597==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==26597==    by 0x4838F4: PyEval_EvalFrameEx (ceval.c:494)\n==26597==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==26597==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)\n==26597==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==26597==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)\n==26597==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n```\nLeak Summary:\n\n```\n==26597==    definitely lost: 16 bytes in 2 blocks.\n==26597==    indirectly lost: 224 bytes in 4 blocks.\n==26597==      possibly lost: 255,295 bytes in 769 blocks.\n==26597==    still reachable: 29,400,323 bytes in 182,486 blocks.\n==26597==         suppressed: 0 bytes in 0 blocks.\n```\n\nCheers,\n\nMichael",
    "created_at": "2008-01-07T18:09:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1092",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1092#issuecomment-6592",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

With Sage 2.10.alpha0 I get:

```
==26597== 104 (8 direct, 96 indirect) bytes in 1 blocks are definitely lost in loss record 1,466 of 7,536
==26597==    at 0x4A1C344: operator new(unsigned long) (vg_replace_malloc.c:227)
==26597==    by 0x5C41A76: ZZ_pE_to_ZZ_pX (in /tmp/Work-mabshoff/release-cycle/sage-2.9.3.rc1ish/devel/sage-main/c_lib/libcs
age.so)
==26597==    by 0xCC170F7: __pyx_f_4sage_4libs_3ntl_9ntl_ZZ_pE_9ntl_ZZ_pE_get_as_ZZ_pX (ntl_ZZ_pE.cpp:4203)
==26597==    by 0xCC1592E: __pyx_pf_4sage_4libs_3ntl_9ntl_ZZ_pE_9ntl_ZZ_pE___reduce__(_object*, _object*) (ntl_ZZ_pE.cpp:312
6)
==26597==    by 0x415542: PyObject_Call (abstract.c:1860)
==26597==    by 0x47C480: PyEval_CallObjectWithKeywords (ceval.c:3433)
==26597==    by 0x4585DF: object_reduce_ex (typeobject.c:2786)
==26597==    by 0x415542: PyObject_Call (abstract.c:1860)
==26597==    by 0x7AEF743: save (cPickle.c:2495)
==26597==    by 0x7AF1597: cpm_dumps (cPickle.c:2577)
==26597==    by 0x415542: PyObject_Call (abstract.c:1860)
==26597==    by 0x47C480: PyEval_CallObjectWithKeywords (ceval.c:3433)

==26597== 136 (8 direct, 128 indirect) bytes in 1 blocks are definitely lost in loss record 3,065 of 7,536
==26597==    at 0x4A1C344: operator new(unsigned long) (vg_replace_malloc.c:227)
==26597==    by 0x5C41A76: ZZ_pE_to_ZZ_pX (in /tmp/Work-mabshoff/release-cycle/sage-2.9.3.rc1ish/devel/sage-main/c_lib/libcs
age.so)
==26597==    by 0xCC170F7: __pyx_f_4sage_4libs_3ntl_9ntl_ZZ_pE_9ntl_ZZ_pE_get_as_ZZ_pX (ntl_ZZ_pE.cpp:4203)
==26597==    by 0xCC14CD9: __pyx_pf_4sage_4libs_3ntl_9ntl_ZZ_pE_9ntl_ZZ_pE_get_as_ZZ_pX_doctest(_object*, _object*) (ntl_ZZ_
pE.cpp:4259)
==26597==    by 0x482C18: PyEval_EvalFrameEx (ceval.c:3548)
==26597==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==26597==    by 0x4838F4: PyEval_EvalFrameEx (ceval.c:494)
==26597==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==26597==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)
==26597==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==26597==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)
==26597==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
```
Leak Summary:

```
==26597==    definitely lost: 16 bytes in 2 blocks.
==26597==    indirectly lost: 224 bytes in 4 blocks.
==26597==      possibly lost: 255,295 bytes in 769 blocks.
==26597==    still reachable: 29,400,323 bytes in 182,486 blocks.
==26597==         suppressed: 0 bytes in 0 blocks.
```

Cheers,

Michael



---

archive/issue_comments_006593.json:
```json
{
    "body": "Attachment [memleak_ZZ_pE_to_ZZ_pX.patch](tarball://root/attachments/some-uuid/ticket1092/memleak_ZZ_pE_to_ZZ_pX.patch) by @wjp created at 2008-01-08 00:20:30",
    "created_at": "2008-01-08T00:20:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1092",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1092#issuecomment-6593",
    "user": "https://github.com/wjp"
}
```

Attachment [memleak_ZZ_pE_to_ZZ_pX.patch](tarball://root/attachments/some-uuid/ticket1092/memleak_ZZ_pE_to_ZZ_pX.patch) by @wjp created at 2008-01-08 00:20:30



---

archive/issue_comments_006594.json:
```json
{
    "body": "Nice catch. Looks good to me.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-08T00:29:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1092",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1092#issuecomment-6594",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Nice catch. Looks good to me.

Cheers,

Michael



---

archive/issue_comments_006595.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-08T02:03:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1092",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1092#issuecomment-6595",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_006596.json:
```json
{
    "body": "Merge in 2.10.alpha0",
    "created_at": "2008-01-08T02:03:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1092",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1092#issuecomment-6596",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merge in 2.10.alpha0



---

archive/issue_events_002942.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-08T02:03:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1092",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1092#event-2942"
}
```
