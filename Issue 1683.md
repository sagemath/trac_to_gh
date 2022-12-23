# Issue 1683: sage -t cubegroup.py & stops instead of running in background

archive/issues_001683.json:
```json
{
    "body": "Assignee: was\n\nWhen running sage -t cubegroup.py & (to run it in the background), the process is stopped.\n\nThis is caused by pexpect.sendeof() (called from rubik.py) calling termios.tcsetattr() on stdin which causes the process to be stopped with a SIGTTOU (=write to tty from a background process).\n\nThe pexpect.sendeof() function has been entirely changed in the current version of pexpect, and using that new sendeof() fixes this problem. So, updating to a newer pexpect (ticket #502) should fix this as well.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1683\n\n",
    "created_at": "2008-01-04T22:38:30Z",
    "labels": [
        "interfaces",
        "minor",
        "bug"
    ],
    "title": "sage -t cubegroup.py & stops instead of running in background",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1683",
    "user": "wjp"
}
```
Assignee: was

When running sage -t cubegroup.py & (to run it in the background), the process is stopped.

This is caused by pexpect.sendeof() (called from rubik.py) calling termios.tcsetattr() on stdin which causes the process to be stopped with a SIGTTOU (=write to tty from a background process).

The pexpect.sendeof() function has been entirely changed in the current version of pexpect, and using that new sendeof() fixes this problem. So, updating to a newer pexpect (ticket #502) should fix this as well.

Issue created by migration from https://trac.sagemath.org/ticket/1683





---

archive/issue_comments_010690.json:
```json
{
    "body": "This issue was reported by William Stein on IRC.",
    "created_at": "2008-01-04T22:50:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1683#issuecomment-10690",
    "user": "wjp"
}
```

This issue was reported by William Stein on IRC.



---

archive/issue_comments_010691.json:
```json
{
    "body": "a temporary workaround for linux only by William",
    "created_at": "2008-01-04T23:28:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1683#issuecomment-10691",
    "user": "mabshoff"
}
```

a temporary workaround for linux only by William



---

archive/issue_comments_010692.json:
```json
{
    "body": "Attachment\n\nI merged trac-1683-partial.patch into Sage 2.9.2.rc1. But the ticket remains open for now since the workaround doesn't work on OSX.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-04T23:29:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1683#issuecomment-10692",
    "user": "mabshoff"
}
```

Attachment

I merged trac-1683-partial.patch into Sage 2.9.2.rc1. But the ticket remains open for now since the workaround doesn't work on OSX.

Cheers,

Michael



---

archive/issue_comments_010693.json:
```json
{
    "body": "I suggest that we can close this ticket now with the new doctest system.",
    "created_at": "2013-07-22T13:51:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1683#issuecomment-10693",
    "user": "mhansen"
}
```

I suggest that we can close this ticket now with the new doctest system.



---

archive/issue_comments_010694.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2013-07-22T13:51:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1683#issuecomment-10694",
    "user": "mhansen"
}
```

Resolution: invalid
