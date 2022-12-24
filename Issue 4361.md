# Issue 4361: [with patch, needs review] poles of gamma on integers

archive/issues_004361.json:
```json
{
    "body": "Assignee: burcin\n\nIn 3.1.4 we have:\n\n\n```\nsage: gamma(-1)\n+Infinity\nsage: gamma(-2)\n-Infinity\n```\n\n\nThe poles should return unsigned infinity.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4361\n\n",
    "created_at": "2008-10-24T09:50:25Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] poles of gamma on integers",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4361",
    "user": "burcin"
}
```
Assignee: burcin

In 3.1.4 we have:


```
sage: gamma(-1)
+Infinity
sage: gamma(-2)
-Infinity
```


The poles should return unsigned infinity.

Issue created by migration from https://trac.sagemath.org/ticket/4361





---

archive/issue_comments_032041.json:
```json
{
    "body": "Attachment [integer_gamma_poles.patch](tarball://root/attachments/some-uuid/ticket4361/integer_gamma_poles.patch) by robertwb created at 2008-10-30 21:37:58",
    "created_at": "2008-10-30T21:37:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4361",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4361#issuecomment-32041",
    "user": "robertwb"
}
```

Attachment [integer_gamma_poles.patch](tarball://root/attachments/some-uuid/ticket4361/integer_gamma_poles.patch) by robertwb created at 2008-10-30 21:37:58



---

archive/issue_comments_032042.json:
```json
{
    "body": "Merged in Sage 3.2.alpha2",
    "created_at": "2008-10-31T01:33:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4361",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4361#issuecomment-32042",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.alpha2



---

archive/issue_comments_032043.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-31T01:33:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4361",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4361#issuecomment-32043",
    "user": "mabshoff"
}
```

Resolution: fixed
