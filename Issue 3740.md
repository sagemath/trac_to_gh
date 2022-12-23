# Issue 3740: sage-3.0.6 blocker -- pickle jar -- exactly one failure

Issue created by migration from https://trac.sagemath.org/ticket/3740

Original creator: was

Original creation time: 2008-07-29 14:58:24

Assignee: cwitty

CC:  mhansen


```
sage: sage.structure.sage_object.unpickle_all('pickle_jar-3.0.3')
** failed:  _class__sage_combinat_crystals_tensor_product_TensorProductOfCrystals__.sobj
Failed:
_class__sage_combinat_crystals_tensor_product_TensorProductOfCrystals__.sobj
Successfully unpickled 355 objects.
Failed to unpickle 1 objects.
```


Email to sage-combinat-devel:

```
Hi,

The only object from sage-3.0.3 that doesn't unpickle in sage-3.0.3.final is 

-----------------------
sage: sage.structure.sage_object.unpickle_all('pickle_jar-3.0.3')
** failed:  _class__sage_combinat_crystals_tensor_product_TensorProductOfCrystals__.sobj
Failed:
_class__sage_combinat_crystals_tensor_product_TensorProductOfCrystals__.sobj
Successfully unpickled 355 objects.
Failed to unpickle 1 objects.
-----------------------

I don't know anything about the stability of TensorProductOfCrystals.    I've attached the sobj
that doesn't unpickle.  This was pickled using sage-3.0.3 because of a loads/dumps doctest.
Please clarify if you want to fix this problem ASAP, or consider this to be a nonissue because
you consider that particular code unstable.

 -- William
```



---

Comment by bump created at 2008-07-30 00:49:45

Presumably the same bug:


```
sage: C = CrystalOfLetters(['A',3])
sage: v = C.list()[0]
sage: T = TensorProductOfCrystals(C, C, generators=[[v,v]])
sage: T == loads(dumps(T))
```


Returns an exception.


---

Comment by mhansen created at 2009-06-04 20:31:16

This is no longer valid


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: sage: C = CrystalOfLetters(['A',3])
sage: sage: v = C.list()[0]
sage: sage: T = TensorProductOfCrystals(C, C, generators=[[v,v]])
sage: sage: T == loads(dumps(T))
True
sage: sage: C = CrystalOfLetters(['A',3])
sage: sage: v = C.list()[0]
sage: sage: T = TensorProductOfCrystals(C, C, generators=[[v,v]])
sage: sage: T == loads(dumps(T))
True
sage: sage: C = CrystalOfLetters(['A',3])
sage: sage: v = C.list()[0]
sage: sage: T = TensorProductOfCrystals(C, C, generators=[[v,v]])
sage: sage: T == loads(dumps(T))
True
```



---

Comment by mhansen created at 2009-06-04 20:31:16

Resolution: invalid
