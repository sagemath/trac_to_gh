# Issue 5504: fix shell script "sage"

archive/issues_005504.json:
```json
{
    "body": "Assignee: was\n\nIt would be great if the line\n\n\"$SAGE_ROOT/local/bin/sage-sage\" $*\n\nin the top level script 'sage' would be changed to\n\n\"$SAGE_ROOT/local/bin/sage-sage\" \"$`@`\"\n\nso it doesn't split up command line arguments that happen to have spaces in them.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5504\n\n",
    "created_at": "2009-03-12T21:03:27Z",
    "labels": [
        "user interface",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "fix shell script \"sage\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5504",
    "user": "dangrayson"
}
```
Assignee: was

It would be great if the line

"$SAGE_ROOT/local/bin/sage-sage" $*

in the top level script 'sage' would be changed to

"$SAGE_ROOT/local/bin/sage-sage" "$`@`"

so it doesn't split up command line arguments that happen to have spaces in them.

Issue created by migration from https://trac.sagemath.org/ticket/5504





---

archive/issue_comments_042752.json:
```json
{
    "body": "The intended change already has happened and was part of trac #4354 : \"loading a file with spaces in the filename doesn't work\"",
    "created_at": "2009-03-27T20:18:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5504#issuecomment-42752",
    "user": "GeorgSWeber"
}
```

The intended change already has happened and was part of trac #4354 : "loading a file with spaces in the filename doesn't work"



---

archive/issue_comments_042753.json:
```json
{
    "body": "Am I allowed to close this?",
    "created_at": "2009-03-27T20:19:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5504#issuecomment-42753",
    "user": "GeorgSWeber"
}
```

Am I allowed to close this?



---

archive/issue_comments_042754.json:
```json
{
    "body": "Replying to [comment:3 GeorgSWeber]:\n\nThis is indeed a dupe of  #4354.\n\n> Am I allowed to close this?\n\nNope, the release manager does that after verifying that it is a dupe. And I have to state that you are right, so closed as a dupe :)\n\nCheers,\n\nMichael",
    "created_at": "2009-03-27T20:37:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5504#issuecomment-42754",
    "user": "mabshoff"
}
```

Replying to [comment:3 GeorgSWeber]:

This is indeed a dupe of  #4354.

> Am I allowed to close this?

Nope, the release manager does that after verifying that it is a dupe. And I have to state that you are right, so closed as a dupe :)

Cheers,

Michael



---

archive/issue_comments_042755.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-03-27T20:37:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5504#issuecomment-42755",
    "user": "mabshoff"
}
```

Resolution: duplicate
