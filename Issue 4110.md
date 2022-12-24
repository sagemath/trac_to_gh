# Issue 4110: Memory leak in saving matrices

archive/issues_004110.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  malb\n\nThis is in sage-3.1.2.rc1.\n\nIf I do\n\n```\nsage: L = [random_matrix(GF(2), 20, 20) for _ in xrange(10^5)]\n```\n\nthen my process is here:\n\n```\n  PID USER      PR  NI  VIRT  RES  SHR S %CPU %MEM    TIME+  COMMAND          \n15889 rlmill    25   0  446m 131m  17m S    0  0.2   0:06.30 sage-ipython\n```\n\n\nThen I do the following:\n\n```\nsage: save(L, 'crap')\nsage: del L\n```\n\n\nAnd my process is here:\n\n```\n  PID USER      PR  NI  VIRT  RES  SHR S %CPU %MEM    TIME+  COMMAND          \n15889 rlmill    16   0 1471m 1.1g  17m S    0  1.8   1:02.37 sage-ipython\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4110\n\n",
    "created_at": "2008-09-13T19:00:31Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "Memory leak in saving matrices",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4110",
    "user": "rlm"
}
```
Assignee: tbd

CC:  malb

This is in sage-3.1.2.rc1.

If I do

```
sage: L = [random_matrix(GF(2), 20, 20) for _ in xrange(10^5)]
```

then my process is here:

```
  PID USER      PR  NI  VIRT  RES  SHR S %CPU %MEM    TIME+  COMMAND          
15889 rlmill    25   0  446m 131m  17m S    0  0.2   0:06.30 sage-ipython
```


Then I do the following:

```
sage: save(L, 'crap')
sage: del L
```


And my process is here:

```
  PID USER      PR  NI  VIRT  RES  SHR S %CPU %MEM    TIME+  COMMAND          
15889 rlmill    16   0 1471m 1.1g  17m S    0  1.8   1:02.37 sage-ipython
```


Issue created by migration from https://trac.sagemath.org/ticket/4110





---

archive/issue_comments_029755.json:
```json
{
    "body": "Changing assignee from tbd to mabshoff.",
    "created_at": "2008-09-13T19:01:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4110",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4110#issuecomment-29755",
    "user": "rlm"
}
```

Changing assignee from tbd to mabshoff.



---

archive/issue_comments_029756.json:
```json
{
    "body": "Changing component from algebra to memleak.",
    "created_at": "2008-09-13T19:01:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4110",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4110#issuecomment-29756",
    "user": "rlm"
}
```

Changing component from algebra to memleak.



---

