# Issue 1513: FLINT install uses make -B, which isn't an option on (slightly) older make versions

archive/issues_001513.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe title pretty much says it all. make 3.79.1 doesn't support make -B, and I'm likely not the only person with a slightly outdated version of make, so we should see if this can be switched around at all.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1513\n\n",
    "created_at": "2007-12-14T23:21:40Z",
    "labels": [
        "packages: standard",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "FLINT install uses make -B, which isn't an option on (slightly) older make versions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1513",
    "user": "@craigcitro"
}
```
Assignee: @williamstein

The title pretty much says it all. make 3.79.1 doesn't support make -B, and I'm likely not the only person with a slightly outdated version of make, so we should see if this can be switched around at all.

Issue created by migration from https://trac.sagemath.org/ticket/1513





---

archive/issue_comments_009699.json:
```json
{
    "body": "The spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/flint-1.02.p0.spkg\n\nshould fix the problem. I don't think we will need \"-B\" since we always build the check from a tree than only had the library build in it once.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-14T23:27:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1513#issuecomment-9699",
    "user": "mabshoff"
}
```

The spkg at

http://sage.math.washington.edu/home/mabshoff/flint-1.02.p0.spkg

should fix the problem. I don't think we will need "-B" since we always build the check from a tree than only had the library build in it once.

Cheers,

Michael



---

archive/issue_comments_009700.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-14T23:44:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1513#issuecomment-9700",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_009701.json:
```json
{
    "body": "Changing assignee from @williamstein to mabshoff.",
    "created_at": "2007-12-14T23:44:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1513#issuecomment-9701",
    "user": "mabshoff"
}
```

Changing assignee from @williamstein to mabshoff.



---

archive/issue_comments_009702.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-14T23:44:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1513#issuecomment-9702",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_009703.json:
```json
{
    "body": "Merged in 2.9.rc0.",
    "created_at": "2007-12-14T23:44:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1513#issuecomment-9703",
    "user": "mabshoff"
}
```

Merged in 2.9.rc0.
