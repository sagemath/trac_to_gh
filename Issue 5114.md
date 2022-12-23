# Issue 5114: something wrong in the initializer for elements of QuaternionAlgebra

Issue created by migration from https://trac.sagemath.org/ticket/5114

Original creator: cwitty

Original creation time: 2009-01-28 03:55:28

Assignee: tbd

CC:  was

Consider:

```
sage: QA = QuaternionAlgebra(QQ, -1, -1)
sage: foo = QA(3.0); foo
3.00000000000000
sage: parent(foo)
Quaternion algebra with generators (i, j, k) over Rational Field
sage: parent(foo.vector()[0])
Real Field with 53 bits of precision
```

I don't think the initializer should let you construct an element with RR members but still claim to be over QQ.


---

Comment by AlexGhitza created at 2009-01-28 22:07:49

I think that QA(3.0) should definitely throw an exception, just as the following does:


```
sage: K.<a> = QuadraticField(11)
sage: K(3.0)
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (858, 0))

ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (863, 0))

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/ghitza/.sage/temp/artin/9038/_home_ghitza__sage_init_sage_0.py in <module>()

/opt/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:3645)()

/opt/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:2793)()

/opt/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps._call_ (sage/structure/coerce_maps.c:2700)()

/opt/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.pyc in _element_constructor_(self, x)
   1417                 raise ValueError, "vector must be of length equal to the degree of this number field"
   1418             return sum([ x[i]*self.gen(0)**i for i in range(self.degree()) ])
-> 1419         return self._coerce_non_number_field_element_in(x)
   1420 
   1421     def _coerce_from_str(self, x):

/opt/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.pyc in _coerce_non_number_field_element_in(self, x)
   1527         except (TypeError, AttributeError), msg:
   1528             pass
-> 1529         raise TypeError, type(x)
   1530 
   1531     def _coerce_map_from_(self, R):

TypeError: <type 'sage.rings.real_mpfr.RealLiteral'>
```



---

Comment by AlexGhitza created at 2009-03-29 03:35:58

For what it's worth, this behaviour changed and became more consistent with the recent reworking of the quaternion algebra code:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: sage: QA = QuaternionAlgebra(QQ, -1, -1)
sage: sage: foo = QA(3.0); foo
3
sage: parent(foo)
Quaternion Algebra (-1, -1) with base ring Rational Field
sage: foo[0]
3
sage: parent(foo[0])
Rational Field
```

| Sage Version 3.4, Release Date: 2009-03-11                         |
| Type notebook() for the GUI, and license() for information.        |
Do we want to consider this fixed now?


---

Comment by cwitty created at 2009-03-31 03:15:37

Yes, it looks like the bug is fixed; but somebody should create a doctest so that we can make sure it stays fixed forever.


---

Comment by AlexGhitza created at 2009-04-29 13:52:06

The attached patch adds the requested doctest.


---

Comment by AlexGhitza created at 2009-04-29 13:52:06

Changing assignee from tbd to AlexGhitza.


---

Comment by AlexGhitza created at 2009-04-29 13:52:06

Changing status from new to assigned.


---

Attachment


---

Comment by davidloeffler created at 2009-05-28 10:07:37

Looks good to me: patch applies fine to 4.0.rc1, all doctests in the quatalg directory pass, and the docs build OK. Positive review.


---

Comment by mhansen created at 2009-06-01 04:25:05

Merged in 4.0.1.alpha0.


---

Comment by mhansen created at 2009-06-01 04:25:05

Resolution: fixed
