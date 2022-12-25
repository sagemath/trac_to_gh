# Issue 8499: improve documentation of partial_fraction_decomposition

archive/issues_008499.json:
```json
{
    "body": "Assignee: @burcin\n\nHow can one compute a partial fraction decomposition over the\ncomplex numbers? Consider the following:\n\n```\nsage: x = PolynomialRing(RationalField(), 'x').gen()\nsage: r = 1 /(x^4 + 1)\nsage: r.partial_fraction_decomposition()\n(0, [1/(x^4 + 1)])\n```\nThis is ok since we explicitely work over QQ. Now compare with:\n\n```\nsage: P.<y> = PolynomialRing(RationalField())\nsage: Qbar.<y> = QuotientRing(P, y^2+1)\nsage: x = PolynomialRing(Qbar, 'x').gen()\nsage: r = 1 /(x^4 + 1)\nsage: r.partial_fraction_decomposition()\n---------------------------------------------------------------------------\nNotImplementedError                       Traceback (most recent call last)\n```\n\n\n**apply** [attachment:trac_8499.patch]\n\nIssue created by migration from https://trac.sagemath.org/ticket/8499\n\n",
    "closed_at": "2014-02-07T00:50:02Z",
    "created_at": "2010-03-11T16:55:05Z",
    "labels": [
        "component: calculus"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.2",
    "title": "improve documentation of partial_fraction_decomposition",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8499",
    "user": "https://github.com/zimmermann6"
}
```
Assignee: @burcin

How can one compute a partial fraction decomposition over the
complex numbers? Consider the following:

```
sage: x = PolynomialRing(RationalField(), 'x').gen()
sage: r = 1 /(x^4 + 1)
sage: r.partial_fraction_decomposition()
(0, [1/(x^4 + 1)])
```
This is ok since we explicitely work over QQ. Now compare with:

```
sage: P.<y> = PolynomialRing(RationalField())
sage: Qbar.<y> = QuotientRing(P, y^2+1)
sage: x = PolynomialRing(Qbar, 'x').gen()
sage: r = 1 /(x^4 + 1)
sage: r.partial_fraction_decomposition()
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)
```


**apply** [attachment:trac_8499.patch]

Issue created by migration from https://trac.sagemath.org/ticket/8499





---

archive/issue_events_020404.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8499",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8499#event-20404"
}
```



---

archive/issue_comments_076596.json:
```json
{
    "body": "I found out the solution by myself. If one wants say a decomposition over Q[sqrt(2)] or Q[I], then simply use `QQ[sqrt(2)]` or `QQ[sqrt(-1)]`:\n\n```\nsage: R.<x> = QQ[sqrt(2)][]\nsage: r=1/(x^4+1)\nsage: r.partial_fraction_decomposition()\n(0,\n [(-1/4*sqrt2*x + 1/2)/(x^2 - sqrt2*x + 1),\n  (1/4*sqrt2*x + 1/2)/(x^2 + sqrt2*x + 1)])\n```\nor:\n\n```\nsage: R.<x> = QQ[sqrt(-1)][]            \nsage: r=1/(x^4+1)                       \nsage: r.partial_fraction_decomposition()\n(0, [(-1/2*I)/(x^2 - I), 1/2*I/(x^2 + I)])\n```\nNow if you want Sage to automatically find the extension where the denominator fully factors, use\n`QQbar`:\n\n```\nsage: R.<x> = QQbar[]                   \nsage: r=1/(x^4+1)                       \nsage: r.partial_fraction_decomposition()\n(0,\n [([-0.17677669529663690 .. -0.17677669529663686] - [0.17677669529663686 .. 0.17677669529663690]*I)/(x + [-0.70710678118654758 .. -0.70710678118654746] - [0.70710678118654746 .. 0.70710678118654758]*I),\n  ([-0.17677669529663690 .. -0.17677669529663686] + [0.17677669529663686 .. 0.17677669529663690]*I)/(x + [-0.70710678118654758 .. -0.70710678118654746] + [0.70710678118654746 .. 0.70710678118654758]*I),\n  ([0.17677669529663686 .. 0.17677669529663690] - [0.17677669529663686 .. 0.17677669529663690]*I)/(x + [0.70710678118654746 .. 0.70710678118654758] - [0.70710678118654746 .. 0.70710678118654758]*I),\n  ([0.17677669529663686 .. 0.17677669529663690] + [0.17677669529663686 .. 0.17677669529663690]*I)/(x + [0.70710678118654746 .. 0.70710678118654758] + [0.70710678118654746 .. 0.70710678118654758]*I)])\n```\nI'll add some examples to the documentation and then we can close this ticket.\n\nPaul",
    "created_at": "2013-08-24T08:41:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8499#issuecomment-76596",
    "user": "https://github.com/zimmermann6"
}
```

I found out the solution by myself. If one wants say a decomposition over Q[sqrt(2)] or Q[I], then simply use `QQ[sqrt(2)]` or `QQ[sqrt(-1)]`:

```
sage: R.<x> = QQ[sqrt(2)][]
sage: r=1/(x^4+1)
sage: r.partial_fraction_decomposition()
(0,
 [(-1/4*sqrt2*x + 1/2)/(x^2 - sqrt2*x + 1),
  (1/4*sqrt2*x + 1/2)/(x^2 + sqrt2*x + 1)])
