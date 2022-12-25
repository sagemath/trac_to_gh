# Issue 3926: [with spkg, needs review] fix Macaulay2 building

archive/issues_003926.json:
```json
{
    "body": "Assignee: mabshoff\n\nI've uploaded a new SPKG for M2 to:\n\n  http://sage.math.washington.edu/home/malb/spkgs/macaulay2-1.1-r7210.p1.spkg\n\nwhich fixes a couple of compilation problems:\n\n* UNAME might not be defined\n* some standard headers are not included in `overflow.hpp`\n\nIssue created by migration from https://trac.sagemath.org/ticket/3926\n\n",
    "created_at": "2008-08-22T12:29:12Z",
    "labels": [
        "component: packages: standard",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "[with spkg, needs review] fix Macaulay2 building",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3926",
    "user": "https://github.com/malb"
}
```
Assignee: mabshoff

I've uploaded a new SPKG for M2 to:

  http://sage.math.washington.edu/home/malb/spkgs/macaulay2-1.1-r7210.p1.spkg

which fixes a couple of compilation problems:

* UNAME might not be defined
* some standard headers are not included in `overflow.hpp`

Issue created by migration from https://trac.sagemath.org/ticket/3926





---

archive/issue_comments_028046.json:
```json
{
    "body": "Positive review. A couple remarks:\n\n* The fixes malb did should go upstream.\n* I fixed the boehm_gc and gdbm detection code since it only works for default spkgs and not optional ones - my bad.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-25T04:58:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3926#issuecomment-28046",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review. A couple remarks:

* The fixes malb did should go upstream.
* I fixed the boehm_gc and gdbm detection code since it only works for default spkgs and not optional ones - my bad.

Cheers,

Michael



---

archive/issue_comments_028047.json:
```json
{
    "body": "Oops, I forgot to mention that the updated spkg is at \n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/alpha1/macaulay2-1.1-r7210.p1.spkg\n\nCheers,\n\nMichael",
    "created_at": "2008-08-25T04:59:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3926#issuecomment-28047",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Oops, I forgot to mention that the updated spkg is at 

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/alpha1/macaulay2-1.1-r7210.p1.spkg

Cheers,

Michael



---

archive/issue_comments_028048.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha1",
    "created_at": "2008-08-25T04:59:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3926#issuecomment-28048",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.2.alpha1



---

archive/issue_events_004151.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-08-25T04:59:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3926",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3926#event-4151"
}
```



---

archive/issue_comments_028049.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-25T04:59:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3926#issuecomment-28049",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
