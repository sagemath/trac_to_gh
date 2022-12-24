# Issue 3391: update scipy to match the numpy 1.1.0 release

archive/issues_003391.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  jason jkantor\n\n#3390 updates numpy to 1.1.0. Since that no longer works with the last stable release we also need to upgrade scipy to svn - figure out which revision to use.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3391\n\n",
    "created_at": "2008-06-10T19:06:36Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.2",
    "title": "update scipy to match the numpy 1.1.0 release",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3391",
    "user": "mabshoff"
}
```
Assignee: mabshoff

CC:  jason jkantor

#3390 updates numpy to 1.1.0. Since that no longer works with the last stable release we also need to upgrade scipy to svn - figure out which revision to use.

Issue created by migration from https://trac.sagemath.org/ticket/3391





---

archive/issue_comments_023737.json:
```json
{
    "body": "See if this fixes the issue at #2303 and re-enable the option if so. (Though perhaps with a rewrite to remove the exessive string processing...)",
    "created_at": "2008-07-08T23:58:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3391#issuecomment-23737",
    "user": "robertwb"
}
```

See if this fixes the issue at #2303 and re-enable the option if so. (Though perhaps with a rewrite to remove the exessive string processing...)



---

archive/issue_comments_023738.json:
```json
{
    "body": "This is now the 1.2.0 numpy release once we merge #4200. We do need this since otherwise we get a boadload of deprecation warnings.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-26T07:08:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3391#issuecomment-23738",
    "user": "mabshoff"
}
```

This is now the 1.2.0 numpy release once we merge #4200. We do need this since otherwise we get a boadload of deprecation warnings.

Cheers,

Michael



---

archive/issue_comments_023739.json:
```json
{
    "body": "Updated spkg at http://sage.math.washington.edu/home/jason/scipy-20080927-0.6.spkg\n\nI have successfully installed it.  I haven't run doctests yet.",
    "created_at": "2008-09-27T06:23:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3391#issuecomment-23739",
    "user": "jason"
}
```

Updated spkg at http://sage.math.washington.edu/home/jason/scipy-20080927-0.6.spkg

I have successfully installed it.  I haven't run doctests yet.



---

archive/issue_comments_023740.json:
```json
{
    "body": "Actually, use this spkg: http://sage.math.washington.edu/home/jason/scipy-0.7r4752svn.spkg",
    "created_at": "2008-09-27T06:35:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3391#issuecomment-23740",
    "user": "jason"
}
```

Actually, use this spkg: http://sage.math.washington.edu/home/jason/scipy-0.7r4752svn.spkg



---

archive/issue_comments_023741.json:
```json
{
    "body": "I fixed a couple tiny issues and \n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.3/alpha2/scipy-0.7r4752svn.spkg\n\nis the latest version. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-27T07:18:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3391#issuecomment-23741",
    "user": "mabshoff"
}
```

I fixed a couple tiny issues and 

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.3/alpha2/scipy-0.7r4752svn.spkg

is the latest version. Positive review.

Cheers,

Michael



---

archive/issue_comments_023742.json:
```json
{
    "body": "We have to fix some deprecation warning, but that will be fixed via #4205.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-27T07:38:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3391#issuecomment-23742",
    "user": "mabshoff"
}
```

We have to fix some deprecation warning, but that will be fixed via #4205.

Cheers,

Michael



---

archive/issue_comments_023743.json:
```json
{
    "body": "Merged in Sage 3.1.3.alpha2",
    "created_at": "2008-09-27T07:38:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3391#issuecomment-23743",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.3.alpha2



---

archive/issue_comments_023744.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-27T07:38:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3391#issuecomment-23744",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_023745.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-09-27T22:21:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3391#issuecomment-23745",
    "user": "mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_023746.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-09-27T22:21:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3391#issuecomment-23746",
    "user": "mabshoff"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_023747.json:
```json
{
    "body": "Due to some trouble with deprecation and other bad, bad things reopen this for now. We will deal with the fallout post Sage 3.1.3. For some details about the trouble see #4205 and #4210.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-27T22:21:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3391#issuecomment-23747",
    "user": "mabshoff"
}
```

Due to some trouble with deprecation and other bad, bad things reopen this for now. We will deal with the fallout post Sage 3.1.3. For some details about the trouble see #4205 and #4210.

Cheers,

Michael



---

archive/issue_comments_023748.json:
```json
{
    "body": "Note that there are various tickets which will can be resolved at the same time as the update.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-12T10:12:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3391#issuecomment-23748",
    "user": "mabshoff"
}
```

Note that there are various tickets which will can be resolved at the same time as the update.

Cheers,

Michael



---

archive/issue_comments_023749.json:
```json
{
    "body": "A new spkg for scipy 0.7.0 is here: http://sage.math.washington.edu/home/jason/scipy-0.7.spkg\n\nI'm attaching a patch which fixes many of the errors and deprecations.  There are a few other errors I am inquiring on the scipy mailing list about.",
    "created_at": "2009-05-27T08:03:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3391#issuecomment-23749",
    "user": "jason"
}
```

A new spkg for scipy 0.7.0 is here: http://sage.math.washington.edu/home/jason/scipy-0.7.spkg

I'm attaching a patch which fixes many of the errors and deprecations.  There are a few other errors I am inquiring on the scipy mailing list about.



---

archive/issue_comments_023750.json:
```json
{
    "body": "Attachment [scipy-0.7-update.patch](tarball://root/attachments/some-uuid/ticket3391/scipy-0.7-update.patch) by jason created at 2009-05-27 20:22:55",
    "created_at": "2009-05-27T20:22:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3391#issuecomment-23750",
    "user": "jason"
}
```

Attachment [scipy-0.7-update.patch](tarball://root/attachments/some-uuid/ticket3391/scipy-0.7-update.patch) by jason created at 2009-05-27 20:22:55



---

archive/issue_comments_023751.json:
```json
{
    "body": "#4205 can likely be closed once this ticket is closed.  See also #6140 for the numpy update.",
    "created_at": "2009-05-27T22:14:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3391#issuecomment-23751",
    "user": "jason"
}
```

#4205 can likely be closed once this ticket is closed.  See also #6140 for the numpy update.



---

archive/issue_comments_023752.json:
```json
{
    "body": "Looks good, positive review.",
    "created_at": "2009-06-01T08:31:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3391#issuecomment-23752",
    "user": "jkantor"
}
```

Looks good, positive review.



---

archive/issue_comments_023753.json:
```json
{
    "body": "spkg and patch merged in 4.0.2.alpha0.",
    "created_at": "2009-06-12T06:58:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3391#issuecomment-23753",
    "user": "craigcitro"
}
```

spkg and patch merged in 4.0.2.alpha0.



---

archive/issue_comments_023754.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-12T06:58:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3391#issuecomment-23754",
    "user": "craigcitro"
}
```

Resolution: fixed



---

archive/issue_comments_023755.json:
```json
{
    "body": "Oops, forgot a field.",
    "created_at": "2009-06-12T06:58:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3391#issuecomment-23755",
    "user": "craigcitro"
}
```

Oops, forgot a field.
