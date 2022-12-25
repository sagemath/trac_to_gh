# Issue 3002: A lot of  spkgs check for fortran even if they don't need it

archive/issues_003002.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\nA lot of configure scripts seem to check for\nfortran, even if they don't use it. It appears the relevant\nenvironment variables are F77 and FFLAGS. Anyway, the variable\nSAGE_FORTRAN seems to be honored fine for the packages that actually\nneed fortran.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3002\n\n",
    "created_at": "2008-04-22T16:52:04Z",
    "labels": [
        "component: spkg-check",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.1",
    "title": "A lot of  spkgs check for fortran even if they don't need it",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3002",
    "user": "https://github.com/dfdeshom"
}
```
Assignee: mabshoff


```
A lot of configure scripts seem to check for
fortran, even if they don't use it. It appears the relevant
environment variables are F77 and FFLAGS. Anyway, the variable
SAGE_FORTRAN seems to be honored fine for the packages that actually
need fortran.
```


Issue created by migration from https://trac.sagemath.org/ticket/3002





---

archive/issue_comments_020612.json:
```json
{
    "body": "Changing component from spkg-check to packages.",
    "created_at": "2008-04-22T16:54:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3002#issuecomment-20612",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing component from spkg-check to packages.



---

archive/issue_comments_020613.json:
```json
{
    "body": "This is not the case and if we don't use an F77 compiler we shouldn't use the F77 env variable. The fact that a lot of them check for a Fortran compiler and don't use them is also something that doesn't matter since the configure process will not fail. So, the whole ticket is clearly \"won't fix\" to me.\n\nThoughts?\n\nCheers,\n\nMichael",
    "created_at": "2008-04-22T16:54:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3002#issuecomment-20613",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is not the case and if we don't use an F77 compiler we shouldn't use the F77 env variable. The fact that a lot of them check for a Fortran compiler and don't use them is also something that doesn't matter since the configure process will not fail. So, the whole ticket is clearly "won't fix" to me.

Thoughts?

Cheers,

Michael



---

archive/issue_comments_020614.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2008-04-22T17:08:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3002#issuecomment-20614",
    "user": "https://github.com/williamstein"
}
```

Resolution: wontfix



---

archive/issue_events_003207.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2008-04-22T17:08:48Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3002",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3002#event-3207"
}
```
