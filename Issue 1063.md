# Issue 1063: [with patch] "sage -sh" should run $SHELL with Sage environment variables set

archive/issues_001063.json:
```json
{
    "body": "Assignee: @williamstein\n\nAfter the patch, this works:\n\n```\ncwitty@magnetar:~/sage$ ./sage -sh\nStarting subshell with Sage environment variables set:\ncwitty@magnetar:~/sage$ echo $SAGE_LOCAL\n/home/cwitty/sage/local\ncwitty@magnetar:~/sage$ exit\nexit\nExited Sage subshell.\n```\n\n\nI also patch sage-spkg, to change the error message it prints on failed package installs:\n\n```\nIf you want to try to fix the problem, yourself *don't* just cd to\n/home/cwitty/sage/spkg/build/genus2reduction-0.3 and type 'make'.\nInstead type \"/home/cwitty/sage/sage -sh\"\nin order to set all environment variables correctly, then cd to\n/home/cwitty/sage/spkg/build/genus2reduction-0.3\n(When you are done debugging, you can type \"exit\" to leave the\nsubshell.)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1063\n\n",
    "created_at": "2007-11-02T01:56:46Z",
    "labels": [
        "component: user interface"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.11",
    "title": "[with patch] \"sage -sh\" should run $SHELL with Sage environment variables set",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1063",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: @williamstein

After the patch, this works:

```
cwitty@magnetar:~/sage$ ./sage -sh
Starting subshell with Sage environment variables set:
cwitty@magnetar:~/sage$ echo $SAGE_LOCAL
/home/cwitty/sage/local
cwitty@magnetar:~/sage$ exit
exit
Exited Sage subshell.
```


I also patch sage-spkg, to change the error message it prints on failed package installs:

```
If you want to try to fix the problem, yourself *don't* just cd to
/home/cwitty/sage/spkg/build/genus2reduction-0.3 and type 'make'.
Instead type "/home/cwitty/sage/sage -sh"
in order to set all environment variables correctly, then cd to
/home/cwitty/sage/spkg/build/genus2reduction-0.3
(When you are done debugging, you can type "exit" to leave the
subshell.)
```


Issue created by migration from https://trac.sagemath.org/ticket/1063





---

archive/issue_comments_006436.json:
```json
{
    "body": "Attachment [sage-sh.patch](tarball://root/attachments/some-uuid/ticket1063/sage-sh.patch) by cwitty created at 2007-11-02 01:56:56",
    "created_at": "2007-11-02T01:56:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1063#issuecomment-6436",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [sage-sh.patch](tarball://root/attachments/some-uuid/ticket1063/sage-sh.patch) by cwitty created at 2007-11-02 01:56:56



---

archive/issue_comments_006437.json:
```json
{
    "body": "applied to 2.8.11.rc1",
    "created_at": "2007-11-02T02:26:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1063#issuecomment-6437",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

applied to 2.8.11.rc1



---

archive/issue_events_001185.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2007-11-02T02:26:17Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1063",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1063#event-1185"
}
```



---

archive/issue_comments_006438.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-02T02:26:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1063#issuecomment-6438",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
