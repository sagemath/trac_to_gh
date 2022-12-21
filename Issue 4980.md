# Issue 4980: add info about slices to developer guide

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-01-15 06:12:26

Assignee: tba

Somewhere we should note the standard way to deal with getting the indices from a slice object is


```
range(*s.indices(size))
```


where s is our slice and size is the size of the object we are applying the slice to.  See #4974 for lots of other information and discussion of various ways to do this, converging on the above simply standard python.


---

Comment by timdumol created at 2010-01-17 09:01:51

Changing type from defect to enhancement.


---

Comment by kcrisman created at 2014-11-20 16:47:54

Changing priority from major to minor.
