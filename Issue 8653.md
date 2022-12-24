# Issue 8653: Command-line "advanced" help has wrong option name for randomized tests

archive/issues_008653.json:
```json
{
    "body": "Assignee: mvngu\n\n`sage -h` says  `sage -t -randorder <files>` will do doctests in a random order and this is correct,\n\nbut `sage -advanced` says `sage -t -rand <files>` will do the job, and this is incorrect\n\nUpcoming patch (to apply at the local/bin repo) corrects the advanced usage message.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8653\n\n",
    "created_at": "2010-04-06T05:58:27Z",
    "labels": [
        "documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "Command-line \"advanced\" help has wrong option name for randomized tests",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8653",
    "user": "rbeezer"
}
```
Assignee: mvngu

`sage -h` says  `sage -t -randorder <files>` will do doctests in a random order and this is correct,

but `sage -advanced` says `sage -t -rand <files>` will do the job, and this is incorrect

Upcoming patch (to apply at the local/bin repo) corrects the advanced usage message.

Issue created by migration from https://trac.sagemath.org/ticket/8653





---

archive/issue_comments_078510.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-06T06:02:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8653#issuecomment-78510",
    "user": "rbeezer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_078511.json:
```json
{
    "body": "Attachment [trac_8653-random-order-doctest-doc.patch](tarball://root/attachments/some-uuid/ticket8653/trac_8653-random-order-doctest-doc.patch) by rbeezer created at 2010-04-06 06:02:03",
    "created_at": "2010-04-06T06:02:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8653#issuecomment-78511",
    "user": "rbeezer"
}
```

Attachment [trac_8653-random-order-doctest-doc.patch](tarball://root/attachments/some-uuid/ticket8653/trac_8653-random-order-doctest-doc.patch) by rbeezer created at 2010-04-06 06:02:03



---

archive/issue_comments_078512.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-18T08:29:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8653#issuecomment-78512",
    "user": "timdumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_078513.json:
```json
{
    "body": "Works as advertised. Positive review.",
    "created_at": "2010-04-18T08:29:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8653#issuecomment-78513",
    "user": "timdumol"
}
```

Works as advertised. Positive review.



---

archive/issue_comments_078514.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-19T05:20:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8653#issuecomment-78514",
    "user": "jhpalmieri"
}
```

Resolution: fixed



---

archive/issue_comments_078515.json:
```json
{
    "body": "Merged into 4.4.alpha1.",
    "created_at": "2010-04-19T05:20:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8653#issuecomment-78515",
    "user": "jhpalmieri"
}
```

Merged into 4.4.alpha1.
