# Issue 7659: fix tests in documentation after pynac printing changes

archive/issues_007659.json:
```json
{
    "body": "Assignee: mvngu\n\nAttached patch fixes minor doctest errors in documentation caused by #7406 in 4.3.rc0.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7659\n\n",
    "created_at": "2009-12-11T13:31:52Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "fix tests in documentation after pynac printing changes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7659",
    "user": "burcin"
}
```
Assignee: mvngu

Attached patch fixes minor doctest errors in documentation caused by #7406 in 4.3.rc0.



Issue created by migration from https://trac.sagemath.org/ticket/7659





---

archive/issue_comments_065512.json:
```json
{
    "body": "Attachment [trac_7659-doctest_fixes.patch](tarball://root/attachments/some-uuid/ticket7659/trac_7659-doctest_fixes.patch) by burcin created at 2009-12-11 13:35:19\n\ndoctest fixes",
    "created_at": "2009-12-11T13:35:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7659#issuecomment-65512",
    "user": "burcin"
}
```

Attachment [trac_7659-doctest_fixes.patch](tarball://root/attachments/some-uuid/ticket7659/trac_7659-doctest_fixes.patch) by burcin created at 2009-12-11 13:35:19

doctest fixes



---

archive/issue_comments_065513.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-11T13:35:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7659#issuecomment-65513",
    "user": "burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_065514.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-11T23:30:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7659#issuecomment-65514",
    "user": "AlexGhitza"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_065515.json:
```json
{
    "body": "Looks good and fixes the problems.",
    "created_at": "2009-12-11T23:30:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7659#issuecomment-65515",
    "user": "AlexGhitza"
}
```

Looks good and fixes the problems.



---

archive/issue_comments_065516.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-14T16:05:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7659#issuecomment-65516",
    "user": "mhansen"
}
```

Resolution: fixed



---

archive/issue_comments_065517.json:
```json
{
    "body": "This is a duplicate of #7747 (or rather, #7747 is a duplicate of this one).  The patch in #7747 does a little more; can we merge that one instead?",
    "created_at": "2009-12-22T19:02:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7659#issuecomment-65517",
    "user": "jhpalmieri"
}
```

This is a duplicate of #7747 (or rather, #7747 is a duplicate of this one).  The patch in #7747 does a little more; can we merge that one instead?



---

archive/issue_comments_065518.json:
```json
{
    "body": "Replying to [comment:5 jhpalmieri]:\n> This is a duplicate of #7747 (or rather, #7747 is a duplicate of this one).  The patch in #7747 does a little more; can we merge that one instead?\n\nAFAICT by looking at comment:3, this patch was merged. The patch on #7747 should be rebased in this case.",
    "created_at": "2009-12-22T22:55:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7659#issuecomment-65518",
    "user": "burcin"
}
```

Replying to [comment:5 jhpalmieri]:
> This is a duplicate of #7747 (or rather, #7747 is a duplicate of this one).  The patch in #7747 does a little more; can we merge that one instead?

AFAICT by looking at comment:3, this patch was merged. The patch on #7747 should be rebased in this case.



---

archive/issue_comments_065519.json:
```json
{
    "body": "I've backed out this patch, and am merging the one at #7747 instead.",
    "created_at": "2009-12-23T13:26:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7659#issuecomment-65519",
    "user": "mhansen"
}
```

I've backed out this patch, and am merging the one at #7747 instead.



---

archive/issue_comments_065520.json:
```json
{
    "body": "I don't see why you couldn't just merge the patch at #7747 on top of this one, and ignored the failed hunks.",
    "created_at": "2009-12-23T13:49:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7659#issuecomment-65520",
    "user": "burcin"
}
```

I don't see why you couldn't just merge the patch at #7747 on top of this one, and ignored the failed hunks.
