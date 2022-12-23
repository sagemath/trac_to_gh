# Issue 5856: elliptic curves over Z/pZ are treated totally differently than elliptic curves over GF(p)

archive/issues_005856.json:
```json
{
    "body": "Assignee: was\n\nCC:  cremona\n\nWe have\n\n```\nsage: type(EllipticCurve(Zmod(11), [1,2]))\n<class 'sage.schemes.elliptic_curves.ell_generic.EllipticCurve_generic'>\nsage: type(EllipticCurve(GF(11), [1,2]))\n<class 'sage.schemes.elliptic_curves.ell_finite_field.EllipticCurve_finite_field'>\n```\n\n\nThis means that if you make a curve over Z/pZ then basically nothing works, but if you make the same curve over GF(p), there is tons of functionality.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5856\n\n",
    "created_at": "2009-04-22T15:47:38Z",
    "labels": [
        "number theory",
        "major",
        "enhancement"
    ],
    "title": "elliptic curves over Z/pZ are treated totally differently than elliptic curves over GF(p)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5856",
    "user": "was"
}
```
Assignee: was

CC:  cremona

We have

```
sage: type(EllipticCurve(Zmod(11), [1,2]))
<class 'sage.schemes.elliptic_curves.ell_generic.EllipticCurve_generic'>
sage: type(EllipticCurve(GF(11), [1,2]))
<class 'sage.schemes.elliptic_curves.ell_finite_field.EllipticCurve_finite_field'>
```


This means that if you make a curve over Z/pZ then basically nothing works, but if you make the same curve over GF(p), there is tons of functionality.

Issue created by migration from https://trac.sagemath.org/ticket/5856





---

archive/issue_comments_046267.json:
```json
{
    "body": "I see two options:\n\n1. Change the `EllipticCurve` constructor so that if it is given `Zmod(p)` for a prime number `p`, it actually returns the corresponding elliptic curve over `GF(p)`.  This would probably only take a couple of minutes to do.  However, this means that creating a curve over `Zmod(5)` would return a different type than creating a curve over `Zmod(4)`.\n\n2. We keep creating the curve over `Zmod(p)` as before but we attach to it the corresponding curve over `GF(p)` (cached).  We put in the headers of all the methods from `GF(p)` and have them call the corresponding methods from `GF(p)` to do all the work.  This is a somewhat ugly.\n\nRight now I like the first option better than the second.  But maybe there are better ideas out there, or convincing arguments in favour of one thing or the other.",
    "created_at": "2009-04-29T08:39:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5856#issuecomment-46267",
    "user": "AlexGhitza"
}
```

I see two options:

1. Change the `EllipticCurve` constructor so that if it is given `Zmod(p)` for a prime number `p`, it actually returns the corresponding elliptic curve over `GF(p)`.  This would probably only take a couple of minutes to do.  However, this means that creating a curve over `Zmod(5)` would return a different type than creating a curve over `Zmod(4)`.

2. We keep creating the curve over `Zmod(p)` as before but we attach to it the corresponding curve over `GF(p)` (cached).  We put in the headers of all the methods from `GF(p)` and have them call the corresponding methods from `GF(p)` to do all the work.  This is a somewhat ugly.

Right now I like the first option better than the second.  But maybe there are better ideas out there, or convincing arguments in favour of one thing or the other.



---

archive/issue_comments_046268.json:
```json
{
    "body": "I vote with Alex for 1.  This is in fact similar to the following:\n\n\n```\nLoading Sage library. Current Mercurial branch is: test2\nsage: E = EllipticCurve(ZZ, [1,2,3,4,5])\nsage: E.base_ring()\nInteger Ring\nsage: E.conductor()\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n\n/home/masgaj/.sage/temp/host_56_150/24208/_home_masgaj__sage_init_sage_0.py in <module>()\n\nAttributeError: 'EllipticCurve_generic' object has no attribute 'conductor'\n```\n\nas compared to \n\n```\nsage: E = EllipticCurve([1,2,3,4,5])\nsage: E.base_ring()\nRational Field\nsage: E.conductor()\n10351\n```\n\ni.e. we already choose to use the field of fractions as base ring when the entries are integers, and if we try to insist otherwise we get an ell_generic on which we can do rather little.\n\nOf course a purist would say that there is no such thing as an elliptic curve over ZZ (it would have to have everywhere good reduction), and we do not allow singular models.",
    "created_at": "2009-04-29T08:45:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5856#issuecomment-46268",
    "user": "cremona"
}
```

