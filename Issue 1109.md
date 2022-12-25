# Issue 1109: [with patch] gp interface raises stack overflow exception if gp stack exceeds available memory

archive/issues_001109.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe gp interface automatically runs allocatemem() to double the Pari stack size if it gets a response back from gp that includes \"the PARI stack overflows\", and then re-executes the failing command.  However, if gp cannot grow the stack further, allocatemem() will simply print a warning message and do nothing; then the interface gets stuck in a loop.  (This gives a stack overflow, rather than an infinite loop, because the re-execution is handled by a recursive call.)\n\nI'm attaching a patch that shows one way to fix this; it notices when allocatemem() fails and simply returns the original stack-overflow error message.  (I'm not sure if this is the best approach; would it be better to raise an exception here?  Somebody familiar with the gp interface should comment.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/1109\n\n",
    "created_at": "2007-11-06T02:43:37Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.12",
    "title": "[with patch] gp interface raises stack overflow exception if gp stack exceeds available memory",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1109",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: @williamstein

The gp interface automatically runs allocatemem() to double the Pari stack size if it gets a response back from gp that includes "the PARI stack overflows", and then re-executes the failing command.  However, if gp cannot grow the stack further, allocatemem() will simply print a warning message and do nothing; then the interface gets stuck in a loop.  (This gives a stack overflow, rather than an infinite loop, because the re-execution is handled by a recursive call.)

I'm attaching a patch that shows one way to fix this; it notices when allocatemem() fails and simply returns the original stack-overflow error message.  (I'm not sure if this is the best approach; would it be better to raise an exception here?  Somebody familiar with the gp interface should comment.)

Issue created by migration from https://trac.sagemath.org/ticket/1109





---

archive/issue_comments_006691.json:
```json
{
    "body": "Attachment [1109.patch](tarball://root/attachments/some-uuid/ticket1109/1109.patch) by cwitty created at 2007-11-06 02:44:46",
    "created_at": "2007-11-06T02:44:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1109#issuecomment-6691",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [1109.patch](tarball://root/attachments/some-uuid/ticket1109/1109.patch) by cwitty created at 2007-11-06 02:44:46



---

archive/issue_comments_006692.json:
```json
{
    "body": "On William's advice, I've revised my patch to raise an exception.  The new patch is 1109b.patch, which should be applied instead of 1109.patch.",
    "created_at": "2007-11-06T03:56:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1109#issuecomment-6692",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

On William's advice, I've revised my patch to raise an exception.  The new patch is 1109b.patch, which should be applied instead of 1109.patch.



---

archive/issue_comments_006693.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-06T22:16:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1109#issuecomment-6693",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_002972.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-11-06T22:16:20Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1109",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1109#event-2972"
}
```



---

archive/issue_comments_006694.json:
```json
{
    "body": "Attachment [1109b.patch](tarball://root/attachments/some-uuid/ticket1109/1109b.patch) by mabshoff created at 2007-11-06 22:16:20\n\napplied to 2.8.12.rc0",
    "created_at": "2007-11-06T22:16:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1109#issuecomment-6694",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [1109b.patch](tarball://root/attachments/some-uuid/ticket1109/1109b.patch) by mabshoff created at 2007-11-06 22:16:20

applied to 2.8.12.rc0
