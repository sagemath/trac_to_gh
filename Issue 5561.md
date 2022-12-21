# Issue 5561: is_primitive does not belong in Polynomial because its definition varies

Issue created by migration from Trac.

Original creator: rhinton

Original creation time: 2009-03-18 17:21:16

Assignee: tbd

CC:  cremona cwitty

(I'm not a mathematician.  Please correct any mistakes!)

The current `Polynomial` class (`sage/rings/polynomial/polynomial_element.pyx`) includes an `is_primitive` method.  However, field theory and ring theory have different definitions of a "primitive polynomial."  Consequently, this base class for all polynomials is not an appropriate place for this method.  

C.Witty suggested on IRC that one way to resolve the issue is to split up the polynomial classes into "polynomials over fields" and "polynomials over rings."  Then these new base classes (and/or their derived classes) can implement `is_primitive` as appropriate.  In other words, create `PolynomialOverField` class and `PolynomialOverRing` classes that derive from `Polynomial`.  The other (univariate) polynomial classes in sage/rings/polynomial/ should then derive from either `PolynomialOverField` or `PolynomialOverRing` to pick up the correct `is_primitive` definition.

There may be other and possibly better ways to resolve the issue.

John Cremona added this comment:

  What Ryan suggest for is_primitive might be a good way to go;  as far
  as I know the meaning which is relevant here, namely "irreducible and
  the root generates the multiplicative group of the extension" is only
  relevant over finite fields (and no other fields).  The other meaning
  (coprime coefficients) is certainly not very useful over fields as it
  is the same as "non-zero", so we are left with the question "what, if
  anything, should we take is_primitive() to mean for polynomials in
  F[x] where F is an infinite field?"




---

Comment by cremona created at 2009-03-18 20:13:43

On second thougths, Carl Witty's suggestion seems to be overdoing things a bit.

We could just do this (all explained properly in docstrings, of course):   

```
R=self.base_ring()
if R.is_field() and R.is_finite():
# use the current code
else:
   return R.ideal(self.coefficient_list())==R.ideal(1)
```



---

Comment by rhinton created at 2009-04-01 15:35:06

Patch applies against 3.4.1.alpha0 or 3.4.0 on top of patch for #5535.  Note that #5658 provides a performance improvement when q<sup>d</sup>-1 is prime (order<sup>degree</sup> - 1).


---

Comment by cremona created at 2009-04-01 16:02:44

review: needs a little work!
    
   1. insert "not" before "R.is_finite()" !
   2. the line  return R.ideal(self.coefficient_list())==R.ideal(1)  does not work.

Both these were discovered using plain "sage -t" on the file.

I fear that resolving the second one will reveal nasty inconsistencies in ideal creation for various rings.   First change self.coefficient_list() to self.list(), I think.  And change R.ideal(1) to R.unit_ideal().  then the only thing which fails is the pair of examples over Integers(10).  But this is a different bug:

```
sage: Integers(10).ideal([5,2])
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/masgaj/.sage/temp/host_56_150/31627/_home_masgaj__sage_init_sage_0.py in <module>()

/local/jec/sage-3.4.1.alpha0/local/lib/python2.5/site-packages/sage/rings/quotient_ring.pyc in ideal(self, *gens, **kwds)
    487             gens = gens[0]
    488         from sage.rings.polynomial.multi_polynomial_libsingular import MPolynomialRing_libsingular
--> 489         if not isinstance(self.__R,MPolynomialRing_libsingular) and not self.__R._has_singular:
    490             # pass through
    491             MPolynomialRing_generic.ideal(self,gens,**kwds)

AttributeError: 'sage.rings.integer_ring.IntegerRing_class' object has no attribute '_has_singular'
```


which will have to get ticketed and fixed before this one is done (unless we just delete that example for now).


---

Comment by rhinton created at 2009-04-01 16:14:59

Thanks for looking at this!  I had already fixed (1) and the coefficient_list part of (2).  I'll comment out the examples for now -- do you want to create a ticket or shall I?

This patch needs some examples of the ring functionality.  Can you provide any good (i.e. non-trivial, working) examples of the ring semantics?


---

Comment by rhinton created at 2009-04-01 16:16:10

Changing assignee from tbd to rhinton.


---

Attachment

The new patch compiles and passes the doctests, but it has no tests for the new ring functionality.  John, can you provide any good examples (that will work)?  Do you want to report the integer mod ring ideal problem, or shall I?


---

Attachment

replaces previous


---

Comment by cremona created at 2009-04-02 08:06:19

I have added a new patch (replaces previous) which just adds examples for the ring functionality.

I could not find a ticket relevant to the ideal creation problem for Integers(10) but have asked about it on sage-devel and will open a new ticket if appropriate.

cwitty, any chance of a review?


---

Comment by cwitty created at 2009-04-11 05:43:02

Code looks good, doctests pass.  Positive review.


---

Comment by mabshoff created at 2009-04-13 03:36:31

Merged trac_5561.patch in Sage 3.4.1.rc3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-13 03:36:31

Resolution: fixed
