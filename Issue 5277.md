# Issue 5277: tachyon.spkg: link against libpng12 instead of libpng

archive/issues_005277.json:
```json
{
    "body": "Assignee: mabshoff\n\ntachyon - in src/unix/Make-config change -lpng to -lpng12:\n\n```\nUSEPNG= -DUSEPNG\nPNGINC= -I$(SAGE_LOCAL)/include\nPNGLIB= -L$(SAGE_LOCAL)/lib -lpng12 -lz\n```\n\nWe can probably set PNGLIB in spkg-install, so we don't have to edit any build system files.\n\nSpkg coming up. Together with some changes via the libpng update at #5217 this will solve a long standing problem when we run into symbol clashes on OSX with its IOKit.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5277\n\n",
    "created_at": "2009-02-15T15:27:42Z",
    "labels": [
        "packages: standard",
        "blocker",
        "bug"
    ],
    "title": "tachyon.spkg: link against libpng12 instead of libpng",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5277",
    "user": "mabshoff"
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

archive/issue_comments_040494.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-15T15:27:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5277#issuecomment-40494",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_040495.json:
```json
{
    "body": "The spkg at\n\n http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/rc1/tachyon-0.98beta.p8.spkg\n\nimplements that change.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-16T04:55:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5277#issuecomment-40495",
    "user": "mabshoff"
}
```

The spkg at

 http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/rc1/tachyon-0.98beta.p8.spkg

implements that change.

Cheers,

Michael



---

archive/issue_comments_040496.json:
```json
{
    "body": "This seems to work fine for me, on an intel mac running 10.5.6.",
    "created_at": "2009-02-16T11:28:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5277#issuecomment-40496",
    "user": "mhampton"
}
```

This seems to work fine for me, on an intel mac running 10.5.6.



---

archive/issue_comments_040497.json:
```json
{
    "body": "Merged in Sage 3.3.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-16T11:31:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5277#issuecomment-40497",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.rc1.

Cheers,

Michael



---

archive/issue_comments_040498.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-16T11:31:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5277#issuecomment-40498",
    "user": "mabshoff"
}
```

Resolution: fixed
