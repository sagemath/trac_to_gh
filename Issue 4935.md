# Issue 4935: is_perfect_power leaks

archive/issues_004935.json:
```json
{
    "body": "Assignee: @robertwb\n\nI discovered this while playing with #4612.\n\nThis is with the old gmp, i.e. not the new eMPIRe, but that also shows roughly the same numbers:\n\n```\nsage: get_memory_usage()\n790.43359375\nsage: time len([a for a in srange(10**5) if not (-a^3).is_perfect_power()])\nCPU times: user 0.27 s, sys: 0.03 s, total: 0.30 s\nWall time: 0.31 s\n24128\nsage: get_memory_usage()\n798.4765625\nsage: time len([a for a in srange(10**6) if not (-a^3).is_perfect_power()])\nCPU times: user 2.84 s, sys: 0.27 s, total: 3.12 s\nWall time: 3.12 s\n241224\nsage: get_memory_usage()\n868.921875\n```\n\n\nValgrinding this didn't turn up anything useful. Thoughts?\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4935\n\n",
    "created_at": "2009-01-04T02:33:12Z",
    "labels": [
        "component: memleak",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "is_perfect_power leaks",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4935",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @robertwb

I discovered this while playing with #4612.

This is with the old gmp, i.e. not the new eMPIRe, but that also shows roughly the same numbers:

```
sage: get_memory_usage()
790.43359375
sage: time len([a for a in srange(10**5) if not (-a^3).is_perfect_power()])
CPU times: user 0.27 s, sys: 0.03 s, total: 0.30 s
Wall time: 0.31 s
24128
sage: get_memory_usage()
798.4765625
sage: time len([a for a in srange(10**6) if not (-a^3).is_perfect_power()])
CPU times: user 2.84 s, sys: 0.27 s, total: 3.12 s
Wall time: 3.12 s
241224
sage: get_memory_usage()
868.921875
```


Valgrinding this didn't turn up anything useful. Thoughts?

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4935





---

archive/issue_comments_037390.json:
```json
{
    "body": "This would almost certainly be a memory leak in mpz_perfect_power_p, as (in this case) (-a^3) is an integer, and the implementation of is_perfect_power is a one-liner.",
    "created_at": "2009-01-04T02:52:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4935#issuecomment-37390",
    "user": "https://github.com/robertwb"
}
```

This would almost certainly be a memory leak in mpz_perfect_power_p, as (in this case) (-a^3) is an integer, and the implementation of is_perfect_power is a one-liner.



---

archive/issue_comments_037391.json:
```json
{
    "body": "Replying to [comment:1 robertwb]:\n> This would almost certainly be a memory leak in mpz_perfect_power_p, as (in this case) (-a^3) is an integer, and the implementation of is_perfect_power is a one-liner. \n\nWell, I did run valgrind on it and nothing showed. I will valgrind some pure C code to make 100% sure it isn't [gmp|mpir]. My guess would be that Cython could be involved, but before I point the finger I should have some data.\n\nIt seems like Cython is the new scape goat taking that role from Coercion :p\n\nCheers,\n\nMichael",
    "created_at": "2009-01-04T02:58:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4935#issuecomment-37391",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:1 robertwb]:
> This would almost certainly be a memory leak in mpz_perfect_power_p, as (in this case) (-a^3) is an integer, and the implementation of is_perfect_power is a one-liner. 

Well, I did run valgrind on it and nothing showed. I will valgrind some pure C code to make 100% sure it isn't [gmp|mpir]. My guess would be that Cython could be involved, but before I point the finger I should have some data.

It seems like Cython is the new scape goat taking that role from Coercion :p

Cheers,

Michael



---

