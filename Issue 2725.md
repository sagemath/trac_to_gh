# Issue 2725: [with patch, needs review] MPolynomial_polydict doc-tests and some refactoring

archive/issues_002725.json:
```json
{
    "body": "Assignee: @malb\n\nThe attached patch adds a number of features and refactorings:\n\n1. A new degrees method which returns the degrees of all the variables in one swoop (and has other useful purposes)\n\n2. More doc-tests\n\n3. ETuple helper function to eliminate fragile duplicate code\n\n4. Fix some latex/repr bugs with -1 (continuation of #291)\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2725\n\n",
    "created_at": "2008-03-29T19:54:16Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "[with patch, needs review] MPolynomial_polydict doc-tests and some refactoring",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2725",
    "user": "jbmohler"
}
```
Assignee: @malb

The attached patch adds a number of features and refactorings:

1. A new degrees method which returns the degrees of all the variables in one swoop (and has other useful purposes)

2. More doc-tests

3. ETuple helper function to eliminate fragile duplicate code

4. Fix some latex/repr bugs with -1 (continuation of #291)


Issue created by migration from https://trac.sagemath.org/ticket/2725





---

archive/issue_comments_018775.json:
```json
{
    "body": "Attachment [etuple2.patch](tarball://root/attachments/some-uuid/ticket2725/etuple2.patch) by jbmohler created at 2008-03-29 19:55:22",
    "created_at": "2008-03-29T19:55:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2725",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2725#issuecomment-18775",
    "user": "jbmohler"
}
```

Attachment [etuple2.patch](tarball://root/attachments/some-uuid/ticket2725/etuple2.patch) by jbmohler created at 2008-03-29 19:55:22



---

archive/issue_comments_018776.json:
```json
{
    "body": "Attachment [2725.patch](tarball://root/attachments/some-uuid/ticket2725/2725.patch) by @mwhansen created at 2008-03-29 20:08:16",
    "created_at": "2008-03-29T20:08:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2725",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2725#issuecomment-18776",
    "user": "@mwhansen"
}
```

Attachment [2725.patch](tarball://root/attachments/some-uuid/ticket2725/2725.patch) by @mwhansen created at 2008-03-29 20:08:16



---

archive/issue_comments_018777.json:
```json
{
    "body": "Looks good to me. I attached a new version of the patch which plays well with the changes in #2702.  Apply that first, and then apply 2725.patch.",
    "created_at": "2008-03-29T20:09:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2725",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2725#issuecomment-18777",
    "user": "@mwhansen"
}
```

Looks good to me. I attached a new version of the patch which plays well with the changes in #2702.  Apply that first, and then apply 2725.patch.



---

archive/issue_comments_018778.json:
```json
{
    "body": "Doctests pass with my current 2.11.rc0 merged tree, so I will merge this.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-29T22:15:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2725",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2725#issuecomment-18778",
    "user": "mabshoff"
}
```

Doctests pass with my current 2.11.rc0 merged tree, so I will merge this.

Cheers,

Michael



---

archive/issue_comments_018779.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-29T22:15:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2725",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2725#issuecomment-18779",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_018780.json:
```json
{
    "body": "Merged in Sage 2.11.rc0",
    "created_at": "2008-03-29T22:15:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2725",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2725#issuecomment-18780",
    "user": "mabshoff"
}
```

Merged in Sage 2.11.rc0
