# Issue 505: memleak in matrix_mod2_dense.so

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-08-28 23:40:48

Assignee: somebody

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


---

Comment by was created at 2007-08-28 23:44:07

Changing assignee from somebody to malb.


---

Attachment

This fixes the m4ri not being cleaned up issue, I hope.


---

Comment by was created at 2007-08-29 03:22:05

Resolution: fixed


---

Comment by mabshoff created at 2007-08-29 11:24:24

I rerun the test with 2.8.3alpha2 and valgrind and can confirm that the problem is gone and the fix works.

Cheers,

Michael
