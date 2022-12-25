# Issue 3785: upgrade atlas in sage to version 3.8.2

archive/issues_003785.json:
```json
{
    "body": "Assignee: @williamstein\n\nThis is a non-negotiable blocker for Sage-3.1.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3785\n\n",
    "created_at": "2008-08-06T23:58:10Z",
    "labels": [
        "component: linear algebra",
        "blocker"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.3",
    "title": "upgrade atlas in sage to version 3.8.2",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3785",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

This is a non-negotiable blocker for Sage-3.1.

Issue created by migration from https://trac.sagemath.org/ticket/3785





---

archive/issue_comments_026852.json:
```json
{
    "body": "Changing assignee from @williamstein to mabshoff.",
    "created_at": "2008-08-07T02:42:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3785",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3785#issuecomment-26852",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from @williamstein to mabshoff.



---

archive/issue_comments_026853.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-08-07T02:42:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3785",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3785#issuecomment-26853",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_026854.json:
```json
{
    "body": "We need this for a quick build on the new sage.math hardware :)\n\nCheers,\n\nMichael",
    "created_at": "2008-12-17T14:15:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3785",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3785#issuecomment-26854",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

We need this for a quick build on the new sage.math hardware :)

Cheers,

Michael



---

archive/issue_comments_026855.json:
```json
{
    "body": "The spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/spkgs/atlas-3.8.2.spkg\n\nfixes the following problems:\n\n* update to 3.8.2\n* better detection of Pentium D and E\n* detect more Core2Duos cores\n* properly detect Dunnington cores\n\nIn addition the spkg has been cleaned up. Build time:\n\n* on the new sage.math down from 180 minutes to \n\n```\nreal\t11m36.903s\nuser\t9m58.840s\nsys\t1m17.870s\n```\n\n* On cleo/iras, i.e. Itanium2 machines on SkyNet:\n\n```\nreal\t37m34.354s\nuser\t34m18.232s\nsys\t1m20.748s\n```\n\n\nThis also fixes #3787\n\nCheers,\n\nMichael",
    "created_at": "2009-01-02T05:56:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3785",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3785#issuecomment-26855",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The spkg at

http://sage.math.washington.edu/home/mabshoff/spkgs/atlas-3.8.2.spkg

fixes the following problems:

* update to 3.8.2
* better detection of Pentium D and E
* detect more Core2Duos cores
* properly detect Dunnington cores

In addition the spkg has been cleaned up. Build time:

* on the new sage.math down from 180 minutes to 

```
real	11m36.903s
user	9m58.840s
sys	1m17.870s
```

* On cleo/iras, i.e. Itanium2 machines on SkyNet:

```
real	37m34.354s
user	34m18.232s
sys	1m20.748s
```


This also fixes #3787

Cheers,

Michael



---

archive/issue_comments_026856.json:
```json
{
    "body": "Michael, do I have to wait until there's a 3.2.3.alpha before testing this?  I have been using 3.2.2 for a while now.  John",
    "created_at": "2009-01-02T09:20:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3785",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3785#issuecomment-26856",
    "user": "https://github.com/JohnCremona"
}
```

Michael, do I have to wait until there's a 3.2.3.alpha before testing this?  I have been using 3.2.2 for a while now.  John



---

archive/issue_comments_026857.json:
```json
{
    "body": "Replying to [comment:5 cremona]:\n> Michael, do I have to wait until there's a 3.2.3.alpha before testing this?  I have been using 3.2.2 for a while now.  John\n\nThis can be tested with any recent Sage release. William did some complete build of Sage with this ATLAS.spkg, so hopefully it will get a review soon :)\n\nCheers,\n\nMichael",
    "created_at": "2009-01-02T15:45:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3785",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3785#issuecomment-26857",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:5 cremona]:
> Michael, do I have to wait until there's a 3.2.3.alpha before testing this?  I have been using 3.2.2 for a while now.  John

This can be tested with any recent Sage release. William did some complete build of Sage with this ATLAS.spkg, so hopefully it will get a review soon :)

Cheers,

Michael



---

archive/issue_events_004007.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-02T21:52:06Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3785",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3785#event-4007"
}
```



---

archive/issue_comments_026858.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-02T21:52:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3785",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3785#issuecomment-26858",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_026859.json:
```json
{
    "body": "Merged in Sage 3.2.3.final\n\nCheers,\n\nMichael",
    "created_at": "2009-01-02T21:52:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3785",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3785#issuecomment-26859",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.3.final

Cheers,

Michael
