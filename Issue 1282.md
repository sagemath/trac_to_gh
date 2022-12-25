# Issue 1282: make flint.spkg depend on python

archive/issues_001282.json:
```json
{
    "body": "Assignee: mabshoff\n\n```\nThe thing to do is to change the sage build process so that building\nFLINT depends on\nhaving already built Python.    Then python-2.5.1 -- built by sage -- will get\nused if you put\n  #!/usr/bin/env python\nat the top of a script or whatever.  I.e., it will be in your path.\n\nI hadn't realized that building flint required Python, so we didn't\nput that as a dependency\nin the overall Sage makefile.\n\nwilliam\n```\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1282\n\n",
    "created_at": "2007-11-26T20:25:01Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.15",
    "title": "make flint.spkg depend on python",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1282",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

```
The thing to do is to change the sage build process so that building
FLINT depends on
having already built Python.    Then python-2.5.1 -- built by sage -- will get
used if you put
  #!/usr/bin/env python
at the top of a script or whatever.  I.e., it will be in your path.

I hadn't realized that building flint required Python, so we didn't
put that as a dependency
in the overall Sage makefile.

william
```

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1282





---

archive/issue_comments_008016.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-11-26T20:25:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1282",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1282#issuecomment-8016",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_008017.json:
```json
{
    "body": "Script started on Mon Dec  3 14:08:30 2007\nWhen trying to build sage-2.8.15 under Slackware Linux, the build broke with the following messages:\n\n/sage/sage-2.8.14/spkg/build/flint-0.9-r1075.p1/src\nbash-3.1# make\npython make-profile-tables.py fmpz_poly\n/usr/bin/python: /usr/bin/python: cannot execute binary file\nmake: *** [fmpz_poly-profile-tables.o] Error 126\nbash-3.1# exit\nexit\n\nActually, I had a broken symlink /usr/bin/python (to python2.4) , but no python was\nreally installed the system. \n\nIt seems that flint tries to use python from the system, instead of the version \nincluded in Sage.",
    "created_at": "2007-12-03T20:03:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1282",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1282#issuecomment-8017",
    "user": "https://github.com/pdenapo"
}
```

Script started on Mon Dec  3 14:08:30 2007
When trying to build sage-2.8.15 under Slackware Linux, the build broke with the following messages:

/sage/sage-2.8.14/spkg/build/flint-0.9-r1075.p1/src
bash-3.1# make
python make-profile-tables.py fmpz_poly
/usr/bin/python: /usr/bin/python: cannot execute binary file
make: *** [fmpz_poly-profile-tables.o] Error 126
bash-3.1# exit
exit

Actually, I had a broken symlink /usr/bin/python (to python2.4) , but no python was
really installed the system. 

It seems that flint tries to use python from the system, instead of the version 
included in Sage.



---

archive/issue_comments_008018.json:
```json
{
    "body": "I made the 10 character change...",
    "created_at": "2007-12-04T06:48:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1282",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1282#issuecomment-8018",
    "user": "https://github.com/williamstein"
}
```

I made the 10 character change...



---

archive/issue_comments_008019.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-04T06:48:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1282",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1282#issuecomment-8019",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_003365.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-12-04T06:48:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1282",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1282#event-3365"
}
```
