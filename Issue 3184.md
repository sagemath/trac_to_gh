# Issue 3184: broken p-adic getslice

archive/issues_003184.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  @craigcitro\n\n(This ticket was split off from #2943)\n\nThis is okay:\n\n\n```\nsage: K = Qp(13,7)\nsage: R.<t> = K[]       \nsage: a = 13^7*t^3 + K(169,4)*t - 13^4\nsage: a[1:2]\n(13^2 + O(13^4))*t\n```\n\n\nThis dies:\n\n\n```\nsage: t[0:1]\n[boom]\n```\n\n\nThe original context for this bug was along the lines of (see #2943 for more examples):\n\n\n```\nsage: K = Qp(p,10)\nsage: C.<t> = LaurentSeriesRing(K)\nsage: D.<s> = PolynomialRing(C)\nsage: z = (1 + O(t)) + t*s^2\nsage: z * z\n[boom]\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3184\n\n",
    "created_at": "2008-05-13T13:00:20Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "broken p-adic getslice",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3184",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: somebody

CC:  @craigcitro

(This ticket was split off from #2943)

This is okay:


```
sage: K = Qp(13,7)
sage: R.<t> = K[]       
sage: a = 13^7*t^3 + K(169,4)*t - 13^4
sage: a[1:2]
(13^2 + O(13^4))*t
```


This dies:


```
sage: t[0:1]
[boom]
```


The original context for this bug was along the lines of (see #2943 for more examples):


```
sage: K = Qp(p,10)
sage: C.<t> = LaurentSeriesRing(K)
sage: D.<s> = PolynomialRing(C)
sage: z = (1 + O(t)) + t*s^2
sage: z * z
[boom]
```



Issue created by migration from https://trac.sagemath.org/ticket/3184





---

archive/issue_comments_021984.json:
```json
{
    "body": "Craig has become a getslice expert, so let's CC him :)\n\nCheers,\n\nMichael",
    "created_at": "2008-11-23T10:15:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3184",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3184#issuecomment-21984",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Craig has become a getslice expert, so let's CC him :)

Cheers,

Michael



---

archive/issue_comments_021985.json:
```json
{
    "body": "Attachment [3184.patch](tarball://root/attachments/some-uuid/ticket3184/3184.patch) by @roed314 created at 2009-01-24 08:41:39",
    "created_at": "2009-01-24T08:41:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3184",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3184#issuecomment-21985",
    "user": "https://github.com/roed314"
}
```

Attachment [3184.patch](tarball://root/attachments/some-uuid/ticket3184/3184.patch) by @roed314 created at 2009-01-24 08:41:39



---

archive/issue_comments_021986.json:
```json
{
    "body": "First comment: getslice is deprecated; it should be __getitem__ now.\n\nSecond, there is a standard block of code for slicing...using that will make sure that things are consistent for people that understand python slices.",
    "created_at": "2009-02-04T15:17:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3184",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3184#issuecomment-21986",
    "user": "https://github.com/jasongrout"
}
```

First comment: getslice is deprecated; it should be __getitem__ now.

Second, there is a standard block of code for slicing...using that will make sure that things are consistent for people that understand python slices.



---

archive/issue_comments_021987.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-03-19T01:20:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3184",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3184#issuecomment-21987",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Looks good to me.



---

archive/issue_comments_021988.json:
```json
{
    "body": "Merged in Sage 3.4.1.alpha0.\n\nCheeers,\n\nMichael",
    "created_at": "2009-03-20T20:34:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3184",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3184#issuecomment-21988",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.1.alpha0.

Cheeers,

Michael



---

archive/issue_events_003402.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-03-20T20:34:56Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3184",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3184#event-3402"
}
```



---

archive/issue_comments_021989.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-20T20:34:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3184",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3184#issuecomment-21989",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
