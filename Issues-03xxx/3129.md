# Issue 3129: [with patch, positive review] The singular interface should not claim to support polynomial rings with no variables

archive/issues_003129.json:
```json
{
    "body": "Assignee: broune\n\nThe function can_convert_to_singular in polynomial_singular_interface claims (by returning True) that Singular can support multivariate polynomial rings with no variables. This claim seems to be unintended, since the wrapper for Singular polynomial ideals claims the opposite.\n\nThe attached trivial patch makes can_convert_to_singular return False if the passed-in ring has zero generators.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3129\n\n",
    "closed_at": "2008-05-11T08:08:18Z",
    "created_at": "2008-05-07T23:01:58Z",
    "labels": [
        "component: algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "[with patch, positive review] The singular interface should not claim to support polynomial rings with no variables",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3129",
    "user": "https://trac.sagemath.org/admin/accounts/users/broune"
}
```
Assignee: broune

The function can_convert_to_singular in polynomial_singular_interface claims (by returning True) that Singular can support multivariate polynomial rings with no variables. This claim seems to be unintended, since the wrapper for Singular polynomial ideals claims the opposite.

The attached trivial patch makes can_convert_to_singular return False if the passed-in ring has zero generators.


Issue created by migration from https://trac.sagemath.org/ticket/3129





---

archive/issue_comments_021634.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-05-07T23:03:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3129",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3129#issuecomment-21634",
    "user": "https://trac.sagemath.org/admin/accounts/users/broune"
}
```

Changing status from new to assigned.



---

archive/issue_comments_021635.json:
```json
{
    "body": "Attachment [novar_singular.changeset](tarball://root/attachments/some-uuid/ticket3129/novar_singular.changeset) by broune created at 2008-05-07 23:03:06",
    "created_at": "2008-05-07T23:03:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3129",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3129#issuecomment-21635",
    "user": "https://trac.sagemath.org/admin/accounts/users/broune"
}
```

Attachment [novar_singular.changeset](tarball://root/attachments/some-uuid/ticket3129/novar_singular.changeset) by broune created at 2008-05-07 23:03:06



---

archive/issue_comments_021636.json:
```json
{
    "body": "Looks good; doctests pass in sage/rings/polynomial.  Positive review.",
    "created_at": "2008-05-10T20:51:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3129",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3129#issuecomment-21636",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Looks good; doctests pass in sage/rings/polynomial.  Positive review.



---

archive/issue_events_007065.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-05-11T08:08:18Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3129",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3129#event-7065"
}
```



---

archive/issue_comments_021637.json:
```json
{
    "body": "Merged in Sage 3.0.2.alpha0",
    "created_at": "2008-05-11T08:08:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3129",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3129#issuecomment-21637",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.2.alpha0



---

archive/issue_comments_021638.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-11T08:08:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3129",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3129#issuecomment-21638",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
