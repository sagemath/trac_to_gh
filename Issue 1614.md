# Issue 1614: cleanup setup.py in sage.spkg

archive/issues_001614.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @craigcitro\n\nWe have a lot of extensions directly listed in the `ext_modules section`. Move those out and also sort the `ext_modules list`\n\nIssue created by migration from https://trac.sagemath.org/ticket/1614\n\n",
    "created_at": "2007-12-28T17:02:27Z",
    "labels": [
        "component: distribution",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "cleanup setup.py in sage.spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1614",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

CC:  @craigcitro

We have a lot of extensions directly listed in the `ext_modules section`. Move those out and also sort the `ext_modules list`

Issue created by migration from https://trac.sagemath.org/ticket/1614





---

archive/issue_comments_010238.json:
```json
{
    "body": "Is there any reason to not list extensions directly in the ext_modules list? This seems far simpler and less error prone. If anything needs to change, I'd move all of them there.",
    "created_at": "2008-01-04T22:31:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1614#issuecomment-10238",
    "user": "https://github.com/robertwb"
}
```

Is there any reason to not list extensions directly in the ext_modules list? This seems far simpler and less error prone. If anything needs to change, I'd move all of them there.



---

archive/issue_comments_010239.json:
```json
{
    "body": "Well, as it it just seems very inconsistent. We can move it either way, it should just be consistent. I have a Cygwin build patch for setup.py that should be applied before anybody else touches setup.py with some major reorg patch. The is needed because the order of libraries matters on Cygwin. That patch is one of the first patches that I plan to merge for 2.10 as I am reluctant to merge it now for 2.9.2.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-04T22:36:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1614#issuecomment-10239",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Well, as it it just seems very inconsistent. We can move it either way, it should just be consistent. I have a Cygwin build patch for setup.py that should be applied before anybody else touches setup.py with some major reorg patch. The is needed because the order of libraries matters on Cygwin. That patch is one of the first patches that I plan to merge for 2.10 as I am reluctant to merge it now for 2.9.2.

Cheers,

Michael



---

archive/issue_comments_010240.json:
```json
{
    "body": "This issue has been fixed via #4480 by Craig Citro.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-13T16:32:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1614#issuecomment-10240",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This issue has been fixed via #4480 by Craig Citro.

Cheers,

Michael



---

archive/issue_comments_010241.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-13T16:32:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1614#issuecomment-10241",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_001773.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-11-13T16:32:39Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1614",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1614#event-1773"
}
```
