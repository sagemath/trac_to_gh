# Issue 7531: Python interface to M4RI's LQUP function

archive/issues_007531.json:
```json
{
    "body": "Assignee: @williamstein\n\nAll this patch does is to add a Python interface to `mzd_lqup` which might be handy for some people. It doesn't have any impact on existing functions etc. and thus should be a fairly low risk merge.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7531\n\n",
    "created_at": "2009-11-25T17:49:48Z",
    "labels": [
        "linear algebra",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "Python interface to M4RI's LQUP function",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7531",
    "user": "@malb"
}
```
Assignee: @williamstein

All this patch does is to add a Python interface to `mzd_lqup` which might be handy for some people. It doesn't have any impact on existing functions etc. and thus should be a fairly low risk merge.

Issue created by migration from https://trac.sagemath.org/ticket/7531





---

archive/issue_comments_063838.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-25T17:50:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7531",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7531#issuecomment-63838",
    "user": "@malb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_063839.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-11-26T02:00:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7531",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7531#issuecomment-63839",
    "user": "ylchapuy"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_063840.json:
```json
{
    "body": "Just a small remark: there is no mmpf algorithm available, this should be removed from the docstring.\n\n(and it needs #7375 ...)",
    "created_at": "2009-11-26T02:00:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7531",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7531#issuecomment-63840",
    "user": "ylchapuy"
}
```

Just a small remark: there is no mmpf algorithm available, this should be removed from the docstring.

(and it needs #7375 ...)



---

archive/issue_comments_063841.json:
```json
{
    "body": "Fixed in updated patch.",
    "created_at": "2009-11-26T12:18:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7531",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7531#issuecomment-63841",
    "user": "@malb"
}
```

Fixed in updated patch.



---

archive/issue_comments_063842.json:
```json
{
    "body": "typo in the pxd: assymptotically\n\nisn't it recommended to add a doctest for each algorithm?\nmaybe just add `lqup(A)==lqup(A,algorithm=\"naive\")` and `lqup(A)==lqup(A,algorithm=\"mmpf\")`",
    "created_at": "2009-11-26T12:56:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7531",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7531#issuecomment-63842",
    "user": "ylchapuy"
}
```

typo in the pxd: assymptotically

isn't it recommended to add a doctest for each algorithm?
maybe just add `lqup(A)==lqup(A,algorithm="naive")` and `lqup(A)==lqup(A,algorithm="mmpf")`



---

archive/issue_comments_063843.json:
```json
{
    "body": "Attachment [m4ri_lqup.patch](tarball://root/attachments/some-uuid/ticket7531/m4ri_lqup.patch) by @malb created at 2009-11-26 14:56:05\n\nThanks, fixed.",
    "created_at": "2009-11-26T14:56:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7531",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7531#issuecomment-63843",
    "user": "@malb"
}
```

Attachment [m4ri_lqup.patch](tarball://root/attachments/some-uuid/ticket7531/m4ri_lqup.patch) by @malb created at 2009-11-26 14:56:05

Thanks, fixed.



---

archive/issue_comments_063844.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-26T14:56:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7531",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7531#issuecomment-63844",
    "user": "@malb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_063845.json:
```json
{
    "body": "seems good to me now :)",
    "created_at": "2009-11-26T16:34:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7531",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7531#issuecomment-63845",
    "user": "ylchapuy"
}
```

seems good to me now :)



---

archive/issue_comments_063846.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-26T16:34:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7531",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7531#issuecomment-63846",
    "user": "ylchapuy"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063847.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-29T05:50:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7531",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7531#issuecomment-63847",
    "user": "@mwhansen"
}
```

Resolution: fixed
