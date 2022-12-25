# Issue 866: [with patch] big NTL patch

archive/issues_000866.json:
```json
{
    "body": "Assignee: @craigcitro\n\nKeywords: ntl\n\nThis is the big NTL patch that several people were working on during SD5. There's a ton of code in here, due to Joel Mohler, Craig Citro, Robert Bradshaw, David Harvey, and probably several more people I've forgotten. \n\nIssue created by migration from https://trac.sagemath.org/ticket/866\n\n",
    "created_at": "2007-10-12T21:11:38Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.7",
    "title": "[with patch] big NTL patch",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/866",
    "user": "https://github.com/craigcitro"
}
```
Assignee: @craigcitro

Keywords: ntl

This is the big NTL patch that several people were working on during SD5. There's a ton of code in here, due to Joel Mohler, Craig Citro, Robert Bradshaw, David Harvey, and probably several more people I've forgotten. 

Issue created by migration from https://trac.sagemath.org/ticket/866





---

archive/issue_comments_005334.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-12T21:11:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/866#issuecomment-5334",
    "user": "https://github.com/craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_005335.json:
```json
{
    "body": "Attachment [full-ntl-bundle.hg](tarball://root/attachments/some-uuid/ticket866/full-ntl-bundle.hg) by @craigcitro created at 2007-10-12 21:11:57",
    "created_at": "2007-10-12T21:11:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/866#issuecomment-5335",
    "user": "https://github.com/craigcitro"
}
```

Attachment [full-ntl-bundle.hg](tarball://root/attachments/some-uuid/ticket866/full-ntl-bundle.hg) by @craigcitro created at 2007-10-12 21:11:57



---

archive/issue_comments_005336.json:
```json
{
    "body": "Hello,\n\nI ran Ifti's code with 3 iterations (see ticket #501) and there is a problem in __repr__:\n\n```\n==6721== 1,337,726 bytes in 97,087 blocks are definitely lost in loss record 2,181 of 2,187\n==6721==    at 0x4A1BFE4: operator new[](unsigned long) (vg_replace_malloc.c:271)\n==6721==    by 0x5FE0769: ZZ_pX_repr (in /tmp/Work-mabshoff/sage-2.8.6/devel/sage-main/c_lib/libcsage.so)\n==6721==    by 0xCBE62C0: __pyx_f_9ntl_ZZ_pX_9ntl_ZZ_pX___repr__(_object*) (ntl_ZZ_pX.cpp:1020)\n==6721==    by 0x443299: _PyObject_Str (object.c:406)\n==6721==    by 0x44333A: PyObject_Str (object.c:426)\n==6721==    by 0x44DC7F: string_new (stringobject.c:3892)\n==6721==    by 0x459172: type_call (typeobject.c:422)\n==6721==    by 0x415522: PyObject_Call (abstract.c:1860)\n==6721==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==6721==    by 0xF1773F3: __pyx_f_25polynomial_modn_dense_ntl_22Polynomial_dense_mod_n_int_list(_object*, _object*) (polynom\nial_modn_dense_ntl.cpp:1831)\n==6721==    by 0x415522: PyObject_Call (abstract.c:1860)\n==6721==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2007-10-13T01:27:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/866#issuecomment-5336",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hello,

I ran Ifti's code with 3 iterations (see ticket #501) and there is a problem in __repr__:

```
==6721== 1,337,726 bytes in 97,087 blocks are definitely lost in loss record 2,181 of 2,187
==6721==    at 0x4A1BFE4: operator new[](unsigned long) (vg_replace_malloc.c:271)
==6721==    by 0x5FE0769: ZZ_pX_repr (in /tmp/Work-mabshoff/sage-2.8.6/devel/sage-main/c_lib/libcsage.so)
==6721==    by 0xCBE62C0: __pyx_f_9ntl_ZZ_pX_9ntl_ZZ_pX___repr__(_object*) (ntl_ZZ_pX.cpp:1020)
==6721==    by 0x443299: _PyObject_Str (object.c:406)
==6721==    by 0x44333A: PyObject_Str (object.c:426)
==6721==    by 0x44DC7F: string_new (stringobject.c:3892)
==6721==    by 0x459172: type_call (typeobject.c:422)
==6721==    by 0x415522: PyObject_Call (abstract.c:1860)
==6721==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)
==6721==    by 0xF1773F3: __pyx_f_25polynomial_modn_dense_ntl_22Polynomial_dense_mod_n_int_list(_object*, _object*) (polynom
ial_modn_dense_ntl.cpp:1831)
==6721==    by 0x415522: PyObject_Call (abstract.c:1860)
==6721==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)
```


Cheers,

Michael



---

archive/issue_comments_005337.json:
```json
{
    "body": "Hello,\n\n__repr__ in ntl_ZZ_pX.pyx leaks. With the following (ugly) patch this problem is solved:\n\n```\n==7976== LEAK SUMMARY:\n==7976==    definitely lost: 616 bytes in 50 blocks.\n==7976==      possibly lost: 325,454 bytes in 776 blocks.\n==7976==    still reachable: 36,843,962 bytes in 19,920 blocks.\n==7976==         suppressed: 0 bytes in 0 blocks.\n```\n\nIt was only one round instead of three, but the problem is gone.\n\nCheers,\n\nMichael",
    "created_at": "2007-10-13T02:02:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/866#issuecomment-5337",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hello,

__repr__ in ntl_ZZ_pX.pyx leaks. With the following (ugly) patch this problem is solved:

```
==7976== LEAK SUMMARY:
==7976==    definitely lost: 616 bytes in 50 blocks.
==7976==      possibly lost: 325,454 bytes in 776 blocks.
==7976==    still reachable: 36,843,962 bytes in 19,920 blocks.
==7976==         suppressed: 0 bytes in 0 blocks.
```

It was only one round instead of three, but the problem is gone.

Cheers,

Michael



---

archive/issue_comments_005338.json:
```json
{
    "body": "Attachment [Sage-2.8.6-fix-__repr__-memleak-in-ntl_ZZ_pX.patch](tarball://root/attachments/some-uuid/ticket866/Sage-2.8.6-fix-__repr__-memleak-in-ntl_ZZ_pX.patch) by mabshoff created at 2007-10-13 02:03:10\n\nfiix the __repr__ leak",
    "created_at": "2007-10-13T02:03:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/866#issuecomment-5338",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [Sage-2.8.6-fix-__repr__-memleak-in-ntl_ZZ_pX.patch](tarball://root/attachments/some-uuid/ticket866/Sage-2.8.6-fix-__repr__-memleak-in-ntl_ZZ_pX.patch) by mabshoff created at 2007-10-13 02:03:10

fiix the __repr__ leak



---

archive/issue_comments_005339.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-13T07:34:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/866#issuecomment-5339",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_000978.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-13T07:34:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/866",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/866#event-978"
}
```
