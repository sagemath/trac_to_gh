# Issue 6608: [with patch, needs review] nodetex is broken

archive/issues_006608.json:
```json
{
    "body": "Assignee: jhpalmieri\n\nIf you type (at the command line)\n\n```\nlatex.blackboard_bold?\n```\n\nyou get the docstring for this, but it is missing all of the backslashes.  This is because the docstring is being processed by the `detex` function, but it's not supposed to be: the docstring contains a \"nodetex\" directive.  (You can see the backslashes and the \"nodetex\" directive if you type `latex.blackboard_bold??`.)\n\nThe attached patch makes this work again.  Test with the above, or with `view?` or with `sage.misc.sagedoc.detex?`, for instance.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6608\n\n",
    "created_at": "2009-07-24T00:26:13Z",
    "labels": [
        "misc",
        "minor",
        "bug"
    ],
    "title": "[with patch, needs review] nodetex is broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6608",
    "user": "jhpalmieri"
}
```
Assignee: jhpalmieri

If you type (at the command line)

```
latex.blackboard_bold?
```

you get the docstring for this, but it is missing all of the backslashes.  This is because the docstring is being processed by the `detex` function, but it's not supposed to be: the docstring contains a "nodetex" directive.  (You can see the backslashes and the "nodetex" directive if you type `latex.blackboard_bold??`.)

The attached patch makes this work again.  Test with the above, or with `view?` or with `sage.misc.sagedoc.detex?`, for instance.

Issue created by migration from https://trac.sagemath.org/ticket/6608





---

archive/issue_comments_054101.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-07-24T00:26:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6608#issuecomment-54101",
    "user": "jhpalmieri"
}
```

Attachment



---

archive/issue_comments_054102.json:
```json
{
    "body": "Looks good to me. I tried to create a new doctest for this but it was a) too big and ugly and/or b) too fragile to be useful. Adam",
    "created_at": "2009-07-26T12:55:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6608#issuecomment-54102",
    "user": "awebb"
}
```

Looks good to me. I tried to create a new doctest for this but it was a) too big and ugly and/or b) too fragile to be useful. Adam



---

archive/issue_comments_054103.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-27T07:57:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6608#issuecomment-54103",
    "user": "mvngu"
}
```

Resolution: fixed
