# Issue 6608: [with patch, needs review] nodetex is broken

archive/issues_006608.json:
```json
{
    "body": "Assignee: @jhpalmieri\n\nIf you type (at the command line)\n\n```\nlatex.blackboard_bold?\n```\n\nyou get the docstring for this, but it is missing all of the backslashes.  This is because the docstring is being processed by the `detex` function, but it's not supposed to be: the docstring contains a \"nodetex\" directive.  (You can see the backslashes and the \"nodetex\" directive if you type `latex.blackboard_bold??`.)\n\nThe attached patch makes this work again.  Test with the above, or with `view?` or with `sage.misc.sagedoc.detex?`, for instance.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6608\n\n",
    "created_at": "2009-07-24T00:26:13Z",
    "labels": [
        "component: misc",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "[with patch, needs review] nodetex is broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6608",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: @jhpalmieri

If you type (at the command line)

```
latex.blackboard_bold?
```

you get the docstring for this, but it is missing all of the backslashes.  This is because the docstring is being processed by the `detex` function, but it's not supposed to be: the docstring contains a "nodetex" directive.  (You can see the backslashes and the "nodetex" directive if you type `latex.blackboard_bold??`.)

The attached patch makes this work again.  Test with the above, or with `view?` or with `sage.misc.sagedoc.detex?`, for instance.

Issue created by migration from https://trac.sagemath.org/ticket/6608





---

archive/issue_comments_054000.json:
```json
{
    "body": "Attachment [trac_6608-nodetex.patch](tarball://root/attachments/some-uuid/ticket6608/trac_6608-nodetex.patch) by @jhpalmieri created at 2009-07-24 00:26:40",
    "created_at": "2009-07-24T00:26:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6608#issuecomment-54000",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_6608-nodetex.patch](tarball://root/attachments/some-uuid/ticket6608/trac_6608-nodetex.patch) by @jhpalmieri created at 2009-07-24 00:26:40



---

archive/issue_comments_054001.json:
```json
{
    "body": "Looks good to me. I tried to create a new doctest for this but it was a) too big and ugly and/or b) too fragile to be useful. Adam",
    "created_at": "2009-07-26T12:55:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6608#issuecomment-54001",
    "user": "https://github.com/maxthemouse"
}
```

Looks good to me. I tried to create a new doctest for this but it was a) too big and ugly and/or b) too fragile to be useful. Adam



---

archive/issue_comments_054002.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-27T07:57:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6608#issuecomment-54002",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
