# Issue 1079: DSage improper get_worker_count

archive/issues_001079.json:
```json
{
    "body": "Assignee: @williamstein\n\nWhen I do D.get_worker_count(), it always tells me that I have 2 workers--even though I have 30 machines connected each with 2 workers so the answer should be 30*2 = 60.  It works OK if I have only one DSage login with, say, 12 workers.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1079\n\n",
    "created_at": "2007-11-03T17:11:50Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.12",
    "title": "DSage improper get_worker_count",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1079",
    "user": "https://github.com/jvoight"
}
```
Assignee: @williamstein

When I do D.get_worker_count(), it always tells me that I have 2 workers--even though I have 30 machines connected each with 2 workers so the answer should be 30*2 = 60.  It works OK if I have only one DSage login with, say, 12 workers.


Issue created by migration from https://trac.sagemath.org/ticket/1079





---

archive/issue_comments_006507.json:
```json
{
    "body": "Changing assignee from @williamstein to @yqiang.",
    "created_at": "2007-11-03T17:48:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1079#issuecomment-6507",
    "user": "https://github.com/yqiang"
}
```

Changing assignee from @williamstein to @yqiang.



---

archive/issue_comments_006508.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-03T20:23:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1079#issuecomment-6508",
    "user": "https://github.com/yqiang"
}
```

Resolution: fixed



---

archive/issue_events_001201.json:
```json
{
    "actor": "@yqiang",
    "created_at": "2007-11-03T20:23:09Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1079",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1079#event-1201"
}
```



---

archive/issue_comments_006509.json:
```json
{
    "body": "Fixed.  Get bundle here:\nhttp://sage.math.washington.edu/home/yqiang/dsage.hg",
    "created_at": "2007-11-03T20:23:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1079#issuecomment-6509",
    "user": "https://github.com/yqiang"
}
```

Fixed.  Get bundle here:
http://sage.math.washington.edu/home/yqiang/dsage.hg



---

archive/issue_comments_006510.json:
```json
{
    "body": "Reopening",
    "created_at": "2007-11-03T20:28:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1079#issuecomment-6510",
    "user": "https://github.com/yqiang"
}
```

Reopening



---

archive/issue_comments_006511.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2007-11-03T20:28:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1079#issuecomment-6511",
    "user": "https://github.com/yqiang"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_006512.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-11-03T20:28:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1079#issuecomment-6512",
    "user": "https://github.com/yqiang"
}
```

Changing status from closed to reopened.



---

archive/issue_events_001202.json:
```json
{
    "actor": "@yqiang",
    "created_at": "2007-11-03T20:28:33Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/1079",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1079#event-1202"
}
```



---

archive/issue_comments_006513.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-06T21:59:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1079#issuecomment-6513",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_006514.json:
```json
{
    "body": "applied to 2.8.12.rc0",
    "created_at": "2007-11-06T21:59:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1079#issuecomment-6514",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

applied to 2.8.12.rc0



---

archive/issue_events_001203.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2007-11-06T21:59:37Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1079",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1079#event-1203"
}
```
