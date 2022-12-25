# Issue 5235: Detect when Sage is build on AFS and issue a warning

archive/issues_005235.json:
```json
{
    "body": "Assignee: mabshoff\n\nFrom http://groups.google.com/group/sage-devel/t/894d29e0bde4550c\n\n```\n> Yes, afs is a strange filessystem and might be the root cause of your \n> trouble, but that is far from certain at this point. \n\n\nNo longer far from certain. The build completed without ANY problems, \nincluding getting past gnutls without error. This is not unprecedented \nbut somewhat surprising nevertheless. Running make test now. \n\nGedaliah \n```\n\n\nAFS seems to be commonly used with RHEL 4 in some instituations. It has come up twice now.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5235\n\n",
    "created_at": "2009-02-11T21:20:04Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Detect when Sage is build on AFS and issue a warning",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5235",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

From http://groups.google.com/group/sage-devel/t/894d29e0bde4550c

```
> Yes, afs is a strange filessystem and might be the root cause of your 
> trouble, but that is far from certain at this point. 


No longer far from certain. The build completed without ANY problems, 
including getting past gnutls without error. This is not unprecedented 
but somewhat surprising nevertheless. Running make test now. 

Gedaliah 
```


AFS seems to be commonly used with RHEL 4 in some instituations. It has come up twice now.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5235





---

archive/issue_comments_040035.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-11T21:20:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5235#issuecomment-40035",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_040036.json:
```json
{
    "body": "Gedaliah responded to my question:\n\n```\n> In case you have a shell code snipped that identifies that the current \n> working directory is on an AFS mount I would be happy to integrate it. \n\n\nThis will work unless somebody very foolishly changed the afs mount \npoint to something other that /afs. \n[[ $(pwd | cut -d'/' -f2) = 'afs' ]] && echo \"we are in afs\" \n```\n\n\nCheers,\n\nMichael",
    "created_at": "2009-02-11T22:52:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5235#issuecomment-40036",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Gedaliah responded to my question:

```
> In case you have a shell code snipped that identifies that the current 
> working directory is on an AFS mount I would be happy to integrate it. 


This will work unless somebody very foolishly changed the afs mount 
point to something other that /afs. 
[[ $(pwd | cut -d'/' -f2) = 'afs' ]] && echo "we are in afs" 
```


Cheers,

Michael



---

archive/issue_comments_040037.json:
```json
{
    "body": "Should anyone want to do this, Sun's `struct stat` has a `st_fstype` field which gives the filesystem type of a file, so from C this might be easy to check.",
    "created_at": "2010-01-16T23:21:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5235#issuecomment-40037",
    "user": "https://github.com/wjp"
}
```

Should anyone want to do this, Sun's `struct stat` has a `st_fstype` field which gives the filesystem type of a file, so from C this might be easy to check.



---

archive/issue_comments_040038.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-09-02T09:03:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5235#issuecomment-40038",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_040039.json:
```json
{
    "body": "I don't think this issue is relevant anymore, haven't heard any such problems recently...",
    "created_at": "2014-09-02T09:03:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5235#issuecomment-40039",
    "user": "https://github.com/jdemeyer"
}
```

I don't think this issue is relevant anymore, haven't heard any such problems recently...



---

archive/issue_comments_040040.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-09-02T09:03:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5235#issuecomment-40040",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_040041.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-09-09T14:52:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5235#issuecomment-40041",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_005491.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2014-09-09T14:52:41Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5235",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5235#event-5491"
}
```
