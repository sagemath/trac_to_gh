# Issue 337: broken (?) discriminant of quaternion algebra

Issue created by migration from Trac.

Original creator: AlexGhitza

Original creation time: 2007-03-29 02:12:59

Assignee: was

Quaternion algebras seem to have a function discriminant(), but this fails when I try to use it.  Here is an example -- as far as I can tell the problem might actually be in gram_matrix():


```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.4.1.2, Release Date: 2007-03-28                     |
| Type notebook() for the GUI, and license() for information.        |
sage: B.<i,j,k> = QuaternionAlgebra(QQ,-3,-1)
sage: B
Quaternion algebra with generators (i, j, k) over Rational Field
sage: B.discriminant()
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)

/home/ghitza/python/<ipython console> in <module>()

/opt/sage/local/lib/python2.5/site-packages/sage/algebras/quaternion_algebra.py in discriminant(self)
    349         
    350     def discriminant(self):
--> 351         return self.gram_matrix().determinant()
    352 
    353     def gram_matrix(self):

/opt/sage/local/lib/python2.5/site-packages/sage/algebras/quaternion_algebra.py in gram_matrix(self)
    353     def gram_matrix(self):
    354         V = self.__vector_space
--> 355         if not V._FreeModule_generic__inner_product_is_dot_product:
    356             return V.inner_product_matrix()
    357         K = self.base_ring()

<type 'exceptions.AttributeError'>: 'FreeModule_ambient_field' object has no attribute '_FreeModule_generic__inner_product_is_dot_product'
```




---

Comment by was created at 2007-08-18 21:01:43

fixed in sage-2.8.


---

Comment by was created at 2007-08-18 21:01:43

Resolution: fixed
