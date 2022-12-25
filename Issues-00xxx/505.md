# Issue 505: memleak in matrix_mod2_dense.so

archive/issues_000505.json:
```json
{
    "body": "Assignee: @malb\n\nKeywords: memleak matrix_mod2_dense\n\nHello,\n\nthis is somewhat of a followup to ticket #501 and should illustrate what a detailed Analysis of the logs can provide pointers on how to resolve memleaks:\n\nhave a look at the following four missing deallocations:\n\n```\n==18345== 136 bytes in 1 blocks are still reachable in loss record 669 of 2,410\n==18345==    at 0x4A04B32: calloc (vg_replace_malloc.c:279)\n==18345==    by 0x1FD9411E: buildAllCodes (grayflex.c:85)\n==18345==    by 0x1FD8FFC2: initmatrix_mod2_dense (matrix_mod2_dense.c:800)\n==18345==    by 0x49F762: _PyImport_LoadDynamicModule (importdl.c:53)\n==18345==    by 0x49D63E: import_submodule (import.c:2394)\n==18345==    by 0x49DB11: load_next (import.c:2214)\n==18345==    by 0x49DD33: import_module_level (import.c:1995)\n==18345==    by 0x49E1A4: PyImport_ImportModuleLevel (import.c:2066)\n==18345==    by 0x47D5D8: builtin___import__ (bltinmodule.c:47)\n==18345==    by 0x4156A2: PyObject_Call (abstract.c:1860)\n==18345==    by 0x47DB71: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==18345==    by 0x480BD3: PyEval_EvalFrameEx (ceval.c:2063)\n\n==18345== 256 bytes in 16 blocks are still reachable in loss record 694 of 2,410\n==18345==    at 0x4A04B32: calloc (vg_replace_malloc.c:279)\n==18345==    by 0x1FD94144: buildAllCodes (grayflex.c:88)\n==18345==    by 0x1FD8FFC2: initmatrix_mod2_dense (matrix_mod2_dense.c:800)\n==18345==    by 0x49F762: _PyImport_LoadDynamicModule (importdl.c:53)\n==18345==    by 0x49D63E: import_submodule (import.c:2394)\n==18345==    by 0x49DB11: load_next (import.c:2214)\n==18345==    by 0x49DD33: import_module_level (import.c:1995)\n==18345==    by 0x49E1A4: PyImport_ImportModuleLevel (import.c:2066)\n==18345==    by 0x47D5D8: builtin___import__ (bltinmodule.c:47)\n==18345==    by 0x4156A2: PyObject_Call (abstract.c:1860)\n==18345==    by 0x47DB71: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==18345==    by 0x480BD3: PyEval_EvalFrameEx (ceval.c:2063)\n\n==18345== 524,280 bytes in 16 blocks are still reachable in loss record 2,383 of 2,410\n==18345==    at 0x4A04B32: calloc (vg_replace_malloc.c:279)\n==18345==    by 0x1FD9417D: buildAllCodes (grayflex.c:90)\n==18345==    by 0x1FD8FFC2: initmatrix_mod2_dense (matrix_mod2_dense.c:800)\n==18345==    by 0x49F762: _PyImport_LoadDynamicModule (importdl.c:53)\n==18345==    by 0x49D63E: import_submodule (import.c:2394)\n==18345==    by 0x49DB11: load_next (import.c:2214)\n==18345==    by 0x49DD33: import_module_level (import.c:1995)\n==18345==    by 0x49E1A4: PyImport_ImportModuleLevel (import.c:2066)\n==18345==    by 0x47D5D8: builtin___import__ (bltinmodule.c:47)\n==18345==    by 0x4156A2: PyObject_Call (abstract.c:1860)\n==18345==    by 0x47DB71: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==18345==    by 0x480BD3: PyEval_EvalFrameEx (ceval.c:2063)\n\n==18345== 524,280 bytes in 16 blocks are still reachable in loss record 2,384 of 2,410\n==18345==    at 0x4A04B32: calloc (vg_replace_malloc.c:279)\n==18345==    by 0x1FD94166: buildAllCodes (grayflex.c:89)\n==18345==    by 0x1FD8FFC2: initmatrix_mod2_dense (matrix_mod2_dense.c:800)\n==18345==    by 0x49F762: _PyImport_LoadDynamicModule (importdl.c:53)\n==18345==    by 0x49D63E: import_submodule (import.c:2394)\n==18345==    by 0x49DB11: load_next (import.c:2214)\n==18345==    by 0x49DD33: import_module_level (import.c:1995)\n==18345==    by 0x49E1A4: PyImport_ImportModuleLevel (import.c:2066)\n==18345==    by 0x47D5D8: builtin___import__ (bltinmodule.c:47)\n==18345==    by 0x4156A2: PyObject_Call (abstract.c:1860)\n==18345==    by 0x47DB71: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==18345==    by 0x480BD3: PyEval_EvalFrameEx (ceval.c:2063)\n```\nFrom sage/libs/m4ri/grayflex.c:\n\n```\nvoid buildAllCodes() {\n  int k;\n  codebook=calloc(MAXKAY+1, sizeof(code *));                  [line 85]\n\n  for(k=1 ; k<MAXKAY+1; k++) {\n    codebook[k] = (code *)calloc(sizeof(code),1);             [line 88]\n    codebook[k]->ord =(int *)calloc(TWOPOW(k),sizeof(int));   [line 89]\n    codebook[k]->inc =(int *)calloc(TWOPOW(k),sizeof(int));   [line 90]\n    buildCodeFlex(codebook[k]->ord, codebook[k]->inc, k);\n  }\n}\n```\n\nNote: using (int *)-pointers seems to be a pretty bad idea.\n\nAll the bits allocated via buildAllCodes() would be freed in\n\n```\nvoid destroyAllCodes() {\n  int i;\n  for(i=1; i<MAXKAY+1; i++) {\n    free(codebook[i]->inc);\n    free(codebook[i]->ord);\n    free(codebook[i]);\n  }\n  free(codebook);\n}\n```\nbut it never gets called, see below:\n\nFrom line 120ff of sage/matrix/matrix_mod2_dense.pyx:\n\n```\ncdef void init_m4ri():\n    global called\n    if called is None:\n        # TODO: remove packingmask\n        setupPackingMasks()\n        buildAllCodes()\n        called = True\n```\nBut we do not call a matching destroyAllCodes()\n\nIssue created by migration from https://trac.sagemath.org/ticket/505\n\n",
    "closed_at": "2007-08-29T03:22:05Z",
    "created_at": "2007-08-28T23:40:48Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.3",
    "title": "memleak in matrix_mod2_dense.so",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/505",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @malb

