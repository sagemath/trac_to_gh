# Issue 9344: matrix constructor does not honor nrows if given a method to generate the entries

archive/issues_009344.json:
```json
{
    "body": "Assignee: @aghitza\n\nThe is a bug in the matrix constructor. If the entries are given by a method, the output matrix is always square of dimension ncols\n\n\n```\nsage: matrix(QQ, 1, 3, lambda x,y: x)\n[0 0 0]\n[1 1 1]\n[2 2 2]\nsage: sage: matrix(QQ, 3, 1, lambda x,y: x)\n[0]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9344\n\n",
    "created_at": "2010-06-26T10:13:59Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "matrix constructor does not honor nrows if given a method to generate the entries",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9344",
    "user": "https://github.com/lftabera"
}
```
Assignee: @aghitza

The is a bug in the matrix constructor. If the entries are given by a method, the output matrix is always square of dimension ncols


```
sage: matrix(QQ, 1, 3, lambda x,y: x)
[0 0 0]
[1 1 1]
[2 2 2]
sage: sage: matrix(QQ, 3, 1, lambda x,y: x)
[0]
```


Issue created by migration from https://trac.sagemath.org/ticket/9344





---

archive/issue_comments_088555.json:
```json
{
    "body": "Attachment [matrices.patch](tarball://root/attachments/some-uuid/ticket9344/matrices.patch) by @lftabera created at 2010-06-26 10:14:08",
    "created_at": "2010-06-26T10:14:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9344#issuecomment-88555",
    "user": "https://github.com/lftabera"
}
```

Attachment [matrices.patch](tarball://root/attachments/some-uuid/ticket9344/matrices.patch) by @lftabera created at 2010-06-26 10:14:08



---

archive/issue_comments_088556.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-26T10:15:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9344#issuecomment-88556",
    "user": "https://github.com/lftabera"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_088557.json:
```json
{
    "body": "Looks fine and all doctests pass. Positive review.",
    "created_at": "2010-06-29T14:36:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9344#issuecomment-88557",
    "user": "https://github.com/loefflerd"
}
```

Looks fine and all doctests pass. Positive review.



---

archive/issue_comments_088558.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-29T14:36:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9344#issuecomment-88558",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_088559.json:
```json
{
    "body": "Attachment [trac_9344-matrix_constructor_bug.patch](tarball://root/attachments/some-uuid/ticket9344/trac_9344-matrix_constructor_bug.patch) by @loefflerd created at 2010-06-30 08:56:04\n\napply this patch -- identical code but with more informative hg header information",
    "created_at": "2010-06-30T08:56:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9344#issuecomment-88559",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_9344-matrix_constructor_bug.patch](tarball://root/attachments/some-uuid/ticket9344/trac_9344-matrix_constructor_bug.patch) by @loefflerd created at 2010-06-30 08:56:04

apply this patch -- identical code but with more informative hg header information



---

archive/issue_comments_088560.json:
```json
{
    "body": "Just an afterthought: I noticed while cleaning up my hg queue that this patch doesn't have a very informative name and also there is essentially no information in the hg header. This makes the release maintainer's job harder (they have to keep track of hundreds of patches and remember what to attribute to whom in the release notes). I've uploaded a patch functionally identical to yours, but with your full username and a more informative filename and commit message.",
    "created_at": "2010-06-30T08:58:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9344#issuecomment-88560",
    "user": "https://github.com/loefflerd"
}
```

Just an afterthought: I noticed while cleaning up my hg queue that this patch doesn't have a very informative name and also there is essentially no information in the hg header. This makes the release maintainer's job harder (they have to keep track of hundreds of patches and remember what to attribute to whom in the release notes). I've uploaded a patch functionally identical to yours, but with your full username and a more informative filename and commit message.



---

archive/issue_comments_088561.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-20T09:30:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9344#issuecomment-88561",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_023049.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-07-20T09:30:38Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9344",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9344#event-23049"
}
```
