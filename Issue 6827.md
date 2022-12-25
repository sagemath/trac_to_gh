# Issue 6827: [with patch, needs review] probability distributions doctests + general discrete distribution

archive/issues_006827.json:
```json
{
    "body": "Assignee: mhampton\n\nThis patch attends to sage/gsl/probability_distribution.pyx:\n\n- 100% doctest coverage (previously this file had nodoctest)\n\n- fixed formatting (all indents now 4 spaces).\n\n- ReST docstring formatting.\n\n- One extra class: general discrete distributions (I think that #6662 should be marked as invalid since the code there fits better here).\n\n- valgrind ok\n\n- probability_distribution.pyx added to the reference manual under Probability.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6827\n\n",
    "created_at": "2009-08-26T08:28:09Z",
    "labels": [
        "component: statistics",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "[with patch, needs review] probability distributions doctests + general discrete distribution",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6827",
    "user": "https://trac.sagemath.org/admin/accounts/users/carlohamalainen"
}
```
Assignee: mhampton

This patch attends to sage/gsl/probability_distribution.pyx:

- 100% doctest coverage (previously this file had nodoctest)

- fixed formatting (all indents now 4 spaces).

- ReST docstring formatting.

- One extra class: general discrete distributions (I think that #6662 should be marked as invalid since the code there fits better here).

- valgrind ok

- probability_distribution.pyx added to the reference manual under Probability.


Issue created by migration from https://trac.sagemath.org/ticket/6827





---

archive/issue_comments_056209.json:
```json
{
    "body": "Attachment [probability_distribution.patch](tarball://root/attachments/some-uuid/ticket6827/probability_distribution.patch) by carlohamalainen created at 2009-08-26 08:28:28",
    "created_at": "2009-08-26T08:28:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6827#issuecomment-56209",
    "user": "https://trac.sagemath.org/admin/accounts/users/carlohamalainen"
}
```

Attachment [probability_distribution.patch](tarball://root/attachments/some-uuid/ticket6827/probability_distribution.patch) by carlohamalainen created at 2009-08-26 08:28:28



---

archive/issue_comments_056210.json:
```json
{
    "body": "Attachment [trac_6827_review.patch](tarball://root/attachments/some-uuid/ticket6827/trac_6827_review.patch) by @mwhansen created at 2009-09-07 21:22:28\n\nLooks good to me.  I added a one character change to get the docs to build without warning.  Both patches should be applied.\n\nIt would probably be good to factor each of the RealDistributions out into their own classes so we don't have to have the massive if/elif/else statements.  It might be a good easy project if someone is working on stats stuff this fall.",
    "created_at": "2009-09-07T21:22:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6827#issuecomment-56210",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_6827_review.patch](tarball://root/attachments/some-uuid/ticket6827/trac_6827_review.patch) by @mwhansen created at 2009-09-07 21:22:28

Looks good to me.  I added a one character change to get the docs to build without warning.  Both patches should be applied.

It would probably be good to factor each of the RealDistributions out into their own classes so we don't have to have the massive if/elif/else statements.  It might be a good easy project if someone is working on stats stuff this fall.



---

archive/issue_comments_056211.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-09T10:39:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6827#issuecomment-56211",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_007061.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-09T10:39:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6827",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6827#event-7061"
}
```



---

archive/issue_comments_056212.json:
```json
{
    "body": "Merged patches in this order:\n\n1. `probability_distribution.patch`\n2. `trac_6827_review.patch`",
    "created_at": "2009-09-09T10:39:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6827#issuecomment-56212",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged patches in this order:

1. `probability_distribution.patch`
2. `trac_6827_review.patch`
