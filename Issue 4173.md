# Issue 4173: [with spkg, needs review] Solaris: fix cddlib build problem on Solaris x86

archive/issues_004173.json:
```json
{
    "body": "Assignee: mabshoff\n\nLL and SS are reserved numerical constants on Solaris, but cddlib uses them in allface.c The spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.3/alpha1/cddlib-094b.p3.spkg\n\nrenames them so that the spkg now builds out of the box on Solaris.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4173\n\n",
    "created_at": "2008-09-23T06:41:00Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "[with spkg, needs review] Solaris: fix cddlib build problem on Solaris x86",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4173",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

LL and SS are reserved numerical constants on Solaris, but cddlib uses them in allface.c The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.3/alpha1/cddlib-094b.p3.spkg

renames them so that the spkg now builds out of the box on Solaris.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4173





---

archive/issue_comments_030217.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-23T06:41:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4173#issuecomment-30217",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_030218.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-09-23T21:25:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4173#issuecomment-30218",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_030219.json:
```json
{
    "body": "Merged in Sage 3.1.3.alpha1",
    "created_at": "2008-09-23T22:01:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4173#issuecomment-30219",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.3.alpha1



---

archive/issue_comments_030220.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-23T22:01:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4173#issuecomment-30220",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
