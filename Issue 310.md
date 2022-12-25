# Issue 310: Debian testing version of mercurial refers to plugin not included in SAGE mercurial

archive/issues_000310.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: mercurial\n\nAt least the latest version of mercurial from Debian testing (version 0.9.3-2), and possibly earlier versions as well, have a line in /etc/mercurial/hgrc.d/hgext.rc that tries to load the extension hgext/churn.  Since SAGE mercurial does not include this extension, every mercurial operation gives the following warning:\n\n```\n*** failed to import extension hgext/churn: No module named hgext/churn\n```\n\n(However, mercurial seems to work fine even with the warning.)\n\nPerhaps SAGE's mercurial should ignore /etc/mercurial, or perhaps SAGE's mercurial should be updated to include the churn extension.\n\nOr, of course, Debian users can remove the line from hgext.rc, or just ignore the warning message.\n\nIssue created by migration from https://trac.sagemath.org/ticket/310\n\n",
    "created_at": "2007-03-06T06:18:40Z",
    "labels": [
        "component: packages: standard",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.9",
    "title": "Debian testing version of mercurial refers to plugin not included in SAGE mercurial",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/310",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: @williamstein

Keywords: mercurial

At least the latest version of mercurial from Debian testing (version 0.9.3-2), and possibly earlier versions as well, have a line in /etc/mercurial/hgrc.d/hgext.rc that tries to load the extension hgext/churn.  Since SAGE mercurial does not include this extension, every mercurial operation gives the following warning:

```
*** failed to import extension hgext/churn: No module named hgext/churn
```

(However, mercurial seems to work fine even with the warning.)

Perhaps SAGE's mercurial should ignore /etc/mercurial, or perhaps SAGE's mercurial should be updated to include the churn extension.

Or, of course, Debian users can remove the line from hgext.rc, or just ignore the warning message.

Issue created by migration from https://trac.sagemath.org/ticket/310





---

archive/issue_comments_001475.json:
```json
{
    "body": "We should discuss and decide what to do about this.\n\nCheers,\n\nMichael",
    "created_at": "2007-09-10T03:32:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/310#issuecomment-1475",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

We should discuss and decide what to do about this.

Cheers,

Michael



---

archive/issue_comments_001476.json:
```json
{
    "body": "I've put up a new mercurial spkg that fixes this problem (by ignoring /etc/mercurial), and also upgrades to mercurial 0.9.5:\nhttp://sage.math.washington.edu/home/cwitty/mercurial-0.9.5.spkg",
    "created_at": "2007-10-21T01:51:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/310#issuecomment-1476",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

I've put up a new mercurial spkg that fixes this problem (by ignoring /etc/mercurial), and also upgrades to mercurial 0.9.5:
http://sage.math.washington.edu/home/cwitty/mercurial-0.9.5.spkg



---

archive/issue_comments_001477.json:
```json
{
    "body": "I put the spkg linked in by cwitty in 2.8.9.alpha0.",
    "created_at": "2007-10-23T17:42:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/310#issuecomment-1477",
    "user": "https://github.com/malb"
}
```

I put the spkg linked in by cwitty in 2.8.9.alpha0.



---

archive/issue_comments_001478.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-23T17:42:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/310#issuecomment-1478",
    "user": "https://github.com/malb"
}
```

Resolution: fixed



---

archive/issue_events_000329.json:
```json
{
    "actor": "https://github.com/malb",
    "created_at": "2007-10-23T17:42:36Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/310",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/310#event-329"
}
```
