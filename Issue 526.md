# Issue 526: better support for parallel make

archive/issues_000526.json:
```json
{
    "body": "Assignee: was\n\nCC:  dmharvey@math.harvard.edu\n\na.k.a. `make -j`\n\nSee discussion at\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/a88d59dc35404507\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/526\n\n",
    "created_at": "2007-08-30T04:30:52Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "title": "better support for parallel make",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/526",
    "user": "dmharvey"
}
```
Assignee: was

CC:  dmharvey@math.harvard.edu

a.k.a. `make -j`

See discussion at

http://groups.google.com/group/sage-devel/browse_thread/thread/a88d59dc35404507


Issue created by migration from https://trac.sagemath.org/ticket/526





---

archive/issue_comments_002672.json:
```json
{
    "body": "Changing keywords from \"\" to \"package audit\".",
    "created_at": "2007-11-20T14:09:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/526#issuecomment-2672",
    "user": "mabshoff"
}
```

Changing keywords from "" to "package audit".



---

archive/issue_comments_002673.json:
```json
{
    "body": "The issue has been solved and needs to be properly documented. If you do\n\n```\nexport MAKE=\"make -j4\"\nmake\n```\n\nSage will be build with up to 4 jobs in parallel. Spkgs like Singular which do not build properly with parallel make make sure that MAKE is reset while building themselves.\n\nSo somebody send us a patch for the manual. We also need to audit all packages and change make to $MAKE.\n\nCheers,\n\nMichaek",
    "created_at": "2007-11-20T14:09:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/526#issuecomment-2673",
    "user": "mabshoff"
}
```

The issue has been solved and needs to be properly documented. If you do

```
export MAKE="make -j4"
make
```

Sage will be build with up to 4 jobs in parallel. Spkgs like Singular which do not build properly with parallel make make sure that MAKE is reset while building themselves.

So somebody send us a patch for the manual. We also need to audit all packages and change make to $MAKE.

Cheers,

Michaek



---

archive/issue_comments_002674.json:
```json
{
    "body": "Changing assignee from was to gfurnish.",
    "created_at": "2008-03-09T05:15:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/526#issuecomment-2674",
    "user": "gfurnish"
}
```

Changing assignee from was to gfurnish.



---

archive/issue_comments_002675.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-09T05:15:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/526#issuecomment-2675",
    "user": "gfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_002676.json:
```json
{
    "body": "Changing assignee from gfurnish to mabshoff.",
    "created_at": "2008-09-26T09:18:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/526#issuecomment-2676",
    "user": "mabshoff"
}
```

Changing assignee from gfurnish to mabshoff.



---

archive/issue_comments_002677.json:
```json
{
    "body": "This has been fixed. Every spkg that can be build in parallel does get build that way.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-26T09:18:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/526#issuecomment-2677",
    "user": "mabshoff"
}
```

This has been fixed. Every spkg that can be build in parallel does get build that way.

Cheers,

Michael



---

archive/issue_comments_002678.json:
```json
{
    "body": "Changing status from assigned to new.",
    "created_at": "2008-09-26T09:18:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/526#issuecomment-2678",
    "user": "mabshoff"
}
```

Changing status from assigned to new.



---

archive/issue_comments_002679.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-26T09:18:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/526#issuecomment-2679",
    "user": "mabshoff"
}
```

Resolution: fixed
