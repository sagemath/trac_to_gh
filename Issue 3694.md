# Issue 3694: Update FLINT to the 1.0.13 release

archive/issues_003694.json:
```json
{
    "body": "Assignee: tbd\n\nSeveral issues were fixed, among them a bug that could in some rather unlikely cases cause random memory to be accessed.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/3694\n\n",
    "created_at": "2008-07-21T17:58:02Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.6",
    "title": "Update FLINT to the 1.0.13 release",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3694",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: tbd

Several issues were fixed, among them a bug that could in some rather unlikely cases cause random memory to be accessed.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/3694





---

archive/issue_comments_026154.json:
```json
{
    "body": "The spkg is at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.6/alpha1/flint-1.0.13.spkg\n\nMake sure to rebuild the following extension by running\n\n```\ntouch devel/sage/sage/rings/polynomial/polynomial_integer_dense_flint.pyx\n./sage -b\n```\n\nOtherwise Sage will complain about an import error. The fix is non-trivial and needs to be coordinated with the packaging teams for Debian and Gentoo, so it is post 3.0.6 material.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-21T18:12:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3694#issuecomment-26154",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.6/alpha1/flint-1.0.13.spkg

Make sure to rebuild the following extension by running

```
touch devel/sage/sage/rings/polynomial/polynomial_integer_dense_flint.pyx
./sage -b
```

Otherwise Sage will complain about an import error. The fix is non-trivial and needs to be coordinated with the packaging teams for Debian and Gentoo, so it is post 3.0.6 material.

Cheers,

Michael



---

archive/issue_comments_026155.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-07-21T18:12:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3694#issuecomment-26155",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_026156.json:
```json
{
    "body": "Changing assignee from tbd to mabshoff.",
    "created_at": "2008-07-21T18:12:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3694#issuecomment-26156",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from tbd to mabshoff.



---

archive/issue_comments_026157.json:
```json
{
    "body": "Changing component from algebra to build.",
    "created_at": "2008-07-21T18:12:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3694#issuecomment-26157",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing component from algebra to build.



---

archive/issue_comments_026158.json:
```json
{
    "body": "Also make sure to \n\n```\ntouch devel/sage/sage/libs/flint/fmpz_poly.pyx\n./sage -b\n```\n\nI knew there were *two* of those suckers to rebuild.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-21T18:34:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3694#issuecomment-26158",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Also make sure to 

```
touch devel/sage/sage/libs/flint/fmpz_poly.pyx
./sage -b
```

I knew there were *two* of those suckers to rebuild.

Cheers,

Michael



---

archive/issue_comments_026159.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-21T22:20:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3694#issuecomment-26159",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_003916.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-07-21T22:20:39Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3694",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3694#event-3916"
}
```



---

archive/issue_comments_026160.json:
```json
{
    "body": "Merged in Sage 3.0.6.rc0",
    "created_at": "2008-07-21T22:20:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3694#issuecomment-26160",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.6.rc0
