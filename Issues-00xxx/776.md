# Issue 776: kernel of linear homomorphism fails

archive/issues_000776.json:
```json
{
    "body": "Assignee: @williamstein\n\n```\nV=VectorSpace(QQ,3)\nid=V.Hom(V)(identity_matrix(QQ,3))\nnull=V.Hom(V)(0*identity_matrix(QQ,3))\nid.kernel()\n```\nproduces\n\n```\n<type 'exceptions.TypeError'>: entries must be coercible to a list or integer\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/776\n\n",
    "closed_at": "2007-10-01T21:44:35Z",
    "created_at": "2007-10-01T21:28:02Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.6",
    "title": "kernel of linear homomorphism fails",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/776",
    "user": "https://github.com/nbruin"
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

archive/issue_comments_004617.json:
```json
{
    "body": "Attachment [6551.patch](tarball://root/attachments/some-uuid/ticket776/6551.patch) by @williamstein created at 2007-10-01 21:44:04\n\nfixes the bug",
    "created_at": "2007-10-01T21:44:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/776#issuecomment-4617",
    "user": "https://github.com/williamstein"
}
```

Attachment [6551.patch](tarball://root/attachments/some-uuid/ticket776/6551.patch) by @williamstein created at 2007-10-01 21:44:04

fixes the bug



---

archive/issue_events_002138.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-01T21:44:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/776",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/776#event-2138"
}
```



---

archive/issue_events_002139.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-01T21:44:35Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/776",
    "milestone": "sage-2.8.6",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/776#event-2139"
}
```



---

archive/issue_comments_004618.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-01T21:44:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/776#issuecomment-4618",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_004619.json:
```json
{
    "body": "Attachment [correct_fix.patch](tarball://root/attachments/some-uuid/ticket776/correct_fix.patch) by @williamstein created at 2007-10-02 03:08:08",
    "created_at": "2007-10-02T03:08:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/776#issuecomment-4619",
    "user": "https://github.com/williamstein"
}
```

Attachment [correct_fix.patch](tarball://root/attachments/some-uuid/ticket776/correct_fix.patch) by @williamstein created at 2007-10-02 03:08:08



---

archive/issue_comments_004620.json:
```json
{
    "body": "I screwed up fixing this.   Apply the correct_fix.patch after the other.  Now this is fixed.",
    "created_at": "2007-10-02T03:08:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/776#issuecomment-4620",
    "user": "https://github.com/williamstein"
}
```

I screwed up fixing this.   Apply the correct_fix.patch after the other.  Now this is fixed.
