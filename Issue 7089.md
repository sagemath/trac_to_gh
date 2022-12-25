# Issue 7089: refactor SAGE_ROOT/makefile

archive/issues_007089.json:
```json
{
    "body": "Assignee: tbd\n\nI've been editing the root makefile while working on a couple tickets, and I have a deep urge to refactor repetitive, boilerplate code. In SAGE_ROOT/makefile, there are many sequences of commands that are repeated in multiple targets.\n\nThe attached patch puts the repetitive bits into variables that can easily be customized later by editing only one thing in the makefile, instead of multiple things.\n\nI'd also like to consider removing the \"install\" and \"gmp\" targets in the makefile. I suspect no one ever uses them.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7089\n\n",
    "created_at": "2009-10-01T03:39:26Z",
    "labels": [
        "component: build",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "refactor SAGE_ROOT/makefile",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7089",
    "user": "https://github.com/dandrake"
}
```
Assignee: tbd

I've been editing the root makefile while working on a couple tickets, and I have a deep urge to refactor repetitive, boilerplate code. In SAGE_ROOT/makefile, there are many sequences of commands that are repeated in multiple targets.

The attached patch puts the repetitive bits into variables that can easily be customized later by editing only one thing in the makefile, instead of multiple things.

I'd also like to consider removing the "install" and "gmp" targets in the makefile. I suspect no one ever uses them.

Issue created by migration from https://trac.sagemath.org/ticket/7089





---

archive/issue_comments_058478.json:
```json
{
    "body": "unified diff for SAGE_ROOT/makefile",
    "created_at": "2009-10-01T03:39:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7089#issuecomment-58478",
    "user": "https://github.com/dandrake"
}
```

unified diff for SAGE_ROOT/makefile



---

archive/issue_comments_058479.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-10-01T03:41:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7089#issuecomment-58479",
    "user": "https://github.com/dandrake"
}
```

Changing status from new to assigned.



---

archive/issue_comments_058480.json:
```json
{
    "body": "Changing keywords from \"\" to \"makefile\".",
    "created_at": "2009-10-01T03:41:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7089#issuecomment-58480",
    "user": "https://github.com/dandrake"
}
```

Changing keywords from "" to "makefile".



---

archive/issue_comments_058481.json:
```json
{
    "body": "Attachment [makefile.patch](tarball://root/attachments/some-uuid/ticket7089/makefile.patch) by @dandrake created at 2009-10-01 03:41:52",
    "created_at": "2009-10-01T03:41:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7089#issuecomment-58481",
    "user": "https://github.com/dandrake"
}
```

Attachment [makefile.patch](tarball://root/attachments/some-uuid/ticket7089/makefile.patch) by @dandrake created at 2009-10-01 03:41:52



---

archive/issue_comments_058482.json:
```json
{
    "body": "Changing assignee from tbd to @dandrake.",
    "created_at": "2009-10-01T03:41:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7089#issuecomment-58482",
    "user": "https://github.com/dandrake"
}
```

Changing assignee from tbd to @dandrake.



---

archive/issue_comments_058483.json:
```json
{
    "body": "Patch applies, and the tests run properly. Positive review.",
    "created_at": "2009-10-01T04:48:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7089#issuecomment-58483",
    "user": "https://github.com/TimDumol"
}
```

Patch applies, and the tests run properly. Positive review.



---

archive/issue_comments_058484.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-16T09:02:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7089#issuecomment-58484",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
