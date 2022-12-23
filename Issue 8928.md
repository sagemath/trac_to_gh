# Issue 8928: Infinite loop caused by Modules.ElementClass.__mul__

Issue created by migration from https://trac.sagemath.org/ticket/8928

Original creator: mguaypaq

Original creation time: 2010-05-07 20:51:19

Assignee: mguaypaq

CC:  vbraun tscrim

Keywords: categories, coercion, infinite loop

There is currently an infinite loop which seems to be a result of `Modules.ElementClass.__mul__` calling `get_coercion_model().bin_op(left, right, operator.mul)`, and `bin_op` calling `operator.mul(left, right)`.

Note that this behavior may even mask `ElementClass.__mul__` from other super-categories that actually implement multiplication.

Here is an illustrative example, showing a class that works (`MyRing1`) and one that breaks (`MyRing2`). The only difference between the two classes is the very last line.


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: class MyRing1(CombinatorialFreeModule):
....:     def __init__(self):
....:         R = QQ
....:         category = (ModulesWithBasis(R), Rngs())
....:         CombinatorialFreeModule.__init__(self, R, Partitions(), category = category)
....:     def product(self, left, right):
....:         return self.zero()
....:     class Element(CombinatorialFreeModule.Element):
....:         __mul__ = Rngs().element_class.__mul__
....:         
sage: class MyRing2(CombinatorialFreeModule):
....:     def __init__(self):
....:         R = QQ
....:         category = (ModulesWithBasis(R), Rngs())
....:         CombinatorialFreeModule.__init__(self, R, Partitions(), category = category)
....:     def product(self, left, right):
....:         return self.zero()
....:     class Element(CombinatorialFreeModule.Element):
....:         pass
....:     
sage: x = MyRing1().basis()[Partition([2,1])]
sage: x
B[[2, 1]]
sage: x*x
0
sage: y = MyRing2().basis()[Partition([2,1])]
sage: y
B[[2, 1]]
sage: y*y
| Sage Version 4.4, Release Date: 2010-04-24                         |
| Type notebook() for the GUI, and license() for information.        |
...

/opt/sage-4.4/local/lib/python2.6/site-packages/sage/categories/modules.pyc in __mul__(left, right)
     95             from sage.structure.element import get_coercion_model
     96             import operator
---> 97             return get_coercion_model().bin_op(left, right, operator.mul)
     98 
     99         def __rmul__(right, left):

/opt/sage-4.4/local/lib/python2.6/site-packages/sage/structure/coerce.so
in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:7063)()

/opt/sage-4.4/local/lib/python2.6/site-packages/sage/structure/coerce.so
in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6034)()

/opt/sage-4.4/local/lib/python2.6/site-packages/sage/categories/modules.pyc in __mul__(left, right)
     95             from sage.structure.element import get_coercion_model
     96             import operator
---> 97             return get_coercion_model().bin_op(left, right, operator.mul)
     98 
     99         def __rmul__(right, left):

/opt/sage-4.4/local/lib/python2.6/site-packages/sage/structure/coerce.so
in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:7063)()

/opt/sage-4.4/local/lib/python2.6/site-packages/sage/structure/coerce.so
in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6034)()

RuntimeError: maximum recursion depth exceeded while calling a Python object
sage: 
```


It seems like this could be fixed by removing `Modules.ElementClass.__mul__`, since it doesn't seem to add any functionality; is there any reason for it being there?



---

Comment by tscrim created at 2014-06-17 18:04:16

FYI, I came across this while working on #14901.


---

Comment by cnassau created at 2014-08-17 20:31:15

This works for me in Sage 6.4beta0. The problem seems to have been fixed, even though `sage.categories.modules.Modules.ElementMethods.__mul__` appears to be unchanged.
