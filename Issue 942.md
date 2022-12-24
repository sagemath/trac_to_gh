# Issue 942: still reachable memory in pow_computer's cache

archive/issues_000942.json:
```json
{
    "body": "Assignee: mabshoff\n\nRunning\n\n```\nZp(next_prime(10^50), 10000)\n```\n\nleads to \n\n```\n==12621== 1,038,246,360 bytes in 9,999 blocks are still reachable in loss record 2,030 of 2,031\n==12621==    at 0x4A1BC36: realloc (vg_replace_malloc.c:420)\n==12621==    by 0x5FACD10: __gmpz_realloc (in /tmp/Work-mabshoff/sage-2.8.7-debian64-x86_64-Linux/local/lib/libgmp.so.3.4.1)\n==12621==    by 0x5FAD7E2: __gmpz_set (in /tmp/Work-mabshoff/sage-2.8.7-debian64-x86_64-Linux/local/lib/libgmp.so.3.4.1)\n==12621==    by 0xE4287B4: __pyx_f_py_12pow_computer_17PowComputer_class___init__ (pow_computer.c:2503)\n==12621==    by 0x459220: type_call (typeobject.c:436)\n==12621==    by 0x415522: PyObject_Call (abstract.c:1860)\n==12621==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==12621==    by 0xE426C81: __pyx_f_py_12pow_computer_PowComputer (pow_computer.c:3376)\n==12621==    by 0x483031: PyEval_EvalFrameEx (ceval.c:3564)\n==12621==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n==12621==    by 0x4CE527: function_call (funcobject.c:517)\n==12621==    by 0x415522: PyObject_Call (abstract.c:1860)\n==12621==\n==12621==\n==12621== 1,038,278,736 bytes in 9,999 blocks are still reachable in loss record 2,031 of 2,031\n==12621==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)\n==12621==    by 0x5FA9783: __gmpz_mul (in /tmp/Work-mabshoff/sage-2.8.7-debian64-x86_64-Linux/local/lib/libgmp.so.3.4.1)\n==12621==    by 0xE42887F: __pyx_f_py_12pow_computer_17PowComputer_class___init__ (pow_computer.c:2481)\n==12621==    by 0x459220: type_call (typeobject.c:436)\n==12621==    by 0x415522: PyObject_Call (abstract.c:1860)\n==12621==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==12621==    by 0xE426C81: __pyx_f_py_12pow_computer_PowComputer (pow_computer.c:3376)\n==12621==    by 0x483031: PyEval_EvalFrameEx (ceval.c:3564)\n==12621==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n==12621==    by 0x4CE527: function_call (funcobject.c:517)\n==12621==    by 0x415522: PyObject_Call (abstract.c:1860)\n==12621==    by 0x41BC42: instancemethod_call (classobject.c:2497)\n```\n\nbecause the memory allocated for caches in the init method never gets deallocated.\n\nSee also #941, which exposed the problem with consumption.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/942\n\n",
    "created_at": "2007-10-20T11:22:32Z",
    "labels": [
        "memleak",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.8",
    "title": "still reachable memory in pow_computer's cache",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/942",
    "user": "mabshoff"
}
```
Assignee: mabshoff

Running

```
Zp(next_prime(10^50), 10000)
```

leads to 

```
==12621== 1,038,246,360 bytes in 9,999 blocks are still reachable in loss record 2,030 of 2,031
==12621==    at 0x4A1BC36: realloc (vg_replace_malloc.c:420)
==12621==    by 0x5FACD10: __gmpz_realloc (in /tmp/Work-mabshoff/sage-2.8.7-debian64-x86_64-Linux/local/lib/libgmp.so.3.4.1)
==12621==    by 0x5FAD7E2: __gmpz_set (in /tmp/Work-mabshoff/sage-2.8.7-debian64-x86_64-Linux/local/lib/libgmp.so.3.4.1)
==12621==    by 0xE4287B4: __pyx_f_py_12pow_computer_17PowComputer_class___init__ (pow_computer.c:2503)
==12621==    by 0x459220: type_call (typeobject.c:436)
==12621==    by 0x415522: PyObject_Call (abstract.c:1860)
==12621==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)
==12621==    by 0xE426C81: __pyx_f_py_12pow_computer_PowComputer (pow_computer.c:3376)
==12621==    by 0x483031: PyEval_EvalFrameEx (ceval.c:3564)
==12621==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==12621==    by 0x4CE527: function_call (funcobject.c:517)
==12621==    by 0x415522: PyObject_Call (abstract.c:1860)
==12621==
==12621==
==12621== 1,038,278,736 bytes in 9,999 blocks are still reachable in loss record 2,031 of 2,031
==12621==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)
==12621==    by 0x5FA9783: __gmpz_mul (in /tmp/Work-mabshoff/sage-2.8.7-debian64-x86_64-Linux/local/lib/libgmp.so.3.4.1)
==12621==    by 0xE42887F: __pyx_f_py_12pow_computer_17PowComputer_class___init__ (pow_computer.c:2481)
==12621==    by 0x459220: type_call (typeobject.c:436)
==12621==    by 0x415522: PyObject_Call (abstract.c:1860)
==12621==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)
==12621==    by 0xE426C81: __pyx_f_py_12pow_computer_PowComputer (pow_computer.c:3376)
==12621==    by 0x483031: PyEval_EvalFrameEx (ceval.c:3564)
==12621==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==12621==    by 0x4CE527: function_call (funcobject.c:517)
==12621==    by 0x415522: PyObject_Call (abstract.c:1860)
==12621==    by 0x41BC42: instancemethod_call (classobject.c:2497)
```

because the memory allocated for caches in the init method never gets deallocated.

See also #941, which exposed the problem with consumption.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/942





---

archive/issue_comments_005764.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-20T11:22:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/942#issuecomment-5764",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_005765.json:
```json
{
    "body": "Fixed via #919 by roed.\n\nCheers,\n\nMichael",
    "created_at": "2007-10-20T18:38:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/942#issuecomment-5765",
    "user": "mabshoff"
}
```

Fixed via #919 by roed.

Cheers,

Michael



---

archive/issue_comments_005766.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-20T18:38:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/942#issuecomment-5766",
    "user": "mabshoff"
}
```

Resolution: fixed
