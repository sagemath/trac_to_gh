# Issue 3678: [with patch, with positive review] fractional powers for polynomial variables bug

archive/issues_003678.json:
```json
{
    "body": "Assignee: tbd\n\nRaising a multivariate polynomial to a fractional power is broken.\nA TypeError should be raised, but it is rounded instead. \n\n```\nsage: pr = PolynomialRing(QQ, \"u,v\")\nsage: pr.injvar()\nDefining u, v\nsage: u^(1/2)\n1\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/3678\n\n",
    "closed_at": "2008-12-21T22:39:38Z",
    "created_at": "2008-07-19T06:00:37Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.3",
    "title": "[with patch, with positive review] fractional powers for polynomial variables bug",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3678",
    "user": "https://github.com/wdjoyner"
}
```
Assignee: tbd

Raising a multivariate polynomial to a fractional power is broken.
A TypeError should be raised, but it is rounded instead. 

```
sage: pr = PolynomialRing(QQ, "u,v")
sage: pr.injvar()
Defining u, v
sage: u^(1/2)
1
```

Issue created by migration from https://trac.sagemath.org/ticket/3678





---

archive/issue_comments_025991.json:
```json
{
    "body": "The attached patch fixes this by introducing the same type-check as in the univariate polynomial case.",
    "created_at": "2008-12-21T05:29:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3678",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3678#issuecomment-25991",
    "user": "https://github.com/aghitza"
}
```

The attached patch fixes this by introducing the same type-check as in the univariate polynomial case.



---

archive/issue_comments_025992.json:
```json
{
    "body": "Attachment [trac_3678.patch](tarball://root/attachments/some-uuid/ticket3678/trac_3678.patch) by @aghitza created at 2008-12-21 05:29:15",
    "created_at": "2008-12-21T05:29:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3678",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3678#issuecomment-25992",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac_3678.patch](tarball://root/attachments/some-uuid/ticket3678/trac_3678.patch) by @aghitza created at 2008-12-21 05:29:15



---

archive/issue_comments_025993.json:
```json
{
    "body": "Positive review.  Patch applies cleanly to 3.2.2 and tests in sage/rings/polynomial pass.",
    "created_at": "2008-12-21T17:58:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3678",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3678#issuecomment-25993",
    "user": "https://github.com/JohnCremona"
}
```

Positive review.  Patch applies cleanly to 3.2.2 and tests in sage/rings/polynomial pass.



---

archive/issue_comments_025994.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-21T22:39:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3678",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3678#issuecomment-25994",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_008420.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-21T22:39:38Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3678",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3678#event-8420"
}
```



---

archive/issue_events_008421.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-21T22:39:38Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3678",
    "milestone": "sage-3.2.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3678#event-8421"
}
```



---

archive/issue_comments_025995.json:
```json
{
    "body": "Merged in Sage 3.2.3.alpha0",
    "created_at": "2008-12-21T22:39:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3678",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3678#issuecomment-25995",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.3.alpha0
