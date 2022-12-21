# Issue 2412: basis_matrix returns matrix over wrong ring

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2008-03-06 22:54:36

Assignee: was

CC:  ncalexan jason

Keywords: basis matrix basis_matrix ZZ


```
sage: (ZZ**3).basis_matrix()

[1 0 0]
[0 1 0]
[0 0 1]
sage: (ZZ**3).basis_matrix().parent()
Full MatrixSpace of 3 by 3 dense matrices over Rational Field
```


That should be over the integer ring; you can't do `(ZZ**3).basis_matrix().smith_form()` otherwise.


---

Comment by was created at 2008-03-07 01:47:07

This is not a bug, it is a design decision.  ZZ modules in Sage in general need *not* be embedded in ZZ^n -- they can be in QQ^n.  For consistency the basis matrix is thus always over QQ.  Here's an example of a module over ZZ but for which the basis matrix is over QQ. 


```
sage: A = (ZZ^3).span([[1,2,3], [1/3,5,6]])
sage: A
Free module of degree 3 and rank 2 over Integer Ring
Echelon basis matrix:
[1/3   5   6]
[  0  13  15]
sage: A.basis_matrix()
[1/3   5   6]
[  0  13  15]
```


I'm willing to consider changing the design to *try* to make the basis
matrix over ZZ if posible, otherwise make it over QQ.  Thoughts?   I doubt
this will break anything.... (famous last words).


---

Comment by jason created at 2008-11-14 05:20:25

Resolution: invalid


---

Comment by jason created at 2008-11-14 05:20:25

As per request on IRC:


```
[23:17] <ncalexan> jason--: I think that decision is fine.  I say close it as invalid.
```

