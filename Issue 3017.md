# Issue 3017: invalid link after make install

archive/issues_003017.json:
```json
{
    "body": "Assignee: mabshoff\n\nAn invalid link is present in sage 3.0 (after make install):\n\n```\n[root@achille local]# ls -l ./sage-3.0/sage/local/lib/python2.5/site-packages/polybori/polybori\nlrwxrwxrwx 1 zimmerma cacao 39 2008-04-24 14:43 ./sage-3.0/sage/local/lib/python2.5/site-packages/polybori/polybori -> ../../../share/polybori/pyroot/polybori\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3017\n\n",
    "created_at": "2008-04-24T12:54:29Z",
    "labels": [
        "component: distribution",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.1",
    "title": "invalid link after make install",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3017",
    "user": "https://github.com/zimmermann6"
}
```
Assignee: mabshoff

An invalid link is present in sage 3.0 (after make install):

```
[root@achille local]# ls -l ./sage-3.0/sage/local/lib/python2.5/site-packages/polybori/polybori
lrwxrwxrwx 1 zimmerma cacao 39 2008-04-24 14:43 ./sage-3.0/sage/local/lib/python2.5/site-packages/polybori/polybori -> ../../../share/polybori/pyroot/polybori
```


Issue created by migration from https://trac.sagemath.org/ticket/3017





---

archive/issue_comments_020686.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-04-26T05:10:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3017#issuecomment-20686",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_020687.json:
```json
{
    "body": "This link is actually pointing to hyperspace *before* make install and due to our spkg-install. It is easy to fix, so I am on it.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-26T05:10:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3017#issuecomment-20687",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This link is actually pointing to hyperspace *before* make install and due to our spkg-install. It is easy to fix, so I am on it.

Cheers,

Michael



---

archive/issue_comments_020688.json:
```json
{
    "body": "The updated spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.1/alpha0/polybori-0.3.1.p2.spkg\n\nfixes the issue.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-26T05:30:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3017#issuecomment-20688",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The updated spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.1/alpha0/polybori-0.3.1.p2.spkg

fixes the issue.

Cheers,

Michael



---

archive/issue_comments_020689.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-04-26T06:48:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3017#issuecomment-20689",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_020690.json:
```json
{
    "body": "Merged in Sage 3.0.1.alpha0",
    "created_at": "2008-04-26T06:49:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3017#issuecomment-20690",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.1.alpha0



---

archive/issue_comments_020691.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-26T06:49:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3017#issuecomment-20691",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_003222.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-26T06:49:59Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3017",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3017#event-3222"
}
```
