# Issue 6775: Create an interface for Disjoint Set data structure

archive/issues_006775.json:
```json
{
    "body": "Assignee: @seblabbe\n\nCC:  @rlmill\n\nKeywords: disjoint set data structure\n\nI would like to have an easy to use disjoint-set data structure like the one described here:\n\nhttp://en.wikipedia.org/wiki/Disjoint_set_data_structure\n\n```\nsage: d = DisjointSet(range(5))\nsage: d\n{{0}, {1}, {2}, {3}, {4}}\nsage: d.union(3,4)\nsage: d\n{{0}, {1}, {2}, {3, 4}}\nsage: d.union(0,2)\nsage: d\n{{0, 2}, {1}, {3, 4}}\nsage: d.union(1,4)\nsage: d.find(3)\n3\nsage: d.find(4)\n3\n```\n\nAs suggested [by Robert Miller on sage-devel](http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/4b6d5bb2983d81c2/f52adb855eb3b09f?lnk=gst&q=disjoint+set#f52adb855eb3b09f), one could use what is defined in\n\n`sage/groups/perm_gps/partn_ref/data_structures_*`\n\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6775\n\n",
    "closed_at": "2010-02-11T14:47:53Z",
    "created_at": "2009-08-19T18:29:55Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "Create an interface for Disjoint Set data structure",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6775",
    "user": "https://github.com/seblabbe"
}
```
Assignee: @seblabbe

CC:  @rlmill

Keywords: disjoint set data structure

I would like to have an easy to use disjoint-set data structure like the one described here:

http://en.wikipedia.org/wiki/Disjoint_set_data_structure

```
sage: d = DisjointSet(range(5))
sage: d
{{0}, {1}, {2}, {3}, {4}}
sage: d.union(3,4)
sage: d
{{0}, {1}, {2}, {3, 4}}
sage: d.union(0,2)
sage: d
{{0, 2}, {1}, {3, 4}}
sage: d.union(1,4)
sage: d.find(3)
3
sage: d.find(4)
3
```