archive/issue_comments_029757.json:
```json
{
    "body": "Oops, with `10^4` elements:\n\n```\n==27766== LEAK SUMMARY:\n==27766==    definitely lost: 73,004,158 bytes in 10,007 blocks.\n==27766==    indirectly lost: 5,586,420 bytes in 209,482 blocks.\n==27766==      possibly lost: 402,505 bytes in 1,011 blocks.\n==27766==    still reachable: 36,106,357 bytes in 217,055 blocks.\n==27766==         suppressed: 305,691 bytes in 4,843 blocks.\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-09-13T22:02:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4110",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4110#issuecomment-29757",
    "user": "mabshoff"
}
```

Oops, with `10^4` elements:

```
==27766== LEAK SUMMARY:
==27766==    definitely lost: 73,004,158 bytes in 10,007 blocks.
==27766==    indirectly lost: 5,586,420 bytes in 209,482 blocks.
==27766==      possibly lost: 402,505 bytes in 1,011 blocks.
==27766==    still reachable: 36,106,357 bytes in 217,055 blocks.
==27766==         suppressed: 305,691 bytes in 4,843 blocks.
```


Cheers,

Michael



---

archive/issue_comments_029758.json:
```json
{
    "body": "Before:\n\n```\n==27766== LEAK SUMMARY:\n==27766==    definitely lost: 73,004,158 bytes in 10,007 blocks.\n==27766==    indirectly lost: 5,586,420 bytes in 209,482 blocks.\n==27766==      possibly lost: 402,505 bytes in 1,011 blocks.\n==27766==    still reachable: 36,106,357 bytes in 217,055 blocks.\n==27766==         suppressed: 305,691 bytes in 4,843 blocks.\n```\n\nSpecifically:\n\n```\n==27766== 78,589,900 (73,003,480 direct, 5,586,420 indirect) bytes in 9,995 blocks are definitely lost in loss record 13,758 of 13,758\n==27766==    at 0x4A1BDEB: malloc (vg_replace_malloc.c:207)\n==27766==    by 0x16A44C5E: gdMalloc (gdhelpers.c:85)\n==27766==    by 0x16A2E130: gdImageCreate (gd.c:83)\n==27766==    by 0x166C828B: __pyx_pf_4sage_6matrix_17matrix_mod2_dense_17Matrix_mod2_dense___reduce__ (matrix_mod2_dense.c:6925)\n==27766==    by 0x415832: PyObject_Call (abstract.c:1861)\n==27766==    by 0x47D750: PyEval_CallObjectWithKeywords (ceval.c:3442)\n==27766==    by 0x458C0F: object_reduce_ex (typeobject.c:2867)\n==27766==    by 0x415832: PyObject_Call (abstract.c:1861)\n==27766==    by 0x7D86723: save (cPickle.c:2498)\n==27766==    by 0x7D87ECC: batch_list (cPickle.c:1561)\n==27766==    by 0x7D86C5B: save (cPickle.c:1629)\n==27766==    by 0x7D88587: cpm_dumps (cPickle.c:2580)\n```\n\n\nAfter:\n\n```\n==29605== LEAK SUMMARY:\n==29605==    definitely lost: 678 bytes in 12 blocks.\n==29605==      possibly lost: 369,938 bytes in 975 blocks.\n==29605==    still reachable: 36,091,754 bytes in 216,569 blocks.\n==29605==         suppressed: 305,691 bytes in 4,843 blocks.\n```\n",
    "created_at": "2008-09-14T00:02:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4110",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4110#issuecomment-29758",
    "user": "mabshoff"
}
```

Before:

```
==27766== LEAK SUMMARY:
==27766==    definitely lost: 73,004,158 bytes in 10,007 blocks.
==27766==    indirectly lost: 5,586,420 bytes in 209,482 blocks.
==27766==      possibly lost: 402,505 bytes in 1,011 blocks.
==27766==    still reachable: 36,106,357 bytes in 217,055 blocks.
==27766==         suppressed: 305,691 bytes in 4,843 blocks.
```

Specifically:

```
==27766== 78,589,900 (73,003,480 direct, 5,586,420 indirect) bytes in 9,995 blocks are definitely lost in loss record 13,758 of 13,758
==27766==    at 0x4A1BDEB: malloc (vg_replace_malloc.c:207)
==27766==    by 0x16A44C5E: gdMalloc (gdhelpers.c:85)
==27766==    by 0x16A2E130: gdImageCreate (gd.c:83)
==27766==    by 0x166C828B: __pyx_pf_4sage_6matrix_17matrix_mod2_dense_17Matrix_mod2_dense___reduce__ (matrix_mod2_dense.c:6925)
==27766==    by 0x415832: PyObject_Call (abstract.c:1861)
==27766==    by 0x47D750: PyEval_CallObjectWithKeywords (ceval.c:3442)
==27766==    by 0x458C0F: object_reduce_ex (typeobject.c:2867)
==27766==    by 0x415832: PyObject_Call (abstract.c:1861)
==27766==    by 0x7D86723: save (cPickle.c:2498)
==27766==    by 0x7D87ECC: batch_list (cPickle.c:1561)
==27766==    by 0x7D86C5B: save (cPickle.c:1629)
==27766==    by 0x7D88587: cpm_dumps (cPickle.c:2580)
```


After:

```
==29605== LEAK SUMMARY:
==29605==    definitely lost: 678 bytes in 12 blocks.
==29605==      possibly lost: 369,938 bytes in 975 blocks.
==29605==    still reachable: 36,091,754 bytes in 216,569 blocks.
==29605==         suppressed: 305,691 bytes in 4,843 blocks.
```




---

archive/issue_comments_029759.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-14T00:02:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4110",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4110#issuecomment-29759",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_029760.json:
```json
{
    "body": "Attachment [trac_4110.patch](tarball://root/attachments/some-uuid/ticket4110/trac_4110.patch) by mabshoff created at 2008-09-14 00:05:35",
    "created_at": "2008-09-14T00:05:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4110",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4110#issuecomment-29760",
    "user": "mabshoff"
}
```

Attachment [trac_4110.patch](tarball://root/attachments/some-uuid/ticket4110/trac_4110.patch) by mabshoff created at 2008-09-14 00:05:35



---

archive/issue_comments_029761.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-14T02:24:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4110",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4110#issuecomment-29761",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_029762.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc3",
    "created_at": "2008-09-14T02:24:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4110",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4110#issuecomment-29762",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.rc3
