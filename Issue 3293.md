# Issue 3293: [with patch, needs review] MPolynomialRing_generic.random_element returns tuple when degree=0

archive/issues_003293.json:
```json
{
    "body": "Assignee: @burcin\n\nAttached patch changes `MPolynomialRing_generic.random_element` so that a random element from the base ring is returned when a degree 0 polynomial is requested.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3293\n\n",
    "created_at": "2008-05-24T18:00:26Z",
    "labels": [
        "component: commutative algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.3",
    "title": "[with patch, needs review] MPolynomialRing_generic.random_element returns tuple when degree=0",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3293",
    "user": "https://github.com/burcin"
}
```
Assignee: @burcin

Attached patch changes `MPolynomialRing_generic.random_element` so that a random element from the base ring is returned when a degree 0 polynomial is requested.

Issue created by migration from https://trac.sagemath.org/ticket/3293





---

archive/issue_comments_022731.json:
```json
{
    "body": "Attachment [mpolynomialring_random_element_d0_fix.patch](tarball://root/attachments/some-uuid/ticket3293/mpolynomialring_random_element_d0_fix.patch) by @burcin created at 2008-05-24 18:00:50\n\nfix for MPolynomialRing_generic.random_element",
    "created_at": "2008-05-24T18:00:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3293#issuecomment-22731",
    "user": "https://github.com/burcin"
}
```

Attachment [mpolynomialring_random_element_d0_fix.patch](tarball://root/attachments/some-uuid/ticket3293/mpolynomialring_random_element_d0_fix.patch) by @burcin created at 2008-05-24 18:00:50

fix for MPolynomialRing_generic.random_element



---

archive/issue_comments_022732.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-05-24T20:50:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3293#issuecomment-22732",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_022733.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-25T03:27:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3293#issuecomment-22733",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_007394.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-05-25T03:27:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3293",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3293#event-7394"
}
```



---

archive/issue_comments_022734.json:
```json
{
    "body": "Merged in Sage 3.0.3.alpha0",
    "created_at": "2008-05-25T03:27:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3293#issuecomment-22734",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.3.alpha0
