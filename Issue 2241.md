# Issue 2241: Leak in totallyreal_rel.py

archive/issues_002241.json:
```json
{
    "body": "Assignee: @craigcitro\n\nThe ticket is different than #2239. \n\nThe issue seems to be in the coercion code somewhere:\n\n```\n==25102== 164,280 bytes in 4,107 blocks are definitely lost in loss record 8,413 of 8,436\n==25102==    at 0x4A1BDEB: malloc (vg_replace_malloc.c:207)\n==25102==    by 0xC90D42B: __pyx_f_4sage_5rings_11real_double_fast_tp_new (real_double.c:10022)\n==25102==    by 0xC9065CA: __pyx_f_4sage_5rings_11real_double_17RealDoubleElement__mul_c_impl (real_double.c:5041)\n==25102==    by 0xA08ECD3: __pyx_pf_4sage_9structure_7element_11RingElement___mul__ (element.c:16691)\n==25102==    by 0x41580C: binary_op1 (abstract.c:398)\n==25102==    by 0x418F47: PyNumber_Multiply (abstract.c:669)\n==25102==    by 0x6D9512D: op_mul (operator.c:73)\n==25102==    by 0x415542: PyObject_Call (abstract.c:1860)\n==25102==    by 0x47CBE0: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==25102==    by 0xA2F21BF: __pyx_f_4sage_9structure_6coerce_24CoercionModel_cache_maps_bin_op_c (coerce.c:5155)\n==25102==    by 0xA08EE41: __pyx_pf_4sage_9structure_7element_11RingElement___mul__ (element.c:8882)\n==25102==    by 0x415861: binary_op1 (abstract.c:404)\n```\n\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/2241\n\n",
    "created_at": "2008-02-21T00:36:17Z",
    "labels": [
        "component: memleak",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "Leak in totallyreal_rel.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2241",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @craigcitro

The ticket is different than #2239. 

The issue seems to be in the coercion code somewhere:

```
==25102== 164,280 bytes in 4,107 blocks are definitely lost in loss record 8,413 of 8,436
==25102==    at 0x4A1BDEB: malloc (vg_replace_malloc.c:207)
==25102==    by 0xC90D42B: __pyx_f_4sage_5rings_11real_double_fast_tp_new (real_double.c:10022)
==25102==    by 0xC9065CA: __pyx_f_4sage_5rings_11real_double_17RealDoubleElement__mul_c_impl (real_double.c:5041)
==25102==    by 0xA08ECD3: __pyx_pf_4sage_9structure_7element_11RingElement___mul__ (element.c:16691)
==25102==    by 0x41580C: binary_op1 (abstract.c:398)
==25102==    by 0x418F47: PyNumber_Multiply (abstract.c:669)
==25102==    by 0x6D9512D: op_mul (operator.c:73)
==25102==    by 0x415542: PyObject_Call (abstract.c:1860)
==25102==    by 0x47CBE0: PyEval_CallObjectWithKeywords (ceval.c:3433)
==25102==    by 0xA2F21BF: __pyx_f_4sage_9structure_6coerce_24CoercionModel_cache_maps_bin_op_c (coerce.c:5155)
==25102==    by 0xA08EE41: __pyx_pf_4sage_9structure_7element_11RingElement___mul__ (element.c:8882)
==25102==    by 0x415861: binary_op1 (abstract.c:404)
```


Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/2241





---

archive/issue_comments_014818.json:
```json
{
    "body": "I don't know how to read this.  Will a similar approach as in #2239 fix this memleak?  (In totallyreal_rel.py, numpy.roots is called on an array of floats instead of ints...)\n\nJV",
    "created_at": "2008-02-29T20:07:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2241#issuecomment-14818",
    "user": "https://github.com/jvoight"
}
```

I don't know how to read this.  Will a similar approach as in #2239 fix this memleak?  (In totallyreal_rel.py, numpy.roots is called on an array of floats instead of ints...)

JV



---

archive/issue_events_002411.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-15T04:43:31Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2241",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2241#event-2411"
}
```



---

archive/issue_comments_014819.json:
```json
{
    "body": "This issue has been fixed some time prior to Sage 3.1.2.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-15T04:43:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2241#issuecomment-14819",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This issue has been fixed some time prior to Sage 3.1.2.

Cheers,

Michael



---

archive/issue_comments_014820.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-15T04:43:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2241#issuecomment-14820",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
