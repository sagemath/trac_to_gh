# Issue 29: implement len for elliptic curve over finite field

Issue created by migration from Trac.

Original creator: was

Original creation time: 2006-09-12 23:26:11

Assignee: somebody


```
sage: E=EllipticCurve(GF(37),range(5))
   sage: len(E)
   Traceback (most recent call last):
   ...
   TypeError: len() of unsized object
```


(also should have trace of frob, charpoly, ap, etc.)



---

Comment by dmharvey created at 2006-10-27 02:19:05

Slight problem is that `__len__()` has to return a python int. Even a long is unacceptable. So this will only work if the curve is not too large, otherwise it will necessarily throw a `TypeError`.


---

Comment by dmharvey created at 2006-10-27 02:51:25

Changing assignee from somebody to dmharvey.


---

Comment by AlexGhitza created at 2008-01-27 05:08:54

Changing component from basic arithmetic to algebraic geometry.


---

Comment by ncalexan created at 2008-02-16 21:42:06

This is essentially completed by #1130.

I think asking for len(E) is not right, in any case -- len(E.points()) makes some sense, and #1130 makes that work.


---

Comment by mabshoff created at 2008-02-16 21:50:29

Resolution: fixed


---

Comment by mabshoff created at 2008-02-16 21:50:29

Closed as fixed since I just merged #1130.

Cheers,

Michael
