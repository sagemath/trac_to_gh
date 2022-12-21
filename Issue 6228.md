# Issue 6228: Wrong multiplicities when solving a univariate polynomial equation

Issue created by migration from Trac.

Original creator: SimonKing

Original creation time: 2009-06-05 19:17:33

Keywords: multiplicities solve

At http://groups.google.com/group/sage-support/browse_thread/thread/d8e22deb18d97253 Michael Friedman asked how to get the multiplicities when solving a set of nonlinear equations. 

It turns out that actually even the multiplicities for a single and rather simple equation are wrong:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: z = var('z')
sage: solve((z^3-1)^3,z,multiplicities=True)
([z == (sqrt(3)*I - 1)/2, z == (-sqrt(3)*I - 1)/2, z == 1], [1, 1, 3])
```

| Sage Version 4.0, Release Date: 2009-05-29                         |
| Type notebook() for the GUI, and license() for information.        |
I am afraid that symbolics isn't my field of expertise. So, I don't know how to cure it.


---

Comment by SimonKing created at 2009-06-05 19:39:27

Note that it seems to be a problem in ``maxima``:

```
sage: maxima.eval('solve((z^3-1)^3,z)')
'[z=(sqrt(3)*%i-1)/2,z=-(sqrt(3)*%i+1)/2,z=1]'
sage: maxima.eval('multiplicities')
'[1,1,3]'
```


So, I suspect this ticket will get a "won't fix"...


---

Comment by kcrisman created at 2009-09-29 14:47:50

This is now fixed, presumably in the Maxima upgrade.


---

Attachment

Based on 4.1.2.alpha4


---

Comment by mhansen created at 2009-10-05 05:46:46

Looks good to me.


---

Comment by mhansen created at 2009-10-15 08:38:47

Resolution: fixed
