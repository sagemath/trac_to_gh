# Issue 884: 2.8.7-alpha0: doctest failure in rings/residue_field.pyx

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2007-10-13 20:19:37

Assignee: failure

On sage.math, the rings/residue_field.pyx doctest fails as follows in 2.8.7:

```
sage -t  devel/sage-rtest/sage/rings/residue_field.pyx      **********************************************************************
File "residue_field.pyx", line 364:
    sage: b*c^2
Exception raised:
    Traceback (most recent call last):
      File "/home/cwitty/pre-sage/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_15[8]>", line 1, in <module>
        b*c**Integer(2)###line 364:
    sage: b*c^2
      File "element.pyx", line 1463, in element.RingElement.__pow__
      File "element.pyx", line 2777, in element.generic_power_c
      File "element.pyx", line 1376, in element.RingElement.__mul__
      File "coerce.pxi", line 126, in element._mul_c
    RuntimeError
**********************************************************************
File "residue_field.pyx", line 221:
    sage: k.coerce_map_from(OK)(OK(a)^7)
Exception raised:
    Traceback (most recent call last):
      File "/home/cwitty/pre-sage/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_9[4]>", line 1, in <module>
        k.coerce_map_from(OK)(OK(a)**Integer(7))###line 221:
    sage: k.coerce_map_from(OK)(OK(a)^7)
      File "element.pyx", line 1463, in element.RingElement.__pow__
      File "element.pyx", line 2782, in element.generic_power_c
      File "element.pyx", line 1376, in element.RingElement.__mul__
      File "coerce.pxi", line 126, in element._mul_c
    RuntimeError
**********************************************************************
2 items had failures:
   1 of  10 in __main__.example_15
   1 of   5 in __main__.example_9
***Test Failed*** 2 failures.
For whitespace errors, see the file .doctest_residue_field.pyxException exceptions.AttributeError: "'AbsoluteOrder' object has no attribute 'polynomial_ntl'" in 'number_field_element.NumberFieldElement_absolute._parent_poly_c_' ignored
ZZX: division by zero
Exception exceptions.AttributeError: "'AbsoluteOrder' object has no attribute 'polynomial_ntl'" in 'number_field_element.NumberFieldElement_absolute._parent_poly_c_' ignored
ZZX: division by zero
```



---

Comment by roed created at 2007-10-14 03:13:42

Changing status from new to assigned.


---

Comment by roed created at 2007-10-14 03:13:42

Changing assignee from failure to roed.


---

Comment by roed created at 2007-10-14 03:24:17

Uncommented region that shouldn't have been commented out.


---

Attachment


---

Comment by was created at 2007-10-14 17:40:44

I reject this patch.  That code was commented out for a reason.  It is conceptually completely wrong to have such methods on an order -- the order can't be defined by a single poly in general, etc.


---

Comment by was created at 2007-10-14 17:57:01

Actually David Roes' code is right and his example just exposes a bug in my code.


---

Comment by was created at 2007-10-14 19:14:01

I'm working on this...


---

Comment by was created at 2007-10-14 19:14:01

Changing status from assigned to new.


---

Comment by was created at 2007-10-14 19:14:01

Changing assignee from roed to was*.


---

Comment by was created at 2007-10-14 19:14:08

Changing status from new to assigned.


---

Comment by was created at 2007-10-14 19:14:08

Changing assignee from was* to was.


---

Comment by was created at 2007-10-15 18:14:47

Resolution: fixed
