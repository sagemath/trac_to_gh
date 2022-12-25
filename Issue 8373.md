# Issue 8373: finite fields constructed with non-primitive defining polynomial

archive/issues_008373.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @pjbruin\n\nConsider the following code:\n\n```\nsage: R.<x> = PolynomialRing(GF(2))\nsage: K.<a> = GF(16, modulus=x^4+x^3+x^2+x+1)\nsage: a^5\n1\n```\n\n\nThis is all fine mathematically, as long as the user is clear what a is and isn't (it isn't a generator for the multiplicative group of the finite field). So the options as I see them (in increasing difficulty for implementation):\n\n1)GF already checks modulus for irreducibility, just add check for modulus.is_primitive().\n\n2)Rewrite the help for the GF function to indicate that the function does not return a generator necessarily (like in this specific case).\n\n3)Find an actual generator (that might not be the polynomial x) and return that.\n\n\nOpinions?\n\nIssue created by migration from https://trac.sagemath.org/ticket/8373\n\n",
    "created_at": "2010-02-26T06:47:28Z",
    "labels": [
        "component: basic arithmetic",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "finite fields constructed with non-primitive defining polynomial",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8373",
    "user": "https://trac.sagemath.org/admin/accounts/users/rkirov"
}
```
Assignee: @aghitza

CC:  @pjbruin

Consider the following code:

```
sage: R.<x> = PolynomialRing(GF(2))
sage: K.<a> = GF(16, modulus=x^4+x^3+x^2+x+1)
sage: a^5
1
```


This is all fine mathematically, as long as the user is clear what a is and isn't (it isn't a generator for the multiplicative group of the finite field). So the options as I see them (in increasing difficulty for implementation):

1)GF already checks modulus for irreducibility, just add check for modulus.is_primitive().

2)Rewrite the help for the GF function to indicate that the function does not return a generator necessarily (like in this specific case).

3)Find an actual generator (that might not be the polynomial x) and return that.


Opinions?

Issue created by migration from https://trac.sagemath.org/ticket/8373





---

archive/issue_comments_074732.json:
```json
{
    "body": "Replying to [ticket:8373 rkirov]:\n\nIn your example,\u00a0`a` *is* a generator; it's an *algebra generator*.  In fact `a` generates `K` in exactly the same sense in which `x` generates `R`.  What you're looking for is:\n\n\n```\nsage: R.<x> = GF(2)[]\nsage: K.<a> = GF(16, modulus=x^4+x^3+x^2+x+1)\nsage: K.multiplicative_generator()\na + 1\n```\n\nIt would be a mistake to insist on having a primitive generator.  Of your options:\u00a0\n\n(1) could slow Sage down unnecessarily, and what should it do if a user wanted to use a non-primitive generator?\n\n(2) yes, if the documentation is confusing, it should be clarified.\n\n(3) I don't quite understand.  If you mean ignore a given modulus if  it is not primitive, that would be very confusing.\n\nWhat *is* needed, for non-prime fields of large characteristic, is a much better way of finding a multiplicative generator:\n\n\n```\nsage: p = 65537\nsage: K.<a> = GF(p^2)\nsage: a.multiplicative_order() == p^2 - 1\nFalse\nsage: time K.multiplicative_generator()\nCPU times: user 498.03 s, sys: 56.61 s, total: 554.64 s\nWall time: 555.20 s\na + 3\n```\n\nWhat's taking the time here is that the current algorithm, after deciding that `a` isn't a multiplicative generator,  pointlessly computes the multiplicative order of all the non-zero elements in the prime field, before trying `a` (again), `a + 1`, `a + 2`, and succeeding with `a + 3`.",
    "created_at": "2010-02-26T09:32:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8373#issuecomment-74732",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Replying to [ticket:8373 rkirov]:

In your example, `a` *is* a generator; it's an *algebra generator*.  In fact `a` generates `K` in exactly the same sense in which `x` generates `R`.  What you're looking for is:


```
sage: R.<x> = GF(2)[]
sage: K.<a> = GF(16, modulus=x^4+x^3+x^2+x+1)
sage: K.multiplicative_generator()
a + 1
```

It would be a mistake to insist on having a primitive generator.  Of your options: 

(1) could slow Sage down unnecessarily, and what should it do if a user wanted to use a non-primitive generator?

(2) yes, if the documentation is confusing, it should be clarified.

(3) I don't quite understand.  If you mean ignore a given modulus if  it is not primitive, that would be very confusing.

What *is* needed, for non-prime fields of large characteristic, is a much better way of finding a multiplicative generator:


```
sage: p = 65537
sage: K.<a> = GF(p^2)
sage: a.multiplicative_order() == p^2 - 1
False
sage: time K.multiplicative_generator()
CPU times: user 498.03 s, sys: 56.61 s, total: 554.64 s
Wall time: 555.20 s
a + 3
```

What's taking the time here is that the current algorithm, after deciding that `a` isn't a multiplicative generator,  pointlessly computes the multiplicative order of all the non-zero elements in the prime field, before trying `a` (again), `a + 1`, `a + 2`, and succeeding with `a + 3`.



---

archive/issue_comments_074733.json:
```json
{
    "body": "I guess you are right, it is a generator as an algebra. Somehow I assumed F.<a> gives you 'a' as a multiplicative generator. So it is really a renaming of 'x'(poly var)->'a'. I didn't see the convenient function F.multiplicative_generator.\n\nI checked that Magma has similar behavior.\n\n\n```\n> F2 := GF(2);\n> FP<x> := PolynomialRing(F2);\n> F<z> := ext< F2 | x^4+x^3+x^2+x+1 >;\n```\n\nIt also seems to have different algorithm for primitive element,\n\n```\n> PrimitiveElement(F);\nz^3 + z + 1\n```\n\n\nIn any case I am leaving this open so someone can work on the bug you found.",
    "created_at": "2010-02-26T10:50:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8373#issuecomment-74733",
    "user": "https://trac.sagemath.org/admin/accounts/users/rkirov"
}
```

I guess you are right, it is a generator as an algebra. Somehow I assumed F.<a> gives you 'a' as a multiplicative generator. So it is really a renaming of 'x'(poly var)->'a'. I didn't see the convenient function F.multiplicative_generator.

I checked that Magma has similar behavior.


```
> F2 := GF(2);
> FP<x> := PolynomialRing(F2);
> F<z> := ext< F2 | x^4+x^3+x^2+x+1 >;
```

It also seems to have different algorithm for primitive element,

```
> PrimitiveElement(F);
z^3 + z + 1
```


In any case I am leaving this open so someone can work on the bug you found.



---

archive/issue_comments_074734.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2014-06-26T14:56:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8373#issuecomment-74734",
    "user": "https://github.com/jdemeyer"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_074735.json:
```json
{
    "body": "This is certainly not a bug, but possibly a feature request.\n\nI would propose adding the option `modulus=\"primitive\"` to solve this ticket.",
    "created_at": "2014-06-26T14:56:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8373#issuecomment-74735",
    "user": "https://github.com/jdemeyer"
}
```

This is certainly not a bug, but possibly a feature request.

I would propose adding the option `modulus="primitive"` to solve this ticket.



---

archive/issue_comments_074736.json:
```json
{
    "body": "Changing assignee from @aghitza to @ClementPernet.",
    "created_at": "2014-06-26T14:56:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8373#issuecomment-74736",
    "user": "https://github.com/jdemeyer"
}
```

Changing assignee from @aghitza to @ClementPernet.



---

archive/issue_comments_074737.json:
```json
{
    "body": "Changing component from basic arithmetic to finite rings.",
    "created_at": "2014-06-26T14:56:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8373#issuecomment-74737",
    "user": "https://github.com/jdemeyer"
}
```

Changing component from basic arithmetic to finite rings.



---

archive/issue_comments_074738.json:
```json
{
    "body": "Replying to [comment:5 jdemeyer]:\n\nThe idea of allowing modulus='primitive' is good.  But a problem with the modified description is that the discussion in comments 1 and 2 is now out of context.",
    "created_at": "2014-08-05T17:48:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8373#issuecomment-74738",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Replying to [comment:5 jdemeyer]:

The idea of allowing modulus='primitive' is good.  But a problem with the modified description is that the discussion in comments 1 and 2 is now out of context.



---

archive/issue_comments_074739.json:
```json
{
    "body": "Replying to [comment:6 fwclarke]:\n> Replying to [comment:5 jdemeyer]:\n> \n> The idea of allowing modulus='primitive' is good.\nAnd sufficient for you to consider this issue fixed?\n\n> But a problem with the modified description is that the discussion in comments 1 and 2 is now out of context.\nSure, but that's not really a problem, right?",
    "created_at": "2014-08-05T19:35:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8373#issuecomment-74739",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:6 fwclarke]:
> Replying to [comment:5 jdemeyer]:
> 
> The idea of allowing modulus='primitive' is good.
And sufficient for you to consider this issue fixed?

> But a problem with the modified description is that the discussion in comments 1 and 2 is now out of context.
Sure, but that's not really a problem, right?



---

archive/issue_comments_074740.json:
```json
{
    "body": "Replying to [ticket:8373 rkirov]:\n\n> Also add an argument `modulus=\"pari\"` (and make it the default) to use PARI's `ffinit()`.\nThis already exists in `PolynomialRing_dense_mod_p.irreducible_element()` under the name `modulus=\"adleman-lenstra\"`.  It is the default if no Conway polynomial is known and the characteristic is odd.\n\nSome finite field implementations accept a string `modulus`, but this should be obsolete; `FiniteFieldFactory.create_key_and_extra_args()` uses the above method to convert a string `modulus` into an actual polynomial.",
    "created_at": "2014-09-03T12:04:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8373#issuecomment-74740",
    "user": "https://github.com/pjbruin"
}
```

Replying to [ticket:8373 rkirov]:

> Also add an argument `modulus="pari"` (and make it the default) to use PARI's `ffinit()`.
This already exists in `PolynomialRing_dense_mod_p.irreducible_element()` under the name `modulus="adleman-lenstra"`.  It is the default if no Conway polynomial is known and the characteristic is odd.

Some finite field implementations accept a string `modulus`, but this should be obsolete; `FiniteFieldFactory.create_key_and_extra_args()` uses the above method to convert a string `modulus` into an actual polynomial.



---

archive/issue_comments_074741.json:
```json
{
    "body": "Thanks for the pointer, I was confused by `PolynomialRing_dense_finite_field.irreducible_element`",
    "created_at": "2014-09-03T12:18:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8373#issuecomment-74741",
    "user": "https://github.com/jdemeyer"
}
```

Thanks for the pointer, I was confused by `PolynomialRing_dense_finite_field.irreducible_element`



---

archive/issue_comments_074742.json:
```json
{
    "body": "Replying to [comment:11 pbruin]:\n> Some finite field implementations accept a string `modulus`, but this should be obsolete\nWhy should it be obsolete? I think the syntax\n\n```\nk.<a> = GF(p^n, modulus=\"primitive\")\n```\n\nis very good to have. Note that the actual modulus polynomial is computed before the implementation is even considered. So it's not that every finite field implementation needs to be aware of this.",
    "created_at": "2014-09-03T12:26:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8373#issuecomment-74742",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:11 pbruin]:
> Some finite field implementations accept a string `modulus`, but this should be obsolete
Why should it be obsolete? I think the syntax

```
k.<a> = GF(p^n, modulus="primitive")
```

is very good to have. Note that the actual modulus polynomial is computed before the implementation is even considered. So it's not that every finite field implementation needs to be aware of this.



---

archive/issue_comments_074743.json:
```json
{
    "body": "Replying to [comment:13 jdemeyer]:\n> Replying to [comment:11 pbruin]:\n> > Some finite field implementations accept a string `modulus`, but this should be obsolete\n> Why should it be obsolete? I think the syntax\n> {{{\n> k.<a> = GF(p^n, modulus=\"primitive\")\n> }}}\n> is very good to have.\nYes, it is certainly not this syntax that needs to be made obsolete!\n> Note that the actual modulus polynomial is computed before the implementation is even considered. So it's not that every finite field implementation needs to be aware of this.\nThat is what I meant; the individual implementation should never need to consider the case where `modulus` is a string, it should all be handled by the factory.",
    "created_at": "2014-09-03T12:30:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8373#issuecomment-74743",
    "user": "https://github.com/pjbruin"
}
```

Replying to [comment:13 jdemeyer]:
> Replying to [comment:11 pbruin]:
> > Some finite field implementations accept a string `modulus`, but this should be obsolete
> Why should it be obsolete? I think the syntax
> {{{
> k.<a> = GF(p^n, modulus="primitive")
> }}}
> is very good to have.
Yes, it is certainly not this syntax that needs to be made obsolete!
> Note that the actual modulus polynomial is computed before the implementation is even considered. So it's not that every finite field implementation needs to be aware of this.
That is what I meant; the individual implementation should never need to consider the case where `modulus` is a string, it should all be handled by the factory.



---

archive/issue_comments_074744.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-09-03T13:49:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8373#issuecomment-74744",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_074745.json:
```json
{
    "body": "New commits:",
    "created_at": "2014-09-03T13:49:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8373#issuecomment-74745",
    "user": "https://github.com/jdemeyer"
}
```

New commits:



---

archive/issue_comments_074746.json:
```json
{
    "body": "Replying to [comment:15 pbruin]:\n> That is what I meant; the individual implementation should never need to consider the case where `modulus` is a string, it should all be handled by the factory.\n\nGood, this will be #16930.",
    "created_at": "2014-09-04T09:23:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8373#issuecomment-74746",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:15 pbruin]:
> That is what I meant; the individual implementation should never need to consider the case where `modulus` is a string, it should all be handled by the factory.

Good, this will be #16930.



---

archive/issue_comments_074747.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-09-04T12:31:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8373#issuecomment-74747",
    "user": "https://github.com/pjbruin"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_074748.json:
```json
{
    "body": "Looks good and passes tests.",
    "created_at": "2014-09-04T12:31:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8373#issuecomment-74748",
    "user": "https://github.com/pjbruin"
}
```

Looks good and passes tests.



---

archive/issue_comments_074749.json:
```json
{
    "body": "I got this on arando (linux 32-bit):\n\n```\nsage -t --long src/sage/rings/polynomial/polynomial_ring.py\n**********************************************************************\nFile \"src/sage/rings/polynomial/polynomial_ring.py\", line 2331, in sage.rings.polynomial.polynomial_ring.PolynomialRing_dense_mod_n.irreducible_element\nFailed example:\n    GF(5)['x'].irreducible_element(32, algorithm=\"primitive\")\nExpected:\n    x^32 + 4*x^31 + x^30 + 4*x^29 + 4*x^28 + 3*x^27 + 2*x^26 + x^25 + x^24 + x^23 + 4*x^21 + 3*x^20 + x^19 + 4*x^17 + 4*x^16 + 4*x^15 + 4*x^14 + 3*x^13 + x^12 + 3*x^11 + 4*x^10 + x^9 + 4*x^8 + x^7 + 2*x^6 + 4*x^5 + 4*x^4 + x^3 + 3*x^2 + 4*x + 2\nGot:\n    x^32 + 3*x^31 + x^30 + 4*x^28 + 2*x^27 + 2*x^26 + 2*x^24 + 2*x^23 + 2*x^22 + x^21 + 3*x^20 + 3*x^19 + x^18 + 3*x^17 + 4*x^16 + 2*x^15 + 3*x^12 + 4*x^11 + x^10 + 2*x^8 + 3*x^7 + 2*x^6 + 3*x^5 + x^4 + 4*x^3 + x + 3\n**********************************************************************\n```\n",
    "created_at": "2014-09-05T21:38:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8373#issuecomment-74749",
    "user": "https://github.com/vbraun"
}
```

I got this on arando (linux 32-bit):

```
sage -t --long src/sage/rings/polynomial/polynomial_ring.py
**********************************************************************
File "src/sage/rings/polynomial/polynomial_ring.py", line 2331, in sage.rings.polynomial.polynomial_ring.PolynomialRing_dense_mod_n.irreducible_element
Failed example:
    GF(5)['x'].irreducible_element(32, algorithm="primitive")
Expected:
    x^32 + 4*x^31 + x^30 + 4*x^29 + 4*x^28 + 3*x^27 + 2*x^26 + x^25 + x^24 + x^23 + 4*x^21 + 3*x^20 + x^19 + 4*x^17 + 4*x^16 + 4*x^15 + 4*x^14 + 3*x^13 + x^12 + 3*x^11 + 4*x^10 + x^9 + 4*x^8 + x^7 + 2*x^6 + 4*x^5 + 4*x^4 + x^3 + 3*x^2 + 4*x + 2
Got:
    x^32 + 3*x^31 + x^30 + 4*x^28 + 2*x^27 + 2*x^26 + 2*x^24 + 2*x^23 + 2*x^22 + x^21 + 3*x^20 + 3*x^19 + x^18 + 3*x^17 + 4*x^16 + 2*x^15 + 3*x^12 + 4*x^11 + x^10 + 2*x^8 + 3*x^7 + 2*x^6 + 3*x^5 + x^4 + 4*x^3 + x + 3
**********************************************************************
```




---

archive/issue_comments_074750.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2014-09-05T21:38:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8373#issuecomment-74750",
    "user": "https://github.com/vbraun"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_074751.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-09-06T06:33:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8373#issuecomment-74751",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_074752.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2014-09-06T06:55:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8373#issuecomment-74752",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_events_008560.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2014-09-08T08:48:58Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8373",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8373#event-8560"
}
```



---

archive/issue_comments_074753.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-09-08T08:48:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8373#issuecomment-74753",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