As suggested [by Robert Miller on sage-devel](http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/4b6d5bb2983d81c2/f52adb855eb3b09f?lnk=gst&q=disjoint+set#f52adb855eb3b09f), one could use what is defined in

`sage/groups/perm_gps/partn_ref/data_structures_*`





Issue created by migration from https://trac.sagemath.org/ticket/6775





---

archive/issue_comments_055692.json:
```json
{
    "body": "I just added a patch. I have two issues :\n\n1. I still have some problems with pikling :\n\n```\nslabbe@slabbe-laptop:~/sage-4.1/devel/sage-combinat/sage/sets$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nLoading Sage library. Current Mercurial branch is: combinat\nsage: d = DisjointSet(5)\nsage: b = loads(dumps(d))\nsage: b\n| Sage Version 4.1, Release Date: 2009-07-09                         |\n| Type notebook() for the GUI, and license() for information.        |\n\n------------------------------------------------------------\nUnhandled SIGSEGV: A segmentation fault occured in SAGE.\nThis probably occured because a *compiled* component\nof SAGE has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run SAGE under gdb with 'sage -gdb' to debug this.\nSAGE will now terminate (sorry).\n------------------------------------------------------------\n```\n\n2. I am using the `__del__` function to call the `OP_dealloc`, but I not sure it is proper...",
    "created_at": "2009-08-19T18:59:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6775#issuecomment-55692",
    "user": "https://github.com/seblabbe"
}
```

I just added a patch. I have two issues :

1. I still have some problems with pikling :

```
slabbe@slabbe-laptop:~/sage-4.1/devel/sage-combinat/sage/sets$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: combinat
sage: d = DisjointSet(5)
sage: b = loads(dumps(d))
sage: b
| Sage Version 4.1, Release Date: 2009-07-09                         |
| Type notebook() for the GUI, and license() for information.        |

------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------
```

2. I am using the `__del__` function to call the `OP_dealloc`, but I not sure it is proper...



---

archive/issue_events_015969.json:
```json
{
    "actor": "https://github.com/seblabbe",
    "created_at": "2009-08-19T19:11:10Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6775",
    "milestone": "sage-4.1.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6775#event-15969"
}
```



---

archive/issue_comments_055693.json:
```json
{
    "body": "Changing assignee from @mwhansen to @seblabbe.",
    "created_at": "2009-11-02T10:23:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6775#issuecomment-55693",
    "user": "https://github.com/seblabbe"
}
```

Changing assignee from @mwhansen to @seblabbe.



---

archive/issue_comments_055694.json:
```json
{
    "body": "1. You should probably declare things like\n\n```\ncdef class DisjointSet_of_integers(SageObject):\n    cdef OrbitPartition *_nodes \n```\nand\n\n```\ncdef class DisjointSet_of_hashable(SageObject):\n   cdef list _int_to_el\n   cdef dict _el_to_int\n   cdef DisjointSet_of_integers _d\n```\nin `disjoint_set.pxd` instead of `disjoint_set.pyx`. That'll make it easier to use these classes elsewhere.\n\n2. You should have `__del__` print something and see if it's even getting called. I would define `__dealloc__` and see if that gets called instead. You're using `OP_dealloc` correctly.",
    "created_at": "2009-11-05T21:12:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6775#issuecomment-55694",
    "user": "https://github.com/rlmill"
}
```

1. You should probably declare things like

```
cdef class DisjointSet_of_integers(SageObject):
    cdef OrbitPartition *_nodes 
```
and

```
cdef class DisjointSet_of_hashable(SageObject):
   cdef list _int_to_el
   cdef dict _el_to_int
   cdef DisjointSet_of_integers _d
```
in `disjoint_set.pxd` instead of `disjoint_set.pyx`. That'll make it easier to use these classes elsewhere.

2. You should have `__del__` print something and see if it's even getting called. I would define `__dealloc__` and see if that gets called instead. You're using `OP_dealloc` correctly.



---

archive/issue_comments_055695.json:
```json
{
    "body": "I just replace the old patch and I solved the pickle problem. \n\nReplying to [comment:4 rlm]:\n> 1. You should probably declare things like\n  \n[snip]\n> in `disjoint_set.pxd` instead of `disjoint_set.pyx`. That'll make it easier to use these classes elsewhere.\n\n\nDone. Thanks for the comment. But is it really necessary since the function `DisjointSet` is the function used as a constructor? Should I also add that one to the `.pxd` ?\n\n> 2. You should have `__del__` print something and see if it's even getting called. I would define `__dealloc__` and see if that gets called instead. You're using `OP_dealloc` correctly.\n\n\nThe function `__del__` was not called, but `__dealloc__` is. Although, I am getting memory errors when using the `__dealloc__` function. I put a `pass` command in it and I get All test pass. Am I losing memory somewhere?\n\nNeeds review!",
    "created_at": "2009-11-24T14:31:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6775#issuecomment-55695",
    "user": "https://github.com/seblabbe"
}
```

I just replace the old patch and I solved the pickle problem. 

Replying to [comment:4 rlm]:
> 1. You should probably declare things like
  
[snip]
> in `disjoint_set.pxd` instead of `disjoint_set.pyx`. That'll make it easier to use these classes elsewhere.


Done. Thanks for the comment. But is it really necessary since the function `DisjointSet` is the function used as a constructor? Should I also add that one to the `.pxd` ?

> 2. You should have `__del__` print something and see if it's even getting called. I would define `__dealloc__` and see if that gets called instead. You're using `OP_dealloc` correctly.


The function `__del__` was not called, but `__dealloc__` is. Although, I am getting memory errors when using the `__dealloc__` function. I put a `pass` command in it and I get All test pass. Am I losing memory somewhere?

Needs review!



---

archive/issue_comments_055696.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-24T14:31:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6775#issuecomment-55696",
    "user": "https://github.com/seblabbe"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_055697.json:
```json
{
    "body": "Replying to [comment:5 slabbe]:\n> Replying to [comment:4 rlm]:\n> > 1. You should probably declare things like\n  \n> [snip]\n> > in `disjoint_set.pxd` instead of `disjoint_set.pyx`. That'll make it easier to use these classes elsewhere.\n\n> \n> Done. Thanks for the comment. But is it really necessary since the function `DisjointSet` is the function used as a constructor?\n\n\nIt would make things easier for developers using this later on, who want to use some Cython with this object. The DisjointSet function is a Python function, so it is irrelevant. I'm just talking about the class definitions.\n\n> > 2. You should have `__del__` print something and see if it's even getting called. I would define `__dealloc__` and see if that gets called instead. You're using `OP_dealloc` correctly.\n  \n> \n> The function `__del__` was not called, but `__dealloc__` is. Although, I am getting memory errors when using the `__dealloc__` function. I put a `pass` command in it and I get All test pass. Am I losing memory somewhere?\n\n\nYes, because your dealloc isn't doing anything. You should replace `pass` with `OP_dealloc(self._nodes)`.",
    "created_at": "2009-11-24T17:07:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6775#issuecomment-55697",
    "user": "https://github.com/rlmill"
}
```

Replying to [comment:5 slabbe]:
> Replying to [comment:4 rlm]:
> > 1. You should probably declare things like
  
> [snip]
> > in `disjoint_set.pxd` instead of `disjoint_set.pyx`. That'll make it easier to use these classes elsewhere.

> 
> Done. Thanks for the comment. But is it really necessary since the function `DisjointSet` is the function used as a constructor?


It would make things easier for developers using this later on, who want to use some Cython with this object. The DisjointSet function is a Python function, so it is irrelevant. I'm just talking about the class definitions.

> > 2. You should have `__del__` print something and see if it's even getting called. I would define `__dealloc__` and see if that gets called instead. You're using `OP_dealloc` correctly.
  
> 
> The function `__del__` was not called, but `__dealloc__` is. Although, I am getting memory errors when using the `__dealloc__` function. I put a `pass` command in it and I get All test pass. Am I losing memory somewhere?


Yes, because your dealloc isn't doing anything. You should replace `pass` with `OP_dealloc(self._nodes)`.



---

archive/issue_comments_055698.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-11-24T17:07:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6775#issuecomment-55698",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_055699.json:
```json
{
    "body": "The patch trac_6775-with_dealloc-sl.patch puts back the dealloc. I now get a mysterious error :\n\n```\nslabbe@pol:~/sage-4.2/devel/sage-combinat/sage/sets$ sage -t disjoint_set.pyx\nsage -t  \"devel/sage-combinat/sage/sets/disjoint_set.pyx\"   \nA mysterious error (perhaps a memory error?) occurred, which may have crashed doctest.\n\t [2.3 s]\nexit code: 768\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n\tsage -t  \"devel/sage-combinat/sage/sets/disjoint_set.pyx\"\nTotal time for all tests: 2.3 seconds\n```\n\nToday I was not able to reproduce the same problem in the command line. Is there a way to get more informations on such a failed test?\n\nAlthough, adding a print statement in the `__init__` gives more information in the failed tests. I am getting the result below. Changing the print statement from one `__init__` to another changes the place where the memory error occur.\n\n```\n...\n**********************************************************************\nFile \"/home/slabbe/sage-4.2/devel/sage-combinat/sage/sets/disjoint_set.pyx\", line 744:\n    sage: d = DisjointSet(range(5))\nExpected nothing\nGot:\n    DisjointSet_of_hashable.__init__ called\n**********************************************************************\nFile \"/home/\n\n------------------------------------------------------------\nUnhandled SIGSEGV: A segmentation fault occured in SAGE.\nThis probably occured because a *compiled* component\nof SAGE has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, line 760:\n    sage: d = DisjointSet(range(5))\nExpected nothing\nGot:\n    DisjointSet_of_hashable.__init__ called\n**********************************************************************\nFile \"/home/slabbe/sage-4.2/devel/sage-combinat/sage/sets/disjoint_set.pyx\", line 781:\n    sage: d = DisjointSet(range(5))\nExpected nothing\nGot:\n    DisjointSet_of_hashable.__init__ called\n**********************************************************************\n...\n```\n\nWill I get the same problem at the same place if I redo all the doctests in the same order as in the file by hand directly in the command line. Can I reproduce the problem is my actual question.\n\nI think I also need to understand when exactly the `__dealloc__` is called.",
    "created_at": "2009-11-24T17:50:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6775#issuecomment-55699",
    "user": "https://github.com/seblabbe"
}
```

The patch trac_6775-with_dealloc-sl.patch puts back the dealloc. I now get a mysterious error :

```
slabbe@pol:~/sage-4.2/devel/sage-combinat/sage/sets$ sage -t disjoint_set.pyx
sage -t  "devel/sage-combinat/sage/sets/disjoint_set.pyx"   
A mysterious error (perhaps a memory error?) occurred, which may have crashed doctest.
	 [2.3 s]
