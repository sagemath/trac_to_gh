# Issue 1296: Fast permutation arithmatic

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2007-11-28 05:44:18

Assignee: mhansen

CC:  sage-combinat

While patching CubeGroup, I noticed that permutation group arithmetic is was extremely slow (every operation passed through the GAP interface for instance). 

It makes sense to re-implement these simple operations in a fast Cython class. 


---

Attachment


---

Attachment


---

Comment by robertwb created at 2007-11-28 05:48:36

Changing assignee from mhansen to robertwb.


---

Attachment


---

Comment by robertwb created at 2007-11-28 18:24:48

Some benchmarks indicating a 4400x speedup. 

The old code:

```
sage: G = SymmetricGroup(10)
sage: g = G.random_element(); h = G.random_element()
sage: A = range(1000)
sage: time for _ in A: z = g*h
CPU time: 2.96 s,  Wall time: 3.09 s
sage: time for _ in A: z = g.sign()
CPU time: 1.36 s,  Wall time: 1.41 s
sage: time for _ in A: z = g.order()
CPU time: 1.36 s,  Wall time: 1.40 s
sage: time for _ in A: z = g.list()
CPU time: 0.95 s,  Wall time: 1.04 s
```


The new code (note the 10<sup>5</sup>, at 10<sup>3</sup> they were unmeasurably fast): 

```
sage: G = SymmetricGroup(10)
sage: g = G.random_element(); h = G.random_element()
sage: A = range(10^5)
sage: time for _ in A: z = g*h
CPU time: 0.07 s,  Wall time: 0.07 s
sage: time for _ in A: z = g.sign()
CPU time: 0.04 s,  Wall time: 0.04 s
sage: time for _ in A: z = g.order()
CPU time: 0.09 s,  Wall time: 0.09 s
sage: time for _ in A: z = g.list()
CPU time: 0.12 s,  Wall time: 0.12 s
```



---

Comment by robertwb created at 2007-11-28 18:24:48

Changing status from new to assigned.


---

Attachment


---

Attachment

Robert,  if I comment out the following doctest then everything passes (on 100 runs through).

```
        #sage: G1 = AlternatingGroup([1,2,4,5])
        #sage: G2 = AlternatingGroup([3,4,6,7])
        #sage: D = direct_product_permgroups([G1,G2,G1])
        #sage: D.order()
        #1728
        #sage: D = direct_product_permgroups([G1])
        #sage: D==G1
        #True
        #sage: direct_product_permgroups([])
        #Symmetric group of order 1! as a permutation group
```


Unfortunately, that doctest works perfectly if I do it from the command-line.


---

Comment by mabshoff created at 2007-12-11 02:01:54

After applying all patches and uncommenting the doctests for direct_product_permgroups like mhansen wrote above I get the following simple to fix doctests:

```
sage -t  devel/sage-main/sage/groups/perm_gps/permgroup.py  
**********************************************************************
File "permgroup.py", line 157:
    sage: G._gap_()
Expected:
    Group([ (1,2,3,4) ])
Got:
    Group( [ (1,2,3,4) ] )
**********************************************************************
File "permgroup.py", line 159:
    sage: gap(G)
Expected:
    Group([ (1,2,3,4) ])
Got:
    Group( [ (1,2,3,4) ] )
**********************************************************************
File "permgroup.py", line 1249:
    sage: G.normalizer(g)
Expected:
    Group([ (1,2,3,4), (1,3)(2,4), (2,4) ])
Got:
    Group( [ (1,2,3,4), (1,3)(2,4), (2,4) ] )
**********************************************************************
2 items had failures:
   2 of  10 in __main__.example_3
   1 of   5 in __main__.example_39
***Test Failed*** 3 failures.
For whitespace errors, see the file .doctest_permgroup.py
         [12.1 s]
exit code: 256
```


Cheers,

Michael


---

Comment by mabshoff created at 2007-12-11 02:13:22

Valgrind says:

