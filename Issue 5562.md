# Issue 5562: coercion error with vectors and polynomial rings with 1 variable

archive/issues_005562.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @robertwb\n\nKeywords: coercion vector polynomial ring\n\nThis is strange: it matters how many variables are specified.  This fails and I think this is a bug:\n\n```\nsage: R.<u> = PolynomialRing(RDF, 1, 'u')\nsage: v1 = vector([u])\nsage: v2 = vector([CDF(2)])\nsage: v1 * v2\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/ncalexan/sage-3.4.rc0-sage.math-only-x86_64-Linux/devel/sage/sage/functions/riemann_theta.py in <module>()\n\n/home/ncalexan/sage-3.4.rc0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.el\\\nement.Vector.__mul__ (sage/structure/element.c:10435)()\n\n/home/ncalexan/sage-3.4.rc0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/coerce.so in sage.structure.coe\\\nrce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:5847)()\n\nTypeError: unsupported operand parent(s) for '*': 'Ambient free module of rank 1 over the integral domain Multivariate Polynomial Ring i\\\nn u over Real Double Field' and 'Vector space of dimension 1 over Complex Double Field'\n```\n\nBut both of these succeed:\n\n```\nsage: R.<u, v> = RDF[]\nsage: v1 = vector([u])\nsage: v2 = vector([CDF(2)])\nsage: v1 * v2\n2.0*u\n```\n\n```\nsage: R.<u> = RDF[]\nsage: v1 = vector([u])\nsage: v2 = vector([CDF(2)])\nsage: v1 * v2\n2.0*u\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/5562\n\n",
    "closed_at": "2013-01-31T09:18:52Z",
    "created_at": "2009-03-18T23:00:00Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.7",
    "title": "coercion error with vectors and polynomial rings with 1 variable",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5562",
    "user": "https://github.com/ncalexan"
}
```
Assignee: @williamstein

CC:  @robertwb

Keywords: coercion vector polynomial ring

This is strange: it matters how many variables are specified.  This fails and I think this is a bug:

```
sage: R.<u> = PolynomialRing(RDF, 1, 'u')
sage: v1 = vector([u])
sage: v2 = vector([CDF(2)])
sage: v1 * v2
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/ncalexan/sage-3.4.rc0-sage.math-only-x86_64-Linux/devel/sage/sage/functions/riemann_theta.py in <module>()

/home/ncalexan/sage-3.4.rc0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.el\
ement.Vector.__mul__ (sage/structure/element.c:10435)()

/home/ncalexan/sage-3.4.rc0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/coerce.so in sage.structure.coe\
rce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:5847)()

TypeError: unsupported operand parent(s) for '*': 'Ambient free module of rank 1 over the integral domain Multivariate Polynomial Ring i\
n u over Real Double Field' and 'Vector space of dimension 1 over Complex Double Field'
```

But both of these succeed:

```
sage: R.<u, v> = RDF[]
sage: v1 = vector([u])
sage: v2 = vector([CDF(2)])
sage: v1 * v2
2.0*u
```

```
sage: R.<u> = RDF[]
sage: v1 = vector([u])
sage: v2 = vector([CDF(2)])
sage: v1 * v2
2.0*u
```

Issue created by migration from https://trac.sagemath.org/ticket/5562





---

archive/issue_comments_043203.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-12-10T21:22:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5562",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5562#issuecomment-43203",
    "user": "https://github.com/tscrim"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_043204.json:
```json
{
    "body": "This seems to be fixed in `5.5.rc0`\n\n```\nsage: R.<u> = PolynomialRing(RDF, 1, 'u')\nsage: v1 = vector([u])\nsage: v2 = vector([CDF(2)])\nsage: v1 * v2\n2.0*u\n```",
    "created_at": "2012-12-10T21:22:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5562",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5562#issuecomment-43204",
    "user": "https://github.com/tscrim"
}
```

This seems to be fixed in `5.5.rc0`

```
sage: R.<u> = PolynomialRing(RDF, 1, 'u')
sage: v1 = vector([u])
sage: v2 = vector([CDF(2)])
sage: v1 * v2
2.0*u
```



---

archive/issue_events_013083.json:
```json
{
    "actor": "https://github.com/tscrim",
    "created_at": "2012-12-10T21:22:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5562",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5562#event-13083"
}
```



---

archive/issue_comments_043205.json:
```json
{
    "body": "I've attached a patch that adds a doctest that makes sure this keeps working.\n\nThe patch also removes plenty of trailing whitespace in the affected file. I got this for free by putting \n\n```\n(add-hook 'before-save-hook 'delete-trailing-whitespace)\n```\ninto my \"`.emacs.rc`\".\n\nBut maybe it might have been better to just give the \"wontfix\" a positive review instead...",
    "created_at": "2013-01-26T14:54:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5562",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5562#issuecomment-43205",
    "user": "https://github.com/cnassau"
}
```

I've attached a patch that adds a doctest that makes sure this keeps working.

