# Issue 232: assert statement does not work in sage

Issue created by migration from https://trac.sagemath.org/ticket/232

Original creator: yi

Original creation time: 2007-01-29 20:07:29

Assignee: was

Keywords: python assert

Different behavior in sage shell than in regular python shell:

sage: x = 5
sage: y = 3
sage: assert x==y
sage:

in python:
>>> x = 5
>>> y = 3
>>> assert x==y
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError
>>>


---

Comment by was created at 2007-01-29 20:17:41

This is a SAGE/Ipython interaction problem, since assert works fine in the SAGE Notebook, and with dsage.client...


---

Comment by was created at 2007-01-29 20:41:07

Resolution: fixed


---

Comment by was created at 2007-01-29 20:41:07

Fixed for sage > 2.0.
