# Issue 5016: bump ecmgmp, make libecm extension depend on local/include/ecm.h

archive/issues_005016.json:
```json
{
    "body": "Assignee: mabshoff\n\nAs the above states. Note that this is required to force a rebuild due to the MPIR update from #4966.\n\nSpkg and patch coming up shortly.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5016\n\n",
    "created_at": "2009-01-18T16:58:00Z",
    "labels": [
        "packages: standard",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "bump ecmgmp, make libecm extension depend on local/include/ecm.h",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5016",
    "user": "mabshoff"
}
```
Assignee: mabshoff

As the above states. Note that this is required to force a rebuild due to the MPIR update from #4966.

Spkg and patch coming up shortly.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5016





---

archive/issue_comments_038220.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-18T16:58:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5016",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5016#issuecomment-38220",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_038221.json:
```json
{
    "body": "The updated spkg is at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/alpha0/ecm-6.2.1.p0.spkg\n\nThere are no functional changes. The patch to make it depend on the ecm header is already in Sage.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-19T10:54:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5016",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5016#issuecomment-38221",
    "user": "mabshoff"
}
```

The updated spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/alpha0/ecm-6.2.1.p0.spkg

There are no functional changes. The patch to make it depend on the ecm header is already in Sage.

Cheers,

Michael



---

archive/issue_comments_038222.json:
```json
{
    "body": "Looks fine.",
    "created_at": "2009-01-19T10:56:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5016",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5016#issuecomment-38222",
    "user": "mhansen"
}
```

Looks fine.



---

archive/issue_comments_038223.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-19T11:10:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5016",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5016#issuecomment-38223",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_038224.json:
```json
{
    "body": "Merged in Sage 3.3.alpha0",
    "created_at": "2009-01-19T11:10:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5016",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5016#issuecomment-38224",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha0
