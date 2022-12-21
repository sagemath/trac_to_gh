# Issue 6398: shorten long doctests in sage/schemes/elliptic_curves/sha_tate.py

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2009-06-24 19:31:44

Assignee: tbd

After this last round of merging:


```
sage -t -long sage/schemes/elliptic_curves/sha_tate.py
         [891.9 s]
```


This is 15 minutes, and the second longest doctest takes just over 4 minutes.


---

Comment by was created at 2009-07-09 05:07:01

On sage.math this is:


```
sage -t -long "devel/sage/sage/schemes/elliptic_curves/sha_tate.py"
         [161.1 s]
```


so this is no longer even a problem.


---

Comment by was created at 2009-07-09 05:07:23

Resolution: fixed