archive/issue_comments_037392.json:
```json
{
    "body": ":)\n\nThe Cython code looks plenty clean though. \n\n\n```\n#define __Pyx_PyBool_FromLong(b) ((b) ? (Py_INCREF(Py_True), Py_True) : (Py_INCREF(Py_False), Py_False))\n\n...\n\nstatic PyObject *__pyx_pf_4sage_5rings_7integer_7Integer_is_perfect_power(PyObject *__pyx_v_self, PyObject *unused) {\n  PyObject *__pyx_r;\n  PyObject *__pyx_1 = 0;\n\n  /* \"/Users/robert/sage/sage-3.1.3/devel/sage-main/sage/rings/integer.pyx\":3002\n *             False\n *         \"\"\"\n *         return mpz_perfect_power_p(self.value)             # <<<<<<<<<<<<<<\n * \n *     def jacobi(self, b):\n */\n  __pyx_1 = __Pyx_PyBool_FromLong(mpz_perfect_power_p(((struct __pyx_obj_4sage_5rings_7integer_Integer *)__pyx_v_self)->value)); if (unlikely(!__pyx_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 3002; __pyx_clineno = __LINE__; goto __pyx_L1_error;}\n  __pyx_r = __pyx_1;\n  __pyx_1 = 0;\n  goto __pyx_L0;\n\n  __pyx_r = Py_None; Py_INCREF(Py_None);\n  goto __pyx_L0;\n  __pyx_L1_error:;\n  Py_XDECREF(__pyx_1);\n  __Pyx_AddTraceback(\"sage.rings.integer.Integer.is_perfect_power\");\n  __pyx_r = NULL;\n  __pyx_L0:;\n  return __pyx_r;\n}\n\n```\n\n\n(Note that much of that gets optimized away at compile time, for example the error branch is never taken).",
    "created_at": "2009-01-04T03:08:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4935#issuecomment-37392",
    "user": "https://github.com/robertwb"
}
```

:)

The Cython code looks plenty clean though. 


```
#define __Pyx_PyBool_FromLong(b) ((b) ? (Py_INCREF(Py_True), Py_True) : (Py_INCREF(Py_False), Py_False))

...

