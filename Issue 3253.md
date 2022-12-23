# Issue 3253: f.jacob() used to work to compute jacobian ideal. Now it doesn't

Issue created by migration from https://trac.sagemath.org/ticket/3253

Original creator: jxxcarlson

Original creation time: 2008-05-18 03:43:31

Assignee: was

CC:  alexghitza

The code {{{ # file = singularlocus1.sage
K = QQ
R.<x,y,z> = PolynomialRing(K)
f = x^3 + y^3 + z^3
J = f.jacob()*R # Jacobian ideal
d = J.dimension()
print "f =", f
print "dimension(Jacobian ideal of f) =", d
print "projective dimension of singular locus of f =", d-1 }}}
generates an error:

[chiquito:jc] sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.0, Release Date: 2008-04-21                         |
| Type notebook() for the GUI, and license() for information.        |
sage: load "singularlocus1.sage"
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)

/Users/carlson/.sage/temp/chiquito.lan/9508/_Users_carlson_docs_chiquito__Research_CIMAT_Lectures_sageprogs_singularlocus1_sage_0.py in <module>()
      7 R = PolynomialRing(K,names=('x', 'y', 'z')); (x, y, z,) = R._first_ngens(Integer(3))
      8 f = x**Integer(3) + y**Integer(3) + z**Integer(3)
----> 9 J = f.jacob()*R # Jacobian ideal
     10 d = J.dimension()
     11 print "f =", f

<type 'exceptions.AttributeError'>: 'sage.rings.polynomial.multi_polynomial_libsingular' object has no attribute 'jacob'
WARNING: Failure executing file: </Users/carlson/.sage/temp/chiquito.lan/9508/_Users_carlson_docs_chiquito__Research_CIMAT_Lectures_sageprogs_singularlocus1_sage_0.py>


It seems that f.jacob() no longer exists.  (for a while it didn't, then it did, now it doesn')


---

Comment by mabshoff created at 2008-05-18 12:50:56

Hi Jim,

in 2.10.3-rc4 jacob() was changed to gradient() - see #2425 for details. We do not yet have a proper procedure to deprecate/rename functions like that, i.e. the old version would print a warning for a couple months and then be removed. I hope this fixes the issue for you.

I will bring the deprecation issue up on sage-devel again since last time we didn't really have an end result from the discussion and as more people that don't follow development too closely use Sage we want to avoid breaking their code needlessly and if we have to change names it should be clear what caused it and suggest a fix.

Cheers,

Michael


---

Comment by malb created at 2008-08-18 17:46:03

What should we do with this ticket? I vote for closing as wontfix since it would be strange to add a jacob method again with a deprecation warning, wouldn't it?


---

Comment by kedlaya created at 2008-08-27 14:16:27

I just encountered this issue myself. I have no problem with what f.gradient() does, but I would like to also have a command f.jacobian_ideal() that returns the ideal rather than the list of partial derivatives. (And I think f.jacobian_ideal() is a better name than f.jacob(), since I think the Sage model is to have long but descriptive names rather than concise but cryptic names for functions.)

Since the original issue from this ticket is resolved, I'm reclassifying this from "major defect" to "minor enhancement".


---

Comment by kedlaya created at 2008-08-27 14:16:27

Changing type from defect to enhancement.


---

Comment by kedlaya created at 2008-08-27 14:16:27

Changing priority from major to minor.


---

Comment by AlexGhitza created at 2008-08-27 22:57:19

The patch implements Kiran's request.


---

Comment by malb created at 2008-08-27 23:39:30

This function should not be implemented for `sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular` but for `sage.rings.polynomial.multi_polynomial.MPolynomial`. The former inherits from the later. I suppose that'd also mean to move `gradient` to `MPolynomial`.


---

Attachment


---

Comment by AlexGhitza created at 2008-08-28 03:40:40

Ah, I thought this might come up.  I have replaced the patch with a new one, where I have put a very simple-minded gradient() function in MPolynomial, but it is of course quite a bit slower than the specialized one for MPolynomial_libsingular, so I don't want to remove the latter.  The function jacobian_ideal() is now in MPolynomial.

BTW, if anyone has ideas on how to make the generic gradient() faster in MPolynomial, I would happily implement them.


---

Comment by malb created at 2008-08-28 10:34:35

Looks good.


---

Comment by mabshoff created at 2008-08-28 12:00:27

Resolution: fixed


---

Comment by mabshoff created at 2008-08-28 12:00:27

Merged in Sage 3.1.2.alpha2
