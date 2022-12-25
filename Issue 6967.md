# Issue 6967: @parallel -- dramatically improve by rewriting with fork directly, using files, timeouts, controlling interfaces, etc.

archive/issues_006967.json:
```json
{
    "body": "Assignee: cwitty\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6967\n\n",
    "created_at": "2009-09-20T10:43:46Z",
    "labels": [
        "component: misc"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "@parallel -- dramatically improve by rewriting with fork directly, using files, timeouts, controlling interfaces, etc.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6967",
    "user": "https://github.com/williamstein"
}
```
Assignee: cwitty



Issue created by migration from https://trac.sagemath.org/ticket/6967





---

archive/issue_comments_057529.json:
```json
{
    "body": "first usable version",
    "created_at": "2009-09-20T11:01:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6967#issuecomment-57529",
    "user": "https://github.com/williamstein"
}
```

first usable version



---

archive/issue_comments_057530.json:
```json
{
    "body": "Attachment [trac_6967-part1.patch](tarball://root/attachments/some-uuid/ticket6967/trac_6967-part1.patch) by @williamstein created at 2009-09-20 11:16:01",
    "created_at": "2009-09-20T11:16:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6967#issuecomment-57530",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_6967-part1.patch](tarball://root/attachments/some-uuid/ticket6967/trac_6967-part1.patch) by @williamstein created at 2009-09-20 11:16:01



---

archive/issue_comments_057531.json:
```json
{
    "body": "Should we also allow each child process to pull off a large chunk of the input (e.g., from a deque), when it's more efficient?  Determine the chunk size dynamically, a la `timeit`?",
    "created_at": "2009-11-18T23:30:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6967#issuecomment-57531",
    "user": "https://github.com/qed777"
}
```

Should we also allow each child process to pull off a large chunk of the input (e.g., from a deque), when it's more efficient?  Determine the chunk size dynamically, a la `timeit`?



---

archive/issue_comments_057532.json:
```json
{
    "body": "Changing type from enhancement to defect.",
    "created_at": "2010-01-18T04:10:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6967#issuecomment-57532",
    "user": "https://github.com/williamstein"
}
```

Changing type from enhancement to defect.



---

archive/issue_comments_057533.json:
```json
{
    "body": "This fixes *major* bugs in `@`parallel sucking.   Without this, `@`parallel gets confused by Sage-isms, preparsing, state, etc., and really hasn't taken off as a result.  This fixes all that.",
    "created_at": "2010-01-18T04:10:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6967#issuecomment-57533",
    "user": "https://github.com/williamstein"
}
```

This fixes *major* bugs in `@`parallel sucking.   Without this, `@`parallel gets confused by Sage-isms, preparsing, state, etc., and really hasn't taken off as a result.  This fixes all that.



---

archive/issue_comments_057534.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-18T12:16:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6967#issuecomment-57534",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_057535.json:
```json
{
    "body": "This also fixes a very serious bug in sage.interfaces.quit which will lead to zombie processes being left around, and improves doctest coverage.",
    "created_at": "2010-01-18T12:16:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6967#issuecomment-57535",
    "user": "https://github.com/williamstein"
}
```

This also fixes a very serious bug in sage.interfaces.quit which will lead to zombie processes being left around, and improves doctest coverage.



---

archive/issue_comments_057536.json:
```json
{
    "body": "Attachment [trac_6967-part2.patch](tarball://root/attachments/some-uuid/ticket6967/trac_6967-part2.patch) by @williamstein created at 2010-01-18 12:30:34",
    "created_at": "2010-01-18T12:30:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6967#issuecomment-57536",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_6967-part2.patch](tarball://root/attachments/some-uuid/ticket6967/trac_6967-part2.patch) by @williamstein created at 2010-01-18 12:30:34



---

archive/issue_comments_057537.json:
```json
{
    "body": "Attachment [trac_6967-part3.patch](tarball://root/attachments/some-uuid/ticket6967/trac_6967-part3.patch) by @williamstein created at 2010-01-18 13:51:42",
    "created_at": "2010-01-18T13:51:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6967#issuecomment-57537",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_6967-part3.patch](tarball://root/attachments/some-uuid/ticket6967/trac_6967-part3.patch) by @williamstein created at 2010-01-18 13:51:42



---

archive/issue_comments_057538.json:
```json
{
    "body": "Awesome!!!",
    "created_at": "2010-01-19T02:44:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6967#issuecomment-57538",
    "user": "https://github.com/rlmill"
}
```

Awesome!!!



---

archive/issue_comments_057539.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-19T02:44:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6967#issuecomment-57539",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_057540.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-19T04:07:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6967#issuecomment-57540",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed
