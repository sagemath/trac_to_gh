# Issue 8751: conversion between non-prime finite fields

Issue created by migration from https://trac.sagemath.org/ticket/8751

Original creator: zimmerma

Original creation time: 2010-04-23 09:28:49

Assignee: AlexGhitza

CC:  cremona jpflori defeo pbruin

I noticed the following with Sage 4.3.5:

```
sage: R = GF(9,name='x')
sage: Q.<x> = PolynomialRing(GF(3))
sage: R2 = GF(9,name='x',modulus=x^2+1)
sage: a=R(x+1)
sage: R2(a)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/users/caramel/zimmerma/svn/sagebook/tex/<ipython console> in <module>()

/usr/local/sage-core2/local/lib/python2.6/site-packages/sage/rings/finite_field_givaro.so in sage.rings.finite_field_givaro.FiniteField_givaro.__call__ (sage/rings/finite_field_givaro.cpp:4754)()

TypeError: unable to coerce from a finite field other than the prime subfield
```

This is ok since indeed a=x+1 is not in the prime subfield.
But:

```
sage: b=R(1)
sage: R2(b)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/users/caramel/zimmerma/svn/sagebook/tex/<ipython console> in <module>()

/usr/local/sage-core2/local/lib/python2.6/site-packages/sage/rings/finite_field_givaro.so in sage.rings.finite_field_givaro.FiniteField_givaro.__call__ (sage/rings/finite_field_givaro.cpp:4754)()

TypeError: unable to coerce from a finite field other than the prime subfield
```

In this case b=1 ***is*** in the prime subfield!!!

Side question: is there a (simple) way to get the isomorphism between R and R2?


---

Comment by zimmerma created at 2013-03-19 13:04:36

any progress on the isomorphism between finite fields?

Paul


---

Comment by cremona created at 2013-03-19 13:10:03

Replying to [comment:1 zimmerma]:
> any progress on the isomorphism between finite fields?
> 
> Paul

See #8335


---

Comment by jpflori created at 2013-06-04 09:22:27

If anything has to be done here, it should definitely be after #8335 gets in indeed.


---

Comment by jpflori created at 2013-06-18 15:06:44

I guess here would be the place to craft a super fast system for "general" finite fields once #8335 and #11938 are done.

Some references:
* historical Magma implementation: http://www.sciencedirect.com/science/article/pii/S0747717197901383
* new Magma implementation:
 * http://magma.maths.usyd.edu.au/magma/releasenotes/2/14#subsection_7_3
 * http://magma.maths.usyd.edu.au/group/seminar/2006/11/09
 * http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.32.9996
 * older papers by Pinch, Allombert, Lenstra...


---

Comment by jpflori created at 2013-06-25 19:22:50

Link to Allombert paper:
* http://www.sciencedirect.com/science/article/pii/S1071579701903442

Rains communicated me its work.

So I guess I now have all that is needed to begin coding.


---

Comment by cremona created at 2013-06-25 19:52:59

Replying to [comment:5 jpflori]:
> Link to Allombert paper:
> * http://www.sciencedirect.com/science/article/pii/S1071579701903442
> 

Since he is a lead developer of pari and says in the paper that he has implemented his algorithm in pari, can we not just use that implementation by wrapping it?


> Rains communicated me its work.
> 
> So I guess I now have all that is needed to begin coding.


---

Comment by jpflori created at 2013-06-25 20:13:50

Replying to [comment:6 cremona]:
> Replying to [comment:5 jpflori]:
> > Link to Allombert paper:
> > * http://www.sciencedirect.com/science/article/pii/S1071579701903442
> > 
> 
> Since he is a lead developer of pari and says in the paper that he has implemented his algorithm in pari, can we not just use that implementation by wrapping it?
Of course, but that will not give us "lattices of compatible finite fields".

The way I see it, we should get the following tickets merged in that order:
* #8335 David Roe's for lattices using (pseudo) Conway polynomials, this only goes up and is obviously inefficient for large fields,
* #11938 which implements going down for finite field using Givaro, 
* maybe extend it to all fields using pseudo-Conway polynomials in a follow-up ticket,
* #13214 by Xavier Caruso, not sure how useful that will be, but that can give a nice code basis to start upon,
* this ticket to implement general lattices of compatible finite fields.
> 
> 
> > Rains communicated me its work.
> > 
> > So I guess I now have all that is needed to begin coding.


---

Comment by defeo created at 2013-06-27 03:13:07

Replying to [comment:4 jpflori]

Since it has been mentioned in the tickets related to this one, here's some more literature (by Doliskani, Schost and myself):

- 2-adic towers http://arxiv.org/abs/1110.4350
- l-adic (small l) towers http://defeo.lu/towers/ (the github repo includes a Sage toy implementation)
- p-adic (Artin-Schreier) towers http://www.sciencedirect.com/science/article/pii/S0747717111002008, with a C++ implementation https://github.com/defeo/FAAST

...still quite far from the complete picture.


---

Comment by pbruin created at 2013-07-13 21:14:25

Changing keywords from "" to "sd51".


---

Comment by zimmerma created at 2017-04-04 10:23:42

any progress on this ticket?


---

Comment by jpflori created at 2017-04-04 10:41:07

Not on my side...
We've been indenpendently working on computation of embeddings with Luca and others at:
* https://github.com/defeo/ffisom/
Inspired by this, the code in PARI/GP should be much better than 4 years ago as well.


---

Comment by jpflori created at 2017-04-04 10:42:44

Here is PARI/GP commit:
* http://pari.math.u-bordeaux.fr/cgi-bin/gitweb.cgi?p=pari.git;a=commit;h=608b3095e7e3dec83dad41fa737eec45d0ac3b2c
