# Issue 8857: lcm over QQ[x] broken

archive/issues_008857.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @orlitzky\n\nReported by Manuel Kauers:\n\n\n```\nsage: R.<x> = QQ[x]\nsage: R(1/2).lcm(R(1))\n<boom>\nsage: R(2^31).lcm(R(1))\n<boom>\n```\n\n\nThe backtrace indicates that we call Singular for this, which is completely unnecessary.\n\nWe should check if this persists with #4000 as well.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8857\n\n",
    "created_at": "2010-05-03T14:40:18Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "lcm over QQ[x] broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8857",
    "user": "@burcin"
}
```
Assignee: @aghitza

CC:  @orlitzky

Reported by Manuel Kauers:


```
sage: R.<x> = QQ[x]
sage: R(1/2).lcm(R(1))
<boom>
sage: R(2^31).lcm(R(1))
<boom>
```


The backtrace indicates that we call Singular for this, which is completely unnecessary.

We should check if this persists with #4000 as well.

Issue created by migration from https://trac.sagemath.org/ticket/8857





---

archive/issue_comments_081391.json:
```json
{
    "body": "We're halfway there:\n\n\n```\nsage: R.<x> = QQ[x]\nsage: R(1/2).lcm(R(1))\n1\nsage: R(2^31).lcm(R(1))\n1\n```\n\n\nbut the second result is clearly wrong.",
    "created_at": "2012-01-09T02:27:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8857#issuecomment-81391",
    "user": "@orlitzky"
}
```

We're halfway there:


```
sage: R.<x> = QQ[x]
sage: R(1/2).lcm(R(1))
1
sage: R(2^31).lcm(R(1))
1
```


but the second result is clearly wrong.



---

archive/issue_comments_081392.json:
```json
{
    "body": "Replying to [comment:1 mjo]:\n> but the second result is clearly wrong.\n\nSorry if this is a stupid question, but why is it wrong? what result would you expect?",
    "created_at": "2013-12-12T14:07:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8857#issuecomment-81392",
    "user": "@mezzarobba"
}
```

Replying to [comment:1 mjo]:
> but the second result is clearly wrong.

Sorry if this is a stupid question, but why is it wrong? what result would you expect?



---

archive/issue_comments_081393.json:
```json
{
    "body": "Replying to [comment:3 mmezzarobba]:\n> \n> Sorry if this is a stupid question, but why is it wrong?\n\nIt isn't, after I read the documentation *facepalm*. Sorry.",
    "created_at": "2013-12-12T14:31:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8857#issuecomment-81393",
    "user": "@orlitzky"
}
```

Replying to [comment:3 mmezzarobba]:
> 
> Sorry if this is a stupid question, but why is it wrong?

It isn't, after I read the documentation *facepalm*. Sorry.



---

archive/issue_comments_081394.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-12-12T14:41:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8857#issuecomment-81394",
    "user": "@mezzarobba"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_081395.json:
```json
{
    "body": "This should get a doctest, since it is a bug that was fixed, albeit not in this ticket.",
    "created_at": "2013-12-12T14:55:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8857#issuecomment-81395",
    "user": "@orlitzky"
}
```

This should get a doctest, since it is a bug that was fixed, albeit not in this ticket.



---

archive/issue_comments_081396.json:
```json
{
    "body": "Replying to [comment:6 mjo]:\n> This should get a doctest, since it is a bug that was fixed, albeit not in this ticket.\n\nYou are right.",
    "created_at": "2013-12-12T17:07:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8857#issuecomment-81396",
    "user": "@mezzarobba"
}
```

Replying to [comment:6 mjo]:
> This should get a doctest, since it is a bug that was fixed, albeit not in this ticket.

You are right.



---

archive/issue_comments_081397.json:
```json
{
    "body": "New commits:",
    "created_at": "2013-12-12T17:10:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8857#issuecomment-81397",
    "user": "@mezzarobba"
}
```

New commits:



---

archive/issue_comments_081398.json:
```json
{
    "body": "I think that this is very counter-intuitive behavior and is inconsistent. Compare:\n\n```\nsage: R.<x> = ZZ['x']\nsage: R(2^31).lcm(2*x + 1)\n4294967296*x + 2147483648\nsage: R(2^31).lcm(1)\n2147483648\n\nsage: QQ(2^31).lcm(QQ(1))\n2147483648\n\nsage: R.<x,y> = QQ['x,y']\nsage: R(2^31).lcm(2*x + 1)\n4294967296*x + 2147483648\nsage: R(2^31).lcm(1)\n2147483648\n```\n\nwith\n\n```\nsage: R.<x> = QQ['x']\nsage: R(2^31).lcm(2*x + 1)\nx + 1/2\n```\n\n\nHowever, I do think that this should have a doctest nevertheless.",
    "created_at": "2013-12-12T17:10:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8857#issuecomment-81398",
    "user": "@tscrim"
}
```

I think that this is very counter-intuitive behavior and is inconsistent. Compare:

```
sage: R.<x> = ZZ['x']
sage: R(2^31).lcm(2*x + 1)
4294967296*x + 2147483648
sage: R(2^31).lcm(1)
2147483648

