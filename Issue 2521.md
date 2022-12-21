# Issue 2521: Bug in gauss_sum_numerical in degenerate case (probably easy to fix)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-03-14 21:24:13

Assignee: was


```
sage: G = DirichletGroup(4)
sage: G(1).gauss_sum_numerical()
Traceback (most recent call last):
...
TypeError: 1 must be coercible into Cyclotomic Field of order 2 and degree 1 (and is not an element)
```


Instead the result should be 0:

```
sage: G(1).gauss_sum()
0
```



---

Comment by AlexGhitza created at 2008-04-13 02:36:05

This is fixed in sage-3.0.alpha2:


```
sage: G=DirichletGroup(4)
sage: G(1).gauss_sum_numerical()
-1.22464679914735e-16
```


I think it is due to Craig Citro's fixes in the cyclotomic fields code (see #2192).


---

Comment by was created at 2008-04-13 02:53:53

Resolution: fixed


---

Comment by mabshoff created at 2008-04-13 03:00:15

For the record:

```
[04:14] <mabshoff> wstein: can you confirm that #2521 is fixed and close it then?
[04:16] <wstein> yep, is fixed.
```

