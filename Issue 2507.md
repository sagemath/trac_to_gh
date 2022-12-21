# Issue 2507: Docstrings and Doctests for rings/quotient_ring_element.py

Issue created by migration from Trac.

Original creator: cswiercz

Original creation time: 2008-03-13 17:47:37

Assignee: failure

Keywords: docstring, doctest

Current coverage in Sage 2.10.3: SCORE quotient_ring_element.py: 3% (1 of 27)


---

Comment by cswiercz created at 2008-03-14 03:59:57

Changing assignee from failure to cswiercz.


---

Comment by cswiercz created at 2008-04-02 21:11:12

doctests and docstrings [SCORE quotient_ring_element.py: 37% (10 of 27)]


---

Attachment

Chris,

please make sure that you properly mark tickets with doctests added. Otherwise we cannot find them since attaching patches does not trigger an email to sage-trac.

Cheers,

Michael


---

Attachment

2507.patch applies against 3.0.alpha2 and passes tests.


---

Comment by mabshoff created at 2008-04-07 23:32:54

This patch needs to be rebase. It fails to apply cleanly against my current merge tree:

```
sage-3.0.alpha3/devel/sage$ patch -p1 < trac_2507_rings.quotient_ring_element.patch
patching file sage/rings/quotient_ring_element.py
Hunk #1 FAILED at 66.
Hunk #2 succeeded at 147 (offset 2 lines).
Hunk #3 succeeded at 274 (offset 2 lines).
```

Cheers,

Michael


---

Comment by malb created at 2008-04-10 23:23:09

I *really* like that someone sat down to write doctests for `quotient_ring_element.py`, but I see some issues:


```
sage: Q = ZZ.quotient(10*ZZ)
sage: type(Q)
<class 'sage.rings.integer_mod_ring.IntegerModRing_generic'>
sage: type(Q.gen())
<type 'sage.rings.integer_mod.IntegerMod_int'>
```


and


```
sage: R.<a> = QuotientRing(QQ[x], x^2 + 1)
sage: type(R)
<class 'sage.rings.polynomial.polynomial_quotient_ring.PolynomialQuotientRing_field'>
sage: type(a)
<class 'sage.rings.polynomial.polynomial_quotient_ring_element.PolynomialQuotientRingElement'>
```


Thus, the documentation doesn't actually illustrate the class. AFAIK this class is mainly useful/used for multivariate polynomial rings. This theory reinforced by the `lm()` and `monomials()` methods. This class is just a mess, maybe?


---

Comment by cswiercz created at 2008-04-17 22:23:59

Addresses (sort of) the issues brought up by malb. Will additional detailed examples in a later patch. APPLY AFTER 2507.patch.


---

Comment by cswiercz created at 2008-04-17 23:53:47

Changing status from new to assigned.


---

Attachment


---

Comment by malb created at 2008-04-18 08:06:16

I am not sure this is the right fix: Doctests should test and demonstrate the class and it doesn't make sense to create the QuotientRing(ZZ,10) when ZZ.quotient(10) is available and much faster. Why not test it with the rings it is intended for (multivariate polynomials)?


---

Comment by mabshoff created at 2008-09-26 19:24:26

Mmm, this patch might have bitrotted. Anyway, it still needs a review.

Cheers,

Michael


---

Comment by malb created at 2008-09-28 14:18:51

I think this patch needs work since it doesn't doctest the main purpose of this class: multivariate polynomial quotients.


---

Comment by jhpalmieri created at 2009-05-10 16:48:33

The patch at #5724 added examples but not actual documentation -- no descriptions of what the various methods do. So I took the docstrings from the patches here, rewrote them a little, and made a new patch.  This patch replaces all of the others.


---

Comment by jhpalmieri created at 2009-05-10 16:51:30

(cswiercz should get credit for this as well as me, since I took the docstrings from the previous patches here.)


---

Comment by mvngu created at 2009-05-11 02:27:48

First, two trivial issues with the patch `trac_2507.patch`. The double colon on line 48 is not indented properly. It should be aligned with the double colon on line 53. Also, the docstring for `_div_` is a bit confusing due to excessive use of the word "quotient". The word "quotient" as used in

```
263	        Quotient of quotient ring element ``self`` by another quotient ring 
264	        element, ``right``. If the quotient is `R/I`, the division is 
265	        carried out in `R` and then reduced to `R/I`.
```

has two meanings: to denote division of one element by another; and to mean a quotient ring. When division is intended, I think "division" should be used instead of quotient. So line 263 of the docstring can be changed as follows to avoid confusion/ambiguity:

```
263	        Division of quotient ring element ``self`` by another quotient ring 
264	        element, ``right``. If the quotient is `R/I`, the division is 
265	        carried out in `R` and then reduced to `R/I`.
```

The other issue is that in the constructor signature

```
77	    def __init__(self, parent, rep, reduce=True):
```

the input are not documented. My knowledge of quotient rings is pretty limited, and it can be difficult to work out what each of the arguments `parent`, `rep` and `reduce=True` means, and how to use them properly.


---

Comment by jhpalmieri created at 2009-05-11 17:06:09

Here's a new patch.


---

Comment by jhpalmieri created at 2009-05-11 17:06:27

apply only this patch


---

Attachment

All my concerns have been addressed in the patch `trac_2507.patch`. Doctest coverage for `sage/rings/quotient_ring_element.py` is now 100%. Positive review.


---

Comment by mabshoff created at 2009-05-13 18:35:31

Merged trac_2507.patch in Sage 4.0.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-13 18:35:31

Resolution: fixed