exit code: 768
 
----------------------------------------------------------------------
The following tests failed:


	sage -t  "devel/sage-combinat/sage/sets/disjoint_set.pyx"
Total time for all tests: 2.3 seconds
```

Today I was not able to reproduce the same problem in the command line. Is there a way to get more informations on such a failed test?

Although, adding a print statement in the `__init__` gives more information in the failed tests. I am getting the result below. Changing the print statement from one `__init__` to another changes the place where the memory error occur.

```
...
**********************************************************************
File "/home/slabbe/sage-4.2/devel/sage-combinat/sage/sets/disjoint_set.pyx", line 744:
    sage: d = DisjointSet(range(5))
Expected nothing
Got:
    DisjointSet_of_hashable.__init__ called
**********************************************************************
File "/home/

------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, line 760:
    sage: d = DisjointSet(range(5))
Expected nothing
Got:
    DisjointSet_of_hashable.__init__ called
**********************************************************************
File "/home/slabbe/sage-4.2/devel/sage-combinat/sage/sets/disjoint_set.pyx", line 781:
    sage: d = DisjointSet(range(5))
Expected nothing
Got:
    DisjointSet_of_hashable.__init__ called
**********************************************************************
...
```

Will I get the same problem at the same place if I redo all the doctests in the same order as in the file by hand directly in the command line. Can I reproduce the problem is my actual question.

I think I also need to understand when exactly the `__dealloc__` is called.



---

archive/issue_comments_055700.json:
```json
{
    "body": "http://wiki.sagemath.org/ValgrindingSage\n\nYou may need to build a fresh version of Sage to use valgrind with it, see the above link for details. Once you get it built, and get your patch attached, you can run the doctest session in valgrind mode, and when it segfaults, valgrind will tell you what leaked.",
    "created_at": "2009-11-24T19:18:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6775#issuecomment-55700",
    "user": "https://github.com/rlmill"
}
```

http://wiki.sagemath.org/ValgrindingSage

You may need to build a fresh version of Sage to use valgrind with it, see the above link for details. Once you get it built, and get your patch attached, you can run the doctest session in valgrind mode, and when it segfaults, valgrind will tell you what leaked.



---

archive/issue_comments_055701.json:
```json
{
    "body": "PS - Make sure to do this on a Linux box :)",
    "created_at": "2009-11-24T19:18:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6775#issuecomment-55701",
    "user": "https://github.com/rlmill"
}
```

PS - Make sure to do this on a Linux box :)



---

archive/issue_comments_055702.json:
```json
{
    "body": "Finally, `sage -t -verbose` gave me enough information to solve the problem. There was one doctest doing :\n\n```\nsage: DisjointSet(-1)\n```\n\nto illustrate that the argument must be non negative. The test `arg < 0` was done inside the `__init__` function of the class so that the attribute `_nodes` was not initialized if an error was raised before. Then, `__dealloc__` was trying to call `OP_dealloc` on a non existing `_nodes` : BOOM!\n\nI moved the `arg < 0` test in the `DisjointSet` function and All tests passed : great !\n\nI just uploaded the second patch.",
    "created_at": "2010-01-19T17:14:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6775#issuecomment-55702",
    "user": "https://github.com/seblabbe"
}
```

Finally, `sage -t -verbose` gave me enough information to solve the problem. There was one doctest doing :

```
sage: DisjointSet(-1)
```

to illustrate that the argument must be non negative. The test `arg < 0` was done inside the `__init__` function of the class so that the attribute `_nodes` was not initialized if an error was raised before. Then, `__dealloc__` was trying to call `OP_dealloc` on a non existing `_nodes` : BOOM!

I moved the `arg < 0` test in the `DisjointSet` function and All tests passed : great !

I just uploaded the second patch.



---

archive/issue_comments_055703.json:
```json
{
    "body": "I am now having problem building the documentation...\n\n```\n/home/slabbe/sage-4.3/devel/sage/doc/en/reference/sage/sets/disjoint_set.rst:6: \n(WARNING/2) error while formatting signature for sage.sets.disjoint_set.OP_represent: \nCould not parse cython argspec\n/home/slabbe/sage-4.3/devel/sage/doc/en/reference/sage/sets/disjoint_set.rst:6: \n(WARNING/2) error while formatting signature for sage.sets.disjoint_set.PS_represent: \nCould not parse cython argspec\n```\n\nI will look at this before changing the status to `needs review`.",
    "created_at": "2010-01-19T17:31:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6775#issuecomment-55703",
    "user": "https://github.com/seblabbe"
}
```

I am now having problem building the documentation...

```
/home/slabbe/sage-4.3/devel/sage/doc/en/reference/sage/sets/disjoint_set.rst:6: 
(WARNING/2) error while formatting signature for sage.sets.disjoint_set.OP_represent: 
Could not parse cython argspec
/home/slabbe/sage-4.3/devel/sage/doc/en/reference/sage/sets/disjoint_set.rst:6: 
(WARNING/2) error while formatting signature for sage.sets.disjoint_set.PS_represent: 
Could not parse cython argspec
```

I will look at this before changing the status to `needs review`.



---

archive/issue_comments_055704.json:
```json
{
    "body": "Attachment [trac_6775-with_dealloc-sl.patch](tarball://root/attachments/some-uuid/ticket6775/trac_6775-with_dealloc-sl.patch) by @seblabbe created at 2010-01-19 17:44:53\n\nApplies over the precedent patch.",
    "created_at": "2010-01-19T17:44:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6775#issuecomment-55704",
    "user": "https://github.com/seblabbe"
}
```

Attachment [trac_6775-with_dealloc-sl.patch](tarball://root/attachments/some-uuid/ticket6775/trac_6775-with_dealloc-sl.patch) by @seblabbe created at 2010-01-19 17:44:53

Applies over the precedent patch.



---

archive/issue_comments_055705.json:
```json
{
    "body": "The docbuild problem comes from `_sage_getargspec_cython` which fails because it doesn't handle the presence of commas inside default value of arguments of a function. In fact, both `OP_represent` and `PS_represent` do use commas in their default arguments... \n\n```\nsage: from sage.misc.sageinspect import _sage_getargspec_cython\nsage: _sage_getargspec_cython('def PS_represent(partition=5, splits=[444]):')\n(['partition', 'splits'], None, None, (5, [444]))\nsage: _sage_getargspec_cython('def PS_represent(partition=5, splits=[444,4]):') \nTraceback (most recent call last):\n...\nValueError: Could not parse cython argspec\n```\n\nOne solution could be to avoid the presence of those two functions in the doc, but I don't know how to do this since they appear from the cython line\n\n```\ninclude '../groups/perm_gps/partn_ref/data_structures_pyx.pxi'\n```\nwhich includes everything in the file including `PS_represent` and `OP_represent` which are not needed for `disjoint_set.pyx`. Is it possible to include only what we need?\n\nI think this problem concerns something independant from this ticket (another ticket could be open for the comma problem). So I change the status of this ticket to `needs review`.",
    "created_at": "2010-02-01T17:26:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6775#issuecomment-55705",
    "user": "https://github.com/seblabbe"
}
```

The docbuild problem comes from `_sage_getargspec_cython` which fails because it doesn't handle the presence of commas inside default value of arguments of a function. In fact, both `OP_represent` and `PS_represent` do use commas in their default arguments... 

```
sage: from sage.misc.sageinspect import _sage_getargspec_cython
sage: _sage_getargspec_cython('def PS_represent(partition=5, splits=[444]):')
(['partition', 'splits'], None, None, (5, [444]))
sage: _sage_getargspec_cython('def PS_represent(partition=5, splits=[444,4]):') 
Traceback (most recent call last):
...
ValueError: Could not parse cython argspec
```

One solution could be to avoid the presence of those two functions in the doc, but I don't know how to do this since they appear from the cython line

```
include '../groups/perm_gps/partn_ref/data_structures_pyx.pxi'
```
which includes everything in the file including `PS_represent` and `OP_represent` which are not needed for `disjoint_set.pyx`. Is it possible to include only what we need?

I think this problem concerns something independant from this ticket (another ticket could be open for the comma problem). So I change the status of this ticket to `needs review`.



---

archive/issue_comments_055706.json:
```json
{
    "body": "Needs review! (Both patches together).",
    "created_at": "2010-02-01T17:27:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6775#issuecomment-55706",
    "user": "https://github.com/seblabbe"
}
```

Needs review! (Both patches together).



---

archive/issue_comments_055707.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-01T17:27:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6775#issuecomment-55707",
    "user": "https://github.com/seblabbe"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_055708.json:
```json
{
    "body": "Are you still having the same problems building the documentation?\n\nIf you are, then you should know that both `OP_` and `PS_` -`represent` are functions which are only intended to illustrate a point. In fact, you could change their default arguments to `None` and simply feed in the original arguments in the doctests, since that is their only purpose.",
    "created_at": "2010-02-06T19:45:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6775#issuecomment-55708",
    "user": "https://github.com/rlmill"
}
```

Are you still having the same problems building the documentation?

If you are, then you should know that both `OP_` and `PS_` -`represent` are functions which are only intended to illustrate a point. In fact, you could change their default arguments to `None` and simply feed in the original arguments in the doctests, since that is their only purpose.



---

archive/issue_comments_055709.json:
```json
{
    "body": "Apply only this one.",
    "created_at": "2010-02-07T16:28:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6775#issuecomment-55709",
    "user": "https://github.com/seblabbe"
}
```

Apply only this one.



---

archive/issue_comments_055710.json:
```json
{
    "body": "Attachment [trac_6775-disjoint_set-sl.patch](tarball://root/attachments/some-uuid/ticket6775/trac_6775-disjoint_set-sl.patch) by @seblabbe created at 2010-02-07 16:33:09\n\nGood point. I followed your suggestion and I folded both precedent patches.\n\nNeeds review!",
    "created_at": "2010-02-07T16:33:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6775#issuecomment-55710",
    "user": "https://github.com/seblabbe"
}
```

Attachment [trac_6775-disjoint_set-sl.patch](tarball://root/attachments/some-uuid/ticket6775/trac_6775-disjoint_set-sl.patch) by @seblabbe created at 2010-02-07 16:33:09

Good point. I followed your suggestion and I folded both precedent patches.

Needs review!



---

archive/issue_comments_055711.json:
```json
{
    "body": "Good work!",
    "created_at": "2010-02-07T20:29:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6775#issuecomment-55711",
    "user": "https://github.com/rlmill"
}
```

Good work!



---

archive/issue_comments_055712.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-07T20:29:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6775#issuecomment-55712",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_055713.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-02-07T20:29:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6775#issuecomment-55713",
    "user": "https://github.com/rlmill"
}
```

Changing type from defect to enhancement.



---

archive/issue_events_015970.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-02-11T14:47:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6775",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6775#event-15970"
}
```



---

archive/issue_comments_055714.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T14:47:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6775#issuecomment-55714",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
