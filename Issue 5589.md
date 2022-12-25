# Issue 5589: [with patch, positive review] binomial() doesn't work with negative integers

archive/issues_005589.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  sage-combinat\n\nKeywords: combinat, binomial coefficients\n\nbinomial() returns zero when its \"numerator\" is a negative integer, but gets it right for floating point numbers:\n\n```\nsage: binomial(-1, 5)\n0\nsage: binomial(-2, 5)\n0\nsage: binomial(-2.0, 5)\n-6.00000000000000\nsage: binomial(-1.0, 5)\n-1.00000000000000\nsage: binomial(-7, 5)  \n0\nsage: binomial(-7.0, 5)\n-462.000000000000\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/5589\n\n",
    "closed_at": "2009-03-26T01:13:16Z",
    "created_at": "2009-03-23T09:35:20Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with patch, positive review] binomial() doesn't work with negative integers",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5589",
    "user": "https://github.com/dandrake"
}
```
Assignee: @mwhansen

CC:  sage-combinat

Keywords: combinat, binomial coefficients

binomial() returns zero when its "numerator" is a negative integer, but gets it right for floating point numbers:

```
sage: binomial(-1, 5)
0
sage: binomial(-2, 5)
0
sage: binomial(-2.0, 5)
-6.00000000000000
sage: binomial(-1.0, 5)
-1.00000000000000
sage: binomial(-7, 5)  
0
sage: binomial(-7.0, 5)
-462.000000000000
```

Issue created by migration from https://trac.sagemath.org/ticket/5589





---

archive/issue_comments_043472.json:
```json
{
    "body": "Attachment [trac_5589.patch](tarball://root/attachments/some-uuid/ticket5589/trac_5589.patch) by @dandrake created at 2009-03-24 01:29:48",
    "created_at": "2009-03-24T01:29:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5589#issuecomment-43472",
    "user": "https://github.com/dandrake"
}
```

Attachment [trac_5589.patch](tarball://root/attachments/some-uuid/ticket5589/trac_5589.patch) by @dandrake created at 2009-03-24 01:29:48



---

archive/issue_comments_043473.json:
```json
{
    "body": "All doctests pass, the code looks reasonable, the documentation fixes are nice.  Positive review.",
    "created_at": "2009-03-26T00:52:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5589#issuecomment-43473",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

All doctests pass, the code looks reasonable, the documentation fixes are nice.  Positive review.



---

archive/issue_events_013162.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-03-26T01:13:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5589",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5589#event-13162"
}
```



---

archive/issue_comments_043474.json:
```json
{
    "body": "Merged in Sage 3.4.1.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-26T01:13:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5589#issuecomment-43474",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael



---

archive/issue_comments_043475.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-26T01:13:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5589#issuecomment-43475",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
