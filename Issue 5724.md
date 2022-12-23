# Issue 5724: [with patch; needs review] get coverage of quotient_ring_element.py to 100%

Issue created by migration from https://trac.sagemath.org/ticket/5724

Original creator: was

Original creation time: 2009-04-09 07:53:27

Assignee: malb




---

Attachment


---

Comment by was created at 2009-04-09 07:55:13

This patch gets coverage of quotient_ring_element.py up from 24% to 100%.  It also deletes a copy method, which we should have, and which was clearly broken (it would never work).   It fixes __cmp__ which always returned -1 if two objects weren't equal, which is really stupid.


---

Comment by malb created at 2009-04-09 10:52:27

You seem to prefer to write doctests which call the method directly rather than calling it indirectly (`_repr_()`, `_singular_()`, `__nonzero__()`, `_add_()`). I think having those in the docstrings as examples encourages bad style. Thus, I'd suggest to change that.


---

Attachment

move some doctests to TESTS:, change others to indirect tests.


---

Comment by malb created at 2009-04-10 12:35:10

*Review*
 * I don't think `sage: a._QuotientRingElement__rep` belongs as an example since it encourages to use hidden attributes directly
 * Why don't you replace the doctest in `_add_` and friends with example which involve `+` and friends? This way it is clear when this function is called.

If this is addressed, I'd give it a positive review.

A side question: It seems `QuotientRingElement` is exclusively used for quotient rings over (multivariate) polynomials ideals. Shouldn't it be moved & renamed to `polynomial.QuotientRingPolynomial`?  Also, I guess the API of QRE should be adapted to have all the methods of multivariate polynomials (except those which don't make sense). That'd be another ticket though.


---

Attachment


---

Comment by cremona created at 2009-04-10 15:49:33

Interesting discussion and patches.  Two comments:

    1. Do these quotient ring elements really only work for multiple-variable polynomial rings?  That is a pity.  I have tried working in quotients R/I where R is the rings of integers of a number field and I an integral ideal, but without much joy, and perhaps this is why.

    2. Although there are now lots of examples/tests, a lot of functions still lack the one-line description.  (e.g. _integer_(), what is that supposed to do?  I don't believe that there is a sensibly canonical map from any quotient ring to ZZ!).


---

Comment by mabshoff created at 2009-04-11 01:30:12

I think William did fix all the things malb asked for, so I am changing this to a positive review in malb's name. All doctests do pass with all three patches applied.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-11 01:30:27

Resolution: fixed


---

Comment by mabshoff created at 2009-04-11 01:30:27

Merged all three patches in Sage 3.4.1.rc2.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-11 01:31:22

Oops, change review status accordingly. 

Cheers,

Michael


---

Comment by was created at 2009-04-11 05:28:36

>   1. Do these quotient ring elements really only 
> work for multiple-variable polynomial rings? That is a 
> pity. I have tried working in quotients R/I where R is ...

The intention was definitely that they work for any commutative ring for which there are algorithms to do some basic things with ideals (e.g., test membership).  This may not work well in practice right now.

> Although there are now lots of examples/tests, a lot of functions
>  still lack the one-line description. (e.g. _integer_(), what is 
> that supposed to do? I don't believe that there is a sensibly
>  canonical map from any quotient ring to ZZ!). 

All I did was add doctests.  Describing what all the functions do is much more work yet.

Regarding _integer_, that is *NOT* used for canonical maps.  It's used for forced coercion, e.g., ZZ(alpha).

William
