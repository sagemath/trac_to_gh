# Issue 2239: Leak in totallyreal.py

archive/issues_002239.json:
```json
{
    "body": "Assignee: @craigcitro\n\nRunning the doctest under valgrind leads to:\n\n```\n==24549== 12,656 (10,848 direct, 1,808 indirect) bytes in 226 blocks are definitely lost in loss record 7,761 of 7,934\n==24549==    at 0x4A1BDEB: malloc (vg_replace_malloc.c:207)\n==24549==    by 0xB323D52: __pyx_f_4sage_5rings_7integer_fast_tp_new (integer.c:19858)\n==24549==    by 0x10FA7030: __pyx_pf_4sage_5rings_10polynomial_28polynomial_integer_dense_ntl_28Polynomial_integer_dense_ntl\n___getitem__(_object*, _object*) (polynomial_integer_dense_ntl.cpp:2898)\n==24549==    by 0x10FA76B0: __pyx_pf_4sage_5rings_10polynomial_28polynomial_integer_dense_ntl_28Polynomial_integer_dense_ntl\n_list(_object*, _object*) (polynomial_integer_dense_ntl.cpp:6561)\n==24549==    by 0x415542: PyObject_Call (abstract.c:1860)\n==24549==    by 0x10FB2902: __pyx_pf_4sage_5rings_10polynomial_28polynomial_integer_dense_ntl_28Polynomial_integer_dense_ntl\n___floordiv__(_object*, _object*) (polynomial_integer_dense_ntl.cpp:4761)\n==24549==    by 0x41580C: binary_op1 (abstract.c:398)\n==24549==    by 0x416CDD: PyNumber_FloorDivide (abstract.c:450)\n==24549==    by 0x142523FE: __pyx_pf_4sage_5rings_12number_field_16totallyreal_data_lagrange_degree_3 (totallyreal_data.c:39\n75)\n==24549==    by 0x415542: PyObject_Call (abstract.c:1860)\n==24549==    by 0x14271583: __pyx_pf_4sage_5rings_12number_field_16totallyreal_data_7tr_data_incr (totallyreal_data.c:7355)\n==24549==    by 0x415542: PyObject_Call (abstract.c:1860)\n```\n\nAnd:\n\n```\n==24549== 25,424 (21,792 direct, 3,632 indirect) bytes in 454 blocks are definitely lost in loss record 7,823 of 7,934\n==24549==    at 0x4A1BDEB: malloc (vg_replace_malloc.c:207)\n==24549==    by 0xB323D52: __pyx_f_4sage_5rings_7integer_fast_tp_new (integer.c:19858)\n==24549==    by 0x458D92: type_call (typeobject.c:422)\n==24549==    by 0x415542: PyObject_Call (abstract.c:1860)\n==24549==    by 0x10FAC427: __pyx_pf_4sage_5rings_10polynomial_28polynomial_integer_dense_ntl_28Polynomial_integer_dense_ntl\n___init__(_object*, _object*, _object*) (polynomial_integer_dense_ntl.cpp:2659)\n==24549==    by 0x458E40: type_call (typeobject.c:436)\n==24549==    by 0x415542: PyObject_Call (abstract.c:1860)\n==24549==    by 0x482221: PyEval_EvalFrameEx (ceval.c:3775)\n==24549==    by 0x4852CA: PyEval_EvalCodeEx (ceval.c:2831)\n==24549==    by 0x4CE817: function_call (funcobject.c:517)\n==24549==    by 0x415542: PyObject_Call (abstract.c:1860)\n==24549==    by 0x41BC62: instancemethod_call (classobject.c:2497)\n```\n\nAnd:\n\n```\n==24549== 25,368 (21,744 direct, 3,624 indirect) bytes in 453 blocks are definitely lost in loss record 7,827 of 7,934\n==24549==    at 0x4A1BDEB: malloc (vg_replace_malloc.c:207)\n==24549==    by 0xB323D52: __pyx_f_4sage_5rings_7integer_fast_tp_new (integer.c:19858)\n==24549==    by 0x458D92: type_call (typeobject.c:422)\n==24549==    by 0x415542: PyObject_Call (abstract.c:1860)\n==24549==    by 0x10FAC427: __pyx_pf_4sage_5rings_10polynomial_28polynomial_integer_dense_ntl_28Polynomial_integer_dense_ntl\n___init__(_object*, _object*, _object*) (polynomial_integer_dense_ntl.cpp:2659)\n==24549==    by 0x458E40: type_call (typeobject.c:436)\n==24549==    by 0x415542: PyObject_Call (abstract.c:1860)\n==24549==    by 0x482221: PyEval_EvalFrameEx (ceval.c:3775)\n==24549==    by 0x4852CA: PyEval_EvalCodeEx (ceval.c:2831)\n==24549==    by 0x4CE7B0: function_call (funcobject.c:517)\n==24549==    by 0x415542: PyObject_Call (abstract.c:1860)\n==24549==    by 0x41BC62: instancemethod_call (classobject.c:2497)\n```\n\nAnd:\n\n```\n==24549== 165,032 (141,456 direct, 23,576 indirect) bytes in 2,947 blocks are definitely lost in loss record 7,910 of 7,934\n==24549==    at 0x4A1BDEB: malloc (vg_replace_malloc.c:207)\n==24549==    by 0xB323D52: __pyx_f_4sage_5rings_7integer_fast_tp_new (integer.c:19858)\n==24549==    by 0xB344219: __pyx_f_4sage_5rings_7integer_7Integer__floordiv (integer.c:7921)\n==24549==    by 0xB343FFF: __pyx_pf_4sage_5rings_7integer_7Integer___floordiv__ (integer.c:8020)\n==24549==    by 0x41580C: binary_op1 (abstract.c:398)\n==24549==    by 0x416CDD: PyNumber_FloorDivide (abstract.c:450)\n==24549==    by 0x10FB29B1: __pyx_pf_4sage_5rings_10polynomial_28polynomial_integer_dense_ntl_28Polynomial_integer_dense_ntl\n___floordiv__(_object*, _object*) (polynomial_integer_dense_ntl.cpp:4779)\n==24549==    by 0x41580C: binary_op1 (abstract.c:398)\n==24549==    by 0x416CDD: PyNumber_FloorDivide (abstract.c:450)\n==24549==    by 0x142523FE: __pyx_pf_4sage_5rings_12number_field_16totallyreal_data_lagrange_degree_3 (totallyreal_data.c:39\n75)\n==24549==    by 0x415542: PyObject_Call (abstract.c:1860)\n==24549==    by 0x14271583: __pyx_pf_4sage_5rings_12number_field_16totallyreal_data_7tr_data_incr (totallyreal_data.c:7355)\n```\n\nIn total:\n\n```\n==24549==    definitely lost: 196,328 bytes in 4,087 blocks.\n==24549==    indirectly lost: 36,148 bytes in 4,090 blocks.\n==24549==      possibly lost: 267,538 bytes in 814 blocks.\n==24549==    still reachable: 30,329,036 bytes in 188,033 blocks.\n==24549==         suppressed: 0 bytes in 0 blocks.\n```\n\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/2239\n\n",
    "created_at": "2008-02-20T23:31:49Z",
    "labels": [
        "component: memleak",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "Leak in totallyreal.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2239",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @craigcitro

Running the doctest under valgrind leads to:

```
==24549== 12,656 (10,848 direct, 1,808 indirect) bytes in 226 blocks are definitely lost in loss record 7,761 of 7,934
==24549==    at 0x4A1BDEB: malloc (vg_replace_malloc.c:207)
==24549==    by 0xB323D52: __pyx_f_4sage_5rings_7integer_fast_tp_new (integer.c:19858)
==24549==    by 0x10FA7030: __pyx_pf_4sage_5rings_10polynomial_28polynomial_integer_dense_ntl_28Polynomial_integer_dense_ntl
___getitem__(_object*, _object*) (polynomial_integer_dense_ntl.cpp:2898)
==24549==    by 0x10FA76B0: __pyx_pf_4sage_5rings_10polynomial_28polynomial_integer_dense_ntl_28Polynomial_integer_dense_ntl
_list(_object*, _object*) (polynomial_integer_dense_ntl.cpp:6561)
==24549==    by 0x415542: PyObject_Call (abstract.c:1860)
==24549==    by 0x10FB2902: __pyx_pf_4sage_5rings_10polynomial_28polynomial_integer_dense_ntl_28Polynomial_integer_dense_ntl
___floordiv__(_object*, _object*) (polynomial_integer_dense_ntl.cpp:4761)
==24549==    by 0x41580C: binary_op1 (abstract.c:398)
==24549==    by 0x416CDD: PyNumber_FloorDivide (abstract.c:450)
==24549==    by 0x142523FE: __pyx_pf_4sage_5rings_12number_field_16totallyreal_data_lagrange_degree_3 (totallyreal_data.c:39
75)
==24549==    by 0x415542: PyObject_Call (abstract.c:1860)
==24549==    by 0x14271583: __pyx_pf_4sage_5rings_12number_field_16totallyreal_data_7tr_data_incr (totallyreal_data.c:7355)
==24549==    by 0x415542: PyObject_Call (abstract.c:1860)
```

And:

```
==24549== 25,424 (21,792 direct, 3,632 indirect) bytes in 454 blocks are definitely lost in loss record 7,823 of 7,934
==24549==    at 0x4A1BDEB: malloc (vg_replace_malloc.c:207)
==24549==    by 0xB323D52: __pyx_f_4sage_5rings_7integer_fast_tp_new (integer.c:19858)
==24549==    by 0x458D92: type_call (typeobject.c:422)
==24549==    by 0x415542: PyObject_Call (abstract.c:1860)
==24549==    by 0x10FAC427: __pyx_pf_4sage_5rings_10polynomial_28polynomial_integer_dense_ntl_28Polynomial_integer_dense_ntl
___init__(_object*, _object*, _object*) (polynomial_integer_dense_ntl.cpp:2659)
==24549==    by 0x458E40: type_call (typeobject.c:436)
==24549==    by 0x415542: PyObject_Call (abstract.c:1860)
==24549==    by 0x482221: PyEval_EvalFrameEx (ceval.c:3775)
==24549==    by 0x4852CA: PyEval_EvalCodeEx (ceval.c:2831)
==24549==    by 0x4CE817: function_call (funcobject.c:517)
==24549==    by 0x415542: PyObject_Call (abstract.c:1860)
==24549==    by 0x41BC62: instancemethod_call (classobject.c:2497)
```

And:

```
==24549== 25,368 (21,744 direct, 3,624 indirect) bytes in 453 blocks are definitely lost in loss record 7,827 of 7,934
==24549==    at 0x4A1BDEB: malloc (vg_replace_malloc.c:207)
==24549==    by 0xB323D52: __pyx_f_4sage_5rings_7integer_fast_tp_new (integer.c:19858)
==24549==    by 0x458D92: type_call (typeobject.c:422)
==24549==    by 0x415542: PyObject_Call (abstract.c:1860)
==24549==    by 0x10FAC427: __pyx_pf_4sage_5rings_10polynomial_28polynomial_integer_dense_ntl_28Polynomial_integer_dense_ntl
___init__(_object*, _object*, _object*) (polynomial_integer_dense_ntl.cpp:2659)
==24549==    by 0x458E40: type_call (typeobject.c:436)
==24549==    by 0x415542: PyObject_Call (abstract.c:1860)
==24549==    by 0x482221: PyEval_EvalFrameEx (ceval.c:3775)
==24549==    by 0x4852CA: PyEval_EvalCodeEx (ceval.c:2831)
==24549==    by 0x4CE7B0: function_call (funcobject.c:517)
==24549==    by 0x415542: PyObject_Call (abstract.c:1860)
==24549==    by 0x41BC62: instancemethod_call (classobject.c:2497)
```

And:

```
==24549== 165,032 (141,456 direct, 23,576 indirect) bytes in 2,947 blocks are definitely lost in loss record 7,910 of 7,934
==24549==    at 0x4A1BDEB: malloc (vg_replace_malloc.c:207)
==24549==    by 0xB323D52: __pyx_f_4sage_5rings_7integer_fast_tp_new (integer.c:19858)
==24549==    by 0xB344219: __pyx_f_4sage_5rings_7integer_7Integer__floordiv (integer.c:7921)
==24549==    by 0xB343FFF: __pyx_pf_4sage_5rings_7integer_7Integer___floordiv__ (integer.c:8020)
==24549==    by 0x41580C: binary_op1 (abstract.c:398)
==24549==    by 0x416CDD: PyNumber_FloorDivide (abstract.c:450)
==24549==    by 0x10FB29B1: __pyx_pf_4sage_5rings_10polynomial_28polynomial_integer_dense_ntl_28Polynomial_integer_dense_ntl
___floordiv__(_object*, _object*) (polynomial_integer_dense_ntl.cpp:4779)
==24549==    by 0x41580C: binary_op1 (abstract.c:398)
==24549==    by 0x416CDD: PyNumber_FloorDivide (abstract.c:450)
==24549==    by 0x142523FE: __pyx_pf_4sage_5rings_12number_field_16totallyreal_data_lagrange_degree_3 (totallyreal_data.c:39
75)
==24549==    by 0x415542: PyObject_Call (abstract.c:1860)
==24549==    by 0x14271583: __pyx_pf_4sage_5rings_12number_field_16totallyreal_data_7tr_data_incr (totallyreal_data.c:7355)
```

In total:

```
==24549==    definitely lost: 196,328 bytes in 4,087 blocks.
==24549==    indirectly lost: 36,148 bytes in 4,090 blocks.
==24549==      possibly lost: 267,538 bytes in 814 blocks.
==24549==    still reachable: 30,329,036 bytes in 188,033 blocks.
==24549==         suppressed: 0 bytes in 0 blocks.
```


Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/2239





---

archive/issue_comments_014797.json:
```json
{
    "body": "So there's definitely a leak somewhere here, but it's not in the totallyreal code. For example, if you define:\n\n\n```\ndef foo(f):\n    tmp = f.list()\n    rts = numpy.roots(tmp)\n```\n\n\nand run this with a `polynomial_integer_dense_ntl` as input, it'll leak like crazy. If you pass it anything else, it doesn't leak at all. It's something to do with the interaction between NTL and numpy, though I don't understand what the problem is yet. In particular, if you run either of the two lines above independently, over and over, you don't get a memory leak. It's only in concert that they leak ...\n\nIf someone understands this, they should explain it to me. :) In any event, it's not in the totallyreal code ...\n\n-cc",
    "created_at": "2008-02-28T06:57:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2239#issuecomment-14797",
    "user": "https://github.com/craigcitro"
}
```

So there's definitely a leak somewhere here, but it's not in the totallyreal code. For example, if you define:


```
def foo(f):
    tmp = f.list()
    rts = numpy.roots(tmp)
