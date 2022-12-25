# Issue 2214: DSage and memory leaks

archive/issues_002214.json:
```json
{
    "body": "Assignee: @yqiang\n\nIf a job has a memory leak, it is not reclaimed when the worker resets itself. If the memory after reset does not go down to \"normal\" (or, say, twice normal) then it should warn the user that the job leaked memory and actually restart the worker. \n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2214\n\n",
    "closed_at": "2008-03-24T16:49:35Z",
    "created_at": "2008-02-19T22:05:09Z",
    "labels": [
        "component: dsage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.4",
    "title": "DSage and memory leaks",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2214",
    "user": "https://github.com/robertwb"
}
```
Assignee: @yqiang

If a job has a memory leak, it is not reclaimed when the worker resets itself. If the memory after reset does not go down to "normal" (or, say, twice normal) then it should warn the user that the job leaked memory and actually restart the worker. 



Issue created by migration from https://trac.sagemath.org/ticket/2214





---

archive/issue_comments_014594.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-29T06:48:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2214",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2214#issuecomment-14594",
    "user": "https://github.com/yqiang"
}
```

Changing status from new to assigned.



---

archive/issue_comments_014595.json:
```json
{
    "body": "This will be fixed once #2322 gets merged.",
    "created_at": "2008-02-29T06:48:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2214",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2214#issuecomment-14595",
    "user": "https://github.com/yqiang"
}
```

This will be fixed once #2322 gets merged.



---

archive/issue_comments_014596.json:
```json
{
    "body": "This bug has been fixed in 2.10.4, please close it.",
    "created_at": "2008-03-24T16:45:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2214",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2214#issuecomment-14596",
    "user": "https://github.com/yqiang"
}
```

This bug has been fixed in 2.10.4, please close it.



---

archive/issue_events_005281.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-24T16:49:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2214",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2214#event-5281"
}
```



---

archive/issue_comments_014597.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-24T16:49:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2214",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2214#issuecomment-14597",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_005282.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-24T16:49:35Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2214",
    "milestone": "sage-2.10.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2214#event-5282"
}
```



---

archive/issue_comments_014598.json:
```json
{
    "body": "Fixed in Sage 2.10.4 according to Yi, so close this.",
    "created_at": "2008-03-24T16:49:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2214",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2214#issuecomment-14598",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Fixed in Sage 2.10.4 according to Yi, so close this.
