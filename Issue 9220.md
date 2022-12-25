# Issue 9220: Upredictable parent for polynomial evaluation

archive/issues_009220.json:
```json
{
    "body": "Assignee: @robertwb\n\nI doubt that it is intended that the names of the variables of a polynomial ring can affect the parent of the result of evaluating such a polynomial:\n\n\n```\nsage: R=QQ['x']\nsage: S=QQ['x','y']\nsage: h=S.0^2\nsage: parent(h(R.0,0))\nMultivariate Polynomial Ring in x, y over Rational Field\n\nsage: R=QQ['x']\nsage: S=QQ['u','v']\nsage: h=S.0^2\nsage: parent(h(R.0,0))\nUnivariate Polynomial Ring in x over Rational Field \n```\n\nI would expect the result of the second example in both cases.\n\nIn\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/4607f62126303ddd?pli=1\n\nJohn Cremona mentions #8502 as fixing a different but similar issue.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9220\n\n",
    "created_at": "2010-06-11T21:06:02Z",
    "labels": [
        "component: coercion",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.7",
    "title": "Upredictable parent for polynomial evaluation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9220",
    "user": "https://github.com/nbruin"
}
```
Assignee: @robertwb

I doubt that it is intended that the names of the variables of a polynomial ring can affect the parent of the result of evaluating such a polynomial:


```
sage: R=QQ['x']
sage: S=QQ['x','y']
sage: h=S.0^2
sage: parent(h(R.0,0))
Multivariate Polynomial Ring in x, y over Rational Field

sage: R=QQ['x']
sage: S=QQ['u','v']
sage: h=S.0^2
sage: parent(h(R.0,0))
Univariate Polynomial Ring in x over Rational Field 
```

I would expect the result of the second example in both cases.

In

http://groups.google.com/group/sage-devel/browse_thread/thread/4607f62126303ddd?pli=1

John Cremona mentions #8502 as fixing a different but similar issue.

Issue created by migration from https://trac.sagemath.org/ticket/9220





---

archive/issue_comments_086254.json:
```json
{
    "body": "I agree, the result should only be a function of the base ring and evaluation argument parents.",
    "created_at": "2010-06-11T23:43:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9220#issuecomment-86254",
    "user": "https://github.com/robertwb"
}
```

I agree, the result should only be a function of the base ring and evaluation argument parents.



---

archive/issue_comments_086255.json:
```json
{
    "body": "I think I've found the culprit in:\n\n```\nbuilt-in method __call__ of sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular\n```\n\nIndeed, it tries to coerce the evaluation values into the polynomial ring. Perhaps it should try to coerce into the base ring of the parent instead?\n\n```\n        if l != parent._ring.N:\n            raise TypeError, \"number of arguments does not match number of variables in parent\"\n\n        try:\n            x = [parent._coerce_c(e) for e in x]\n        except TypeError:\n            # give up, evaluate functional\n            y = parent.base_ring()(0)\n            for (m,c) in self.dict().iteritems():\n                y += c*mul([ x[i]**m[i] for i in m.nonzero_positions()])\n            return y\n\n```\n\nIf I were to fix this code, I'd simply always do the code under the \"except\", but someone probably had a good reason for doing it the way it's done. Probably because `singular_polynomial_call` is more efficient? I see several options:\n\n* Ask the coercion system for a common overring of the base ring of parent and all the parents of x. If that is parent, then coerce and use singular_polynomial_call. Otherwise just multiply out manually.\n\n* see if the parent of all members of x is equal to parent (due to the lax coercion rules, *coercible into* isn't good enough)\n\n* just always evaluate by multiplying out\n\nThe first one is the \"proper\" one in that it uses the coercion system to figure out if a more efficient option is available. The second option should be cheap and catch the case where most speed-up should be attainable. The third option wouldn't waste any time on checking parents, but would need coercion calls for each coefficient-monomial multiplication.",
    "created_at": "2010-06-14T18:36:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9220#issuecomment-86255",
    "user": "https://github.com/nbruin"
}
```

I think I've found the culprit in:

```
built-in method __call__ of sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular
```

Indeed, it tries to coerce the evaluation values into the polynomial ring. Perhaps it should try to coerce into the base ring of the parent instead?

```
        if l != parent._ring.N:
            raise TypeError, "number of arguments does not match number of variables in parent"

        try:
            x = [parent._coerce_c(e) for e in x]
        except TypeError:
            # give up, evaluate functional
            y = parent.base_ring()(0)
            for (m,c) in self.dict().iteritems():
                y += c*mul([ x[i]**m[i] for i in m.nonzero_positions()])
            return y

