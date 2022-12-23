# Issue 8240: cannot coerce p-adic field into residue field

archive/issues_008240.json:
```json
{
    "body": "Assignee: roed\n\nCC:  roed robertwb saraedum caruso kedlaya\n\n\n```\nsage: K.<a> = Qq(25)\nsage: F = K.residue_field()\nsage: F(a)\nTraceback (click to the left of this block for traceback)\n...\nTypeError: unable to coerce\n```\n\n\nPerhaps this is a \"feature request\", but it seems like a pretty basic feature...\n\n(It works fine for prime fields)\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8240\n\n",
    "created_at": "2010-02-11T19:51:59Z",
    "labels": [
        "padics",
        "major",
        "bug"
    ],
    "title": "cannot coerce p-adic field into residue field",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8240",
    "user": "dmharvey"
}
```
Assignee: roed

CC:  roed robertwb saraedum caruso kedlaya


```
sage: K.<a> = Qq(25)
sage: F = K.residue_field()
sage: F(a)
Traceback (click to the left of this block for traceback)
...
TypeError: unable to coerce
```


Perhaps this is a "feature request", but it seems like a pretty basic feature...

(It works fine for prime fields)


Issue created by migration from https://trac.sagemath.org/ticket/8240





---

archive/issue_comments_072807.json:
```json
{
    "body": "Attachment\n\npadic base coercion",
    "created_at": "2012-02-21T01:37:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8240#issuecomment-72807",
    "user": "roed"
}
```

Attachment

padic base coercion



---

archive/issue_comments_072808.json:
```json
{
    "body": "Attachment\n\ncoercion for extensions, part 1",
    "created_at": "2012-02-21T01:40:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8240#issuecomment-72808",
    "user": "roed"
}
```

Attachment

coercion for extensions, part 1



---

archive/issue_comments_072809.json:
```json
{
    "body": "Attachment\n\ncoercion for extensions, part 2",
    "created_at": "2012-02-21T01:41:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8240#issuecomment-72809",
    "user": "roed"
}
```

Attachment

coercion for extensions, part 2



---

archive/issue_comments_072810.json:
```json
{
    "body": "I've updated the dependencies.  If you care about this ticket, review them!\n\nNote that the 8240.patch is a duplicate of #12077 and should be removed.  8240_ext1.patch and 8240_ext2.patch are in progress: I basically didn't finish writing them.  Feel free to add to these patches in the same vein as #12077.",
    "created_at": "2012-02-21T12:51:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8240#issuecomment-72810",
    "user": "roed"
}
```

I've updated the dependencies.  If you care about this ticket, review them!

Note that the 8240.patch is a duplicate of #12077 and should be removed.  8240_ext1.patch and 8240_ext2.patch are in progress: I basically didn't finish writing them.  Feel free to add to these patches in the same vein as #12077.



---

archive/issue_comments_072811.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-07-23T09:10:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8240#issuecomment-72811",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_072812.json:
```json
{
    "body": "Last 10 new commits:",
    "created_at": "2017-07-23T09:11:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8240#issuecomment-72812",
    "user": "roed"
}
```

Last 10 new commits:



---

