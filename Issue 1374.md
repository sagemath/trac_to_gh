# Issue 1374: segfault in coercion with matrices and ints

archive/issues_001374.json:
```json
{
    "body": "Assignee: somebody\n\nThis is the bug that was causing #1231; the fix there was easy, but as cwitty points out, the underlying bug is still there. It's something specifically to do with an entry becoming 0 in a matrix. I haven't looked into this at all; it's probably easy pickings for someone who knows the coercion code.\n\nHere's a sample session:\n\n\n```\nsage: M = MatrixSpace(GF(5),2,2)\n\nsage: A = M([1,0,0,1])\n\nsage: A - int(-1)\n \n[2 0]\n[0 2]\n\nsage: B = M([4,0,0,1])\n\nsage: B - int(-1)\n\n\n------------------------------------------------------------\nUnhandled SIGBUS: A bus error occured in SAGE.\nThis probably occured because a *compiled* component\nof SAGE has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run SAGE under gdb with 'sage -gdb' to debug this.\nSAGE will now terminate (sorry).\n------------------------------------------------------------\n\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1374\n\n",
    "created_at": "2007-12-02T19:23:51Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "segfault in coercion with matrices and ints",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1374",
    "user": "craigcitro"
}
```
Assignee: somebody

This is the bug that was causing #1231; the fix there was easy, but as cwitty points out, the underlying bug is still there. It's something specifically to do with an entry becoming 0 in a matrix. I haven't looked into this at all; it's probably easy pickings for someone who knows the coercion code.

Here's a sample session:


```
sage: M = MatrixSpace(GF(5),2,2)

sage: A = M([1,0,0,1])

sage: A - int(-1)
 
[2 0]
[0 2]

sage: B = M([4,0,0,1])

sage: B - int(-1)


------------------------------------------------------------
Unhandled SIGBUS: A bus error occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------


```


Issue created by migration from https://trac.sagemath.org/ticket/1374





---

archive/issue_comments_008811.json:
```json
{
    "body": "Changing assignee from somebody to robertwb.",
    "created_at": "2007-12-02T19:26:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1374#issuecomment-8811",
    "user": "craigcitro"
}
```

Changing assignee from somebody to robertwb.



---

archive/issue_comments_008812.json:
```json
{
    "body": "Changing component from basic arithmetic to coercion.",
    "created_at": "2007-12-02T19:26:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1374#issuecomment-8812",
    "user": "craigcitro"
}
```

Changing component from basic arithmetic to coercion.



---

archive/issue_comments_008813.json:
```json
{
    "body": "First obvious thing to do (on sage.math):\n\n\n```\nsage: matrix(GF(5), 2, [4,0,0,1]) - int(-1)\n\nProgram received signal SIGSEGV, Segmentation fault.\n[Switching to Thread 47703056093024 (LWP 5657)]\n__pyx_f_4sage_5rings_11integer_mod_15NativeIntStruct_lookup (__pyx_v_self=0x2b62cd298e30, __pyx_v_value=5)\n    at sage/rings/integer_mod.c:2750\n2750      Py_INCREF(__pyx_1);\n```\n",
    "created_at": "2007-12-02T19:32:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1374#issuecomment-8813",
    "user": "was"
}
```

First obvious thing to do (on sage.math):


```
sage: matrix(GF(5), 2, [4,0,0,1]) - int(-1)

Program received signal SIGSEGV, Segmentation fault.
[Switching to Thread 47703056093024 (LWP 5657)]
__pyx_f_4sage_5rings_11integer_mod_15NativeIntStruct_lookup (__pyx_v_self=0x2b62cd298e30, __pyx_v_value=5)
    at sage/rings/integer_mod.c:2750
2750      Py_INCREF(__pyx_1);
```




---

archive/issue_comments_008814.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2007-12-02T21:20:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1374#issuecomment-8814",
    "user": "was"
}
```

Changing priority from major to critical.



---

archive/issue_comments_008815.json:
```json
{
    "body": "The problem is very likely related to this:\n\n\n```\nsage: matrix(GF(5),2, [4,0,0,1]).parent()(int(6))\n[6 0]\n[0 6]\n```\n\n\nThis is over GF(5), so we should not see 6!",
    "created_at": "2007-12-02T21:26:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1374#issuecomment-8815",
    "user": "was"
}
```

The problem is very likely related to this:


```
sage: matrix(GF(5),2, [4,0,0,1]).parent()(int(6))
[6 0]
[0 6]
```


This is over GF(5), so we should not see 6!



---

archive/issue_comments_008816.json:
```json
{
    "body": "\n```\nsage: m = matrix(GF(5),2, [4,0,0,1])\nsage: a = matrix(GF(5),2, [4,0,0,1]).parent()(int(7))\nsage: m[1,1]\n1\nsage: a[1,1]\n7\nsage: m[1,1] - a[1,1]\n\n\n------------------------------------------------------------\nUnhandled SIGBUS: A bus error occured in SAGE.\n```\n",
    "created_at": "2007-12-02T21:27:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1374#issuecomment-8816",
    "user": "was"
}
```


```
sage: m = matrix(GF(5),2, [4,0,0,1])
sage: a = matrix(GF(5),2, [4,0,0,1]).parent()(int(7))
sage: m[1,1]
1
sage: a[1,1]
7
sage: m[1,1] - a[1,1]


------------------------------------------------------------
Unhandled SIGBUS: A bus error occured in SAGE.
```




---

archive/issue_comments_008817.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-12-02T21:32:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1374#issuecomment-8817",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_008818.json:
```json
{
    "body": "Merged in 2.8.15.rc0.",
    "created_at": "2007-12-02T21:37:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1374#issuecomment-8818",
    "user": "mabshoff"
}
```

Merged in 2.8.15.rc0.



---

archive/issue_comments_008819.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-02T21:37:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1374#issuecomment-8819",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_008820.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-12-02T23:19:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1374#issuecomment-8820",
    "user": "cwitty"
}
```

Attachment



---

archive/issue_comments_008821.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2007-12-02T23:20:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1374#issuecomment-8821",
    "user": "cwitty"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_008822.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-12-02T23:20:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1374#issuecomment-8822",
    "user": "cwitty"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_008823.json:
```json
{
    "body": "It's good that we don't crash any more; but maybe we should also give the right answer? :)\n\nI think we also need to apply my 1374-part2.patch",
    "created_at": "2007-12-02T23:20:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1374#issuecomment-8823",
    "user": "cwitty"
}
```

It's good that we don't crash any more; but maybe we should also give the right answer? :)

I think we also need to apply my 1374-part2.patch



---

archive/issue_comments_008824.json:
```json
{
    "body": "Merged cwitty's patch in 2.8.15.rc0. All doctests pass.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-03T00:28:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1374#issuecomment-8824",
    "user": "mabshoff"
}
```

Merged cwitty's patch in 2.8.15.rc0. All doctests pass.

Cheers,

Michael



---

archive/issue_comments_008825.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-03T00:28:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1374#issuecomment-8825",
    "user": "mabshoff"
}
```

Resolution: fixed
