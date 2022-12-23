# Issue 1244: update flint to r1075, add spkg-check

archive/issues_001244.json:
```json
{
    "body": "Assignee: mabshoff\n\nFrom Bill:\n\n```\nActually I've got no idea how to create an spkg-check script. But the\nthings you would type at the command line, supposing you were in the\nFLINT source tree in the trunk directory are:\n\nmake -Bj test\n./mpn_extras-test\n./ZmodF-test\n./ZmodF_mul-test\n./ZmodF_poly-test\n./fmpz-test\n./fmpz_poly-test\n```\n\nThose tests take about 6.5 minutes to run on sage.math, but we should run the tests per default for at least on release cycle (2.8.14) and disable them right before the final release. This will help Bill to shake out the last esoteric bug before the 1.0 release. The current Sage doctests don't even push the envelope. \n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1244\n\n",
    "created_at": "2007-11-22T21:43:26Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "title": "update flint to r1075, add spkg-check",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1244",
    "user": "mabshoff"
}
```
Assignee: mabshoff

From Bill:

```
Actually I've got no idea how to create an spkg-check script. But the
things you would type at the command line, supposing you were in the
FLINT source tree in the trunk directory are:

make -Bj test
./mpn_extras-test
./ZmodF-test
./ZmodF_mul-test
./ZmodF_poly-test
./fmpz-test
./fmpz_poly-test
```

Those tests take about 6.5 minutes to run on sage.math, but we should run the tests per default for at least on release cycle (2.8.14) and disable them right before the final release. This will help Bill to shake out the last esoteric bug before the 1.0 release. The current Sage doctests don't even push the envelope. 

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1244





---

archive/issue_comments_007794.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-11-22T21:43:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1244#issuecomment-7794",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_007795.json:
```json
{
    "body": "Ok, spkg is at\n\nhttp://sage.math.washington.edu/home/mabshoff/flint-0.9-r1075.spkg\n\nThe forced tests can take 15-30 minutes.\n\nCheers,\n\nMichael",
    "created_at": "2007-11-24T03:52:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1244#issuecomment-7795",
    "user": "mabshoff"
}
```

Ok, spkg is at

http://sage.math.washington.edu/home/mabshoff/flint-0.9-r1075.spkg

The forced tests can take 15-30 minutes.

Cheers,

Michael



---

archive/issue_comments_007796.json:
```json
{
    "body": "Changing component from algebraic geometry to packages.",
    "created_at": "2007-11-24T03:52:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1244#issuecomment-7796",
    "user": "mabshoff"
}
```

Changing component from algebraic geometry to packages.



---

archive/issue_comments_007797.json:
```json
{
    "body": "Ok, Bill found a bug that cause memory leakes. Updated spkg is at\n\nhttp://sage.math.washington.edu/home/mabshoff/flint-0.9-r1075.p0.spkg\n\nCheers,\n\nMichael",
    "created_at": "2007-11-24T10:14:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1244#issuecomment-7797",
    "user": "mabshoff"
}
```

Ok, Bill found a bug that cause memory leakes. Updated spkg is at

http://sage.math.washington.edu/home/mabshoff/flint-0.9-r1075.p0.spkg

Cheers,

Michael



---

archive/issue_comments_007798.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-24T15:36:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1244#issuecomment-7798",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_007799.json:
```json
{
    "body": "Merged in 2.8.14.rc1. Various people reported that the spkg works.\n\nCheers,\n\nMichael",
    "created_at": "2007-11-24T15:36:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1244#issuecomment-7799",
    "user": "mabshoff"
}
```

Merged in 2.8.14.rc1. Various people reported that the spkg works.

Cheers,

Michael
