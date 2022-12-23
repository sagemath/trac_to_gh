# Issue 4328: bug in roots

Issue created by migration from https://trac.sagemath.org/ticket/4328

Original creator: zimmerma

Original creation time: 2008-10-20 11:39:21

Assignee: somebody


```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.1.4, Release Date: 2008-10-16                       |
| Type notebook() for the GUI, and license() for information.        |
sage: R=PolynomialRing(ZZ, x)
sage: f=R(x^4+1)
sage: f.roots(GF(2))
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
...
ValueError: factorization of 0 not defined
```



---

Comment by zimmerma created at 2008-10-20 11:58:10

I should have said it works with vanilla 3.1.4, thus it is most likely related to the recent patches for
GF(2)[x] I have applied to my 3.1.4 version.


---

Comment by mabshoff created at 2008-10-20 12:06:45

It works with my current 3.2.alpha0 merge tree:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.alpha0$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.1.4, Release Date: 2008-10-16                       |
| Type notebook() for the GUI, and license() for information.        |
sage: R=PolynomialRing(ZZ, x)
sage: sage: f=R(x^4+1)
sage: sage: f.roots(GF(2))
[(1, 4)]
```

I suspect the root cause could be #4302.

Cheers,

Michael


---

Comment by malb created at 2008-10-20 13:23:34

worksforme:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading SAGE library. Current Mercurial branch is: test
sage: R=PolynomialRing(ZZ, x)
sage: f=R(x^4+1)
sage: f.roots(GF(2))
[(1, 4)]
| SAGE Version 3.1.3, Release Date: 2008-10-14                       |
| Type notebook() for the GUI, and license() for information.        |
sage: P.<x> = PolynomialRing(GF(2))
sage: type(x) # check whether the patch is applied
<type 'sage.rings.polynomial.polynomial_gf2x.Polynomial_GF2X'>
```


Note that I updates #4302 recently.


---

Comment by malb created at 2008-10-20 13:23:34

Resolution: worksforme
