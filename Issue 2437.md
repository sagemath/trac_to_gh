# Issue 2437: update eclib.spkg to eclib-20080304.spkg

archive/issues_002437.json:
```json
{
    "body": "Assignee: mabshoff\n\nThis spkg is required for #2394 to wrap newforms\n\nIssue created by migration from https://trac.sagemath.org/ticket/2437\n\n",
    "created_at": "2008-03-09T06:45:02Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "update eclib.spkg to eclib-20080304.spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2437",
    "user": "mabshoff"
}
```
Assignee: mabshoff

This spkg is required for #2394 to wrap newforms

Issue created by migration from https://trac.sagemath.org/ticket/2437





---

archive/issue_comments_016487.json:
```json
{
    "body": "I fail to see any difference to eclib-20080127.p0 in the hg log, so can somebody enlighten me what is different?\n\nCheers,\n\nMichael",
    "created_at": "2008-03-09T06:50:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2437",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2437#issuecomment-16487",
    "user": "mabshoff"
}
```

I fail to see any difference to eclib-20080127.p0 in the hg log, so can somebody enlighten me what is different?

Cheers,

Michael



---

archive/issue_comments_016488.json:
```json
{
    "body": "http://sage.math.washington.edu/home/boothby/SPKG/2.10.4/eclib-20080310.spkg",
    "created_at": "2008-03-13T06:20:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2437",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2437#issuecomment-16488",
    "user": "boothby"
}
```

http://sage.math.washington.edu/home/boothby/SPKG/2.10.4/eclib-20080310.spkg



---

archive/issue_comments_016489.json:
```json
{
    "body": "I tried installing this with 'sage -i' and got the following error:\n\n\n```\neclib-20080127.p1/src/g0n/nfd.cc\neclib-20080127.p1/src/g0n/nflist.cc\neclib-20080127.p1/src/g0n/nftest.out\neclib-20080127.p1/src/g0n/nftest.in\neclib-20080127.p1/src/g0n/documentation.txt\neclib-20080127.p1/src/Makefile.dynamic\neclib-20080127.p1/src/lib/\nFinished extraction\nsage: After decompressing the directory eclib-20080310 does not exist\nThis means that the corresponding .spkg needs to be downloaded\nagain.\nhttp://www.sagemath.org//packages/optional/eclib-20080310.spkg --> eclib-20080310.spkg\n[.]\nhttp://www.sagemath.org//packages/standard/eclib-20080310.spkg --> eclib-20080310.spkg\n[.]\nhttp://www.sagemath.org//packages/experimental/eclib-20080310.spkg --> eclib-20080310.spkg\n[.]\nhttp://www.sagemath.org//packages/archive/eclib-20080310.spkg --> eclib-20080310.spkg\n[.]\nUnable to download eclib-20080310\nPlease see http://www.sagemath.org//packages for a list of valid packages\n/home/mhansen/sage-2.10.4.alpha0-sage.math-only-x86_64-Linux/spkg/build\nbunzip2: Can't open input file eclib-20080310.spkg: No such file or directory.\ntar: eclib-20080310.spkg: Cannot open: No such file or directory\ntar: Error is not recoverable: exiting now\nSecond download resulted in a corrupted package.\n```\n",
    "created_at": "2008-03-15T21:39:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2437",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2437#issuecomment-16489",
    "user": "@mwhansen"
}
```

I tried installing this with 'sage -i' and got the following error:


```
eclib-20080127.p1/src/g0n/nfd.cc
eclib-20080127.p1/src/g0n/nflist.cc
eclib-20080127.p1/src/g0n/nftest.out
eclib-20080127.p1/src/g0n/nftest.in
eclib-20080127.p1/src/g0n/documentation.txt
eclib-20080127.p1/src/Makefile.dynamic
eclib-20080127.p1/src/lib/
Finished extraction
sage: After decompressing the directory eclib-20080310 does not exist
This means that the corresponding .spkg needs to be downloaded
again.
http://www.sagemath.org//packages/optional/eclib-20080310.spkg --> eclib-20080310.spkg
[.]
http://www.sagemath.org//packages/standard/eclib-20080310.spkg --> eclib-20080310.spkg
[.]
http://www.sagemath.org//packages/experimental/eclib-20080310.spkg --> eclib-20080310.spkg
[.]
http://www.sagemath.org//packages/archive/eclib-20080310.spkg --> eclib-20080310.spkg
[.]
Unable to download eclib-20080310
Please see http://www.sagemath.org//packages for a list of valid packages
/home/mhansen/sage-2.10.4.alpha0-sage.math-only-x86_64-Linux/spkg/build
bunzip2: Can't open input file eclib-20080310.spkg: No such file or directory.
tar: eclib-20080310.spkg: Cannot open: No such file or directory
tar: Error is not recoverable: exiting now
Second download resulted in a corrupted package.
```




---

archive/issue_comments_016490.json:
```json
{
    "body": "Hi Tom,\n\nthe spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/SPKG/eclib-20080310.p0.spkg\n\nfixes the problem Mike had and another thing I found:\n\n* the name of the spkg must match the directory name, i.e. eclib-20080310.p0.spkg unpacks into eclib-20080310.p0\n* you forgot to update SPKG.txt\n\nThe new spkg builds fine, but I am doing some more testing before giving it a positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-19T10:37:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2437",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2437#issuecomment-16490",
    "user": "mabshoff"
}
```

Hi Tom,

the spkg at

http://sage.math.washington.edu/home/mabshoff/SPKG/eclib-20080310.p0.spkg

fixes the problem Mike had and another thing I found:

* the name of the spkg must match the directory name, i.e. eclib-20080310.p0.spkg unpacks into eclib-20080310.p0
* you forgot to update SPKG.txt

The new spkg builds fine, but I am doing some more testing before giving it a positive review.

Cheers,

Michael



---

archive/issue_comments_016491.json:
```json
{
    "body": "I also fixed some permission issues since John seems to have a rather tight umask. In total I give this spkg a positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-19T11:01:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2437",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2437#issuecomment-16491",
    "user": "mabshoff"
}
```

I also fixed some permission issues since John seems to have a rather tight umask. In total I give this spkg a positive review.

Cheers,

Michael



---

archive/issue_comments_016492.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-19T11:35:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2437",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2437#issuecomment-16492",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_016493.json:
```json
{
    "body": "Merged in Sage 2.11.alpha0",
    "created_at": "2008-03-19T11:35:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2437",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2437#issuecomment-16493",
    "user": "mabshoff"
}
```

Merged in Sage 2.11.alpha0
