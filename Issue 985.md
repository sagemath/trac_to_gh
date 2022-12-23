# Issue 985: sage-2.8.9.rc1: maxima printing changed in equations.py and ell_generic.py

Issue created by migration from https://trac.sagemath.org/ticket/985

Original creator: cwitty

Original creation time: 2007-10-25 00:55:12

Assignee: was

equations.py:

```
File "equations.py", line 12:
    sage: print solve(qe, x)
Expected:
    [
                                          2
                                  - sqrt(b  - 4 a c) - b
                              x == ----------------------
                                           2 a,
                                         2
                                   sqrt(b  - 4 a c) - b
                               x == --------------------
                                           2 a
    ]
Got:
    [x == (-sqrt(b^2 - 4*a*c) - b)/(2*a), x == (sqrt(b^2 - 4*a*c) - b)/(2*a)]
```


ell_generic.py:

```
File "ell_generic.py", line 249:
    sage: print F.solve(y)
Expected:
    [
                          3      2
                - sqrt(4 x  - 4 x  - 40 x - 79) - 1
            y == -----------------------------------
                                 2,
                         3      2
                 sqrt(4 x  - 4 x  - 40 x - 79) - 1
             y == ---------------------------------
                                 2
    ]
Got:
    [y == (-sqrt(4*x^3 - 4*x^2 - 40*x - 79) - 1)/2, y == (sqrt(4*x^3 - 4*x^2 - 40*x - 79) - 1)/2]
```




---

Attachment


---

Comment by mhansen created at 2007-10-25 02:08:44

Changing assignee from was to mhansen.


---

Comment by mhansen created at 2007-10-25 02:08:44

Changing status from new to assigned.


---

Attachment

Use the second patch.


---

Comment by was created at 2007-10-25 06:44:17

Resolution: fixed