I vote with Alex for 1.  This is in fact similar to the following:


```
Loading Sage library. Current Mercurial branch is: test2
sage: E = EllipticCurve(ZZ, [1,2,3,4,5])
sage: E.base_ring()
Integer Ring
sage: E.conductor()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/masgaj/.sage/temp/host_56_150/24208/_home_masgaj__sage_init_sage_0.py in <module>()

AttributeError: 'EllipticCurve_generic' object has no attribute 'conductor'
```

as compared to 

```
sage: E = EllipticCurve([1,2,3,4,5])
sage: E.base_ring()
Rational Field
sage: E.conductor()
10351
```

i.e. we already choose to use the field of fractions as base ring when the entries are integers, and if we try to insist otherwise we get an ell_generic on which we can do rather little.

Of course a purist would say that there is no such thing as an elliptic curve over ZZ (it would have to have everywhere good reduction), and we do not allow singular models.



---

archive/issue_comments_046269.json:
```json
{
    "body": "The attached patch implements option 1 above in the cleanest way I could think of, and adds some doctests and explanations.",
    "created_at": "2009-04-29T13:26:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5856#issuecomment-46269",
    "user": "AlexGhitza"
}
```

The attached patch implements option 1 above in the cleanest way I could think of, and adds some doctests and explanations.



---

archive/issue_comments_046270.json:
```json
{
    "body": "Changing keywords from \"\" to \"elliptic curve integers mod prime\".",
    "created_at": "2009-04-29T13:26:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5856#issuecomment-46270",
    "user": "AlexGhitza"
}
```

Changing keywords from "" to "elliptic curve integers mod prime".



---

archive/issue_comments_046271.json:
```json
{
    "body": "Changing assignee from was to AlexGhitza.",
    "created_at": "2009-04-29T13:26:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5856#issuecomment-46271",
    "user": "AlexGhitza"
}
```

Changing assignee from was to AlexGhitza.



---

archive/issue_comments_046272.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-04-29T13:26:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5856#issuecomment-46272",
    "user": "AlexGhitza"
}
```

Changing status from new to assigned.



---

archive/issue_comments_046273.json:
```json
{
    "body": "I was expecting that here,\n\n```\nsage: F = Zmod(101) \n \t92\t        sage: EllipticCurve(F, [2, 3]) \n \t93\t        Elliptic Curve defined by y^2 = x^3 + 2*x + 3 over Ring of integers modulo 101 \n \t94\t        sage: E = EllipticCurve([F(2), F(3)]) \n \t95\t        sage: type(E) \n \t96\t        <class 'sage.schemes.elliptic_curves.ell_finite_field.EllipticCurve_finite_field'> \n```\n\nboth would end up as EllipticCurve_finite_field objects, but I guess that we have to have a way of constructing the other things, so that is ok.\nBut would it not be better to change the base_ring (and base_field) of E in the second case to GF(101)?\n\nNext (but not this patch's fault at all):\n\n\n```\nsage: R = Zmod(101)\nsage: is_Field(R)\nTrue\nsage: is_FiniteField(R)\nFalse\n```\n\n\nNow the second is justified since the is_*() functions are supposed to do a type test, not prove a theorem, but then why should the first not also return False?  Should this be a new ticket?\n\n\nHere:\n\n```\n227\t \t        raise ValueError, \"sequence of coefficients must have length at 2 or 5\" \n \t246\t        raise ValueError, \"sequence of coefficients must have length between 2 and 5\" \n```\n\nIt is [2,5] and not [2..5], and the only valid lengths are 2 and 5, so can we put that back to how it was?  \n\nSorry to be such a pain with my reviews...I'll give it a positive review if the very last point is seen to.",
    "created_at": "2009-04-29T15:29:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5856#issuecomment-46273",
    "user": "cremona"
}
```

I was expecting that here,

```
sage: F = Zmod(101) 
 	92	        sage: EllipticCurve(F, [2, 3]) 
 	93	        Elliptic Curve defined by y^2 = x^3 + 2*x + 3 over Ring of integers modulo 101 
 	94	        sage: E = EllipticCurve([F(2), F(3)]) 
 	95	        sage: type(E) 
 	96	        <class 'sage.schemes.elliptic_curves.ell_finite_field.EllipticCurve_finite_field'> 
