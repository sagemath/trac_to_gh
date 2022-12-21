# Issue 2573: problem with Abelian groups and trivial elements

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2008-03-17 18:12:34

Assignee: mabshoff

CC:  ncalexan

Keywords: trivial abelian group class group

This is a problem:


```
sage: AbelianGroup(1, [1], names='e')
Trivial Abelian Group
sage: AbelianGroup(1, [1], names='e').list()
[]
```


The handling of 1's in the list of element orders is a problem:


```
sage: AbelianGroup(3, [2, 1, 2], names=list('abc')).list()
---------------------------------------------------------------------------
<type 'exceptions.IndexError'>            Traceback (most recent call last)

/Users/ncalexan/Documents/School/MATH235/genus2cm/<ipython console> in <module>()

/Users/ncalexan/sage-2.10.3.rc3/local/lib/python2.5/site-packages/sage/groups/abelian_gps/abelian_group.py in AbelianGroup(n, invfac, names)
    304     elif len(invfac) > n:
    305         raise ValueError, "invfac (=%s) must have length n (=%s)"%(invfac, n)
--> 306     M = AbelianGroup_class(n, invfac, names)
    307     return M
    308 

/Users/ncalexan/sage-2.10.3.rc3/local/lib/python2.5/site-packages/sage/groups/abelian_gps/abelian_group.py in __init__(self, n, invfac, names)
    371         # *now* define ngens
    372         self.__ngens = len(self.__invariants)
--> 373         self._assign_names(names)
    374 
    375 

/Users/ncalexan/Documents/School/MATH235/genus2cm/parent_gens.pyx in sage.structure.parent_gens.ParentWithGens._assign_names()

/Users/ncalexan/Documents/School/MATH235/genus2cm/parent_gens.pyx in sage.structure.parent_gens.normalize_names()

<type 'exceptions.IndexError'>: the number of names must equal the number of generators
```


This is the cause of strange things like:


```
sage: x = ZZ['x'].gen()
sage: K
Number Field in a with defining polynomial x^4 + 4*x^2 + 2
sage: K = NumberField(x^4 + 4*x^2 + 2, 'a')
sage: K.class_group()
Class group of order 1 with structure  of Number Field in a with defining polynomial x^4 + 4*x^2 + 2
```



---

Comment by mhansen created at 2008-03-17 20:04:54

Resolution: duplicate
