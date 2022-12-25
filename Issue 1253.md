# Issue 1253: make sage compile on OSX 10.5.1

archive/issues_001253.json:
```json
{
    "body": "Assignee: mabshoff\n\nThe checks for workarounds we implemented for 10.5 fail on 10.5.1 because we usually check for \n\n```\nDarwin-9.0.0\n```\n\nBut 10.5.1 is\n\n```\nDarwin-9.1.0\n```\n\nSo far we need fixes for\n* gmp\n* python\nBut probably some more down the road. I am taking care of those.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1253\n\n",
    "created_at": "2007-11-24T12:51:24Z",
    "labels": [
        "component: packages: standard",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.14",
    "title": "make sage compile on OSX 10.5.1",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1253",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

The checks for workarounds we implemented for 10.5 fail on 10.5.1 because we usually check for 

```
Darwin-9.0.0
```

But 10.5.1 is

```
Darwin-9.1.0
```

So far we need fixes for
* gmp
* python
But probably some more down the road. I am taking care of those.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1253





---

archive/issue_comments_007814.json:
```json
{
    "body": "Ok, here we go with fixed spkgs:\n\nhttp://sage.math.washington.edu/home/mabshoff/gmp-4.2.1.p12.spkg\nhttp://sage.math.washington.edu/home/mabshoff/python-2.5.1.p9.spkg\nhttp://sage.math.washington.edu/home/mabshoff/clisp-2.41.p11.spkg\n\nThose will all be in rc1.\n\nCheers,\n\nMichael",
    "created_at": "2007-11-24T15:28:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1253#issuecomment-7814",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ok, here we go with fixed spkgs:

http://sage.math.washington.edu/home/mabshoff/gmp-4.2.1.p12.spkg
http://sage.math.washington.edu/home/mabshoff/python-2.5.1.p9.spkg
http://sage.math.washington.edu/home/mabshoff/clisp-2.41.p11.spkg

Those will all be in rc1.

Cheers,

Michael



---

archive/issue_comments_007815.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-11-24T15:28:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1253#issuecomment-7815",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_007816.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-24T15:47:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1253#issuecomment-7816",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_007817.json:
```json
{
    "body": "Merged in 2.8.14.rc1. Let's hope it still works on OSX < 10.5.1 :)\n\nCheers,\n\nMichael",
    "created_at": "2007-11-24T15:47:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1253#issuecomment-7817",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.8.14.rc1. Let's hope it still works on OSX < 10.5.1 :)

Cheers,

Michael
