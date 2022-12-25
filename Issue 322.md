# Issue 322: Have global code page for Notebook

archive/issues_000322.json:
```json
{
    "body": "Assignee: boothby\n\nCreate a system for adding code to a notebook that can be executed by code in any cell in the worksheet. Before a chuck of code could become global the system would check it to make sure it does overwrite current SAGE functions, variables, and classes. Maybe the system could do that by executing the code and using the name space key in the various dictionaries to then see if a not found error is returned when name space called. It would be also be important for it to be easy to download a code package to be made global. I want this so I can make apps and use them from any cell in the notebook.\n\nIssue created by migration from https://trac.sagemath.org/ticket/322\n\n",
    "closed_at": "2020-03-29T02:12:30Z",
    "created_at": "2007-03-15T09:20:37Z",
    "labels": [
        "component: notebook",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-feature",
    "title": "Have global code page for Notebook",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/322",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```
Assignee: boothby

Create a system for adding code to a notebook that can be executed by code in any cell in the worksheet. Before a chuck of code could become global the system would check it to make sure it does overwrite current SAGE functions, variables, and classes. Maybe the system could do that by executing the code and using the name space key in the various dictionaries to then see if a not found error is returned when name space called. It would be also be important for it to be easy to download a code package to be made global. I want this so I can make apps and use them from any cell in the notebook.

Issue created by migration from https://trac.sagemath.org/ticket/322





---

archive/issue_comments_001522.json:
```json
{
    "body": "This functionality is already provided in the SAGE notebook by putting #auto somewhere\nin a cell.  Also, using %hideall one can even hide the global code.  \n\nIt's odd, because I've seen you use this functionality in your example sage notebook\napplications, so you know about it.  Hmm.",
    "created_at": "2007-03-21T22:46:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/322#issuecomment-1522",
    "user": "https://github.com/williamstein"
}
```

This functionality is already provided in the SAGE notebook by putting #auto somewhere
in a cell.  Also, using %hideall one can even hide the global code.  

It's odd, because I've seen you use this functionality in your example sage notebook
applications, so you know about it.  Hmm.



---

archive/issue_events_000749.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-03-21T22:46:42Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/322",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/322#event-749"
}
```



---

archive/issue_comments_001523.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2007-03-21T22:46:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/322#issuecomment-1523",
    "user": "https://github.com/williamstein"
}
```

Resolution: invalid



---

archive/issue_comments_001524.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-03-26T03:58:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/322#issuecomment-1524",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Changing status from closed to reopened.



---

archive/issue_events_000750.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans",
    "created_at": "2007-03-26T03:58:37Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/322",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/322#event-750"
}
```



---

archive/issue_comments_001525.json:
```json
{
    "body": "I said notebook not worksheet. I'm talking about writing a function or class in a global worksheet from I could use from anyother worksheet. #auto has nothing to do with global just writing a function in a cell makes that function global for the whole worksheet that the function is defined in.",
    "created_at": "2007-03-26T03:58:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/322#issuecomment-1525",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

I said notebook not worksheet. I'm talking about writing a function or class in a global worksheet from I could use from anyother worksheet. #auto has nothing to do with global just writing a function in a cell makes that function global for the whole worksheet that the function is defined in.



---

archive/issue_comments_001526.json:
```json
{
    "body": "Resolution changed from invalid to ",
    "created_at": "2007-03-26T03:58:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/322#issuecomment-1526",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Resolution changed from invalid to 



---

archive/issue_events_000751.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-09-11T00:51:04Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/322",
    "milestone": "sage-feature",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/322#event-751"
}
```



---

archive/issue_comments_001527.json:
```json
{
    "body": "See https://github.com/sagemath/sagenb/issues/263 where I suggest that the easiest thing to do is have a 'global' (per user) DATA directory just like there is the per-worksheet DATA directory.",
    "created_at": "2014-11-20T13:59:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/322#issuecomment-1527",
    "user": "https://github.com/kcrisman"
}
```

See https://github.com/sagemath/sagenb/issues/263 where I suggest that the easiest thing to do is have a 'global' (per user) DATA directory just like there is the per-worksheet DATA directory.



---

archive/issue_comments_001528.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-03-29T02:12:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/322#issuecomment-1528",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Resolution: invalid



---

archive/issue_events_000752.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/boothby",
    "created_at": "2020-03-29T02:12:30Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/322",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/322#event-752"
}
```



---

archive/issue_comments_001529.json:
```json
{
    "body": "Closing deprecated notebook tickets",
    "created_at": "2020-03-29T02:12:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/322#issuecomment-1529",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Closing deprecated notebook tickets
