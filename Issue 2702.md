# Issue 2702: [with patch, needs review] multi_polynomial_libsingular coverage almost 100%

archive/issues_002702.json:
```json
{
    "body": "Assignee: failure\n\n\n```\n----------------------------------------------------------------------\nsage/rings/polynomial/multi_polynomial_libsingular.pyx\nSCORE sage/rings/polynomial/multi_polynomial_libsingular.pyx: 98% (80 of 81)\n\nMissing doctests:\n         * _macaulay2_set_ring(self, macaulay2)\n\n----------------------------------------------------------------------\n```\n\n\nI cannot write a doctest for `_macaulay2_set_ring` yet because the optional M2 spkg is not installable.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2702\n\n",
    "created_at": "2008-03-28T17:24:12Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "[with patch, needs review] multi_polynomial_libsingular coverage almost 100%",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2702",
    "user": "https://github.com/malb"
}
```
Assignee: failure


```
----------------------------------------------------------------------
sage/rings/polynomial/multi_polynomial_libsingular.pyx
SCORE sage/rings/polynomial/multi_polynomial_libsingular.pyx: 98% (80 of 81)

Missing doctests:
         * _macaulay2_set_ring(self, macaulay2)

----------------------------------------------------------------------
```


I cannot write a doctest for `_macaulay2_set_ring` yet because the optional M2 spkg is not installable.

Issue created by migration from https://trac.sagemath.org/ticket/2702





---

archive/issue_comments_018594.json:
```json
{
    "body": "Attachment [mpoly_coverage_100.patch](tarball://root/attachments/some-uuid/ticket2702/mpoly_coverage_100.patch) by jbmohler created at 2008-03-28 18:50:14\n\nThis is a positive review about the patch, but it's a big patch and could use another set of eyes, I expect.  I think it looks like it cleans up a lot of evolved changes to make the whole thing more cohesive.  I did not apply and doc-test (because I don't have a recent 2.11.alphaX build).\n\nTwo specific comments:\n* 1) I think the documentation of is_monomial should be very clear that 2*x is not monomial (with a sentence in the initial header).  This is not my intuitive definition of monomial, but it's a sane definition.  I would prefer that 2*x be a monomial, but it's not a big deal.\n* 2)  I see a number of lines like\n\n```\nsage: Q.<x,y,z>=MPolynomialRing(QQ,3)\n```\n\nI think they should be one of the following:\n\n```\nsage: Q.<x,y,z>=PolynomialRing(QQ)\nsage: Q.<x,y,z>=QQ[]\n```\n\nWilliam has made the comment that doc-tests should represent good sage usage and I think both of those are better than the first (certainly the \"3\" is unnecessary and obnoxious -- I suspect it's only recently that the 3 wasn't required.).  I think there is some room for personal opinion here -- perhaps some mixture is also good to let people see alternate styles as well.",
    "created_at": "2008-03-28T18:50:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2702#issuecomment-18594",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```

Attachment [mpoly_coverage_100.patch](tarball://root/attachments/some-uuid/ticket2702/mpoly_coverage_100.patch) by jbmohler created at 2008-03-28 18:50:14

This is a positive review about the patch, but it's a big patch and could use another set of eyes, I expect.  I think it looks like it cleans up a lot of evolved changes to make the whole thing more cohesive.  I did not apply and doc-test (because I don't have a recent 2.11.alphaX build).

Two specific comments:
* 1) I think the documentation of is_monomial should be very clear that 2*x is not monomial (with a sentence in the initial header).  This is not my intuitive definition of monomial, but it's a sane definition.  I would prefer that 2*x be a monomial, but it's not a big deal.
* 2)  I see a number of lines like

```
sage: Q.<x,y,z>=MPolynomialRing(QQ,3)
```

I think they should be one of the following:

```
sage: Q.<x,y,z>=PolynomialRing(QQ)
sage: Q.<x,y,z>=QQ[]
```

William has made the comment that doc-tests should represent good sage usage and I think both of those are better than the first (certainly the "3" is unnecessary and obnoxious -- I suspect it's only recently that the 3 wasn't required.).  I think there is some room for personal opinion here -- perhaps some mixture is also good to let people see alternate styles as well.



---

