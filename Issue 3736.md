# Issue 3736: pairwise_product fails for vectors over CDF

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2008-07-29 00:22:13

Assignee: malb

CC:  bryan.head@gmail.com


```
sage: x = vector(CDF, range(10))
sage: y = vector(CDF, range(10))
sage: x.pa
x.pairwise_product  x.parent            
sage: x.pairwise_product(y)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/mike/src/combinat/branches/multisort-experiment/combinat/<ipython console> in <module>()

/home/mike/src/combinat/branches/multisort-experiment/combinat/free_module_element.pyx in sage.modules.free_module_element.FreeModuleElement.pairwise_product (sage/modules/free_module_element.c:7363)()

/home/mike/src/combinat/branches/multisort-experiment/combinat/element.pyx in sage.structure.element.Vector._pairwise_product_c (sage/structure/element.c:11073)()

/home/mike/src/combinat/branches/multisort-experiment/combinat/element.pyx in sage.structure.element.Vector._pairwise_product_c_impl (sage/structure/element.c:11134)()

TypeError: unsupported operation for 'Vector space of dimension 10 over Complex Double Field' and 'Vector space of dimension 10 over Complex Double Field'
```



---

Attachment


---

Comment by robertwb created at 2008-08-09 07:09:06

Works well for me.


---

Comment by mabshoff created at 2008-08-10 03:26:45

Merged in Sage 3.1.alpha1


---

Comment by mabshoff created at 2008-08-10 03:26:45

Resolution: fixed
