# Issue 4105: multiplication of permutations in distinct subgroups sometimes doesn't work

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-09-12 15:47:05

Assignee: joyner

I think the following session (reported by Beezer) says it all:


```
tetra=AlternatingGroup(4)
stab1=PermutationGroup_subgroup(tetra, ["(1,2,3)"])
stab4=PermutationGroup_subgroup(tetra, ["(2,3,4)"])
for g in stab1:
 for h in stab4:
   print g*h
///

Traceback (most recent call last):       print g*h
  File "/home/wstein/sage/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/", line 3, in <module>
    
  File "element.pyx", line 1090, in sage.structure.element.MonoidElement.__mul__ (sage/structure/element.c:7938)
  File "coerce.pyx", line 651, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6154)
  File "permgroup_element.pyx", line 463, in sage.groups.perm_gps.permgroup_element.PermutationGroupElement._r_action (sage/groups/perm_gps/permgroup_element.c:3598)
  File "permgroup_element.pyx", line 254, in sage.groups.perm_gps.permgroup_element.PermutationGroupElement.__init__ (sage/groups/perm_gps/permgroup_element.c:2097)
  File "/home/wstein/sage/local/lib/python2.5/site-packages/sage/groups/perm_gps/permgroup_named.py", line 134, in __init__
    raise ValueError, "n (=%s) must be >= 1"%n
ValueError: n (=0) must be >= 1
```



```
tetra=AlternatingGroup(4)
stab1=PermutationGroup_subgroup(tetra, ["(1,2,3)"])
stab4=PermutationGroup_subgroup(tetra, ["(2,3,4)"])
for g in stab1:
 for h in stab4:
   print tetra(g)*tetra(h)
///

()
(2,3,4)
(2,4,3)
(1,2,3)
(1,3)(2,4)
(1,4,3)
(1,3,2)
(1,4,2)
(1,2)(3,4)
```



---

Comment by wdj created at 2008-09-13 01:59:28

I'm not sure I should be the owner of this. I guess the _mul_ method should be changed to coerce the PermutationGroup elements into a common parent (like SymmetricGroup(n), where n =
largest_moved_point=LargestMovedPoint). Now the module for permutation_group_element is in Cython and the method _mul_ seems to be renamed as cdef MonoidElement _mul_c_impl ?
I don't know how to make the changes though, sorry.


---

Comment by jason created at 2008-09-17 18:27:09

Apparently #4139 fixes this, according to the description there.


---

Comment by mabshoff created at 2008-10-31 03:14:10

This remains unfixed by #4139:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.1.4, Release Date: 2008-10-16                       |
| Type notebook() for the GUI, and license() for information.        |
sage: tetra=AlternatingGroup(4)
sage: stab1=PermutationGroup_subgroup(tetra, ["(1,2,3)"])
sage: stab4=PermutationGroup_subgroup(tetra, ["(2,3,4)"])
sage: for g in stab1:
....:      for h in stab4:
....:        print g*h
....: 
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)

/scratch/mabshoff/release-cycle/sage-3.1.3.final/<ipython console> in <module>()

/scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.MonoidElement.__mul__ (sage/structure/element.c:6829)()

/scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/python2.5/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:5206)()

/scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/python2.5/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.canonical_coercion (sage/structure/coerce.c:5743)()

/scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/python2.5/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.coercion_maps (sage/structure/coerce.c:6842)()

/scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/python2.5/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.discover_coercion (sage/structure/coerce.c:8090)()

/scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/python2.5/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.coerce_map_from (sage/structure/parent.c:7495)()

/scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/python2.5/site-packages/sage/groups/perm_gps/permgroup.pyc in __cmp__(self, other)
   1910         c = cmp(self.ambient_group(), other.ambient_group())
   1911         if c: return c
-> 1912         if self.is_subgroup(other):
   1913             return -1
   1914         else:

/scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/python2.5/site-packages/sage/groups/perm_gps/permgroup.pyc in is_subgroup(self, other)
   1541         for i in range(len(gens)):
   1542             x = gens[i]
-> 1543             if not (G.has_element(x)):
   1544                 return False
   1545         return True

/scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/python2.5/site-packages/sage/groups/perm_gps/permgroup.pyc in has_element(self, item)
    491 
    492         """
--> 493         item = PermutationGroupElement(item, self, check=False)
    494         return item in self.list()
    495 

/scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/python2.5/site-packages/sage/groups/perm_gps/permgroup_element.so in sage.groups.perm_gps.permgroup_element.PermutationGroupElement.__init__ (sage/groups/perm_gps/permgroup_element.c:2663)()

AssertionError: 
sage: 
Exiting SAGE (CPU time 0m1.22s, Wall time 0m28.50s).
Exiting spawned Gap process.
```


Cheers,

Michael


---

Comment by ppurka created at 2012-03-20 06:07:13

Sorry for the necro, but this seems fixed at least in sage-5.0beta2.

```
sage: tetra=AlternatingGroup(4)
sage: stab1=PermutationGroup_subgroup(tetra, ["(1,2,3)"])
sage: stab4=PermutationGroup_subgroup(tetra, ["(2,3,4)"])
sage: for g in stab1:
....:     for h in stab4:
....:         print g*h
....:         
()
(2,3,4)
(2,4,3)
(1,2,3)
(1,3)(2,4)
(1,4,3)
(1,3,2)
(1,4,2)
(1,2)(3,4)
```



---

Comment by tscrim created at 2012-12-10 19:35:37

Works for me as well in `5.5.rc0`.


---

Comment by tscrim created at 2012-12-10 19:35:37

Changing status from new to needs_review.


---

Comment by knsam created at 2013-02-02 10:18:33

Works for me in Sage 5.6. So, I'd give this positive review.


---

Comment by knsam created at 2013-02-02 10:18:52

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-02-03 19:20:34

Resolution: worksforme