```


and run this with a `polynomial_integer_dense_ntl` as input, it'll leak like crazy. If you pass it anything else, it doesn't leak at all. It's something to do with the interaction between NTL and numpy, though I don't understand what the problem is yet. In particular, if you run either of the two lines above independently, over and over, you don't get a memory leak. It's only in concert that they leak ...

If someone understands this, they should explain it to me. :) In any event, it's not in the totallyreal code ...

-cc



---

archive/issue_comments_014798.json:
```json
{
    "body": "SOLUTION: If you change the list into a list of Python ints (which is surely what numpy is vastly more comfortable with) taht completely gets rid of the memory leak.  I'm guessing numpy is just doing some sort of black magic to convert the list to some internal format, and it makes assumptions that aren't satisfied by Sage integers.  The right solution is to give numpy standard Python input, so it can do whatever black magic it wants under valid assumptions.  The code below illustrates how to do this.\n\n\n\n```\nid=115|\nimport numpy\ndef foo(f):\n    tmp = [int(a) for a in f.list()]\n    rts = numpy.roots(tmp)\n```\n\n\n\n```\nid=114|\nx = polygen(ZZ)\nf = x^10 - 1\nprint get_memory_usage()\nfor _ in xrange(10^4): a = foo(f)\nprint get_memory_usage()\n///\n172M+\n172M+\n```\n",
    "created_at": "2008-02-28T17:33:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2239#issuecomment-14798",
    "user": "https://github.com/williamstein"
}
```

SOLUTION: If you change the list into a list of Python ints (which is surely what numpy is vastly more comfortable with) taht completely gets rid of the memory leak.  I'm guessing numpy is just doing some sort of black magic to convert the list to some internal format, and it makes assumptions that aren't satisfied by Sage integers.  The right solution is to give numpy standard Python input, so it can do whatever black magic it wants under valid assumptions.  The code below illustrates how to do this.



```
id=115|
import numpy
def foo(f):
    tmp = [int(a) for a in f.list()]
    rts = numpy.roots(tmp)