```

both would end up as EllipticCurve_finite_field objects, but I guess that we have to have a way of constructing the other things, so that is ok.
But would it not be better to change the base_ring (and base_field) of E in the second case to GF(101)?

Next (but not this patch's fault at all):


```
sage: R = Zmod(101)
sage: is_Field(R)
True
sage: is_FiniteField(R)
False
```


Now the second is justified since the is_*() functions are supposed to do a type test, not prove a theorem, but then why should the first not also return False?  Should this be a new ticket?


Here:

```
227	 	        raise ValueError, "sequence of coefficients must have length at 2 or 5" 
 	246	        raise ValueError, "sequence of coefficients must have length between 2 and 5" 
```

It is [2,5] and not [2..5], and the only valid lengths are 2 and 5, so can we put that back to how it was?  

Sorry to be such a pain with my reviews...I'll give it a positive review if the very last point is seen to.



---

archive/issue_comments_046274.json:
```json
{
    "body": "Attachment\n\nReplying to [comment:5 cremona]:\n> I was expecting that here,\n> {{{\n> sage: F = Zmod(101) \n>  \t92\t        sage: EllipticCurve(F, [2, 3]) \n>  \t93\t        Elliptic Curve defined by y^2 = x^3 + 2*x + 3 over Ring of integers modulo 101 \n>  \t94\t        sage: E = EllipticCurve([F(2), F(3)]) \n>  \t95\t        sage: type(E) \n>  \t96\t        <class 'sage.schemes.elliptic_curves.ell_finite_field.EllipticCurve_finite_field'> \n> }}}\n> both would end up as EllipticCurve_finite_field objects, but I guess that we have to have a way of constructing the other things, so that is ok.\n> But would it not be better to change the base_ring (and base_field) of E in the second case to GF(101)?\n\nBoth of these do end up as `EllipticCurve_finite_field` objects, which is fine because (mathematically) `Zmod(101)` is a finite field.  However, I did not want to just change the base ring to `GF(101)` because I don't think it is necessary, and after all the user specified that she wanted the base ring to be `Zmod(101)`.  It's a bit pedantic, but we should give the user the object she asks for (if possible), not something that's isomorphic to it.  I think the point becomes more clear in another situation, which I ran into while testing this code: say you have an elliptic curve over a number field, and you take its reduction at some good prime.  You end up with an elliptic curve over what is mathematically a finite field, so should we just force this curve to be over `GF(q)` rather than `Residue field of...`?  We would be throwing away some information here, and I think we shouldn't.\n\nSo my philosophy in this patch was that we keep the base ring that the user asked for, but we're smart enough to recognise that it's (mathematically) a finite field so we create an elliptic curve of the appropriate type.\n\n> Next (but not this patch's fault at all):\n> \n> {{{\n> sage: R = Zmod(101)\n> sage: is_Field(R)\n> True\n> sage: is_FiniteField(R)\n> False\n> }}}\n> \n> Now the second is justified since the is_*() functions are supposed to do a type test, not prove a theorem, but then why should the first not also return False?  Should this be a new ticket?\n\nI noticed this as well when writing the code because I was getting inconsistent behaviour from these two functions.  It's a bit annoying for the developer (since we somehow assume that `is_*()` just checks types), but I guess it is documented...\n\n> \n> Here:\n> {{{\n> 227\t \t        raise ValueError, \"sequence of coefficients must have length at 2 or 5\" \n>  \t246\t        raise ValueError, \"sequence of coefficients must have length between 2 and 5\" \n> }}}\n> It is [2,5] and not [2..5], and the only valid lengths are 2 and 5, so can we put that back to how it was?  \n\nSorry about this one, I saw it from the corner of my eye and my hands did the typing before the brain had time to process it properly.  Also the \"at\" in \"length at 2 or 5\" confused me.  I've changed it now, and replaced the patch.\n\n> Sorry to be such a pain with my reviews...I'll give it a positive review if the very last point is seen to.\n\nI'm happy you are so careful with the reviews.  It's hard to think of everything that could go wrong (thank god for doctests), or that could be confusing, or that could be bad design, especially when you fix a particular bug without necessarily having the big picture in mind.  So it's great to have a fresh pair of eyes look over this stuff.\n\nI'm marking this as \"needs review\" again, but the only new change is reverting the \"2 to 5\" mistake.",
    "created_at": "2009-04-29T23:56:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5856#issuecomment-46274",
    "user": "AlexGhitza"
}
```

Attachment

Replying to [comment:5 cremona]:
> I was expecting that here,
> {{{
> sage: F = Zmod(101) 
>  	92	        sage: EllipticCurve(F, [2, 3]) 
>  	93	        Elliptic Curve defined by y^2 = x^3 + 2*x + 3 over Ring of integers modulo 101 
>  	94	        sage: E = EllipticCurve([F(2), F(3)]) 
>  	95	        sage: type(E) 
>  	96	        <class 'sage.schemes.elliptic_curves.ell_finite_field.EllipticCurve_finite_field'> 
> }}}
> both would end up as EllipticCurve_finite_field objects, but I guess that we have to have a way of constructing the other things, so that is ok.
> But would it not be better to change the base_ring (and base_field) of E in the second case to GF(101)?

Both of these do end up as `EllipticCurve_finite_field` objects, which is fine because (mathematically) `Zmod(101)` is a finite field.  However, I did not want to just change the base ring to `GF(101)` because I don't think it is necessary, and after all the user specified that she wanted the base ring to be `Zmod(101)`.  It's a bit pedantic, but we should give the user the object she asks for (if possible), not something that's isomorphic to it.  I think the point becomes more clear in another situation, which I ran into while testing this code: say you have an elliptic curve over a number field, and you take its reduction at some good prime.  You end up with an elliptic curve over what is mathematically a finite field, so should we just force this curve to be over `GF(q)` rather than `Residue field of...`?  We would be throwing away some information here, and I think we shouldn't.

So my philosophy in this patch was that we keep the base ring that the user asked for, but we're smart enough to recognise that it's (mathematically) a finite field so we create an elliptic curve of the appropriate type.

> Next (but not this patch's fault at all):
> 
> {{{
> sage: R = Zmod(101)
> sage: is_Field(R)
> True
> sage: is_FiniteField(R)
> False
> }}}
> 
> Now the second is justified since the is_*() functions are supposed to do a type test, not prove a theorem, but then why should the first not also return False?  Should this be a new ticket?

I noticed this as well when writing the code because I was getting inconsistent behaviour from these two functions.  It's a bit annoying for the developer (since we somehow assume that `is_*()` just checks types), but I guess it is documented...

> 
> Here:
> {{{
> 227	 	        raise ValueError, "sequence of coefficients must have length at 2 or 5" 
>  	246	        raise ValueError, "sequence of coefficients must have length between 2 and 5" 
> }}}
> It is [2,5] and not [2..5], and the only valid lengths are 2 and 5, so can we put that back to how it was?  

Sorry about this one, I saw it from the corner of my eye and my hands did the typing before the brain had time to process it properly.  Also the "at" in "length at 2 or 5" confused me.  I've changed it now, and replaced the patch.

> Sorry to be such a pain with my reviews...I'll give it a positive review if the very last point is seen to.

I'm happy you are so careful with the reviews.  It's hard to think of everything that could go wrong (thank god for doctests), or that could be confusing, or that could be bad design, especially when you fix a particular bug without necessarily having the big picture in mind.  So it's great to have a fresh pair of eyes look over this stuff.

I'm marking this as "needs review" again, but the only new change is reverting the "2 to 5" mistake.



---

archive/issue_comments_046275.json:
```json
{
    "body": "Thanks for the well-argued response.  The example you gave (reduction of an elliptic curve over a number field) is an excellent one.\n\nI just diff'd this patch with the earlier one to give the Positive Review.",
    "created_at": "2009-04-30T08:07:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5856#issuecomment-46275",
    "user": "cremona"
}
```

Thanks for the well-argued response.  The example you gave (reduction of an elliptic curve over a number field) is an excellent one.

I just diff'd this patch with the earlier one to give the Positive Review.



---

archive/issue_comments_046276.json:
```json
{
    "body": "Merged in Sage 3.4.2.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-30T09:07:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5856#issuecomment-46276",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.2.rc0.

Cheers,

Michael



---

archive/issue_comments_046277.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-30T09:07:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5856#issuecomment-46277",
    "user": "mabshoff"
}
```

Resolution: fixed
