# Issue 9458: Bug with variable names in solve()

Issue created by migration from Trac.

Original creator: tastalian

Original creation time: 2010-07-08 18:33:47

Assignee: AlexGhitza

Keywords: var solve name factorial

Some variable names yield strange behavior with the solve() function. Here is an example:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: var('d2 d3 x')
(d2, d3, x)
sage: solve((d2+d3)*x==1, x)
[x == factorial(2*k + 6*n)/(d3*factorial(2*k + 6*n) + factorial(k + 3*n - 1))]
```

| Sage Version 4.4.2, Release Date: 2010-05-19                       |
| Type notebook() for the GUI, and license() for information.        |
These factorials are strange. They don't occur with other variable names, e.g.,


```
sage: var('y1 y2 x')
(y1, y2, x)
sage: solve((y1+y2)*x==1, x)
[x == (1/(y1 + y2))]
```


Documentation for solve() does not mention reserved variable names.


---

Comment by mhansen created at 2010-07-08 19:37:31

Resolution: duplicate


---

Comment by mhansen created at 2010-07-08 19:37:31

This is basically a duplicate of #8734.
