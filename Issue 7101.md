# Issue 7101: Inconsistency in polynomial ring creation.

archive/issues_007101.json:
```json
{
    "body": "Assignee: tbd\n\n      Hi sage developers,\n\nI need to play with polynomials on various kind of coefficients. So I tried\nthe following:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nLoading Sage library. Current Mercurial branch is: combinat\nsage: R=QQ[x]\nsage: R(1+x)\nx + 1\nsage: R=ZZ[x]\nsage: R(1+x)\nx + 1\nsage: R=RealField(200)[x]\nsage: R(1+x)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n[...]\nTypeError: x is not a variable of Univariate Polynomial Ring in x over Real Field with 200 bits of precision\n```\n\n| Sage Version 4.1.1, Release Date: 2009-08-14                       |\n| Type notebook() for the GUI, and license() for information.        |\nAs mvngu pointed out on irc: the following works\n\n```\nsage: R.<x> = RealField(20)[\"x\"]\nsage: R(1 + x)\n1.0000*x + 1.0000\n```\n\nBut this is not very beautiful and worse it is very inconsistent...\nAt least the error message should be more understandable...\n\nWhat should we do about it ?\n\nCheers,\n\nFlorent\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7101\n\n",
    "created_at": "2009-10-03T15:53:26Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Inconsistency in polynomial ring creation.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7101",
    "user": "https://github.com/hivert"
}
```
Assignee: tbd

      Hi sage developers,

I need to play with polynomials on various kind of coefficients. So I tried
the following:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: combinat
sage: R=QQ[x]
sage: R(1+x)
x + 1
sage: R=ZZ[x]
sage: R(1+x)
x + 1
sage: R=RealField(200)[x]
sage: R(1+x)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
[...]
TypeError: x is not a variable of Univariate Polynomial Ring in x over Real Field with 200 bits of precision
```

| Sage Version 4.1.1, Release Date: 2009-08-14                       |
| Type notebook() for the GUI, and license() for information.        |
As mvngu pointed out on irc: the following works

```
sage: R.<x> = RealField(20)["x"]
sage: R(1 + x)
1.0000*x + 1.0000
```

But this is not very beautiful and worse it is very inconsistent...
At least the error message should be more understandable...

What should we do about it ?

Cheers,

Florent


Issue created by migration from https://trac.sagemath.org/ticket/7101





---

archive/issue_comments_058666.json:
```json
{
    "body": "This is fixed by the patches at #7007 and #5639.",
    "created_at": "2009-10-04T03:48:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7101",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7101#issuecomment-58666",
    "user": "https://github.com/mwhansen"
}
```

This is fixed by the patches at #7007 and #5639.



---

archive/issue_comments_058667.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-10-04T03:50:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7101",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7101#issuecomment-58667",
    "user": "https://github.com/mwhansen"
}
```

Resolution: duplicate



---

archive/issue_comments_058668.json:
```json
{
    "body": "Err, it's a duplicate of #5755 which has been fixed.",
    "created_at": "2009-10-04T03:50:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7101",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7101#issuecomment-58668",
    "user": "https://github.com/mwhansen"
}
```

Err, it's a duplicate of #5755 which has been fixed.



---

archive/issue_events_016794.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-10-04T03:50:29Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7101",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7101#event-16794"
}
```



---

archive/issue_events_016795.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-10-14T16:57:47Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7101",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7101#event-16795"
}
```
