# Issue 5955: Sage 3.4.2.rc0: Set stacksize for clisp.spkg to 32kb

archive/issues_005955.json:
```json
{
    "body": "Assignee: mabshoff\n\nVarious boxen have too little stacksapce, i.e. FC 10 and RHEL 10 for example use 10k. This makes clisp blow up during the build, so raise the limit to 32k on linux in general.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5955\n\n",
    "created_at": "2009-05-01T06:39:31Z",
    "labels": [
        "packages: standard",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.2",
    "title": "Sage 3.4.2.rc0: Set stacksize for clisp.spkg to 32kb",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5955",
    "user": "mabshoff"
}
```
Assignee: mabshoff

Various boxen have too little stacksapce, i.e. FC 10 and RHEL 10 for example use 10k. This makes clisp blow up during the build, so raise the limit to 32k on linux in general.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5955





---

archive/issue_comments_047104.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-01T06:39:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5955#issuecomment-47104",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_047105.json:
```json
{
    "body": "The spkg at \n\n  http://sage.math.washington.edu/home/mabshoff/release-cycles-3.4.2/final/clisp-2.47.p1.spkg\n\nfixes the problem.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-04T05:16:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5955#issuecomment-47105",
    "user": "mabshoff"
}
```

The spkg at 

  http://sage.math.washington.edu/home/mabshoff/release-cycles-3.4.2/final/clisp-2.47.p1.spkg

fixes the problem.

Cheers,

Michael



---

archive/issue_comments_047106.json:
```json
{
    "body": "I installed the spkg, rebuilt maxima.  Sage starts fine, and maxima works.",
    "created_at": "2009-05-04T09:08:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5955#issuecomment-47106",
    "user": "@roed314"
}
```

I installed the spkg, rebuilt maxima.  Sage starts fine, and maxima works.



---

archive/issue_comments_047107.json:
```json
{
    "body": "Merged in sage 3.4.2.final.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-04T09:16:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5955#issuecomment-47107",
    "user": "mabshoff"
}
```

Merged in sage 3.4.2.final.

Cheers,

Michael



---

archive/issue_comments_047108.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-04T09:16:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5955#issuecomment-47108",
    "user": "mabshoff"
}
```

Resolution: fixed
