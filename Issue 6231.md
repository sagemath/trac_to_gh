# Issue 6231: Solving a system of equations ignores multiplicities

Issue created by migration from Trac.

Original creator: SimonKing

Original creation time: 2009-06-06 07:20:46

Keywords: multiplicities system of equations

A follow-up from http://groups.google.com/group/sage-support/browse_thread/thread/d8e22deb18d97253 but different from #6228:


```
sage: solve((x^2-1)^3==0, x, multiplicities=True)
([x == -1, x == 1], [3, 3])
sage: solve(((x^2-1)^3==0,(x^2-1)^3==0), x, multiplicities=True)
[[x == 1], [x == -1]]
```


So, at least in this example, we get the correct multiplicities for a single equation, but we don't get any multiplicity when the same equation together with a copy of itself forms a _system_ of equations.

Note that ``maxima`` provides the correct answer:

```
sage: maxima.eval('solve(((x^2-1)^3,(x^2-1)^3),x)')
'[x=-1,x=1]'
sage: maxima.eval('multiplicities')
'[3,3]'

```


Probably this bug can be easily done by working at the code of the ``solve`` command.

What format should the multiplicities be provided in?

 - When one solves a single equation with a single variable, the solutions are given by a simple list. Accordingly, the multiplicities are given as a simple list.
 - When a system of equations in a single variable is given, the solutions are given by a list of lists. So, should the multiplicities be given by a list of lists?
