# Issue 4762: Odd error message for congruence subgroups

Issue created by migration from Trac.

Original creator: ljpk

Original creation time: 2008-12-11 19:43:52

Assignee: craigcitro

I was looking at generators of various different congruence subgroups, and got the following error:


```
sage: Gamma0(5).generators()[0]

[1 1]
[0 1]

sage: Gamma0(5).generators()[0] in Gamma0(7)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/home/ljpk/<ipython console> in <module>()

/home/was/s/local/lib/python2.5/site-packages/sage/groups/group.so in sage.groups.group.Group.__contains__ (sage/groups/group.c:1034)()

/home/was/s/local/lib/python2.5/site-packages/sage/modular/congroup.pyc in __call__(self, x, check)
   1654         if isinstance(x, CongruenceSubgroupElement) and x.parent() == self:
   1655             return x
-> 1656         x = CongruenceSubgroupElement(self, x, check=check)
   1657         if not check:
   1658             return x

/home/was/s/local/lib/python2.5/site-packages/sage/modular/congroup_element.pyc in __init__(self, parent, x, check)
     46             if not congroup.is_CongruenceSubgroup(parent):
     47                 raise TypeError, "parent (= %s) must be a congruence subgroup"%parent
---> 48             x = M2Z(x)
     49             if x.determinant() != 1:
     50                 raise ValueError, "matrix must have determinant 1"

/home/was/s/local/lib/python2.5/site-packages/sage/matrix/matrix_space.pyc in __call__(self, entries, coerce, copy, rows)
    306             entries = 0
    307
--> 308         if entries == 0 and hasattr(self, '__zero_matrix'):
    309             return self.zero_matrix()
    310

/home/was/s/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.Element.__richcmp__ (sage/structure/element.c:5247)()

/home/was/s/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.Element._richcmp (sage/structure/element.c:4954)()

/home/was/s/local/lib/python2.5/site-packages/sage/modular/congroup.pyc in __call__(self, x, check)
   1654         if isinstance(x, CongruenceSubgroupElement) and x.parent() == self:
   1655             return x
-> 1656         x = CongruenceSubgroupElement(self, x, check=check)
   1657         if not check:
   1658             return x

/home/was/s/local/lib/python2.5/site-packages/sage/modular/congroup_element.pyc in __init__(self, parent, x, check)
     48             x = M2Z(x)
     49             if x.determinant() != 1:
---> 50                 raise ValueError, "matrix must have determinant 1"
     51             x.set_immutable()
     52

ValueError: matrix must have determinant 1
```


It might be correct not to allow coercions from one congruence subgroup to another, but the matrix *does* have determinant 1, so the error message should be changed to one that is more suitable.


---

Comment by ljpk created at 2008-12-12 12:21:25

This error message also comes up for groups which genuinely are subgroups of one another:


