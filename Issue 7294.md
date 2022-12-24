# Issue 7294: Degree constrained subgraph

archive/issues_007294.json:
```json
{
    "body": "Assignee: rlm\n\nThere should be a way in Sage to find a degree-constrained subgraph. This should be done through LP ( there may be a better way to do it, but I am not aware of it )\n\nIssue created by migration from https://trac.sagemath.org/ticket/7294\n\n",
    "created_at": "2009-10-25T09:26:41Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "title": "Degree constrained subgraph",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7294",
    "user": "ncohen"
}
```
Assignee: rlm

There should be a way in Sage to find a degree-constrained subgraph. This should be done through LP ( there may be a better way to do it, but I am not aware of it )

Issue created by migration from https://trac.sagemath.org/ticket/7294





---

archive/issue_comments_060727.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-01T17:07:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7294#issuecomment-60727",
    "user": "ncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_060728.json:
```json
{
    "body": "Attachment [trac_7294.patch](tarball://root/attachments/some-uuid/ticket7294/trac_7294.patch) by ncohen created at 2009-11-01 17:08:53",
    "created_at": "2009-11-01T17:08:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7294#issuecomment-60728",
    "user": "ncohen"
}
```

Attachment [trac_7294.patch](tarball://root/attachments/some-uuid/ticket7294/trac_7294.patch) by ncohen created at 2009-11-01 17:08:53



---

archive/issue_comments_060729.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-15T17:10:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7294#issuecomment-60729",
    "user": "rlm"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_060730.json:
```json
{
    "body": "This looks good to me. I should note that you can use `if bounds is None`, since in Python the None type is unique.",
    "created_at": "2009-12-15T17:10:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7294#issuecomment-60730",
    "user": "rlm"
}
```

This looks good to me. I should note that you can use `if bounds is None`, since in Python the None type is unique.



---

archive/issue_comments_060731.json:
```json
{
    "body": "Attachment [trac_7294-fix.patch](tarball://root/attachments/some-uuid/ticket7294/trac_7294-fix.patch) by mhansen created at 2009-12-15 17:52:21",
    "created_at": "2009-12-15T17:52:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7294#issuecomment-60731",
    "user": "mhansen"
}
```

Attachment [trac_7294-fix.patch](tarball://root/attachments/some-uuid/ticket7294/trac_7294-fix.patch) by mhansen created at 2009-12-15 17:52:21



---

archive/issue_comments_060732.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-15T17:52:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7294#issuecomment-60732",
    "user": "mhansen"
}
```

Resolution: fixed



---

archive/issue_comments_060733.json:
```json
{
    "body": "I merged both patches above.",
    "created_at": "2009-12-15T17:52:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7294#issuecomment-60733",
    "user": "mhansen"
}
```

I merged both patches above.
