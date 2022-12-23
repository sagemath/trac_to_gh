# Issue 1740: Fix Pentium M detection for ATLAS BLAS

archive/issues_001740.json:
```json
{
    "body": "Assignee: mabshoff\n\nThere is a know problem with ATLAS BLAS that misdetects Pentium Ms as CoreDuos and consequently takes a long, long time tuning to build. This patch by Paul Zimmermann fixes the issue. It has been integrated into \n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-2.10/alpha1/atlas-3.8.p7.spkg\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1740\n\n",
    "created_at": "2008-01-10T05:05:29Z",
    "labels": [
        "packages: standard",
        "blocker",
        "bug"
    ],
    "title": "Fix Pentium M detection for ATLAS BLAS",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1740",
    "user": "mabshoff"
}
```
Assignee: mabshoff

There is a know problem with ATLAS BLAS that misdetects Pentium Ms as CoreDuos and consequently takes a long, long time tuning to build. This patch by Paul Zimmermann fixes the issue. It has been integrated into 

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10/alpha1/atlas-3.8.p7.spkg

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1740





---

archive/issue_comments_011004.json:
```json
{
    "body": "FYI: I posted the patch at \n\nhttps://sourceforge.net/tracker/index.php?func=detail&aid=1868203&group_id=23725&atid=379483\n\nOnce I hear back from Clint I will let you guys know.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-10T05:21:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1740#issuecomment-11004",
    "user": "mabshoff"
}
```

FYI: I posted the patch at 

https://sourceforge.net/tracker/index.php?func=detail&aid=1868203&group_id=23725&atid=379483

Once I hear back from Clint I will let you guys know.

Cheers,

Michael



---

archive/issue_comments_011005.json:
```json
{
    "body": "Merged in Sage 2.10.alpha1.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-10T05:42:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1740#issuecomment-11005",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.alpha1.

Cheers,

Michael



---

archive/issue_comments_011006.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-10T05:42:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1740#issuecomment-11006",
    "user": "mabshoff"
}
```

Resolution: fixed
