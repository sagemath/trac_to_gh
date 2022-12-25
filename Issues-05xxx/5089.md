# Issue 5089: [with patch, positive review] add kernel method for sparse integer matrices

archive/issues_005089.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: sparse integer matrix kernel\n\n```\nsage: M = matrix(ZZ, 2, 3, [1,2,3,4,5,6])\nsage: M.kernel()\n```\nworks fine, while\n\n```\nsage: M = matrix(ZZ, 2, 3, [1,2,3,4,5,6], sparse=True)\nsage: M.kernel()\n```\ngives an error, `TypeError: Argument K (= Integer Ring) must be a field.`\n\nThe attached patch fixes this -- it adds a kernel method for sparse integer matrices, which just calls `self.dense_matrix().kernel(...)`.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5089\n\n",
    "closed_at": "2009-01-24T18:08:22Z",
    "created_at": "2009-01-24T16:29:12Z",
    "labels": [
        "component: linear algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[with patch, positive review] add kernel method for sparse integer matrices",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5089",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: @williamstein

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

archive/issue_comments_038702.json:
```json
{
    "body": "Attachment [5089.patch](tarball://root/attachments/some-uuid/ticket5089/5089.patch) by @jhpalmieri created at 2009-01-24 16:30:32",
    "created_at": "2009-01-24T16:30:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5089#issuecomment-38702",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [5089.patch](tarball://root/attachments/some-uuid/ticket5089/5089.patch) by @jhpalmieri created at 2009-01-24 16:30:32



---

archive/issue_comments_038703.json:
```json
{
    "body": "looks good.",
    "created_at": "2009-01-24T16:40:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5089#issuecomment-38703",
    "user": "https://github.com/williamstein"
}
```

looks good.



---

archive/issue_events_011744.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-24T18:08:22Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5089",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5089#event-11744"
}
```



---

archive/issue_comments_038704.json:
```json
{
    "body": "Merged in Sage 3.3.alpha2\n\nCheers,\n\nMichael",
    "created_at": "2009-01-24T18:08:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5089#issuecomment-38704",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha2

Cheers,

Michael



---

archive/issue_comments_038705.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-24T18:08:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5089#issuecomment-38705",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
