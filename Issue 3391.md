# Issue 3391: update scipy to match the numpy 1.1.0 release

archive/issues_003391.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @jasongrout jkantor\n\n#3390 updates numpy to 1.1.0. Since that no longer works with the last stable release we also need to upgrade scipy to svn - figure out which revision to use.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3391\n\n",
    "created_at": "2008-06-10T19:06:36Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.2",
    "title": "update scipy to match the numpy 1.1.0 release",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3391",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

CC:  @jasongrout jkantor

#3390 updates numpy to 1.1.0. Since that no longer works with the last stable release we also need to upgrade scipy to svn - figure out which revision to use.

Issue created by migration from https://trac.sagemath.org/ticket/3391





---

archive/issue_comments_023689.json:
```json
{
    "body": "See if this fixes the issue at #2303 and re-enable the option if so. (Though perhaps with a rewrite to remove the exessive string processing...)",
    "created_at": "2008-07-08T23:58:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3391#issuecomment-23689",
    "user": "https://github.com/robertwb"
}
```

See if this fixes the issue at #2303 and re-enable the option if so. (Though perhaps with a rewrite to remove the exessive string processing...)



---

archive/issue_comments_023690.json:
```json
{
    "body": "This is now the 1.2.0 numpy release once we merge #4200. We do need this since otherwise we get a boadload of deprecation warnings.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-26T07:08:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3391#issuecomment-23690",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is now the 1.2.0 numpy release once we merge #4200. We do need this since otherwise we get a boadload of deprecation warnings.

Cheers,

Michael



---

archive/issue_comments_023691.json:
```json
{
    "body": "Updated spkg at http://sage.math.washington.edu/home/jason/scipy-20080927-0.6.spkg\n\nI have successfully installed it.  I haven't run doctests yet.",
    "created_at": "2008-09-27T06:23:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3391#issuecomment-23691",
    "user": "https://github.com/jasongrout"
}
```

Updated spkg at http://sage.math.washington.edu/home/jason/scipy-20080927-0.6.spkg

I have successfully installed it.  I haven't run doctests yet.



---

archive/issue_comments_023692.json:
```json
{
    "body": "Actually, use this spkg: http://sage.math.washington.edu/home/jason/scipy-0.7r4752svn.spkg",
    "created_at": "2008-09-27T06:35:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3391#issuecomment-23692",
    "user": "https://github.com/jasongrout"
}
```

Actually, use this spkg: http://sage.math.washington.edu/home/jason/scipy-0.7r4752svn.spkg



---

archive/issue_comments_023693.json:
```json
{
    "body": "I fixed a couple tiny issues and \n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.3/alpha2/scipy-0.7r4752svn.spkg\n\nis the latest version. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-27T07:18:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3391#issuecomment-23693",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I fixed a couple tiny issues and 

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.3/alpha2/scipy-0.7r4752svn.spkg

is the latest version. Positive review.

Cheers,

Michael



---

archive/issue_comments_023694.json:
```json
{
    "body": "We have to fix some deprecation warning, but that will be fixed via #4205.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-27T07:38:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3391#issuecomment-23694",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

We have to fix some deprecation warning, but that will be fixed via #4205.

Cheers,

Michael



---

archive/issue_events_007652.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-27T07:38:37Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3391",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3391#event-7652"
}
```



---

archive/issue_comments_023695.json:
```json
{
    "body": "Merged in Sage 3.1.3.alpha2",
    "created_at": "2008-09-27T07:38:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3391#issuecomment-23695",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.3.alpha2



---

archive/issue_comments_023696.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-27T07:38:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3391#issuecomment-23696",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_023697.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-09-27T22:21:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3391#issuecomment-23697",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_events_007653.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-27T22:21:54Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/3391",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3391#event-7653"
}
```



---

archive/issue_comments_023698.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-09-27T22:21:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3391#issuecomment-23698",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_023699.json:
```json
{
    "body": "Due to some trouble with deprecation and other bad, bad things reopen this for now. We will deal with the fallout post Sage 3.1.3. For some details about the trouble see #4205 and #4210.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-27T22:21:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3391#issuecomment-23699",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Due to some trouble with deprecation and other bad, bad things reopen this for now. We will deal with the fallout post Sage 3.1.3. For some details about the trouble see #4205 and #4210.

Cheers,

Michael



---

archive/issue_comments_023700.json:
```json
{
    "body": "Note that there are various tickets which will can be resolved at the same time as the update.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-12T10:12:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3391#issuecomment-23700",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Note that there are various tickets which will can be resolved at the same time as the update.

Cheers,

Michael



---

archive/issue_comments_023701.json:
```json
{
    "body": "A new spkg for scipy 0.7.0 is here: http://sage.math.washington.edu/home/jason/scipy-0.7.spkg\n\nI'm attaching a patch which fixes many of the errors and deprecations.  There are a few other errors I am inquiring on the scipy mailing list about.",
    "created_at": "2009-05-27T08:03:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3391#issuecomment-23701",
    "user": "https://github.com/jasongrout"
}
```

A new spkg for scipy 0.7.0 is here: http://sage.math.washington.edu/home/jason/scipy-0.7.spkg

I'm attaching a patch which fixes many of the errors and deprecations.  There are a few other errors I am inquiring on the scipy mailing list about.



---

archive/issue_comments_023702.json:
```json
{
    "body": "Attachment [scipy-0.7-update.patch](tarball://root/attachments/some-uuid/ticket3391/scipy-0.7-update.patch) by @jasongrout created at 2009-05-27 20:22:55",
    "created_at": "2009-05-27T20:22:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3391#issuecomment-23702",
    "user": "https://github.com/jasongrout"
}
```

Attachment [scipy-0.7-update.patch](tarball://root/attachments/some-uuid/ticket3391/scipy-0.7-update.patch) by @jasongrout created at 2009-05-27 20:22:55



---

archive/issue_comments_023703.json:
```json
{
    "body": "#4205 can likely be closed once this ticket is closed.  See also #6140 for the numpy update.",
    "created_at": "2009-05-27T22:14:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3391#issuecomment-23703",
    "user": "https://github.com/jasongrout"
}
```

#4205 can likely be closed once this ticket is closed.  See also #6140 for the numpy update.



---

archive/issue_comments_023704.json:
```json
{
    "body": "Looks good, positive review.",
    "created_at": "2009-06-01T08:31:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3391#issuecomment-23704",
    "user": "https://trac.sagemath.org/admin/accounts/users/jkantor"
}
```

Looks good, positive review.



---

archive/issue_comments_023705.json:
```json
{
    "body": "spkg and patch merged in 4.0.2.alpha0.",
    "created_at": "2009-06-12T06:58:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3391#issuecomment-23705",
    "user": "https://github.com/craigcitro"
}
```

spkg and patch merged in 4.0.2.alpha0.



---

archive/issue_events_007654.json:
```json
{
    "actor": "https://github.com/craigcitro",
    "created_at": "2009-06-12T06:58:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3391",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3391#event-7654"
}
```



---

archive/issue_comments_023706.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-12T06:58:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3391#issuecomment-23706",
    "user": "https://github.com/craigcitro"
}
```

Resolution: fixed



---

archive/issue_comments_023707.json:
```json
{
    "body": "Oops, forgot a field.",
    "created_at": "2009-06-12T06:58:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3391#issuecomment-23707",
    "user": "https://github.com/craigcitro"
}
```

Oops, forgot a field.
