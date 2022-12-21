# Issue 107: can't multiply matrix by vector over an arbitrary ring?

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2006-10-03 17:50:08

Assignee: was


```
sage: R = Integers(125)
sage: M = Matrix(R, 2, 2, [0, 1, 2, 3])
sage: V = Vector(R, [2, 3])
sage: M * V
---------------------------------------------------------------------------
exceptions.AttributeError                            Traceback (most recent call last)

/home/dmharvey/sage-1.3.7.3.3/<ipython console> 

/home/dmharvey/sage-1.3.7.3.3/matrix_pyx.pyx in matrix_pyx.Matrix.__mul__()

/home/dmharvey/sage-1.3.7.3.3/matrix_pyx.pyx in matrix_pyx.Matrix.vector_matrix_multiply()

/home/dmharvey/sage/local/lib/python2.4/site-packages/sage/modules/free_module_element.py in __add__(self, right)
     65         if self.parent() is right.parent():
     66             V = self.parent()
---> 67         elif self.parent().ambient_vector_space() == right.parent().ambient_vector_space():
     68             V = self.parent().ambient_vector_space()
     69         else:

AttributeError: 'FreeModule_ambient' object has no attribute 'ambient_vector_space'
```




---

Comment by was created at 2006-10-05 08:16:03

We shouldn't bother fixing this until when we are doing the serious pyrexing of linear algebra...


---

Comment by was created at 2007-01-07 19:42:39

This works fine now in sage-1.5:

```
sage: R = Integers(125)
sage: M = Matrix(R, 2, 2, [0, 1, 2, 3])
sage: V = vector(R, [2, 3])
sage: M * V
(3, 13)
```



---

Comment by was created at 2007-01-07 19:42:39

Resolution: fixed
