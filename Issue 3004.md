# Issue 3004: bug in coercion edge case -- probably easy to fix

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-04-22 21:56:35

Assignee: somebody

bug from Kari Christianson:


```
sage: PolynomialRing(ZZ, 'x').gen()*Mod(1,15)
x
```




```
sage: PolynomialRing(ZZ, 1, 'x').gen()*Mod(1,15)
Traceback (most recent call last):
...
TypeError: unsupported operand parent(s) for '*': 'Multivariate Polynomial Ring in x over Integer Ring' and 'Ring of integers modulo 15'
```



---

Comment by mabshoff created at 2008-10-28 16:34:10

This has been fixed by the new coercion system:

```
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.2.alpha2$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| Sage Version 3.2.alpha1, Release Date: 2008-10-26                  |
| Type notebook() for the GUI, and license() for information.        |
sage: PolynomialRing(ZZ, 'x').gen()*Mod(1,15)
x
sage: PolynomialRing(ZZ, 1, 'x').gen()*Mod(1,15)
x
sage: 
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-10-28 16:34:10

Resolution: fixed