sage: QQ(2^31).lcm(QQ(1))
2147483648

sage: R.<x,y> = QQ['x,y']
sage: R(2^31).lcm(2*x + 1)
4294967296*x + 2147483648
sage: R(2^31).lcm(1)
2147483648
```

with

```
sage: R.<x> = QQ['x']
sage: R(2^31).lcm(2*x + 1)
x + 1/2
```


However, I do think that this should have a doctest nevertheless.



---

archive/issue_comments_081399.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-12-12T17:10:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8857#issuecomment-81399",
    "user": "@tscrim"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_081400.json:
```json
{
    "body": "Ack, I deleted the branch due to race conditions.\n----\nNew commits:",
    "created_at": "2013-12-12T17:11:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8857#issuecomment-81400",
    "user": "@tscrim"
}
```

Ack, I deleted the branch due to race conditions.
----
New commits:



---

archive/issue_comments_081401.json:
```json
{
    "body": "Replying to [comment:9 tscrim]:\n> I think that this is very counter-intuitive behavior and is inconsistent.\n\nWhat part do you find counter-intuitive? That `p.lcm(q)`\ufffd for `p, q \u2208 QQ[x]` returns the monic lcm of `p` and `q` is clearly what I would expect, even though it might make sense to ask that `gcd\u00b7lcm = p\u00b7q`. However, I do find the definition of `gcd` and `lcm` over `QQ` counter-intuitive.",
    "created_at": "2014-01-27T12:48:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8857#issuecomment-81401",
    "user": "@mezzarobba"
}
```

Replying to [comment:9 tscrim]:
> I think that this is very counter-intuitive behavior and is inconsistent.

What part do you find counter-intuitive? That `p.lcm(q)`� for `p, q ∈ QQ[x]` returns the monic lcm of `p` and `q` is clearly what I would expect, even though it might make sense to ask that `gcd·lcm = p·q`. However, I do find the definition of `gcd` and `lcm` over `QQ` counter-intuitive.



---

archive/issue_comments_081402.json:
```json
{
    "body": "It's just not what my naive/non-number-theorist self expects, but I can see why `lcm` would be counter-intuitive. However you do agree that this behavior is inconsistent? Also, a similar problem with using `RR` (and other like fields) as in the this ticket:\n\n```\nsage: R.<x,y> = RR[]\nsage: R(2^31).lcm(R(2*x+1)) # Boom\n```\n\nand `R.<x,y> = FractionField(QQ['t'])[]`. So should we use this ticket as one to fix this as well since it essentially is the same bug?",
    "created_at": "2014-01-27T15:52:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8857#issuecomment-81402",
    "user": "@tscrim"
}
```

It's just not what my naive/non-number-theorist self expects, but I can see why `lcm` would be counter-intuitive. However you do agree that this behavior is inconsistent? Also, a similar problem with using `RR` (and other like fields) as in the this ticket:

```
sage: R.<x,y> = RR[]
sage: R(2^31).lcm(R(2*x+1)) # Boom
```

and `R.<x,y> = FractionField(QQ['t'])[]`. So should we use this ticket as one to fix this as well since it essentially is the same bug?



---

archive/issue_comments_081403.json:
```json
{
    "body": "Replying to [comment:12 tscrim]:\n> However you do agree that this behavior is inconsistent?\n\nFrom a user interface point of view, yes, I do. From a mathematical (or programming) point of view I am not sure.\n\n> Also, a similar problem with using `RR` (and other like fields) as in the this ticket:\n> {{{\n> sage: R.<x,y> = RR[]\n> sage: R(2^31).lcm(R(2*x+1)) # Boom\n> }}}\n> and `R.<x,y> = FractionField(QQ['t'])[]`. So should we use this ticket as one to fix this as well since it essentially is the same bug?\n\nYes, why not.",
    "created_at": "2014-01-27T16:36:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8857#issuecomment-81403",
    "user": "@mezzarobba"
}
```

Replying to [comment:12 tscrim]:
> However you do agree that this behavior is inconsistent?

From a user interface point of view, yes, I do. From a mathematical (or programming) point of view I am not sure.

> Also, a similar problem with using `RR` (and other like fields) as in the this ticket:
> {{{
> sage: R.<x,y> = RR[]
> sage: R(2^31).lcm(R(2*x+1)) # Boom
> }}}
> and `R.<x,y> = FractionField(QQ['t'])[]`. So should we use this ticket as one to fix this as well since it essentially is the same bug?

Yes, why not.
