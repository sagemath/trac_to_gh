# Issue 889: 2.8.7-alpha0: doctest failure in schemes/elliptic_curves/lseries_ell.py (tiny differences in answer)

Issue created by migration from https://trac.sagemath.org/ticket/889

Original creator: cwitty

Original creation time: 2007-10-13 20:39:16

Assignee: failure


```
File "lseries_ell.py", line 59:
    sage: L.taylor_series(series_prec=3)
Expected:
    -1.28158145691931e-23 + (7.26268290635587e-24)*z + 0.759316500288427*z^2 + O(z^3)
Got:
    -2.69129566562797e-23 + (1.52514901968783e-23)*z + 0.759316500288427*z^2 + O(z^3)
```




---

Attachment

Fixes the doctest


---

Comment by was created at 2007-10-14 22:56:41

Resolution: fixed
