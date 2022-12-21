# Issue 2086: iPython bug? Python decorators don't play nicely with docstrings

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-02-07 17:22:26

Assignee: tba

Consider:


```
sage: P.<x,y> = PolynomialRing(QQ)
sage: I =  Ideal([x, y])
sage: I.reduced_basis?
    x.__init__(...) initializes x; see x.__class__.__doc__ for signature

sage: I.reduced_basis??
    def wrapper(*args, **kwds):
        with RedSBContext():
            return func(*args, **kwds)
```


which is caused by the ``@`redSB` decorator. 


---

Comment by malb created at 2008-03-28 12:17:09

This is invalid because there is a standard (?) way to work around this.


---

Comment by malb created at 2008-03-28 12:17:09

Resolution: invalid
