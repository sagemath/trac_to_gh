# Issue 1298: [with spkg] To build atlas on osx, we need to actual build lapack on osx.

archive/issues_001298.json:
```json
{
    "body": "Assignee: jkantor\n\nThe current lapack.spkg doesn't build on osx (because osx intel has one in /usr/lib)\nSince we will buid atlas on all platforms, we need to build lapack on osx. \n\nhttp://sage.math.washington.edu/home/jkantor/spkgs/lapack-20071123.spkg \n\n\n\n\n               \n\nIssue created by migration from https://trac.sagemath.org/ticket/1298\n\n",
    "created_at": "2007-11-28T09:47:57Z",
    "labels": [
        "component: numerical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.15",
    "title": "[with spkg] To build atlas on osx, we need to actual build lapack on osx.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1298",
    "user": "https://trac.sagemath.org/admin/accounts/users/jkantor"
}
```
Assignee: jkantor

The current lapack.spkg doesn't build on osx (because osx intel has one in /usr/lib)
Since we will buid atlas on all platforms, we need to build lapack on osx. 

http://sage.math.washington.edu/home/jkantor/spkgs/lapack-20071123.spkg 




               

Issue created by migration from https://trac.sagemath.org/ticket/1298





---

archive/issue_comments_008133.json:
```json
{
    "body": "Looks good to me.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-01T23:21:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1298#issuecomment-8133",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Looks good to me.

Cheers,

Michael



---

archive/issue_comments_008134.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-01T23:25:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1298#issuecomment-8134",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_008135.json:
```json
{
    "body": "Merged in 2.8.15.alpha2.",
    "created_at": "2007-12-01T23:25:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1298#issuecomment-8135",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.8.15.alpha2.
