# Issue 6967: @parallel -- dramatically improve by rewriting with fork directly, using files, timeouts, controlling interfaces, etc.

archive/issues_006967.json:
```json
{
    "body": "Assignee: cwitty\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6967\n\n",
    "created_at": "2009-09-20T10:43:46Z",
    "labels": [
        "misc",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "@parallel -- dramatically improve by rewriting with fork directly, using files, timeouts, controlling interfaces, etc.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6967",
    "user": "@williamstein"
}
```
Assignee: cwitty



Issue created by migration from https://trac.sagemath.org/ticket/6967





---

archive/issue_comments_057637.json:
```json
{
    "body": "first usable version",
    "created_at": "2009-09-20T11:01:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6967#issuecomment-57637",
    "user": "@williamstein"
}
```

first usable version



---

archive/issue_comments_057638.json:
```json
{
    "body": "Attachment [trac_6967-part1.patch](tarball://root/attachments/some-uuid/ticket6967/trac_6967-part1.patch) by @williamstein created at 2009-09-20 11:16:01",
    "created_at": "2009-09-20T11:16:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6967#issuecomment-57638",
    "user": "@williamstein"
}
```

Attachment [trac_6967-part1.patch](tarball://root/attachments/some-uuid/ticket6967/trac_6967-part1.patch) by @williamstein created at 2009-09-20 11:16:01



---

archive/issue_comments_057639.json:
```json
{
    "body": "Should we also allow each child process to pull off a large chunk of the input (e.g., from a deque), when it's more efficient?  Determine the chunk size dynamically, a la `timeit`?",
    "created_at": "2009-11-18T23:30:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6967#issuecomment-57639",
    "user": "@qed777"
}
```

Should we also allow each child process to pull off a large chunk of the input (e.g., from a deque), when it's more efficient?  Determine the chunk size dynamically, a la `timeit`?



---

archive/issue_comments_057640.json:
```json
{
    "body": "Changing type from enhancement to defect.",
    "created_at": "2010-01-18T04:10:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6967#issuecomment-57640",
    "user": "@williamstein"
}
```

Changing type from enhancement to defect.



---

archive/issue_comments_057641.json:
```json
{
    "body": "This fixes *major* bugs in `@`parallel sucking.   Without this, `@`parallel gets confused by Sage-isms, preparsing, state, etc., and really hasn't taken off as a result.  This fixes all that.",
    "created_at": "2010-01-18T04:10:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6967#issuecomment-57641",
    "user": "@williamstein"
}
```

This fixes *major* bugs in `@`parallel sucking.   Without this, `@`parallel gets confused by Sage-isms, preparsing, state, etc., and really hasn't taken off as a result.  This fixes all that.



---

archive/issue_comments_057642.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-18T12:16:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6967#issuecomment-57642",
    "user": "@williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_057643.json:
```json
{
    "body": "This also fixes a very serious bug in sage.interfaces.quit which will lead to zombie processes being left around, and improves doctest coverage.",
    "created_at": "2010-01-18T12:16:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6967#issuecomment-57643",
    "user": "@williamstein"
}
```

This also fixes a very serious bug in sage.interfaces.quit which will lead to zombie processes being left around, and improves doctest coverage.



---

archive/issue_comments_057644.json:
```json
{
    "body": "Attachment [trac_6967-part2.patch](tarball://root/attachments/some-uuid/ticket6967/trac_6967-part2.patch) by @williamstein created at 2010-01-18 12:30:34",
    "created_at": "2010-01-18T12:30:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6967#issuecomment-57644",
    "user": "@williamstein"
}
```

Attachment [trac_6967-part2.patch](tarball://root/attachments/some-uuid/ticket6967/trac_6967-part2.patch) by @williamstein created at 2010-01-18 12:30:34



---

archive/issue_comments_057645.json:
```json
{
    "body": "Attachment [trac_6967-part3.patch](tarball://root/attachments/some-uuid/ticket6967/trac_6967-part3.patch) by @williamstein created at 2010-01-18 13:51:42",
    "created_at": "2010-01-18T13:51:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6967#issuecomment-57645",
    "user": "@williamstein"
}
```

Attachment [trac_6967-part3.patch](tarball://root/attachments/some-uuid/ticket6967/trac_6967-part3.patch) by @williamstein created at 2010-01-18 13:51:42



---

archive/issue_comments_057646.json:
```json
{
    "body": "Awesome!!!",
    "created_at": "2010-01-19T02:44:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6967#issuecomment-57646",
    "user": "@rlmill"
}
```

Awesome!!!



---

archive/issue_comments_057647.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-19T02:44:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6967#issuecomment-57647",
    "user": "@rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_057648.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-19T04:07:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6967#issuecomment-57648",
    "user": "@rlmill"
}
```

Resolution: fixed