archive/issue_comments_072813.json:
```json
{
    "body": "\n```\nsage -t --warn-long 53.3 src/sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py  # 27 doctests failed\nsage -t --warn-long 53.3 src/sage/modular/btquotients/pautomorphicform.py  # 24 doctests failed\nsage -t --warn-long 53.3 src/sage/schemes/elliptic_curves/padics.py  # 1 doctest failed\nsage -t --warn-long 53.3 src/sage/modular/btquotients/btquotient.py  # 4 doctests failed\nsage -t --warn-long 53.3 src/sage/schemes/hyperelliptic_curves/monsky_washnitzer.py  # 4 doctests failed\n```\n",
    "created_at": "2017-07-23T09:17:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8240#issuecomment-72813",
    "user": "roed"
}
```


```
sage -t --warn-long 53.3 src/sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py  # 27 doctests failed
sage -t --warn-long 53.3 src/sage/modular/btquotients/pautomorphicform.py  # 24 doctests failed
sage -t --warn-long 53.3 src/sage/schemes/elliptic_curves/padics.py  # 1 doctest failed
sage -t --warn-long 53.3 src/sage/modular/btquotients/btquotient.py  # 4 doctests failed
sage -t --warn-long 53.3 src/sage/schemes/hyperelliptic_curves/monsky_washnitzer.py  # 4 doctests failed
```




---

archive/issue_comments_072814.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-08-03T22:14:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8240#issuecomment-72814",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_072815.json:
```json
{
    "body": "So, there are a number of failures coming from following change\n\n```\nsage: R = Zp(5); S = Zmod(5^5)\nsage: a = R(1, 3); a\n1 + O(5^3)\nsage: S(a)\nTraceback (most recent call last):\n...\nPrecisionError: Not enough precision to determine reduction.\n```\n\nPreviously, Sage performed this reduction without complaint.  Some questions:\n* Do we want a coercion from `R` to `S`?  Mathematically, this coercion is very similar to the one from `ZZ` to `Zmod(N)`, so I think the answer is yes.\n* If there is a coercion, what should its behavior be on elements without enough precision, as in the example above?  A `PrecisionError` seems reasonable, but normally coercions don't raise errors....\n* The coercion model demands that if there is a coercion between two parents, then that morphism should be used as the conversion as well (this is implemented in `discover_convert_map`, which calls `_internal_coerce_map_from` as the first step).  So we can't have different behavior for the coercion and the conversion from `R` to `S`.\n* It's pretty annoying to have these kind of `PrecisionError`s in conversions.  For example, conversions are used in `change_ring` on polynomials, and there are plenty of examples in the Sage library where `change_ring` that trigger this kind of `PrecisionError`.\n\nAny suggestions?",
    "created_at": "2017-08-04T07:21:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8240#issuecomment-72815",
    "user": "roed"
}
```

So, there are a number of failures coming from following change

```
sage: R = Zp(5); S = Zmod(5^5)
sage: a = R(1, 3); a
1 + O(5^3)
sage: S(a)
Traceback (most recent call last):
...
PrecisionError: Not enough precision to determine reduction.
```

Previously, Sage performed this reduction without complaint.  Some questions:
* Do we want a coercion from `R` to `S`?  Mathematically, this coercion is very similar to the one from `ZZ` to `Zmod(N)`, so I think the answer is yes.
* If there is a coercion, what should its behavior be on elements without enough precision, as in the example above?  A `PrecisionError` seems reasonable, but normally coercions don't raise errors....
* The coercion model demands that if there is a coercion between two parents, then that morphism should be used as the conversion as well (this is implemented in `discover_convert_map`, which calls `_internal_coerce_map_from` as the first step).  So we can't have different behavior for the coercion and the conversion from `R` to `S`.
* It's pretty annoying to have these kind of `PrecisionError`s in conversions.  For example, conversions are used in `change_ring` on polynomials, and there are plenty of examples in the Sage library where `change_ring` that trigger this kind of `PrecisionError`.

Any suggestions?



---

archive/issue_comments_072816.json:
```json
{
    "body": "I just checked the following:\n\n```\nsage: R1 = RealIntervalField(10)\nsage: C1 = ComplexIntervalField(10)\nsage: C1.coerce_map_from(R1)\n\nCall morphism:\n  From: Real Interval Field with 10 bits of precision\n  To:   Complex Interval Field with 10 bits of precision\nsage: C1 = ComplexIntervalField(11)\nsage: C1.coerce_map_from(R1)\nsage: C1.convert_map_from(R1)\n\nCall morphism:\n  From: Real Interval Field with 10 bits of precision\n  To:   Complex Interval Field with 11 bits of precision\n```\n\nSo, there's a precedent in the archimedean code to only have a convert map, not a coerce map, when mapping from a lower precision to a higher precision. For Zp(5) to Zmod(5<sup>5</sup>), you're mapping an inexact ring to an exact ring, so this would suggest that there should be no coercion, only a conversion.",
    "created_at": "2017-08-04T07:54:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8240#issuecomment-72816",
    "user": "robharron"
}
```

I just checked the following:

```
sage: R1 = RealIntervalField(10)
sage: C1 = ComplexIntervalField(10)
sage: C1.coerce_map_from(R1)

