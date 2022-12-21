# Issue 8412: Trivial Center of Matrix Group

Issue created by migration from Trac.

Original creator: iandrus

Original creation time: 2010-03-01 22:46:04

Assignee: joyner

When calculating the center of a group, GAP returns an empty list of generators if the center is trivial.  This however throws off the creation of the MatrixGroup in Sage which checks to ensure that there is at least one generator.


```
sage: a=Matrix(FiniteField(5),
....: [[2,0,0],
....: [0,3,0],
....: [0,0,1]])
sage: 
sage: b=Matrix(FiniteField(5),
....: [[0,1,0],
....: [4,0,0],
....: [0,0,1]])
sage: 
sage: c=Matrix(FiniteField(5),
....: [[1,0,0],
....: [0,1,0],
....: [0,1,1]])
sage: 
sage: d=Matrix(FiniteField(5),
....: [[1,0,0],
....: [0,1,0],
....: [1,0,1]])
sage: 
sage: G = MatrixGroup([a,b,c,d])
sage: G.center()
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/Users/gvol/Desktop/Sage-4.3.1.rc1.app/Contents/Resources/sage/<ipython console> in <module>()

/Users/gvol/Desktop/Sage-4.3.1.rc1.app/Contents/Resources/sage/local/lib/python2.6/site-packages/sage/groups/matrix_gps/matrix_group.pyc in center(self)
    733         F = self.field_of_definition()
    734         from sage.groups.matrix_gps.matrix_group import MatrixGroup
--> 735         self.__center = MatrixGroup([g._matrix_(F) for g in G])
    736         return self.__center
    737     

/Users/gvol/Desktop/Sage-4.3.1.rc1.app/Contents/Resources/sage/local/lib/python2.6/site-packages/sage/groups/matrix_gps/matrix_group.pyc in MatrixGroup(gens)
    156     """
    157     if len(gens) == 0:
--> 158         raise ValueError, "gens must have positive length"
    159     try:
    160         R = gens[0].base_ring()

ValueError: gens must have positive length
```



---

Comment by iandrus created at 2010-03-01 23:07:16

Changing status from new to needs_review.


---

Comment by iandrus created at 2010-03-01 23:07:16

I added a patch which checks for a trivial center, and uses the identity for the group as a generator in this case.  

Sorry for the trailing whitespace differences.


---

Comment by wdj created at 2010-03-01 23:15:23

Replying to [comment:1 iandrus]:
> I added a patch which checks for a trivial center, and uses the identity for the group as a generator in this case.  
> 
> Sorry for the trailing whitespace differences.

Thank you for noticing this problem and submitting a patch.

I have not tested your patch yet, but it does not seem form reading the patch code that you have also added an example to the docstring which *tests* your new patch. If this is correct, can you please consider doing that?


---

Comment by iandrus created at 2010-03-01 23:35:26

Changing status from needs_review to needs_work.


---

Comment by iandrus created at 2010-03-01 23:35:26

Oops, you're absolutely right.  I'll get to it tomorrow.


---

Attachment


---

Comment by iandrus created at 2010-03-02 11:06:06

Changing status from needs_work to needs_review.


---

Comment by iandrus created at 2010-03-02 11:06:06

Okay, new patch up.


---

Comment by wdj created at 2010-03-03 00:37:45

Seems to apply okay (there was some "fuzz") to sage 4.3.3.a1 on a 10.6.2 mac. Pases sage -testall.

Patch looks good to me.


---

Comment by wdj created at 2010-03-03 00:37:45

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-03-03 02:51:03

properly folded patch; apply only this one


---

Attachment

It looks like [trac_8412_trivial_center.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8412/trac_8412_trivial_center.patch) consists of two patch files rolled into one, as evident from this snippet:

```
     ::
-    
+
         sage: F = GF(5); MS = MatrixSpace(F,2,2)
         sage: G = MatrixGroup([MS.0])
         Traceback (most recent call last):
# HG changeset patch
# User Ivan Andrus <darthandrus`@`gmail.com>
# Date 1267527460 -3600
# Node ID fa0a59cf132bca55c4500e7c134157e57a23dc3d
# Parent  023d02e0af46ae4e4450e3f2f14db54345aa8774
Added doctest for trivial center patch

diff -r 023d02e0af46 -r fa0a59cf132b sage/groups/matrix_gps/matrix_group.py
--- a/sage/groups/matrix_gps/matrix_group.py	Mon Mar 01 23:52:39 2010 +0100
+++ b/sage/groups/matrix_gps/matrix_group.py	Tue Mar 02 11:57:40 2010 +0100
`@``@` -739,6 +739,11 `@``@`
```

A patch file shouldn't be like that. I have attached the same patch, which also include the ticket number in the commit message. (Every commit message must have a ticket number.)


---

Comment by mvngu created at 2010-03-03 13:54:42

Merged [trac_8412-folded.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8412/trac_8412-folded.patch).


---

Comment by mvngu created at 2010-03-03 13:54:42

Resolution: fixed
