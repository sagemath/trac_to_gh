# Issue 891: [with patch] symmetrica needs to have its deallocation routine called upon exit

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2007-10-13 20:44:34

Assignee: mhansen




---

Attachment

Here are some statistics: The really big one is

```
==26643== 80,000 bytes in 1 blocks are still reachable in loss record 1,797 of 1,866
==26643==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)
==26643==    by 0xDFD414A: SYM_malloc (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/devel/sage-main/build/sage/libs/symmetrica/sy
mmetrica.so)
==26643==    by 0xDFD4219: anfang (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/devel/sage-main/build/sage/libs/symmetrica/symmet
rica.so)
==26643==    by 0xDFAF13A: __pyx_f_py_10symmetrica_start (symmetrica.c:6089)
==26643==    by 0x482FE8: PyEval_EvalFrameEx (ceval.c:3548)
==26643==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==26643==    by 0x4851D1: PyEval_EvalCode (ceval.c:494)
==26643==    by 0x49B4FE: PyImport_ExecCodeModuleEx (import.c:669)
==26643==    by 0x49BE0F: load_source_module (import.c:953)
==26643==    by 0x49C45D: import_submodule (import.c:2394)
==26643==    by 0x49C920: load_next (import.c:2214)
==26643==    by 0x49CB7D: import_module_level (import.c:2002)
```

But there are a bunch of smaller issues (mostly 8, 16 or 32 bytes)

Without the patch:

```
==26643== LEAK SUMMARY:
==26643==    definitely lost: 0 bytes in 0 blocks.
==26643==      possibly lost: 198,182 bytes in 521 blocks.
==26643==    still reachable: 34,535,836 bytes in 16,831 blocks.
==26643==         suppressed: 0 bytes in 0 blocks.
```

With the patch:

```
==26449== LEAK SUMMARY:
==26449==    definitely lost: 0 bytes in 0 blocks.
==26449==      possibly lost: 198,654 bytes in 522 blocks.
==26449==    still reachable: 34,454,092 bytes in 16,785 blocks.
==26449==         suppressed: 0 bytes in 0 blocks.
```


Every byte counts!

Cheers,

Michael


---

Comment by was created at 2007-10-14 05:18:43

Resolution: fixed
