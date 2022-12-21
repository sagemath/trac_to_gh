# Issue 3961: bug in ell_finite_field.abelian_group()

Issue created by migration from Trac.

Original creator: cremona

Original creation time: 2008-08-26 19:48:12

Assignee: cremona

CC:  alexghitza

Keywords: elliptic curve fineite field

This works in 3.1.1:

```
sage: p=10^4+7; p       
10007
sage: F.<i>=GF(p^2)
sage: E = EllipticCurve([0,0,0,i,i+3]); E
Elliptic Curve defined by y^2  = x^3 + i*x + (i+3) over Finite Field in i of size 10007^2
sage: E.abelian_group()

(Multiplicative Abelian Group isomorphic to C100130006,
 ((8287*i + 5423 : 9131*i + 6741 : 1),))
```


but this does not:

```
sage: K.<i> = QuadraticField(-1)
sage: P=K.factor(p)[0][0]; P
Fractional ideal (10007)
sage: E = EllipticCurve([0,0,0,i,i+3]); E
Elliptic Curve defined by y^2  = x^3 + i*x + (i+3) over Number Field in i with defining polynomial x^2 + 1            
sage: Emod = E.change_ring(K.ring_of_integers().residue_field(P)); Emod
Elliptic Curve defined by y^2  = x^3 + ibar*x + (ibar+3) over Residue field in ibar of Fractional ideal (10007)
sage: Emod.abelian_group()
---------------------------------------------------------------------------
UnboundLocalError                         Traceback (most recent call last)

/home/john/sage-3.1.final/<ipython console> in <module>()

/home/john/sage-3.1.final/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_finite_field.py in abelian_group(self, debug)
   1121                 if debug: print "n1a=",n1a
   1122                 a = None
-> 1123                 for m in (N//n1).divisors():
   1124                     try:
   1125                         a = generic.bsgs(m*P1a,m*Q,(0,(n1b//m)-1),operation='+')

UnboundLocalError: local variable 'N' referenced before assignment
```


That's a bug in code I wrote, and I will fix it.  But it's a mystery why it only arises when the same (abstract) finite field is defined as a quotient field of ZZ[i].



---

Attachment


---

Comment by cremona created at 2008-08-27 09:57:00

The attached patch fixes the bug (and at the same time slightly improves the debug output, and also introduces a small speedup).  The bug was in the line now number 1135.

The apparent inconsistency noted at the end of the bug report is bogus:  the default generator for `GF(10007^2)` is not sqrt(-1) so the two curves are actually different.

Patch is based on 3.1.1, and all doctests in sage.schemes.elliptic_curves pass.


---

Comment by cremona created at 2008-08-27 09:57:00

Changing keywords from "elliptic curve fineite field" to "elliptic curve finite field".


---

Comment by cremona created at 2008-08-27 09:57:00

Changing component from algebra to number theory.


---

Comment by AlexGhitza created at 2008-08-29 04:07:05

The patch indeed fixes the bug, and there is a small speed gain.


---

Comment by mabshoff created at 2008-08-29 06:29:53

Merged in Sage 3.1.2.alpha2


---

Comment by mabshoff created at 2008-08-29 06:29:53

Resolution: fixed
