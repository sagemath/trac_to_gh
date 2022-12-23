# Issue 2929: [with spkg, needs review] gcc 4.3: fix gmp.spkg

archive/issues_002929.json:
```json
{
    "body": "Assignee: mabshoff\n\nThe gmp.spkg fails to build on gcc 4.3 [at least we cannot link properly against it] due to some changes to the inline handling as well as missing std::FILE issues. The spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.0/alpha5/gmp-4.2.1.p14.spkg\n\nfixes that by slightly patching gmp-h.in.\n\nTo test build gmp, then FLINT for example since gmp by itself builds fine ;) - imagine my excitement debugging the problem. \n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/2929\n\n",
    "created_at": "2008-04-15T05:52:53Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "title": "[with spkg, needs review] gcc 4.3: fix gmp.spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2929",
    "user": "mabshoff"
}
```
Assignee: mabshoff

The gmp.spkg fails to build on gcc 4.3 [at least we cannot link properly against it] due to some changes to the inline handling as well as missing std::FILE issues. The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0/alpha5/gmp-4.2.1.p14.spkg

fixes that by slightly patching gmp-h.in.

To test build gmp, then FLINT for example since gmp by itself builds fine ;) - imagine my excitement debugging the problem. 

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/2929





---

archive/issue_comments_020168.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-04-15T05:53:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2929",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2929#issuecomment-20168",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_020169.json:
```json
{
    "body": "works for me.",
    "created_at": "2008-04-15T05:56:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2929",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2929#issuecomment-20169",
    "user": "gfurnish"
}
```

works for me.



---

archive/issue_comments_020170.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-15T06:08:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2929",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2929#issuecomment-20170",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_020171.json:
```json
{
    "body": "Merged in Sage 3.0.alpha5",
    "created_at": "2008-04-15T06:08:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2929",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2929#issuecomment-20171",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha5
