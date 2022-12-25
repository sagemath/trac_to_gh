# Issue 2393: the version of mercurial shipped with sage does not include the queue extension

archive/issues_002393.json:
```json
{
    "body": "Assignee: mabshoff\n\nIt is very annoying when trying to run hg under a Sage shell.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2393\n\n",
    "created_at": "2008-03-05T06:20:44Z",
    "labels": [
        "component: packages: standard",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "the version of mercurial shipped with sage does not include the queue extension",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2393",
    "user": "https://github.com/mwhansen"
}
```
Assignee: mabshoff

It is very annoying when trying to run hg under a Sage shell.

Issue created by migration from https://trac.sagemath.org/ticket/2393





---

archive/issue_comments_016104.json:
```json
{
    "body": "Actually, Sage's mercurial does include the queue extension; it's just not enabled by default.\n\nYou can enable it by adding these lines to $HOME/.hgrc:\n\n```\n[extensions]\n# patch queues for mercurial\n# add the 'q*' commands\nhgext.mq=\n```\n\n\nDebian enables the queue extension (along with many others) for its version of mercurial, using configuration files in /etc/mercurial.  I patched Sage's mercurial spkg to not look in /etc/mercurial, because Debian's configuration enabled extensions that were not included in Sage's mercurial, leading to annoying (although harmless) warning messages on every mercurial command.\n\nSo this bug could be resolved by:\n\n1) tell everybody who cares to add the above lines to their .hgrc\n\n2) patch Sage's mercurial to look in $SAGE_LOCAL/etc/mercurial, and install a default configuration there that enables queues",
    "created_at": "2008-03-05T16:55:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2393",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2393#issuecomment-16104",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Actually, Sage's mercurial does include the queue extension; it's just not enabled by default.

You can enable it by adding these lines to $HOME/.hgrc:

```
[extensions]
# patch queues for mercurial
# add the 'q*' commands
hgext.mq=
```


Debian enables the queue extension (along with many others) for its version of mercurial, using configuration files in /etc/mercurial.  I patched Sage's mercurial spkg to not look in /etc/mercurial, because Debian's configuration enabled extensions that were not included in Sage's mercurial, leading to annoying (although harmless) warning messages on every mercurial command.

So this bug could be resolved by:

1) tell everybody who cares to add the above lines to their .hgrc

2) patch Sage's mercurial to look in $SAGE_LOCAL/etc/mercurial, and install a default configuration there that enables queues



---

archive/issue_comments_016105.json:
```json
{
    "body": "Aha, I had I thought I enabled it in .hgrc, but it turns out it was just in /etc/mercurial.  Thanks!",
    "created_at": "2008-03-05T22:48:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2393",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2393#issuecomment-16105",
    "user": "https://github.com/mwhansen"
}
```

Aha, I had I thought I enabled it in .hgrc, but it turns out it was just in /etc/mercurial.  Thanks!



---

archive/issue_comments_016106.json:
```json
{
    "body": "> 2) patch Sage's mercurial to look in \n> $SAGE_LOCAL/etc/mercurial, and install a default \n> configuration there that enables queues\n\nI like this suggestion, since \"1) tell everybody ...\" is always doomed to failure and frustration.",
    "created_at": "2008-03-05T22:59:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2393",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2393#issuecomment-16106",
    "user": "https://github.com/williamstein"
}
```

> 2) patch Sage's mercurial to look in 
> $SAGE_LOCAL/etc/mercurial, and install a default 
> configuration there that enables queues

I like this suggestion, since "1) tell everybody ..." is always doomed to failure and frustration.



---

archive/issue_comments_016107.json:
```json
{
    "body": "\n```\n[01:39am] mabshoff: mhansen: isn't the que extension now part of hg 1.0.x?\n[01:40am] mabshoff: I.e. we can close #2393 as fixed.\n[01:40am] ddrake: mabshoff: queue is now standard in hg\n[01:40am] mabshoff: excellent\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-10-30T08:45:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2393",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2393#issuecomment-16107",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```


```
[01:39am] mabshoff: mhansen: isn't the que extension now part of hg 1.0.x?
[01:40am] mabshoff: I.e. we can close #2393 as fixed.
[01:40am] ddrake: mabshoff: queue is now standard in hg
[01:40am] mabshoff: excellent
```


Cheers,

Michael



---

archive/issue_comments_016108.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-30T08:45:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2393",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2393#issuecomment-16108",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
