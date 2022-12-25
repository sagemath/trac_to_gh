# Issue 8557: is_singular method for projective plane curves

archive/issues_008557.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @JohnCremona\n\nIt would be useful to have a way of checking whether a projective curve has any singular points. \nA patch to do this is on its way.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8557\n\n",
    "created_at": "2010-03-18T15:09:13Z",
    "labels": [
        "component: algebraic geometry",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "is_singular method for projective plane curves",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8557",
    "user": "https://trac.sagemath.org/admin/accounts/users/cturner"
}
```
Assignee: @aghitza

CC:  @JohnCremona

It would be useful to have a way of checking whether a projective curve has any singular points. 
A patch to do this is on its way.

Issue created by migration from https://trac.sagemath.org/ticket/8557





---

archive/issue_comments_077284.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-20T10:17:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8557#issuecomment-77284",
    "user": "https://trac.sagemath.org/admin/accounts/users/cturner"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077285.json:
```json
{
    "body": "Attachment [trac_8557_is_singular.patch](tarball://root/attachments/some-uuid/ticket8557/trac_8557_is_singular.patch) by cturner created at 2010-03-20 10:17:26",
    "created_at": "2010-03-20T10:17:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8557#issuecomment-77285",
    "user": "https://trac.sagemath.org/admin/accounts/users/cturner"
}
```

Attachment [trac_8557_is_singular.patch](tarball://root/attachments/some-uuid/ticket8557/trac_8557_is_singular.patch) by cturner created at 2010-03-20 10:17:26



---

archive/issue_comments_077286.json:
```json
{
    "body": "Looks good.\n\nWe should (more generally) wrap Singular's slocus function which computes the singular locus of an ideal in a multivariate polynomial ring, but that should be a new ticket.",
    "created_at": "2010-04-03T06:01:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8557#issuecomment-77286",
    "user": "https://github.com/aghitza"
}
```

Looks good.

We should (more generally) wrap Singular's slocus function which computes the singular locus of an ideal in a multivariate polynomial ring, but that should be a new ticket.



---

archive/issue_comments_077287.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-03T06:01:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8557#issuecomment-77287",
    "user": "https://github.com/aghitza"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_077288.json:
```json
{
    "body": "This doesn't apply cleanly; it apparently conflicts with a patch merged into Sage 4.4.alpha0.  Please rebase it against 4.4.alpha0, and we'll try hard to get this into 4.4.alpha1.",
    "created_at": "2010-04-17T04:11:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8557#issuecomment-77288",
    "user": "https://github.com/jhpalmieri"
}
```

This doesn't apply cleanly; it apparently conflicts with a patch merged into Sage 4.4.alpha0.  Please rebase it against 4.4.alpha0, and we'll try hard to get this into 4.4.alpha1.



---

archive/issue_comments_077289.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-04-17T04:11:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8557#issuecomment-77289",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_077290.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-18T05:30:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8557#issuecomment-77290",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_077291.json:
```json
{
    "body": "Never mind, I've taken care of it.",
    "created_at": "2010-04-18T05:30:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8557#issuecomment-77291",
    "user": "https://github.com/jhpalmieri"
}
```

Never mind, I've taken care of it.



---

archive/issue_comments_077292.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-18T05:30:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8557#issuecomment-77292",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_077293.json:
```json
{
    "body": "Attachment [trac_8557_rebased.patch](tarball://root/attachments/some-uuid/ticket8557/trac_8557_rebased.patch) by @jhpalmieri created at 2010-04-18 05:31:00",
    "created_at": "2010-04-18T05:31:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8557#issuecomment-77293",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_8557_rebased.patch](tarball://root/attachments/some-uuid/ticket8557/trac_8557_rebased.patch) by @jhpalmieri created at 2010-04-18 05:31:00



---

archive/issue_comments_077294.json:
```json
{
    "body": "Merged \"trac_8557_rebased.patch\" into 4.4.alpha1.",
    "created_at": "2010-04-19T05:19:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8557#issuecomment-77294",
    "user": "https://github.com/jhpalmieri"
}
```

Merged "trac_8557_rebased.patch" into 4.4.alpha1.



---

archive/issue_comments_077295.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-19T05:19:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8557#issuecomment-77295",
    "user": "https://github.com/jhpalmieri"
}
```

Resolution: fixed
