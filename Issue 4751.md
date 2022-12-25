# Issue 4751: if spkg/standard contains an extracted directory then "sage -upgrade" fails in multiple ways

archive/issues_004751.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\n  File \"/home/was/build/sage-3.2.2.alpha0/local/bin/sage-update\", line 178, in do_update\n    if 'Placeholder spkg file' in open(F).readline():\nIOError: [Errno 21] Is a directory\nError getting new packages!\nwas@sage:~/build/sage-3.2.2.alpha0$ \n```\n\n\nAlso, later it would try to move the directory out of the way, which will fail.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4751\n\n",
    "created_at": "2008-12-10T13:28:03Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "if spkg/standard contains an extracted directory then \"sage -upgrade\" fails in multiple ways",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4751",
    "user": "https://github.com/williamstein"
}
```
Assignee: mabshoff


```
  File "/home/was/build/sage-3.2.2.alpha0/local/bin/sage-update", line 178, in do_update
    if 'Placeholder spkg file' in open(F).readline():
IOError: [Errno 21] Is a directory
Error getting new packages!
was@sage:~/build/sage-3.2.2.alpha0$ 
```


Also, later it would try to move the directory out of the way, which will fail.

Issue created by migration from https://trac.sagemath.org/ticket/4751





---

archive/issue_comments_035882.json:
```json
{
    "body": "Attachment [trac_4751.patch](tarball://root/attachments/some-uuid/ticket4751/trac_4751.patch) by @williamstein created at 2008-12-10 13:40:29",
    "created_at": "2008-12-10T13:40:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4751#issuecomment-35882",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_4751.patch](tarball://root/attachments/some-uuid/ticket4751/trac_4751.patch) by @williamstein created at 2008-12-10 13:40:29



---

archive/issue_comments_035883.json:
```json
{
    "body": "Looks good to me.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-11T11:14:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4751#issuecomment-35883",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Looks good to me.

Cheers,

Michael



---

archive/issue_comments_035884.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-11T11:15:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4751#issuecomment-35884",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_035885.json:
```json
{
    "body": "Merged in Sage 3.2.2.alpha2",
    "created_at": "2008-12-11T11:15:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4751#issuecomment-35885",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.2.alpha2



---

archive/issue_events_004994.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-11T11:15:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4751",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4751#event-4994"
}
```
