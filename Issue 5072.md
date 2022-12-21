# Issue 5072: segfault in libsingular gcd when base rings aren't identical

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-01-23 13:08:23

Assignee: malb

If you take the gcd of a polynomial over GF(9) with one over GF(3), Sage SEGFAULTS.


```
teragon:sage-3.3.alpha0 wstein$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: sage: k.<a> = GF(9)
sage: sage: R.<x,y> = PolynomialRing(k)
sage: k.<a> = GF(9); R.<x,y> = PolynomialRing(k)
sage: f = R.change_ring(GF(3)).gen()
sage: g = x+y
sage: g.gcd(f)
| Sage Version 3.3.alpha0, Release Date: 2009-01-19                  |
| Type notebook() for the GUI, and license() for information.        |

------------------------------------------------------------
Unhandled SIGBUS: A bus error occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------

teragon:sage-3.3.alpha0 wstein$ 
```



---

Attachment


---

Comment by mabshoff created at 2009-01-24 14:31:45

Merged in Sage 3.3.alpha2


---

Comment by mabshoff created at 2009-01-24 14:31:45

Resolution: fixed
