# Issue 7030: quaddouble-2.2.p9 believe Sun's C++ compiler is broken.

archive/issues_007030.json:
```json
{
    "body": "Assignee: tbd\n\nUsing\n\n* Solaris 10 update 7 on SPARC\n* sage-4.1.2.alpha2\n* Sun Studio 12.1\n* An updated configure script to allow the Sun compiler to be used\n\nCC was set to the Sun C compler, and CXX to the Sun C++ compiler,\n\nThe 'quaddouble-2.2.p9' package believes the Sun C++ compiler can't create executables. \n\n\n```\nconfigure: error: C++ compiler cannot create executables\nSee `config.log' for more details.\nerror configuring quad double\n```\n\n\nBut other configure scripts have found the default output is a.out, so I'm pretty sure the Sun compiler can create executables! Maybe the test used is invalid. \n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7030\n\n",
    "created_at": "2009-09-27T13:58:25Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "quaddouble-2.2.p9 believe Sun's C++ compiler is broken.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7030",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: tbd

Using

* Solaris 10 update 7 on SPARC
* sage-4.1.2.alpha2
* Sun Studio 12.1
* An updated configure script to allow the Sun compiler to be used

CC was set to the Sun C compler, and CXX to the Sun C++ compiler,

The 'quaddouble-2.2.p9' package believes the Sun C++ compiler can't create executables. 


```
configure: error: C++ compiler cannot create executables
See `config.log' for more details.
error configuring quad double
```


But other configure scripts have found the default output is a.out, so I'm pretty sure the Sun compiler can create executables! Maybe the test used is invalid. 




Issue created by migration from https://trac.sagemath.org/ticket/7030





---

archive/issue_events_007251.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-10-01T15:35:37Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7030",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7030#event-7251"
}
```



---

archive/issue_comments_058119.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-10-01T15:35:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7030#issuecomment-58119",
    "user": "https://github.com/williamstein"
}
```

Resolution: invalid



---

archive/issue_comments_058120.json:
```json
{
    "body": "Quaddouble was supposed to be removed from Sage long ago.   So there is no point in fixing it.",
    "created_at": "2009-10-01T15:35:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7030#issuecomment-58120",
    "user": "https://github.com/williamstein"
}
```

Quaddouble was supposed to be removed from Sage long ago.   So there is no point in fixing it.
