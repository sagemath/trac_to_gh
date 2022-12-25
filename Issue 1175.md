# Issue 1175: circular link in sage/local/lib/python2.5

archive/issues_001175.json:
```json
{
    "body": "Assignee: mabshoff\n\nWhen building sage-2.8.12, there are two circular links in sage/local/lib/python2.5:\n\n```\nachille% pwd\n/net/achille/localdisk/zimmerma/sage-2.8.12/local/lib/python2.5\nachille% ls -l pyt*\nlrwxrwxrwx 1 zimmerma spaces 6 2007-11-14 09:53 python -> python\nlrwxrwxrwx 1 zimmerma spaces 9 2007-11-14 09:53 python2.5 -> python2.5\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1175\n\n",
    "created_at": "2007-11-15T08:27:09Z",
    "labels": [
        "component: distribution",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9.1",
    "title": "circular link in sage/local/lib/python2.5",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1175",
    "user": "https://github.com/zimmermann6"
}
```
Assignee: mabshoff

When building sage-2.8.12, there are two circular links in sage/local/lib/python2.5:

```
achille% pwd
/net/achille/localdisk/zimmerma/sage-2.8.12/local/lib/python2.5
achille% ls -l pyt*
lrwxrwxrwx 1 zimmerma spaces 6 2007-11-14 09:53 python -> python
lrwxrwxrwx 1 zimmerma spaces 9 2007-11-14 09:53 python2.5 -> python2.5
```


Issue created by migration from https://trac.sagemath.org/ticket/1175





---

archive/issue_comments_007243.json:
```json
{
    "body": "I thought we did fix that a while ago. Kate did report at least a similar issue. I will look into this in this release cycle.\n\nCheers,\n\nMichael",
    "created_at": "2007-11-21T22:20:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1175",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1175#issuecomment-7243",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I thought we did fix that a while ago. Kate did report at least a similar issue. I will look into this in this release cycle.

Cheers,

Michael



---

archive/issue_comments_007244.json:
```json
{
    "body": "Ok, while we fixed the issue in the python.spkg itself the same problem pops up when we install the mercurial.spkg. The spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/mercurial-0.9.5.p0.spkg\n\nfixes that issue and actually creates an hg repo inside the spkk as well as does some general cleanup. Another python based spkg might still recreate those links, so this might not be over yet.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-19T07:40:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1175",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1175#issuecomment-7244",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ok, while we fixed the issue in the python.spkg itself the same problem pops up when we install the mercurial.spkg. The spkg at

http://sage.math.washington.edu/home/mabshoff/mercurial-0.9.5.p0.spkg

fixes that issue and actually creates an hg repo inside the spkk as well as does some general cleanup. Another python based spkg might still recreate those links, so this might not be over yet.

Cheers,

Michael



---

archive/issue_comments_007245.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-19T19:08:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1175",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1175#issuecomment-7245",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_comments_007246.json:
```json
{
    "body": "Merged in Sage 2.9.1 alpha2",
    "created_at": "2007-12-19T19:08:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1175",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1175#issuecomment-7246",
    "user": "https://github.com/rlmill"
}
```

Merged in Sage 2.9.1 alpha2



---

archive/issue_events_001307.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2007-12-19T19:08:01Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1175",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1175#event-1307"
}
```
