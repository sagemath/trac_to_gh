# Issue 3501: [with patch, needs review] charpoly of zero matrix over a cyclotomic field fails

archive/issues_003501.json:
```json
{
    "body": "Assignee: @craigcitro\n\nThis is broken:\n\n\n```\nsage: Matrix(CyclotomicField(13),3).charpoly()\n```\n\n\nThe attached patch fixes it.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3501\n\n",
    "created_at": "2008-06-24T07:51:07Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "[with patch, needs review] charpoly of zero matrix over a cyclotomic field fails",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3501",
    "user": "@craigcitro"
}
```
Assignee: @craigcitro

This is broken:


```
sage: Matrix(CyclotomicField(13),3).charpoly()
```


The attached patch fixes it.

Issue created by migration from https://trac.sagemath.org/ticket/3501





---

archive/issue_comments_024693.json:
```json
{
    "body": "Attachment [trac-3501.patch](tarball://root/attachments/some-uuid/ticket3501/trac-3501.patch) by @craigcitro created at 2008-06-24 07:51:58",
    "created_at": "2008-06-24T07:51:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3501#issuecomment-24693",
    "user": "@craigcitro"
}
```

Attachment [trac-3501.patch](tarball://root/attachments/some-uuid/ticket3501/trac-3501.patch) by @craigcitro created at 2008-06-24 07:51:58



---

archive/issue_comments_024694.json:
```json
{
    "body": "This patch looks good and fixes the bug. \nI have run the doctest on 3.0.4alpha1, and they pass.",
    "created_at": "2008-06-24T23:12:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3501#issuecomment-24694",
    "user": "@ClementPernet"
}
```

This patch looks good and fixes the bug. 
I have run the doctest on 3.0.4alpha1, and they pass.



---

archive/issue_comments_024695.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-25T01:09:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3501#issuecomment-24695",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_024696.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha1",
    "created_at": "2008-06-25T01:09:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3501#issuecomment-24696",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.4.alpha1
