# Issue 7101: Inconsistency in polynomial ring creation.

Issue created by migration from Trac.

Original creator: hivert

Original creation time: 2009-10-03 15:53:26

Assignee: tbd

**Hi sage developers,

I need to play with polynomials on various kind of coefficients. So I tried
the following:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: combinat
sage: R=QQ[x]
sage: R(1+x)
x + 1
sage: R=ZZ[x]
sage: R(1+x)
x + 1
sage: R=RealField(200)[x]
sage: R(1+x)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
[...]
TypeError: x is not a variable of Univariate Polynomial Ring in x over Real Field with 200 bits of precision
```

| Sage Version 4.1.1, Release Date: 2009-08-14                       |
| Type notebook() for the GUI, and license() for information.        |
As mvngu pointed out on irc: the following works

```
sage: R.<x> = RealField(20)["x"]
sage: R(1 + x)
1.0000*x + 1.0000
```

But this is not very beautiful and worse it is very inconsistent...
At least the error message should be more understandable...

What should we do about it ?

Cheers,

Florent



---

Comment by mhansen created at 2009-10-04 03:48:36

This is fixed by the patches at #7007 and #5639.


---

Comment by mhansen created at 2009-10-04 03:50:29

Resolution: duplicate


---

Comment by mhansen created at 2009-10-04 03:50:29

Err, it's a duplicate of #5755 which has been fixed.
