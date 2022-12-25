# Issue 4024: [with spkg, needs review] upgrade M4RI to newest upstream release

archive/issues_004024.json:
```json
{
    "body": "Assignee: @malb\n\nKeywords: spkg\n\nThe newest M4RI upstream release improves performance, has some bug fixes and support for parallel matrix elimination (only makes sense on an Opteron). \n\n## 20080624 (Sage 3.1.2.alpha3)\n\n### Matrix Elimination\n|       |        |        |        |        |\n|-------|--------|--------|--------|--------|\n| Dim   | min    | avg    | med    | max    |\n| 10000 |  1.809 |  1.820 |  1.821 |  1.850 |\n| 16384 |  7.625 |  7.772 |  7.761 |  8.090 |\n| 20000 | 13.746 | 13.932 | 13.899 | 14.370 |\n| 32000 | 45.865 | 46.001 | 46.081 | 46.121 |\n### Matrix Multiplication\n|       |        |        |        |        |\n|-------|--------|--------|--------|--------|\n| Dim   | min    | avg    | med    | max    |\n| 10000 |  1.817 |  1.822 |  1.821 |  1.839 |\n| 16384 |  6.856 |  6.895 |  6.865 |  7.012 |\n| 20000 | 12.690 | 12.703 | 12.699 | 12.761 |\n| 32000 | 52.878 | 53.929 | 53.460 | 58.142 |\n## 20080826 (newest upstream)\n### Matrix Elimination\n|       |        |        |        |        |\n|-------|--------|--------|--------|--------|\n| Dim   | min    | avg    | med    | max    |\n| 10000 |  1.501 |  1.509 |  1.515 |  1.515 |\n| 16384 |  6.468 |  6.670 |  6.801 |  6.990 |\n| 20000 | 11.877 | 11.901 | 11.910 | 11.934 |\n| 32000 | 41.513 | 41.623 | 41.671 | 41.691 |\n### Matrix Multiplication\n\nIssue created by migration from https://trac.sagemath.org/ticket/4024\n\n",
    "created_at": "2008-08-31T19:21:03Z",
    "labels": [
        "component: packages: standard"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "[with spkg, needs review] upgrade M4RI to newest upstream release",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4024",
    "user": "https://github.com/malb"
}
```
Assignee: @malb

Keywords: spkg

The newest M4RI upstream release improves performance, has some bug fixes and support for parallel matrix elimination (only makes sense on an Opteron). 

## 20080624 (Sage 3.1.2.alpha3)

### Matrix Elimination
|       |        |        |        |        |
|-------|--------|--------|--------|--------|
| Dim   | min    | avg    | med    | max    |
| 10000 |  1.809 |  1.820 |  1.821 |  1.850 |
| 16384 |  7.625 |  7.772 |  7.761 |  8.090 |
| 20000 | 13.746 | 13.932 | 13.899 | 14.370 |
| 32000 | 45.865 | 46.001 | 46.081 | 46.121 |
### Matrix Multiplication
|       |        |        |        |        |
|-------|--------|--------|--------|--------|
| Dim   | min    | avg    | med    | max    |
| 10000 |  1.817 |  1.822 |  1.821 |  1.839 |
| 16384 |  6.856 |  6.895 |  6.865 |  7.012 |
| 20000 | 12.690 | 12.703 | 12.699 | 12.761 |
| 32000 | 52.878 | 53.929 | 53.460 | 58.142 |
## 20080826 (newest upstream)
### Matrix Elimination
|       |        |        |        |        |
|-------|--------|--------|--------|--------|
| Dim   | min    | avg    | med    | max    |
| 10000 |  1.501 |  1.509 |  1.515 |  1.515 |
| 16384 |  6.468 |  6.670 |  6.801 |  6.990 |
| 20000 | 11.877 | 11.901 | 11.910 | 11.934 |
| 32000 | 41.513 | 41.623 | 41.671 | 41.691 |
### Matrix Multiplication

Issue created by migration from https://trac.sagemath.org/ticket/4024





---

archive/issue_comments_028963.json:
```json
{
    "body": "The SPKG is here:\n\n   http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20080831.spkg\n\nIt is based on 20080624 from 3.1.2.alpha3 so it should have all SPKG.txt fixes applied.",
    "created_at": "2008-08-31T19:22:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4024#issuecomment-28963",
    "user": "https://github.com/malb"
}
```

The SPKG is here:

   http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20080831.spkg

It is based on 20080624 from 3.1.2.alpha3 so it should have all SPKG.txt fixes applied.



---

archive/issue_comments_028964.json:
```json
{
    "body": "See #4027",
    "created_at": "2008-09-01T11:23:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4024#issuecomment-28964",
    "user": "https://github.com/malb"
}
```

See #4027



---

archive/issue_comments_028965.json:
```json
{
    "body": "The spkg at\n\nhttp://sage.math.washington.edu/home/malb/spkgs/libm4ri-20080901.spkg\n\nworks for me and fixes the at #4027 reported segfault on OSX.\n\nPositive review.\n\nCheers,\n\nMicheal",
    "created_at": "2008-09-01T12:10:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4024#issuecomment-28965",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The spkg at

http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20080901.spkg

works for me and fixes the at #4027 reported segfault on OSX.

Positive review.

Cheers,

Micheal



---

archive/issue_comments_028966.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-01T12:11:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4024#issuecomment-28966",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004254.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-01T12:11:08Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4024",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4024#event-4254"
}
```



---

archive/issue_comments_028967.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha4",
    "created_at": "2008-09-01T12:11:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4024#issuecomment-28967",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.2.alpha4
