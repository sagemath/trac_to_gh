# Issue 2664: [with patch, needs review] implement a symplectic form for finding symplectic bases

Issue created by migration from https://trac.sagemath.org/ticket/2664

Original creator: ncalexan

Original creation time: 2008-03-25 19:26:39

Assignee: was

CC:  ncalexan

Keywords: symplectic basis form integer matrix

Implement a `symplectic_form` for computing symplectic bases for alternating, anti-symmetric matrices.  This is essential for computing with polarized Abelian varieties.

The attached patch computes symplectic forms over fields and the integers.


---

Attachment


---

Comment by craigcitro created at 2008-03-28 21:15:05

Patch looks *great*! There are one or two tiny things I'd like to see fixed:

 * I don't like the line `alternating_form = symplectic_form`, for the same reasons as my similar comment on #2707.

 * Should the new `matrix/symplectic_basis.py` file have a copyright notice at the top?

 * Given that there's this nice code for computing symplectic bases, it might be nice for someone to write a `SymplecticSpace` class that inherits from some kind of vector space class, and uses this code behind the scenes where necessary. (Do we already have an inner product space class?) I'm not saying you should implement this right now, of course! But maybe file a trac ticket? Would you use this in what you're doing with this code? (I don't personally have any need of it right now, but it seems like it would be useful in general.)


---

Attachment


---

Comment by mabshoff created at 2008-03-28 21:51:52

Merged in Sage 2.11.alpha2


---

Comment by mabshoff created at 2008-03-28 21:51:52

Resolution: fixed
