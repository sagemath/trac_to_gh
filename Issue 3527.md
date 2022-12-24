# Issue 3527: Build python with "-O2" instead of "-O3" on Itanium

archive/issues_003527.json:
```json
{
    "body": "Assignee: mabshoff\n\nWhen building Sage's pyhton and extensions with gcc 4.3 on Itanium we get some doctest failures that disappear with \"-O2\"\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/3527\n\n",
    "created_at": "2008-06-28T09:32:34Z",
    "labels": [
        "build",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "Build python with \"-O2\" instead of \"-O3\" on Itanium",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3527",
    "user": "mabshoff"
}
```
Assignee: mabshoff

When building Sage's pyhton and extensions with gcc 4.3 on Itanium we get some doctest failures that disappear with "-O2"

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/3527





---

archive/issue_comments_024881.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-06-28T09:32:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3527",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3527#issuecomment-24881",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_024882.json:
```json
{
    "body": "This is starting to look invalid since all failures I see seem to be triggered by bugs not normally observed on non-Itanium, but valgrind finds faults in those cases on x86-64.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-07T22:28:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3527",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3527#issuecomment-24882",
    "user": "mabshoff"
}
```

This is starting to look invalid since all failures I see seem to be triggered by bugs not normally observed on non-Itanium, but valgrind finds faults in those cases on x86-64.

Cheers,

Michael



---

archive/issue_comments_024883.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-09T16:09:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3527",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3527#issuecomment-24883",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_024884.json:
```json
{
    "body": "positive review.",
    "created_at": "2008-07-09T16:09:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3527",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3527#issuecomment-24884",
    "user": "was"
}
```

positive review.



---

archive/issue_comments_024885.json:
```json
{
    "body": "Merged in Sage 3.0.4.rc2",
    "created_at": "2008-07-09T16:18:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3527",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3527#issuecomment-24885",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.4.rc2