Keywords: memleak matrix_mod2_dense

Hello,

this is somewhat of a followup to ticket #501 and should illustrate what a detailed Analysis of the logs can provide pointers on how to resolve memleaks:

have a look at the following four missing deallocations:

```
==18345== 136 bytes in 1 blocks are still reachable in loss record 669 of 2,410
==18345==    at 0x4A04B32: calloc (vg_replace_malloc.c:279)
==18345==    by 0x1FD9411E: buildAllCodes (grayflex.c:85)
==18345==    by 0x1FD8FFC2: initmatrix_mod2_dense (matrix_mod2_dense.c:800)
==18345==    by 0x49F762: _PyImport_LoadDynamicModule (importdl.c:53)
==18345==    by 0x49D63E: import_submodule (import.c:2394)
==18345==    by 0x49DB11: load_next (import.c:2214)
==18345==    by 0x49DD33: import_module_level (import.c:1995)
==18345==    by 0x49E1A4: PyImport_ImportModuleLevel (import.c:2066)
==18345==    by 0x47D5D8: builtin___import__ (bltinmodule.c:47)
==18345==    by 0x4156A2: PyObject_Call (abstract.c:1860)
==18345==    by 0x47DB71: PyEval_CallObjectWithKeywords (ceval.c:3433)
==18345==    by 0x480BD3: PyEval_EvalFrameEx (ceval.c:2063)

==18345== 256 bytes in 16 blocks are still reachable in loss record 694 of 2,410
==18345==    at 0x4A04B32: calloc (vg_replace_malloc.c:279)
==18345==    by 0x1FD94144: buildAllCodes (grayflex.c:88)
==18345==    by 0x1FD8FFC2: initmatrix_mod2_dense (matrix_mod2_dense.c:800)
==18345==    by 0x49F762: _PyImport_LoadDynamicModule (importdl.c:53)
==18345==    by 0x49D63E: import_submodule (import.c:2394)
==18345==    by 0x49DB11: load_next (import.c:2214)
==18345==    by 0x49DD33: import_module_level (import.c:1995)
==18345==    by 0x49E1A4: PyImport_ImportModuleLevel (import.c:2066)
==18345==    by 0x47D5D8: builtin___import__ (bltinmodule.c:47)
==18345==    by 0x4156A2: PyObject_Call (abstract.c:1860)
==18345==    by 0x47DB71: PyEval_CallObjectWithKeywords (ceval.c:3433)
==18345==    by 0x480BD3: PyEval_EvalFrameEx (ceval.c:2063)

==18345== 524,280 bytes in 16 blocks are still reachable in loss record 2,383 of 2,410
==18345==    at 0x4A04B32: calloc (vg_replace_malloc.c:279)
==18345==    by 0x1FD9417D: buildAllCodes (grayflex.c:90)
==18345==    by 0x1FD8FFC2: initmatrix_mod2_dense (matrix_mod2_dense.c:800)
==18345==    by 0x49F762: _PyImport_LoadDynamicModule (importdl.c:53)
==18345==    by 0x49D63E: import_submodule (import.c:2394)
==18345==    by 0x49DB11: load_next (import.c:2214)
==18345==    by 0x49DD33: import_module_level (import.c:1995)
==18345==    by 0x49E1A4: PyImport_ImportModuleLevel (import.c:2066)
==18345==    by 0x47D5D8: builtin___import__ (bltinmodule.c:47)
==18345==    by 0x4156A2: PyObject_Call (abstract.c:1860)
==18345==    by 0x47DB71: PyEval_CallObjectWithKeywords (ceval.c:3433)
==18345==    by 0x480BD3: PyEval_EvalFrameEx (ceval.c:2063)

==18345== 524,280 bytes in 16 blocks are still reachable in loss record 2,384 of 2,410
==18345==    at 0x4A04B32: calloc (vg_replace_malloc.c:279)
==18345==    by 0x1FD94166: buildAllCodes (grayflex.c:89)
==18345==    by 0x1FD8FFC2: initmatrix_mod2_dense (matrix_mod2_dense.c:800)
==18345==    by 0x49F762: _PyImport_LoadDynamicModule (importdl.c:53)
==18345==    by 0x49D63E: import_submodule (import.c:2394)
==18345==    by 0x49DB11: load_next (import.c:2214)
==18345==    by 0x49DD33: import_module_level (import.c:1995)
==18345==    by 0x49E1A4: PyImport_ImportModuleLevel (import.c:2066)
==18345==    by 0x47D5D8: builtin___import__ (bltinmodule.c:47)
==18345==    by 0x4156A2: PyObject_Call (abstract.c:1860)
==18345==    by 0x47DB71: PyEval_CallObjectWithKeywords (ceval.c:3433)
==18345==    by 0x480BD3: PyEval_EvalFrameEx (ceval.c:2063)
```
From sage/libs/m4ri/grayflex.c:

