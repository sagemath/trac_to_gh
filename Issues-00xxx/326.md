# Issue 326: rebuild system doesn't recognise changed pyrex files on OS X

archive/issues_000326.json:
```json
{
    "body": "Assignee: @williamstein\n\nWhen I change a pyrex file (specifically rings/integer.pyx), sage -b doesn't seem to notice. I have to manually delete the corresponding .c file to get a rebuild happening. This is mac OS 10.4.9, powerpc G5, sage 2.3.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/326\n\n",
    "closed_at": "2007-03-22T02:21:45Z",
    "created_at": "2007-03-21T04:25:32Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "title": "rebuild system doesn't recognise changed pyrex files on OS X",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/326",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: @williamstein

When I change a pyrex file (specifically rings/integer.pyx), sage -b doesn't seem to notice. I have to manually delete the corresponding .c file to get a rebuild happening. This is mac OS 10.4.9, powerpc G5, sage 2.3.


Issue created by migration from https://trac.sagemath.org/ticket/326





---

archive/issue_events_000756.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-03-21T22:35:11Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/326",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/326#event-756"
}
```



---

archive/issue_comments_001537.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2007-03-21T22:35:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/326#issuecomment-1537",
    "user": "https://github.com/williamstein"
}
```

Resolution: invalid



---

archive/issue_comments_001538.json:
```json
{
    "body": "Depedency checking works fine on OS X Intel.  In fact I wrote it under OS X intel.  I\ntried exactly your example and it works. \n\nI also just tested on a G5 intel machine and dependency testing works fine under sage-2.3.\n\nI have no idea how your install is messed up, but the problem isn't something general.",
    "created_at": "2007-03-21T22:35:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/326#issuecomment-1538",
    "user": "https://github.com/williamstein"
}
```

Depedency checking works fine on OS X Intel.  In fact I wrote it under OS X intel.  I
tried exactly your example and it works. 

I also just tested on a G5 intel machine and dependency testing works fine under sage-2.3.

I have no idea how your install is messed up, but the problem isn't something general.



---

archive/issue_comments_001539.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-03-22T02:21:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/326#issuecomment-1539",
    "user": "https://github.com/williamstein"
}
```

Changing status from closed to reopened.



---

archive/issue_events_000757.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-03-22T02:21:02Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/326",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/326#event-757"
}
```



---

archive/issue_comments_001540.json:
```json
{
    "body": "Resolution changed from invalid to ",
    "created_at": "2007-03-22T02:21:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/326#issuecomment-1540",
    "user": "https://github.com/williamstein"
}
```

Resolution changed from invalid to 



---

archive/issue_events_000758.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-03-22T02:21:45Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/326",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/326#event-758"
}
```



---

archive/issue_comments_001541.json:
```json
{
    "body": "We changed some getctimes to getmtimes and all is well now for David.",
    "created_at": "2007-03-22T02:21:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/326#issuecomment-1541",
    "user": "https://github.com/williamstein"
}
```

We changed some getctimes to getmtimes and all is well now for David.



---

archive/issue_comments_001542.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-03-22T02:21:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/326#issuecomment-1542",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
