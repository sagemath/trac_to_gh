# Issue 5919: [with patch, needs review] bug in conversion of polys over GF(2,e) from NTL to singular

Issue created by migration from Trac.

Original creator: cremona

Original creation time: 2009-04-28 15:40:18

Assignee: tbd

CC:  alexghitza malb

Keywords: polynomial finite field

In 3.4.2.alpha0 we have

```
sage: F.<a> = GF(2^16)
sage: R.<x, y> = F[]
sage: R({(1,2):1})
0*x*y^2
```

which Alex Ghitza tracked down to a line in libs/singular/singular.pyx and which I fixed by replacing one character in that line from 'i' to '0'.  After that:

```
sage: sage: F.<a> = GF(2^16)
sage: sage: R.<x, y> = F[]
sage: sage: R({(1,2):1})
x*y^2
```

and hence also

```
sage: Fx.<b>=GF(2^(4*5))
sage: Ex=EllipticCurve(Fx,[0,0,1,1,1])
sage: Ex.defining_polynomial()
x^3 + y^2*z + x*z^2 + y*z^2 + z^3
```

which was not working properly (as reported to sage-devel).




---

Attachment

applies to 3.4.2.alpha0


---

Comment by malb created at 2009-04-28 15:47:53

Patch looks good.


---

Comment by cremona created at 2009-04-28 15:55:33

Thanks -- I did not add a doctest, since the function in which the bug was is a long way (it seems) from the user level where the above examples make sense.

Specifically, the bug is in the cdef function  Conversion.*sa2si_GFqNTLGF2E(self, FiniteField_ntl_gf2eElement elem, ring *_ring) which has an empty docstring!


---

Comment by mabshoff created at 2009-04-29 22:49:56

Merged in Sage 3.4.2.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-29 22:49:56

Resolution: fixed
