# Issue 913: real_roots code fails if polynomial obviously has no roots

archive/issues_000913.json:
```json
{
    "body": "Assignee: cwitty\n\nThe following test case will loop forever:\n\n```\nsage: x = polygen(ZZ)\nsage: (x^2 + 1).real_root_intervals()\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/913\n\n",
    "created_at": "2007-10-17T15:38:15Z",
    "labels": [
        "numerical",
        "major",
        "bug"
    ],
    "title": "real_roots code fails if polynomial obviously has no roots",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/913",
    "user": "cwitty"
}
```
Assignee: cwitty

The following test case will loop forever:

```
sage: x = polygen(ZZ)
sage: (x^2 + 1).real_root_intervals()
```



Issue created by migration from https://trac.sagemath.org/ticket/913





---

archive/issue_comments_005605.json:
```json
{
    "body": "Attachment [7002.patch](tarball://root/attachments/some-uuid/ticket913/7002.patch) by cwitty created at 2007-10-20 17:19:19\n\nFixed.",
    "created_at": "2007-10-20T17:19:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/913#issuecomment-5605",
    "user": "cwitty"
}
```

Attachment [7002.patch](tarball://root/attachments/some-uuid/ticket913/7002.patch) by cwitty created at 2007-10-20 17:19:19

Fixed.



---

archive/issue_comments_005606.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-21T00:49:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/913#issuecomment-5606",
    "user": "was"
}
```

Resolution: fixed