```

If I were to fix this code, I'd simply always do the code under the "except", but someone probably had a good reason for doing it the way it's done. Probably because `singular_polynomial_call` is more efficient? I see several options:

* Ask the coercion system for a common overring of the base ring of parent and all the parents of x. If that is parent, then coerce and use singular_polynomial_call. Otherwise just multiply out manually.

* see if the parent of all members of x is equal to parent (due to the lax coercion rules, *coercible into* isn't good enough)

* just always evaluate by multiplying out

The first one is the "proper" one in that it uses the coercion system to figure out if a more efficient option is available. The second option should be cheap and catch the case where most speed-up should be attainable. The third option wouldn't waste any time on checking parents, but would need coercion calls for each coefficient-monomial multiplication.



---

archive/issue_comments_086256.json:
```json
{
    "body": "Indeed the present code does seem to address real overhead:\n\n```\nsage: R=QQ['x']\nsage: S=QQ['x','y']\nsage: h=S.0^2\nsage: timeit('h(R.0,0)')\n625 loops, best of 3: 269 \u00b5s per loop\n```\n\nbut\n\n```\nsage: R=QQ['x']\nsage: S=QQ['u','v']\nsage: h=S.0^2\nsage: timeit('h(R.0,0)')\n625 loops, best of 3: 523 \u00b5s per loop\n```\n\nso option one or two above is probably the proper one.",
    "created_at": "2010-06-14T18:41:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9220#issuecomment-86256",
    "user": "https://github.com/nbruin"
}
```

Indeed the present code does seem to address real overhead:

```
sage: R=QQ['x']
sage: S=QQ['x','y']
sage: h=S.0^2
sage: timeit('h(R.0,0)')
625 loops, best of 3: 269 µs per loop
```

but

```
sage: R=QQ['x']
sage: S=QQ['u','v']
sage: h=S.0^2
sage: timeit('h(R.0,0)')
625 loops, best of 3: 523 µs per loop
```

so option one or two above is probably the proper one.



---

archive/issue_comments_086257.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-14T19:47:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9220#issuecomment-86257",
    "user": "https://github.com/nbruin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_086258.json:
```json
{
    "body": "Attached patch is efficient when evaluation point has the same parent. I guess previously some efficiency was gained when a point was in the base ring as well (the result was subsequently recognised as a constant and coerced back?) by used libsingular evaluation directly. This is lost with attached patch. This probably means that this patch solves #8502 independently as well.\n\nTo reviewer or merger: feel free to change patch. I won't be touching the code anymore.",
    "created_at": "2010-06-14T19:51:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9220#issuecomment-86258",
    "user": "https://github.com/nbruin"
}
```

Attached patch is efficient when evaluation point has the same parent. I guess previously some efficiency was gained when a point was in the base ring as well (the result was subsequently recognised as a constant and coerced back?) by used libsingular evaluation directly. This is lost with attached patch. This probably means that this patch solves #8502 independently as well.

To reviewer or merger: feel free to change patch. I won't be touching the code anymore.



---

archive/issue_comments_086259.json:
```json
{
    "body": "Attachment [9220-poly-evaluation-coerce.patch](tarball://root/attachments/some-uuid/ticket9220/9220-poly-evaluation-coerce.patch) by @robertwb created at 2010-06-22 23:43:58\n\nadd instead of previous",
    "created_at": "2010-06-22T23:43:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9220#issuecomment-86259",
    "user": "https://github.com/robertwb"
}
```

Attachment [9220-poly-evaluation-coerce.patch](tarball://root/attachments/some-uuid/ticket9220/9220-poly-evaluation-coerce.patch) by @robertwb created at 2010-06-22 23:43:58

add instead of previous



---

archive/issue_comments_086260.json:
```json
{
    "body": "I've attached a patch that returns the correct parent without sacrificing the singular efficiency (together with a utility method in the coercion model to make this kind of thing easier elsewhere).",
    "created_at": "2010-06-22T23:45:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9220#issuecomment-86260",
    "user": "https://github.com/robertwb"
}
```

I've attached a patch that returns the correct parent without sacrificing the singular efficiency (together with a utility method in the coercion model to make this kind of thing easier elsewhere).



---

archive/issue_comments_086261.json:
```json
{
    "body": "Apply only 9220-poly-evaluation-coerce.patch",
    "created_at": "2011-01-26T06:31:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9220#issuecomment-86261",
    "user": "https://github.com/robertwb"
}
```

Apply only 9220-poly-evaluation-coerce.patch



---

archive/issue_comments_086262.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-03-20T02:26:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9220#issuecomment-86262",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_086263.json:
```json
{
    "body": "Works with 4.7.1.",
    "created_at": "2012-03-20T02:26:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9220#issuecomment-86263",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Works with 4.7.1.



---

archive/issue_comments_086264.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-03-29T14:44:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9220#issuecomment-86264",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_086265.json:
```json
{
    "body": "Needs to be rebased to sage-5.0.beta11:\n\n```\napplying 9220-poly-evaluation-coerce.patch\npatching file sage/rings/polynomial/multi_polynomial_libsingular.pyx\nHunk #2 succeeded at 4512 with fuzz 2 (offset 2764 lines).\nHunk #4 FAILED at 1785\n1 out of 4 hunks FAILED -- saving rejects to file sage/rings/polynomial/multi_polynomial_libsingular.pyx.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nerrors during apply, please fix and refresh 9220-poly-evaluation-coerce.patch\n```\n",
    "created_at": "2012-03-29T14:44:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9220#issuecomment-86265",
    "user": "https://github.com/jdemeyer"
}
```

Needs to be rebased to sage-5.0.beta11:

```
applying 9220-poly-evaluation-coerce.patch
patching file sage/rings/polynomial/multi_polynomial_libsingular.pyx
Hunk #2 succeeded at 4512 with fuzz 2 (offset 2764 lines).
Hunk #4 FAILED at 1785
1 out of 4 hunks FAILED -- saving rejects to file sage/rings/polynomial/multi_polynomial_libsingular.pyx.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh 9220-poly-evaluation-coerce.patch
```




---

archive/issue_comments_086266.json:
```json
{
    "body": "Attachment [9220-poly-evaluation-coerce-5.4.rebase.patch](tarball://root/attachments/some-uuid/ticket9220/9220-poly-evaluation-coerce-5.4.rebase.patch) by @robertwb created at 2012-10-24 07:01:35\n\nRebased on sage-5.4.rc2, apply only this patch.",
    "created_at": "2012-10-24T07:01:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9220#issuecomment-86266",
    "user": "https://github.com/robertwb"
}
```

Attachment [9220-poly-evaluation-coerce-5.4.rebase.patch](tarball://root/attachments/some-uuid/ticket9220/9220-poly-evaluation-coerce-5.4.rebase.patch) by @robertwb created at 2012-10-24 07:01:35

Rebased on sage-5.4.rc2, apply only this patch.



---

archive/issue_comments_086267.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-10-24T07:02:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9220#issuecomment-86267",
    "user": "https://github.com/robertwb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_086268.json:
```json
{
    "body": "Some docstring things:\n- Please use auto-trac linking `:trac:`9220``\n- For `common_parent()`, I would recommend:\n\n```\nComputes a common parent for all the inputs.\n\nThis is essentially an `n`-ary canonical coercion except it\ncan operate on parents rather than just elements. \n\nINPUT: \n\n- ``args`` -- a set of elements and/or parents\n\nOUTPUT: \n\nA :class:`Parent` into which each input should coerce, or raises a \n``TypeError`` if no such :class:`Parent` can be found. \n```\n\n  In particular, there is should not be an indent on the `INPUT:` and `OUTPUT:` blocks.\n\nThanks, \n\nTravis",
    "created_at": "2012-10-27T22:57:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9220#issuecomment-86268",
    "user": "https://github.com/tscrim"
}
```

Some docstring things:
- Please use auto-trac linking `:trac:`9220``
- For `common_parent()`, I would recommend:

```
Computes a common parent for all the inputs.

