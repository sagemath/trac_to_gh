# Issue 4631: possible memory leak in matrix code?

archive/issues_004631.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  robertwb\n\nSo I was looking at another ticket, and noticed the following memory usage of Hermite normal form:\n\n\n```\nsage: M = random_matrix(ZZ,50,50)\n\nsage: get_memory_usage()\n'1104M+'\n\nsage: for _ in range(100): foo = M.hermite_form()\n   ....: \n\nsage: get_memory_usage()\n'1170M+'\n```\n\n\nIt could be that the memory is getting \"lost\" in some other way, but it might be nice to see why it's happening. In fact, it's probably got nothing to do with HNF:\n\n\n```\nsage: get_memory_usage()\n'1170M+'\n\nsage: for _ in range(100): foo = M.echelon_form()\n   ....: \n\nsage: get_memory_usage()\n'1237M+'\n```\n\n\nI'm happy to find out that there's a reasonable explanation for this.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4631\n\n",
    "created_at": "2008-11-27T00:34:14Z",
    "labels": [
        "memleak",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "possible memory leak in matrix code?",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4631",
    "user": "craigcitro"
}
```
Assignee: mabshoff

CC:  robertwb

So I was looking at another ticket, and noticed the following memory usage of Hermite normal form:


```
sage: M = random_matrix(ZZ,50,50)

sage: get_memory_usage()
'1104M+'

sage: for _ in range(100): foo = M.hermite_form()
   ....: 

sage: get_memory_usage()
'1170M+'
```


It could be that the memory is getting "lost" in some other way, but it might be nice to see why it's happening. In fact, it's probably got nothing to do with HNF:


```
sage: get_memory_usage()
'1170M+'

sage: for _ in range(100): foo = M.echelon_form()
   ....: 

sage: get_memory_usage()
'1237M+'
```


I'm happy to find out that there's a reasonable explanation for this.

Issue created by migration from https://trac.sagemath.org/ticket/4631





---

archive/issue_comments_034810.json:
```json
{
    "body": "This might be related to #4639.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-28T21:36:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4631",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4631#issuecomment-34810",
    "user": "mabshoff"
}
```

This might be related to #4639.

Cheers,

Michael



---

archive/issue_comments_034811.json:
```json
{
    "body": "This may be relevant here. Either way it warrants consideration to call %reset at the end of Sage, but that would be another ticket.\n\n```\nOn Mon, Dec 8, 2008 at 19:15, frank wang <f.yw@hotmail.com> wrote:\n> > Hi,\n> >\n> > I have a program with some variables consume a lot of memory. The first time\n> > I run it, it is fine. The second time I run it, I will get MemoryError. If I\n> > close the ipython and reopen it again, then I can run the program once. I am\n> > looking for a command to delete the intermediate variable once it is not\n> > used to save memory like in matlab clear command.\n\nHow are you running this program? Be aware that IPython may be holding\non to objects and preventing them from being deallocated. For example:\n\nIn [7]: !cat memtest.py\nclass A(object):\n    def __del__(self):\n        print 'Deleting %r' % self\n\n\na = A()\n\nIn [8]: %run memtest.py\n\nIn [9]: %run memtest.py\n\nIn [10]: %run memtest.py\n\nIn [11]: del a\n\nIn [12]:\nDo you really want to exit ([y]/n)?\n\n$ python memtest.py\nDeleting <__main__.A object at 0x915ab0>\n\n\nYou can remove some of these references with %reset and maybe a\ngc.collect() for good measure.\n\n\nIn [1]: %run memtest\n\nIn [2]: %run memtest\n\nIn [3]: %run memtest\n\nIn [4]: %reset\nOnce deleted, variables cannot be recovered. Proceed (y/[n])?  y\nDeleting <__main__.A object at 0xf3e950>\nDeleting <__main__.A object at 0xf3e6d0>\nDeleting <__main__.A object at 0xf3e930>\n\n-- Robert Kern \"I have come to believe that the whole world is an enigma, \na harmless enigma that is made terrible by our own mad attempt to interpret \nit as though it had an underlying truth.\" -- Umberto Eco _______________________________________________ \nNumpy-discussion mailing list Numpy-discussion@scipy.org \nhttp://projects.scipy.org/mailman/listinfo/numpy-discussion \n```\n",
    "created_at": "2008-12-10T06:26:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4631",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4631#issuecomment-34811",
    "user": "mabshoff"
}
```

This may be relevant here. Either way it warrants consideration to call %reset at the end of Sage, but that would be another ticket.

```
On Mon, Dec 8, 2008 at 19:15, frank wang <f.yw@hotmail.com> wrote:
> > Hi,
> >
> > I have a program with some variables consume a lot of memory. The first time
> > I run it, it is fine. The second time I run it, I will get MemoryError. If I
> > close the ipython and reopen it again, then I can run the program once. I am
> > looking for a command to delete the intermediate variable once it is not
> > used to save memory like in matlab clear command.

