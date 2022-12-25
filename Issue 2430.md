# Issue 2430: is_EuclideanDomain() gives wrong answers

archive/issues_002430.json:
```json
{
    "body": "In 2.10.2 and 2.10.3.rc2:\n\n```\nsage: is_EuclideanDomain(ZZ)\nFalse\n```\n\nI looked to whether any of Sage's rings would ever return True for this function, and came up with pAdicRingGeneric and no others:\n\n```\nsage: is_EuclideanDomain(pAdicRing(7))\nTrue\n```\n\nSo this idea (to have EuclideanDomains as a class) just has not been properly implemented.\nAs a start we could make rings which are certainly Euclidean (e,g, ZZ and univariate polynomials over a field) be derived from EuclideanDomain instead of PrincipalIdealDomain as they are now.\n\nThat would not be a complete solution, since (for example) some rings of integers of number fields are Euclidean, though it is not easy to say which;  and there is no functionality to answer the question \"is R Euclidean\" except to see if R's class is (derived from) EuclideanDomain, which for rings of integers it never will be!\n\nOne other puzzling -- and inconsistent -- thing is that EuclideanDomainElement has a broader scope than EuclideanDomain:\n\n```\nsage: is_EuclideanDomain(ZZ)\nFalse\nsage: is_EuclideanDomainElement(ZZ(1))\nTrue\n\nsage: is_EuclideanDomain(R)\nFalse\nsage: is_EuclideanDomainElement(x)\nTrue\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2430\n\n",
    "closed_at": "2008-09-26T18:48:24Z",
    "created_at": "2008-03-08T20:35:42Z",
    "labels": [
        "component: commutative algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "is_EuclideanDomain() gives wrong answers",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2430",
    "user": "https://github.com/JohnCremona"
}
```
In 2.10.2 and 2.10.3.rc2:

```
sage: is_EuclideanDomain(ZZ)
False
```

I looked to whether any of Sage's rings would ever return True for this function, and came up with pAdicRingGeneric and no others:

```
sage: is_EuclideanDomain(pAdicRing(7))
True
```

So this idea (to have EuclideanDomains as a class) just has not been properly implemented.
As a start we could make rings which are certainly Euclidean (e,g, ZZ and univariate polynomials over a field) be derived from EuclideanDomain instead of PrincipalIdealDomain as they are now.

That would not be a complete solution, since (for example) some rings of integers of number fields are Euclidean, though it is not easy to say which;  and there is no functionality to answer the question "is R Euclidean" except to see if R's class is (derived from) EuclideanDomain, which for rings of integers it never will be!

One other puzzling -- and inconsistent -- thing is that EuclideanDomainElement has a broader scope than EuclideanDomain:

```
sage: is_EuclideanDomain(ZZ)
False
sage: is_EuclideanDomainElement(ZZ(1))
True

sage: is_EuclideanDomain(R)
False
sage: is_EuclideanDomainElement(x)
True
```



Issue created by migration from https://trac.sagemath.org/ticket/2430





---

archive/issue_events_005737.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-09T00:09:22Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2430",
    "milestone": "sage-2.10.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2430#event-5737"
}
```



---

archive/issue_comments_016405.json:
```json
{
    "body": "Changing assignee from mabshoff to @williamstein.",
    "created_at": "2008-03-09T00:09:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2430#issuecomment-16405",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from mabshoff to @williamstein.



---

archive/issue_comments_016406.json:
```json
{
    "body": "Changing component from Cygwin to linear algebra.",
    "created_at": "2008-03-09T00:09:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2430#issuecomment-16406",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing component from Cygwin to linear algebra.



---

archive/issue_comments_016407.json:
```json
{
    "body": "Changing assignee from @williamstein to @malb.",
    "created_at": "2008-03-16T02:29:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2430#issuecomment-16407",
    "user": "https://github.com/aghitza"
}
```

Changing assignee from @williamstein to @malb.



---

archive/issue_comments_016408.json:
```json
{
    "body": "Changing component from linear algebra to commutative algebra.",
    "created_at": "2008-03-16T02:29:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2430#issuecomment-16408",
    "user": "https://github.com/aghitza"
}
```

Changing component from linear algebra to commutative algebra.



---

archive/issue_comments_016409.json:
```json
{
    "body": "Remove assignee @malb.",
    "created_at": "2008-06-03T14:20:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2430#issuecomment-16409",
    "user": "https://github.com/malb"
}
```

Remove assignee @malb.



---

archive/issue_comments_016410.json:
```json
{
    "body": "I think that the current behavior is in line with the issues dealt with by #4192, and so this ticket should be closed.",
    "created_at": "2008-09-26T18:19:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2430#issuecomment-16410",
    "user": "https://github.com/jhpalmieri"
}
```

I think that the current behavior is in line with the issues dealt with by #4192, and so this ticket should be closed.



---

archive/issue_events_005738.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-26T18:48:24Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2430",
    "milestone": "sage-2.10.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2430#event-5738"
}
```



---

archive/issue_comments_016411.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2008-09-26T18:48:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2430#issuecomment-16411",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: wontfix



---

archive/issue_comments_016412.json:
```json
{
    "body": "I agreee. Closed as wontix. \n\nJohn: If you disagree please open another ticket that takes into consideration #4192, i.e. implements the proper methods exposed on the top level.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-26T18:48:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2430#issuecomment-16412",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I agreee. Closed as wontix. 

John: If you disagree please open another ticket that takes into consideration #4192, i.e. implements the proper methods exposed on the top level.

Cheers,

Michael



---

archive/issue_events_005739.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-26T18:48:24Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2430",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2430#event-5739"
}
```
