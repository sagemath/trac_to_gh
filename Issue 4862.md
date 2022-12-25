# Issue 4862: two trivial-to-fix issues with the macaulay2 spkg

archive/issues_004862.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @haraldschilly\n\n1. The name of it in experimental is macaulay2-20061014.p1.spkg but it should be macaulay2-20081014.p1.spkg\n\n2. If you do `export MAKE=\"make -j4\"` then the build fails as follows:\n\n```\nchecking for gmake... make -j20\nchecking whether make -j20 is GNU make... ./configure: line 1497: make -j20: command not found\nconfigure: make -j20: GNU make is required\n```\n\n\nThis could be fixed by not using $MAKE to do anything in parallel, which would be better than just having it break.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4862\n\n",
    "created_at": "2008-12-24T02:16:14Z",
    "labels": [
        "component: packages: standard",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.3",
    "title": "two trivial-to-fix issues with the macaulay2 spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4862",
    "user": "https://github.com/williamstein"
}
```
Assignee: mabshoff

CC:  @haraldschilly

1. The name of it in experimental is macaulay2-20061014.p1.spkg but it should be macaulay2-20081014.p1.spkg

2. If you do `export MAKE="make -j4"` then the build fails as follows:

```
checking for gmake... make -j20
checking whether make -j20 is GNU make... ./configure: line 1497: make -j20: command not found
configure: make -j20: GNU make is required
```


This could be fixed by not using $MAKE to do anything in parallel, which would be better than just having it break.

Issue created by migration from https://trac.sagemath.org/ticket/4862





---

archive/issue_comments_036779.json:
```json
{
    "body": "And, for the record, the spkg doesn't build on the new sage.math (Ubuntu 8.04",
    "created_at": "2008-12-24T02:27:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4862#issuecomment-36779",
    "user": "https://github.com/williamstein"
}
```

And, for the record, the spkg doesn't build on the new sage.math (Ubuntu 8.04



---

archive/issue_comments_036780.json:
```json
{
    "body": "The issue is with the website, i.e. all the spkgs are in www-files.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-24T02:37:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4862#issuecomment-36780",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The issue is with the website, i.e. all the spkgs are in www-files.

Cheers,

Michael



---

archive/issue_comments_036781.json:
```json
{
    "body": "now fixed.  and it does build on sage.math, but not in parallel...",
    "created_at": "2008-12-24T03:49:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4862#issuecomment-36781",
    "user": "https://github.com/williamstein"
}
```

now fixed.  and it does build on sage.math, but not in parallel...



---

archive/issue_comments_036782.json:
```json
{
    "body": "The spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/macaulay2-1.1-r7221.p0.spkg\n\nfixes the issue:\n\n```\nmabshoff@sage:/scratch/release-cycle/junk/sage-3.2.2$ export MAKE=\"make -j8\"\nmabshoff@sage:/scratch/release-cycle/junk/sage-3.2.2$ ./sage -i macaulay2-1.1-r7221.p0\n<SNIP - things do not blow up>\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-12-24T14:34:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4862#issuecomment-36782",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The spkg at

http://sage.math.washington.edu/home/mabshoff/macaulay2-1.1-r7221.p0.spkg

fixes the issue:

```
mabshoff@sage:/scratch/release-cycle/junk/sage-3.2.2$ export MAKE="make -j8"
mabshoff@sage:/scratch/release-cycle/junk/sage-3.2.2$ ./sage -i macaulay2-1.1-r7221.p0
<SNIP - things do not blow up>
```


Cheers,

Michael



---

archive/issue_comments_036783.json:
```json
{
    "body": "Looks good.",
    "created_at": "2008-12-24T21:29:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4862#issuecomment-36783",
    "user": "https://github.com/williamstein"
}
```

Looks good.



---

archive/issue_comments_036784.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-26T17:18:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4862#issuecomment-36784",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_005105.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-26T17:18:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4862",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4862#event-5105"
}
```



---

archive/issue_comments_036785.json:
```json
{
    "body": "Merged in Sage 3.2.3.final and uploaded to the optional spkg repo.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-26T17:18:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4862#issuecomment-36785",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.3.final and uploaded to the optional spkg repo.

Cheers,

Michael
