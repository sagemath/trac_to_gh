# Issue 1228: 2.8.13.rc1: sage/rings/arith.py doctest failure

Issue created by migration from https://trac.sagemath.org/ticket/1228

Original creator: mabshoff

Original creation time: 2007-11-20 23:03:57

Assignee: mabshoff

We get:

```
File "arith.py", line 2393:
     sage: continued_fraction_list(sqrt(4/19))
Expected:
     [0, 2, 5, 1, 1, 2, 1, 16, 1, 2, 1, 1, 5, 4, 5, 1, 1, 2, 1, 18]
Got:
     [0, 2, 5, 1, 1, 2, 1, 16, 1, 2, 1, 1, 5, 4, 5, 1, 1, 2, 1, 15, 2]
```

This is fallout from #1196:

```
With 2.8.12 we get:

sage: n(sqrt(4/19))
0.458831467741123

With 2.8.13.rc1 we get:

sage: n(sqrt(4/19))
0.458831467741124
```


Cheers,

Michael


---

Comment by mabshoff created at 2007-11-20 23:04:04

Changing status from new to assigned.


---

Comment by was created at 2007-11-21 12:57:47


```
Regarding #1228 change the doctest to the new answer.
It's actually much better.
```



---

Comment by mabshoff created at 2007-11-21 13:05:28

Merged in 2.8.13.rc2.

Fixed the doctest directly :)


---

Comment by mabshoff created at 2007-11-21 13:05:28

Resolution: fixed
