# Issue 6160: Segmentation Fault with Multivariate Polynomial Ring

Issue created by migration from Trac.

Original creator: stankewicz

Original creation time: 2009-05-30 21:04:28

Assignee: somebody

CC:  malb wjp

This is an example over a 2- variable polynomial ring over QQ (although sage does not see K as isomorphic to QQ

login`@`sage:~$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: K.<j> = NumberField(x-1728)
sage: R.<b,c> = K[]
sage: f = b-j*c
| Sage Version 3.4.1, Release Date: 2009-04-21                       |
| Type notebook() for the GUI, and license() for information.        |

------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------

login`@`sage:~$

Note that this does not pose a problem if the number field is not QQ

sage: K.<j> = NumberField(x^2 - 2)
sage: R.<b,c> = K[]
sage: f = b-j*c
sage: f
b + (-j)*c

Nor if the Polynomial Ring is Univariate

sage: F.<i> = NumberField(x-1728)
sage: S.<y> = F[]
sage: y - i
y - 1728
sage: g = y - i
sage: g = i*y^2 + 1
sage: g
1728*y^2 + 1

Also note that this has nothing to do with Pari's occasional trouble with the ordering of variables

sage: K.<j> = NumberField(x-1728)
sage: R.<k,l> = K[]
sage: f = k - j*l


------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------


login`@`sage:~$


---

Comment by burcin created at 2010-01-17 02:12:37

The patch attached to #7582 fixes this. I'm closing this as a duplicate.


---

Comment by burcin created at 2010-01-17 02:12:37

Resolution: duplicate


---

Comment by burcin created at 2010-01-17 02:12:37

Changing keywords from "" to "singular".