Call morphism:
  From: Real Interval Field with 10 bits of precision
  To:   Complex Interval Field with 10 bits of precision
sage: C1 = ComplexIntervalField(11)
sage: C1.coerce_map_from(R1)
sage: C1.convert_map_from(R1)

Call morphism:
  From: Real Interval Field with 10 bits of precision
  To:   Complex Interval Field with 11 bits of precision
```

So, there's a precedent in the archimedean code to only have a convert map, not a coerce map, when mapping from a lower precision to a higher precision. For Zp(5) to Zmod(5<sup>5</sup>), you're mapping an inexact ring to an exact ring, so this would suggest that there should be no coercion, only a conversion.



---

archive/issue_comments_072817.json:
```json
{
    "body": "Yeah, just having a conversion seems like the simplest solution.  I think it may be reasonable to have a coercion to the residue field though?",
    "created_at": "2017-08-05T02:37:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8240#issuecomment-72817",
    "user": "roed"
}
```

Yeah, just having a conversion seems like the simplest solution.  I think it may be reasonable to have a coercion to the residue field though?



---

archive/issue_comments_072818.json:
```json
{
    "body": "Replying to [comment:10 roed]:\n> Yeah, just having a conversion seems like the simplest solution.  I think it may be reasonable to have a coercion to the residue field though?\n\nYeah, I think coercion to the residue field makes sense, though a PrecisionError will still need to be raised for O(5<sup>0</sup>); I think that's reasonable since O(5<sup>0</sup>) basically means you have no idea what element of Zp you have!",
    "created_at": "2017-08-05T02:43:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8240#issuecomment-72818",
    "user": "robharron"
}
```

Replying to [comment:10 roed]:
> Yeah, just having a conversion seems like the simplest solution.  I think it may be reasonable to have a coercion to the residue field though?

Yeah, I think coercion to the residue field makes sense, though a PrecisionError will still need to be raised for O(5<sup>0</sup>); I think that's reasonable since O(5<sup>0</sup>) basically means you have no idea what element of Zp you have!



---

archive/issue_comments_072819.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-08-05T07:31:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8240#issuecomment-72819",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_072820.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2017-08-05T07:42:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8240#issuecomment-72820",
    "user": "roed"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_072821.json:
```json
{
    "body": "IMO, It's a kinda weird to promote reduction modulo p to a coercion map but not reduction modulo p^n.",
    "created_at": "2017-08-05T12:30:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8240#issuecomment-72821",
    "user": "caruso"
}
```

IMO, It's a kinda weird to promote reduction modulo p to a coercion map but not reduction modulo p^n.



---

archive/issue_comments_072822.json:
```json
{
    "body": "Replying to [comment:14 caruso]:\n> IMO, It's a kinda weird to promote reduction modulo p to a coercion map but not reduction modulo p^n.\n\nI agree that it's kind of weird.  I'd really like for them both to be coercions, but I explain above why that doesn't seem to be possible.\n\nI think it's probably okay to also delete the coercion to the residue field.  For integers, you really want to be able to ask for `a+1` if `a` is an element of `Zmod(N)`, but I think that this is a lot less important for p-adics.\n\nIf nobody else has input, I can go ahead and make this change.",
    "created_at": "2017-08-06T05:46:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8240#issuecomment-72822",
    "user": "roed"
}
```

Replying to [comment:14 caruso]:
> IMO, It's a kinda weird to promote reduction modulo p to a coercion map but not reduction modulo p^n.

I agree that it's kind of weird.  I'd really like for them both to be coercions, but I explain above why that doesn't seem to be possible.

I think it's probably okay to also delete the coercion to the residue field.  For integers, you really want to be able to ask for `a+1` if `a` is an element of `Zmod(N)`, but I think that this is a lot less important for p-adics.

If nobody else has input, I can go ahead and make this change.



---

archive/issue_comments_072823.json:
```json
{
    "body": "Replying to [comment:14 caruso]:\n> IMO, It's a kinda weird to promote reduction modulo p to a coercion map but not reduction modulo p^n.\n\nI agree that it's kind of weird.  I'd really like for them both to be coercions, but I explain above why that doesn't seem to be possible.\n\nI think it's probably okay to also delete the coercion to the residue field.  For integers, you really want to be able to ask for `a+1` if `a` is an element of `Zmod(N)`, but I think that this is a lot less important for p-adics.",
    "created_at": "2017-08-06T05:49:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8240#issuecomment-72823",
    "user": "roed"
}
```

Replying to [comment:14 caruso]:
> IMO, It's a kinda weird to promote reduction modulo p to a coercion map but not reduction modulo p^n.

I agree that it's kind of weird.  I'd really like for them both to be coercions, but I explain above why that doesn't seem to be possible.

I think it's probably okay to also delete the coercion to the residue field.  For integers, you really want to be able to ask for `a+1` if `a` is an element of `Zmod(N)`, but I think that this is a lot less important for p-adics.



---

archive/issue_comments_072824.json:
```json
{
    "body": "Can we try to live with a conversion? if that raise problems we cna try to make all maps coercions.\nBut as David said, there is a precendent with other constructions in sagE.",
    "created_at": "2017-08-21T16:44:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8240#issuecomment-72824",
    "user": "jpflori"
}
```

Can we try to live with a conversion? if that raise problems we cna try to make all maps coercions.
But as David said, there is a precendent with other constructions in sagE.



---

archive/issue_comments_072825.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-09-20T17:12:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8240#issuecomment-72825",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_072826.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. Last 10 new commits:",
    "created_at": "2017-09-20T18:52:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8240#issuecomment-72826",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. Last 10 new commits:



---

archive/issue_comments_072827.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-09-20T20:31:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8240#issuecomment-72827",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_072828.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-09-20T20:36:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8240#issuecomment-72828",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_072829.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-09-20T20:48:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8240#issuecomment-72829",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_072830.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-09-20T21:57:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8240#issuecomment-72830",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_072831.json:
```json
{
    "body": "Attachment\n\nDiff against #14825 for ease of review",
    "created_at": "2017-09-20T21:59:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8240#issuecomment-72831",
    "user": "roed"
}
```

Attachment

Diff against #14825 for ease of review



---

archive/issue_comments_072832.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-09-22T19:40:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8240#issuecomment-72832",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_072833.json:
```json
{
    "body": "I'm getting an error from the docbuild plugin:\n\n```\nOSError: [padics   ] ...docstring of sage.rings.padics.padic_generic.pAdicGeneric.residue_ring:1: WARNING: Inline interpreted text or phrase reference start-string without end-string.\n```\n\nThe relevant docstring is\n\n```\n    \"\"\"\n    Return the quotient of the ring of integers by the nth power of its maximal ideal.\n\n    EXAMPLES::\n\n        sage: S.<x> = ZZ[]\n \tsage: W.<w> = Zp(5).extension(x^2 - 5)\n \tsage: W.residue_ring(1)\n \tRing of integers modulo 5\n\n    The following requires implementing more general Artinian rings::\n\n \tsage: W.residue_ring(2)\n \tTraceback (most recent call last):\n \t...\n \tNotImplementedError\n    \"\"\"\n```\n\n\nAny ideas what might be going on?",
    "created_at": "2017-09-23T18:32:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8240#issuecomment-72833",
    "user": "roed"
}
```

I'm getting an error from the docbuild plugin:

```
OSError: [padics   ] ...docstring of sage.rings.padics.padic_generic.pAdicGeneric.residue_ring:1: WARNING: Inline interpreted text or phrase reference start-string without end-string.
```

The relevant docstring is

```
    """
    Return the quotient of the ring of integers by the nth power of its maximal ideal.

    EXAMPLES::

        sage: S.<x> = ZZ[]
 	sage: W.<w> = Zp(5).extension(x^2 - 5)
 	sage: W.residue_ring(1)
 	Ring of integers modulo 5

    The following requires implementing more general Artinian rings::

 	sage: W.residue_ring(2)
 	Traceback (most recent call last):
 	...
 	NotImplementedError
    """
