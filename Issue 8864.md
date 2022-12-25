# Issue 8864: make zeta function symbolic

archive/issues_008864.json:
```json
{
    "body": "Assignee: @aghitza\n\nConsider:\n\n```\nsage: zeta(3)\n1.20205690315959\n```\nWe expect `zeta(3)` as answer.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8864\n\n",
    "created_at": "2010-05-03T20:58:14Z",
    "labels": [
        "component: basic arithmetic"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "make zeta function symbolic",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8864",
    "user": "https://github.com/zimmermann6"
}
```
Assignee: @aghitza

Consider:

```
sage: zeta(3)
1.20205690315959
```
We expect `zeta(3)` as answer.

Issue created by migration from https://trac.sagemath.org/ticket/8864





---

archive/issue_comments_081322.json:
```json
{
    "body": "Note: this is a followup of #7748.",
    "created_at": "2010-05-03T21:00:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8864#issuecomment-81322",
    "user": "https://github.com/zimmermann6"
}
```

Note: this is a followup of #7748.



---

archive/issue_comments_081323.json:
```json
{
    "body": "Attachment [trac_8864-symbolic_zeta.patch](tarball://root/attachments/some-uuid/ticket8864/trac_8864-symbolic_zeta.patch) by @burcin created at 2010-05-06 20:01:38\n\nWith attachment:trac_8864-symbolic_zeta.patch you can do this:\n\n```\nsage: zeta(3)\nzeta(3)\nsage: zeta(2)\n1/6*pi^2\n```\n\nProbably, the changes to `sage/symbolic/random_tests.py` depend on #6949.",
    "created_at": "2010-05-06T20:01:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8864#issuecomment-81323",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_8864-symbolic_zeta.patch](tarball://root/attachments/some-uuid/ticket8864/trac_8864-symbolic_zeta.patch) by @burcin created at 2010-05-06 20:01:38

With attachment:trac_8864-symbolic_zeta.patch you can do this:

```
sage: zeta(3)
zeta(3)
sage: zeta(2)
1/6*pi^2
```

Probably, the changes to `sage/symbolic/random_tests.py` depend on #6949.



---

archive/issue_comments_081324.json:
```json
{
    "body": "Changing component from basic arithmetic to symbolics.",
    "created_at": "2010-05-06T20:01:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8864#issuecomment-81324",
    "user": "https://github.com/burcin"
}
```

Changing component from basic arithmetic to symbolics.



---

archive/issue_comments_081325.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-06T20:01:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8864#issuecomment-81325",
    "user": "https://github.com/burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_081326.json:
```json
{
    "body": "I applied that patch to 4.4.1. The new behaviour is ok, I get only one doctest failure in\n`lfunctions/dokchitser.py`. With 4.4.1 we got:\n\n```\nsage:  h = RR('0.0000000000001') \nsage: (zeta(2+h) - zeta(2))/h\n-0.937028232783632\n```\nWith the patch, we get:\n\n```\nsage: h = RR('0.0000000000001') \nsage: (zeta(2+h) - zeta(2))/h\n-1.66666666666667e12*pi^2 + 1.64493406684813e13\n```\nI guess the doctest result has to be changed, or zeta(2) changed to zeta(2.), since Sage does not\nautomatically propagate floats, for example `pi+1.0` remains unchanged.",
    "created_at": "2010-05-08T12:08:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8864#issuecomment-81326",
    "user": "https://github.com/zimmermann6"
}
```

I applied that patch to 4.4.1. The new behaviour is ok, I get only one doctest failure in
`lfunctions/dokchitser.py`. With 4.4.1 we got:

```
sage:  h = RR('0.0000000000001') 
sage: (zeta(2+h) - zeta(2))/h
-0.937028232783632
```
With the patch, we get:

```
sage: h = RR('0.0000000000001') 
sage: (zeta(2+h) - zeta(2))/h
-1.66666666666667e12*pi^2 + 1.64493406684813e13
```
I guess the doctest result has to be changed, or zeta(2) changed to zeta(2.), since Sage does not
automatically propagate floats, for example `pi+1.0` remains unchanged.



---

archive/issue_comments_081327.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-05-08T12:08:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8864#issuecomment-81327",
    "user": "https://github.com/zimmermann6"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_081328.json:
```json
{
    "body": "Attachment [trac_8864-symbolic_zeta.take2.patch](tarball://root/attachments/some-uuid/ticket8864/trac_8864-symbolic_zeta.take2.patch) by @burcin created at 2010-05-08 22:19:06\n\napply only this patch",
    "created_at": "2010-05-08T22:19:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8864#issuecomment-81328",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_8864-symbolic_zeta.take2.patch](tarball://root/attachments/some-uuid/ticket8864/trac_8864-symbolic_zeta.take2.patch) by @burcin created at 2010-05-08 22:19:06

apply only this patch



---

archive/issue_comments_081329.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-05-08T22:24:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8864#issuecomment-81329",
    "user": "https://github.com/burcin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_081330.json:
```json
{
    "body": "I uploaded attachment:trac_8864-symbolic_zeta.take2.patch which also includes a fix for the `lfunctions/dokchitser.py` doctest. I simply replaced `zeta(2)` with `zeta(2)` to get a numeric evaluation.\n\nI agree that `pi+1.0` looks strange, but that is not so trivial to fix. :) FWIW, maple also seems to leave that unevaluated:\n\n```\n    |\\^/|     Maple 12 (IBM INTEL LINUX)\n._|\\|   |/|_. Copyright (c) Maplesoft, a division of Waterloo Maple Inc. 2008\n \\  MAPLE  /  All rights reserved. Maple is a trademark of\n <____ ____>  Waterloo Maple Inc.\n      |       Type ? for help.\n> Pi +1.0;\n                                   Pi + 1.0\n\n> 1.0*Pi;\n                                    1.0 Pi\n```",
    "created_at": "2010-05-08T22:24:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8864#issuecomment-81330",
    "user": "https://github.com/burcin"
}
```

I uploaded attachment:trac_8864-symbolic_zeta.take2.patch which also includes a fix for the `lfunctions/dokchitser.py` doctest. I simply replaced `zeta(2)` with `zeta(2)` to get a numeric evaluation.

I agree that `pi+1.0` looks strange, but that is not so trivial to fix. :) FWIW, maple also seems to leave that unevaluated:

```
    |\^/|     Maple 12 (IBM INTEL LINUX)
._|\|   |/|_. Copyright (c) Maplesoft, a division of Waterloo Maple Inc. 2008
 \  MAPLE  /  All rights reserved. Maple is a trademark of
 <____ ____>  Waterloo Maple Inc.
      |       Type ? for help.
> Pi +1.0;
                                   Pi + 1.0

> 1.0*Pi;
                                    1.0 Pi
```



---

archive/issue_comments_081331.json:
```json
{
    "body": "All tests pass now. Thus a positive review. Good work!\n\nPaul",
    "created_at": "2010-05-09T09:21:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8864#issuecomment-81331",
    "user": "https://github.com/zimmermann6"
}
```

All tests pass now. Thus a positive review. Good work!

Paul



---

archive/issue_comments_081332.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-09T09:21:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8864#issuecomment-81332",
    "user": "https://github.com/zimmermann6"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_081333.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-06T07:35:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8864#issuecomment-81333",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_021641.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-06-06T07:35:03Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8864",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8864#event-21641"
}
```
