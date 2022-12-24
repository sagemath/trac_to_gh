# Issue 7089: refactor SAGE_ROOT/makefile

archive/issues_007089.json:
```json
{
    "body": "Assignee: tbd\n\nI've been editing the root makefile while working on a couple tickets, and I have a deep urge to refactor repetitive, boilerplate code. In SAGE_ROOT/makefile, there are many sequences of commands that are repeated in multiple targets.\n\nThe attached patch puts the repetitive bits into variables that can easily be customized later by editing only one thing in the makefile, instead of multiple things.\n\nI'd also like to consider removing the \"install\" and \"gmp\" targets in the makefile. I suspect no one ever uses them.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7089\n\n",
    "created_at": "2009-10-01T03:39:26Z",
    "labels": [
        "build",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "refactor SAGE_ROOT/makefile",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7089",
    "user": "@dandrake"
}
```
Assignee: tbd

I've been editing the root makefile while working on a couple tickets, and I have a deep urge to refactor repetitive, boilerplate code. In SAGE_ROOT/makefile, there are many sequences of commands that are repeated in multiple targets.

The attached patch puts the repetitive bits into variables that can easily be customized later by editing only one thing in the makefile, instead of multiple things.

I'd also like to consider removing the "install" and "gmp" targets in the makefile. I suspect no one ever uses them.

Issue created by migration from https://trac.sagemath.org/ticket/7089





---

archive/issue_comments_058588.json:
```json
{
    "body": "unified diff for SAGE_ROOT/makefile",
    "created_at": "2009-10-01T03:39:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7089#issuecomment-58588",
    "user": "@dandrake"
}
```

unified diff for SAGE_ROOT/makefile



---

archive/issue_comments_058589.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-10-01T03:41:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7089#issuecomment-58589",
    "user": "@dandrake"
}
```

Changing status from new to assigned.



---

archive/issue_comments_058590.json:
```json
{
    "body": "Changing keywords from \"\" to \"makefile\".",
    "created_at": "2009-10-01T03:41:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7089#issuecomment-58590",
    "user": "@dandrake"
}
```

Changing keywords from "" to "makefile".



---

archive/issue_comments_058591.json:
```json
{
    "body": "Attachment [makefile.patch](tarball://root/attachments/some-uuid/ticket7089/makefile.patch) by @dandrake created at 2009-10-01 03:41:52",
    "created_at": "2009-10-01T03:41:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7089#issuecomment-58591",
    "user": "@dandrake"
}
```

Attachment [makefile.patch](tarball://root/attachments/some-uuid/ticket7089/makefile.patch) by @dandrake created at 2009-10-01 03:41:52



---

archive/issue_comments_058592.json:
```json
{
    "body": "Changing assignee from tbd to @dandrake.",
    "created_at": "2009-10-01T03:41:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7089#issuecomment-58592",
    "user": "@dandrake"
}
```

Changing assignee from tbd to @dandrake.



---

archive/issue_comments_058593.json:
```json
{
    "body": "Patch applies, and the tests run properly. Positive review.",
    "created_at": "2009-10-01T04:48:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7089#issuecomment-58593",
    "user": "@TimDumol"
}
```

Patch applies, and the tests run properly. Positive review.



---

archive/issue_comments_058594.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-16T09:02:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7089#issuecomment-58594",
    "user": "@mwhansen"
}
```

Resolution: fixed
