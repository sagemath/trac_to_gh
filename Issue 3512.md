# Issue 3512: [with spkg, needs review] upgrade to sqlalchemy 0.4.6

archive/issues_003512.json:
```json
{
    "body": "Assignee: @yqiang\n\nCC:  @jvoight\n\nJohn Voight ran into a problem running dsage that is caused by a bug in the version of sqlalchemy (0.4.3) we ship. The latest upstream stable version is 0.4.6. \nAll dsage unit tests pass with the new sqlalchemy installed, and I think dsage is the only package using sqlalchemy currently.\n\nHere is the new spkg:\n\nhttp://sage.math.washington.edu/home/yqiang/spkgs/sqlalchemy-0.4.6.p0.spkg\n\nI commented out copying the documentation since it's readily available online, and I saw very little else in $SAGE_ROOT/local/doc. Feel to uncomment that if need be. \n\nIssue created by migration from https://trac.sagemath.org/ticket/3512\n\n",
    "created_at": "2008-06-25T21:51:23Z",
    "labels": [
        "component: dsage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "[with spkg, needs review] upgrade to sqlalchemy 0.4.6",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3512",
    "user": "https://github.com/yqiang"
}
```
Assignee: @yqiang

CC:  @jvoight

John Voight ran into a problem running dsage that is caused by a bug in the version of sqlalchemy (0.4.3) we ship. The latest upstream stable version is 0.4.6. 
All dsage unit tests pass with the new sqlalchemy installed, and I think dsage is the only package using sqlalchemy currently.

Here is the new spkg:

http://sage.math.washington.edu/home/yqiang/spkgs/sqlalchemy-0.4.6.p0.spkg

I commented out copying the documentation since it's readily available online, and I saw very little else in $SAGE_ROOT/local/doc. Feel to uncomment that if need be. 

Issue created by migration from https://trac.sagemath.org/ticket/3512





---

archive/issue_comments_024691.json:
```json
{
    "body": "Positive review. I added a line to delete old SQLAlchemy installs.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-26T03:10:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3512#issuecomment-24691",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review. I added a line to delete old SQLAlchemy installs.

Cheers,

Michael



---

archive/issue_comments_024692.json:
```json
{
    "body": "Changing assignee from @yqiang to mabshoff.",
    "created_at": "2008-06-26T03:10:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3512#issuecomment-24692",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from @yqiang to mabshoff.



---

archive/issue_comments_024693.json:
```json
{
    "body": "Changing component from dsage to packages.",
    "created_at": "2008-06-26T03:10:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3512#issuecomment-24693",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing component from dsage to packages.



---

archive/issue_comments_024694.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-26T03:10:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3512#issuecomment-24694",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_024695.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha1",
    "created_at": "2008-06-26T03:10:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3512#issuecomment-24695",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.4.alpha1



---

archive/issue_events_003729.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-06-26T03:10:51Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3512",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3512#event-3729"
}
```
