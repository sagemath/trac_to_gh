# Issue 3500: [with patch, needs review] bug in cyclotomic linear algebra code

archive/issues_003500.json:
```json
{
    "body": "Assignee: @craigcitro\n\nWow, here's an embarrassing bug in the cyclotomic linear algebra code:\n\n\n```\nsage: cf4 = CyclotomicField(4) ; z4 = cf4.0\nsage: A = Matrix(cf4, 1, 2, [-z4, 1])\nsage: A.echelon_form()\n\n[1 0]\n[0 1]\n```\n\n\nThe attached patch fixes it. \n\nIssue created by migration from https://trac.sagemath.org/ticket/3500\n\n",
    "created_at": "2008-06-24T06:49:15Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "[with patch, needs review] bug in cyclotomic linear algebra code",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3500",
    "user": "@craigcitro"
}
```
Assignee: @craigcitro

Wow, here's an embarrassing bug in the cyclotomic linear algebra code:


```
sage: cf4 = CyclotomicField(4) ; z4 = cf4.0
sage: A = Matrix(cf4, 1, 2, [-z4, 1])
sage: A.echelon_form()

[1 0]
[0 1]
```


The attached patch fixes it. 

Issue created by migration from https://trac.sagemath.org/ticket/3500





---

archive/issue_comments_024690.json:
```json
{
    "body": "Attachment [trac-3500.patch](tarball://root/attachments/some-uuid/ticket3500/trac-3500.patch) by @ClementPernet created at 2008-06-24 23:37:58\n\nThis patch looks correct and fixes the bug. \nThe docstrings pass on 3.0.4alpha1.",
    "created_at": "2008-06-24T23:37:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3500#issuecomment-24690",
    "user": "@ClementPernet"
}
```

Attachment [trac-3500.patch](tarball://root/attachments/some-uuid/ticket3500/trac-3500.patch) by @ClementPernet created at 2008-06-24 23:37:58

This patch looks correct and fixes the bug. 
The docstrings pass on 3.0.4alpha1.



---

archive/issue_comments_024691.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha1",
    "created_at": "2008-06-25T01:09:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3500#issuecomment-24691",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.4.alpha1



---

archive/issue_comments_024692.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-25T01:09:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3500#issuecomment-24692",
    "user": "mabshoff"
}
```

Resolution: fixed
