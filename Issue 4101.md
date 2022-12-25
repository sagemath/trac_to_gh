# Issue 4101: [with spkg, needs review] cpdef horribly broken in last Cython

archive/issues_004101.json:
```json
{
    "body": "Assignee: mabshoff\n\nThe way cpdef functions were implemented broke in some classes when being used across modules. This came up now because the new coercion uses cpdef much more. This is just the old cython+bug fix rather than a new release for time reasons, and passes sage -testall with the attached (nearly trivial) patch. A sage -ba is required. \n\nhttp://sage.math.washington.edu/home/robertwb/cython/cython-0.9.8.1.1p1.spkg\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4101\n\n",
    "created_at": "2008-09-11T17:14:55Z",
    "labels": [
        "component: packages: standard",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "[with spkg, needs review] cpdef horribly broken in last Cython",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4101",
    "user": "https://github.com/robertwb"
}
```
Assignee: mabshoff

The way cpdef functions were implemented broke in some classes when being used across modules. This came up now because the new coercion uses cpdef much more. This is just the old cython+bug fix rather than a new release for time reasons, and passes sage -testall with the attached (nearly trivial) patch. A sage -ba is required. 

http://sage.math.washington.edu/home/robertwb/cython/cython-0.9.8.1.1p1.spkg



Issue created by migration from https://trac.sagemath.org/ticket/4101





---

archive/issue_comments_029532.json:
```json
{
    "body": "Attachment [4101-cpdef-fix.patch](tarball://root/attachments/some-uuid/ticket4101/4101-cpdef-fix.patch) by @robertwb created at 2008-09-11 17:15:19",
    "created_at": "2008-09-11T17:15:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4101",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4101#issuecomment-29532",
    "user": "https://github.com/robertwb"
}
```

Attachment [4101-cpdef-fix.patch](tarball://root/attachments/some-uuid/ticket4101/4101-cpdef-fix.patch) by @robertwb created at 2008-09-11 17:15:19



---

archive/issue_comments_029533.json:
```json
{
    "body": "Hi Robert,\n\nI fixed some issues in the spkg, which is now at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/rc2/cython-0.9.8.1.1.p0.spkg\n\nNote that the patch level usually starts at p0 and that the name of the spkg and the directory name were not in sync.\n\nI am testing the spkg with the patch to the Sage library applied right now, so expect a review in about 45 minutes.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-13T00:29:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4101",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4101#issuecomment-29533",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hi Robert,

I fixed some issues in the spkg, which is now at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/rc2/cython-0.9.8.1.1.p0.spkg

Note that the patch level usually starts at p0 and that the name of the spkg and the directory name were not in sync.

I am testing the spkg with the patch to the Sage library applied right now, so expect a review in about 45 minutes.

Cheers,

Michael



---

archive/issue_comments_029534.json:
```json
{
    "body": "Spkg and a following `-ba` passes doctests. Positive review. Let's hope this spkg does not bite us in the ass so late in the release cycle :)\n\nCheers,\n\nMichael",
    "created_at": "2008-09-13T01:51:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4101",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4101#issuecomment-29534",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Spkg and a following `-ba` passes doctests. Positive review. Let's hope this spkg does not bite us in the ass so late in the release cycle :)

Cheers,

Michael



---

archive/issue_comments_029535.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc2",
    "created_at": "2008-09-13T01:52:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4101",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4101#issuecomment-29535",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.2.rc2



---

archive/issue_events_004338.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-13T01:52:10Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4101",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4101#event-4338"
}
```



---

archive/issue_comments_029536.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-13T01:52:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4101",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4101#issuecomment-29536",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_029537.json:
```json
{
    "body": "Thanks. I realized later that I had changed the name of the spkg rather than the folder name, but I was at work by then. \n\nThis is intentionally a p0 rather than the next release, so I'm pretty sure it won't bite us. (Famous last words...)",
    "created_at": "2008-09-13T03:58:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4101",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4101#issuecomment-29537",
    "user": "https://github.com/robertwb"
}
```

Thanks. I realized later that I had changed the name of the spkg rather than the folder name, but I was at work by then. 

This is intentionally a p0 rather than the next release, so I'm pretty sure it won't bite us. (Famous last words...)



---

archive/issue_comments_029538.json:
```json
{
    "body": "Replying to [comment:4 robertwb]:\n> Thanks. I realized later that I had changed the name of the spkg rather than the folder name, but I was at work by then. \n\nCool. It would be nice if you could base future cython.spkg off this on in 3.1.2.rc2. I did some fixed to spkg-install and SPKG.txt. It would also be great if you could add to the changes in SPKG.txt once you update it.\n\n> This is intentionally a p0 rather than the next release, so I'm pretty sure it won't bite us. \n\nWell, the name was p1, so that was mostly my point. I fully understand that you added only one patch on top of the latest Cython release.\n\n> (Famous last words...)\n\nYeah, what could go wrong :)\n\nI am valgrinding the startup of 3.1.2.rc2 to see if anything fishy was introduced.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-13T04:07:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4101",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4101#issuecomment-29538",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:4 robertwb]:
> Thanks. I realized later that I had changed the name of the spkg rather than the folder name, but I was at work by then. 

Cool. It would be nice if you could base future cython.spkg off this on in 3.1.2.rc2. I did some fixed to spkg-install and SPKG.txt. It would also be great if you could add to the changes in SPKG.txt once you update it.

> This is intentionally a p0 rather than the next release, so I'm pretty sure it won't bite us. 

Well, the name was p1, so that was mostly my point. I fully understand that you added only one patch on top of the latest Cython release.

> (Famous last words...)

Yeah, what could go wrong :)

I am valgrinding the startup of 3.1.2.rc2 to see if anything fishy was introduced.

Cheers,

Michael
