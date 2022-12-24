# Issue 2975: opening ports to conservative -- breaks on some os x systems

archive/issues_002975.json:
```json
{
    "body": "Assignee: boothby\n\non bsd.math and fermat this happens but shouldn't.  I'm sure it is my fault.\n\n\n```\nsage: inotebook()\nThe notebook files are stored in: /Users/was/.sage//sage_notebook\nWARNING: Running the notebook insecurely may be dangerous.\nMake sure you know what you are doing.\nPort 8000 is already in use.\nTrying next port...\nPort 8001 is already in use.\nTrying next port...\nPort 8002 is already in use.\nTrying next port...\nPort 8003 is already in use.\nTrying next port...\nPort 8004 is already in use.\nTrying next port...\nPort 8005 is already in use.\nTrying next port...\nPort 8006 is already in use.\nTrying next port...\nPort 8007 is already in use.\nTrying next port...\nPort 8008 is already in use.\nTrying next port...\nPort 8009 is already in use.\nTrying next port...\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2975\n\n",
    "created_at": "2008-04-20T21:09:11Z",
    "labels": [
        "notebook",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "opening ports to conservative -- breaks on some os x systems",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2975",
    "user": "was"
}
```
Assignee: boothby

on bsd.math and fermat this happens but shouldn't.  I'm sure it is my fault.


```
sage: inotebook()
The notebook files are stored in: /Users/was/.sage//sage_notebook
WARNING: Running the notebook insecurely may be dangerous.
Make sure you know what you are doing.
Port 8000 is already in use.
Trying next port...
Port 8001 is already in use.
Trying next port...
Port 8002 is already in use.
Trying next port...
Port 8003 is already in use.
Trying next port...
Port 8004 is already in use.
Trying next port...
Port 8005 is already in use.
Trying next port...
Port 8006 is already in use.
Trying next port...
Port 8007 is already in use.
Trying next port...
Port 8008 is already in use.
Trying next port...
Port 8009 is already in use.
Trying next port...
```


Issue created by migration from https://trac.sagemath.org/ticket/2975





---

archive/issue_comments_020499.json:
```json
{
    "body": "Attachment [sage-2975.patch](tarball://root/attachments/some-uuid/ticket2975/sage-2975.patch) by was created at 2008-04-20 21:52:55",
    "created_at": "2008-04-20T21:52:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2975",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2975#issuecomment-20499",
    "user": "was"
}
```

Attachment [sage-2975.patch](tarball://root/attachments/some-uuid/ticket2975/sage-2975.patch) by was created at 2008-04-20 21:52:55



---

archive/issue_comments_020500.json:
```json
{
    "body": "Works for me on 64-bit Linux.",
    "created_at": "2008-04-21T03:49:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2975",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2975#issuecomment-20500",
    "user": "mhansen"
}
```

Works for me on 64-bit Linux.



---

archive/issue_comments_020501.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-21T04:06:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2975",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2975#issuecomment-20501",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_020502.json:
```json
{
    "body": "Merged in Sage 3.0.rc1",
    "created_at": "2008-04-21T04:06:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2975",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2975#issuecomment-20502",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.rc1
