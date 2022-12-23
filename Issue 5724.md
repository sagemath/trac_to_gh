# Issue 5724: [with patch; needs review] get coverage of quotient_ring_element.py to 100%

archive/issues_005724.json:
```json
{
    "body": "Assignee: malb\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5724\n\n",
    "created_at": "2009-04-09T07:53:27Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "title": "[with patch; needs review] get coverage of quotient_ring_element.py to 100%",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5724",
    "user": "was"
}
```
Assignee: malb



Issue created by migration from https://trac.sagemath.org/ticket/5724





---

archive/issue_comments_044728.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-04-09T07:54:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5724#issuecomment-44728",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_044729.json:
```json
{
    "body": "This patch gets coverage of quotient_ring_element.py up from 24% to 100%.  It also deletes a copy method, which we should have, and which was clearly broken (it would never work).   It fixes __cmp__ which always returned -1 if two objects weren't equal, which is really stupid.",
    "created_at": "2009-04-09T07:55:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5724#issuecomment-44729",
    "user": "was"
}
```

This patch gets coverage of quotient_ring_element.py up from 24% to 100%.  It also deletes a copy method, which we should have, and which was clearly broken (it would never work).   It fixes __cmp__ which always returned -1 if two objects weren't equal, which is really stupid.



---

archive/issue_comments_044730.json:
```json
{
    "body": "You seem to prefer to write doctests which call the method directly rather than calling it indirectly (`_repr_()`, `_singular_()`, `__nonzero__()`, `_add_()`). I think having those in the docstrings as examples encourages bad style. Thus, I'd suggest to change that.",
    "created_at": "2009-04-09T10:52:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5724#issuecomment-44730",
    "user": "malb"
}
```

You seem to prefer to write doctests which call the method directly rather than calling it indirectly (`_repr_()`, `_singular_()`, `__nonzero__()`, `_add_()`). I think having those in the docstrings as examples encourages bad style. Thus, I'd suggest to change that.



---

archive/issue_comments_044731.json:
```json
{
    "body": "Attachment\n\nmove some doctests to TESTS:, change others to indirect tests.",
    "created_at": "2009-04-10T01:15:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5724#issuecomment-44731",
    "user": "was"
}
```

Attachment

move some doctests to TESTS:, change others to indirect tests.



---

archive/issue_comments_044732.json:
```json
{
    "body": "**Review**\n* I don't think `sage: a._QuotientRingElement__rep` belongs as an example since it encourages to use hidden attributes directly\n* Why don't you replace the doctest in `_add_` and friends with example which involve `+` and friends? This way it is clear when this function is called.\n\nIf this is addressed, I'd give it a positive review.\n\nA side question: It seems `QuotientRingElement` is exclusively used for quotient rings over (multivariate) polynomials ideals. Shouldn't it be moved & renamed to `polynomial.QuotientRingPolynomial`?  Also, I guess the API of QRE should be adapted to have all the methods of multivariate polynomials (except those which don't make sense). That'd be another ticket though.",
    "created_at": "2009-04-10T12:35:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5724#issuecomment-44732",
    "user": "malb"
}
```

**Review**
* I don't think `sage: a._QuotientRingElement__rep` belongs as an example since it encourages to use hidden attributes directly
* Why don't you replace the doctest in `_add_` and friends with example which involve `+` and friends? This way it is clear when this function is called.

If this is addressed, I'd give it a positive review.

A side question: It seems `QuotientRingElement` is exclusively used for quotient rings over (multivariate) polynomials ideals. Shouldn't it be moved & renamed to `polynomial.QuotientRingPolynomial`?  Also, I guess the API of QRE should be adapted to have all the methods of multivariate polynomials (except those which don't make sense). That'd be another ticket though.



---

archive/issue_comments_044733.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-04-10T14:43:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5724#issuecomment-44733",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_044734.json:
```json
{
    "body": "Interesting discussion and patches.  Two comments:\n\n1. Do these quotient ring elements really only work for multiple-variable polynomial rings?  That is a pity.  I have tried working in quotients R/I where R is the rings of integers of a number field and I an integral ideal, but without much joy, and perhaps this is why.\n\n2. Although there are now lots of examples/tests, a lot of functions still lack the one-line description.  (e.g. _integer_(), what is that supposed to do?  I don't believe that there is a sensibly canonical map from any quotient ring to ZZ!).",
    "created_at": "2009-04-10T15:49:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5724#issuecomment-44734",
    "user": "cremona"
}
```

Interesting discussion and patches.  Two comments:

1. Do these quotient ring elements really only work for multiple-variable polynomial rings?  That is a pity.  I have tried working in quotients R/I where R is the rings of integers of a number field and I an integral ideal, but without much joy, and perhaps this is why.

2. Although there are now lots of examples/tests, a lot of functions still lack the one-line description.  (e.g. _integer_(), what is that supposed to do?  I don't believe that there is a sensibly canonical map from any quotient ring to ZZ!).



---

archive/issue_comments_044735.json:
```json
{
    "body": "I think William did fix all the things malb asked for, so I am changing this to a positive review in malb's name. All doctests do pass with all three patches applied.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-11T01:30:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5724#issuecomment-44735",
    "user": "mabshoff"
}
```

I think William did fix all the things malb asked for, so I am changing this to a positive review in malb's name. All doctests do pass with all three patches applied.

Cheers,

Michael



---

archive/issue_comments_044736.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-11T01:30:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5724#issuecomment-44736",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_044737.json:
```json
{
    "body": "Merged all three patches in Sage 3.4.1.rc2.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-11T01:30:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5724#issuecomment-44737",
    "user": "mabshoff"
}
```

Merged all three patches in Sage 3.4.1.rc2.

Cheers,

Michael



---

archive/issue_comments_044738.json:
```json
{
    "body": "Oops, change review status accordingly. \n\nCheers,\n\nMichael",
    "created_at": "2009-04-11T01:31:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5724#issuecomment-44738",
    "user": "mabshoff"
}
```

Oops, change review status accordingly. 

Cheers,

Michael



---

archive/issue_comments_044739.json:
```json
{
    "body": ">   1. Do these quotient ring elements really only \n> work for multiple-variable polynomial rings? That is a \n> pity. I have tried working in quotients R/I where R is ...\n\nThe intention was definitely that they work for any commutative ring for which there are algorithms to do some basic things with ideals (e.g., test membership).  This may not work well in practice right now.\n\n> Although there are now lots of examples/tests, a lot of functions\n>  still lack the one-line description. (e.g. _integer_(), what is \n> that supposed to do? I don't believe that there is a sensibly\n>  canonical map from any quotient ring to ZZ!). \n\nAll I did was add doctests.  Describing what all the functions do is much more work yet.\n\nRegarding _integer_, that is *NOT* used for canonical maps.  It's used for forced coercion, e.g., ZZ(alpha).\n\nWilliam",
    "created_at": "2009-04-11T05:28:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5724#issuecomment-44739",
    "user": "was"
}
```

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