```
or:

```
sage: R.<x> = QQ[sqrt(-1)][]            
sage: r=1/(x^4+1)                       
sage: r.partial_fraction_decomposition()
(0, [(-1/2*I)/(x^2 - I), 1/2*I/(x^2 + I)])
```
Now if you want Sage to automatically find the extension where the denominator fully factors, use
`QQbar`:

```
sage: R.<x> = QQbar[]                   
sage: r=1/(x^4+1)                       
sage: r.partial_fraction_decomposition()
(0,
 [([-0.17677669529663690 .. -0.17677669529663686] - [0.17677669529663686 .. 0.17677669529663690]*I)/(x + [-0.70710678118654758 .. -0.70710678118654746] - [0.70710678118654746 .. 0.70710678118654758]*I),
  ([-0.17677669529663690 .. -0.17677669529663686] + [0.17677669529663686 .. 0.17677669529663690]*I)/(x + [-0.70710678118654758 .. -0.70710678118654746] + [0.70710678118654746 .. 0.70710678118654758]*I),
  ([0.17677669529663686 .. 0.17677669529663690] - [0.17677669529663686 .. 0.17677669529663690]*I)/(x + [0.70710678118654746 .. 0.70710678118654758] - [0.70710678118654746 .. 0.70710678118654758]*I),
  ([0.17677669529663686 .. 0.17677669529663690] + [0.17677669529663686 .. 0.17677669529663690]*I)/(x + [0.70710678118654746 .. 0.70710678118654758] + [0.70710678118654746 .. 0.70710678118654758]*I)])
```
I'll add some examples to the documentation and then we can close this ticket.

Paul



---

archive/issue_comments_076597.json:
```json
{
    "body": "Attachment [trac_8499.patch](tarball://root/attachments/some-uuid/ticket8499/trac_8499.patch) by @zimmermann6 created at 2013-08-24 11:55:32",
    "created_at": "2013-08-24T11:55:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8499#issuecomment-76597",
    "user": "https://github.com/zimmermann6"
}
```

Attachment [trac_8499.patch](tarball://root/attachments/some-uuid/ticket8499/trac_8499.patch) by @zimmermann6 created at 2013-08-24 11:55:32



---

archive/issue_comments_076598.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-08-24T11:59:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8499#issuecomment-76598",
    "user": "https://github.com/zimmermann6"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_076599.json:
```json
{
    "body": "I've changed the ticket summary, and attached a patch (against Sage 5.9) which improves the documentation of `partial_fraction_decomposition`.\n\nPaul",
    "created_at": "2013-08-24T11:59:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8499#issuecomment-76599",
    "user": "https://github.com/zimmermann6"
}
```

I've changed the ticket summary, and attached a patch (against Sage 5.9) which improves the documentation of `partial_fraction_decomposition`.

Paul



---

archive/issue_comments_076600.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2013-08-24T12:00:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8499#issuecomment-76600",
    "user": "https://github.com/zimmermann6"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_076601.json:
```json
{
    "body": "Looks good, but I have a question. How is computing the rational fraction decomposition over QQbar gives you the extension where the denominator splits? It just returns the full decomposition over QQbar no more no less. The extension would be in any case the splitting field of the denominator, isn't it?\n\nI would expect something like \"Now if you want Sage to compute an extension where the denominator fully factors, use QQbar: \"",
    "created_at": "2013-12-21T12:35:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8499#issuecomment-76601",
    "user": "https://github.com/lftabera"
}
```

Looks good, but I have a question. How is computing the rational fraction decomposition over QQbar gives you the extension where the denominator splits? It just returns the full decomposition over QQbar no more no less. The extension would be in any case the splitting field of the denominator, isn't it?

I would expect something like "Now if you want Sage to compute an extension where the denominator fully factors, use QQbar: "



---

archive/issue_comments_076602.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2013-12-21T12:35:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8499#issuecomment-76602",
    "user": "https://github.com/lftabera"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_076603.json:
```json
{
    "body": "thank you for your feedback. You have two questions in fact:\n\n> How is computing the rational fraction decomposition over QQbar gives you the extension where the denominator splits?\n\n\nthis is given in the denominators of the output.\n\n> The extension would be in any case the splitting field of the denominator, isn't it? \n\n\nyes.\n\nFeel free to propose a reviewer patch!\n\nPaul",
    "created_at": "2013-12-21T12:51:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8499#issuecomment-76603",
    "user": "https://github.com/zimmermann6"
}
```

thank you for your feedback. You have two questions in fact:

> How is computing the rational fraction decomposition over QQbar gives you the extension where the denominator splits?


this is given in the denominators of the output.

> The extension would be in any case the splitting field of the denominator, isn't it? 


yes.

Feel free to propose a reviewer patch!

Paul



---

archive/issue_events_020405.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8499",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8499#event-20405"
}
```



