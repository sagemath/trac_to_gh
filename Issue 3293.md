# Issue 3293: [with patch, needs review] MPolynomialRing_generic.random_element returns tuple when degree=0

archive/issues_003293.json:
```json
{
    "body": "Assignee: @burcin\n\nAttached patch changes `MPolynomialRing_generic.random_element` so that a random element from the base ring is returned when a degree 0 polynomial is requested.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3293\n\n",
    "created_at": "2008-05-24T18:00:26Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.3",
    "title": "[with patch, needs review] MPolynomialRing_generic.random_element returns tuple when degree=0",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3293",
    "user": "@burcin"
}
```
Assignee: @burcin

Attached patch changes `MPolynomialRing_generic.random_element` so that a random element from the base ring is returned when a degree 0 polynomial is requested.

Issue created by migration from https://trac.sagemath.org/ticket/3293





---

archive/issue_comments_022778.json:
```json
{
    "body": "Attachment [mpolynomialring_random_element_d0_fix.patch](tarball://root/attachments/some-uuid/ticket3293/mpolynomialring_random_element_d0_fix.patch) by @burcin created at 2008-05-24 18:00:50\n\nfix for MPolynomialRing_generic.random_element",
    "created_at": "2008-05-24T18:00:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3293#issuecomment-22778",
    "user": "@burcin"
}
```

Attachment [mpolynomialring_random_element_d0_fix.patch](tarball://root/attachments/some-uuid/ticket3293/mpolynomialring_random_element_d0_fix.patch) by @burcin created at 2008-05-24 18:00:50

fix for MPolynomialRing_generic.random_element



---

archive/issue_comments_022779.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-05-24T20:50:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3293#issuecomment-22779",
    "user": "@mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_022780.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-25T03:27:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3293#issuecomment-22780",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_022781.json:
```json
{
    "body": "Merged in Sage 3.0.3.alpha0",
    "created_at": "2008-05-25T03:27:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3293#issuecomment-22781",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.3.alpha0
