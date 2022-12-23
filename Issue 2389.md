# Issue 2389: linbox charpoly crashes on OS X 10.5-intel

archive/issues_002389.json:
```json
{
    "body": "Assignee: cpernet\n\nThe proposed linbox-1.1.5rc1.p0 crashes on OS X 10.5-intel for charpoly computations. The bug shows up at initialization of static variables, and may be related to the specific OS X gcc compiler behaviour.\n\nhttp://gcc.gnu.org/ml/gcc-bugs/2004-02/msg02055.html, may help. \n\nSame issue as #2388, but need a clean fix.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2389\n\n",
    "created_at": "2008-03-04T22:07:30Z",
    "labels": [
        "Cygwin",
        "major",
        "bug"
    ],
    "title": "linbox charpoly crashes on OS X 10.5-intel",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2389",
    "user": "cpernet"
}
```
Assignee: cpernet

The proposed linbox-1.1.5rc1.p0 crashes on OS X 10.5-intel for charpoly computations. The bug shows up at initialization of static variables, and may be related to the specific OS X gcc compiler behaviour.

http://gcc.gnu.org/ml/gcc-bugs/2004-02/msg02055.html, may help. 

Same issue as #2388, but need a clean fix.

Issue created by migration from https://trac.sagemath.org/ticket/2389





---

archive/issue_comments_016122.json:
```json
{
    "body": "Changing component from Cygwin to packages.",
    "created_at": "2008-03-04T22:10:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2389#issuecomment-16122",
    "user": "cpernet"
}
```

Changing component from Cygwin to packages.



---

archive/issue_comments_016123.json:
```json
{
    "body": "This ticket has been superseded by #2525 and ought to be closed once that ticket has been merged.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-15T05:45:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2389#issuecomment-16123",
    "user": "mabshoff"
}
```

This ticket has been superseded by #2525 and ought to be closed once that ticket has been merged.

Cheers,

Michael



---

archive/issue_comments_016124.json:
```json
{
    "body": "Changing assignee from cpernet to mabshoff.",
    "created_at": "2008-03-15T05:45:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2389#issuecomment-16124",
    "user": "mabshoff"
}
```

Changing assignee from cpernet to mabshoff.



---

archive/issue_comments_016125.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-15T05:45:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2389#issuecomment-16125",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_016126.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-05T18:47:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2389#issuecomment-16126",
    "user": "mabshoff"
}
```

Resolution: fixed
