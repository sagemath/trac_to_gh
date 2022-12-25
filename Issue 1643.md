# Issue 1643: Fortran.spkg: If SAGE_FORTRAN is set do not copy the binary to sage_fortran.bin

archive/issues_001643.json:
```json
{
    "body": "Assignee: mabshoff\n\nWe shouldn't copy the binary named in `SAGE_FORTRAN` to `sage_fortran.bin` since it seems to break gfortran. Some times it seems to assume the position of libgfortran.so to be relative to the invoking executable and then breaks things will break. Just make the script `sage_fortran` call\n\n```/bin/bash\nvalue of SAGE_FORTRAN $*\n```\n\nThat way a bdist is also less likely to break if the version of the fortran compiler is slightly different. It will also result in a slightly smaller Sage install, which is also a good thing.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1643\n\n",
    "created_at": "2007-12-30T18:56:17Z",
    "labels": [
        "component: packages: standard",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9.2",
    "title": "Fortran.spkg: If SAGE_FORTRAN is set do not copy the binary to sage_fortran.bin",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1643",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

We shouldn't copy the binary named in `SAGE_FORTRAN` to `sage_fortran.bin` since it seems to break gfortran. Some times it seems to assume the position of libgfortran.so to be relative to the invoking executable and then breaks things will break. Just make the script `sage_fortran` call

```/bin/bash
value of SAGE_FORTRAN $*
```

That way a bdist is also less likely to break if the version of the fortran compiler is slightly different. It will also result in a slightly smaller Sage install, which is also a good thing.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1643





---

archive/issue_comments_010422.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-31T10:24:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1643#issuecomment-10422",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_010423.json:
```json
{
    "body": "Hopefully this fixes that problem. In case that SAGE_FORTRAN is a valid path\nthe sage_fortran wrapper directly calls that as opposed to calling sage_fortran.bin which is symlinked to sage_fortran. \n\n(note I didn't change the case where g95 doesn't work but we find something without the users specifying a valid SAGE_FORTRAN, maybe I should change that too)\n\nAlso, i tested that which produces a correctly function sage_fortran, but didn't build anything with it yet so that should be done.\n\nhttp://sage.math.washington.edu/home/jkantor/spkgs/fortran-20071120.p2.spkg",
    "created_at": "2008-01-04T09:16:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1643#issuecomment-10423",
    "user": "https://trac.sagemath.org/admin/accounts/users/jkantor"
}
```

Hopefully this fixes that problem. In case that SAGE_FORTRAN is a valid path
the sage_fortran wrapper directly calls that as opposed to calling sage_fortran.bin which is symlinked to sage_fortran. 

(note I didn't change the case where g95 doesn't work but we find something without the users specifying a valid SAGE_FORTRAN, maybe I should change that too)

Also, i tested that which produces a correctly function sage_fortran, but didn't build anything with it yet so that should be done.

http://sage.math.washington.edu/home/jkantor/spkgs/fortran-20071120.p2.spkg



---

archive/issue_events_001803.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-01-04T10:44:12Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1643",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1643#event-1803"
}
```



---

archive/issue_comments_010424.json:
```json
{
    "body": "Merged in 2.9.2.rc0",
    "created_at": "2008-01-04T10:44:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1643#issuecomment-10424",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.9.2.rc0



---

archive/issue_comments_010425.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-04T10:44:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1643#issuecomment-10425",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
