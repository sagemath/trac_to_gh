# Issue 9093: is_square broken for constant polynomials

archive/issues_009093.json:
```json
{
    "body": "Assignee: @aghitza\n\n\n```\nsage: R.<x> = QQ[]\nsage: R(1).is_square()\nFalse\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9093\n\n",
    "created_at": "2010-05-30T08:37:36Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.3",
    "title": "is_square broken for constant polynomials",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9093",
    "user": "https://github.com/robertwb"
}
```
Assignee: @aghitza


```
sage: R.<x> = QQ[]
sage: R(1).is_square()
False
```



Issue created by migration from https://trac.sagemath.org/ticket/9093





---

archive/issue_comments_084318.json:
```json
{
    "body": "Attachment [9093-poly-is_square.patch](tarball://root/attachments/some-uuid/ticket9093/9093-poly-is_square.patch) by @robertwb created at 2010-05-30 08:44:15",
    "created_at": "2010-05-30T08:44:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9093",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9093#issuecomment-84318",
    "user": "https://github.com/robertwb"
}
```

Attachment [9093-poly-is_square.patch](tarball://root/attachments/some-uuid/ticket9093/9093-poly-is_square.patch) by @robertwb created at 2010-05-30 08:44:15



---

archive/issue_comments_084319.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-30T08:45:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9093",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9093#issuecomment-84319",
    "user": "https://github.com/robertwb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_084320.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2010-05-30T09:28:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9093",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9093#issuecomment-84320",
    "user": "https://github.com/robertwb"
}
```

Changing priority from major to critical.



---

archive/issue_comments_084321.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-02T14:37:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9093",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9093#issuecomment-84321",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084322.json:
```json
{
    "body": "Patch applied fine to 4.4.3.alpha0.  Code looks fine, and all tests in sage/rings/polynomial pass.\n\nNote (needs another ticket?)   I do not think that this is correct:\n\n```\nsage: R.<x> = ZZ[]\nsage: R(100).squarefree_decomposition()\n100\n```\n\nBut it works better now than it did before by a long way, so I will give this a positive review and suggest that another ticket is opened.",
    "created_at": "2010-06-02T14:37:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9093",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9093#issuecomment-84322",
    "user": "https://github.com/JohnCremona"
}
```

Patch applied fine to 4.4.3.alpha0.  Code looks fine, and all tests in sage/rings/polynomial pass.

Note (needs another ticket?)   I do not think that this is correct:

```
sage: R.<x> = ZZ[]
sage: R(100).squarefree_decomposition()
100
```

But it works better now than it did before by a long way, so I will give this a positive review and suggest that another ticket is opened.



---

archive/issue_comments_084323.json:
```json
{
    "body": "Thanks! As with factoring, we don't decompose the unit part. There should probably be at least a note about this.",
    "created_at": "2010-06-02T17:28:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9093",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9093#issuecomment-84323",
    "user": "https://github.com/robertwb"
}
```

Thanks! As with factoring, we don't decompose the unit part. There should probably be at least a note about this.



---

archive/issue_comments_084324.json:
```json
{
    "body": "My point was that in ZZ[X], as opposed to QQ[X], 100 is *not* a unit factor so should be included in the squarefree factorization.  It would have to be done differently, of course (and Integers don't have a squarefree_decomposition method, presumably because over ZZ there is no known algorithm which avoids factoring).",
    "created_at": "2010-06-02T19:53:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9093",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9093#issuecomment-84324",
    "user": "https://github.com/JohnCremona"
}
```

My point was that in ZZ[X], as opposed to QQ[X], 100 is *not* a unit factor so should be included in the squarefree factorization.  It would have to be done differently, of course (and Integers don't have a squarefree_decomposition method, presumably because over ZZ there is no known algorithm which avoids factoring).



---

archive/issue_comments_084325.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-03T04:33:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9093",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9093#issuecomment-84325",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