How are you running this program? Be aware that IPython may be holding
on to objects and preventing them from being deallocated. For example:

In [7]: !cat memtest.py
class A(object):
    def __del__(self):
        print 'Deleting %r' % self


a = A()

In [8]: %run memtest.py

In [9]: %run memtest.py

In [10]: %run memtest.py

In [11]: del a

In [12]:
Do you really want to exit ([y]/n)?

$ python memtest.py
Deleting <__main__.A object at 0x915ab0>


You can remove some of these references with %reset and maybe a
gc.collect() for good measure.


In [1]: %run memtest

In [2]: %run memtest

In [3]: %run memtest

In [4]: %reset
Once deleted, variables cannot be recovered. Proceed (y/[n])?  y
Deleting <__main__.A object at 0xf3e950>
Deleting <__main__.A object at 0xf3e6d0>
Deleting <__main__.A object at 0xf3e930>

-- Robert Kern "I have come to believe that the whole world is an enigma, 
a harmless enigma that is made terrible by our own mad attempt to interpret 
it as though it had an underlying truth." -- Umberto Eco _______________________________________________ 
Numpy-discussion mailing list Numpy-discussion@scipy.org 
http://projects.scipy.org/mailman/listinfo/numpy-discussion 
```




---

archive/issue_comments_034812.json:
```json
{
    "body": "Note that the latest upstream Cython 0.10.3 (merged in Sage 3.2.2.rc0 via #4798) improves things considerably:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: M = random_matrix(ZZ,50,50)\nsage: get_memory_usage()\n416.19921875\nsage: for _ in range(100): foo = M.hermite_form()\n....: \nsage: del foo\nsage: get_memory_usage()\n423.74609375\nsage: for _ in range(100): foo = M.hermite_form()\n....: \nsage: get_memory_usage()\n424.73828125\nsage: for _ in range(100): foo = M.hermite_form()\n....: \nsage: get_memory_usage()\n425.703125\n```\n",
    "created_at": "2008-12-14T17:53:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4631",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4631#issuecomment-34812",
    "user": "mabshoff"
}
```

Note that the latest upstream Cython 0.10.3 (merged in Sage 3.2.2.rc0 via #4798) improves things considerably:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: M = random_matrix(ZZ,50,50)
sage: get_memory_usage()
416.19921875
sage: for _ in range(100): foo = M.hermite_form()
....: 
sage: del foo
sage: get_memory_usage()
423.74609375
sage: for _ in range(100): foo = M.hermite_form()
....: 
sage: get_memory_usage()
424.73828125
sage: for _ in range(100): foo = M.hermite_form()
....: 
sage: get_memory_usage()
425.703125
```




---

