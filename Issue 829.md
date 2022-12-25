# Issue 829: edit() always puts the editor into the background

archive/issues_000829.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe new edit() command in SAGE forces the chosen editor into the background.  I'm not sure of the ramifications, but I have a change to the command that does the following: if DISPLAY is set in the user's environment, the assumption is that the editor will work with X (the window system).  Since the default 'emacs' in Mac OS X does not work with X, the result is that edit() terminates prematurely, complaining that standard output is not a tty.\n\nMy fix is to retain the current behavior only if DISPLAY is set.  Otherwise, the editor command is invoked as a \"foreground\" task, not a background task.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/829\n\n",
    "created_at": "2007-10-05T05:57:41Z",
    "labels": [
        "component: user interface",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "edit() always puts the editor into the background",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/829",
    "user": "https://trac.sagemath.org/admin/accounts/users/justin"
}
```
Assignee: @williamstein

The new edit() command in SAGE forces the chosen editor into the background.  I'm not sure of the ramifications, but I have a change to the command that does the following: if DISPLAY is set in the user's environment, the assumption is that the editor will work with X (the window system).  Since the default 'emacs' in Mac OS X does not work with X, the result is that edit() terminates prematurely, complaining that standard output is not a tty.

My fix is to retain the current behavior only if DISPLAY is set.  Otherwise, the editor command is invoked as a "foreground" task, not a background task.


Issue created by migration from https://trac.sagemath.org/ticket/829





---

archive/issue_comments_005117.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2007-10-05T05:58:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/829#issuecomment-5117",
    "user": "https://trac.sagemath.org/admin/accounts/users/justin"
}
```

Resolution: invalid



---

archive/issue_comments_005118.json:
```json
{
    "body": "FIddle.  Somehow, I submitted it twice.  Somehow, I submitted it twice.",
    "created_at": "2007-10-05T05:58:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/829#issuecomment-5118",
    "user": "https://trac.sagemath.org/admin/accounts/users/justin"
}
```

FIddle.  Somehow, I submitted it twice.  Somehow, I submitted it twice.



---

archive/issue_comments_005119.json:
```json
{
    "body": "Resolution changed from invalid to ",
    "created_at": "2007-10-05T22:41:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/829#issuecomment-5119",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution changed from invalid to 



---

archive/issue_comments_005120.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-10-05T22:41:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/829#issuecomment-5120",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_005121.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2007-10-05T22:41:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/829#issuecomment-5121",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: invalid
