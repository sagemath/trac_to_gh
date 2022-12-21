# Issue 5347: divides() may fail for 1 on the rhs.

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2009-02-23 08:21:33

Assignee: somebody

CC:  mhansen


```
sage: K = GF(7)
sage: K(3).divides(1)
False
sage: K(3).divides(K(1))
Traceback (most recent call last)
...
ZeroDivisionError: reduction modulo right not defined.
```


This is because of this code added at http://hg.sagemath.org/sage-main/rev/0cb746e1a4bd


```
def divides(self, x):
    return (x % self) == 0
```




---

Attachment

Applies to 4.1.1


---

Comment by cremona created at 2009-08-30 17:45:39

Changing keywords from "" to "ring element divides".


---

Comment by cremona created at 2009-08-30 17:45:39

The patch handles this by testing all the easy cases of a.divides(b) (a is 1 or a unit, b is zero) before trying the % operation.  Doctest added to show that it works.


---

Comment by mhansen created at 2009-09-08 23:52:30

Looks good to me.


---

Comment by mvngu created at 2009-09-09 04:48:58

Resolution: fixed
