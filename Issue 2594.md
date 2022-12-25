# Issue 2594: [with patch, needs review] MPolynomial_polydict __floordiv__ wrong arithmetic

archive/issues_002594.json:
```json
{
    "body": "Assignee: @malb\n\nThe __floordiv__ special implementation for monomials throws away coefficients.\n\n\n```\nsage: R.<x,y,z>=ZZ[]\nsage: f=3*x^2-1\nsage: f//x\nx\n```\n\n\nA patch is attached to fix this along with some other coercion issues.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2594\n\n",
    "created_at": "2008-03-19T11:56:35Z",
    "labels": [
        "component: commutative algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "[with patch, needs review] MPolynomial_polydict __floordiv__ wrong arithmetic",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2594",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```
Assignee: @malb

The __floordiv__ special implementation for monomials throws away coefficients.


```
sage: R.<x,y,z>=ZZ[]
sage: f=3*x^2-1
sage: f//x
x
```


A patch is attached to fix this along with some other coercion issues.

Issue created by migration from https://trac.sagemath.org/ticket/2594





---

archive/issue_comments_017712.json:
```json
{
    "body": "Attachment [mpoly-div-bug.patch](tarball://root/attachments/some-uuid/ticket2594/mpoly-div-bug.patch) by @malb created at 2008-03-19 16:07:02\n\nPatch looks good.",
    "created_at": "2008-03-19T16:07:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2594",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2594#issuecomment-17712",
    "user": "https://github.com/malb"
}
```

Attachment [mpoly-div-bug.patch](tarball://root/attachments/some-uuid/ticket2594/mpoly-div-bug.patch) by @malb created at 2008-03-19 16:07:02

Patch looks good.



---

archive/issue_comments_017713.json:
```json
{
    "body": "Merged in Sage 2.11.alpha0",
    "created_at": "2008-03-19T23:38:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2594",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2594#issuecomment-17713",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.11.alpha0



---

archive/issue_comments_017714.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-19T23:38:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2594",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2594#issuecomment-17714",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
