# Issue 6534: Jacobi sums are calculated in a ridiculously roundabout fashion

Issue created by migration from https://trac.sagemath.org/ticket/6534

Original creator: davidloeffler

Original creation time: 2009-07-14 19:55:02

Assignee: craigcitro

Keywords: dirichlet characters

Why are we using a devious and roundabout algorithm to compute Jacobi sums using Gauss sums, which is actually many orders of magnitude slower than using the definition directly? I'm not joking here: for a pretty small prime, the obvious algorithm is more than 800 times as fast as the implementation we currently have.


```
sage: chi = DirichletGroup(67).0
sage: psi = chi**3
sage: time sum([chi(a)*psi(1-a) for a in Zmod(67)])
CPU times: user 0.03 s, sys: 0.00 s, total: 0.03 s
Wall time: 0.05 s
-5*zeta66^19 - 3*zeta66^18 + 6*zeta66^17 + 11*zeta66^16 + 3*zeta66^15 - 3*zeta66^14 - 7*zeta66^13 - 2*zeta66^12 + 3*zeta66^11 + 4*zeta66^10 + 5*zeta66^9 + 5*zeta66^8 - 4*zeta66^7 - 8*zeta66^6 - 8*zeta66^5 + 4*zeta66^4+ 6*zeta66^3 + 6*zeta66^2 - 3*zeta66 - 8
sage: time chi.jacobi_sum(psi)
CPU times: user 25.59 s, sys: 0.06 s, total: 25.65 s
Wall time: 29.02 s
-5*zeta4422^1273 - 3*zeta4422^1206 + 6*zeta4422^1139 + 11*zeta4422^1072 + 3*zeta4422^1005 - 3*zeta4422^938 -7*zeta4422^871 - 2*zeta4422^804 + 3*zeta4422^737 + 4*zeta4422^670 + 5*zeta4422^603 + 5*zeta4422^536 - 4*zeta4422^469 - 8*zeta4422^402 - 8*zeta4422^335 + 4*zeta4422^268 + 6*zeta4422^201 + 6*zeta4422^134 - 3*zeta4422^67- 8
```



---

Attachment


---

Comment by davidloeffler created at 2009-07-14 20:31:19

Here are two patches. One is intended to be applied on top of the patch at #6393, and the other without it; both give identical results. (This is intended to future-proof this ticket in case #6393 gets merged before anyone gets around to reviewing this one.)

While I was at it, I couldn't resist doing some streamlining to dirichlet.py by using the ``@`cached_method` decorator, and fixing a non-ReSTified docstring for Kloosterman sums.


---

Attachment

apply over exactly one of the above two patches


---

Comment by davidloeffler created at 2009-07-14 20:58:38

The third patch above fixes some formatting slips in the documentation. I also added a definition of the Jacobi sum to the docstring, since there wasn't one before. This should apply fine over either of the previous two patches.


---

Comment by cremona created at 2009-07-18 16:53:17

I like this patch.  (I tested the version which goes on top of #6393 having applied that first).  The code is a lot simpler, and it is faster, and it is more general (it works for characters withe values in non-prime finite fields).  What more can one ask?

All files in sage/modular test ok.

I must check out this cached_method trick, since it simplifies code a lot!


---

Comment by mvngu created at 2009-07-19 08:02:29

Resolution: fixed


---

Comment by mvngu created at 2009-07-19 08:02:29

Merged `trac_6534-jacobi_sums_faster-with_6393.patch` and `trac_6534_fix.patch`, since #6393 has already been merged.
