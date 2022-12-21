# Issue 2106: Implement univariate polynomials over GF(2) via ntl.GF2X

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-02-08 09:44:08

Assignee: somebody

CC:  malb

Marshall Buck on [sage-support] writes:

It is a shame that normal arithmetic for polys over GF(2) still seems
to be implemented by the ntl ZZ_pX library, which is usually at least
10 times slower than GF2X,  up to degree 2<sup>17</sup> anyway. In that range
GF2X matches the speed of magma.


---

Comment by zimmerma created at 2008-10-18 11:41:13

This is related to #4302, and will probably be fixed with #4302, thus might be marked as
duplicate of #4302.


---

Comment by malb created at 2008-11-01 22:18:39

Resolution: duplicate


---

Comment by malb created at 2008-11-01 22:18:39

This is a duplicate #4302