---

archive/issue_events_020406.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8499",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8499#event-20406"
}
```



---

archive/issue_comments_076604.json:
```json
{
    "body": "My complain is that using QQbar does not give you the splitting field of the denominator in an obvious way. I have changed the documentation accordingly. Paul, could you take a look at my changes and check if you agree with them?\n\nLuis",
    "created_at": "2014-01-31T16:02:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8499#issuecomment-76604",
    "user": "https://github.com/lftabera"
}
```

My complain is that using QQbar does not give you the splitting field of the denominator in an obvious way. I have changed the documentation accordingly. Paul, could you take a look at my changes and check if you agree with them?

Luis



---

archive/issue_comments_076605.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2014-01-31T16:02:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8499#issuecomment-76605",
    "user": "https://github.com/lftabera"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_076606.json:
```json
{
    "body": "I get an error when I try this example:\n\n```\nsage: R.<x> = QQ[]\nsage: r = 1/(x^4+2)\nsage: N = r.denominator().splitting_field('a')\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n<ipython-input-9-c9d534f911a3> in <module>()\n----> 1 N = r.denominator().splitting_field('a')\n\n/usr/local/sage-6.0-x86_64-Linux/local/lib/python2.7/site-packages/sage/structure/element.so in sage.structure.element.Element.__getattr__ (sage/structure/element.c:3873)()\n\n/usr/local/sage-6.0-x86_64-Linux/local/lib/python2.7/site-packages/sage/structure/misc.so in sage.structure.misc.getattr_from_other_class (sage/structure/misc.c:1696)()\n\nAttributeError: 'sage.rings.polynomial.polynomial_rational_flint.Polynomial_rational_flint' object has no attribute 'splitting_field'\n```",
    "created_at": "2014-01-31T16:20:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8499#issuecomment-76606",
    "user": "https://github.com/zimmermann6"
}
```

I get an error when I try this example:

```
sage: R.<x> = QQ[]
sage: r = 1/(x^4+2)
sage: N = r.denominator().splitting_field('a')
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-9-c9d534f911a3> in <module>()
----> 1 N = r.denominator().splitting_field('a')

/usr/local/sage-6.0-x86_64-Linux/local/lib/python2.7/site-packages/sage/structure/element.so in sage.structure.element.Element.__getattr__ (sage/structure/element.c:3873)()

/usr/local/sage-6.0-x86_64-Linux/local/lib/python2.7/site-packages/sage/structure/misc.so in sage.structure.misc.getattr_from_other_class (sage/structure/misc.c:1696)()

AttributeError: 'sage.rings.polynomial.polynomial_rational_flint.Polynomial_rational_flint' object has no attribute 'splitting_field'
```



---

archive/issue_comments_076607.json:
```json
{
    "body": "Sorry for not telling, you need sage 6.1 released today...",
    "created_at": "2014-01-31T16:23:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8499#issuecomment-76607",
    "user": "https://github.com/lftabera"
}
```

Sorry for not telling, you need sage 6.1 released today...



---

archive/issue_comments_076608.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-02-04T20:59:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8499#issuecomment-76608",
    "user": "https://github.com/zimmermann6"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076609.json:
```json
{
    "body": "I tried the added examples with Sage 6.1 and they work, thus positive review for me.",
    "created_at": "2014-02-04T20:59:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8499#issuecomment-76609",
    "user": "https://github.com/zimmermann6"
}
```

I tried the added examples with Sage 6.1 and they work, thus positive review for me.



---

archive/issue_events_020407.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2014-02-07T00:50:02Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8499",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8499#event-20407"
}
```



---

archive/issue_comments_076610.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-02-07T00:50:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8499#issuecomment-76610",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
