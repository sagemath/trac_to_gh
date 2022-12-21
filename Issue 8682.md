# Issue 8682: Improve AlgebraicScheme_subscheme.__init__ and AmbientSpace._validate

Issue created by migration from Trac.

Original creator: novoselt

Original creation time: 2010-04-13 21:19:45

Assignee: AlexGhitza

Creation of a subscheme given by polynomial equations in some ambient space involves converting the input to polynomials in the correct ring and checking that these polynomials are "OK", e.g. that they are homogeneous for the projective space. There are the following (little) problems with the current realization:
 * converting to the coordinate ring is done in _validate method of ambient spaces, but it is the same for all of them and in general I would expect that a method with such a name just checks something without modifying the input
 * if a subscheme is constructed using an ideal of a wrong ring, but polynomials can be converted into the coordinate ring of the ambient space, then wrong ideal will be saved for later use
 * _validate is not listed as a mandatory method for overriding by subclasses of AmbientSpace

The attached patch makes the following:
 * all conversions are done in !__init!__ of the subscheme
 * _validate of AmbientSpace's must check that the polynomials are OK, but they are already guaranteed to lie in the correct ring
 * _validate is listed as a method which must be overridden 
 * error messages in exceptions include only the polynomial that lead to the error, not the whole input

Apply on top of #8675.


---

Attachment


---

Comment by novoselt created at 2010-04-13 21:42:12

Changing status from new to needs_review.


---

Comment by AlexGhitza created at 2010-05-18 12:36:22

Changing status from needs_review to positive_review.


---

Comment by AlexGhitza created at 2010-05-18 12:36:22

Looks good to me.


---

Comment by mhansen created at 2010-06-06 07:49:08

Resolution: fixed
