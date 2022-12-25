# Issue 676: Solaris 10: fix python build

archive/issues_000676.json:
```json
{
    "body": "Assignee: mabshoff\n\nKeywords: Solaris 10, python\n\nWe need to add\n\n```\n --with-libs='-lrt -laio -lmd -lmp -lscf -lgen -ldoor -lgcc_s -L/lib/ -luutil -ldl -lm -lsocket -lnsl -lxnet'\n```\non Solaris 10 only. It is not needed on Solaris 9.\n\nIssue created by migration from https://trac.sagemath.org/ticket/676\n\n",
    "created_at": "2007-09-17T00:44:11Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.1",
    "title": "Solaris 10: fix python build",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/676",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

Keywords: Solaris 10, python

We need to add

```
 --with-libs='-lrt -laio -lmd -lmp -lscf -lgen -ldoor -lgcc_s -L/lib/ -luutil -ldl -lm -lsocket -lnsl -lxnet'
```
on Solaris 10 only. It is not needed on Solaris 9.

Issue created by migration from https://trac.sagemath.org/ticket/676





---

archive/issue_comments_003492.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-09-17T05:50:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/676#issuecomment-3492",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_003493.json:
```json
{
    "body": "The problem seems to be Solaris 10 on amd64 specific. See \n\nhttp://www.mail-archive.com/openpkg-cvs`@`openpkg.org/msg13989.html\n\nfor a workaround like:\n\n```\nif [ \".`isainfo -k`\" = .amd64 ]; then\n ADD extra configure flags\nfi\n```\n\nCheers,\n\nMichael",
    "created_at": "2007-09-17T15:28:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/676#issuecomment-3493",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The problem seems to be Solaris 10 on amd64 specific. See 

http://www.mail-archive.com/openpkg-cvs`@`openpkg.org/msg13989.html

for a workaround like:

```
if [ ".`isainfo -k`" = .amd64 ]; then
 ADD extra configure flags
fi
```

Cheers,

Michael



---

archive/issue_comments_003494.json:
```json
{
    "body": "This problem also exists on Solaris 10/Sparc. It would be interesting to see if Python 2.5.2 fixes this problem.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-19T12:48:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/676#issuecomment-3494",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This problem also exists on Solaris 10/Sparc. It would be interesting to see if Python 2.5.2 fixes this problem.

Cheers,

Michael



---

archive/issue_events_001800.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-22T02:51:17Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/676",
    "milestone": "sage-2.11",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/676#event-1800"
}
```



---

archive/issue_events_001801.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-27T07:23:11Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/676",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/676#event-1801"
}
```



---

archive/issue_comments_003495.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2008-04-27T07:23:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/676#issuecomment-3495",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: wontfix



---

archive/issue_comments_003496.json:
```json
{
    "body": "This is a non-issue with the Sun Compiler. So close it as won't fix. \n\nCheers,\n\nMicahell",
    "created_at": "2008-04-27T07:23:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/676#issuecomment-3496",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is a non-issue with the Sun Compiler. So close it as won't fix. 

Cheers,

Micahell
