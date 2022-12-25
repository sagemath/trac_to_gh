# Issue 4188: [with spkg, needs review] Fix cvxopt.spkg build on Solaris due to broken complex.h headers

archive/issues_004188.json:
```json
{
    "body": "Assignee: mabshoff\n\ncomplex.h on Solaris is broken - see http://bugs.opensolaris.org/bugdatabase/view_bug.do?bug_id=6549313\n\nThis causes the build of cvxopt to fail. The spkg at \n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.3/alpha1/cvxopt-0.9.p7.spkg\n\nfixes that problem.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4188\n\n",
    "created_at": "2008-09-24T10:11:56Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "[with spkg, needs review] Fix cvxopt.spkg build on Solaris due to broken complex.h headers",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4188",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

complex.h on Solaris is broken - see http://bugs.opensolaris.org/bugdatabase/view_bug.do?bug_id=6549313

This causes the build of cvxopt to fail. The spkg at 

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.3/alpha1/cvxopt-0.9.p7.spkg

fixes that problem.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4188





---

archive/issue_comments_030328.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-24T10:12:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4188#issuecomment-30328",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_030329.json:
```json
{
    "body": "I tested on my machine, and it installs fine, and seems to work (doctests in `sage/numerical` all pass). Michael tells me that it also works on Sun, which was the issue, so that's what we needed.",
    "created_at": "2008-09-24T10:29:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4188#issuecomment-30329",
    "user": "https://github.com/craigcitro"
}
```

I tested on my machine, and it installs fine, and seems to work (doctests in `sage/numerical` all pass). Michael tells me that it also works on Sun, which was the issue, so that's what we needed.



---

archive/issue_events_004427.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-24T10:35:48Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4188",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4188#event-4427"
}
```



---

archive/issue_comments_030330.json:
```json
{
    "body": "Merged in Sage 3.1.3.alpha1",
    "created_at": "2008-09-24T10:35:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4188#issuecomment-30330",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.3.alpha1



---

archive/issue_comments_030331.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-24T10:35:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4188#issuecomment-30331",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
