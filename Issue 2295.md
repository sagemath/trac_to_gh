# Issue 2295: [with patch, needs review] build cache check fails on paths containing symlinks

archive/issues_002295.json:
```json
{
    "body": "Assignee: burcin\n\nMy SAGE_ROOT contains a symlinked component, upgrading from 2.10.2.alpha0 to 2.10.2 failed with the error message in this thread:\n\nhttp://groups.google.com/group/sage-support/browse_thread/thread/d8ee3de015fbf7be\n\nOnly the filename listed was different.\n\nThis is caused by the module_path function in setup.py, assuming os.path.abspath starts with SAGE_ROOT, which is not the case when path contains a symlink. Attached patch fixes this issue.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2295\n\n",
    "created_at": "2008-02-24T20:00:54Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] build cache check fails on paths containing symlinks",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2295",
    "user": "burcin"
}
```
Assignee: burcin

My SAGE_ROOT contains a symlinked component, upgrading from 2.10.2.alpha0 to 2.10.2 failed with the error message in this thread:

http://groups.google.com/group/sage-support/browse_thread/thread/d8ee3de015fbf7be

Only the filename listed was different.

This is caused by the module_path function in setup.py, assuming os.path.abspath starts with SAGE_ROOT, which is not the case when path contains a symlink. Attached patch fixes this issue.



Issue created by migration from https://trac.sagemath.org/ticket/2295





---

archive/issue_comments_015223.json:
```json
{
    "body": "Attachment\n\nfix build cache problem when sage_root has symlinks",
    "created_at": "2008-02-24T20:02:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2295",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2295#issuecomment-15223",
    "user": "burcin"
}
```

Attachment

fix build cache problem when sage_root has symlinks



---

archive/issue_comments_015224.json:
```json
{
    "body": "I tested the patch with a non-symlinked $SAGE_ROOT and it keeps working. The problem has come up before and it is good that it has been finally fixed. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-24T20:44:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2295",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2295#issuecomment-15224",
    "user": "mabshoff"
}
```

I tested the patch with a non-symlinked $SAGE_ROOT and it keeps working. The problem has come up before and it is good that it has been finally fixed. Positive review.

Cheers,

Michael



---

archive/issue_comments_015225.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-24T20:45:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2295",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2295#issuecomment-15225",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_015226.json:
```json
{
    "body": "Merged in Sage 2.10.3.alpha0",
    "created_at": "2008-02-24T20:45:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2295",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2295#issuecomment-15226",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.3.alpha0
