# Issue 6775: Having an easy to use Disjoint Set data structure

Issue created by migration from Trac.

Original creator: slabbe

Original creation time: 2009-08-19 18:29:55

Assignee: mhansen

CC:  rlm

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






---

Comment by slabbe created at 2009-08-19 18:59:43

I just added a patch. I have two issues :

1. I still have some problems with pikling :


```
slabbe`@`slabbe-laptop:~/sage-4.1/devel/sage-combinat/sage/sets$ sage
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

Comment by slabbe created at 2009-11-02 10:23:03

Changing assignee from mhansen to slabbe.


---

Comment by rlm created at 2009-11-05 21:12:41

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

Comment by slabbe created at 2009-11-24 14:31:01

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

Comment by slabbe created at 2009-11-24 14:31:01

Changing status from needs_work to needs_review.


---

Comment by rlm created at 2009-11-24 17:07:09

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

Comment by rlm created at 2009-11-24 17:07:09

Changing status from needs_review to needs_work.


---

Comment by slabbe created at 2009-11-24 17:50:21

The patch trac_6775-with_dealloc-sl.patch puts back the dealloc. I now get a mysterious error :


```
slabbe`@`pol:~/sage-4.2/devel/sage-combinat/sage/sets$ sage -t disjoint_set.pyx
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

Comment by rlm created at 2009-11-24 19:18:20

http://wiki.sagemath.org/ValgrindingSage

You may need to build a fresh version of Sage to use valgrind with it, see the above link for details. Once you get it built, and get your patch attached, you can run the doctest session in valgrind mode, and when it segfaults, valgrind will tell you what leaked.


---

Comment by rlm created at 2009-11-24 19:18:51

PS - Make sure to do this on a Linux box :)


---

Comment by slabbe created at 2010-01-19 17:14:11

Finally, `sage -t -verbose` gave me enough information to solve the problem. There was one doctest doing :


```
sage: DisjointSet(-1)
```


to illustrate that the argument must be non negative. The test `arg < 0` was done inside the `__init__` function of the class so that the attribute `_nodes` was not initialized if an error was raised before. Then, `__dealloc__` was trying to call `OP_dealloc` on a non existing `_nodes` : BOOM!

I moved the `arg < 0` test in the `DisjointSet` function and All tests passed : great !

I just uploaded the second patch.


---

Comment by slabbe created at 2010-01-19 17:31:55

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

Attachment

Applies over the precedent patch.


---

Comment by slabbe created at 2010-02-01 17:26:30

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

Comment by slabbe created at 2010-02-01 17:27:30

Needs review! (Both patches together).


---

Comment by slabbe created at 2010-02-01 17:27:30

Changing status from needs_work to needs_review.


---

Comment by rlm created at 2010-02-06 19:45:05

Are you still having the same problems building the documentation?

If you are, then you should know that both `OP_` and `PS_` -`represent` are functions which are only intended to illustrate a point. In fact, you could change their default arguments to `None` and simply feed in the original arguments in the doctests, since that is their only purpose.


---

Comment by slabbe created at 2010-02-07 16:28:32

Apply only this one.


---

Attachment

Good point. I followed your suggestion and I folded both precedent patches.

Needs review!


---

Comment by rlm created at 2010-02-07 20:29:33

Good work!


---

Comment by rlm created at 2010-02-07 20:29:33

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-02-07 20:29:50

Changing type from defect to enhancement.


---

Comment by mpatel created at 2010-02-11 14:47:53

Resolution: fixed
