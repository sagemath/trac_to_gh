# Issue 7294: Degree constrained subgraph

archive/issues_007294.json:
```json
{
    "body": "Assignee: @rlmill\n\nThere should be a way in Sage to find a degree-constrained subgraph. This should be done through LP ( there may be a better way to do it, but I am not aware of it )\n\nIssue created by migration from https://trac.sagemath.org/ticket/7294\n\n",
    "created_at": "2009-10-25T09:26:41Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "Degree constrained subgraph",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7294",
    "user": "https://github.com/nathanncohen"
}
```
Assignee: @rlmill

There should be a way in Sage to find a degree-constrained subgraph. This should be done through LP ( there may be a better way to do it, but I am not aware of it )

Issue created by migration from https://trac.sagemath.org/ticket/7294





---

archive/issue_comments_060614.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-01T17:07:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7294#issuecomment-60614",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_060615.json:
```json
{
    "body": "Attachment [trac_7294.patch](tarball://root/attachments/some-uuid/ticket7294/trac_7294.patch) by @nathanncohen created at 2009-11-01 17:08:53",
    "created_at": "2009-11-01T17:08:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7294#issuecomment-60615",
    "user": "https://github.com/nathanncohen"
}
```

Attachment [trac_7294.patch](tarball://root/attachments/some-uuid/ticket7294/trac_7294.patch) by @nathanncohen created at 2009-11-01 17:08:53



---

archive/issue_comments_060616.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-15T17:10:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7294#issuecomment-60616",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_060617.json:
```json
{
    "body": "This looks good to me. I should note that you can use `if bounds is None`, since in Python the None type is unique.",
    "created_at": "2009-12-15T17:10:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7294#issuecomment-60617",
    "user": "https://github.com/rlmill"
}
```

This looks good to me. I should note that you can use `if bounds is None`, since in Python the None type is unique.



---

archive/issue_comments_060618.json:
```json
{
    "body": "Attachment [trac_7294-fix.patch](tarball://root/attachments/some-uuid/ticket7294/trac_7294-fix.patch) by @mwhansen created at 2009-12-15 17:52:21",
    "created_at": "2009-12-15T17:52:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7294#issuecomment-60618",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_7294-fix.patch](tarball://root/attachments/some-uuid/ticket7294/trac_7294-fix.patch) by @mwhansen created at 2009-12-15 17:52:21



---

archive/issue_comments_060619.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-15T17:52:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7294#issuecomment-60619",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_060620.json:
```json
{
    "body": "I merged both patches above.",
    "created_at": "2009-12-15T17:52:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7294#issuecomment-60620",
    "user": "https://github.com/mwhansen"
}
```

I merged both patches above.
