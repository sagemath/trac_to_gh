# Issue 5116: update M4RI to newest upstream release

archive/issues_005116.json:
```json
{
    "body": "Assignee: mabshoff\n\nKeywords: m4ri\n\nA new version of M4RI is available. \n\nRelease notes: http://bitbucket.org/malb/m4ri/wiki/M4RI-20090105\n\nIssue created by migration from https://trac.sagemath.org/ticket/5116\n\n",
    "created_at": "2009-01-28T11:43:10Z",
    "labels": [
        "component: packages: standard"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "update M4RI to newest upstream release",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5116",
    "user": "https://github.com/malb"
}
```
Assignee: mabshoff

Keywords: m4ri

A new version of M4RI is available. 

Release notes: http://bitbucket.org/malb/m4ri/wiki/M4RI-20090105

Issue created by migration from https://trac.sagemath.org/ticket/5116





---

archive/issue_comments_039027.json:
```json
{
    "body": "Attachment [m4ri_200901.patch](tarball://root/attachments/some-uuid/ticket5116/m4ri_200901.patch) by @malb created at 2009-01-28 13:15:21\n\n* builds/checks/doctests clean on sage.math (Linux 64-bit)\n  * builds/checks/doctests clean on bsd (OSX 32-bit)\n  * builds/checks/doctests clean on iras (Linux IA-64)\n\nNote that the SPKG has `make check` enabled.",
    "created_at": "2009-01-28T13:15:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5116",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5116#issuecomment-39027",
    "user": "https://github.com/malb"
}
```

Attachment [m4ri_200901.patch](tarball://root/attachments/some-uuid/ticket5116/m4ri_200901.patch) by @malb created at 2009-01-28 13:15:21

* builds/checks/doctests clean on sage.math (Linux 64-bit)
  * builds/checks/doctests clean on bsd (OSX 32-bit)
  * builds/checks/doctests clean on iras (Linux IA-64)

Note that the SPKG has `make check` enabled.



---

archive/issue_comments_039028.json:
```json
{
    "body": "* builds/checks/doctests clean on vbox-linux-32-bit (Linux 32-bit)",
    "created_at": "2009-01-28T23:40:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5116",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5116#issuecomment-39028",
    "user": "https://github.com/malb"
}
```

* builds/checks/doctests clean on vbox-linux-32-bit (Linux 32-bit)



---

archive/issue_comments_039029.json:
```json
{
    "body": "The spkg can be found at\n\nhttp://sage.math.washington.edu/home/malb/spkgs/libm4ri-20090128.spkg\n\nCheers,\n\nMichael",
    "created_at": "2009-02-03T23:18:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5116",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5116#issuecomment-39029",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The spkg can be found at

http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20090128.spkg

Cheers,

Michael



---

archive/issue_comments_039030.json:
```json
{
    "body": "Spkg builds fine and passes make check also on OSX 10.4/PPC. The patch is also good to go and passes doctests.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-04T00:07:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5116",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5116#issuecomment-39030",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Spkg builds fine and passes make check also on OSX 10.4/PPC. The patch is also good to go and passes doctests.

Cheers,

Michael



---

archive/issue_comments_039031.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-04T00:08:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5116",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5116#issuecomment-39031",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_039032.json:
```json
{
    "body": "Merged patch and spkg into Sage 3.3.alpha4.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-04T00:08:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5116",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5116#issuecomment-39032",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged patch and spkg into Sage 3.3.alpha4.

Cheers,

Michael
