# Issue 1109: [with patch] gp interface raises stack overflow exception if gp stack exceeds available memory

archive/issues_001109.json:
```json
{
    "body": "Assignee: was\n\nThe gp interface automatically runs allocatemem() to double the Pari stack size if it gets a response back from gp that includes \"the PARI stack overflows\", and then re-executes the failing command.  However, if gp cannot grow the stack further, allocatemem() will simply print a warning message and do nothing; then the interface gets stuck in a loop.  (This gives a stack overflow, rather than an infinite loop, because the re-execution is handled by a recursive call.)\n\nI'm attaching a patch that shows one way to fix this; it notices when allocatemem() fails and simply returns the original stack-overflow error message.  (I'm not sure if this is the best approach; would it be better to raise an exception here?  Somebody familiar with the gp interface should comment.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/1109\n\n",
    "created_at": "2007-11-06T02:43:37Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "title": "[with patch] gp interface raises stack overflow exception if gp stack exceeds available memory",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1109",
    "user": "cwitty"
}
```
Assignee: was

The gp interface automatically runs allocatemem() to double the Pari stack size if it gets a response back from gp that includes "the PARI stack overflows", and then re-executes the failing command.  However, if gp cannot grow the stack further, allocatemem() will simply print a warning message and do nothing; then the interface gets stuck in a loop.  (This gives a stack overflow, rather than an infinite loop, because the re-execution is handled by a recursive call.)

I'm attaching a patch that shows one way to fix this; it notices when allocatemem() fails and simply returns the original stack-overflow error message.  (I'm not sure if this is the best approach; would it be better to raise an exception here?  Somebody familiar with the gp interface should comment.)

Issue created by migration from https://trac.sagemath.org/ticket/1109





---

archive/issue_comments_006711.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-11-06T02:44:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1109#issuecomment-6711",
    "user": "cwitty"
}
```

Attachment



---

archive/issue_comments_006712.json:
```json
{
    "body": "On William's advice, I've revised my patch to raise an exception.  The new patch is 1109b.patch, which should be applied instead of 1109.patch.",
    "created_at": "2007-11-06T03:56:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1109#issuecomment-6712",
    "user": "cwitty"
}
```

On William's advice, I've revised my patch to raise an exception.  The new patch is 1109b.patch, which should be applied instead of 1109.patch.



---

archive/issue_comments_006713.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-06T22:16:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1109#issuecomment-6713",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_006714.json:
```json
{
    "body": "Attachment\n\napplied to 2.8.12.rc0",
    "created_at": "2007-11-06T22:16:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1109#issuecomment-6714",
    "user": "mabshoff"
}
```

Attachment

applied to 2.8.12.rc0
