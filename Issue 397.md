# Issue 397: ZZ.digits(base) and inverse

archive/issues_000397.json:
```json
{
    "body": "Assignee: somebody\n\nThe attache file is a patch to allow the following code to work:\n\n```\nsage: e = 7\nsage: e.digits(2)\n[1, 1, 1]\nsage: e.digits(3)\n[1, 2]\nsage: e.digits(10)\n[7]\nsage: ZZ(e.digits(3),3)\n7\n```\n\nThe return type of ZZ.digits() is a list with Integer entries in little endian order.\n\nIssue created by migration from https://trac.sagemath.org/ticket/397\n\n",
    "created_at": "2007-06-30T18:27:03Z",
    "labels": [
        "basic arithmetic",
        "trivial",
        "enhancement"
    ],
    "title": "ZZ.digits(base) and inverse",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/397",
    "user": "malb"
}
```
Assignee: somebody

The attache file is a patch to allow the following code to work:

```
sage: e = 7
sage: e.digits(2)
[1, 1, 1]
sage: e.digits(3)
[1, 2]
sage: e.digits(10)
[7]
sage: ZZ(e.digits(3),3)
7
```

The return type of ZZ.digits() is a list with Integer entries in little endian order.

Issue created by migration from https://trac.sagemath.org/ticket/397





---

archive/issue_comments_001953.json:
```json
{
    "body": "main patch",
    "created_at": "2007-06-30T18:27:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/397",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/397#issuecomment-1953",
    "user": "malb"
}
```

main patch



---

archive/issue_comments_001954.json:
```json
{
    "body": "Attachment [4867.patch](tarball://root/attachments/some-uuid/ticket397/4867.patch) by malb created at 2007-06-30 20:08:33\n\nfollow-up patch for faster ZZ.digits()",
    "created_at": "2007-06-30T20:08:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/397",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/397#issuecomment-1954",
    "user": "malb"
}
```

Attachment [4867.patch](tarball://root/attachments/some-uuid/ticket397/4867.patch) by malb created at 2007-06-30 20:08:33

follow-up patch for faster ZZ.digits()



---

archive/issue_comments_001955.json:
```json
{
    "body": "Attachment [4868.patch](tarball://root/attachments/some-uuid/ticket397/4868.patch) by malb created at 2007-06-30 20:11:14\n\nAdded follow-up patch based on William's input.",
    "created_at": "2007-06-30T20:11:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/397",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/397#issuecomment-1955",
    "user": "malb"
}
```

Attachment [4868.patch](tarball://root/attachments/some-uuid/ticket397/4868.patch) by malb created at 2007-06-30 20:11:14

Added follow-up patch based on William's input.



---

archive/issue_comments_001956.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-09T13:32:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/397",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/397#issuecomment-1956",
    "user": "malb"
}
```

Resolution: fixed
