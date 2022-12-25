# Issue 2149: Rename BooleanPolynomialRing

archive/issues_002149.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  @burcin\n\nKeywords: polybori\n\nWilliam Stein wrote in #2146:\n\n\"\"\"\n\nBy the way, wouldn't it be better to call it `PolynomialBooleanRing` instead of `BooleanPolynomialRing` I suggest this for two reasons: \n* It is `PolyBoRi`, after all, not `BoPolyRi`. \n* The other Sage polynomial ring(s) starts with \"Polynomial\" \n\n\"\"\"\n\nIssue created by migration from https://trac.sagemath.org/ticket/2149\n\n",
    "created_at": "2008-02-13T13:11:35Z",
    "labels": [
        "component: commutative algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "Rename BooleanPolynomialRing",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2149",
    "user": "https://github.com/malb"
}
```
Assignee: @malb

CC:  @burcin

Keywords: polybori

William Stein wrote in #2146:

"""

By the way, wouldn't it be better to call it `PolynomialBooleanRing` instead of `BooleanPolynomialRing` I suggest this for two reasons: 
* It is `PolyBoRi`, after all, not `BoPolyRi`. 
* The other Sage polynomial ring(s) starts with "Polynomial" 

"""

Issue created by migration from https://trac.sagemath.org/ticket/2149





---

archive/issue_comments_014072.json:
```json
{
    "body": "Attachment [2149.patch](tarball://root/attachments/some-uuid/ticket2149/2149.patch) by @mwhansen created at 2008-02-29 02:15:05",
    "created_at": "2008-02-29T02:15:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2149#issuecomment-14072",
    "user": "https://github.com/mwhansen"
}
```

Attachment [2149.patch](tarball://root/attachments/some-uuid/ticket2149/2149.patch) by @mwhansen created at 2008-02-29 02:15:05



---

archive/issue_comments_014073.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-29T02:15:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2149#issuecomment-14073",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_014074.json:
```json
{
    "body": "Changing assignee from @malb to @mwhansen.",
    "created_at": "2008-02-29T02:15:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2149#issuecomment-14074",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from @malb to @mwhansen.



---

archive/issue_comments_014075.json:
```json
{
    "body": "By inspection only, the patch looks good. I assume it passes all the tests.\n\nI am still not decided about this naming issue though. The arguments for renaming are not really valid.\n- It's named `PolyBoRi` to make it easy to pronounce. All the literature on `PolyBoRi` talks about Boolean polynomials, see http://polybori.sourceforge.net/further.shtml.\n- The class names should be easy to understand for humans, machines don't care what they are anyway. So why make them look machine like? `UnivariateRationalPolynomialRing` is more natural and easier to understand than `PolynomialRingUnivariateRational`.\n\nIf we agree that the original reasoning is correct, we should consider renaming `BooleanPolynomial` to `Polynomial_Boolean`, similarly for `BooleanMonomial` and `BooleanMonomialMonoid`. \n\nNote that none of these names are meant to be seen/used directly. AFAIK, the intention was to remove the `BooleanPolynomialRing` from the global scope, when it can be constructed with the usual methods.\n\nBTW, to comply with current naming scheme, the new name should be `MPolynomial_something`.",
    "created_at": "2008-02-29T09:16:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2149#issuecomment-14075",
    "user": "https://github.com/burcin"
}
```

By inspection only, the patch looks good. I assume it passes all the tests.

I am still not decided about this naming issue though. The arguments for renaming are not really valid.
- It's named `PolyBoRi` to make it easy to pronounce. All the literature on `PolyBoRi` talks about Boolean polynomials, see http://polybori.sourceforge.net/further.shtml.
- The class names should be easy to understand for humans, machines don't care what they are anyway. So why make them look machine like? `UnivariateRationalPolynomialRing` is more natural and easier to understand than `PolynomialRingUnivariateRational`.

If we agree that the original reasoning is correct, we should consider renaming `BooleanPolynomial` to `Polynomial_Boolean`, similarly for `BooleanMonomial` and `BooleanMonomialMonoid`. 

Note that none of these names are meant to be seen/used directly. AFAIK, the intention was to remove the `BooleanPolynomialRing` from the global scope, when it can be constructed with the usual methods.

BTW, to comply with current naming scheme, the new name should be `MPolynomial_something`.



---

archive/issue_comments_014076.json:
```json
{
    "body": "Burcin's case makes sense to me.  If I understand what these gadgets actually are, they are not a special case of polynomial ring, but rather a quotient of a polynomial ring (by lots of relations like `x^2-x`).  So it is a ring of these \"boolean polynomials\" rather than a polynomial ring over some underlying Boolean gadget.\n\nIt seem a pity for mhansen to have wasted his time, but that is not in itself a very strong argument!",
    "created_at": "2008-03-27T17:32:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2149#issuecomment-14076",
    "user": "https://github.com/JohnCremona"
}
```

Burcin's case makes sense to me.  If I understand what these gadgets actually are, they are not a special case of polynomial ring, but rather a quotient of a polynomial ring (by lots of relations like `x^2-x`).  So it is a ring of these "boolean polynomials" rather than a polynomial ring over some underlying Boolean gadget.

It seem a pity for mhansen to have wasted his time, but that is not in itself a very strong argument!



---

archive/issue_comments_014077.json:
```json
{
    "body": "I'm not at all attached to this.  It was just a 2 minute search and replace.",
    "created_at": "2008-03-28T01:35:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2149#issuecomment-14077",
    "user": "https://github.com/mwhansen"
}
```

I'm not at all attached to this.  It was just a 2 minute search and replace.



---

archive/issue_comments_014078.json:
```json
{
    "body": "I vote against renaming it.",
    "created_at": "2008-03-28T12:16:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2149#issuecomment-14078",
    "user": "https://github.com/malb"
}
```

I vote against renaming it.



---

archive/issue_events_002313.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-29T00:09:37Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2149",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2149#event-2313"
}
```



---

archive/issue_comments_014079.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2008-03-29T00:09:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2149#issuecomment-14079",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: wontfix



---

archive/issue_comments_014080.json:
```json
{
    "body": "\n```\n[00:31] <mhansen> mabshoff: For 2149, I think the consensus is to mark it as invalid.\n[00:31] <mhansen> Or wontfix.\n[00:31] <mabshoff> let me check in a minute\n[00:31] <mhansen> Sure, no problem.\n[00:37] <mabshoff> re #2149: won't fix it is.\n```\n",
    "created_at": "2008-03-29T00:09:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2149#issuecomment-14080",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```


```
[00:31] <mhansen> mabshoff: For 2149, I think the consensus is to mark it as invalid.
[00:31] <mhansen> Or wontfix.
[00:31] <mabshoff> let me check in a minute
[00:31] <mhansen> Sure, no problem.
[00:37] <mabshoff> re #2149: won't fix it is.
```

