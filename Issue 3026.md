# Issue 3026: multivariate polynomial ring with no variables do not print properly

archive/issues_003026.json:
```json
{
    "body": "Assignee: @malb\n\nThe following output from sage does not make too much sense.\n\nsage: PolynomialRing(QQ, names=[])\nMultivariate Polynomial Ring in  over Rational Field\n\nwstein suggested that it might print something like the following.\n\nMultivariate Polynomial Ring in no variables over Rational Field\n\nIssue created by migration from https://trac.sagemath.org/ticket/3026\n\n",
    "created_at": "2008-04-26T00:24:06Z",
    "labels": [
        "component: commutative algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "multivariate polynomial ring with no variables do not print properly",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3026",
    "user": "https://trac.sagemath.org/admin/accounts/users/broune"
}
```
Assignee: @malb

The following output from sage does not make too much sense.

sage: PolynomialRing(QQ, names=[])
Multivariate Polynomial Ring in  over Rational Field

wstein suggested that it might print something like the following.

Multivariate Polynomial Ring in no variables over Rational Field

Issue created by migration from https://trac.sagemath.org/ticket/3026





---

archive/issue_comments_020762.json:
```json
{
    "body": "Changing assignee from @malb to broune.",
    "created_at": "2008-05-07T20:15:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3026",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3026#issuecomment-20762",
    "user": "https://trac.sagemath.org/admin/accounts/users/broune"
}
```

Changing assignee from @malb to broune.



---

archive/issue_comments_020763.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-05-07T20:16:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3026",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3026#issuecomment-20763",
    "user": "https://trac.sagemath.org/admin/accounts/users/broune"
}
```

Changing status from new to assigned.



---

archive/issue_comments_020764.json:
```json
{
    "body": "Attachment [novariables.changeset](tarball://root/attachments/some-uuid/ticket3026/novariables.changeset) by broune created at 2008-05-07 20:23:49",
    "created_at": "2008-05-07T20:23:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3026",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3026#issuecomment-20764",
    "user": "https://trac.sagemath.org/admin/accounts/users/broune"
}
```

Attachment [novariables.changeset](tarball://root/attachments/some-uuid/ticket3026/novariables.changeset) by broune created at 2008-05-07 20:23:49



---

archive/issue_comments_020765.json:
```json
{
    "body": "Code looks good, doctests pass in sage/rings/polynomial.  Positive review.",
    "created_at": "2008-05-10T23:06:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3026",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3026#issuecomment-20765",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Code looks good, doctests pass in sage/rings/polynomial.  Positive review.



---

archive/issue_comments_020766.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-11T09:22:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3026",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3026#issuecomment-20766",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_020767.json:
```json
{
    "body": "Merged in Sage 3.0.2.alpha0",
    "created_at": "2008-05-11T09:22:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3026",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3026#issuecomment-20767",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.2.alpha0



---

archive/issue_events_003231.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-05-11T09:22:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3026",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3026#event-3231"
}
```