```


Any ideas what might be going on?



---

archive/issue_comments_072834.json:
```json
{
    "body": "in\n`Returns the quotient of the ring of integers by the `n`th power of the maximal ideal.`\nadd a space after ``n``",
    "created_at": "2017-09-23T18:40:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8240#issuecomment-72834",
    "user": "chapoton"
}
```

in
`Returns the quotient of the ring of integers by the `n`th power of the maximal ideal.`
add a space after ``n``



---

archive/issue_comments_072835.json:
```json
{
    "body": "in\n\n```\nrichcmp((type(self), self.domain(), self.codomain()), (type(other), other.domain(), other.codomain()), op)\n```\n\nyou compare types, which is not allowed in python3.\n\n**EDIT**\nInstead you can do something like\n\n```\nif type(self) != type(other):\n    return NotImplemented\nreturn richcmp(...)\n```\n",
    "created_at": "2017-09-23T18:44:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8240#issuecomment-72835",
    "user": "chapoton"
}
```

in

```
richcmp((type(self), self.domain(), self.codomain()), (type(other), other.domain(), other.codomain()), op)
```

you compare types, which is not allowed in python3.

**EDIT**
Instead you can do something like

```
if type(self) != type(other):
    return NotImplemented
return richcmp(...)
```




---

archive/issue_comments_072836.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-09-23T19:08:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8240#issuecomment-72836",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_072837.json:
```json
{
    "body": "Thanks; I've fixed the richcmp error you pointed out.",
    "created_at": "2017-09-24T02:33:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8240#issuecomment-72837",
    "user": "roed"
}
```

Thanks; I've fixed the richcmp error you pointed out.



---

archive/issue_comments_072838.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-09-24T02:45:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8240#issuecomment-72838",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_072839.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-09-25T06:50:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8240#issuecomment-72839",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_072840.json:
```json
{
    "body": "Tests pass.",
    "created_at": "2017-09-25T19:29:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8240#issuecomment-72840",
    "user": "roed"
}
```

Tests pass.



---

archive/issue_comments_072841.json:
```json
{
    "body": "I confess to not having inspected all of this code line-by-line. But I did go through the main blocks, and I tried a few tests of my own without finding any issues. Positive review.",
    "created_at": "2017-09-26T02:26:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8240#issuecomment-72841",
    "user": "kedlaya"
}
```

I confess to not having inspected all of this code line-by-line. But I did go through the main blocks, and I tried a few tests of my own without finding any issues. Positive review.



---

archive/issue_comments_072842.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2017-09-26T02:26:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8240#issuecomment-72842",
    "user": "kedlaya"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072843.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2017-10-09T20:04:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8240#issuecomment-72843",
    "user": "vbraun"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_072844.json:
```json
{
    "body": "Merge conflict",
    "created_at": "2017-10-09T20:04:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8240#issuecomment-72844",
    "user": "vbraun"
}
```

Merge conflict



---

archive/issue_comments_072845.json:
```json
{
    "body": "No conflicts for me.\n----\nNew commits:",
    "created_at": "2017-10-13T05:54:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8240#issuecomment-72845",
    "user": "saraedum"
}
```

No conflicts for me.
----
New commits:



---

archive/issue_comments_072846.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2017-10-13T05:54:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8240#issuecomment-72846",
    "user": "saraedum"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_072847.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2017-10-15T15:29:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8240#issuecomment-72847",
    "user": "vbraun"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_072848.json:
```json
{
    "body": "wait for next beta",
    "created_at": "2017-10-15T15:29:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8240#issuecomment-72848",
    "user": "vbraun"
}
```

wait for next beta



---

archive/issue_comments_072849.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2017-10-18T20:16:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8240#issuecomment-72849",
    "user": "roed"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_072850.json:
```json
{
    "body": "Fixed the merge conflict and ran all tests.\n----\nNew commits:",
    "created_at": "2017-10-18T20:16:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8240#issuecomment-72850",
    "user": "roed"
}
```

Fixed the merge conflict and ran all tests.
----
New commits:



---

archive/issue_comments_072851.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2017-10-20T09:15:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8240#issuecomment-72851",
    "user": "vbraun"
}
```

Resolution: fixed
