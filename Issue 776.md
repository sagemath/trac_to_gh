# Issue 776: kernel of linear homomorphism fails

archive/issues_000776.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nV=VectorSpace(QQ,3)\nid=V.Hom(V)(identity_matrix(QQ,3))\nnull=V.Hom(V)(0*identity_matrix(QQ,3))\nid.kernel()\n```\n\nproduces\n\n```\n<type 'exceptions.TypeError'>: entries must be coercible to a list or integer\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/776\n\n",
    "created_at": "2007-10-01T21:28:02Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.6",
    "title": "kernel of linear homomorphism fails",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/776",
    "user": "@nbruin"
}
```
Assignee: @williamstein


```
V=VectorSpace(QQ,3)
id=V.Hom(V)(identity_matrix(QQ,3))
null=V.Hom(V)(0*identity_matrix(QQ,3))
id.kernel()
```

produces

```
<type 'exceptions.TypeError'>: entries must be coercible to a list or integer
```



Issue created by migration from https://trac.sagemath.org/ticket/776





---

archive/issue_comments_004633.json:
```json
{
    "body": "Attachment [6551.patch](tarball://root/attachments/some-uuid/ticket776/6551.patch) by @williamstein created at 2007-10-01 21:44:04\n\nfixes the bug",
    "created_at": "2007-10-01T21:44:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/776#issuecomment-4633",
    "user": "@williamstein"
}
```

Attachment [6551.patch](tarball://root/attachments/some-uuid/ticket776/6551.patch) by @williamstein created at 2007-10-01 21:44:04

fixes the bug



---

archive/issue_comments_004634.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-01T21:44:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/776#issuecomment-4634",
    "user": "@williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_004635.json:
```json
{
    "body": "Attachment [correct_fix.patch](tarball://root/attachments/some-uuid/ticket776/correct_fix.patch) by @williamstein created at 2007-10-02 03:08:08",
    "created_at": "2007-10-02T03:08:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/776#issuecomment-4635",
    "user": "@williamstein"
}
```

Attachment [correct_fix.patch](tarball://root/attachments/some-uuid/ticket776/correct_fix.patch) by @williamstein created at 2007-10-02 03:08:08



---

archive/issue_comments_004636.json:
```json
{
    "body": "I screwed up fixing this.   Apply the correct_fix.patch after the other.  Now this is fixed.",
    "created_at": "2007-10-02T03:08:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/776#issuecomment-4636",
    "user": "@williamstein"
}
```

I screwed up fixing this.   Apply the correct_fix.patch after the other.  Now this is fixed.
