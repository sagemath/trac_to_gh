# Issue 4193: Coercion between relative and absolute number fields

archive/issues_004193.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  fwclarke\n\nIs there supposed to be a canonical coercion map between a relative number field and its associated absolute field?\n\nAt the moment (in 3.1.2) there apparently isn't, and trying to force one raises a TypeError:\n\n```\nsage: K1.<a> = NumberField(x^3 - 2)\nsage: R.<y> = PolynomialRing(K1).gen()\nsage: K2.<b> = K1.extension(y^2 - a)\nsage: K2abs = K2.absolute_field('w')\nsage: K2abs(b)\nTypeError: Cannot coerce element into this number field\n```\n\n\nI suppose it's sort of fair enough as there exist multiple K1-linear embeddings from K2 into K2abs, but shouldn't the definition of K2abs give a distinguished element of this set, sending the generator b of K2 to the generator w of K2abs?\n\nThis causes problems elsewhere, as the code for relative orders in number fields relies on having such a coercion to do basic element-creation and membership-testing routines, and these are all broken as a result:\n\n```\nsage: R = K2.order(b)\nsage: b in R\nFalse\nsage: bb = R.gens()[1] # b by any other name\nsage: bb == b\nTrue\nsage: bb.parent() is R\nTrue\nsage: bb in R\nFalse\nsage: R(bb) # trying to coerce something into its own parent!\nTypeError: Cannot coerce element into this number field\n```\n\n\nI uncovered this last problem first while trying to fix #4190, or more precisely while trying to write a doctest for a fix that I'd already written. (I have a fix which works for absolute orders and should work for relative orders too, but there's no way it can work given the above general brokenness.)\n\nDavid\n\nIssue created by migration from https://trac.sagemath.org/ticket/4193\n\n",
    "created_at": "2008-09-25T10:15:29Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.2",
    "title": "Coercion between relative and absolute number fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4193",
    "user": "@loefflerd"
}
```
Assignee: @williamstein

CC:  fwclarke

Is there supposed to be a canonical coercion map between a relative number field and its associated absolute field?

At the moment (in 3.1.2) there apparently isn't, and trying to force one raises a TypeError:

```
sage: K1.<a> = NumberField(x^3 - 2)
sage: R.<y> = PolynomialRing(K1).gen()
sage: K2.<b> = K1.extension(y^2 - a)
sage: K2abs = K2.absolute_field('w')
sage: K2abs(b)
TypeError: Cannot coerce element into this number field
```


I suppose it's sort of fair enough as there exist multiple K1-linear embeddings from K2 into K2abs, but shouldn't the definition of K2abs give a distinguished element of this set, sending the generator b of K2 to the generator w of K2abs?

This causes problems elsewhere, as the code for relative orders in number fields relies on having such a coercion to do basic element-creation and membership-testing routines, and these are all broken as a result:

```
sage: R = K2.order(b)
sage: b in R
False
sage: bb = R.gens()[1] # b by any other name
sage: bb == b
True
sage: bb.parent() is R
True
sage: bb in R
False
sage: R(bb) # trying to coerce something into its own parent!
TypeError: Cannot coerce element into this number field
```


I uncovered this last problem first while trying to fix #4190, or more precisely while trying to write a doctest for a fix that I'd already written. (I have a fix which works for absolute orders and should work for relative orders too, but there's no way it can work given the above general brokenness.)

David

Issue created by migration from https://trac.sagemath.org/ticket/4193





---

archive/issue_comments_030430.json:
```json
{
    "body": "I'm pleased to report that this seems to be fixed by fwclarke's patch for #5508. There isn't  automatic coercion between relative + absolute fields but it's debatable whether there should be; the more severe issue was the problems with orders assuming that there was in their coercion code, which is now fixed. Well done that man.",
    "created_at": "2009-03-17T10:06:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4193#issuecomment-30430",
    "user": "@loefflerd"
}
```

I'm pleased to report that this seems to be fixed by fwclarke's patch for #5508. There isn't  automatic coercion between relative + absolute fields but it's debatable whether there should be; the more severe issue was the problems with orders assuming that there was in their coercion code, which is now fixed. Well done that man.



---

archive/issue_comments_030431.json:
```json
{
    "body": "To close this we would need a doctest.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-25T08:54:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4193#issuecomment-30431",
    "user": "mabshoff"
}
```

To close this we would need a doctest.

Cheers,

Michael



---

archive/issue_comments_030432.json:
```json
{
    "body": "I have added a doctest that checks this is corrected to my latest patch at #5159. This also includes another patch to catch a doctest failure arising from #5508 on 32-bit machines.",
    "created_at": "2009-03-27T10:39:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4193#issuecomment-30432",
    "user": "@loefflerd"
}
```

I have added a doctest that checks this is corrected to my latest patch at #5159. This also includes another patch to catch a doctest failure arising from #5508 on 32-bit machines.



---

archive/issue_comments_030433.json:
```json
{
    "body": "Michael: can we close this ticket now, as with 5508 and 5159 merged, the code contains both a fix and a doctest to prove the fix works?\n\nRegards,\n\nDavid",
    "created_at": "2009-04-24T08:39:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4193#issuecomment-30433",
    "user": "@loefflerd"
}
```

Michael: can we close this ticket now, as with 5508 and 5159 merged, the code contains both a fix and a doctest to prove the fix works?

Regards,

David



---

archive/issue_comments_030434.json:
```json
{
    "body": "Fixed in Sage 3.4.2.alpha0 by #5508.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-24T08:44:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4193#issuecomment-30434",
    "user": "mabshoff"
}
```

Fixed in Sage 3.4.2.alpha0 by #5508.

Cheers,

Michael



---

archive/issue_comments_030435.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-24T08:44:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4193#issuecomment-30435",
    "user": "mabshoff"
}
```

Resolution: fixed
