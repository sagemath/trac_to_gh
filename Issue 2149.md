# Issue 2149: Rename BooleanPolynomialRing

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-02-13 13:11:35

Assignee: malb

CC:  burcin

Keywords: polybori

William Stein wrote in #2146:

"""

By the way, wouldn't it be better to call it `PolynomialBooleanRing` instead of `BooleanPolynomialRing` I suggest this for two reasons: 
 * It is `PolyBoRi`, after all, not `BoPolyRi`. 
 * The other Sage polynomial ring(s) starts with "Polynomial" 

"""


---

Attachment


---

Comment by mhansen created at 2008-02-29 02:15:40

Changing status from new to assigned.


---

Comment by mhansen created at 2008-02-29 02:15:40

Changing assignee from malb to mhansen.


---

Comment by burcin created at 2008-02-29 09:16:23

By inspection only, the patch looks good. I assume it passes all the tests.

I am still not decided about this naming issue though. The arguments for renaming are not really valid.
 - It's named `PolyBoRi` to make it easy to pronounce. All the literature on `PolyBoRi` talks about Boolean polynomials, see http://polybori.sourceforge.net/further.shtml.
 - The class names should be easy to understand for humans, machines don't care what they are anyway. So why make them look machine like? `UnivariateRationalPolynomialRing` is more natural and easier to understand than `PolynomialRingUnivariateRational`.

If we agree that the original reasoning is correct, we should consider renaming `BooleanPolynomial` to `Polynomial_Boolean`, similarly for `BooleanMonomial` and `BooleanMonomialMonoid`. 

Note that none of these names are meant to be seen/used directly. AFAIK, the intention was to remove the `BooleanPolynomialRing` from the global scope, when it can be constructed with the usual methods.

BTW, to comply with current naming scheme, the new name should be `MPolynomial_something`.


---

Comment by cremona created at 2008-03-27 17:32:08

Burcin's case makes sense to me.  If I understand what these gadgets actually are, they are not a special case of polynomial ring, but rather a quotient of a polynomial ring (by lots of relations like `x^2-x`).  So it is a ring of these "boolean polynomials" rather than a polynomial ring over some underlying Boolean gadget.

It seem a pity for mhansen to have wasted his time, but that is not in itself a very strong argument!


---

Comment by mhansen created at 2008-03-28 01:35:40

I'm not at all attached to this.  It was just a 2 minute search and replace.


---

Comment by malb created at 2008-03-28 12:16:46

I vote against renaming it.


---

Comment by mabshoff created at 2008-03-29 00:09:37

Resolution: wontfix


---

Comment by mabshoff created at 2008-03-29 00:09:37


```
[00:31] <mhansen> mabshoff: For 2149, I think the consensus is to mark it as invalid.
[00:31] <mhansen> Or wontfix.
[00:31] <mabshoff> let me check in a minute
[00:31] <mhansen> Sure, no problem.
[00:37] <mabshoff> re #2149: won't fix it is.
```

