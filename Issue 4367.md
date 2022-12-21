# Issue 4367: plot gamma bug

Issue created by migration from Trac.

Original creator: jvoight

Original creation time: 2008-10-25 18:54:40

Assignee: was


```
   sage: plot(gamma(x),(x,1,5))
```


Gives error.  


```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/jvoight/.sage/sage_notebook/worksheets/jvoight/10/code/18.py", line 6, in <module>
    plot(gamma(x),(x,Integer(1),Integer(5)))
  File "/usr/local/sage/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/", line 1, in <module>
    
  File "/usr/local/sage/local/lib/python2.5/site-packages/sage/functions/transcendental.py", line 106, in gamma
    return CC(s).gamma()
  File "/usr/local/sage/local/lib/python2.5/site-packages/sage/rings/complex_field.py", line 211, in __call__
    return x._complex_mpfr_field_( self )
  File "/usr/local/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 1451, in _complex_mpfr_field_
    raise TypeError
TypeError
```


There seems to be some confusing type error in coercion between floats and complex numbers.

JV


---

Comment by robertwb created at 2008-12-19 07:31:18

This has been resolved with #4432.


---

Comment by mabshoff created at 2008-12-19 07:36:00

If we have a doctest in tree we can close this ticket, if not we should add a doctest and then close this ticket after merging it.

Cheers,

Michael


---

Comment by robertwb created at 2008-12-19 07:40:26

will do


---

Attachment

Trivial doctest patch up.


---

Comment by mabshoff created at 2008-12-20 21:56:12

Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-21 12:22:17

Merged in Sage 3.2.3.alpha0


---

Comment by mabshoff created at 2008-12-21 12:22:17

Resolution: fixed
