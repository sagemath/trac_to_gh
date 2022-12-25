# Issue 2295: [with patch, positive review] build cache check fails on paths containing symlinks

archive/issues_002295.json:
```json
{
    "body": "Assignee: @burcin\n\nMy SAGE_ROOT contains a symlinked component, upgrading from 2.10.2.alpha0 to 2.10.2 failed with the error message in this thread:\n\nhttp://groups.google.com/group/sage-support/browse_thread/thread/d8ee3de015fbf7be\n\nOnly the filename listed was different.\n\nThis is caused by the module_path function in setup.py, assuming os.path.abspath starts with SAGE_ROOT, which is not the case when path contains a symlink. Attached patch fixes this issue.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2295\n\n",
    "closed_at": "2008-02-24T20:45:35Z",
    "created_at": "2008-02-24T20:00:54Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "[with patch, positive review] build cache check fails on paths containing symlinks",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2295",
    "user": "https://github.com/burcin"
}
```
Assignee: @burcin

My SAGE_ROOT contains a symlinked component, upgrading from 2.10.2.alpha0 to 2.10.2 failed with the error message in this thread:

http://groups.google.com/group/sage-support/browse_thread/thread/d8ee3de015fbf7be

Only the filename listed was different.

This is caused by the module_path function in setup.py, assuming os.path.abspath starts with SAGE_ROOT, which is not the case when path contains a symlink. Attached patch fixes this issue.



Issue created by migration from https://trac.sagemath.org/ticket/2295





---

archive/issue_comments_015190.json:
```json
{
    "body": "Attachment [build_cache_symlink.patch](tarball://root/attachments/some-uuid/ticket2295/build_cache_symlink.patch) by @burcin created at 2008-02-24 20:02:06\n\nfix build cache problem when sage_root has symlinks",
    "created_at": "2008-02-24T20:02:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2295",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2295#issuecomment-15190",
    "user": "https://github.com/burcin"
}
```

Attachment [build_cache_symlink.patch](tarball://root/attachments/some-uuid/ticket2295/build_cache_symlink.patch) by @burcin created at 2008-02-24 20:02:06

fix build cache problem when sage_root has symlinks



---

archive/issue_comments_015191.json:
```json
{
    "body": "I tested the patch with a non-symlinked $SAGE_ROOT and it keeps working. The problem has come up before and it is good that it has been finally fixed. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-24T20:44:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2295",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2295#issuecomment-15191",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I tested the patch with a non-symlinked $SAGE_ROOT and it keeps working. The problem has come up before and it is good that it has been finally fixed. Positive review.

Cheers,

Michael



---

archive/issue_comments_015192.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-24T20:45:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2295",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2295#issuecomment-15192",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_015193.json:
```json
{
    "body": "Merged in Sage 2.10.3.alpha0",
    "created_at": "2008-02-24T20:45:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2295",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2295#issuecomment-15193",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.3.alpha0



---

archive/issue_events_005417.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-24T20:45:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2295",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2295#event-5417"
}
```
