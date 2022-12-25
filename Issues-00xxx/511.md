# Issue 511: memory leak: ntl wrapper leaks in __repr__

archive/issues_000511.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: ntl wrapper memory leak\n\nSee ticket #501 for more details:\n\nThe problem:\n\n```\n==22784== 791,674 bytes in 65,421 blocks are definitely lost in loss record 2,472 of 2,481\n==22784==    at 0x4A05CB9: operator new[](unsigned long) (vg_replace_malloc.c:199)\n==22784==    by 0x9280247: ZZ_pX_repr (in /tmp/Work2/sage-2.8.3.alpha2/local/lib/libcsage.so.0.0.0)\n==22784==    by 0x176D6D57: __pyx_f_3ntl_9ntl_ZZ_pX___repr__ (ntl.c:6216)\n==22784==    by 0x443C61: _PyObject_Str (object.c:406)\n==22784==    by 0x443D0A: PyObject_Str (object.c:426)\n==22784==    by 0x44EA8F: string_new (stringobject.c:3892)\n==22784==    by 0x45A272: type_call (typeobject.c:422)\n==22784==    by 0x4156A2: PyObject_Call (abstract.c:1860)\n==22784==    by 0x480783: PyEval_EvalFrameEx (ceval.c:3775)\n==22784==    by 0x485025: PyEval_EvalFrameEx (ceval.c:3650)\n==22784==    by 0x4865EF: PyEval_EvalCodeEx (ceval.c:2831)\n==22784==    by 0x4CFF37: function_call (funcobject.c:517)\n```\n\nThe fix was suggested by was but never implemented:\n\n```\n17:53 < wstein> I changed that __repr__ code to this:\n17:53 < wstein> ntl.set_modulus(ntl.ZZ(20))\n17:53 < wstein> f = ntl.ZZ_pX(range(10000))\n17:54 < wstein>     def __repr__(self):\n17:54 < wstein>         cdef char* s = ZZ_pX_repr(self.x)\n17:54 < wstein>         t = str(s)\n17:54 < wstein>         free(s)\n17:54 < wstein>         return t\n17:54 < wstein> And the memory leak completely vanishes.\n17:54 < mabshoff> :)\n17:54 < wstein> Of course, this is wrong since I'm mixing malloc's free with C++'s new.\n17:54 < wstein> It's just a demo.\n17:54 < mabshoff> mmmh\n```\nSo the credit should go to him, but I also fixed a second analog problem further down the code.\n\nWithout the patch:\n\n```\n==22784== LEAK SUMMARY:\n==22784==    definitely lost: 794,838 bytes in 65,475 blocks.\n==22784==      possibly lost: 350,158 bytes in 953 blocks.\n==22784==    still reachable: 137,588,639 bytes in 19,728 blocks.\n==22784==         suppressed: 0 bytes in 0 blocks.\n```\n\nWith the patch:\n\n```\n==22993== LEAK SUMMARY:\n==22993==    definitely lost: 3,103 bytes in 49 blocks.\n==22993==      possibly lost: 349,334 bytes in 931 blocks.\n==22993==    still reachable: 137,589,847 bytes in 19,621 blocks.\n==22993==         suppressed: 0 bytes in 0 blocks.\n```\n\nThe test computation finished, but I have no clue if it is correct.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/511\n\n",
    "closed_at": "2007-08-30T02:11:41Z",
    "created_at": "2007-08-29T12:06:18Z",
    "labels": [
        "component: basic arithmetic",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.3",
    "title": "memory leak: ntl wrapper leaks in __repr__",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/511",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @williamstein

Keywords: ntl wrapper memory leak

See ticket #501 for more details:

The problem:

```
==22784== 791,674 bytes in 65,421 blocks are definitely lost in loss record 2,472 of 2,481
==22784==    at 0x4A05CB9: operator new[](unsigned long) (vg_replace_malloc.c:199)
==22784==    by 0x9280247: ZZ_pX_repr (in /tmp/Work2/sage-2.8.3.alpha2/local/lib/libcsage.so.0.0.0)
==22784==    by 0x176D6D57: __pyx_f_3ntl_9ntl_ZZ_pX___repr__ (ntl.c:6216)
==22784==    by 0x443C61: _PyObject_Str (object.c:406)
==22784==    by 0x443D0A: PyObject_Str (object.c:426)
==22784==    by 0x44EA8F: string_new (stringobject.c:3892)
==22784==    by 0x45A272: type_call (typeobject.c:422)
==22784==    by 0x4156A2: PyObject_Call (abstract.c:1860)
==22784==    by 0x480783: PyEval_EvalFrameEx (ceval.c:3775)
==22784==    by 0x485025: PyEval_EvalFrameEx (ceval.c:3650)
==22784==    by 0x4865EF: PyEval_EvalCodeEx (ceval.c:2831)
==22784==    by 0x4CFF37: function_call (funcobject.c:517)
```

The fix was suggested by was but never implemented:

```
17:53 < wstein> I changed that __repr__ code to this:
17:53 < wstein> ntl.set_modulus(ntl.ZZ(20))
17:53 < wstein> f = ntl.ZZ_pX(range(10000))
17:54 < wstein>     def __repr__(self):
17:54 < wstein>         cdef char* s = ZZ_pX_repr(self.x)
17:54 < wstein>         t = str(s)
17:54 < wstein>         free(s)
17:54 < wstein>         return t
17:54 < wstein> And the memory leak completely vanishes.
17:54 < mabshoff> :)
17:54 < wstein> Of course, this is wrong since I'm mixing malloc's free with C++'s new.
17:54 < wstein> It's just a demo.
17:54 < mabshoff> mmmh
```
So the credit should go to him, but I also fixed a second analog problem further down the code.

Without the patch:

```
==22784== LEAK SUMMARY:
==22784==    definitely lost: 794,838 bytes in 65,475 blocks.
==22784==      possibly lost: 350,158 bytes in 953 blocks.
==22784==    still reachable: 137,588,639 bytes in 19,728 blocks.
==22784==         suppressed: 0 bytes in 0 blocks.
```

With the patch:

```
==22993== LEAK SUMMARY:
==22993==    definitely lost: 3,103 bytes in 49 blocks.
==22993==      possibly lost: 349,334 bytes in 931 blocks.
==22993==    still reachable: 137,589,847 bytes in 19,621 blocks.
==22993==         suppressed: 0 bytes in 0 blocks.
```

The test computation finished, but I have no clue if it is correct.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/511





---

archive/issue_comments_002572.json:
```json
{
    "body": "Changing assignee from somebody to @williamstein.",
    "created_at": "2007-08-29T12:08:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/511#issuecomment-2572",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from somebody to @williamstein.



---

archive/issue_comments_002573.json:
```json
{
    "body": "Hmm, trac refused to accept by patch. So here is a link:\n\nhttp://fsmath.mathematik.uni-dortmund.de/~mabshoff/patches/sage-2.8.3alpha2-fix-ntl-memleak-in-__repr__.patch\n\n\nCheers,\n\nMichael",
    "created_at": "2007-08-29T12:08:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/511#issuecomment-2573",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hmm, trac refused to accept by patch. So here is a link:

http://fsmath.mathematik.uni-dortmund.de/~mabshoff/patches/sage-2.8.3alpha2-fix-ntl-memleak-in-__repr__.patch


Cheers,

Michael



---

archive/issue_comments_002574.json:
```json
{
    "body": "Trac still refuses attachments, so here is the patch for the c_lib which 'calloc's (instead of 'new') the memory mabshoff's patch 'free's\nhttp://sage.math.washington.edu/home/malb/ntl_wrap_calloc.patch",
    "created_at": "2007-08-29T13:30:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/511#issuecomment-2574",
    "user": "https://github.com/malb"
}
```

Trac still refuses attachments, so here is the patch for the c_lib which 'calloc's (instead of 'new') the memory mabshoff's patch 'free's
http://sage.math.washington.edu/home/malb/ntl_wrap_calloc.patch



---

archive/issue_comments_002575.json:
```json
{
    "body": "If #411 goes in this might or might not be needed any more.\n\nCheers,\n\nMichael",
    "created_at": "2007-08-29T20:35:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/511#issuecomment-2575",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

If #411 goes in this might or might not be needed any more.

Cheers,

Michael



---

archive/issue_comments_002576.json:
```json
{
    "body": "Fixed in sage-2.8.3.",
    "created_at": "2007-08-30T02:11:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/511#issuecomment-2576",
    "user": "https://github.com/williamstein"
}
```

Fixed in sage-2.8.3.



---

archive/issue_comments_002577.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-30T02:11:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/511#issuecomment-2577",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_001307.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-08-30T02:11:41Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/511",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/511#event-1307"
}
```