archive/issue_comments_018595.json:
```json
{
    "body": "Replying to [comment:1 jbmohler]:\n> Two specific comments:\n>  * 1) I think the documentation of is_monomial should be very clear that 2*x is not monomial (with a sentence in the initial header).  This is not my intuitive definition of monomial, but it's a sane definition.  I would prefer that 2*x be a monomial, but it's not a big deal.\n\nI'll add that to the docstring.\n\n>  * 2)  I see a number of lines like\n> {{{\n> sage: Q.<x,y,z>=MPolynomialRing(QQ,3)\n> }}}\n> I think they should be one of the following:\n> {{{\n> sage: Q.<x,y,z>=PolynomialRing(QQ)\n> sage: Q.<x,y,z>=QQ[]\n> }}}\n\nIt is still not clear what will happen to `MPolynomialRing` and `PolynomialRing`, but I'll remove the unnecessary \"3\".",
    "created_at": "2008-03-28T19:23:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2702#issuecomment-18595",
    "user": "https://github.com/malb"
}
```

Replying to [comment:1 jbmohler]:
> Two specific comments:
>  * 1) I think the documentation of is_monomial should be very clear that 2*x is not monomial (with a sentence in the initial header).  This is not my intuitive definition of monomial, but it's a sane definition.  I would prefer that 2*x be a monomial, but it's not a big deal.

I'll add that to the docstring.

>  * 2)  I see a number of lines like
> {{{
> sage: Q.<x,y,z>=MPolynomialRing(QQ,3)
> }}}
> I think they should be one of the following:
> {{{
> sage: Q.<x,y,z>=PolynomialRing(QQ)
> sage: Q.<x,y,z>=QQ[]
> }}}

It is still not clear what will happen to `MPolynomialRing` and `PolynomialRing`, but I'll remove the unnecessary "3".



---

archive/issue_comments_018596.json:
```json
{
    "body": "Replying to [comment:2 malb]:\n> Replying to [comment:1 jbmohler]:\n> > Two specific comments:\n> >  * 1) I think the documentation of is_monomial should be very clear that 2*x is not monomial (with a sentence in the initial header).  This is not my intuitive definition of monomial, but it's a sane definition.  I would prefer that 2*x be a monomial, but it's not a big deal.\n> \n> I'll add that to the docstring.\n\nUpon more checking, I noticed that MPolynomial_polydict takes the differing convention.  They certainly should be consistent -- I don't care which way.",
    "created_at": "2008-03-28T22:37:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2702#issuecomment-18596",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```

Replying to [comment:2 malb]:
> Replying to [comment:1 jbmohler]:
> > Two specific comments:
> >  * 1) I think the documentation of is_monomial should be very clear that 2*x is not monomial (with a sentence in the initial header).  This is not my intuitive definition of monomial, but it's a sane definition.  I would prefer that 2*x be a monomial, but it's not a big deal.
> 
> I'll add that to the docstring.

Upon more checking, I noticed that MPolynomial_polydict takes the differing convention.  They certainly should be consistent -- I don't care which way.



---

archive/issue_comments_018597.json:
```json
{
    "body": "malb, I'm reviewing the patch too and taking care of these issues.",
    "created_at": "2008-03-29T08:12:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2702#issuecomment-18597",
    "user": "https://github.com/mwhansen"
}
```

malb, I'm reviewing the patch too and taking care of these issues.



---

archive/issue_comments_018598.json:
```json
{
    "body": "I changed many of the doctests to use a more \"modern\" style for constructing the polynomial rings.  I also changed is_monomial to treat 2*x as a monomial since it agrees with _polydict and matches the standard mathematical definition for a monomial.\n\nApply the last two patches.  They apply to 2.11 alpha1 and pass -testall",
    "created_at": "2008-03-29T08:44:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2702#issuecomment-18598",
    "user": "https://github.com/mwhansen"
}
```

I changed many of the doctests to use a more "modern" style for constructing the polynomial rings.  I also changed is_monomial to treat 2*x as a monomial since it agrees with _polydict and matches the standard mathematical definition for a monomial.

Apply the last two patches.  They apply to 2.11 alpha1 and pass -testall



---

