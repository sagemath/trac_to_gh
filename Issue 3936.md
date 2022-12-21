# Issue 3936: Throw exceptions on nonsensical comparisons?

Issue created by migration from Trac.

Original creator: nbruin

Original creation time: 2008-08-23 20:08:58

Assignee: tbd

CC:  jakobkroeker

It is impossible to have Python's universal comparison and have mathematically sound meaning to comparison. Transitivity and/or other properties have to cave at some point.

One example:

```
sage: L=[int(0),None,1,int(2),3]
sage: L.sort()
sage: L
[1, None, 0, 2, 3]
sage: L[0]<L[2]
False
```

Would it be at all feasible to throw exceptions on non-sensical comparisons, such as 1 > None ?
`**` instead of `^` seems pretty mild compared to this.


---

Comment by robertwb created at 2008-09-11 06:03:06

What about `1 == None` or `1 != None`, should those throw errors as well? (They use the same code).


---

Comment by craigcitro created at 2009-01-23 07:38:04

As Rob points out, there's really no way to do this cleanly. In particular, though, how often do you end up accidentally comparing an integer to something like `None`? It seems much better to have an occasional result that seems strange at first than to break Python conventions, and run into more serious problems because of it.

I'm closing this as invalid.


---

Comment by craigcitro created at 2009-01-23 07:38:04

Resolution: invalid