```



```
id=114|
x = polygen(ZZ)
f = x^10 - 1
print get_memory_usage()
for _ in xrange(10^4): a = foo(f)
print get_memory_usage()
///
172M+
172M+
```




---

archive/issue_comments_014799.json:
```json
{
    "body": "Sorry, I forgot to delete the id's:\n\n\n```\nimport numpy\ndef foo(f):\n    tmp = [int(a) for a in f.list()]\n    rts = numpy.roots(tmp)\n```\n\n\n\n```\nx = polygen(ZZ)\nf = x^10 - 1\nprint get_memory_usage()\nfor _ in xrange(10^4): a = foo(f)\nprint get_memory_usage()\n///\n172M+\n172M+\n```\n",
    "created_at": "2008-02-28T17:34:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2239#issuecomment-14799",
    "user": "https://github.com/williamstein"
}
```

Sorry, I forgot to delete the id's:


```
import numpy
def foo(f):
    tmp = [int(a) for a in f.list()]
    rts = numpy.roots(tmp)
```



```
x = polygen(ZZ)
f = x^10 - 1
print get_memory_usage()
for _ in xrange(10^4): a = foo(f)
print get_memory_usage()
///
172M+
172M+
```




---

archive/issue_comments_014800.json:
```json
{
    "body": "I followed Will's advice to fix the memleak.  Please review--it worked for me.  JV",
    "created_at": "2008-02-29T20:04:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2239#issuecomment-14800",
    "user": "https://github.com/jvoight"
}
```

I followed Will's advice to fix the memleak.  Please review--it worked for me.  JV



---

archive/issue_comments_014801.json:
```json
{
    "body": "Attachment [8685.patch](tarball://root/attachments/some-uuid/ticket2239/8685.patch) by @jvoight created at 2008-02-29 20:04:46",
    "created_at": "2008-02-29T20:04:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2239#issuecomment-14801",
    "user": "https://github.com/jvoight"
}
```

Attachment [8685.patch](tarball://root/attachments/some-uuid/ticket2239/8685.patch) by @jvoight created at 2008-02-29 20:04:46



---

archive/issue_comments_014802.json:
```json
{
    "body": "The patch looks ok to me.",
    "created_at": "2008-03-02T17:39:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2239#issuecomment-14802",
    "user": "https://github.com/JohnCremona"
}
```

The patch looks ok to me.



---

archive/issue_comments_014803.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-02T18:03:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2239#issuecomment-14803",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014804.json:
```json
{
    "body": "Merged in Sage 2.10.3.rc1. This patch is a work around and William, Travis, Gary, Josh and various other people have tracked the issue down, so there will be a new ticket about this.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-02T18:03:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2239#issuecomment-14804",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.3.rc1. This patch is a work around and William, Travis, Gary, Josh and various other people have tracked the issue down, so there will be a new ticket about this.

Cheers,

Michael



---

archive/issue_events_002409.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-03-02T18:03:02Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2239",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2239#event-2409"
}
```
