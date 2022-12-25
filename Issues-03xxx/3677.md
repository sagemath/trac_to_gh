# Issue 3677: [with patch, positive review] sage -tp does not take into account the current directory

archive/issues_003677.json:
```json
{
    "body": "Assignee: @garyfurnish\n\nCC:  @mwhansen\n\nAt the end of testing when reporting the results, sage -t does not take into account the current directory.  It produces output like this:\n\n```\nsage -t  devel/sage-combinat/sage/combinat/root_system/ambient_space.py\nsage -t  devel/sage-combinat/sage/combinat/root_system/root_lattice_realization.py\nsage -t  devel/sage-combinat/sage/combinat/root_system/root_space.py\nsage -t  devel/sage-combinat/sage/combinat/root_system/root_system.py\nsage -t  devel/sage-combinat/sage/combinat/root_system/weight_space.py\n```\n\nwhen it should be giving output like \n\n```\nsage -t  ambient_space.py\nsage -t  root_lattice_realization.py\nsage -t  root_space.py\nsage -t  root_system.py\nsage -t  weight_space.py\n```\n\nif I am in $SAGE_ROOT/devel/sage-combinat/sage/combinat/root_system .\n\nIssue created by migration from https://trac.sagemath.org/ticket/3677\n\n",
    "closed_at": "2008-12-14T05:38:18Z",
    "created_at": "2008-07-19T01:48:02Z",
    "labels": [
        "component: misc",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "[with patch, positive review] sage -tp does not take into account the current directory",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3677",
    "user": "https://github.com/mwhansen"
}
```
Assignee: @garyfurnish

CC:  @mwhansen

At the end of testing when reporting the results, sage -t does not take into account the current directory.  It produces output like this:

```
sage -t  devel/sage-combinat/sage/combinat/root_system/ambient_space.py
sage -t  devel/sage-combinat/sage/combinat/root_system/root_lattice_realization.py
sage -t  devel/sage-combinat/sage/combinat/root_system/root_space.py
sage -t  devel/sage-combinat/sage/combinat/root_system/root_system.py
sage -t  devel/sage-combinat/sage/combinat/root_system/weight_space.py
```

when it should be giving output like 

```
sage -t  ambient_space.py
sage -t  root_lattice_realization.py
sage -t  root_space.py
sage -t  root_system.py
sage -t  weight_space.py
```

if I am in $SAGE_ROOT/devel/sage-combinat/sage/combinat/root_system .

Issue created by migration from https://trac.sagemath.org/ticket/3677





---

archive/issue_comments_025984.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-12-11T15:17:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3677",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3677#issuecomment-25984",
    "user": "https://github.com/garyfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_025985.json:
```json
{
    "body": "Attachment [trac_3677_bin.patch](tarball://root/attachments/some-uuid/ticket3677/trac_3677_bin.patch) by @garyfurnish created at 2008-12-11 15:17:28\n\nThis fixes this issue for sage -tp but not for sage -t.",
    "created_at": "2008-12-11T15:17:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3677",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3677#issuecomment-25985",
    "user": "https://github.com/garyfurnish"
}
```

Attachment [trac_3677_bin.patch](tarball://root/attachments/some-uuid/ticket3677/trac_3677_bin.patch) by @garyfurnish created at 2008-12-11 15:17:28

This fixes this issue for sage -tp but not for sage -t.



---

archive/issue_comments_025986.json:
```json
{
    "body": "Is it possible to get this reviewed for 3.2.2?",
    "created_at": "2008-12-14T01:51:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3677",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3677#issuecomment-25986",
    "user": "https://github.com/garyfurnish"
}
```

Is it possible to get this reviewed for 3.2.2?



---

archive/issue_comments_025987.json:
```json
{
    "body": "The \"-t\" case of this has been split to #4790",
    "created_at": "2008-12-14T05:29:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3677",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3677#issuecomment-25987",
    "user": "https://github.com/garyfurnish"
}
```

The "-t" case of this has been split to #4790



---

archive/issue_comments_025988.json:
```json
{
    "body": "Yep, this works Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-14T05:38:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3677",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3677#issuecomment-25988",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Yep, this works Positive review.

Cheers,

Michael



---

archive/issue_events_008419.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-14T05:38:18Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3677",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3677#event-8419"
}
```



---

archive/issue_comments_025989.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-14T05:38:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3677",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3677#issuecomment-25989",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_025990.json:
```json
{
    "body": "Merged in Sage 3.2.2.rc0",
    "created_at": "2008-12-14T05:38:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3677",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3677#issuecomment-25990",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.2.rc0
