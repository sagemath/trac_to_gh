# Issue 1638: FreeBSD: change "/bin/bash" to "/usr/bin/env bash"

archive/issues_001638.json:
```json
{
    "body": "Assignee: mabshoff\n\nKeywords: FreeBSD\n\nOn FreeBSD the default bash installtion location is `/neusr/local`. Hence all our shell scripts with `/bin/bash` will break. The solution is to use `/usr/bin/env bash` instead. The same might apply to python and perl scripts.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1638\n\n",
    "created_at": "2007-12-30T12:57:41Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "title": "FreeBSD: change \"/bin/bash\" to \"/usr/bin/env bash\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1638",
    "user": "mabshoff"
}
```
Assignee: mabshoff

Keywords: FreeBSD

On FreeBSD the default bash installtion location is `/neusr/local`. Hence all our shell scripts with `/bin/bash` will break. The solution is to use `/usr/bin/env bash` instead. The same might apply to python and perl scripts.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1638





---

archive/issue_comments_010415.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-31T10:26:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1638",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1638#issuecomment-10415",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_010416.json:
```json
{
    "body": "All known instances of /bin/bash have been fixed. So I am closing this and any new instances can be fixed via new tickets.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-25T04:16:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1638",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1638#issuecomment-10416",
    "user": "mabshoff"
}
```

All known instances of /bin/bash have been fixed. So I am closing this and any new instances can be fixed via new tickets.

Cheers,

Michael



---

archive/issue_comments_010417.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-25T04:16:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1638",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1638#issuecomment-10417",
    "user": "mabshoff"
}
```

Resolution: fixed