This is essentially an `n`-ary canonical coercion except it
can operate on parents rather than just elements. 

INPUT: 

- ``args`` -- a set of elements and/or parents

OUTPUT: 

A :class:`Parent` into which each input should coerce, or raises a 
``TypeError`` if no such :class:`Parent` can be found. 
```

  In particular, there is should not be an indent on the `INPUT:` and `OUTPUT:` blocks.

Thanks, 

Travis



---

archive/issue_comments_086269.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-11-26T06:28:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9220#issuecomment-86269",
    "user": "https://github.com/tscrim"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_086270.json:
```json
{
    "body": "Attachment [13933-doctests.patch](tarball://root/attachments/some-uuid/ticket9220/13933-doctests.patch) by @robertwb created at 2013-01-22 05:24:15\n\nminor docstring fixes",
    "created_at": "2013-01-22T05:24:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9220#issuecomment-86270",
    "user": "https://github.com/robertwb"
}
```

Attachment [13933-doctests.patch](tarball://root/attachments/some-uuid/ticket9220/13933-doctests.patch) by @robertwb created at 2013-01-22 05:24:15

minor docstring fixes



---

archive/issue_comments_086271.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-01-22T05:24:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9220#issuecomment-86271",
    "user": "https://github.com/robertwb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_086272.json:
```json
{
    "body": "Minor fixes to docstrings",
    "created_at": "2013-01-31T17:03:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9220#issuecomment-86272",
    "user": "https://github.com/tscrim"
}
```

Minor fixes to docstrings



---

archive/issue_comments_086273.json:
```json
{
    "body": "Attachment [trac_9220-poly_evaluation-review-ts.patch](tarball://root/attachments/some-uuid/ticket9220/trac_9220-poly_evaluation-review-ts.patch) by @tscrim created at 2013-01-31 17:12:04\n\nThe rebased version worked for me. I've attached a small reviewer patch which just does the minor tweaks to the docstrings. Jeroen, I hope you don't mind me setting this back to a positive review.\n\nBest,\n\nTravis\n\nFor patchbot:\n\nApply only: 9220-poly-evaluation-coerce-5.4.rebase.patch, trac_9220-poly_evaluation-review-ts.patch",
    "created_at": "2013-01-31T17:12:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9220#issuecomment-86273",
    "user": "https://github.com/tscrim"
}
```

Attachment [trac_9220-poly_evaluation-review-ts.patch](tarball://root/attachments/some-uuid/ticket9220/trac_9220-poly_evaluation-review-ts.patch) by @tscrim created at 2013-01-31 17:12:04

The rebased version worked for me. I've attached a small reviewer patch which just does the minor tweaks to the docstrings. Jeroen, I hope you don't mind me setting this back to a positive review.

Best,

Travis

For patchbot:

Apply only: 9220-poly-evaluation-coerce-5.4.rebase.patch, trac_9220-poly_evaluation-review-ts.patch



---

archive/issue_comments_086274.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-01-31T17:12:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9220#issuecomment-86274",
    "user": "https://github.com/tscrim"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_086275.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-02-05T08:17:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9220#issuecomment-86275",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
