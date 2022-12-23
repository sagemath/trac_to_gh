# Issue 1003: [with patch] GF(2^n) elements powering overflow

Issue created by migration from https://trac.sagemath.org/ticket/1003

Original creator: malb

Original creation time: 2007-10-26 09:23:15

Assignee: malb

Carl Witty reported:

```
On my 32-bit linux box, I had an additional failure:
 **********************************************************************
File "finite_field_element.py", line 18:
    sage: c = a^e
Exception raised:
    Traceback (most recent call last):
      File "/home/cwitty/sage/local/lib/python2.5/doctest.py", line
1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[9]>", line 1, in <module>
        c = a**e###line 18:
    sage: c = a^e
      File "finite_field_ntl_gf2e.pyx", line 925, in
finite_field_ntl_gf2e.FiniteField_ntl_gf2eElement.__pow__
        GF2E_power(r.x, (<FiniteField_ntl_gf2eElement>self).x, exp)
    OverflowError: long int too large to convert to int
**********************************************************************
```


The attached patch should fix that issue.


---

Attachment


---

Comment by cwitty created at 2007-10-27 04:52:09

Resolution: fixed
