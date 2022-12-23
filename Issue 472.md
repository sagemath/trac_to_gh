# Issue 472: Drop dependencies on flex and bison

archive/issues_000472.json:
```json
{
    "body": "Assignee: jmbr\n\nTo build Singular we need flex and bison but we could make sure those programs are not needed by using some spkg-install trickery.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/472\n\n",
    "created_at": "2007-08-20T23:13:13Z",
    "labels": [
        "packages: standard",
        "minor",
        "enhancement"
    ],
    "title": "Drop dependencies on flex and bison",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/472",
    "user": "jmbr"
}
```
Assignee: jmbr

To build Singular we need flex and bison but we could make sure those programs are not needed by using some spkg-install trickery.


Issue created by migration from https://trac.sagemath.org/ticket/472





---

archive/issue_comments_002359.json:
```json
{
    "body": "Replying to [ticket:472 jmbr]:\n> To build Singular we need flex and bison but we could make sure those programs are not needed by using some spkg-install trickery.\n\nMake will invoke flex and bison if the *.[ly] files are newer than the C++ files they generate.  Thus, we have to make sure the C++ files are fresher.",
    "created_at": "2007-08-23T00:04:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/472#issuecomment-2359",
    "user": "jmbr"
}
```

Replying to [ticket:472 jmbr]:
> To build Singular we need flex and bison but we could make sure those programs are not needed by using some spkg-install trickery.

Make will invoke flex and bison if the *.[ly] files are newer than the C++ files they generate.  Thus, we have to make sure the C++ files are fresher.



---

archive/issue_comments_002360.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2007-08-23T00:04:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/472#issuecomment-2360",
    "user": "jmbr"
}
```

Resolution: worksforme



---

archive/issue_comments_002361.json:
```json
{
    "body": "This is not closed, since there isn't a singular spkg yet that implements it.",
    "created_at": "2007-08-29T03:43:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/472#issuecomment-2361",
    "user": "was"
}
```

This is not closed, since there isn't a singular spkg yet that implements it.



---

archive/issue_comments_002362.json:
```json
{
    "body": "Resolution changed from worksforme to ",
    "created_at": "2007-08-29T03:43:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/472#issuecomment-2362",
    "user": "was"
}
```

Resolution changed from worksforme to 



---

archive/issue_comments_002363.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-08-29T03:43:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/472#issuecomment-2363",
    "user": "was"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_002364.json:
```json
{
    "body": "If malb's new singular.spkg goes in this is resolved.\n\nCheers,\n\nMichael",
    "created_at": "2007-08-29T21:08:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/472#issuecomment-2364",
    "user": "mabshoff"
}
```

If malb's new singular.spkg goes in this is resolved.

Cheers,

Michael



---

archive/issue_comments_002365.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-29T21:13:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/472#issuecomment-2365",
    "user": "was"
}
```

Resolution: fixed