The patch also removes plenty of trailing whitespace in the affected file. I got this for free by putting 

```
(add-hook 'before-save-hook 'delete-trailing-whitespace)
```
into my "`.emacs.rc`".

But maybe it might have been better to just give the "wontfix" a positive review instead...



---

archive/issue_events_013084.json:
```json
{
    "actor": "https://github.com/tscrim",
    "created_at": "2013-01-28T17:46:16Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5562",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5562#event-13084"
}
```



---

archive/issue_events_013085.json:
```json
{
    "actor": "https://github.com/tscrim",
    "created_at": "2013-01-28T17:46:16Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5562",
    "milestone": "sage-5.7",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5562#event-13085"
}
```



---

archive/issue_comments_043206.json:
```json
{
    "body": "Hey,\n\nFor doctest formatting, I would change:\n\n```\n    sage: # check that #5562 has been fixed\n    sage: R.<u> = PolynomialRing(RDF, 1, 'u')\n...\n```\nto\n\n```\nCheck that :trac:`5562` has been fixed::\n\n    sage: R.<u> = PolynomialRing(RDF, 1, 'u')\n...\n```\n\nI think the trailing whitespace removal should be okay...\n\nBest,\n\nTravis",
    "created_at": "2013-01-28T17:46:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5562",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5562#issuecomment-43206",
    "user": "https://github.com/tscrim"
}
```

Hey,

For doctest formatting, I would change:

```
    sage: # check that #5562 has been fixed
    sage: R.<u> = PolynomialRing(RDF, 1, 'u')
...
```
to

```
Check that :trac:`5562` has been fixed::

    sage: R.<u> = PolynomialRing(RDF, 1, 'u')
...
```

I think the trailing whitespace removal should be okay...

Best,

Travis



---

archive/issue_comments_043207.json:
```json
{
    "body": "Hi Travis,\n\nI agree, in theory, that the doctest should be reformatted. However, I don't know how to do this because the patch has apparently already been merged in 5.7.beta1. Would I create a new patch based on beta1, or edit the old one?\n\nCheers,\nChristian",
    "created_at": "2013-01-29T17:26:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5562",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5562#issuecomment-43207",
    "user": "https://github.com/cnassau"
}
```

Hi Travis,

I agree, in theory, that the doctest should be reformatted. However, I don't know how to do this because the patch has apparently already been merged in 5.7.beta1. Would I create a new patch based on beta1, or edit the old one?

Cheers,
Christian



---

archive/issue_comments_043208.json:
```json
{
    "body": "This won't be merged until it's positively reviewed and closed, it's just the target that was changed. You can create a new patch or edit the old, whichever makes it clearer what your changes were.",
    "created_at": "2013-01-29T17:46:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5562",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5562#issuecomment-43208",
    "user": "https://github.com/robertwb"
}
```

This won't be merged until it's positively reviewed and closed, it's just the target that was changed. You can create a new patch or edit the old, whichever makes it clearer what your changes were.



---

archive/issue_comments_043209.json:
```json
{
    "body": "Attachment [5562.patch](tarball://root/attachments/some-uuid/ticket5562/5562.patch) by @cnassau created at 2013-01-29 18:07:43",
    "created_at": "2013-01-29T18:07:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5562",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5562#issuecomment-43209",
    "user": "https://github.com/cnassau"
}
```

Attachment [5562.patch](tarball://root/attachments/some-uuid/ticket5562/5562.patch) by @cnassau created at 2013-01-29 18:07:43



---

archive/issue_comments_043210.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-01-29T18:10:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5562",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5562#issuecomment-43210",
    "user": "https://github.com/tscrim"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_043211.json:
```json
{
    "body": "Looks good to me. Thanks Christian.",
    "created_at": "2013-01-29T18:10:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5562",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5562#issuecomment-43211",
    "user": "https://github.com/tscrim"
}
```

Looks good to me. Thanks Christian.



---

archive/issue_comments_043212.json:
```json
{
    "body": "Replying to [comment:6 tscrim]:\n> Looks good to me. Thanks Christian.\n\n\nIndeed, my working copy had been garbled, presumably by running \"hg import\" earlier when I meant \"hg qimport\" which made me believe that this ticket had somehow magically be merged already... anyway, glad we got rid of this now ;-)\n\nCheers,\nChristian",
    "created_at": "2013-01-29T18:12:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5562",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5562#issuecomment-43212",
    "user": "https://github.com/cnassau"
}
```

Replying to [comment:6 tscrim]:
> Looks good to me. Thanks Christian.


Indeed, my working copy had been garbled, presumably by running "hg import" earlier when I meant "hg qimport" which made me believe that this ticket had somehow magically be merged already... anyway, glad we got rid of this now ;-)

Cheers,
Christian



---

archive/issue_events_013086.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-01-31T09:18:52Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5562",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5562#event-13086"
}
```



---

archive/issue_comments_043213.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-01-31T09:18:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5562",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5562#issuecomment-43213",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
