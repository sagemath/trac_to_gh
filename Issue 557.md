# Issue 557: missing dictionary deallocation in Cython's init code

archive/issues_000557.json:
```json
{
    "body": "Assignee: mabshoff\n\nOkay, the problem I found is deep in Cython generated code and \nmaybe not the fault of Cython, but might be an underlying issue \nin Python. For each of the 244 pyx files we have in the tree \nwe do not deallocate  a dictionary. While this \nisn't a defect per se it makes the valgrind output more noise \nand therefor more difficult to parse.\n\nThe example output below is from rational.pyx. The function initrational \nis created via Cython (there is no init-method, but that comes out of \nthe creation of the class as far as I can tell):\n\n```\n==25825== 3,072 bytes in 1 blocks are still reachable in loss record 2,268 of 2,539\n==25825==    at 0x4A05809: malloc (vg_replace_malloc.c:149)\n==25825==    by 0x43F179: dictresize (dictobject.c:513)\n==25825==    by 0x45B00C: PyType_Ready (typeobject.c:5575)\n==25825==    by 0x169D79A0: initrational (rational.c:10789)\n==25825==    by 0x49F762: _PyImport_LoadDynamicModule (importdl.c:53)\n==25825==    by 0x49D63E: import_submodule (import.c:2394)\n==25825==    by 0x49DB11: load_next (import.c:2214)\n==25825==    by 0x49DD6E: import_module_level (import.c:2002)\n==25825==    by 0x49E1A4: PyImport_ImportModuleLevel (import.c:2066)\n==25825==    by 0x47D5D8: builtin___import__ (bltinmodule.c:47)\n==25825==    by 0x4156A2: PyObject_Call (abstract.c:1860)\n==25825==    by 0x47DB71: PyEval_CallObjectWithKeywords (ceval.c:3433)\n```\n\nThe exact line from rational.c:10789 is:\n\nif (PyType_Ready(&__pyx_type_8rational_Rational) < 0) {__pyx_filename = __pyx_f[1]; __pyx_lineno = 126; goto __pyx_L1;}\n\nIt mentions line 126 which in rational.pyx is:\n\ncdef class Rational(sage.structure.element.FieldElement):\n\nSo can be dereference the class somehow upon exit? Looking \nat valgrind-sessions from python it appears that this is \npossible because otherwise there would be a large number of \nleak dictionaries from the buildin c-libraries.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/557\n\n",
    "created_at": "2007-09-01T23:32:30Z",
    "labels": [
        "component: memleak",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "missing dictionary deallocation in Cython's init code",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/557",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

Okay, the problem I found is deep in Cython generated code and 
maybe not the fault of Cython, but might be an underlying issue 
in Python. For each of the 244 pyx files we have in the tree 
we do not deallocate  a dictionary. While this 
isn't a defect per se it makes the valgrind output more noise 
and therefor more difficult to parse.

The example output below is from rational.pyx. The function initrational 
is created via Cython (there is no init-method, but that comes out of 
the creation of the class as far as I can tell):

```
==25825== 3,072 bytes in 1 blocks are still reachable in loss record 2,268 of 2,539
==25825==    at 0x4A05809: malloc (vg_replace_malloc.c:149)
==25825==    by 0x43F179: dictresize (dictobject.c:513)
==25825==    by 0x45B00C: PyType_Ready (typeobject.c:5575)
==25825==    by 0x169D79A0: initrational (rational.c:10789)
==25825==    by 0x49F762: _PyImport_LoadDynamicModule (importdl.c:53)
==25825==    by 0x49D63E: import_submodule (import.c:2394)
==25825==    by 0x49DB11: load_next (import.c:2214)
==25825==    by 0x49DD6E: import_module_level (import.c:2002)
==25825==    by 0x49E1A4: PyImport_ImportModuleLevel (import.c:2066)
==25825==    by 0x47D5D8: builtin___import__ (bltinmodule.c:47)
==25825==    by 0x4156A2: PyObject_Call (abstract.c:1860)
==25825==    by 0x47DB71: PyEval_CallObjectWithKeywords (ceval.c:3433)
```

The exact line from rational.c:10789 is:

if (PyType_Ready(&__pyx_type_8rational_Rational) < 0) {__pyx_filename = __pyx_f[1]; __pyx_lineno = 126; goto __pyx_L1;}

It mentions line 126 which in rational.pyx is:

cdef class Rational(sage.structure.element.FieldElement):

So can be dereference the class somehow upon exit? Looking 
at valgrind-sessions from python it appears that this is 
possible because otherwise there would be a large number of 
leak dictionaries from the buildin c-libraries.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/557





---

archive/issue_comments_002866.json:
```json
{
    "body": "The link to the discussion in sage-devel is \n\nhttp://groups.google.com/group/sage-devel/t/673812f3d9ed262a\n\nCheers,\n\nMichael",
    "created_at": "2007-09-01T23:32:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/557#issuecomment-2866",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The link to the discussion in sage-devel is 

http://groups.google.com/group/sage-devel/t/673812f3d9ed262a

Cheers,

Michael



---

archive/issue_comments_002867.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-09-02T00:29:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/557#issuecomment-2867",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_002868.json:
```json
{
    "body": "For some more discussion and a potential cause check out \n\nhttp://groups.google.com/group/sage-devel/t/5a1d104614ced3aa\n\nCheers,\n\nMichael",
    "created_at": "2007-10-18T04:18:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/557#issuecomment-2868",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

For some more discussion and a potential cause check out 

http://groups.google.com/group/sage-devel/t/5a1d104614ced3aa

Cheers,

Michael
