# Issue 8751: conversion between non-prime finite fields

archive/issues_008751.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @JohnCremona jpflori @defeo @pjbruin\n\nI noticed the following with Sage 4.3.5:\n\n```\nsage: R = GF(9,name='x')\nsage: Q.<x> = PolynomialRing(GF(3))\nsage: R2 = GF(9,name='x',modulus=x^2+1)\nsage: a=R(x+1)\nsage: R2(a)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/users/caramel/zimmerma/svn/sagebook/tex/<ipython console> in <module>()\n\n/usr/local/sage-core2/local/lib/python2.6/site-packages/sage/rings/finite_field_givaro.so in sage.rings.finite_field_givaro.FiniteField_givaro.__call__ (sage/rings/finite_field_givaro.cpp:4754)()\n\nTypeError: unable to coerce from a finite field other than the prime subfield\n```\n\nThis is ok since indeed a=x+1 is not in the prime subfield.\nBut:\n\n```\nsage: b=R(1)\nsage: R2(b)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/users/caramel/zimmerma/svn/sagebook/tex/<ipython console> in <module>()\n\n/usr/local/sage-core2/local/lib/python2.6/site-packages/sage/rings/finite_field_givaro.so in sage.rings.finite_field_givaro.FiniteField_givaro.__call__ (sage/rings/finite_field_givaro.cpp:4754)()\n\nTypeError: unable to coerce from a finite field other than the prime subfield\n```\n\nIn this case b=1 ***is*** in the prime subfield!!!\n\nSide question: is there a (simple) way to get the isomorphism between R and R2?\n\nIssue created by migration from https://trac.sagemath.org/ticket/8751\n\n",
    "created_at": "2010-04-23T09:28:49Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "bug"
    ],
    "title": "conversion between non-prime finite fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8751",
    "user": "@zimmermann6"
}
```
Assignee: @aghitza

CC:  @JohnCremona jpflori @defeo @pjbruin

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

Issue created by migration from https://trac.sagemath.org/ticket/8751





---

archive/issue_comments_080060.json:
```json
{
    "body": "any progress on the isomorphism between finite fields?\n\nPaul",
    "created_at": "2013-03-19T13:04:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8751#issuecomment-80060",
    "user": "@zimmermann6"
}
```

any progress on the isomorphism between finite fields?

Paul



---

archive/issue_comments_080061.json:
```json
{
    "body": "Replying to [comment:1 zimmerma]:\n> any progress on the isomorphism between finite fields?\n> \n> Paul\n\nSee #8335",
    "created_at": "2013-03-19T13:10:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8751#issuecomment-80061",
    "user": "@JohnCremona"
}
```

Replying to [comment:1 zimmerma]:
> any progress on the isomorphism between finite fields?
> 
> Paul

See #8335



---

archive/issue_comments_080062.json:
```json
{
    "body": "If anything has to be done here, it should definitely be after #8335 gets in indeed.",
    "created_at": "2013-06-04T09:22:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8751#issuecomment-80062",
    "user": "jpflori"
}
```

If anything has to be done here, it should definitely be after #8335 gets in indeed.



---

archive/issue_comments_080063.json:
```json
{
    "body": "I guess here would be the place to craft a super fast system for \"general\" finite fields once #8335 and #11938 are done.\n\nSome references:\n* historical Magma implementation: http://www.sciencedirect.com/science/article/pii/S0747717197901383\n* new Magma implementation:\n  * http://magma.maths.usyd.edu.au/magma/releasenotes/2/14#subsection_7_3\n  * http://magma.maths.usyd.edu.au/group/seminar/2006/11/09\n  * http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.32.9996\n  * older papers by Pinch, Allombert, Lenstra...",
    "created_at": "2013-06-18T15:06:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8751#issuecomment-80063",
    "user": "jpflori"
}
```

I guess here would be the place to craft a super fast system for "general" finite fields once #8335 and #11938 are done.

Some references:
* historical Magma implementation: http://www.sciencedirect.com/science/article/pii/S0747717197901383
* new Magma implementation:
  * http://magma.maths.usyd.edu.au/magma/releasenotes/2/14#subsection_7_3
  * http://magma.maths.usyd.edu.au/group/seminar/2006/11/09
  * http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.32.9996
  * older papers by Pinch, Allombert, Lenstra...



---

archive/issue_comments_080064.json:
```json
{
    "body": "Link to Allombert paper:\n* http://www.sciencedirect.com/science/article/pii/S1071579701903442\n\nRains communicated me its work.\n\nSo I guess I now have all that is needed to begin coding.",
    "created_at": "2013-06-25T19:22:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8751#issuecomment-80064",
    "user": "jpflori"
}
```

Link to Allombert paper:
* http://www.sciencedirect.com/science/article/pii/S1071579701903442

Rains communicated me its work.

So I guess I now have all that is needed to begin coding.



---

archive/issue_comments_080065.json:
```json
{
    "body": "Replying to [comment:5 jpflori]:\n> Link to Allombert paper:\n> * http://www.sciencedirect.com/science/article/pii/S1071579701903442\n> \n\nSince he is a lead developer of pari and says in the paper that he has implemented his algorithm in pari, can we not just use that implementation by wrapping it?\n\n\n> Rains communicated me its work.\n> \n> So I guess I now have all that is needed to begin coding.",
    "created_at": "2013-06-25T19:52:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8751#issuecomment-80065",
    "user": "@JohnCremona"
}
```

Replying to [comment:5 jpflori]:
> Link to Allombert paper:
> * http://www.sciencedirect.com/science/article/pii/S1071579701903442
> 

Since he is a lead developer of pari and says in the paper that he has implemented his algorithm in pari, can we not just use that implementation by wrapping it?


> Rains communicated me its work.
> 
> So I guess I now have all that is needed to begin coding.



---

archive/issue_comments_080066.json:
```json
{
    "body": "Replying to [comment:6 cremona]:\n> Replying to [comment:5 jpflori]:\n> > Link to Allombert paper:\n> > * http://www.sciencedirect.com/science/article/pii/S1071579701903442\n> > \n> \n> Since he is a lead developer of pari and says in the paper that he has implemented his algorithm in pari, can we not just use that implementation by wrapping it?\nOf course, but that will not give us \"lattices of compatible finite fields\".\n\nThe way I see it, we should get the following tickets merged in that order:\n* #8335 David Roe's for lattices using (pseudo) Conway polynomials, this only goes up and is obviously inefficient for large fields,\n* #11938 which implements going down for finite field using Givaro, \n* maybe extend it to all fields using pseudo-Conway polynomials in a follow-up ticket,\n* #13214 by Xavier Caruso, not sure how useful that will be, but that can give a nice code basis to start upon,\n* this ticket to implement general lattices of compatible finite fields.\n> \n> \n> > Rains communicated me its work.\n> > \n> > So I guess I now have all that is needed to begin coding.",
    "created_at": "2013-06-25T20:13:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8751#issuecomment-80066",
    "user": "jpflori"
}
```

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

archive/issue_comments_080067.json:
```json
{
    "body": "Replying to [comment:4 jpflori]\n\nSince it has been mentioned in the tickets related to this one, here's some more literature (by Doliskani, Schost and myself):\n\n- 2-adic towers http://arxiv.org/abs/1110.4350\n- l-adic (small l) towers http://defeo.lu/towers/ (the github repo includes a Sage toy implementation)\n- p-adic (Artin-Schreier) towers http://www.sciencedirect.com/science/article/pii/S0747717111002008, with a C++ implementation https://github.com/defeo/FAAST\n\n...still quite far from the complete picture.",
    "created_at": "2013-06-27T03:13:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8751#issuecomment-80067",
    "user": "@defeo"
}
```

Replying to [comment:4 jpflori]

Since it has been mentioned in the tickets related to this one, here's some more literature (by Doliskani, Schost and myself):

- 2-adic towers http://arxiv.org/abs/1110.4350
- l-adic (small l) towers http://defeo.lu/towers/ (the github repo includes a Sage toy implementation)
- p-adic (Artin-Schreier) towers http://www.sciencedirect.com/science/article/pii/S0747717111002008, with a C++ implementation https://github.com/defeo/FAAST

...still quite far from the complete picture.



---

archive/issue_comments_080068.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd51\".",
    "created_at": "2013-07-13T21:14:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8751#issuecomment-80068",
    "user": "@pjbruin"
}
```

