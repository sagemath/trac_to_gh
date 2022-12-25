# Issue 1683: sage -t cubegroup.py & stops instead of running in background

archive/issues_001683.json:
```json
{
    "body": "Assignee: @williamstein\n\nWhen running sage -t cubegroup.py & (to run it in the background), the process is stopped.\n\nThis is caused by pexpect.sendeof() (called from rubik.py) calling termios.tcsetattr() on stdin which causes the process to be stopped with a SIGTTOU (=write to tty from a background process).\n\nThe pexpect.sendeof() function has been entirely changed in the current version of pexpect, and using that new sendeof() fixes this problem. So, updating to a newer pexpect (ticket #502) should fix this as well.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1683\n\n",
    "created_at": "2008-01-04T22:38:30Z",
    "labels": [
        "component: interfaces",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.11",
    "title": "sage -t cubegroup.py & stops instead of running in background",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1683",
    "user": "https://github.com/wjp"
}
```
Assignee: @williamstein

When running sage -t cubegroup.py & (to run it in the background), the process is stopped.

This is caused by pexpect.sendeof() (called from rubik.py) calling termios.tcsetattr() on stdin which causes the process to be stopped with a SIGTTOU (=write to tty from a background process).

The pexpect.sendeof() function has been entirely changed in the current version of pexpect, and using that new sendeof() fixes this problem. So, updating to a newer pexpect (ticket #502) should fix this as well.

Issue created by migration from https://trac.sagemath.org/ticket/1683





---

archive/issue_comments_010663.json:
```json
{
    "body": "This issue was reported by William Stein on IRC.",
    "created_at": "2008-01-04T22:50:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1683#issuecomment-10663",
    "user": "https://github.com/wjp"
}
```

This issue was reported by William Stein on IRC.



---

archive/issue_comments_010664.json:
```json
{
    "body": "a temporary workaround for linux only by William",
    "created_at": "2008-01-04T23:28:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1683#issuecomment-10664",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

a temporary workaround for linux only by William



---

archive/issue_comments_010665.json:
```json
{
    "body": "Attachment [trac-1683-partial.patch](tarball://root/attachments/some-uuid/ticket1683/trac-1683-partial.patch) by mabshoff created at 2008-01-04 23:29:14\n\nI merged trac-1683-partial.patch into Sage 2.9.2.rc1. But the ticket remains open for now since the workaround doesn't work on OSX.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-04T23:29:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1683#issuecomment-10665",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac-1683-partial.patch](tarball://root/attachments/some-uuid/ticket1683/trac-1683-partial.patch) by mabshoff created at 2008-01-04 23:29:14

I merged trac-1683-partial.patch into Sage 2.9.2.rc1. But the ticket remains open for now since the workaround doesn't work on OSX.

Cheers,

Michael



---

archive/issue_comments_010666.json:
```json
{
    "body": "I suggest that we can close this ticket now with the new doctest system.",
    "created_at": "2013-07-22T13:51:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1683#issuecomment-10666",
    "user": "https://github.com/mwhansen"
}
```

I suggest that we can close this ticket now with the new doctest system.



---

archive/issue_comments_010667.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2013-07-22T13:51:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1683#issuecomment-10667",
    "user": "https://github.com/mwhansen"
}
```

Resolution: invalid
