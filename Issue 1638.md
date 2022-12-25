# Issue 1638: FreeBSD: change "/bin/bash" to "/usr/bin/env bash"

archive/issues_001638.json:
```json
{
    "body": "Assignee: mabshoff\n\nKeywords: FreeBSD\n\nOn FreeBSD the default bash installtion location is `/neusr/local`. Hence all our shell scripts with `/bin/bash` will break. The solution is to use `/usr/bin/env bash` instead. The same might apply to python and perl scripts.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1638\n\n",
    "created_at": "2007-12-30T12:57:41Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "FreeBSD: change \"/bin/bash\" to \"/usr/bin/env bash\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1638",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

Keywords: FreeBSD

On FreeBSD the default bash installtion location is `/neusr/local`. Hence all our shell scripts with `/bin/bash` will break. The solution is to use `/usr/bin/env bash` instead. The same might apply to python and perl scripts.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1638





---

archive/issue_comments_010388.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-31T10:26:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1638",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1638#issuecomment-10388",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_010389.json:
```json
{
    "body": "All known instances of /bin/bash have been fixed. So I am closing this and any new instances can be fixed via new tickets.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-25T04:16:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1638",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1638#issuecomment-10389",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

All known instances of /bin/bash have been fixed. So I am closing this and any new instances can be fixed via new tickets.

Cheers,

Michael



---

archive/issue_comments_010390.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-25T04:16:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1638",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1638#issuecomment-10390",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_001796.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-08-25T04:16:36Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1638",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1638#event-1796"
}
```
