# Issue 1720: [with spkg] update numpy to 1.0.4, also fix silent build problems with gfortran

archive/issues_001720.json:
```json
{
    "body": "Assignee: mabshoff\n\nThis updates the numpy package to the latest version \n\nhttp://sage.math.washington.edu/home/jkantor/spkgs/numpy-20080104-1.0.4.spkg\n\n(note I have removed a section of the spkg-install that was allowing numpy to build without\natlas if the inital build didn't work. I saw that this was happengin when using gfortran. I think I fixed the initial problem but this may cause build failures that were going unnoticed to become manifest. I want to know so I can fix them.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/1720\n\n",
    "created_at": "2008-01-08T10:05:30Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10",
    "title": "[with spkg] update numpy to 1.0.4, also fix silent build problems with gfortran",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1720",
    "user": "https://trac.sagemath.org/admin/accounts/users/jkantor"
}
```
Assignee: mabshoff

This updates the numpy package to the latest version 

http://sage.math.washington.edu/home/jkantor/spkgs/numpy-20080104-1.0.4.spkg

(note I have removed a section of the spkg-install that was allowing numpy to build without
atlas if the inital build didn't work. I saw that this was happengin when using gfortran. I think I fixed the initial problem but this may cause build failures that were going unnoticed to become manifest. I want to know so I can fix them.)

Issue created by migration from https://trac.sagemath.org/ticket/1720





---

archive/issue_comments_010873.json:
```json
{
    "body": "An updated spkg with SPKG.txt and hg repo added is at \n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-2.10/alpha1/numpy-20080104-1.0.4.p0.spkg\n\nCheers,\n\nMichael",
    "created_at": "2008-01-08T23:54:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1720#issuecomment-10873",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

An updated spkg with SPKG.txt and hg repo added is at 

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10/alpha1/numpy-20080104-1.0.4.p0.spkg

Cheers,

Michael



---

archive/issue_comments_010874.json:
```json
{
    "body": "Added detailed information to SPKG.txt\n\n\nhttp://sage.math.washington.edu/home/jkantor/spkgs/numpy-20080104-1.0.4.p1.spkg",
    "created_at": "2008-01-09T00:40:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1720#issuecomment-10874",
    "user": "https://trac.sagemath.org/admin/accounts/users/jkantor"
}
```

Added detailed information to SPKG.txt


http://sage.math.washington.edu/home/jkantor/spkgs/numpy-20080104-1.0.4.p1.spkg



---

archive/issue_comments_010875.json:
```json
{
    "body": "I updated the SPKG.txt with a changelog entry, removed `*~` from the spkg and updated `.hgignore`. The updated spkg with the same name as Josh's last one linked above is at \n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-2.10/alpha1/numpy-20080104-1.0.4.p1.spkg\n\nCheers,\n\nMichael",
    "created_at": "2008-01-09T01:57:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1720#issuecomment-10875",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I updated the SPKG.txt with a changelog entry, removed `*~` from the spkg and updated `.hgignore`. The updated spkg with the same name as Josh's last one linked above is at 

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10/alpha1/numpy-20080104-1.0.4.p1.spkg

Cheers,

Michael



---

archive/issue_events_004184.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-09T01:57:47Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1720",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1720#event-4184"
}
```



---

archive/issue_comments_010876.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-09T01:57:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1720#issuecomment-10876",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
