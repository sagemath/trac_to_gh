# Issue 5089: [with patch, needs review] add kernel method for sparse integer matrices

archive/issues_005089.json:
```json
{
    "body": "Assignee: was\n\nKeywords: sparse integer matrix kernel\n\n\n```\nsage: M = matrix(ZZ, 2, 3, [1,2,3,4,5,6])\nsage: M.kernel()\n```\n\nworks fine, while\n\n```\nsage: M = matrix(ZZ, 2, 3, [1,2,3,4,5,6], sparse=True)\nsage: M.kernel()\n```\n\ngives an error, `TypeError: Argument K (= Integer Ring) must be a field.`\n\nThe attached patch fixes this -- it adds a kernel method for sparse integer matrices, which just calls `self.dense_matrix().kernel(...)`.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5089\n\n",
    "created_at": "2009-01-24T16:29:12Z",
    "labels": [
        "linear algebra",
        "minor",
        "bug"
    ],
    "title": "[with patch, needs review] add kernel method for sparse integer matrices",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5089",
    "user": "jhpalmieri"
}
```
Assignee: was

Keywords: sparse integer matrix kernel


```
sage: M = matrix(ZZ, 2, 3, [1,2,3,4,5,6])
sage: M.kernel()
```

works fine, while

```
sage: M = matrix(ZZ, 2, 3, [1,2,3,4,5,6], sparse=True)
sage: M.kernel()
```

gives an error, `TypeError: Argument K (= Integer Ring) must be a field.`

The attached patch fixes this -- it adds a kernel method for sparse integer matrices, which just calls `self.dense_matrix().kernel(...)`.



Issue created by migration from https://trac.sagemath.org/ticket/5089





---

archive/issue_comments_038776.json:
```json
{
    "body": "Attachment [5089.patch](tarball://root/attachments/some-uuid/ticket5089/5089.patch) by jhpalmieri created at 2009-01-24 16:30:32",
    "created_at": "2009-01-24T16:30:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5089#issuecomment-38776",
    "user": "jhpalmieri"
}
```

Attachment [5089.patch](tarball://root/attachments/some-uuid/ticket5089/5089.patch) by jhpalmieri created at 2009-01-24 16:30:32



---

archive/issue_comments_038777.json:
```json
{
    "body": "looks good.",
    "created_at": "2009-01-24T16:40:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5089#issuecomment-38777",
    "user": "was"
}
```

looks good.



---

archive/issue_comments_038778.json:
```json
{
    "body": "Merged in Sage 3.3.alpha2\n\nCheers,\n\nMichael",
    "created_at": "2009-01-24T18:08:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5089#issuecomment-38778",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha2

Cheers,

Michael



---

archive/issue_comments_038779.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-24T18:08:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5089#issuecomment-38779",
    "user": "mabshoff"
}
```

Resolution: fixed
