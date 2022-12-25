# Issue 640: get rid of the circular link that is created when installing the python spkg

archive/issues_000640.json:
```json
{
    "body": "Assignee: @williamstein\n\n```\nwas@ubuntu:~/s/local/lib/python$ ls -l|grep python\nlrwxrwxrwx  1 was was      6 2007-09-03 20:06 python -> python\nlrwxrwxrwx  1 was was      9 2007-09-03 20:06 python2.5 -> python2.5\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/640\n\n",
    "created_at": "2007-09-11T20:25:30Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.4.2",
    "title": "get rid of the circular link that is created when installing the python spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/640",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

```
was@ubuntu:~/s/local/lib/python$ ls -l|grep python
lrwxrwxrwx  1 was was      6 2007-09-03 20:06 python -> python
lrwxrwxrwx  1 was was      9 2007-09-03 20:06 python2.5 -> python2.5
```

Issue created by migration from https://trac.sagemath.org/ticket/640





---

archive/issue_comments_003294.json:
```json
{
    "body": "A fixed spkg can be found at:\n\nhttp://fsmath.mathematik.uni-dortmund.de/~mabshoff/sage/python-2.5.1.p7.spkg\n\nCheers,\n\nMichael",
    "created_at": "2007-09-13T12:38:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/640#issuecomment-3294",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

A fixed spkg can be found at:

http://fsmath.mathematik.uni-dortmund.de/~mabshoff/sage/python-2.5.1.p7.spkg

Cheers,

Michael



---

archive/issue_comments_003295.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-13T14:03:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/640#issuecomment-3295",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_001705.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-09-13T14:03:20Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/640",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/640#event-1705"
}
```



---

archive/issue_events_001706.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-09-13T14:03:20Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/640",
    "milestone": "sage-2.8.4.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/640#event-1706"
}
```
