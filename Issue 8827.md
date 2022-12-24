# Issue 8827: Cache heights of points on elliptic curves

archive/issues_008827.json:
```json
{
    "body": "Assignee: cremona\n\nI've found myself taking the height of the same points over and over again, and have been starting to wish they were cached (especially over number fields). This patch does it. \n\nIssue created by migration from https://trac.sagemath.org/ticket/8827\n\n",
    "created_at": "2010-04-30T06:38:15Z",
    "labels": [
        "elliptic curves",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.2",
    "title": "Cache heights of points on elliptic curves",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8827",
    "user": "robertwb"
}
```
Assignee: cremona

I've found myself taking the height of the same points over and over again, and have been starting to wish they were cached (especially over number fields). This patch does it. 

Issue created by migration from https://trac.sagemath.org/ticket/8827





---

archive/issue_comments_081057.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-30T06:39:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8827#issuecomment-81057",
    "user": "robertwb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_081058.json:
```json
{
    "body": "Attachment [8827-point-height-cache.patch](tarball://root/attachments/some-uuid/ticket8827/8827-point-height-cache.patch) by robertwb created at 2010-04-30 06:39:41",
    "created_at": "2010-04-30T06:39:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8827#issuecomment-81058",
    "user": "robertwb"
}
```

Attachment [8827-point-height-cache.patch](tarball://root/attachments/some-uuid/ticket8827/8827-point-height-cache.patch) by robertwb created at 2010-04-30 06:39:41



---

archive/issue_comments_081059.json:
```json
{
    "body": "I can't believe that we never cached heights before!  (Perhaps we did when they were only implemented over QQ, but I'm not going to go back and check).\n\nNote that this is one case where the caching is slightly less trivial since we need to recompute of the desired precision is > the cached precision.  The patched code does that properly.\n\nApplies fine to 4.4 and all elliptic_curves tests pass.",
    "created_at": "2010-04-30T08:17:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8827#issuecomment-81059",
    "user": "cremona"
}
```

I can't believe that we never cached heights before!  (Perhaps we did when they were only implemented over QQ, but I'm not going to go back and check).

Note that this is one case where the caching is slightly less trivial since we need to recompute of the desired precision is > the cached precision.  The patched code does that properly.

Applies fine to 4.4 and all elliptic_curves tests pass.



---

archive/issue_comments_081060.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-30T08:17:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8827#issuecomment-81060",
    "user": "cremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_081061.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-08T21:55:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8827#issuecomment-81061",
    "user": "mvngu"
}
```

Resolution: fixed