```
sage: Gamma0(2).is_subgroup(SL2Z)
True
sage: Gamma0(2)([1,0,0,1]) in SL2Z
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/home/ljpk/congroup_upper.py in <module>()
----> 1
      2
      3
      4
      5

/home/was/s/local/lib/python2.5/site-packages/sage/groups/group.so in sage.groups.group.Group.__contains__ (sage/groups/group.c:1034)()
     46
     47
---> 48
     49
     50

/home/was/s/local/lib/python2.5/site-packages/sage/modular/congroup.pyc in __call__(self, x, check)
   1654         if isinstance(x, CongruenceSubgroupElement) and x.parent() == self:
   1655             return x
-> 1656         x = CongruenceSubgroupElement(self, x, check=check)
   1657         if not check:
   1658             return x

/home/was/s/local/lib/python2.5/site-packages/sage/modular/congroup_element.pyc in __init__(self, parent, x, check)
     46             if not congroup.is_CongruenceSubgroup(parent):
     47                 raise TypeError, "parent (= %s) must be a congruence subgroup"%parent
---> 48             x = M2Z(x)
     49             if x.determinant() != 1:
     50                 raise ValueError, "matrix must have determinant 1"

/home/was/s/local/lib/python2.5/site-packages/sage/matrix/matrix_space.pyc in __call__(self, entries, coerce, copy, rows)
    306             entries = 0
    307
--> 308         if entries == 0 and hasattr(self, '__zero_matrix'):
    309             return self.zero_matrix()
    310

/home/was/s/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.Element.__richcmp__ (sage/structure/element.c:5247)()
    556
    557
--> 558
    559
    560

/home/was/s/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.Element._richcmp (sage/structure/element.c:4954)()
    516
    517
--> 518
    519
    520

/home/was/s/local/lib/python2.5/site-packages/sage/modular/congroup.pyc in __call__(self, x, check)
   1654         if isinstance(x, CongruenceSubgroupElement) and x.parent() == self:
   1655             return x
-> 1656         x = CongruenceSubgroupElement(self, x, check=check)
   1657         if not check:
   1658             return x

/home/was/s/local/lib/python2.5/site-packages/sage/modular/congroup_element.pyc in __init__(self, parent, x, check)
     48             x = M2Z(x)
     49             if x.determinant() != 1:
---> 50                 raise ValueError, "matrix must have determinant 1"
     51             x.set_immutable()
     52

ValueError: matrix must have determinant 1

```



---

Attachment


---

Comment by AlexGhitza created at 2008-12-14 00:01:32

This is due to two underlying problems:

 * coercing an element of a congruence subgroup into the set of 2x2 integer matrices is broken
 * if g is an element of a congruence subgroup, testing g == 0 is broken

The attached patch fixes both issues.  Note that if CongruenceSubgroup were to inherit from MatrixGroup (which it probably should?), then the first problem would just go away.


---

Comment by craigcitro created at 2008-12-16 06:54:37

Patch looks good, but there are still some troubles in the code. Here's an example:


```
sage: G = Gamma0(5)

sage: G.0 in SL2Z
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (131, 0))

---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/Users/craigcitro/.sage/temp/sharma.local/18290/_Users_craigcitro__sage_init_sage_0.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

/sage/local/lib/python2.5/site-packages/sage/groups/group.so in sage.groups.group.Group.__contains__ (sage/groups/group.c:1034)()
     46 
     47 
---> 48 
     49 
     50 

/sage/local/lib/python2.5/site-packages/sage/modular/congroup.pyc in __call__(self, x, check)
   1665         if isinstance(x, CongruenceSubgroupElement) and x.parent() == self:
   1666             return x
-> 1667         x = CongruenceSubgroupElement(self, x, check=check)
   1668         if not check:
   1669             return x

/sage/local/lib/python2.5/site-packages/sage/modular/congroup_element.pyc in __init__(self, parent, x, check)
     49             if x.determinant() != 1:
     50                 raise TypeError, "matrix must have determinant 1"
---> 51             x.set_immutable()
     52 
     53         MultiplicativeGroupElement.__init__(self, parent)

/sage/local/lib/python2.5/site-packages/sage/matrix/matrix0.so in sage.matrix.matrix0.Matrix.set_immutable (sage/matrix/matrix0.c:3464)()
    407 
    408 
--> 409 
    410 
    411 

AttributeError: 'NoneType' object has no attribute 'set_immutable'

sage:
```


I'm


---

Comment by AlexGhitza created at 2008-12-20 12:58:03

I'm attaching an additional patch that fixes the issue reported by Craig, and doctests it.


---

Comment by AlexGhitza created at 2008-12-20 12:58:30

apply after the previous patch


---

Attachment

This is fine by me, but the congruence subgroup code really needs to be migrated to the new coercion model -- see #5048.


---

Comment by mabshoff created at 2009-01-23 10:26:49

Merged in Sage 3.3.alpha1

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-23 10:26:49

Resolution: fixed
