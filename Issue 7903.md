# Issue 7903: mixing a non-GNU Fortran compiler with GCC is not detected very early

archive/issues_007903.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nMixing compilers (say GNU and Sun), should not be permitted. There is code in prereq which carefully checks this for C and C++ compilers, and even checks the version numbers for gcc. But for Fortran the checks are not as well done. \n\nMixing Sun Studio compilers with gfortran is detected in readline, but it should be done earlier. \n\nI'm the one to blame for this, as I've updated 'prereq' a few times. That said, it will catch a lot more errors than it used to do. \n\nDave \n\nIssue created by migration from https://trac.sagemath.org/ticket/7903\n\n",
    "created_at": "2010-01-12T06:42:07Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "mixing a non-GNU Fortran compiler with GCC is not detected very early",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7903",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: GeorgSWeber

Mixing compilers (say GNU and Sun), should not be permitted. There is code in prereq which carefully checks this for C and C++ compilers, and even checks the version numbers for gcc. But for Fortran the checks are not as well done. 

Mixing Sun Studio compilers with gfortran is detected in readline, but it should be done earlier. 

I'm the one to blame for this, as I've updated 'prereq' a few times. That said, it will catch a lot more errors than it used to do. 

Dave 

Issue created by migration from https://trac.sagemath.org/ticket/7903





---

archive/issue_comments_068607.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-31T22:33:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7903#issuecomment-68607",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_008118.json:
```json
{
    "actor": "mvngu",
    "created_at": "2010-01-31T22:33:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7903",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7903#event-8118"
}
```



---

archive/issue_comments_068608.json:
```json
{
    "body": "Close as fixed by #8052.",
    "created_at": "2010-01-31T22:33:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7903#issuecomment-68608",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Close as fixed by #8052.
