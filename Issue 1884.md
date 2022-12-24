# Issue 1884: memory leak in real numbers

archive/issues_001884.json:
```json
{
    "body": "Assignee: mabshoff\n\nThis leaks like a sieve in 2.10:\n\n\n```\nt = 0.0\nwhile True:\n    t = t * 2.0\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1884\n\n",
    "created_at": "2008-01-22T02:53:16Z",
    "labels": [
        "memleak",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "memory leak in real numbers",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1884",
    "user": "dmharvey"
}
```
Assignee: mabshoff

This leaks like a sieve in 2.10:


```
t = 0.0
while True:
    t = t * 2.0
```



Issue created by migration from https://trac.sagemath.org/ticket/1884





---

archive/issue_comments_011927.json:
```json
{
    "body": "I ran 10000 loops with 2.9.3 and I got:\n\n```\n==5050== 2,807,000 bytes in 10,025 blocks are still reachable in loss record 8,029 of 8,033\n==5050==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)\n==5050==    by 0x4B0079: _PyObject_GC_Malloc (gcmodule.c:1321)\n==5050==    by 0x4B01AC: _PyObject_GC_New (gcmodule.c:1343)\n==5050==    by 0x441339: PyDict_New (dictobject.c:216)\n==5050==    by 0x964A11F: __pyx_pf_4sage_9structure_6parent_6Parent___init__ (parent.c:404)\n==5050==    by 0x453A9B: wrap_init (typeobject.c:3962)\n==5050==    by 0x415542: PyObject_Call (abstract.c:1860)\n==5050==    by 0x47C480: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==5050==    by 0x4CAF84: wrapperdescr_call (descrobject.c:304)\n==5050==    by 0x415542: PyObject_Call (abstract.c:1860)\n==5050==    by 0x47C480: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==5050==    by 0x9537A94: __pyx_pf_4sage_9structure_11parent_base_14ParentWithBase___init__ (parent_base.c:388)\n==5050==\n==5050== 2,807,560 bytes in 10,027 blocks are still reachable in loss record 8,030 of 8,033\n==5050==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)\n==5050==    by 0x4B0079: _PyObject_GC_Malloc (gcmodule.c:1321)\n==5050==    by 0x4B01AC: _PyObject_GC_New (gcmodule.c:1343)\n==5050==    by 0x441339: PyDict_New (dictobject.c:216)\n==5050==    by 0x964A873: __pyx_pf_4sage_9structure_6parent_6Parent___init__ (parent.c:553)\n==5050==    by 0x453A9B: wrap_init (typeobject.c:3962)\n==5050==    by 0x415542: PyObject_Call (abstract.c:1860)\n==5050==    by 0x47C480: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==5050==    by 0x4CAF84: wrapperdescr_call (descrobject.c:304)\n==5050==    by 0x415542: PyObject_Call (abstract.c:1860)\n==5050==    by 0x47C480: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==5050==    by 0x9537A94: __pyx_pf_4sage_9structure_11parent_base_14ParentWithBase___init__ (parent_base.c:388)\n==5050==\n==5050==\n==5050== 2,812,600 bytes in 10,045 blocks are still reachable in loss record 8,031 of 8,033\n==5050==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)\n==5050==    by 0x4B0079: _PyObject_GC_Malloc (gcmodule.c:1321)\n==5050==    by 0x4B01AC: _PyObject_GC_New (gcmodule.c:1343)\n==5050==    by 0x441339: PyDict_New (dictobject.c:216)\n==5050==    by 0x98C03B6: __pyx_pf_4sage_9structure_11parent_gens_14ParentWithGens___init__ (parent_gens.c:1552)\n==5050==    by 0x453A9B: wrap_init (typeobject.c:3962)\n==5050==    by 0x415542: PyObject_Call (abstract.c:1860)\n==5050==    by 0x47C480: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==5050==    by 0x4CAF84: wrapperdescr_call (descrobject.c:304)\n==5050==    by 0x415542: PyObject_Call (abstract.c:1860)\n==5050==    by 0x47C480: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==5050==    by 0xBD5AF19: __pyx_pf_4sage_5rings_9real_mpfr_9RealField___init__ (real_mpfr.c:2798)\n```\n\n\nI am running the same code under omega now, but that might take an hour or two.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-22T03:25:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1884#issuecomment-11927",
    "user": "mabshoff"
}
```

I ran 10000 loops with 2.9.3 and I got:

```
==5050== 2,807,000 bytes in 10,025 blocks are still reachable in loss record 8,029 of 8,033
==5050==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)
==5050==    by 0x4B0079: _PyObject_GC_Malloc (gcmodule.c:1321)
==5050==    by 0x4B01AC: _PyObject_GC_New (gcmodule.c:1343)
==5050==    by 0x441339: PyDict_New (dictobject.c:216)
==5050==    by 0x964A11F: __pyx_pf_4sage_9structure_6parent_6Parent___init__ (parent.c:404)
==5050==    by 0x453A9B: wrap_init (typeobject.c:3962)
==5050==    by 0x415542: PyObject_Call (abstract.c:1860)
==5050==    by 0x47C480: PyEval_CallObjectWithKeywords (ceval.c:3433)
==5050==    by 0x4CAF84: wrapperdescr_call (descrobject.c:304)
==5050==    by 0x415542: PyObject_Call (abstract.c:1860)
==5050==    by 0x47C480: PyEval_CallObjectWithKeywords (ceval.c:3433)
==5050==    by 0x9537A94: __pyx_pf_4sage_9structure_11parent_base_14ParentWithBase___init__ (parent_base.c:388)
==5050==
==5050== 2,807,560 bytes in 10,027 blocks are still reachable in loss record 8,030 of 8,033
==5050==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)
==5050==    by 0x4B0079: _PyObject_GC_Malloc (gcmodule.c:1321)
==5050==    by 0x4B01AC: _PyObject_GC_New (gcmodule.c:1343)
==5050==    by 0x441339: PyDict_New (dictobject.c:216)
==5050==    by 0x964A873: __pyx_pf_4sage_9structure_6parent_6Parent___init__ (parent.c:553)
==5050==    by 0x453A9B: wrap_init (typeobject.c:3962)
==5050==    by 0x415542: PyObject_Call (abstract.c:1860)
==5050==    by 0x47C480: PyEval_CallObjectWithKeywords (ceval.c:3433)
==5050==    by 0x4CAF84: wrapperdescr_call (descrobject.c:304)
==5050==    by 0x415542: PyObject_Call (abstract.c:1860)
==5050==    by 0x47C480: PyEval_CallObjectWithKeywords (ceval.c:3433)
==5050==    by 0x9537A94: __pyx_pf_4sage_9structure_11parent_base_14ParentWithBase___init__ (parent_base.c:388)
==5050==
==5050==
==5050== 2,812,600 bytes in 10,045 blocks are still reachable in loss record 8,031 of 8,033
==5050==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)
==5050==    by 0x4B0079: _PyObject_GC_Malloc (gcmodule.c:1321)
==5050==    by 0x4B01AC: _PyObject_GC_New (gcmodule.c:1343)
==5050==    by 0x441339: PyDict_New (dictobject.c:216)
==5050==    by 0x98C03B6: __pyx_pf_4sage_9structure_11parent_gens_14ParentWithGens___init__ (parent_gens.c:1552)
==5050==    by 0x453A9B: wrap_init (typeobject.c:3962)
==5050==    by 0x415542: PyObject_Call (abstract.c:1860)
==5050==    by 0x47C480: PyEval_CallObjectWithKeywords (ceval.c:3433)
==5050==    by 0x4CAF84: wrapperdescr_call (descrobject.c:304)
==5050==    by 0x415542: PyObject_Call (abstract.c:1860)
==5050==    by 0x47C480: PyEval_CallObjectWithKeywords (ceval.c:3433)
==5050==    by 0xBD5AF19: __pyx_pf_4sage_5rings_9real_mpfr_9RealField___init__ (real_mpfr.c:2798)
```


I am running the same code under omega now, but that might take an hour or two.

Cheers,

Michael



---

archive/issue_comments_011928.json:
```json
{
    "body": "Hmm, this might be the real culprit:\n\n```\n==5050== 800,000 bytes in 10,000 blocks are still reachable in loss record 8,010 of 8,033\n==5050==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)\n==5050==    by 0x4B0079: _PyObject_GC_Malloc (gcmodule.c:1321)\n==5050==    by 0x454C29: PyType_GenericAlloc (typeobject.c:454)\n==5050==    by 0x9762350: __pyx_tp_new_4sage_9structure_7element_Element (element.c:22358)\n==5050==    by 0x9D27AF0: __pyx_tp_new_4sage_10categories_8morphism_Morphism (morphism.c:4733)\n==5050==    by 0x9D27F30: __pyx_tp_new_4sage_10categories_8morphism_CallMorphism (morphism.c:5232)\n==5050==    by 0x458D92: type_call (typeobject.c:422)\n==5050==    by 0x415542: PyObject_Call (abstract.c:1860)\n==5050==    by 0x47C480: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==5050==    by 0x9647DE9: __pyx_f_4sage_9structure_6parent_6Parent_coerce_map_from_c (parent.c:1015)\n==5050==    by 0x99E25B4: __pyx_f_4sage_9structure_6coerce_24CoercionModel_cache_maps_discover_coercion_c (coerce.c:7583)\n==5050==    by 0x99DBBD5: __pyx_f_4sage_9structure_6coerce_24CoercionModel_cache_maps_coercion_maps_c (coerce.c:7350)\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-01-22T03:29:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1884#issuecomment-11928",
    "user": "mabshoff"
}
```

Hmm, this might be the real culprit:

```
==5050== 800,000 bytes in 10,000 blocks are still reachable in loss record 8,010 of 8,033
==5050==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)
==5050==    by 0x4B0079: _PyObject_GC_Malloc (gcmodule.c:1321)
==5050==    by 0x454C29: PyType_GenericAlloc (typeobject.c:454)
==5050==    by 0x9762350: __pyx_tp_new_4sage_9structure_7element_Element (element.c:22358)
==5050==    by 0x9D27AF0: __pyx_tp_new_4sage_10categories_8morphism_Morphism (morphism.c:4733)
==5050==    by 0x9D27F30: __pyx_tp_new_4sage_10categories_8morphism_CallMorphism (morphism.c:5232)
==5050==    by 0x458D92: type_call (typeobject.c:422)
==5050==    by 0x415542: PyObject_Call (abstract.c:1860)
==5050==    by 0x47C480: PyEval_CallObjectWithKeywords (ceval.c:3433)
==5050==    by 0x9647DE9: __pyx_f_4sage_9structure_6parent_6Parent_coerce_map_from_c (parent.c:1015)
==5050==    by 0x99E25B4: __pyx_f_4sage_9structure_6coerce_24CoercionModel_cache_maps_discover_coercion_c (coerce.c:7583)
==5050==    by 0x99DBBD5: __pyx_f_4sage_9structure_6coerce_24CoercionModel_cache_maps_coercion_maps_c (coerce.c:7350)
```


Cheers,

Michael



---

archive/issue_comments_011929.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-01-23T09:27:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1884#issuecomment-11929",
    "user": "mabshoff"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_011930.json:
```json
{
    "body": "I'll try to look into this today. Is the above from omega, or if not what did that tell you?",
    "created_at": "2008-01-23T18:19:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1884#issuecomment-11930",
    "user": "@robertwb"
}
```

I'll try to look into this today. Is the above from omega, or if not what did that tell you?



---

archive/issue_comments_011931.json:
```json
{
    "body": "Hi Robert,\n\nthe above is from memcheck. I hadn't had time to try the same under omega, but since the above is \"still reachable\" memory omega wouldn't help in that case anyway since it only prints out messages about \"definitely lost\" memory. There were a variety of places in the code where about 10.000 buffers were lost, some of which are on the first comment. Only later I did discover that there was one buffer with the exact number of 10,000 losses, so it became my prime candidate. The complere log (6.8MB) is at \n\nhttp://sage.math.washington.edu/home/mabshoff/sage-memcheck-1884.log\n\nI should be in IRC if you want to discuss this issue or any input from my end. Note that the memcheck log was created with 2.9.3, so in 2.10 the number might be off.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-23T21:27:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1884#issuecomment-11931",
    "user": "mabshoff"
}
```

Hi Robert,

the above is from memcheck. I hadn't had time to try the same under omega, but since the above is "still reachable" memory omega wouldn't help in that case anyway since it only prints out messages about "definitely lost" memory. There were a variety of places in the code where about 10.000 buffers were lost, some of which are on the first comment. Only later I did discover that there was one buffer with the exact number of 10,000 losses, so it became my prime candidate. The complere log (6.8MB) is at 

http://sage.math.washington.edu/home/mabshoff/sage-memcheck-1884.log

I should be in IRC if you want to discuss this issue or any input from my end. Note that the memcheck log was created with 2.9.3, so in 2.10 the number might be off.

Cheers,

Michael



---

archive/issue_comments_011932.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-29T19:44:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1884#issuecomment-11932",
    "user": "@robertwb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_011933.json:
```json
{
    "body": "Changing assignee from mabshoff to @robertwb.",
    "created_at": "2008-01-29T19:44:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1884#issuecomment-11933",
    "user": "@robertwb"
}
```

Changing assignee from mabshoff to @robertwb.



---

archive/issue_comments_011934.json:
```json
{
    "body": "This is due to non-uniqueness of real fields. \n\n\n```\nsage: parent(2.0) == parent(2.0)\nTrue\nsage: parent(2.0) is parent(2.0)\nFalse\n```\n\n\nIt's making a new parent for the constant in the loop, and adding it to the coercion model. I will fix this now.",
    "created_at": "2008-01-29T19:44:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1884#issuecomment-11934",
    "user": "@robertwb"
}
```

This is due to non-uniqueness of real fields. 


```
sage: parent(2.0) == parent(2.0)
True
sage: parent(2.0) is parent(2.0)
False
```


It's making a new parent for the constant in the loop, and adding it to the coercion model. I will fix this now.



---

archive/issue_comments_011935.json:
```json
{
    "body": "Attachment [1884-real-memleak.diff](tarball://root/attachments/some-uuid/ticket1884/1884-real-memleak.diff) by @robertwb created at 2008-01-29 20:52:32",
    "created_at": "2008-01-29T20:52:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1884#issuecomment-11935",
    "user": "@robertwb"
}
```

Attachment [1884-real-memleak.diff](tarball://root/attachments/some-uuid/ticket1884/1884-real-memleak.diff) by @robertwb created at 2008-01-29 20:52:32



---

archive/issue_comments_011936.json:
```json
{
    "body": "Attachment [1884-real-memleak2.diff](tarball://root/attachments/some-uuid/ticket1884/1884-real-memleak2.diff) by @robertwb created at 2008-01-29 20:53:04",
    "created_at": "2008-01-29T20:53:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1884#issuecomment-11936",
    "user": "@robertwb"
}
```

Attachment [1884-real-memleak2.diff](tarball://root/attachments/some-uuid/ticket1884/1884-real-memleak2.diff) by @robertwb created at 2008-01-29 20:53:04



---

archive/issue_comments_011937.json:
```json
{
    "body": "The first patch fixes the issue (with a doctest), and the second ensures uniqueness in a couple of places that imported RealField directly.",
    "created_at": "2008-01-29T20:54:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1884#issuecomment-11937",
    "user": "@robertwb"
}
```

The first patch fixes the issue (with a doctest), and the second ensures uniqueness in a couple of places that imported RealField directly.



---

archive/issue_comments_011938.json:
```json
{
    "body": "Ok, after applying both patches I get \n\n```\nExiting SAGE (CPU time 0m0.00s, Wall time 0m1.00s).\n*** glibc detected *** double free or corruption (out): 0x0000000000ec69a0 ***\n```\n\non exit each time I start Sage. The valgrind log points to #1337.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-30T04:25:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1884#issuecomment-11938",
    "user": "mabshoff"
}
```

Ok, after applying both patches I get 

```
Exiting SAGE (CPU time 0m0.00s, Wall time 0m1.00s).
*** glibc detected *** double free or corruption (out): 0x0000000000ec69a0 ***
```

on exit each time I start Sage. The valgrind log points to #1337.

Cheers,

Michael



---

archive/issue_comments_011939.json:
```json
{
    "body": "I have no idea--this must be exposing some previously undetected bug. I don't allocate or free anything here, in fact most of the patch is Python code...",
    "created_at": "2008-01-30T06:05:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1884#issuecomment-11939",
    "user": "@robertwb"
}
```

I have no idea--this must be exposing some previously undetected bug. I don't allocate or free anything here, in fact most of the patch is Python code...



---

archive/issue_comments_011940.json:
```json
{
    "body": "Replying to [comment:10 robertwb]:\n> I have no idea--this must be exposing some previously undetected bug. I don't allocate or free anything here, in fact most of the patch is Python code...\n\nI agree that the bug is not in your patches, but it is exposed by the code. I have attempted to track this issue, i.e. #1337 before, but failed. Maybe we can sit down at SD7 and see if we can come up with a solution.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-30T06:08:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1884#issuecomment-11940",
    "user": "mabshoff"
}
```

Replying to [comment:10 robertwb]:
> I have no idea--this must be exposing some previously undetected bug. I don't allocate or free anything here, in fact most of the patch is Python code...

I agree that the bug is not in your patches, but it is exposed by the code. I have attempted to track this issue, i.e. #1337 before, but failed. Maybe we can sit down at SD7 and see if we can come up with a solution.

Cheers,

Michael



---

archive/issue_comments_011941.json:
```json
{
    "body": "It's certainly an elusive bug. OK, I'll spend some time on it with you at SD7.",
    "created_at": "2008-01-30T09:32:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1884#issuecomment-11941",
    "user": "@robertwb"
}
```

It's certainly an elusive bug. OK, I'll spend some time on it with you at SD7.



---

archive/issue_comments_011942.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-09T05:08:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1884#issuecomment-11942",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_011943.json:
```json
{
    "body": "Merged both patches in Sage 2.10.3.rc3",
    "created_at": "2008-03-09T05:08:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1884#issuecomment-11943",
    "user": "mabshoff"
}
```

Merged both patches in Sage 2.10.3.rc3
