# Issue 2071: SymbolicExpression conjugate() method assumes variables are real

Issue created by migration from https://trac.sagemath.org/ticket/2071

Original creator: cwitty

Original creation time: 2008-02-06 06:37:57

Assignee: was


```
sage: var('x')
x
sage: x.conjugate()
x
```


Under the assumption that x might be complex, this should really return conjugate(x).



---

Comment by gfurnish created at 2008-03-16 20:10:41

Changing assignee from was to gfurnish.


---

Comment by gfurnish created at 2008-03-16 20:10:41

Changing status from new to assigned.


---

Comment by mhansen created at 2008-11-14 09:13:10

This could be handled using Maxima's declare facility:


```
sage: sage.calculus.calculus.maxima.eval('declare(x, complex)')
'done'
sage: x.conjugate()
conjugate(x)
```


This also fixed by Pynac:


```
sage: x = var('x', ns=1)
sage: x
x
sage: x.conjugate()
conjugate(x)
```



---

Comment by burcin created at 2009-05-25 09:27:32

This is fixed in 4.0.rc0. There is a doctest in line 3871 of sage/symbolic/expression.pyx.

This bug should be closed as fixed.


---

Comment by mhansen created at 2009-05-26 16:17:23

Resolution: fixed
