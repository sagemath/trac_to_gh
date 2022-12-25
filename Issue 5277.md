# Issue 5277: [with spkg, positive review] tachyon.spkg: link against libpng12 instead of libpng

archive/issues_005277.json:
```json
{
    "body": "Assignee: mabshoff\n\ntachyon - in src/unix/Make-config change -lpng to -lpng12:\n\n```\nUSEPNG= -DUSEPNG\nPNGINC= -I$(SAGE_LOCAL)/include\nPNGLIB= -L$(SAGE_LOCAL)/lib -lpng12 -lz\n```\nWe can probably set PNGLIB in spkg-install, so we don't have to edit any build system files.\n\nSpkg coming up. Together with some changes via the libpng update at #5217 this will solve a long standing problem when we run into symbol clashes on OSX with its IOKit.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5277\n\n",
    "closed_at": "2009-02-16T11:31:21Z",
    "created_at": "2009-02-15T15:27:42Z",
    "labels": [
        "component: packages: standard",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[with spkg, positive review] tachyon.spkg: link against libpng12 instead of libpng",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5277",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

tachyon - in src/unix/Make-config change -lpng to -lpng12:

```
USEPNG= -DUSEPNG
PNGINC= -I$(SAGE_LOCAL)/include
PNGLIB= -L$(SAGE_LOCAL)/lib -lpng12 -lz
```
We can probably set PNGLIB in spkg-install, so we don't have to edit any build system files.

Spkg coming up. Together with some changes via the libpng update at #5217 this will solve a long standing problem when we run into symbol clashes on OSX with its IOKit.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5277





---

archive/issue_comments_040415.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-15T15:27:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5277#issuecomment-40415",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_040416.json:
```json
{
    "body": "The spkg at\n\n http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/rc1/tachyon-0.98beta.p8.spkg\n\nimplements that change.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-16T04:55:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5277#issuecomment-40416",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The spkg at

 http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/rc1/tachyon-0.98beta.p8.spkg

implements that change.

Cheers,

Michael



---

archive/issue_comments_040417.json:
```json
{
    "body": "This seems to work fine for me, on an intel mac running 10.5.6.",
    "created_at": "2009-02-16T11:28:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5277#issuecomment-40417",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

This seems to work fine for me, on an intel mac running 10.5.6.



---

archive/issue_events_012256.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-16T11:31:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5277",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5277#event-12256"
}
```



---

archive/issue_comments_040418.json:
```json
{
    "body": "Merged in Sage 3.3.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-16T11:31:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5277#issuecomment-40418",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.rc1.

Cheers,

Michael



---

archive/issue_comments_040419.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-16T11:31:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5277#issuecomment-40419",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
