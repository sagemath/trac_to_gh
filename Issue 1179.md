# Issue 1179: change all #!/bin/sh to #!/bin/bash in $SAGE_LOCAL/bin (Solaris related)

archive/issues_001179.json:
```json
{
    "body": "Assignee: mabshoff\n\nThis is related to Solaris:\n\nKlas writes:\n\n```\n\nI've tried started it from bash and tcsh, if that matters.\nBut please note that on Solaris /bin/sh is not bash, so\nif scripts start with\n\n#!/bin/sh\n\nsome things may not work as expected. \n```\n\n\nOn neron, i.e. William's Sun we replaced /bin/sh by /bin/bash because the original /bin/sh caused all kinds of problems during the build.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1179\n\n",
    "created_at": "2007-11-15T16:28:49Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "title": "change all #!/bin/sh to #!/bin/bash in $SAGE_LOCAL/bin (Solaris related)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1179",
    "user": "mabshoff"
}
```
Assignee: mabshoff

This is related to Solaris:

Klas writes:

```

I've tried started it from bash and tcsh, if that matters.
But please note that on Solaris /bin/sh is not bash, so
if scripts start with

#!/bin/sh

some things may not work as expected. 
```


On neron, i.e. William's Sun we replaced /bin/sh by /bin/bash because the original /bin/sh caused all kinds of problems during the build.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1179





---

archive/issue_comments_007280.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-11-15T16:28:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1179#issuecomment-7280",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_007281.json:
```json
{
    "body": "Attachment [bash.patch](tarball://root/attachments/some-uuid/ticket1179/bash.patch) by was created at 2007-12-02 02:56:34\n\nLooks good to me.",
    "created_at": "2007-12-02T02:56:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1179#issuecomment-7281",
    "user": "was"
}
```

Attachment [bash.patch](tarball://root/attachments/some-uuid/ticket1179/bash.patch) by was created at 2007-12-02 02:56:34

Looks good to me.



---

archive/issue_comments_007282.json:
```json
{
    "body": "Testall successful.",
    "created_at": "2007-12-02T03:59:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1179#issuecomment-7282",
    "user": "rlm"
}
```

Testall successful.



---

archive/issue_comments_007283.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-02T04:10:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1179#issuecomment-7283",
    "user": "mabshoff"
}
```

Resolution: fixed