archive/issue_comments_034813.json:
```json
{
    "body": "But #4639 does not improve this further. Note that \"base\" is the initial memory consumption:\n\n```\nsage: base=get_memory_usage()\nsage: M = random_matrix(ZZ,50,50)\nsage: for _ in range(100): foo = M.hermite_form()\n....: \nsage: get_memory_usage()-base\n7.5625\nsage: for _ in range(100): foo = M.hermite_form()\n....: \nsage: get_memory_usage()-base\n8.515625\nsage: for _ in range(100): foo = M.hermite_form()\n....: \nsage: get_memory_usage()-base\n9.5\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-12-17T04:39:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4631",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4631#issuecomment-34813",
    "user": "mabshoff"
}
```

But #4639 does not improve this further. Note that "base" is the initial memory consumption:

```
sage: base=get_memory_usage()
sage: M = random_matrix(ZZ,50,50)
sage: for _ in range(100): foo = M.hermite_form()
....: 
sage: get_memory_usage()-base
7.5625
sage: for _ in range(100): foo = M.hermite_form()
....: 
sage: get_memory_usage()-base
8.515625
sage: for _ in range(100): foo = M.hermite_form()
....: 
sage: get_memory_usage()-base
9.5
```


Cheers,

Michael



---

archive/issue_comments_034814.json:
```json
{
    "body": "#4883 might be relevant here.",
    "created_at": "2008-12-27T00:56:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4631",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4631#issuecomment-34814",
    "user": "burcin"
}
```

#4883 might be relevant here.



---

archive/issue_comments_034815.json:
```json
{
    "body": "The new Sage 3.2.3+eMPIRe build picked up the following leak in tut.py:\n\n```\n==5027== 8 bytes in 1 blocks are definitely lost in loss record 32 of 19,079\n==5027==    at 0x4C22FEB: malloc (vg_replace_malloc.c:207)\n==5027==    by 0x84B3A4B: __gmpz_init_set_si (in /home/mabshoff/build/eMPIRe/sage-3.2.3.final/local/lib/libgmp.so.3.4.1)\n==5027==    by 0x271A110A: __pyx_pf_4sage_6matrix_4misc_matrix_integer_sparse_rational_reconstruction (misc.c:129\n17)\n==5027==    by 0x417E92: PyObject_Call (abstract.c:1861)\n==5027==    by 0x25632FFA: __pyx_pf_4sage_6matrix_21matrix_integer_sparse_21Matrix_integer_sparse_rational_recons\ntruction (matrix_integer_sparse.c:8698)==5027==    by 0x417E92: PyObject_Call (abstract.c:1861)\n==5027==    by 0x271B2171: __pyx_pf_4sage_6matrix_4misc_matrix_rational_echelon_form_multimodular (misc.c:15034)\n==5027==    by 0x417E92: PyObject_Call (abstract.c:1861)\n==5027==    by 0x4816E1: PyEval_CallObjectWithKeywords (ceval.c:3442)\n==5027==    by 0x25CAAAE3: __pyx_pf_4sage_6matrix_22matrix_rational_sparse_22Matrix_rational_sparse__echelon_form\n_multimodular (matrix_rational_sparse.c:12416)\n==5027==    by 0x417E92: PyObject_Call (abstract.c:1861)\n==5027==    by 0x4816E1: PyEval_CallObjectWithKeywords (ceval.c:3442)\n==5027==    by 0x25CABA89: __pyx_pf_4sage_6matrix_22matrix_rational_sparse_22Matrix_rational_sparse_echelon_form \n(matrix_rational_sparse.c:12116)\n```\n\nWilliam says:\n\n```\n[6:49pm] mabs: Yeah, I need to start poking around.\n[6:52pm] wstein: That could only leak if there is an exception raised somewhere in the body of the function.\n[6:52pm] wstein: In misc.pyx\n[6:53pm] wstein: So an exception must be raised.\n[6:54pm] wstein: maybe line 235 of matrix/misc.pyx could raise an exception,\n[6:54pm] wstein: hence return from that function without clearing gmp vars\n[6:58pm] mabs: mmhh\n```\n",
    "created_at": "2009-01-04T03:05:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4631",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4631#issuecomment-34815",
    "user": "mabshoff"
}
```

The new Sage 3.2.3+eMPIRe build picked up the following leak in tut.py:

```
==5027== 8 bytes in 1 blocks are definitely lost in loss record 32 of 19,079
==5027==    at 0x4C22FEB: malloc (vg_replace_malloc.c:207)
==5027==    by 0x84B3A4B: __gmpz_init_set_si (in /home/mabshoff/build/eMPIRe/sage-3.2.3.final/local/lib/libgmp.so.3.4.1)
==5027==    by 0x271A110A: __pyx_pf_4sage_6matrix_4misc_matrix_integer_sparse_rational_reconstruction (misc.c:129
17)
==5027==    by 0x417E92: PyObject_Call (abstract.c:1861)
==5027==    by 0x25632FFA: __pyx_pf_4sage_6matrix_21matrix_integer_sparse_21Matrix_integer_sparse_rational_recons
truction (matrix_integer_sparse.c:8698)==5027==    by 0x417E92: PyObject_Call (abstract.c:1861)
==5027==    by 0x271B2171: __pyx_pf_4sage_6matrix_4misc_matrix_rational_echelon_form_multimodular (misc.c:15034)
==5027==    by 0x417E92: PyObject_Call (abstract.c:1861)
==5027==    by 0x4816E1: PyEval_CallObjectWithKeywords (ceval.c:3442)
==5027==    by 0x25CAAAE3: __pyx_pf_4sage_6matrix_22matrix_rational_sparse_22Matrix_rational_sparse__echelon_form
_multimodular (matrix_rational_sparse.c:12416)
==5027==    by 0x417E92: PyObject_Call (abstract.c:1861)
==5027==    by 0x4816E1: PyEval_CallObjectWithKeywords (ceval.c:3442)
==5027==    by 0x25CABA89: __pyx_pf_4sage_6matrix_22matrix_rational_sparse_22Matrix_rational_sparse_echelon_form 
(matrix_rational_sparse.c:12116)
```

William says:

```
[6:49pm] mabs: Yeah, I need to start poking around.
[6:52pm] wstein: That could only leak if there is an exception raised somewhere in the body of the function.
[6:52pm] wstein: In misc.pyx
[6:53pm] wstein: So an exception must be raised.
[6:54pm] wstein: maybe line 235 of matrix/misc.pyx could raise an exception,
[6:54pm] wstein: hence return from that function without clearing gmp vars
[6:58pm] mabs: mmhh
```




---

archive/issue_comments_034816.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-04T03:05:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4631",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4631#issuecomment-34816",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_034817.json:
```json
{
    "body": "This seems to be fixed in sage-4.3:\n\n\n```\nsage: M = random_matrix(ZZ, 50, 50)\nsage: get_memory_usage()\n182.859375\nsage: for _ in range(100): foo = M.echelon_form()\n....: \nsage: get_memory_usage()\n183.32421875\nsage: for _ in range(100): foo = M.hermite_form()\n....: \nsage: get_memory_usage()\n183.32421875\n```\n\n\nGiven that it was vague to start with, I'm closing this as worksforme. (I tested on my machine and sage.math, with the same results.)",
    "created_at": "2010-01-17T19:13:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4631",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4631#issuecomment-34817",
    "user": "craigcitro"
}
```

This seems to be fixed in sage-4.3:


```
sage: M = random_matrix(ZZ, 50, 50)
sage: get_memory_usage()
182.859375
sage: for _ in range(100): foo = M.echelon_form()
....: 
sage: get_memory_usage()
183.32421875
sage: for _ in range(100): foo = M.hermite_form()
....: 
sage: get_memory_usage()
183.32421875
```


Given that it was vague to start with, I'm closing this as worksforme. (I tested on my machine and sage.math, with the same results.)



---

archive/issue_comments_034818.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2010-01-17T19:13:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4631",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4631#issuecomment-34818",
    "user": "craigcitro"
}
```

Resolution: worksforme
