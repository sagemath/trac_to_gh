# Issue 1001: "Use of uninitialised value of size 4" in pari.pyx

archive/issues_001001.json:
```json
{
    "body": "Assignee: @williamstein\n\nJust by doing a sage start + immediate quit under valgrind leads to:\n\n```\n==12979== Conditional jump or move depends on uninitialised value(s)\n==12979==    at 0x8088C18: PyObject_Free (obmalloc.c:920)\n==12979==    by 0x8106892: code_dealloc (codeobject.c:270)\n==12979==    by 0x810C769: frame_dealloc (frameobject.c:444)\n==12979==    by 0x80EBB0B: tb_dealloc (traceback.c:34)\n==12979==    by 0x5764226: __Pyx_GetExcValue (gen.c:30664)\n==12979==    by 0x5788110: __pyx_f_py_3gen_12PariInstance___call__ (gen.c:23295)\n==12979==    by 0x805A276: PyObject_Call (abstract.c:1860)\n==12979==    by 0x80BE7CB: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==12979==    by 0x805A48F: PyObject_CallObject (abstract.c:1851)\n==12979==    by 0x5791B62: __pyx_f_py_3gen_12PariInstance___init__ (gen.c:21789)\n==12979==    by 0x809C412: type_call (typeobject.c:436)\n==12979==    by 0x805A276: PyObject_Call (abstract.c:1860)\n==12979==\n==12979== Use of uninitialised value of size 4\n==12979==    at 0x8088C23: PyObject_Free (obmalloc.c:920)\n==12979==    by 0x8106892: code_dealloc (codeobject.c:270)\n==12979==    by 0x810C769: frame_dealloc (frameobject.c:444)\n==12979==    by 0x80EBB0B: tb_dealloc (traceback.c:34)\n==12979==    by 0x5764226: __Pyx_GetExcValue (gen.c:30664)\n==12979==    by 0x5788110: __pyx_f_py_3gen_12PariInstance___call__ (gen.c:23295)\n==12979==    by 0x805A276: PyObject_Call (abstract.c:1860)\n==12979==    by 0x80BE7CB: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==12979==    by 0x805A48F: PyObject_CallObject (abstract.c:1851)\n==12979==    by 0x5791B62: __pyx_f_py_3gen_12PariInstance___init__ (gen.c:21789)\n==12979==    by 0x809C412: type_call (typeobject.c:436)\n==12979==    by 0x805A276: PyObject_Call (abstract.c:1860)\n```\n\nI tracked this down to gen.pyx:5566:\n\n```\n        self.ONE = self(1)\n```\n\nbut I have no clue how to fix this.\n\nCheers,\n\nMichael\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1001\n\n",
    "created_at": "2007-10-26T02:20:40Z",
    "labels": [
        "component: memleak",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "\"Use of uninitialised value of size 4\" in pari.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1001",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @williamstein

Just by doing a sage start + immediate quit under valgrind leads to:

```
==12979== Conditional jump or move depends on uninitialised value(s)
==12979==    at 0x8088C18: PyObject_Free (obmalloc.c:920)
==12979==    by 0x8106892: code_dealloc (codeobject.c:270)
==12979==    by 0x810C769: frame_dealloc (frameobject.c:444)
==12979==    by 0x80EBB0B: tb_dealloc (traceback.c:34)
==12979==    by 0x5764226: __Pyx_GetExcValue (gen.c:30664)
==12979==    by 0x5788110: __pyx_f_py_3gen_12PariInstance___call__ (gen.c:23295)
==12979==    by 0x805A276: PyObject_Call (abstract.c:1860)
==12979==    by 0x80BE7CB: PyEval_CallObjectWithKeywords (ceval.c:3433)
==12979==    by 0x805A48F: PyObject_CallObject (abstract.c:1851)
==12979==    by 0x5791B62: __pyx_f_py_3gen_12PariInstance___init__ (gen.c:21789)
==12979==    by 0x809C412: type_call (typeobject.c:436)
==12979==    by 0x805A276: PyObject_Call (abstract.c:1860)
==12979==
==12979== Use of uninitialised value of size 4
==12979==    at 0x8088C23: PyObject_Free (obmalloc.c:920)
==12979==    by 0x8106892: code_dealloc (codeobject.c:270)
==12979==    by 0x810C769: frame_dealloc (frameobject.c:444)
==12979==    by 0x80EBB0B: tb_dealloc (traceback.c:34)
==12979==    by 0x5764226: __Pyx_GetExcValue (gen.c:30664)
==12979==    by 0x5788110: __pyx_f_py_3gen_12PariInstance___call__ (gen.c:23295)
==12979==    by 0x805A276: PyObject_Call (abstract.c:1860)
==12979==    by 0x80BE7CB: PyEval_CallObjectWithKeywords (ceval.c:3433)
==12979==    by 0x805A48F: PyObject_CallObject (abstract.c:1851)
==12979==    by 0x5791B62: __pyx_f_py_3gen_12PariInstance___init__ (gen.c:21789)
==12979==    by 0x809C412: type_call (typeobject.c:436)
==12979==    by 0x805A276: PyObject_Call (abstract.c:1860)
```

I tracked this down to gen.pyx:5566:

```
        self.ONE = self(1)
```

but I have no clue how to fix this.

Cheers,

Michael


Issue created by migration from https://trac.sagemath.org/ticket/1001





---

archive/issue_comments_006075.json:
```json
{
    "body": "this is likely fixed by the fix for #875, since the offending line in gen.pyx has been changed.",
    "created_at": "2007-10-28T06:04:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1001#issuecomment-6075",
    "user": "https://github.com/craigcitro"
}
```

this is likely fixed by the fix for #875, since the offending line in gen.pyx has been changed.



---

archive/issue_comments_006076.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2007-10-28T06:47:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1001#issuecomment-6076",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: invalid



---

archive/issue_events_002754.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-10-28T06:47:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1001",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1001#event-2754"
}
```



---

archive/issue_comments_006077.json:
```json
{
    "body": "\n```\n[07:35] <cwitty> Whenever you pass an address to PyObject_Free, it will read the first 4 bytes of the 4096-byte page containing that address.  If Python allocated that memory, then those 4 bytes will be valid to read.  But if the system malloc allocated them, then there may or may not be valid (according to valgrind) data there.\n[07:35] <cwitty> It just depends on the particular history of allocations/frees in the program so far.\n```\n",
    "created_at": "2007-10-28T06:48:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1001#issuecomment-6077",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```


```
[07:35] <cwitty> Whenever you pass an address to PyObject_Free, it will read the first 4 bytes of the 4096-byte page containing that address.  If Python allocated that memory, then those 4 bytes will be valid to read.  But if the system malloc allocated them, then there may or may not be valid (according to valgrind) data there.
[07:35] <cwitty> It just depends on the particular history of allocations/frees in the program so far.
```




---

archive/issue_comments_006078.json:
```json
{
    "body": "For more details, read the comment describing Py_ADDRESS_IN_RANGE, in Objects/obmalloc.c in the Python source code.",
    "created_at": "2007-10-28T06:50:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1001#issuecomment-6078",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

For more details, read the comment describing Py_ADDRESS_IN_RANGE, in Objects/obmalloc.c in the Python source code.
