# Issue 7919: Doctest in sage/misc/test_class_pickling.py doesn't test anything

archive/issues_007919.json:
```json
{
    "body": "Assignee: @nthiery\n\nCC:  @nthiery\n\nThere's a doctest in `sage/misc/test_class_pickling.py` that doesn't actually test anything. I was a reviewer for this patch, which means it's my bad for letting it through. Of course, this code gets tested anyway, so it's not so serious, but we should fix it anyway. Patch attached.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7919\n\n",
    "created_at": "2010-01-13T09:40:22Z",
    "labels": [
        "component: categories",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "Doctest in sage/misc/test_class_pickling.py doesn't test anything",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7919",
    "user": "https://github.com/craigcitro"
}
```
Assignee: @nthiery

CC:  @nthiery

There's a doctest in `sage/misc/test_class_pickling.py` that doesn't actually test anything. I was a reviewer for this patch, which means it's my bad for letting it through. Of course, this code gets tested anyway, so it's not so serious, but we should fix it anyway. Patch attached.

Issue created by migration from https://trac.sagemath.org/ticket/7919





---

archive/issue_comments_068783.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-13T09:43:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7919#issuecomment-68783",
    "user": "https://github.com/craigcitro"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_068784.json:
```json
{
    "body": "Attachment [trac_7919.patch](tarball://root/attachments/some-uuid/ticket7919/trac_7919.patch) by @craigcitro created at 2010-01-13 09:43:37",
    "created_at": "2010-01-13T09:43:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7919#issuecomment-68784",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac_7919.patch](tarball://root/attachments/some-uuid/ticket7919/trac_7919.patch) by @craigcitro created at 2010-01-13 09:43:37



---

archive/issue_comments_068785.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-13T11:44:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7919#issuecomment-68785",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_068786.json:
```json
{
    "body": "Good catch. That actually was a relic from a former (failed) attempt at getting c1 and c2 to be garbage collected by putting them out of scope, and see if this had any influence.\n\nReplacing it by an equality test is sure better. Thanks!",
    "created_at": "2010-01-13T11:44:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7919#issuecomment-68786",
    "user": "https://github.com/nthiery"
}
```

Good catch. That actually was a relic from a former (failed) attempt at getting c1 and c2 to be garbage collected by putting them out of scope, and see if this had any influence.

Replacing it by an equality test is sure better. Thanks!



---

archive/issue_comments_068787.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-14T06:52:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7919#issuecomment-68787",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed
