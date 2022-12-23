# Issue 4007: OSX 10.4/5: build libpng.dylib again

archive/issues_004007.json:
```json
{
    "body": "Assignee: mabshoff\n\nOn OSX we delete libpng.dylib due to missing symbols when building R and python. But this is causing trouble for code at #3324 for example. The spkg at \n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/alpha3/libpng-1.2.22.p8.spkg\n\ndoes no longer delete the old dynamic lib. But this ticket needs to be merged with the following two tickets updating R and python.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4007\n\n",
    "created_at": "2008-08-30T23:39:07Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "title": "OSX 10.4/5: build libpng.dylib again",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4007",
    "user": "mabshoff"
}
```
Assignee: mabshoff

On OSX we delete libpng.dylib due to missing symbols when building R and python. But this is causing trouble for code at #3324 for example. The spkg at 

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/alpha3/libpng-1.2.22.p8.spkg

does no longer delete the old dynamic lib. But this ticket needs to be merged with the following two tickets updating R and python.

Issue created by migration from https://trac.sagemath.org/ticket/4007





---

archive/issue_comments_028929.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-08-30T23:43:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4007#issuecomment-28929",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_028930.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-30T23:51:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4007#issuecomment-28930",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_028931.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha3",
    "created_at": "2008-08-30T23:51:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4007#issuecomment-28931",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.alpha3
