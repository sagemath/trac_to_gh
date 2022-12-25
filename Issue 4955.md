# Issue 4955: Magma needs write access to $SAGE_ROOT/data/excode/magma

archive/issues_004955.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: magma\n\nThis was on [sage-devel] (2009-01-08):\n>> RuntimeError: While attempting to compile /usr/local/sage-3.2.3/data/\n>> extcode//magma/latex/latex.m (Data file non-existent):\n>> Can't open lock file /usr/local/sage-3.2.3/data/extcode//magma/latex/\n>> latex.lck for writing (Permission denied)\n\n>>\n>> While attempting to compile /usr/local/sage-3.2.3/data/extcode//magma/\n>> sage/basic.m (Data file non-existent):\n>> Can't open lock file /usr/local/sage-3.2.3/data/extcode//magma/sage/\n>> basic.lck for writing (Permission denied\n\n>\n> It seems like you need write access to extcode (see above) at least for the\n> first time you're running Magma from Sage. IIRC there was some talk about\n> lifting this requirement somehow.\n\n\nThe only idea I have to deal with this is to copy all of extcode/magma\ninto .sage/extcode/magma say, and then have sage only use magma code\nthat's in .sage/extcode/magma/.\nWhenever sage is upgraded, the .sage/extcode/magma would have to get\ndeleted and re-copied, using a facility similar to how the Gap\nworkspace always gets updated when Sage has been upgraded.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4955\n\n",
    "created_at": "2009-01-08T17:15:56Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Magma needs write access to $SAGE_ROOT/data/excode/magma",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4955",
    "user": "https://github.com/malb"
}
```
Assignee: @williamstein

Keywords: magma

This was on [sage-devel] (2009-01-08):
>> RuntimeError: While attempting to compile /usr/local/sage-3.2.3/data/
>> extcode//magma/latex/latex.m (Data file non-existent):
>> Can't open lock file /usr/local/sage-3.2.3/data/extcode//magma/latex/
>> latex.lck for writing (Permission denied)

>>
>> While attempting to compile /usr/local/sage-3.2.3/data/extcode//magma/
>> sage/basic.m (Data file non-existent):
>> Can't open lock file /usr/local/sage-3.2.3/data/extcode//magma/sage/
>> basic.lck for writing (Permission denied

>
> It seems like you need write access to extcode (see above) at least for the
> first time you're running Magma from Sage. IIRC there was some talk about
> lifting this requirement somehow.


The only idea I have to deal with this is to copy all of extcode/magma
into .sage/extcode/magma say, and then have sage only use magma code
that's in .sage/extcode/magma/.
Whenever sage is upgraded, the .sage/extcode/magma would have to get
deleted and re-copied, using a facility similar to how the Gap
workspace always gets updated when Sage has been upgraded.

Issue created by migration from https://trac.sagemath.org/ticket/4955





---

archive/issue_events_011456.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-01-23T07:39:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4955",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4955#event-11456"
}
```



---

archive/issue_comments_037599.json:
```json
{
    "body": "dup of #5041",
    "created_at": "2009-01-23T07:39:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4955#issuecomment-37599",
    "user": "https://github.com/williamstein"
}
```

dup of #5041



---

archive/issue_comments_037600.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-01-23T07:39:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4955#issuecomment-37600",
    "user": "https://github.com/williamstein"
}
```

Resolution: duplicate



---

archive/issue_events_011457.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-23T10:56:25Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4955",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4955#event-11457"
}
```