Changing keywords from "" to "sd51".



---

archive/issue_comments_080069.json:
```json
{
    "body": "any progress on this ticket?",
    "created_at": "2017-04-04T10:23:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8751#issuecomment-80069",
    "user": "@zimmermann6"
}
```

any progress on this ticket?



---

archive/issue_comments_080070.json:
```json
{
    "body": "Not on my side...\nWe've been indenpendently working on computation of embeddings with Luca and others at:\n* https://github.com/defeo/ffisom/\nInspired by this, the code in PARI/GP should be much better than 4 years ago as well.",
    "created_at": "2017-04-04T10:41:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8751#issuecomment-80070",
    "user": "jpflori"
}
```

Not on my side...
We've been indenpendently working on computation of embeddings with Luca and others at:
* https://github.com/defeo/ffisom/
Inspired by this, the code in PARI/GP should be much better than 4 years ago as well.



---

archive/issue_comments_080071.json:
```json
{
    "body": "Here is PARI/GP commit:\n* http://pari.math.u-bordeaux.fr/cgi-bin/gitweb.cgi?p=pari.git;a=commit;h=608b3095e7e3dec83dad41fa737eec45d0ac3b2c",
    "created_at": "2017-04-04T10:42:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8751#issuecomment-80071",
    "user": "jpflori"
}
```

Here is PARI/GP commit:
* http://pari.math.u-bordeaux.fr/cgi-bin/gitweb.cgi?p=pari.git;a=commit;h=608b3095e7e3dec83dad41fa737eec45d0ac3b2c
