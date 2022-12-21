# Issue 8924: Comparison between Sage and mpmath numbers is broken

Issue created by migration from Trac.

Original creator: fredrik.johansson

Original creation time: 2010-05-07 19:23:24

Assignee: AlexGhitza

Comparison between Sage and mpmath numbers works with mpmath numbers on the left, but not on the right:


```
sage: mpmath.mpf(1) < 3
True
sage: 1 < mpmath.mpf(3)
False
sage: 4 == mpmath.mpf(4)
False
```


Found by Harald Schilly (see #8791).

This appears to be a bug in Sage (or Cython). Sage's numbers do the pure-Python equivalent of not returning NotImplemented when compared to unrecognized types. For a minimal example:


```
sage: class X(object):
....:         def __init__(self, v): self.v = v
....:     def __lt__(self, other): return self.v < int(other)
....:     def __gt__(self, other): return self.v > int(other)
....:
sage: X(1) < 3
True
sage: 1 < X(3)
False
sage: X(1) < int(3)
True
sage: int(1) < X(3)
True
```



---

Comment by mkoeppe created at 2016-08-15 17:54:44

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2016-08-15 17:54:44

The tests from the description work as of 7.4.beta0.


---

Comment by jdemeyer created at 2016-08-15 17:59:56

I think this is fixed by #21163.


---

Comment by jdemeyer created at 2016-08-15 17:59:56

Changing status from needs_review to positive_review.


---

Comment by embray created at 2016-08-30 13:32:25

Resolution: wontfix


---

Comment by embray created at 2016-08-30 13:32:25

Determined to be invalid/duplicate/wontfix (closing as "wontfix" as a catch-all resolution).
