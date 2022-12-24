# Issue 7083: Improve a few special functions

archive/issues_007083.json:
```json
{
    "body": "Assignee: @burcin\n\nA few functions in functions/special.py need a little help to actually accept valid input.  Also, exp_int is duplicated in its functionality.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7083\n\n",
    "created_at": "2009-09-30T15:03:10Z",
    "labels": [
        "calculus",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "Improve a few special functions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7083",
    "user": "@kcrisman"
}
```
Assignee: @burcin

A few functions in functions/special.py need a little help to actually accept valid input.  Also, exp_int is duplicated in its functionality.

Issue created by migration from https://trac.sagemath.org/ticket/7083





---

archive/issue_comments_058549.json:
```json
{
    "body": "Attachment [trac_7083-special-funcs.patch](tarball://root/attachments/some-uuid/ticket7083/trac_7083-special-funcs.patch) by @kcrisman created at 2009-09-30 15:04:02\n\nBased on 4.1.2.alpha4",
    "created_at": "2009-09-30T15:04:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7083#issuecomment-58549",
    "user": "@kcrisman"
}
```

Attachment [trac_7083-special-funcs.patch](tarball://root/attachments/some-uuid/ticket7083/trac_7083-special-funcs.patch) by @kcrisman created at 2009-09-30 15:04:02

Based on 4.1.2.alpha4



---

archive/issue_comments_058550.json:
```json
{
    "body": "Another option to deprecating exp_int() is to just make it call exponential_integral_1, and I would be happy to implement either way as a reviewer indicates is useful.",
    "created_at": "2009-09-30T15:05:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7083#issuecomment-58550",
    "user": "@kcrisman"
}
```

Another option to deprecating exp_int() is to just make it call exponential_integral_1, and I would be happy to implement either way as a reviewer indicates is useful.



---

archive/issue_comments_058551.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-25T13:41:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7083#issuecomment-58551",
    "user": "@wdjoyner"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_058552.json:
```json
{
    "body": "Passes sage -testall on ubuntu 9.04 32 bit. It seems to pass on an imac running 10.6 but there are so many other failures, I'm not sure. Does what it claims to do and adds nice functionality.",
    "created_at": "2009-10-25T13:41:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7083#issuecomment-58552",
    "user": "@wdjoyner"
}
```

Passes sage -testall on ubuntu 9.04 32 bit. It seems to pass on an imac running 10.6 but there are so many other failures, I'm not sure. Does what it claims to do and adds nice functionality.



---

archive/issue_comments_058553.json:
```json
{
    "body": "Resolution: ",
    "created_at": "2009-10-31T15:31:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7083#issuecomment-58553",
    "user": "@mwhansen"
}
```

Resolution: 



---

archive/issue_comments_058554.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-23T14:25:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7083#issuecomment-58554",
    "user": "@kcrisman"
}
```

Resolution: fixed
