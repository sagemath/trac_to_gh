# Issue 9480: Sage mixes Infinity and +Infinity

archive/issues_009480.json:
```json
{
    "body": "Assignee: burcin\n\nThis is related to #8942. The limit function can output either\n`+Infinity`, `-Infinity`, or `Infinity`, the later\nmeaning a complex infinity. For example:\n\n```\nsage: limit(1/x, x=0, dir='above')\n+Infinity\nsage: limit(1/x, x=0, dir='below')\n-Infinity\nsage: limit(1/x, x=0)             \nInfinity\n```\n\nHowever Sage does not distinguish `+Infinity` and `Infinity`:\n\n```\nsage: l1=limit(1/x, x=0, dir='above')\nsage: l2=limit(1/x, x=0, dir='below')\nsage: l3=limit(1/x, x=0)\nsage: l1==l3\nTrue\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9480\n\n",
    "created_at": "2010-07-12T12:48:51Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "title": "Sage mixes Infinity and +Infinity",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9480",
    "user": "zimmerma"
}
```
Assignee: burcin

This is related to #8942. The limit function can output either
`+Infinity`, `-Infinity`, or `Infinity`, the later
meaning a complex infinity. For example:

```
sage: limit(1/x, x=0, dir='above')
+Infinity
sage: limit(1/x, x=0, dir='below')
-Infinity
sage: limit(1/x, x=0)             
Infinity
```

However Sage does not distinguish `+Infinity` and `Infinity`:

```
sage: l1=limit(1/x, x=0, dir='above')
sage: l2=limit(1/x, x=0, dir='below')
sage: l3=limit(1/x, x=0)
sage: l1==l3
True
```


Issue created by migration from https://trac.sagemath.org/ticket/9480





---

archive/issue_comments_091007.json:
```json
{
    "body": "This is more of a problem with the equality checking rules in Sage and the coercion system than symbolics, so I'm changing the component to coercion.\n\nIf the arguments compare equal when coerced to a common parent, Sage returns `True` for the equality. In this case, the coercion goes to the `UnsignedInfinityRing`, where `+Infinity` is mapped to `unsigned_infinity`.\n\n\n```\nsage: UnsignedInfinityRing.has_coerce_map_from(InfinityRing)\nTrue\nsage: Infinity\n+Infinity\nsage: UnsignedInfinityRing.coerce(Infinity)\nInfinity\n```\n\n\nBTW, isn't there an inconsistency in the capitalization of `Infinity`. Shouldn't it be lowercase according to Python conventions?",
    "created_at": "2010-08-29T10:54:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9480",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9480#issuecomment-91007",
    "user": "burcin"
}
```

This is more of a problem with the equality checking rules in Sage and the coercion system than symbolics, so I'm changing the component to coercion.

If the arguments compare equal when coerced to a common parent, Sage returns `True` for the equality. In this case, the coercion goes to the `UnsignedInfinityRing`, where `+Infinity` is mapped to `unsigned_infinity`.


```
sage: UnsignedInfinityRing.has_coerce_map_from(InfinityRing)
True
sage: Infinity
+Infinity
sage: UnsignedInfinityRing.coerce(Infinity)
Infinity
```


BTW, isn't there an inconsistency in the capitalization of `Infinity`. Shouldn't it be lowercase according to Python conventions?



---

archive/issue_comments_091008.json:
```json
{
    "body": "Changing assignee from burcin to robertwb.",
    "created_at": "2010-08-29T10:54:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9480",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9480#issuecomment-91008",
    "user": "burcin"
}
```

Changing assignee from burcin to robertwb.



---

archive/issue_comments_091009.json:
```json
{
    "body": "Changing keywords from \"\" to \"infinity, equality\".",
    "created_at": "2010-08-29T10:54:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9480",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9480#issuecomment-91009",
    "user": "burcin"
}
```

Changing keywords from "" to "infinity, equality".



---

archive/issue_comments_091010.json:
```json
{
    "body": "Changing component from calculus to coercion.",
    "created_at": "2010-08-29T10:54:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9480",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9480#issuecomment-91010",
    "user": "burcin"
}
```

Changing component from calculus to coercion.



---

archive/issue_comments_091011.json:
```json
{
    "body": "Sometimes it's `infinity` and others its `Infinity`. At the very least this should be consistent. Also there are other issues with infinity: #11506 #9547.",
    "created_at": "2012-05-11T13:39:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9480",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9480#issuecomment-91011",
    "user": "tscrim"
}
```

Sometimes it's `infinity` and others its `Infinity`. At the very least this should be consistent. Also there are other issues with infinity: #11506 #9547.



---

archive/issue_comments_091012.json:
```json
{
    "body": "in Sage 5.11 we get:\n\n```\nsage: l1=limit(1/x, x=0, dir='right'); l1\n+Infinity\nsage: l2=limit(1/x, x=0, dir='left'); l2 \n-Infinity\nsage: l3=limit(1/x, x=0); l3             \nInfinity\nsage: bool(l1==l2), bool(l2==l3), bool(l3==l1)\n(False, False, False)\n```\n\nhowever the objects returned are in SR and not in the `infinity` class:\n\n```\nsage: type(l1), l1.parent()\n(sage.symbolic.expression.Expression, Symbolic Ring)\nsage: p1=+Infinity\nsage: type(p1), p1.parent()\n(sage.rings.infinity.PlusInfinity, The Infinity Ring)\n```\n\nI propose to close that ticket, and open a new one about the above issue (or add it to an existing ticket).\n\nPaul",
    "created_at": "2013-08-25T13:45:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9480",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9480#issuecomment-91012",
    "user": "zimmerma"
}
```

in Sage 5.11 we get:

```
sage: l1=limit(1/x, x=0, dir='right'); l1
+Infinity
sage: l2=limit(1/x, x=0, dir='left'); l2 
-Infinity
sage: l3=limit(1/x, x=0); l3             
Infinity
sage: bool(l1==l2), bool(l2==l3), bool(l3==l1)
(False, False, False)
```

however the objects returned are in SR and not in the `infinity` class:

```
sage: type(l1), l1.parent()
(sage.symbolic.expression.Expression, Symbolic Ring)
sage: p1=+Infinity
sage: type(p1), p1.parent()
(sage.rings.infinity.PlusInfinity, The Infinity Ring)
```

I propose to close that ticket, and open a new one about the above issue (or add it to an existing ticket).

Paul



---

archive/issue_comments_091013.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-08-25T13:45:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9480",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9480#issuecomment-91013",
    "user": "zimmerma"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_091014.json:
```json
{
    "body": "> or add it to an existing ticket\n\nI've added a comment in #14857\n\nPaul",
    "created_at": "2013-08-25T13:59:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9480",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9480#issuecomment-91014",
    "user": "zimmerma"
}
```

> or add it to an existing ticket

I've added a comment in #14857

Paul



---

archive/issue_comments_091015.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2013-12-26T19:26:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9480",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9480#issuecomment-91015",
    "user": "ncohen"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_091016.json:
```json
{
    "body": "No patch to review on this ticket...\n\nPaul : when you want to close a ticket, you should set its milestone to wontfix/duplicate, say why on a comment, and change the status to `positive_review` so that the release manager will see it.\n\nNathann",
    "created_at": "2013-12-26T19:26:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9480",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9480#issuecomment-91016",
    "user": "ncohen"
}
```

No patch to review on this ticket...

Paul : when you want to close a ticket, you should set its milestone to wontfix/duplicate, say why on a comment, and change the status to `positive_review` so that the release manager will see it.

Nathann



---

archive/issue_comments_091017.json:
```json
{
    "body": "in Sage 6.0 we get:\n\n```\nsage: l1=limit(1/x, x=0, dir='above')\nsage: l3=limit(1/x, x=0)\nsage: bool(l1==l3)\nFalse\n```\n\nthus the issue is fixed now, and I change the status to \"fixed\".\n\nPaul",
    "created_at": "2014-01-03T09:36:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9480",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9480#issuecomment-91017",
    "user": "zimmerma"
}
```

in Sage 6.0 we get:

```
sage: l1=limit(1/x, x=0, dir='above')
sage: l3=limit(1/x, x=0)
sage: bool(l1==l3)
False
```

thus the issue is fixed now, and I change the status to "fixed".

Paul



---

archive/issue_comments_091018.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-01-03T09:36:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9480",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9480#issuecomment-91018",
    "user": "zimmerma"
}
```

Resolution: fixed



---

archive/issue_comments_091019.json:
```json
{
    "body": "sorry when changing to \"fixed\" (which made more sense to me than invalid or wontfix) the status was changed automatically to \"closed\"...\n\nPaul",
    "created_at": "2014-01-03T09:38:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9480",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9480#issuecomment-91019",
    "user": "zimmerma"
}
```

sorry when changing to "fixed" (which made more sense to me than invalid or wontfix) the status was changed automatically to "closed"...

Paul



---

archive/issue_comments_091020.json:
```json
{
    "body": "I also verified that it works in `6.1.beta2`.",
    "created_at": "2014-01-03T15:09:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9480",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9480#issuecomment-91020",
    "user": "tscrim"
}
```

I also verified that it works in `6.1.beta2`.
