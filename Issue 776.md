# Issue 776: kernel of linear homomorphism fails

archive/issues_000776.json:
```json
{
    "body": "Assignee: was\n\n\n```\nV=VectorSpace(QQ,3)\nid=V.Hom(V)(identity_matrix(QQ,3))\nnull=V.Hom(V)(0*identity_matrix(QQ,3))\nid.kernel()\n```\n\nproduces\n\n```\n<type 'exceptions.TypeError'>: entries must be coercible to a list or integer\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/776\n\n",
    "created_at": "2007-10-01T21:28:02Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "title": "kernel of linear homomorphism fails",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/776",
    "user": "nbruin"
}
```
Assignee: was


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
    "body": "Attachment\n\nfixes the bug",
    "created_at": "2007-10-01T21:44:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/776#issuecomment-4633",
    "user": "was"
}
```

Attachment

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
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_004635.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-10-02T03:08:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/776#issuecomment-4635",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_004636.json:
```json
{
    "body": "I screwed up fixing this.   Apply the correct_fix.patch after the other.  Now this is fixed.",
    "created_at": "2007-10-02T03:08:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/776#issuecomment-4636",
    "user": "was"
}
```

I screwed up fixing this.   Apply the correct_fix.patch after the other.  Now this is fixed.
