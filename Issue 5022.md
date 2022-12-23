# Issue 5022: Solaris 10: update libgcrypt to 1.4.3

archive/issues_005022.json:
```json
{
    "body": "Assignee: mabshoff\n\nThe update fixes two important issues:\n\n* padlock support has been fixed, so we don't need to disable it\n* gcrypt no longer needs huge amounts of entropy which made key generation a pain. The bug was introduced in gcrypt 1.4 and affected Solaris among other platforms.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5022\n\n",
    "created_at": "2009-01-19T10:16:45Z",
    "labels": [
        "porting: Solaris",
        "critical",
        "bug"
    ],
    "title": "Solaris 10: update libgcrypt to 1.4.3",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5022",
    "user": "mabshoff"
}
```
Assignee: mabshoff

The update fixes two important issues:

* padlock support has been fixed, so we don't need to disable it
* gcrypt no longer needs huge amounts of entropy which made key generation a pain. The bug was introduced in gcrypt 1.4 and affected Solaris among other platforms.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5022





---

archive/issue_comments_038250.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-19T10:33:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5022",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5022#issuecomment-38250",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_038251.json:
```json
{
    "body": "The updated spkg can be found at\n\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/alpha0/libgcrypt-1.4.3.spkg\n\nCheers,\n\nMichael",
    "created_at": "2009-01-19T10:33:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5022",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5022#issuecomment-38251",
    "user": "mabshoff"
}
```

The updated spkg can be found at


http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/alpha0/libgcrypt-1.4.3.spkg

Cheers,

Michael



---

archive/issue_comments_038252.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-01-19T10:37:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5022",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5022#issuecomment-38252",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_038253.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-19T10:42:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5022",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5022#issuecomment-38253",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_038254.json:
```json
{
    "body": "Merged in Sage 3.3.alpha0",
    "created_at": "2009-01-19T10:42:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5022",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5022#issuecomment-38254",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha0