```
void buildAllCodes() {
  int k;
  codebook=calloc(MAXKAY+1, sizeof(code *));                  [line 85]

  for(k=1 ; k<MAXKAY+1; k++) {
    codebook[k] = (code *)calloc(sizeof(code),1);             [line 88]
    codebook[k]->ord =(int *)calloc(TWOPOW(k),sizeof(int));   [line 89]
    codebook[k]->inc =(int *)calloc(TWOPOW(k),sizeof(int));   [line 90]
    buildCodeFlex(codebook[k]->ord, codebook[k]->inc, k);
  }
}
```

Note: using (int *)-pointers seems to be a pretty bad idea.

All the bits allocated via buildAllCodes() would be freed in

```
void destroyAllCodes() {
  int i;
  for(i=1; i<MAXKAY+1; i++) {
    free(codebook[i]->inc);
    free(codebook[i]->ord);
    free(codebook[i]);
  }
  free(codebook);
}
```
but it never gets called, see below:

From line 120ff of sage/matrix/matrix_mod2_dense.pyx:

```
cdef void init_m4ri():
    global called
    if called is None:
        # TODO: remove packingmask
        setupPackingMasks()
        buildAllCodes()
        called = True
```
But we do not call a matching destroyAllCodes()

Issue created by migration from https://trac.sagemath.org/ticket/505





---

archive/issue_comments_002518.json:
```json
{
    "body": "Changing assignee from somebody to @malb.",
    "created_at": "2007-08-28T23:44:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/505#issuecomment-2518",
    "user": "https://github.com/williamstein"
}
```

Changing assignee from somebody to @malb.



---

archive/issue_comments_002519.json:
```json
{
    "body": "Attachment [m4ri_cleanup.patch](tarball://root/attachments/some-uuid/ticket505/m4ri_cleanup.patch) by @williamstein created at 2007-08-28 23:52:25\n\nThis fixes the m4ri not being cleaned up issue, I hope.",
    "created_at": "2007-08-28T23:52:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/505#issuecomment-2519",
    "user": "https://github.com/williamstein"
}
```

Attachment [m4ri_cleanup.patch](tarball://root/attachments/some-uuid/ticket505/m4ri_cleanup.patch) by @williamstein created at 2007-08-28 23:52:25

This fixes the m4ri not being cleaned up issue, I hope.



---

archive/issue_events_001287.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-08-28T23:52:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/505",
    "milestone": "sage-2.8.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/505#event-1287"
}
```



---

archive/issue_comments_002520.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-29T03:22:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/505#issuecomment-2520",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_001288.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-08-29T03:22:05Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/505",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/505#event-1288"
}
```



---

archive/issue_comments_002521.json:
```json
{
    "body": "I rerun the test with 2.8.3alpha2 and valgrind and can confirm that the problem is gone and the fix works.\n\nCheers,\n\nMichael",
    "created_at": "2007-08-29T11:24:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/505#issuecomment-2521",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I rerun the test with 2.8.3alpha2 and valgrind and can confirm that the problem is gone and the fix works.

Cheers,

Michael
