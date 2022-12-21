# Issue 893: 2.8.7-alpha0: doctest failure in const.tex

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2007-10-13 20:51:36

Assignee: tba

There are three failures, but the last two are direct consequences of the first one:

```
File "const.py", line 749:
    sage: vals = E.Lseries_values_along_line(1-I, 1+10*I, 100) # critical line
Exception raised:
    Traceback (most recent call last):
      File "/home/cwitty/pre-sage/local/lib/python2.5/doctest.py", line 1212, in
 __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_22[1]>", line 1, in <module>
        vals = E.Lseries_values_along_line(Integer(1)-I, Integer(1)+Integer(10)*
I, Integer(100)) # critical line###line 749:
    sage: vals = E.Lseries_values_along_line(1-I, 1+10*I, 100) # critical line
    AttributeError: 'EllipticCurve_rational_field' object has no attribute 'Lser
ies_values_along_line'
```




---

Comment by cwitty created at 2007-10-13 23:06:53

This function was in 2.8.6 but is no longer in 2.8.7.  Was it deliberately removed?


---

Comment by was created at 2007-10-13 23:29:20

This was caused by David Roe's refactoring of the ell_rational_field command.
Now one does L = E.Lseries(), and there is a method
    L.values_along_line(...)


---

Attachment

Text patch fixing the doctest


---

Comment by was created at 2007-10-14 22:54:12

Resolution: fixed
