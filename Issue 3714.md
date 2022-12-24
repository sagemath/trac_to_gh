# Issue 3714: add quotes to paramteres passed in lisp and clisp scripts

archive/issues_003714.json:
```json
{
    "body": "Assignee: mabshoff\n\nFriCAS calls clisp with multiple parameters, i.e. there are spaces involved. Wrapping $`@` in quotes solves the problem. This is required to fix the optional FriCAS 1.0.3.spkg.\n\nThe patch was provided by Waldek Hebisch.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/3714\n\n",
    "created_at": "2008-07-23T18:03:22Z",
    "labels": [
        "build",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "add quotes to paramteres passed in lisp and clisp scripts",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3714",
    "user": "mabshoff"
}
```
Assignee: mabshoff

FriCAS calls clisp with multiple parameters, i.e. there are spaces involved. Wrapping $`@` in quotes solves the problem. This is required to fix the optional FriCAS 1.0.3.spkg.

The patch was provided by Waldek Hebisch.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/3714





---

archive/issue_comments_026363.json:
```json
{
    "body": "William opened #3715, so I am closing this as a dupe because of the better description at his ticket.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-23T18:44:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3714#issuecomment-26363",
    "user": "mabshoff"
}
```

William opened #3715, so I am closing this as a dupe because of the better description at his ticket.

Cheers,

Michael



---

archive/issue_comments_026364.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-07-23T18:44:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3714#issuecomment-26364",
    "user": "mabshoff"
}
```

Resolution: duplicate
