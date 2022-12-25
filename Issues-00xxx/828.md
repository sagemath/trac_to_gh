# Issue 828: edit() always puts the editor into the background

archive/issues_000828.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe new edit() command in SAGE forces the chosen editor into the background.  I'm not sure of the ramifications, but I have a change to the command that does the following: if DISPLAY is set in the user's environment, the assumption is that the editor will work with X (the window system).  Since the default 'emacs' in Mac OS X does not work with X, the result is that edit() terminates prematurely, complaining that standard output is not a tty.\n\nMy fix is to retain the current behavior only if DISPLAY is set.  Otherwise, the editor command is invoked as a \"foreground\" task, not a background task.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/828\n\n",
    "closed_at": "2007-10-13T07:33:16Z",
    "created_at": "2007-10-05T05:56:32Z",
    "labels": [
        "component: user interface",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.7",
    "title": "edit() always puts the editor into the background",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/828",
    "user": "https://trac.sagemath.org/admin/accounts/users/justin"
}
```
Assignee: @williamstein

The new edit() command in SAGE forces the chosen editor into the background.  I'm not sure of the ramifications, but I have a change to the command that does the following: if DISPLAY is set in the user's environment, the assumption is that the editor will work with X (the window system).  Since the default 'emacs' in Mac OS X does not work with X, the result is that edit() terminates prematurely, complaining that standard output is not a tty.

My fix is to retain the current behavior only if DISPLAY is set.  Otherwise, the editor command is invoked as a "foreground" task, not a background task.


Issue created by migration from https://trac.sagemath.org/ticket/828





---

archive/issue_comments_005112.json:
```json
{
    "body": "Patch file fixing an edit() problem",
    "created_at": "2007-10-05T05:57:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/828#issuecomment-5112",
    "user": "https://trac.sagemath.org/admin/accounts/users/justin"
}
```

Patch file fixing an edit() problem



---

archive/issue_comments_005113.json:
```json
{
    "body": "Attachment [edit.patch](tarball://root/attachments/some-uuid/ticket828/edit.patch) by @nbruin created at 2007-10-05 07:43:29\n\nI don't think the DISPLAY variable is a good indication. Even when DISPLAY is set, if the editor is vi then running it in the background is a bad idea.\nI would propose:\n* if a full template is supplied, then take it as the user gives it\n* if you're trying to guess from the \"EDITOR\" variable, you'll have to look up\nhow to pass a line number anyway. For each of these editors you know whether an & makes sense, and this is independent of the &",
    "created_at": "2007-10-05T07:43:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/828#issuecomment-5113",
    "user": "https://github.com/nbruin"
}
```

Attachment [edit.patch](tarball://root/attachments/some-uuid/ticket828/edit.patch) by @nbruin created at 2007-10-05 07:43:29

I don't think the DISPLAY variable is a good indication. Even when DISPLAY is set, if the editor is vi then running it in the background is a bad idea.
I would propose:
* if a full template is supplied, then take it as the user gives it
* if you're trying to guess from the "EDITOR" variable, you'll have to look up
how to pass a line number anyway. For each of these editors you know whether an & makes sense, and this is independent of the &



---

archive/issue_comments_005114.json:
```json
{
    "body": "sorry. Why can't I edit my comments? I meant \"independent of the value of EDITOR\".",
    "created_at": "2007-10-05T07:44:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/828#issuecomment-5114",
    "user": "https://github.com/nbruin"
}
```

sorry. Why can't I edit my comments? I meant "independent of the value of EDITOR".



---

archive/issue_events_002332.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-10-06T17:38:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/828",
    "milestone": "sage-2.8.7",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/828#event-2332"
}
```



---

archive/issue_comments_005115.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2007-10-13T07:33:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/828#issuecomment-5115",
    "user": "https://github.com/williamstein"
}
```

Resolution: invalid



---

archive/issue_comments_005116.json:
```json
{
    "body": "I don't think this is needed -- it was only need for the old version...",
    "created_at": "2007-10-13T07:33:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/828#issuecomment-5116",
    "user": "https://github.com/williamstein"
}
```

I don't think this is needed -- it was only need for the old version...



---

archive/issue_events_002333.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-13T07:33:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/828",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/828#event-2333"
}
```