```
==28125== Invalid write of size 4
==28125==    at 0x17B6BC9D: __pyx_pf_4sage_6groups_8perm_gps_17permgroup_element_23PermutationGroupElement___init__ (permgro
up_element.c:2237)
==28125==    by 0x458E40: type_call (typeobject.c:436)
==28125==    by 0x415542: PyObject_Call (abstract.c:1860)
==28125==    by 0x481AC1: PyEval_EvalFrameEx (ceval.c:3775)
==28125==    by 0x483C6A: PyEval_EvalFrameEx (ceval.c:3650)
==28125==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==28125==    by 0x4CDFF0: function_call (funcobject.c:517)
==28125==    by 0x415542: PyObject_Call (abstract.c:1860)
==28125==    by 0x41BC62: instancemethod_call (classobject.c:2497)
==28125==    by 0x415542: PyObject_Call (abstract.c:1860)
==28125==    by 0x481AC1: PyEval_EvalFrameEx (ceval.c:3775)
==28125==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==28125==  Address 0x533f868 is 0 bytes after a block of size 16 alloc'd
==28125==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)
==28125==    by 0x17B6C391: __pyx_pf_4sage_6groups_8perm_gps_17permgroup_element_23PermutationGroupElement___init__ (permgro
up_element.c:2075)
==28125==    by 0x458E40: type_call (typeobject.c:436)
==28125==    by 0x415542: PyObject_Call (abstract.c:1860)
==28125==    by 0x481AC1: PyEval_EvalFrameEx (ceval.c:3775)
==28125==    by 0x483C6A: PyEval_EvalFrameEx (ceval.c:3650)
==28125==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==28125==    by 0x4CDFF0: function_call (funcobject.c:517)
==28125==    by 0x415542: PyObject_Call (abstract.c:1860)
==28125==    by 0x41BC62: instancemethod_call (classobject.c:2497)
==28125==    by 0x415542: PyObject_Call (abstract.c:1860)
==28125==    by 0x481AC1: PyEval_EvalFrameEx (ceval.c:3775)
```


Cheers,

Michael


---

Comment by mabshoff created at 2007-12-11 02:46:38

Adding the following around line 267 of permgroup_element.pyx

```
        cdef int i
        print v
        print len(v)
        print self.n
        assert(len(v) <= self.n)
        for i from 0 <= i < len(v):
            self.perm[i] = v[i] - 1
        for i from len(v) <= i < self.n:
            self.perm[i] = i
```

produces:

```
sage: G1 = AlternatingGroup([1,2,4,5])
[2, 4, 3, 1]
4
4
[1, 4, 3, 5, 2]
5
4
---------------------------------------------------------------------------
<type 'exceptions.AssertionError'>        Traceback (most recent call last)

/tmp/Work-mabshoff/release-cycles-2.9/sage-2.9.alpha5/<ipython console> in <module>()

/tmp/Work-mabshoff/release-cycles-2.9/sage-2.9.alpha5/local/lib/python2.5/site-packages/sage/groups/perm_gps/permgroup_named.py in __init__(self, n)
    160         if isinstance(n, list):
    161             self._deg = len(n)
--> 162             PermutationGroup_generic.__init__(self, 'AlternatingGroup(%s)'%n, from_group = True)
    163         else:
    164             try:

/tmp/Work-mabshoff/release-cycles-2.9/sage-2.9.alpha5/local/lib/python2.5/site-packages/sage/groups/perm_gps/permgroup.py in __init__(self, gens, from_group, check)
    189         if from_group and isinstance(gens, str):
    190             self.__gap = gens
--> 191             self.gens()  # so will check that group can be defined in GAP (e.g., no missing packages, etc.)
    192             return
    193         if is_GapElement(gens):

/tmp/Work-mabshoff/release-cycles-2.9/sage-2.9.alpha5/local/lib/python2.5/site-packages/sage/groups/perm_gps/permgroup.py in gens(self)
    468             self.__gens = tuple([PermutationGroupElement(gens[n],
    469                                     self, check = False) for n in \
--> 470                                  range(1, int(gens.Length())+1)])
    471             return self.__gens
    472

/tmp/Work-mabshoff/release-cycles-2.9/sage-2.9.alpha5/permgroup_element.pyx in sage.groups.perm_gps.permgroup_element.PermutationGroupElement.__init__()

<type 'exceptions.AssertionError'>:
```


Cheers,

Michael


---

Comment by robertwb created at 2007-12-11 03:19:17

I had tried tracking this down, but to no avail. I bet that's it. 

The contents of v (if the user passes it in) really should be verified--I fear bad things can happen if it's not correct.


---

Comment by mabshoff created at 2007-12-11 03:54:23

Merged

 * 1296-fast-permgroup.patch
 * 1296-fast-permgroup2.patch
 * 1296-fast-permgroup3.patch
 * 1296-fast-permgroup4.patch
 * 1296-fast-permgroup5.patch
 * 1296-permgroup_element.pxd

in 2.9.alpha5. William also fixed the segfault issue.

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-11 05:27:42

Failing doctests with 2.9.alpha5, as far as I can tell all related to #1296:

 * devel/sage-main/sage/groups/group.pyx
 * devel/sage-main/sage/groups/abelian_gps/abelian_group.py
 * devel/sage-main/sage/gsl/dft.py
 * devel/sage-main/sage/calculus/calculus.py
 * devel/sage-main/sage/interfaces/gap.py
 * devel/sage-main/sage/functions/functions.py
 * devel/sage-main/sage/functions/constants.py
 * devel/sage-main/sage/rings/polynomial/polynomial_element.pyx
 * devel/sage-main/sage/rings/polynomial/polynomial_ring.py

Additionally also failures in tut.tex and const.tex.

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-14 06:58:06

The patches were merged in 2.9.alpha5, the doctests fixed in 2.9.alpha6.


---

Comment by mabshoff created at 2007-12-14 06:58:06

Resolution: fixed