static PyObject *__pyx_pf_4sage_5rings_7integer_7Integer_is_perfect_power(PyObject *__pyx_v_self, PyObject *unused) {
  PyObject *__pyx_r;
  PyObject *__pyx_1 = 0;

  /* "/Users/robert/sage/sage-3.1.3/devel/sage-main/sage/rings/integer.pyx":3002
 *             False
 *         """
 *         return mpz_perfect_power_p(self.value)             # <<<<<<<<<<<<<<
 * 
 *     def jacobi(self, b):
 */
  __pyx_1 = __Pyx_PyBool_FromLong(mpz_perfect_power_p(((struct __pyx_obj_4sage_5rings_7integer_Integer *)__pyx_v_self)->value)); if (unlikely(!__pyx_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 3002; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __pyx_r = __pyx_1;
  __pyx_1 = 0;
  goto __pyx_L0;

  __pyx_r = Py_None; Py_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  Py_XDECREF(__pyx_1);
  __Pyx_AddTraceback("sage.rings.integer.Integer.is_perfect_power");
  __pyx_r = NULL;
  __pyx_L0:;
  return __pyx_r;
}

```


(Note that much of that gets optimized away at compile time, for example the error branch is never taken).



---

archive/issue_comments_037393.json:
```json
{
    "body": "Well, sorry to disappoint you, but t-perfpow.c from very recent mpir-svn doesn't leak:\n\n```\ngmp-mpir-svn1523/src/tests/mpz/.libs$ valgrind --tool=memcheck --leak-resolution=high ./t-perfpow\n==31616== Memcheck, a memory error detector.\n==31616== Copyright (C) 2002-2007, and GNU GPL'd, by Julian Seward et al.\n==31616== Using LibVEX rev 1854, a library for dynamic binary translation.\n==31616== Copyright (C) 2004-2007, and GNU GPL'd, by OpenWorks LLP.\n==31616== Using valgrind-3.3.1, a dynamic binary instrumentation framework.\n==31616== Copyright (C) 2000-2007, and GNU GPL'd, by Julian Seward et al.\n==31616== For more details, rerun with: -v\n==31616== \n==31616== \n==31616== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 3 from 1)\n==31616== malloc/free: in use at exit: 0 bytes in 0 blocks.\n==31616== malloc/free: 375,348 allocs, 375,348 frees, 7,978,732 bytes allocated.\n==31616== For counts of detected errors, rerun with: -v\n==31616== All heap blocks were freed -- no leaks are possible.\n```\n\nSo I am starting to blame not-mpir :)\n\nCheers,\n\nMichael",
    "created_at": "2009-01-04T04:03:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4935#issuecomment-37393",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Well, sorry to disappoint you, but t-perfpow.c from very recent mpir-svn doesn't leak:

```
gmp-mpir-svn1523/src/tests/mpz/.libs$ valgrind --tool=memcheck --leak-resolution=high ./t-perfpow
==31616== Memcheck, a memory error detector.
==31616== Copyright (C) 2002-2007, and GNU GPL'd, by Julian Seward et al.
==31616== Using LibVEX rev 1854, a library for dynamic binary translation.
==31616== Copyright (C) 2004-2007, and GNU GPL'd, by OpenWorks LLP.
==31616== Using valgrind-3.3.1, a dynamic binary instrumentation framework.
==31616== Copyright (C) 2000-2007, and GNU GPL'd, by Julian Seward et al.
==31616== For more details, rerun with: -v
==31616== 
==31616== 
==31616== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 3 from 1)
==31616== malloc/free: in use at exit: 0 bytes in 0 blocks.
==31616== malloc/free: 375,348 allocs, 375,348 frees, 7,978,732 bytes allocated.
==31616== For counts of detected errors, rerun with: -v
==31616== All heap blocks were freed -- no leaks are possible.
```

So I am starting to blame not-mpir :)

Cheers,

Michael



---

archive/issue_comments_037394.json:
```json
{
    "body": "Hmm... perhaps it's just the integer pool filling up? \n\n\n```\nsage: get_memory_usage()\n'415M'\nsage: time len([a for a in srange(10**6) if not (-a^3).is_perfect_power()])\nCPU times: user 5.68 s, sys: 1.01 s, total: 6.69 s\nWall time: 9.47 s\n241224\nsage: get_memory_usage()\n'431M'\nsage: time len([a for a in srange(10**6) if not (-a^3).is_perfect_power()])\nCPU times: user 5.55 s, sys: 0.90 s, total: 6.45 s\nWall time: 6.53 s\n241224\nsage: get_memory_usage()\n'431M'\nsage: time len([a for a in srange(10**6) if not (-a^3).is_perfect_power()])\nCPU times: user 5.58 s, sys: 0.92 s, total: 6.50 s\nWall time: 6.58 s\n241224\nsage: get_memory_usage()\n'431M'\n```\n\n\nAnd a fresh start\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nLoading Sage library. Current Mercurial branch is: bugs\nsage: get_memory_usage()\n'415M'\nsage: time len(srange(10**6))\nCPU times: user 0.40 s, sys: 0.16 s, total: 0.56 s\nWall time: 0.57 s\n1000000\nsage: get_memory_usage()\n'431M'\n```\n\n| Sage Version 3.2.2, Release Date: 2008-12-18                       |\n| Type notebook() for the GUI, and license() for information.        |\nSo it's something in srange or the integer pool or something... Or the fact that the large number of objects that all get allocated at the same time enlarge the heap (and it never gives it back). \n\n\n```\nsage: get_memory_usage()\n'415M'\nsage: len(ZZ.range(10^6))\n1000000\nsage: get_memory_usage()\n'431M'\n```\n\n\nAlso\n\n\n```\nsage: get_memory_usage()\n'415M'\nsage: time len([True for a in (1..10**6) if not (-a^3).is_perfect_power()])\nCPU times: user 9.90 s, sys: 0.96 s, total: 10.86 s\nWall time: 10.98 s\n241225\nsage: get_memory_usage()\n'415M'\n```\n\n\nshows that is_perfect_power is clean, so I think it's just a heap with a million live elements that doesn't shrink back down when the list is freed.",
    "created_at": "2009-01-04T04:42:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4935#issuecomment-37394",
    "user": "https://github.com/robertwb"
}
```

Hmm... perhaps it's just the integer pool filling up? 


```
sage: get_memory_usage()
'415M'
sage: time len([a for a in srange(10**6) if not (-a^3).is_perfect_power()])
CPU times: user 5.68 s, sys: 1.01 s, total: 6.69 s
Wall time: 9.47 s
241224
sage: get_memory_usage()
'431M'
sage: time len([a for a in srange(10**6) if not (-a^3).is_perfect_power()])
CPU times: user 5.55 s, sys: 0.90 s, total: 6.45 s
Wall time: 6.53 s
241224
sage: get_memory_usage()
'431M'
sage: time len([a for a in srange(10**6) if not (-a^3).is_perfect_power()])
CPU times: user 5.58 s, sys: 0.92 s, total: 6.50 s
Wall time: 6.58 s
241224
sage: get_memory_usage()
'431M'
```


And a fresh start


```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: bugs
sage: get_memory_usage()
'415M'
sage: time len(srange(10**6))
CPU times: user 0.40 s, sys: 0.16 s, total: 0.56 s
Wall time: 0.57 s
1000000
sage: get_memory_usage()
'431M'
```

| Sage Version 3.2.2, Release Date: 2008-12-18                       |
| Type notebook() for the GUI, and license() for information.        |
So it's something in srange or the integer pool or something... Or the fact that the large number of objects that all get allocated at the same time enlarge the heap (and it never gives it back). 


```
sage: get_memory_usage()
'415M'
sage: len(ZZ.range(10^6))
1000000
sage: get_memory_usage()
'431M'
```


Also


```
sage: get_memory_usage()
'415M'
sage: time len([True for a in (1..10**6) if not (-a^3).is_perfect_power()])
CPU times: user 9.90 s, sys: 0.96 s, total: 10.86 s
Wall time: 10.98 s
241225
sage: get_memory_usage()
'415M'
```


shows that is_perfect_power is clean, so I think it's just a heap with a million live elements that doesn't shrink back down when the list is freed.



---

archive/issue_comments_037395.json:
```json
{
    "body": "Ok, but isn't the integer pool too aggressive here or am I just not getting the idea here? \n\nTo this day I do not understand why we have to change the GMP allocator to use Python memory since if we used C heap all that memory would be returned to the system.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-04T04:49:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4935#issuecomment-37395",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ok, but isn't the integer pool too aggressive here or am I just not getting the idea here? 

To this day I do not understand why we have to change the GMP allocator to use Python memory since if we used C heap all that memory would be returned to the system.

Cheers,

Michael



---

archive/issue_comments_037396.json:
```json
{
    "body": "No, I don't think this has anything to do with pools or the gmp allocator. \n\n\n```\nsage: get_memory_usage()\n'415M'\nsage: len(range(10^6))\n1000000\nsage: get_memory_usage()\n'423M'\nsage: len([float(a) for a in range(10^6)])\n1000000\nsage: get_memory_usage()\n'439M'\nsage: len(range(10^7))\n10000000\nsage: get_memory_usage()\n'552M'\n```\n\n\n(Note that int objects have a smaller memory footprint than Integers).\n\nMy understanding is that when a new, small, object is allocated, the python memory manager tries to return an already-allocated chunk of the right size out of the heap. If there isn't one, it needs to grow the heap. The \"leaking\" examples all construct huge lists, so the heap grows to the size of the whole list. When objects are freed, the memory goes back to the heap, but doesn't get freed (just like the integer pool idea). Usually this makes sense, as thousands of ephemeral Python objects are used and collected all the time, and usually the number of objects grows over time. In our case, if we make another huge list, the memory is sitting there pre-allocated just waiting to be used. \n\nLarge (>256 bytes?) allocations are deferred directly to malloc, as are user-requested and external library ones, so this kind of memory does get reclaimed immediately.",
    "created_at": "2009-01-04T05:13:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4935#issuecomment-37396",
    "user": "https://github.com/robertwb"
}
```

No, I don't think this has anything to do with pools or the gmp allocator. 


```
sage: get_memory_usage()
'415M'
sage: len(range(10^6))
1000000
sage: get_memory_usage()
'423M'
sage: len([float(a) for a in range(10^6)])
1000000
sage: get_memory_usage()
'439M'
sage: len(range(10^7))
10000000
sage: get_memory_usage()
'552M'
```


(Note that int objects have a smaller memory footprint than Integers).

My understanding is that when a new, small, object is allocated, the python memory manager tries to return an already-allocated chunk of the right size out of the heap. If there isn't one, it needs to grow the heap. The "leaking" examples all construct huge lists, so the heap grows to the size of the whole list. When objects are freed, the memory goes back to the heap, but doesn't get freed (just like the integer pool idea). Usually this makes sense, as thousands of ephemeral Python objects are used and collected all the time, and usually the number of objects grows over time. In our case, if we make another huge list, the memory is sitting there pre-allocated just waiting to be used. 

Large (>256 bytes?) allocations are deferred directly to malloc, as are user-requested and external library ones, so this kind of memory does get reclaimed immediately.



---

archive/issue_comments_037397.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-01-04T19:38:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4935#issuecomment-37397",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: invalid



---

archive/issue_comments_037398.json:
```json
{
    "body": "Ok, invalid then. Sorry got the noise :(\n\nI will use iterators for testing then in the future.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-04T19:38:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4935#issuecomment-37398",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ok, invalid then. Sorry got the noise :(

I will use iterators for testing then in the future.

Cheers,

Michael



---

archive/issue_events_005178.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-01-04T19:38:56Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4935",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4935#event-5178"
}
```
