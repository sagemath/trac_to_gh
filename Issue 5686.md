# Issue 5686: mpi4py is very outdated

archive/issues_005686.json:
```json
{
    "body": "Assignee: mabshoff\n\nmpi4py in the optional package is version 0.3.1, while the newest version is 1.0.0.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5686\n\n",
    "created_at": "2009-04-04T22:55:34Z",
    "labels": [
        "component: optional packages",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "mpi4py is very outdated",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5686",
    "user": "https://github.com/syazdani77"
}
```
Assignee: mabshoff

mpi4py in the optional package is version 0.3.1, while the newest version is 1.0.0.

Issue created by migration from https://trac.sagemath.org/ticket/5686





---

archive/issue_comments_044385.json:
```json
{
    "body": "Changing component from optional packages to experimental package.",
    "created_at": "2009-04-04T23:08:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5686#issuecomment-44385",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing component from optional packages to experimental package.



---

archive/issue_comments_044386.json:
```json
{
    "body": "mpi4py is experimental, not optional.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-04T23:08:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5686#issuecomment-44386",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

mpi4py is experimental, not optional.

Cheers,

Michael



---

archive/issue_comments_044387.json:
```json
{
    "body": "I have an .spkg for this package now. Here is the link:\nhttp://sage.math.washington.edu/home/syazdani/mpi4py-1.0.0.spkg\n\nSoroosh",
    "created_at": "2009-04-05T19:29:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5686#issuecomment-44387",
    "user": "https://github.com/syazdani77"
}
```

I have an .spkg for this package now. Here is the link:
http://sage.math.washington.edu/home/syazdani/mpi4py-1.0.0.spkg

Soroosh



---

archive/issue_comments_044388.json:
```json
{
    "body": "I've created a new version here:\n\n  http://sage.math.washington.edu/home/wstein/patches/mpi4py-1.1.0.spkg\n\n\nTo build it and test do:\n\n\n```\nsage -i openmpi-1.1.4 mpi4py-1.1.0.spkg\n```\n\n\nThen\n\n\n```\nsage: import mpi4py\nsage: help(mpi4py)\n```\n\n\nNote: I will also update openmpi spkg at #7701",
    "created_at": "2009-12-16T02:03:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5686#issuecomment-44388",
    "user": "https://github.com/williamstein"
}
```

I've created a new version here:

  http://sage.math.washington.edu/home/wstein/patches/mpi4py-1.1.0.spkg


To build it and test do:


```
sage -i openmpi-1.1.4 mpi4py-1.1.0.spkg
```


Then


```
sage: import mpi4py
sage: help(mpi4py)
```


Note: I will also update openmpi spkg at #7701



---

archive/issue_comments_044389.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-16T02:04:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5686#issuecomment-44389",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_044390.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-17T21:20:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5686#issuecomment-44390",
    "user": "https://github.com/syazdani77"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_044391.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-19T05:22:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5686#issuecomment-44391",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_005928.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2009-12-19T05:22:40Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5686",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5686#event-5928"
}
```



---

archive/issue_comments_044392.json:
```json
{
    "body": "I posted the spkg.",
    "created_at": "2009-12-19T05:22:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5686#issuecomment-44392",
    "user": "https://github.com/williamstein"
}
```

I posted the spkg.