archive/issue_comments_018599.json:
```json
{
    "body": "Replying to [comment:5 mhansen]:\n> I changed many of the doctests to use a more \"modern\" style for constructing the polynomial rings.  \n\nmhansen, thanks for taking car of this!\n\n> I also changed is_monomial to treat 2*x as a monomial since it agrees with \n> _polydict and matches the standard mathematical definition for a monomial.\n\nPlease don't!\n* there is no standard mathematical definition for a monomial. If **t = 2xy** Cox, Little, O'Shea call **xy** a monomial and **2xy** a term in \"Ideals, Varieties, and Algorithms\". Becker and Weispfennig call **xy** the term and **2xy** the monomial in \"Gr\u00f6bner Bases\".\n* Singular is inconsistent: `lead` returns the leading term and means **2yx**, `leadmonom` returns **yx** but they define a monomial as\n\n```\n[coefficient] ring_variable [ exponent] [ring_variable [exponent] ...]\n```\n\n* Magma has **yx** == monomial too: \"A monomial (or power product) of P is a product of powers of the variables (or indeterminates) of P, that is, an expression of the form x1> ... xn> with ei \u22650 for 1 \u2264i \u2264n. Multivariate polynomials in Magma are stored efficiently in distributive form, using arrays of coefficient-monomial pairs, where the coefficient is in the base ring R. The word `term' will always refer to a coefficient multiplied by a monomial.\"\n* Sage is (or should be) strict so far: `lm()` returns **xy** and not **2yx**\n\n\n> Apply the last two patches.  They apply to 2.11 alpha1 and pass -testall",
    "created_at": "2008-03-29T11:39:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2702#issuecomment-18599",
    "user": "https://github.com/malb"
}
```

Replying to [comment:5 mhansen]:
> I changed many of the doctests to use a more "modern" style for constructing the polynomial rings.  

mhansen, thanks for taking car of this!

> I also changed is_monomial to treat 2*x as a monomial since it agrees with 
> _polydict and matches the standard mathematical definition for a monomial.

Please don't!
* there is no standard mathematical definition for a monomial. If **t = 2xy** Cox, Little, O'Shea call **xy** a monomial and **2xy** a term in "Ideals, Varieties, and Algorithms". Becker and Weispfennig call **xy** the term and **2xy** the monomial in "Gröbner Bases".
* Singular is inconsistent: `lead` returns the leading term and means **2yx**, `leadmonom` returns **yx** but they define a monomial as

```
[coefficient] ring_variable [ exponent] [ring_variable [exponent] ...]
```

* Magma has **yx** == monomial too: "A monomial (or power product) of P is a product of powers of the variables (or indeterminates) of P, that is, an expression of the form x1> ... xn> with ei ≥0 for 1 ≤i ≤n. Multivariate polynomials in Magma are stored efficiently in distributive form, using arrays of coefficient-monomial pairs, where the coefficient is in the base ring R. The word `term' will always refer to a coefficient multiplied by a monomial."
* Sage is (or should be) strict so far: `lm()` returns **xy** and not **2yx**


> Apply the last two patches.  They apply to 2.11 alpha1 and pass -testall



---

archive/issue_comments_018600.json:
```json
{
    "body": "I've updated 2702-referee.patch to use the old definition of monomial, added an extra docstest, and a sentence in the docstring describing what it's using for the definition of monomial.\n\n\nThis should probably be taken to sage-devel.\n\n\nI'm fine with the last two patches being applied.",
    "created_at": "2008-03-29T19:50:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2702#issuecomment-18600",
    "user": "https://github.com/mwhansen"
}
```

I've updated 2702-referee.patch to use the old definition of monomial, added an extra docstest, and a sentence in the docstring describing what it's using for the definition of monomial.


This should probably be taken to sage-devel.


I'm fine with the last two patches being applied.



---

archive/issue_comments_018601.json:
```json
{
    "body": "Attachment [2702.patch](tarball://root/attachments/some-uuid/ticket2702/2702.patch) by @mwhansen created at 2008-03-29 20:28:13",
    "created_at": "2008-03-29T20:28:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2702#issuecomment-18601",
    "user": "https://github.com/mwhansen"
}
```

Attachment [2702.patch](tarball://root/attachments/some-uuid/ticket2702/2702.patch) by @mwhansen created at 2008-03-29 20:28:13



---

archive/issue_comments_018602.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-29T20:30:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2702#issuecomment-18602",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_018603.json:
```json
{
    "body": "Attachment [2702-referee.patch](tarball://root/attachments/some-uuid/ticket2702/2702-referee.patch) by mabshoff created at 2008-03-29 20:30:46\n\nMerged 2702.patch and 2702-referee.patch in Sage 2.11.rc0",
    "created_at": "2008-03-29T20:30:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2702#issuecomment-18603",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [2702-referee.patch](tarball://root/attachments/some-uuid/ticket2702/2702-referee.patch) by mabshoff created at 2008-03-29 20:30:46

Merged 2702.patch and 2702-referee.patch in Sage 2.11.rc0
