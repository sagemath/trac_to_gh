# Issue 209: sageinspect bug on 64-bit linux?

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-01-23 18:49:10

Assignee: was


```
age -t  devel/sage-main/sage/misc/sageinspect.py           **********************************************\
************************
File "sageinspect.py", line 65:
    sage: sage.misc.sageinspect._sage_getargspec_sagex(sage.rings.integer.Integer.factor)
Exception raised:
    Traceback (most recent call last):
      File "/home/was/tmp/sage-1.8/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[2]>", line 1, in <module>
        sage.misc.sageinspect._sage_getargspec_sagex(sage.rings.integer.Integer.factor)###line 65:
    sage: sage.misc.sageinspect._sage_getargspec_sagex(sage.rings.integer.Integer.factor)
      File "/home/was/tmp/sage-1.8/local/lib/python2.5/site-packages/sage/misc/sageinspect.py", line 121, \
in _sage_getargspec_sagex
        raise ValueError, "Could not parse sagex argspec"
    ValueError: Could not parse sagex argspec
**********************************************************************
File "sageinspect.py", line 67:
    sage: sage.misc.sageinspect._sage_getargspec_sagex(sage.rings.rational.make_rational)
Exception raised:
    Traceback (most recent call last):
      File "/home/was/tmp/sage-1.8/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[3]>", line 1, in <module>
        sage.misc.sageinspect._sage_getargspec_sagex(sage.rings.rational.make_rational)###line 67:
    sage: sage.misc.sageinspect._sage_getargspec_sagex(sage.rings.rational.make_rational)
      File "/home/was/tmp/sage-1.8/local/lib/python2.5/site-packages/sage/misc/sageinspect.py", line 121, \
in _sage_getargspec_sagex
        raise ValueError, "Could not parse sagex argspec"
    ValueError: Could not parse sagex argspec
**********************************************************************
**********************************************************************
File "sageinspect.py", line 134:
    sage: sage.misc.sageinspect.sage_getargspec(sage.rings.integer.Integer.factor)
Exception raised:
    Traceback (most recent call last):
      File "/home/was/tmp/sage-1.8/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[0]>", line 1, in <module>
        sage.misc.sageinspect.sage_getargspec(sage.rings.integer.Integer.factor)###line 134:
    sage: sage.misc.sageinspect.sage_getargspec(sage.rings.integer.Integer.factor)
      File "/home/was/tmp/sage-1.8/local/lib/python2.5/site-packages/sage/misc/sageinspect.py", line 154, \
in sage_getargspec
        raise TypeError, 'arg is not a Python or a Sagex function'
    TypeError: arg is not a Python or a Sagex function
**********************************************************************
File "sageinspect.py", line 166:
    sage: sage.misc.sageinspect.sage_getdef(sage.rings.rational.make_rational, obj_name='mr')
Expected:
    'mr(s)'
Got:
    'mr( ... )'
**********************************************************************
**********************************************************************
File "sageinspect.py", line 168:
    sage: sage.misc.sageinspect.sage_getdef(sage.rings.integer.Integer.factor, obj_name='factor')
Expected:
    "factor(algorithm='pari')"
Got:
    'factor( ... )'
**********************************************************************
```



---

Comment by was created at 2007-01-25 07:08:46

Resolution: fixed


---

Comment by was created at 2007-01-25 07:08:46

It disappeared with sage-1.8.2.1
