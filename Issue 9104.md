# Issue 9104: _name is set too late when creating a combinatorial free module

archive/issues_009104.json:
```json
{
    "body": "Assignee: sage-combinat\n\nKeywords: CombinatorialFreeModule name\n\nThis is a followup to #8882\n\nIn the `__init__` of `CombinatorialFreeModule`, an attribute `_name` is set if it wasn't before. However it can be used during the initialization of Parent by the coercion mechanism leading to some failure. The patch fixes the problem.\n\nNote: right now the problem does appear but it will in the upcomming #8881\n\nIssue created by migration from https://trac.sagemath.org/ticket/9104\n\n",
    "created_at": "2010-05-31T13:07:27Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "_name is set too late when creating a combinatorial free module",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9104",
    "user": "@hivert"
}
```
Assignee: sage-combinat

Keywords: CombinatorialFreeModule name

This is a followup to #8882

In the `__init__` of `CombinatorialFreeModule`, an attribute `_name` is set if it wasn't before. However it can be used during the initialization of Parent by the coercion mechanism leading to some failure. The patch fixes the problem.

Note: right now the problem does appear but it will in the upcomming #8881

Issue created by migration from https://trac.sagemath.org/ticket/9104





---

archive/issue_comments_084599.json:
```json
{
    "body": "Attachment [trac_9104_freemod_name-fix-nt.patch](tarball://root/attachments/some-uuid/ticket9104/trac_9104_freemod_name-fix-nt.patch) by @hivert created at 2010-05-31 13:10:52",
    "created_at": "2010-05-31T13:10:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9104#issuecomment-84599",
    "user": "@hivert"
}
```

Attachment [trac_9104_freemod_name-fix-nt.patch](tarball://root/attachments/some-uuid/ticket9104/trac_9104_freemod_name-fix-nt.patch) by @hivert created at 2010-05-31 13:10:52



---

archive/issue_comments_084600.json:
```json
{
    "body": "Note: This patch was forgotten during the uploading of #8882 but the problem only appeared later on.",
    "created_at": "2010-05-31T13:12:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9104#issuecomment-84600",
    "user": "@hivert"
}
```

Note: This patch was forgotten during the uploading of #8882 but the problem only appeared later on.



---

archive/issue_comments_084601.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-31T13:12:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9104#issuecomment-84601",
    "user": "@hivert"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_084602.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-31T13:12:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9104#issuecomment-84602",
    "user": "@hivert"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084603.json:
```json
{
    "body": "Patch is ok !",
    "created_at": "2010-05-31T13:12:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9104#issuecomment-84603",
    "user": "@hivert"
}
```

Patch is ok !



---

archive/issue_comments_084604.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-05T21:39:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9104#issuecomment-84604",
    "user": "@mwhansen"
}
```

Resolution: fixed
